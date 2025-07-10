import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/varun19424/mini-mlops-project.mlflow")
dagshub.init(repo_owner='varun19424', repo_name='mini-mlops-project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)