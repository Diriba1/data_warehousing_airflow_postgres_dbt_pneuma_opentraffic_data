import airflow.utils.dates
from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
args = {'owner': 'airflow'}
dag = DAG(
   dag_id="extract_data_and_create_table",
   default_args=args,
   schedule_interval=None,
   start_date=airflow.utils.dates.days_ago(1),
   catchup=False,
)
create_vehicle_table = PostgresOperator(
    task_id="create_table",
    postgres_conn_id="postgres_local_host",
    sql="sql/create_table.sql",
    dag=dag
)
# create_trajectory_table = PostgresOperator(
#     task_id="create_trajectory_table",
#     postgres_conn_id="postgres_local_host",
#     sql="sql/create_table.sql",
#     dag=dag
# )
extract_data = PostgresOperator(
    dag=dag,
    task_id="extract_data",
    sql="sql/upload.sql",
    postgres_conn_id="postgres_local_host",
    
)

create_vehicle_table >> extract_data

# extract_data >> create_trajectory_table
if __name__ == "__main__":
    dag.cli()