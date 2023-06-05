from django.http import JsonResponse
import json
from etl_app.models import ETL_results
from .scripts.bulk_upload_compounds import run_job
import pandas as pd



def trigger_etl(request):
    experiments = ETL_results.objects.order_by('pk').values()
    print(list(experiments))
    # run_job()
    
    data = {"ETL_results": list(experiments)}
    # Trigger your ETL process here
    # etl()
    return JsonResponse({"message": "ETL process started", "data": data})

def get_users(file_path):
    users = {}
    df = pd.read_csv(file_path, sep=',\t')
    for index, row in df.iterrows():
        print(index, row['name'], row['email'], row['signup_date'])
        users[index+1] = { 
            'id': index+1,
            'name': row['name'],
            'email': row['email'],
            'signup_date': row['signup_date'],
        }
    return users

def get_experiments(file_path):
    
    df = pd.read_csv(file_path, sep=',\t')
    experiments_list = [list(row) for index, row in df.iterrows()]
    return experiments_list

def get_compounds(file_path): 
    df = pd.read_csv(file_path, sep=',\t')
    compound = {}
    for i,r in df.iterrows():
        id = r['compound_id']
        name = r['compound_name']
        structure = r['compound_structure']
        compound[id] = {'name':name, 'structure': structure}

    return compound

def etl_job(request):
    user_csv_path = "csv_data/users.csv"
    experiments_csv_path = "csv_data/user_experiments.csv"
    compounds_csv_path = "csv_data/compounds.csv"

    users = get_users(user_csv_path)
    experiments_list = get_experiments(experiments_csv_path)
    compound_map = get_compounds(compounds_csv_path)

    user_experiment_details = {}

    for e in experiments_list:
        user = e[1]
        compounds = e[2]
        time_taken = e[3]
        if user not in user_experiment_details:
            compound_freq = {}
            for c in compounds.split(';'):
                compound_freq[c] = 1

            user_experiment_details[user] = {'freq': 1, 'time_taken': time_taken, 'avg': time_taken, 'compounds':compound_freq, 'most_used_compound': ""}
            #initalize id count
            

        else:
            user_experiment_details[user]['freq'] +=1
            user_experiment_details[user]['time_taken'] += time_taken
            compound_freq = user_experiment_details[user]['compounds']

            # Add up extra compunds used
            for c in compounds.split(';'):
                if c in compound_freq:
                    compound_freq[c] += 1
                else:
                    compound_freq[c] = 1
            
            # Set it back to the user_experiment_details
            user_experiment_details[user]['compounds'] = compound_freq
    
        user_experiment_details[user]['avg'] = user_experiment_details[user]['time_taken'] / user_experiment_details[user]['freq']

    sorted_compunds_list = []
    for k,v in user_experiment_details.items():
        used_compounds = v['compounds']
        sorted_by_compund_freq = sorted(used_compounds.items(), key=lambda x: x[1], reverse=True)
        sorted_compunds_list.append([k,sorted_by_compund_freq[0]])
    
    for item in sorted_compunds_list:
        k, v = item
        compund_id, freq = v
        user_experiment_details[k]['sorted_by_compund_freq_0'] = v
        user_experiment_details[k]['most_used_compound'] = compound_map[int(compund_id)]['name']
    
    new_ETL_result = ETL_results()
    print(user_experiment_details)
    new_ETL_result.payload = user_experiment_details
    new_ETL_result.save()


    return JsonResponse({"message": "ETL stuff", 'users': users, 'experiments_list': experiments_list, 'user_experiment_details':user_experiment_details})






def users(request):
    
    
    return JsonResponse({"message": "ETL process started"})