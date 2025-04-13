from sqlalchemy.orm import Session

import csv, os
from dotenv import load_dotenv

from application.models.movie import Movie

load_dotenv()
csv_path = os.getenv("CSV_PATH")
print(csv_path)

def load_data(db: Session):
    
    # preventive
    if not csv_path or not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    try:
        # read css
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            # separed by ;
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                # create database object
                db_movie = Movie(
                    year=int(row["year"]),
                    title=row["title"].strip(),
                    studios=row["studios"].strip(),
                    producers=row["producers"].strip(),
                    winner=row["winner"].strip().lower()
                )
                # add object created
                db.add(db_movie)
                # created log 
                print(f"[Seeder] inserted: {row['title']} ({row['year']})")
            # commit in database
            db.commit()
    except Exception as e:
        print(f"[Seeder] Can't loader CSV: {e}")
        db.rollback()
        raise