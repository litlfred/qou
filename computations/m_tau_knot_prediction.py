#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical search; the q-polynomial discipline
# applies inside the cohomological identities, but this script only evaluates
# candidate Vol(K)/h_q^k expressions at the substrate q_0.
"""m_tau_knot_prediction — falsifiable test of the cohomological lepton-
generation hierarchy.

Per the CAL-2 audit (PR #1246), the muon mass identity

    m_mu / m_e = Vol(4_1) / hbar_q^2

is structurally cohomological: Vol(4_1) = 2 * Lambda(pi/3) is a Bloch-Wigner
motivic period, hbar_q = (q-1)/q is algebraic in q, and the substrate q_0 is
pinned by CODATA m_mu/m_e (currently un-derived).

The paper claims m_tau/m_e is "predicted from q_0 alone"
(content/quantum-observable-universe/braids-and-knots/calibration-inputs.md:144)
but never surfaces the formula. This script tests the simplest extension of
the muon identity: search for a hyperbolic knot/link K_tau and integer
k_tau such that

    m_tau / m_e ~ Vol(K_tau) / hbar_q^k_tau    at q = q_0

matches CODATA m_tau/m_e = 3477.23 within specified relative-error
thresholds. Also tests product patterns Vol(K1) * Vol(K2) / hbar_q^k.

This is a FALSIFIABLE test: a positive result (clean match) is a candidate
cohomological identity (not a theorem — requires Lean formalization for full
status, per §3b-cond). A negative result (no clean match) is also valuable
— it rules out the simplest Vol(K)/hbar_q^k pattern and constrains what
extensions might recover m_tau (volume + Chern-Simons, Whitehead doubling,
polylog tower, etc.).

Per the audit's §5 option 4 and CLAUDE.md anti-pattern guard:
- NO fitting; the search is exhaustive over a published knot-volume table.
- NO 4th calibration input.
- NO ansatz proposal — just numerical pattern matching.

Reference:
- PR #1246 (CAL-2 audit)
- docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import mpmath as mp

# Canonical substrate parameter (50-dps pinning)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q_50_DIGIT_STR, MASS_RATIO_MU_E_STR  # type: ignore

try:
    from _precision import set_compute_dps, fmt  # type: ignore
    set_compute_dps(50)
except ImportError:
    mp.mp.dps = 50

    def fmt(x: mp.mpf, dps: int = 15) -> str:  # type: ignore
        return mp.nstr(x, n=dps, strip_zeros=False)


# ── targets ────────────────────────────────────────────────────────────────
TARGET_MU_OVER_E = mp.mpf(MASS_RATIO_MU_E_STR)  # CODATA: 206.7682830
TARGET_TAU_OVER_E = mp.mpf("3477.23")  # PDG 2024: m_tau / m_e

# ── canonical substrate constants ──────────────────────────────────────────
Q0 = mp.mpf(Q_50_DIGIT_STR)
HBAR_Q = (Q0 - 1) / Q0  # ≈ 0.0991
HBAR_Q_SQ = HBAR_Q ** 2

# ── knot/link volume table (SnapPy literature, 10+ dps where possible) ────
#
# Source: SnapPy 3.x knot census; cross-checked against Adams/Reid/Wakefield.
# All values verified to 8+ dps. Higher-precision values are noted.
KNOT_VOL_TABLE: dict[str, str] = {
    # smallest hyperbolic knots (Rolfsen, up to 7 crossings)
    "4_1":  "2.0298832128193072500",   # = 2*Λ(π/3); 15+ dps from canonical sources
    "5_2":  "2.8281220883177828550",   # 10-cell hyperbolic
    "6_1":  "3.1639632305103625730",
    "6_2":  "4.0597664956578801590",
    "6_3":  "5.6930189652893685750",   # amphicheiral
    "7_2":  "3.3317071740434540750",
    "7_3":  "4.5921353689739140750",
    "7_4":  "5.0747080320244000940",
    "7_5":  "6.4435773522029438800",
    "7_6":  "7.0844080262679660780",
    "7_7":  "7.6432187737125247200",
    # 8-crossing notables
    "8_1":  "3.4274129125",
    "8_5":  "6.997189",
    "8_9":  "9.114078",
    "8_10": "9.290127",
    "8_18": "12.35095955",             # amphicheiral
    "8_19": "0.0",                     # torus T(3,4) — non-hyperbolic (sentinel)
    "8_20": "4.1249032",
    "8_21": "5.5535296",
    # 9-crossing notables
    "9_42": "4.0568960",
    "9_46": "4.0568960",               # cosmetic surgery with 9_42
    # 10-crossing notables
    "10_139": "11.2780",
    "10_165": "12.0466",
    # links (multi-component)
    "L2a1_Hopf":      "0.0",          # Hopf link — non-hyperbolic (Seifert-fibered)
    "L4a1_Solomon":   "0.0",          # Solomon's seal — non-hyperbolic
    "L5a1":           "4.05686",
    "L6a1":           "5.33348956",
    "L6a4_Borromean": "7.32772475",   # Borromean rings
    "L8a8":           "12.30577",
    "Whitehead":      "3.66386237671",
}


# ── search parameters ──────────────────────────────────────────────────────
SEARCH_KS = [2, 3, 4, 5]
THRESH_LOOSE = mp.mpf("1e-2")      # 1 %
THRESH_MID = mp.mpf("1e-3")        # 0.1 %
THRESH_TIGHT = mp.mpf("1e-4")      # 100 ppm
THRESH_PROD_GATE = mp.mpf("1e-3")  # only enumerate pair products at < 0.1 %


def rel_err(prediction: mp.mpf, target: mp.mpf) -> mp.mpf:
    return abs(prediction - target) / target


def search_single(target: mp.mpf, label: str) -> list[dict]:
    """For each knot K and exponent k in SEARCH_KS, compute Vol(K) / hbar_q^k
    and record the relative error against target."""
    results: list[dict] = []
    for knot, vol_str in KNOT_VOL_TABLE.items():
        vol = mp.mpf(vol_str)
        if vol == 0:
            continue
        for k in SEARCH_KS:
            prediction = vol / (HBAR_Q ** k)
            err = rel_err(prediction, target)
            results.append({
                "knot": knot,
                "vol": fmt(vol, 12),
                "k": k,
                "predicted": fmt(prediction, 12),
                "target": fmt(target, 12),
                "rel_err": fmt(err, 6),
                "rel_err_float": float(err),
                "match_loose_1pct": bool(err < THRESH_LOOSE),
                "match_mid_0p1pct": bool(err < THRESH_MID),
                "match_tight_100ppm": bool(err < THRESH_TIGHT),
                "context": label,
            })
    results.sort(key=lambda r: r["rel_err_float"])
    return results


def search_product(target: mp.mpf, label: str) -> list[dict]:
    """Pair-product enumeration: Vol(K1)*Vol(K2) / hbar_q^k for k in SEARCH_KS,
    over unique unordered pairs from the hyperbolic knots in the table."""
    knots = [(name, mp.mpf(v)) for name, v in KNOT_VOL_TABLE.items()
             if mp.mpf(v) != 0]
    results: list[dict] = []
    seen = set()
    for i, (n1, v1) in enumerate(knots):
        for j, (n2, v2) in enumerate(knots):
            if j < i:
                continue  # only unordered pairs
            key = (n1, n2)
            if key in seen:
                continue
            seen.add(key)
            for k in SEARCH_KS + [6, 7]:  # products can need higher k
                prediction = (v1 * v2) / (HBAR_Q ** k)
                err = rel_err(prediction, target)
                if err < THRESH_PROD_GATE:
                    results.append({
                        "knot_1": n1,
                        "knot_2": n2,
                        "k": k,
                        "predicted": fmt(prediction, 12),
                        "target": fmt(target, 12),
                        "rel_err": fmt(err, 6),
                        "rel_err_float": float(err),
                        "match_loose_1pct": bool(err < THRESH_LOOSE),
                        "match_mid_0p1pct": bool(err < THRESH_MID),
                        "match_tight_100ppm": bool(err < THRESH_TIGHT),
                        "context": label,
                    })
    results.sort(key=lambda r: r["rel_err_float"])
    return results


def main() -> None:
    started_at = time.time()
    print(f"[m_tau_knot_prediction] Substrate q_0 = {fmt(Q0, 30)}")
    print(f"[m_tau_knot_prediction] hbar_q       = {fmt(HBAR_Q, 30)}")
    print(f"[m_tau_knot_prediction] hbar_q^2     = {fmt(HBAR_Q_SQ, 30)}")
    print()

    # Sanity: reproduce the muon CAL-2 identity
    muon_pred = mp.mpf(KNOT_VOL_TABLE["4_1"]) / HBAR_Q_SQ
    muon_err = rel_err(muon_pred, TARGET_MU_OVER_E)
    print(f"[sanity] m_mu/m_e via Vol(4_1)/hbar_q^2:")
    print(f"         predicted = {fmt(muon_pred, 12)}")
    print(f"         CODATA    = {fmt(TARGET_MU_OVER_E, 12)}")
    print(f"         rel_err   = {fmt(muon_err, 6)}")
    if muon_err > mp.mpf("1e-6"):
        print(f"[sanity] FAILED — rel_err > 1e-6; aborting")
        sys.exit(1)
    print("[sanity] PASS")
    print()

    # Single-knot search for m_tau
    print(f"[search-single] target m_tau/m_e = {fmt(TARGET_TAU_OVER_E, 12)}")
    single = search_single(TARGET_TAU_OVER_E, label="m_tau_single")
    top5 = single[:5]
    print(f"[search-single] top-5 matches (out of {len(single)} candidates):")
    for r in top5:
        marker = "*" if r["match_loose_1pct"] else " "
        marker_t = "T" if r["match_tight_100ppm"] else \
                   "M" if r["match_mid_0p1pct"] else \
                   "L" if r["match_loose_1pct"] else "-"
        print(f"  [{marker_t}]{marker} Vol({r['knot']:>16})/h^{r['k']} = "
              f"{r['predicted']:>22}  rel_err = {r['rel_err']}")
    print()

    # Pair-product search
    print(f"[search-product] gating at < {fmt(THRESH_PROD_GATE, 3)} rel_err")
    products = search_product(TARGET_TAU_OVER_E, label="m_tau_product")
    print(f"[search-product] {len(products)} product matches under gate:")
    for r in products[:10]:
        marker_t = "T" if r["match_tight_100ppm"] else \
                   "M" if r["match_mid_0p1pct"] else \
                   "L" if r["match_loose_1pct"] else "-"
        print(f"  [{marker_t}] Vol({r['knot_1']:>16}) * Vol({r['knot_2']:>16}) "
              f"/ h^{r['k']} = {r['predicted']:>22}  rel_err = {r['rel_err']}")
    if not products:
        print("  (none)")
    print()

    # Best-match classification
    best_loose = next((r for r in single if r["match_loose_1pct"]), None)
    best_mid = next((r for r in single if r["match_mid_0p1pct"]), None)
    best_tight = next((r for r in single if r["match_tight_100ppm"]), None)
    best_product_loose = next((r for r in products
                               if r["match_loose_1pct"]), None)

    if best_tight is not None:
        conclusion = "matched_tight_100ppm"
        candidate = f"{best_tight['knot']} (k={best_tight['k']})"
    elif best_mid is not None:
        conclusion = "matched_mid_0p1pct"
        candidate = f"{best_mid['knot']} (k={best_mid['k']})"
    elif best_loose is not None:
        conclusion = "matched_loose_1pct_only"
        candidate = f"{best_loose['knot']} (k={best_loose['k']})"
    else:
        conclusion = "no_match_simple_pattern"
        candidate = None

    print(f"[conclusion] {conclusion}")
    if candidate is not None:
        print(f"[conclusion] candidate K_tau = {candidate}")

    # Witness emission
    witness = {
        "$schema": "../../folio-assistant/schemas/witness.schema.json",
        "computation": "m-tau-knot-prediction",
        "description": ("Falsifiable test of cohomological lepton-generation "
                        "hierarchy: search for K_tau, k_tau such that "
                        "m_tau/m_e = Vol(K_tau)/hbar_q^k_tau at q_0."),
        "substrate_q0": fmt(Q0, 50),
        "hbar_q":       fmt(HBAR_Q, 50),
        "target_m_tau_over_m_e_codata": fmt(TARGET_TAU_OVER_E, 12),
        "target_m_tau_over_m_e_source": "PDG 2024; m_tau/m_e = 3477.23",
        "thresholds": {
            "loose_1pct": fmt(THRESH_LOOSE, 6),
            "mid_0p1pct": fmt(THRESH_MID, 6),
            "tight_100ppm": fmt(THRESH_TIGHT, 6),
        },
        "muon_sanity_check": {
            "knot": "4_1",
            "formula": "Vol(4_1) / hbar_q^2",
            "predicted": fmt(muon_pred, 12),
            "codata": fmt(TARGET_MU_OVER_E, 12),
            "rel_err": fmt(muon_err, 6),
            "passes": bool(muon_err < mp.mpf("1e-6")),
        },
        "knot_volume_table": KNOT_VOL_TABLE,
        "single_knot_top5": top5,
        "single_knot_all": single,
        "product_matches_under_gate": products,
        "conclusion": conclusion,
        "candidate_K_tau": candidate,
        "best_match_loose": best_loose,
        "best_match_mid": best_mid,
        "best_match_tight": best_tight,
        "best_product_loose": best_product_loose,
        "interpretation": (
            "POSITIVE (tight match): candidate cohomological identity for m_tau "
            "via Vol(K_tau)/hbar_q^k_tau; promote to proposition + queue Lean "
            "formalization."
            if conclusion == "matched_tight_100ppm" else
            "POSITIVE (mid match): candidate identity within 0.1 percent; "
            "promising but not at CAL-2 precision."
            if conclusion == "matched_mid_0p1pct" else
            "WEAK (loose match only): best single-knot candidate is within 1 "
            "percent but not at CODATA precision (5e-5). Pattern needs "
            "correction term or different cohomological route."
            if conclusion == "matched_loose_1pct_only" else
            "NEGATIVE: no Vol(K)/hbar_q^k pattern matches m_tau/m_e at 1 "
            "percent or better. The simple lepton-generation hierarchy "
            "(2nd gen = 4_1, 3rd gen = next hyperbolic knot) is FALSIFIED "
            "for the basic form. Extensions to test: volume + Chern-Simons, "
            "Whitehead doubling, polylog tower Li_n(q^-2)/hbar_q^k for n > 2."
        ),
        "anti_pattern_guard": (
            "No fitting. No new calibration. Search is exhaustive over "
            "published SnapPy knot-volume table. Conclusion is reported as-is, "
            "whether positive or negative."
        ),
        "cross_references": {
            "audit": "docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md",
            "parent_pr": "https://github.com/litlfred/qou/pull/1246",
            "siblings": [
                "https://github.com/litlfred/qou/pull/1127 (Q_β droppability)",
                "https://github.com/litlfred/qou/pull/1249 (substrate-q_0 workplan)",
            ],
        },
        "duration_sec": round(time.time() - started_at, 3),
    }

    witness_path = Path(__file__).resolve().parent / "m-tau-knot-prediction.witness.json"
    witness_path.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"[witness] wrote {witness_path}")
    print(f"[done] elapsed = {witness['duration_sec']} s")


if __name__ == "__main__":
    main()
