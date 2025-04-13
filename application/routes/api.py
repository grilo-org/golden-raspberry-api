from fastapi import APIRouter, Depends
from application.controllers import movie

router = APIRouter()

@router.get("/producers/intervals", tags=["Producers"])
def get_producer_intervals(db=Depends(movie.init)):
    return movie.getProducerIntervals(db)

@router.get("/producers/intervals/min", tags=["Producers"])
def get_producer_intervals_min(db=Depends(movie.init)):
    return movie.getProducerIntervalsMin(db)

@router.get("/producers/intervals/max", tags=["Producers"])
def get_producer_intervals_max(db=Depends(movie.init)):
    return movie.getProducerIntervalsMax(db)