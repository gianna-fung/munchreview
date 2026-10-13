# generated code (Opus 5.5 Oct 2026)

import os
import duckdb

con = duckdb.connect()
os.makedirs("data/clean", exist_ok=True)

TEXT_COLS = ["name", "address", "city", "state", "postal_code", "categories"]


def clean_business():
    src = "data/processed/business.parquet"
    dst = "data/clean/business.parquet"

    # standardize missing text: empty and whitespace-only strings become NULL
    replacements = ", ".join(f"NULLIF(TRIM({c}), '') AS {c}" for c in TEXT_COLS)
    con.sql(f"""
        COPY (SELECT * REPLACE ({replacements}) FROM '{src}')
        TO '{dst}' (FORMAT PARQUET)
    """)

    # cleaning must not drop rows
    before = con.sql(f"SELECT COUNT(*) FROM '{src}'").fetchone()[0]
    after = con.sql(f"SELECT COUNT(*) FROM '{dst}'").fetchone()[0]
    assert before == after, f"business: row count changed ({before:,} -> {after:,})"

    # report how many nulls each column has after standardizing
    for c in TEXT_COLS:
        nulls = con.sql(f"SELECT COUNT(*) - COUNT({c}) FROM '{dst}'").fetchone()[0]
        print(f"{c:12} nulls after cleaning: {nulls:,}")


clean_business()