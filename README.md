# MunchReview

> 🚧 Currently a work in progress! See Roadmap for project progress.

Ever heard of the "3.5-star sweet spot"? The theory, popularized by [Freddie Wong](https://www.tiktok.com/@rocketjump/video/7142660978868489515?lang=en), is that the best "authentic" Chinese restaurants sit around 3.5 stars on Yelp, because their ratings about how good the food is gets dragged down by reviews about service, ambiance, or wait times.

MunchReview tests that idea, then asks the broader question across all types of restaurants: what do reviews reveal about food quality, consistency, and customer experience that a star rating hides?

## Data
- Source: Yelp Open Dataset (JSON). Not included in this repo per Yelp's
  dataset terms. See "Reproducing" below to see how to obtain the dataset.
- Businesses: [150346]
- Reviews: [6990280]
- Restaurants: TBD
- Restaurant reviews: TBD
- Review date range: TBD

## Pipeline (so far)
1. `src/convert_to_parquet.py` — converts raw JSON to Parquet with DuckDB,
   with row-count checks to verify no rows are lost.

## Roadmap
- [x] Raw data conversion + validation
- [ ] Data profiling
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