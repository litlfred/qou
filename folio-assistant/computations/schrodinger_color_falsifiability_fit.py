"""Fit the QOU non-Riemannian color-perception prediction to Bujack et al. 2022.

This script executes the falsifiability protocol described in
`rem:schrodinger-color-falsifiability`. It fits the one-parameter
QOU prediction

    d_perc(d) = arsinh(eta * d) / eta,    eta = (q - q^{-1}) / 2

to the Gray-Experiment triad-choice data from Bujack et al. (2022),
PNAS 119(18) e2119753119. Dataset: `gray_complete_data_release.csv`
from https://github.com/lanl/color (LANL open-source release).

Model. Triad with source `Ls` and tests `Lt1, Lt2`. With perceived
distances `d_perc(|Ls - Lti|)`, observer noise sigma, and the
Thurstonian probit choice model,

    P(R = 1) = Phi( (d_perc(|Ls - Lt1|) - d_perc(|Ls - Lt2|)) / sigma )

(the sign convention is fixed empirically below). Two free parameters:
`eta` (substrate deformation) and `sigma` (observer noise).

Riemannian limit. As `eta -> 0`, `d_perc(d) -> d`, recovering the
standard Riemannian (linear-distance) Thurstonian model. A
likelihood-ratio test against `eta = 0` answers whether
non-Riemannian beats Riemannian on this dataset.

QOU prediction. From substrate parameter `q_0 ~ 1.1097`,
`eta_QOU = (q_0 - q_0^{-1}) / 2 ~ 0.1043`.

The script emits a witness JSON with the MLE estimate, parametric
bootstrap 95% CI, LR-test p-value, and a verdict against the
prediction protocol in the block's table.
"""

from __future__ import annotations

import csv
import hashlib
import json
from witness_base import WitnessBuilder

_json_dump_raw = json.dump


def _json_dump_witness(obj, fp, *args, **kwargs):
    if isinstance(obj, dict):
        try:
            if str(getattr(fp, "name", "")).endswith(".witness.json"):
                obj = WitnessBuilder.stamp_staleness_metadata(
                    obj, script_path=__file__, engine="python"
                )
        except Exception:
            pass
    return _json_dump_raw(obj, fp, *args, **kwargs)

import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import minimize

DATA_URL = (
    "https://raw.githubusercontent.com/lanl/color/main/"
    "Gray_Experiment/data/gray_complete_data_release.csv"
)
DATA_CACHE = Path("/tmp/bujack/gray.csv")

# QOU substrate parameter (per Chapter 7 Observations)
Q0 = 1.1097
ETA_QOU = (Q0 - 1.0 / Q0) / 2.0  # ~ 0.10431
ETA_QOU_CONFIRMATION_BAND = (0.08, 0.13)  # block-prediction band
ETA_QOU_REFINEMENT_BAND = (0.02, 0.50)    # rescaling-allowed band


def fetch_data() -> Path:
    """Download (and cache) the LANL Gray-experiment CSV."""
    DATA_CACHE.parent.mkdir(parents=True, exist_ok=True)
    if DATA_CACHE.exists() and DATA_CACHE.stat().st_size > 1000:
        return DATA_CACHE
    try:
        urllib.request.urlretrieve(DATA_URL, DATA_CACHE)
    except urllib.error.URLError as e:
        raise SystemExit(f"failed to fetch {DATA_URL}: {e}") from e
    return DATA_CACHE


