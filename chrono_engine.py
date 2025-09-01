import json
import math
from datetime import datetime

def decayweightedscore(lag_seconds, magnitude):
    decay = math.exp(-lag_seconds / 3600)
    return round(magnitude * decay, 4)

def flaganomaly(eventtime, lag_seconds, magnitude, threshold=0.5):
    score = decayweightedscore(lag_seconds, magnitude)
    return {
        "eventtime": eventtime,
        "lagseconds": lagseconds,
        "magnitude": magnitude,
        "score": score,
        "flagged": score >= threshold
    }

def analyze_events(events):
    flagged = []
    for e in events:
        result = flaganomaly(e["eventtime"], e["lag_seconds"], e["magnitude"])
        if result["flagged"]:
            flagged.append(result)
    return flagged

if name == "main":
    with open("dashboard_overlay.json") as f:
        events = json.load(f)
    results = analyze_events(events)
    print(json.dumps(results, indent=2))
