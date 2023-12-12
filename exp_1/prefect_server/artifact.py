from prefect import flow, task
from prefect.artifacts import create_link_artifact, create_markdown_artifact


@task
def my_first_task():
    create_link_artifact(
        key="irregular-data",
        link="https://nyc3.digitaloceanspaces.com/my-bucket-name/highly_variable_data.csv",
        description="## Highly variable data",
    )


@task
def my_second_task():
    create_link_artifact(
        key="irregular-data",
        link="https://nyc3.digitaloceanspaces.com/my-bucket-name/low_pred_data.csv",
        description="# Low prediction accuracy",
    )


@task
def markdown_task():
    na_revenue = 500000
    markdown_report = f"""# Sales Report

In the past quarter, our company saw a significant increase in sales, with a total revenue of $1,000,000. 
This represents a 20% increase over the same period last year.

## Sales by Region

| Region        | Revenue |
|:--------------|-------:|
| North America | ${na_revenue:,} |
| Europe        | $250,000 |
| Asia          | $150,000 |
| South America | $75,000 |
| Africa        | $25,000 |

## Top Products

1. Product A - $300,000 in revenue
2. Product B - $200,000 in revenue
3. Product C - $150,000 in revenue

## Conclusion

Overall, these results are very encouraging and demonstrate the success of our sales team in increasing revenue 
across all regions. However, we still have room for improvement and should focus on further increasing sales in 
the coming quarter.
"""
    create_markdown_artifact(
        key="gtm-report",
        markdown=markdown_report,
        description="Quarterly Sales Report",
    )


@flow
def my_flow():
    my_first_task()
    my_second_task()
    markdown_task()


if __name__ == "__main__":
    my_flow()
