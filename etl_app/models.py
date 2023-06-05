from django.db import models


class ETL_results(models.Model):
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class Compound(models.Model):
    compound_id = models.IntegerField(primary_key=True)
    compound_name = models.CharField(max_length=255)
    compound_structure = models.CharField(max_length=255)

    def __str__(self):
        return f"Compound {self.compound_name}"

class Experiment(models.Model):
    experiment_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    experiment_compound_ids = models.CharField(max_length=255)
    experiment_run_time = models.IntegerField()

    def __str__(self):
        return f"Experiment {self.experiment_id}"

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    signup_date = models.DateField()

    def __str__(self):
        return f"User: {self.name}"
