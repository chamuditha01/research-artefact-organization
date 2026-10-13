"""
classifiers.py - copied verbatim from the project's claude/classifiers.py
(2026-09-29 version) for the E2 end-to-end evaluation script. Not modified.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

STAGE1_THRESHOLDS = {
    "shape_compactness": 0.36,
    "slope_deg": 4.43,
    "dist_to_prior_loss_m": 212.0,
}


@dataclass
class Stage1Result:
    label: str
    legs_passed: dict
    confidence: str
    evidence_note: str


def stage1_classify(features: dict) -> Stage1Result:
    legs = {
        "shape_compactness": features["shape_compactness"] < STAGE1_THRESHOLDS["shape_compactness"],
        "slope_deg": features["slope_deg"] > STAGE1_THRESHOLDS["slope_deg"],
        "dist_to_prior_loss_m": features["dist_to_prior_loss_m"] > STAGE1_THRESHOLDS["dist_to_prior_loss_m"],
    }
    label = "candidate_natural" if all(legs.values()) else "candidate_human"
    note = f"{sum(legs.values())}/3 legs passed"
    return Stage1Result(label=label, legs_passed=legs, confidence="high", evidence_note=note)


STAGE2_FEATURES = ["trend_nbr_per_day", "wobble_std", "cycle_count_provisional"]


@dataclass
class Stage2Result:
    label: str
    probability_permanent: float
    confidence: str
    evidence_note: str


def _confidence_band(prob_permanent: float) -> str:
    margin = abs(prob_permanent - 0.5)
    if margin >= 0.3:
        return "high"
    if margin >= 0.15:
        return "medium"
    return "low"


class Stage2Classifier:
    def __init__(self):
        self._scaler: Optional[StandardScaler] = None
        self._model: Optional[LogisticRegression] = None
        self._n_train: int = 0

    @classmethod
    def fit_from_labelled_events(cls, rows: list[dict]) -> "Stage2Classifier":
        eligible = [r for r in rows if r["known_class"] in (
            "cultivation", "cultivation_pasture", "permanent_encroachment"
        )]
        X = np.array([[r[f] for f in STAGE2_FEATURES] for r in eligible])
        y = np.array([1 if r["known_class"] == "permanent_encroachment" else 0 for r in eligible])

        clf = cls()
        clf._scaler = StandardScaler().fit(X)
        clf._model = LogisticRegression(max_iter=1000).fit(clf._scaler.transform(X), y)
        clf._n_train = len(eligible)
        return clf

    def classify(self, features: dict) -> Stage2Result:
        x = np.array([[features[f] for f in STAGE2_FEATURES]])
        x_scaled = self._scaler.transform(x)
        prob_permanent = float(self._model.predict_proba(x_scaled)[0][1])
        label = "permanent_encroachment" if prob_permanent >= 0.5 else "cultivation"
        return Stage2Result(
            label=label,
            probability_permanent=prob_permanent,
            confidence=_confidence_band(prob_permanent),
            evidence_note="",
        )
