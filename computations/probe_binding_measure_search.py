#!/usr/bin/env python3
"""EXPLORATORY shape-probe — search for the per-block BINDING measure w_λ^bind.

Prior probes established: the per-block q-Reeb phase θ_λ = arccos(χ^λ/d_λ) ∈ ℂ
is the right CARRIER (differences close to +8% with no fit), but the Markov
trace measure y_λ is the WRONG measure for ABSOLUTE binding — Σ y_λ|Δθ_λ|
ANTI-correlates with A because y_λ suppresses the growth channels (|χ/d|>1)
where the extensive binding lives (2026-06-02-full-theta-binding-probe.md).

This probe searches for a parameter-free, structurally-motivated per-block
weight w_λ^bind (≠ y_λ) such that

    B(K) = E · Σ_λ w_λ^bind · |Δθ_λ|      (Δθ_λ = arccos-complex, atom − free)

tracks the extensive A-growth (D 2.22 → ⁴He 28.30 MeV, ~13×). Candidate weights
(all functions of λ alone, NO fit to binding):
  y_lambda      — the trace measure (baseline; known to anti-correlate)
  dim_classical — d_λ = # SYT (grows with block)
  dim_q         — quantum dimension via q-hook-length (grows; the natural
                  Plancherel-conjugate weight)
  abs_content   — Σ_cells |j−i|  (emphasises long rows/cols = growth reps)
  inv_y         — 1/y_λ           (directly emphasises what y_λ suppresses)
  bar_y         — y_λ(q→q⁻¹)      (bar-conjugate measure)

Reports worst |err| (1 global scale) + the T/³He difference for each weight.
EXPLORATORY (production-vs-exploratory-discipline): asserts the refutation;
a positive (some structural weight closes all four) is surfaced for promotion
review + a categorical derivation. Δ_λ / A≥3-absolute remains an open gate.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, fabs, acos

sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
M_E = mpf("0.51099895069")
q0 = mpf(str(Q0))

AME_B = {"D": mpf("2.2245662"), "T": mpf("8.4818"),
         "3He": mpf("7.7180"), "4He": mpf("28.29566")}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}


def q_int(m, q):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def hooks(lam):
    colh = [0] * (max(lam) if lam else 0)
    for ri in lam:
        for j in range(ri):
            colh[j] += 1
    hs = []
    for i, ri in enumerate(lam):
        for j in range(ri):
            arm = ri - j - 1
            leg = colh[j] - i - 1
            hs.append(arm + leg + 1)
    return hs


def dim_classical(lam):
    n = sum(lam)
    den = mpf(1)
    for h in hooks(lam):
        den *= h
    return mp.factorial(n) / den


def dim_q(lam, q):
    """Quantum dimension via the q-hook-length formula:
       dim_q(λ) = ([n]_q!) / Π_cells [hook]_q ."""
    n = sum(lam)
    num = mpf(1)
    for k in range(1, n + 1):
        num *= q_int(k, q)
    den = mpf(1)
    for h in hooks(lam):
        den *= q_int(h, q)
    return num / den


def abs_content(lam):
    return mpf(sum(abs(j - i) for i, ri in enumerate(lam) for j in range(ri)))


def load_y(n, q_inv=False):
    d = json.load(open(HERE / "y-lambda-at-q0.witness.json"))
    byn = d.get("data", d)["by_n"][str(n)]
    return {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in byn}


def main() -> int:
    weights = ["y_lambda", "dim_classical", "dim_q", "abs_content", "inv_y", "bar_y"]
    S = {w: {} for w in weights}
    qb = 1 / q0  # bar
    for name, fname in CHI.items():
        raw = json.load(open(HERE / fname))
        d = raw["data"] if "data" in raw else raw
        atom = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["atom"]["by_partition"]}
        free = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["free"]["by_partition"]}
        n = d["atom"]["n_strands"]
        y = load_y(n)
        acc = {w: mpf(0) for w in weights}
        for lam in atom:
            dl = dim_classical(list(lam))
            dth = acos(mp.mpc(atom[lam] / dl)) - acos(mp.mpc(free[lam] / dl))
            a = fabs(dth)
            wv = {
                "y_lambda": y[lam],
                "dim_classical": dl,
                "dim_q": dim_q(list(lam), q0),
                "abs_content": abs_content(list(lam)),
                "inv_y": (1 / y[lam] if y[lam] != 0 else mpf(0)),
                "bar_y": dim_q(list(lam), qb),  # bar-conjugate dim as y-proxy
            }
            for w in weights:
                acc[w] += wv[w] * a
        for w in weights:
            S[w][name] = acc[w]

    results = {}
    best = None
    for w in weights:
        num = sum(S[w][k] * AME_B[k] for k in CHI)
        den = sum(S[w][k] ** 2 for k in CHI)
        scale = num / den if den else mpf(0)
        worst = mpf(0); per = {}
        for k in CHI:
            Bp = scale * S[w][k]
            err = (Bp - AME_B[k]) / AME_B[k]
            per[k] = {"B_pred": float(Bp), "err": float(err)}
            worst = max(worst, fabs(err))
        diff = scale * (S[w]["T"] - S[w]["3He"])
        diff_err = (diff - (AME_B["T"] - AME_B["3He"])) / (AME_B["T"] - AME_B["3He"])
        # A-correlation sign: does Σ grow with A like binding?
        a_growth = float(S[w]["4He"] / S[w]["D"]) if S[w]["D"] != 0 else float("nan")
        results[w] = {"global_scale": float(scale), "worst_err": float(worst),
                      "t_he3_diff_err": float(diff_err),
                      "S_4He_over_S_D": a_growth, "per_isotope": per}
        if best is None or worst < results[best]["worst_err"]:
            best = w
        print(f"── {w:<14} worst|err|={float(worst)*100:7.1f}%  "
              f"T/³He diff={float(diff_err)*100:+7.1f}%  "
              f"S(⁴He)/S(D)={a_growth:6.2f}  (binding ratio = 12.72)")

    print(f"\nbest weight: {best}  worst|err|={results[best]['worst_err']*100:.1f}%")
    print("target S(⁴He)/S(D) ≈ 12.72 (binding grows ~13× D→⁴He)")
    closes = results[best]["worst_err"] <= 0.05

    wb = WitnessBuilder("probe-binding-measure-search", engine="mpmath")
    wb.set_description(
        "EXPLORATORY: search for the per-block binding measure w_λ^bind such "
        "that B = E·Σ_λ w_λ |Δθ_λ| (full-order complex θ_λ) tracks A≥3 "
        "absolute binding. Tests y_λ / dim_classical / dim_q / abs_content / "
        "1/y_λ / bar-y. The A-growth ratio S(⁴He)/S(D) should match the "
        "binding ratio 12.72. Δ_λ / A≥3-absolute remains open."
    )
    wb.add_data("weights", results)
    wb.add_data("best_weight", best)
    wb.add_data("target_A_growth_ratio", 12.72)
    wb.add_assertion(
        name="no_parameter_free_weight_closes_A3plus_absolute",
        computed=str(int(not closes)),
        expected="1",
        tolerance=0,
        source=(f"best weight {best} worst |err| = {results[best]['worst_err']*100:.1f}% "
                "(1 global scale); no parameter-free per-block weight closes A≥3 "
                "absolute binding to 5%. Reports the A-growth ratio per weight to "
                "guide w_λ^bind structural derivation."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
