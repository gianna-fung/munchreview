import duckdb

con = duckdb.connect()

def convert(name):
    json_path = f"data/raw/yelp_academic_dataset_{name}.json"
    parquet_path = f"data/processed/{name}.parquet"

    json_count = con.sql(f"SELECT COUNT(*) FROM read_json_auto('{json_path}')").fetchone()[0] #count rows in json

    con.sql(f"""
        COPY (SELECT * FROM read_json_auto('{json_path}'))
        TO '{parquet_path}' (FORMAT PARQUET)
    """)

    parquet_count = con.sql(                    #count rows in converted parquet
        f"SELECT COUNT(*) FROM '{parquet_path}'"
    ).fetchone()[0]  

    # check if row counts match
    assert json_count == parquet_count, (f"{name}: row counts don't match (JSON {json_count:,} vs Parquet {parquet_count:,})")
    print(f"{name}: {parquet_count:,} rows converted, counts match")

convert("business")
convert("review")