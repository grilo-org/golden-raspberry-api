from collections import defaultdict

import re

def producerIntervals(winners):
    producer_map = defaultdict(list)

    for movie in winners:
        for producer in re.split(r',| and ', movie.producers):
            producer_map[producer.strip()].append(movie.year)

    interval_results = []

    for producer, years in producer_map.items():
        years = sorted(years)
        if len(years) < 2:
            continue
        for i in range(len(years) - 1):
            interval_results.append({
                "producer": producer,
                "interval": years[i + 1] - years[i],
                "previousWin": years[i],
                "followingWin": years[i + 1]
            })

    return interval_results