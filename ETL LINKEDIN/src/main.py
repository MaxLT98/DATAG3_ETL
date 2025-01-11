from prefect import flow
from tasks.task_extract_linkedin import task_extract_linkedin

@flow(name="ETL Prueba")
def main_flow():
    extraccion = task_extract_linkedin()
    print(extraccion)

if __name__ == "__main__":
    main_flow()