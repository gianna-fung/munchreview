# MunchReview

> 🚧 Currently a work in progress! See Roadmap for project progress.

Have you heard of the "3.5-star sweet spot"? This theory, popularized by [Freddie Wong](https://www.tiktok.com/@rocketjump/video/7142660978868489515), is that the best "authentic" Chinese restaurants sit around 3.5 stars on Yelp, because the actually good food spots get their ratings dragged down by reviews about service, ambiance, or wait times.

MunchReview tests that idea, then asks the broader question across 4.7 million Yelp restaurant reviews: what do reviews reveal about food quality, consistency, and customer experience that a star rating hides?

## Data
- Source: Yelp Open Dataset (JSON). Not included in this repo per Yelp's
  dataset terms. See "Reproducing" below for how to obtain the dataset.
- Businesses: 150,346
- Reviews: 6,990,280
- Restaurants: 52,268
- Restaurant reviews: 4,724,471
- Review date range: Feb 2005 - Jan 2022

## Pipeline (so far)
1. `src/convert_to_parquet.py` — converts raw JSON to Parquet with DuckDB,
   with row-count checks to verify no rows are lost.
2. `notebooks/01_profiling.ipynb` — measures the raw data before any changes:
   restaurant scope, missing values, and other data-quality issues.
3. `src/clean.py` — standardizes missing text values (empty and
   whitespace-only strings) to null. Null counts after cleaning are checked
   against the profiling counts.

## Roadmap
- [x] Raw data conversion + validation
- [ ] Data profiling 🚧 (in progress)
- [ ] Restaurant chain name normalization / entity resolution
- [ ] Topic-level sentiment (food, service, price, wait, cleanliness)
- [ ] Food quality vs. star rating gap
- [ ] Cross-location consistency (with Bayesian shrinkage)
- [ ] Trends over time + closure analysis
- [ ] Chain scorecard + chain profiles

## Reproducing
1. Download the Yelp Open Dataset (JSON) from yelp.com/dataset.
2. Extract the JSON files into `data/raw/`.
3. `pip install -r requirements.txt`
4. `python src/convert_to_parquet.py`
5. `python src/clean.py`