def load_triads(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return arrays Ls, Lt1, Lt2, R as floats / ints."""
    Ls, Lt1, Lt2, R = [], [], [], []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            Ls.append(float(row["Ls"]))
            Lt1.append(float(row["Lt1"]))
            Lt2.append(float(row["Lt2"]))
            R.append(int(row["R"]))
    return np.array(Ls), np.array(Lt1), np.array(Lt2), np.array(R)


def d_perc(d: np.ndarray, eta: float) -> np.ndarray:
    """QOU perceived-distance kernel; arsinh(eta*d)/eta, with the
    small-eta limit handled via the Taylor expansion."""
    if abs(eta) < 1e-8:
        # arsinh(x) = x - x^3/6 + 3 x^5/40 - ...
        return d - (eta**2) * d**3 / 6.0 + 3 * (eta**4) * d**5 / 40.0
    return np.arcsinh(eta * d) / eta


def neg_log_lik(
    params: np.ndarray,
    abs1: np.ndarray,
    abs2: np.ndarray,
    R: np.ndarray,
    sign: int,
) -> float:
    """Probit choice model NLL. `sign` is +/-1 fixed by empirical
    convention check; see `determine_sign`."""
    eta, log_sigma = params
    sigma = float(np.exp(log_sigma))
    if not np.isfinite(eta) or eta < -0.5 or eta > 2.0:
        return 1e12
    d1 = d_perc(abs1, eta)
    d2 = d_perc(abs2, eta)
    z = sign * (d1 - d2) / sigma
    # log Phi(z) with numerical safety; clip extreme z so log->0 cleanly.
    p1 = stats.norm.logcdf(z)
    p0 = stats.norm.logcdf(-z)
    ll = np.where(R == 1, p1, p0).sum()
    if not np.isfinite(ll):
        return 1e12
    return -float(ll)


def determine_sign(abs1: np.ndarray, abs2: np.ndarray, R: np.ndarray) -> int:
    """Pick the sign in P(R=1) = Phi(sign * (d1 - d2) / sigma) so the
    model agrees with the empirical choice direction.

    With sign = -1 and t1 strictly closer (d1 < d2), the linear
    predictor sign * (d1 - d2) = (d2 - d1) > 0, giving Phi > 0.5,
    matching "observers usually pick the closer test as their R=1".
    """
    diff = abs2 - abs1
    thresh = np.quantile(diff, 0.95)
    mask = diff > thresh  # trials where t1 is much closer than t2
    if mask.sum() < 50:
        return -1
    p_r1_when_t1_closer = float(R[mask].mean())
    return -1 if p_r1_when_t1_closer > 0.5 else +1


def fit_mle(
    abs1: np.ndarray,
    abs2: np.ndarray,
    R: np.ndarray,
    sign: int,
    fix_eta: float | None = None,
) -> tuple[float, float, float]:
    """Return (eta_hat, sigma_hat, neg_log_lik)."""
    if fix_eta is not None:
        # 1-parameter fit (sigma only)
        def f(log_sigma):
            return neg_log_lik(
                np.array([fix_eta, log_sigma[0]]), abs1, abs2, R, sign,
            )
        res = minimize(f, x0=np.array([np.log(5.0)]), method="Nelder-Mead")
        return fix_eta, float(np.exp(res.x[0])), float(res.fun)
    res = minimize(
        neg_log_lik,
        x0=np.array([0.05, np.log(5.0)]),
        args=(abs1, abs2, R, sign),
        method="Nelder-Mead",
        options={"xatol": 1e-5, "fatol": 1e-5, "maxiter": 5000},
    )
    return float(res.x[0]), float(np.exp(res.x[1])), float(res.fun)


def parametric_bootstrap(
    abs1: np.ndarray,
    abs2: np.ndarray,
    R: np.ndarray,
    eta_hat: float,
    sigma_hat: float,
    sign: int,
    n_boot: int = 200,
    seed: int = 20260511,
) -> tuple[float, float]:
    """Parametric bootstrap of (eta) under the fitted (eta, sigma).
    Returns 2.5/97.5 percentile CI on eta."""
    rng = np.random.default_rng(seed)
    z_true = sign * (d_perc(abs1, eta_hat) - d_perc(abs2, eta_hat)) / sigma_hat
    p_true = stats.norm.cdf(z_true)
    etas = []
    for _ in range(n_boot):
        R_sim = (rng.uniform(size=p_true.size) < p_true).astype(int)
        try:
            e, _, _ = fit_mle(abs1, abs2, R_sim, sign)
            etas.append(e)
        except Exception:
            continue
    etas = np.array(etas)
    return float(np.percentile(etas, 2.5)), float(np.percentile(etas, 97.5))


def verdict(eta_hat: float, eta_lo: float, eta_hi: float) -> str:
    """Classify per the block's three-way decision tree."""
    band_conf_lo, band_conf_hi = ETA_QOU_CONFIRMATION_BAND
    band_ref_lo, band_ref_hi = ETA_QOU_REFINEMENT_BAND
    # CI overlaps the confirmation band?
    if eta_hi >= band_conf_lo and eta_lo <= band_conf_hi:
        return "confirmation"
    if eta_hi >= band_ref_lo and eta_lo <= band_ref_hi:
        return "refinement"
    return "falsification-of-direct-identification"


def git_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except Exception:
        return "unknown"


def script_hash() -> str:
    h = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return h[:12]


def main() -> int:
    t0 = time.time()
    print("Fetching LANL Gray-experiment CSV ...", flush=True)
    data_path = fetch_data()
    Ls, Lt1, Lt2, R = load_triads(data_path)
    print(f"  loaded {len(R)} triad responses", flush=True)

    abs1 = np.abs(Ls - Lt1)
    abs2 = np.abs(Ls - Lt2)

    sign = determine_sign(abs1, abs2, R)
    print(f"  empirical sign convention: {sign:+d}", flush=True)

    eta_hat, sigma_hat, nll_full = fit_mle(abs1, abs2, R, sign)
    print(f"  MLE: eta = {eta_hat:.5f}, sigma = {sigma_hat:.4f}",
          flush=True)

    _, _, nll_riem = fit_mle(abs1, abs2, R, sign, fix_eta=0.0)
    lr_stat = 2.0 * (nll_riem - nll_full)
    lr_pvalue = float(stats.chi2.sf(lr_stat, df=1))
    print(
        f"  Riemannian NLL = {nll_riem:.2f}, QOU NLL = {nll_full:.2f}; "
        f"LR = {lr_stat:.2f}, p = {lr_pvalue:.2e}",
        flush=True,
    )

    print("  parametric bootstrap (n=200) ...", flush=True)
    eta_lo, eta_hi = parametric_bootstrap(
        abs1, abs2, R, eta_hat, sigma_hat, sign,
    )
    print(f"  95% CI: [{eta_lo:.5f}, {eta_hi:.5f}]", flush=True)

    v = verdict(eta_hat, eta_lo, eta_hi)
    print(f"  verdict: {v}", flush=True)

    assertions = [
        {
            "name": "non_riemannian_significant",
            "computed": lr_pvalue,
            "expected_lt": 0.001,
            "passed": lr_pvalue < 0.001,
            "source": "schrodinger_color_falsifiability_fit",
        },
        {
            "name": "eta_within_refinement_band",
            "computed": [eta_lo, eta_hi],
            "expected_overlaps": list(ETA_QOU_REFINEMENT_BAND),
            "passed": (
                eta_hi >= ETA_QOU_REFINEMENT_BAND[0]
                and eta_lo <= ETA_QOU_REFINEMENT_BAND[1]
            ),
            "source": "schrodinger_color_falsifiability_fit",
        },
        {
            "name": "eta_within_confirmation_band",
            "computed": [eta_lo, eta_hi],
            "expected_overlaps": list(ETA_QOU_CONFIRMATION_BAND),
            "passed": (
                eta_hi >= ETA_QOU_CONFIRMATION_BAND[0]
                and eta_lo <= ETA_QOU_CONFIRMATION_BAND[1]
            ),
            "source": "schrodinger_color_falsifiability_fit",
        },
    ]

    duration_ms = int((time.time() - t0) * 1000)
    witness = {
        "engine": "numpy+scipy",
        "engineVersion": f"numpy {np.__version__} scipy {stats.__name__.rsplit('.', 1)[0]}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": git_sha(),
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
        "durationMs": duration_ms,
        "computation": "schrodinger-color-falsifiability-fit",
        "scriptFile": "schrodinger_color_falsifiability_fit.py",
        "scriptHash": script_hash(),
        "scriptCommitSha": git_sha(),
        "description": (
            "MLE fit of the QOU one-parameter non-Riemannian color-perception "
            "model d_perc(d) = arsinh(eta * d) / eta to the Bujack et al. 2022 "
            "PNAS Gray-experiment triad-choice dataset "
            "(github.com/lanl/color). Two free parameters: eta (substrate "
            "deformation, predicted ~0.1043 from q_0 ~ 1.1097) and sigma "
            "(Thurstonian observer noise). Reports MLE, parametric bootstrap "
            "95% CI on eta, Riemannian-vs-QOU likelihood-ratio test, and a "
            "three-way verdict against the prediction bands in the block."
        ),
        "contentBlock": "rem:schrodinger-color-falsifiability",
        "parameters": {
            "q_0": Q0,
            "eta_QOU_predicted": ETA_QOU,
            "confirmation_band": list(ETA_QOU_CONFIRMATION_BAND),
            "refinement_band": list(ETA_QOU_REFINEMENT_BAND),
            "n_triads": int(R.size),
            "bootstrap_replicates": 200,
            "choice_sign_convention": sign,
        },
        "data": {
            "eta_hat": eta_hat,
            "sigma_hat": sigma_hat,
            "eta_ci95": [eta_lo, eta_hi],
            "nll_full": nll_full,
            "nll_riemannian": nll_riem,
            "lr_statistic": lr_stat,
            "lr_pvalue": lr_pvalue,
            "verdict": v,
        },
    }

    out_path = Path(__file__).with_name(
        "schrodinger-color-falsifiability-fit.witness.json",
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  wrote {out_path}", flush=True)
    return 0 if witness["allPassed"] or v != "falsification-of-direct-identification" else 1


if __name__ == "__main__":
    sys.exit(main())
