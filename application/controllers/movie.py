from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# application
from application.database.sqlite import init
from application.models.movie import Movie
from application.helpers.producerInterval import producerIntervals

##############################################################
# I comented only first method
##############################################################

#  List producer intervals max and min
def getProducerIntervals(db: Session = Depends(init)):

    # get all movies that won
    winners = db.query(Movie).filter(Movie.winner == "yes").all()

    # if not found movie return 404
    if not winners:
        raise HTTPException(status_code=404, detail="Nenhum vencedor encontrado no banco.")
    
    # create empty list
    results = producerIntervals(winners)
    if not results:
        return {"min": [], "max": []}

    # get minimum value
    min_interval = min(results, key=lambda x: x["interval"])["interval"]

    # get maximun value
    max_interval = max(results, key=lambda x: x["interval"])["interval"]

    # filter in map "interval_results" who have the max and min resulto
    return {
        "min": [r for r in results if r["interval"] == min_interval],
        "max": [r for r in results if r["interval"] == max_interval]
    }

#  List producer min
def getProducerIntervalsMax(db: Session = Depends(init)):
    winners = db.query(Movie).filter(Movie.winner == "yes").all()
    if not winners:
        raise HTTPException(status_code=404, detail="Nenhum vencedor encontrado no banco.")
    
    results = producerIntervals(winners)
    if not results:
        return {"min": [], "max": []}

    intervalMin = min(results, key=lambda x: x["interval"])["interval"]
    return [r for r in results if r["interval"] == intervalMin]

#  List producer min
def getProducerIntervalsMin(db: Session = Depends(init)):
   
    winners = db.query(Movie).filter(Movie.winner == "yes").all()
    if not winners:
        raise HTTPException(status_code=404, detail="Nenhum vencedor encontrado no banco.")
    
    results = producerIntervals(winners)
    if not results:
        return {"min": [], "max": []}

    intervalMax = max(results, key=lambda x: x["interval"])["interval"]
    return [r for r in results if r["interval"] == intervalMax]
