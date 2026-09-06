"""
log_delta_full_mass_subtract.py — categorical derivation of B(K) as
the FULL-MASS DIFFERENCE under the unified formula.

Per the prior finding (log_delta_categorical_derivation.py): applying
prop:unified-curvature-rank-mass-formula with paper's prescribed
weight ~w_λ = dim_q²/[n]_q! to compute B(K) directly gives 43× cross-
atom variance. Identity weight gives 4.6×.

**Hypothesis to test:** the unified formula with ~w_λ is correct for
the FULL atomic mass m_{q,K}, NOT for the binding energy B(K). The
binding is the *difference* between atomic full-mass and constituent
proton/neutron full-mass:

    B(K) = m_{q,K} - Z · m_{q,p} - N · m_{q,n}

This script:
  1. Computes m_{q,X} for X ∈ {p, n, D, T, ³He, ⁴He} using the unified
     formula under four weight forms (see WEIGHT_FORMS below).
  2. Forms B_pred(K) = m_{q,K} - Z · m_{q,p} - N · m_{q,n}.
  3. Compares to AME binding.
  4. Reports cross-atom variance.

NORMALIZATION (2026-09-05, bean qou-uk8o).  The weight this producer has
always used is (f^λ)²/[n]_q! — the χ witnesses' `dim` field is the classical
Specht dimension, so the historical variable name `dim_q` was wrong.  That
weight is not a probability measure: it sums to n!/[n]_q!, which runs
0.980 / 0.858 / 0.612 / 0.326 at n = 3 / 6 / 9 / 12 and so rescales each
atom's B_pred by a *different*, monotonically shrinking factor.  The form is
kept (renamed `f2_over_qfact`, numbers unchanged) beside two self-normalized
forms that are measures at every n.  What the correction shows is that the
old 9.35× "cross-atom variance" was a partial cancellation between two
errors: self-normalized, T/³He/⁴He agree to 1.10× and the whole spread is
the deuteron.

If B_pred matches AME with variance ≪ 5.22× (or even ≪ 4.6×), this
substantiates the categorical claim that the unified formula is
PAPER-CORRECT and the binding energy is the n-strand-renormalized
difference, NOT a direct application of the formula.

Ref: prop:unified-curvature-rank-mass-formula
Ref: docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import fmt, set_compute_dps  # noqa: E402 — dps must rise before module constants
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV,
)
from q_parameter import Q as Q0

CHI_FILES = {
    "p":   "chi-proton-h3-at-q0-50dps.witness.json",
    "n":   "chi-neutron-h3-at-q0-50dps.witness.json",
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

B_AME = {  # binding energies (MeV); 0 for free nucleons
    "p":   mp.mpf(0),
    "n":   mp.mpf(0),
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

# (Z, N) for each species
ZN = {"p": (1, 0), "n": (0, 1), "D": (1, 1), "T": (1, 2),
      "3He": (2, 1), "4He": (2, 2)}


def depth(lam):
    return len(lam) - 1


def alpha_k(k):
    z_mark = Q0**3 / (Q0**2 + 1)
    G = mp.catalan
    if k == 0 or k == 1 or k == 3: return mp.mpf(1)
    if k == 2: return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G  # k >= 4 (CAL-1)


def q_int(k):
    """[k]_q = (q^k - q^{-k})/(q - q^{-1})"""
    return (Q0 ** k - Q0 ** (-k)) / (Q0 - 1 / Q0)


def q_factorial(n):
    """[n]_q! = [1]_q [2]_q ... [n]_q"""
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= q_int(k)
    return r


def _hooks(lam):
    """Hook lengths of every cell of `lam` (arm + leg + 1)."""
    out = []
    for r, row in enumerate(lam):
        for c in range(row):
            arm = row - c - 1
            leg = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            out.append(arm + leg + 1)
    return out


def dim_q(lam):
    """d_q(λ) = [n]_q! / ∏_cells [h]_q — the *quantum* dimension.

    Distinct from the classical Specht dimension f^λ = n!/∏h, which is what
    the χ witnesses carry in their `dim` field.  Keeping the two apart matters
    here: the weight forms below use one or the other and they are NOT
    interchangeable at q ≠ 1.
    """
    d = q_factorial(sum(lam))
    for h in _hooks(lam):
        d /= q_int(h)
    return d


def load_chi(species):
    """Load (n, partitions) for species X."""
    w = json.loads((HERE / CHI_FILES[species]).read_text())
    n = int(w["n_strands"])
    parts = []
    for p in w["by_partition"]:
        lam = p["partition"] if isinstance(p["partition"], list) else ast.literal_eval(p["partition"])
        parts.append({
            "partition": tuple(lam),
            "depth": depth(lam),
            "dim": int(p["dim"]),
            "chi": mp.mpf(p["chi_lambda"]),
        })
    return n, parts


# ── weight forms ────────────────────────────────────────────────────────────
# `f2_over_qfact` is what this producer has always computed, and its name is
# now literal: the χ witness's `dim` field is the CLASSICAL Specht dimension
# f^λ, not d_q, so the weight it forms is (f^λ)²/[n]_q! — neither the textbook
# q-Plancherel weight nor the classical Plancherel measure.  It is NOT a
# probability measure: Σ_λ (f^λ)² = n! exactly (Burnside), so it sums to
#     n!/[n]_q!  =  0.98029937 / 0.85832883 / 0.61193301 / 0.32612477
# at n = 3 / 6 / 9 / 12 — a factor 3.0 spread across the light series, and it
# is *decreasing* in n.  Since Φ_k is linear in the weights, every Φ and hence
# every B_pred at strand count n is scaled by exactly that factor; it cancels
# from any ratio taken at one n and does NOT cancel from the cross-atom
# max/min this producer is scored on.  (This is the same defect class as
# docs/audits/2026-09-04-plancherel-convention-gap.md, but a *different and
# larger* constant: that audit's c_n = Σ d_q²/[n]_q! runs 0.99/1.11/1.52 and
# increases with n.  Measure per producer; do not reuse c_n.)
#
# The two `_selfnorm` forms below divide by the weight's own total, so each is
# a probability measure at every n by construction and the cross-atom
# comparison is normalization-free.  Bean qou-uk8o.
WEIGHT_FORMS = ("f2_over_qfact", "f2_selfnorm", "dq2_selfnorm", "identity")


def _weight_map(parts, n, w_form):
    """{partition-index: w_λ} for the chosen form, self-normalized where named.

    `parts` entries carry the classical f^λ in `dim`; d_q is recomputed here.
    """
    if w_form == "identity":
        return [mp.mpf(1) for _ in parts]
    if w_form == "f2_over_qfact":
        qfact = q_factorial(n)
        return [mp.mpf(p["dim"]) ** 2 / qfact for p in parts]
    if w_form == "f2_selfnorm":
        raw = [mp.mpf(p["dim"]) ** 2 for p in parts]
    elif w_form == "dq2_selfnorm":
        raw = [dim_q(p["partition"]) ** 2 for p in parts]
    else:
        raise ValueError(w_form)
    tot = sum(raw, mp.mpf(0))
    if tot == 0:
        raise ZeroDivisionError(f"{w_form}: weight total is zero at n={n}")
    return [r / tot for r in raw]


def phi_k(parts, n, k, w_form="f2_over_qfact"):
    """Φ_k(β) under chosen weight form."""
    total = mp.mpf(0)
    weights = _weight_map(parts, n, w_form)
    for p, w in zip(parts, weights):
        if p["depth"] != k: continue
        chi = p["chi"]; f_lam = mp.mpf(p["dim"])
        f = mp.fabs(chi) * f_lam
        if f < mp.mpf("1e-30"): continue
        total += w * mp.log(f)
    return total


def unified_mass(species, w_form="f2_over_qfact"):
    n, parts = load_chi(species)
    total = mp.mpf(0)
    for k in range(n):
        total += alpha_k(k) * phi_k(parts, n, k, w_form)
    return total, n


def main() -> int:
    builder = WitnessBuilder("log-delta-full-mass-subtract")
    builder.set_description(
        "Categorical test: B(K) = m_{q,K} - Z·m_{q,p} - N·m_{q,n} via "
        "prop:unified-curvature-rank-mass-formula with paper-prescribed "
        "four weight forms. Tests if the binding-energy projection IS the "
        "n-strand-renormalized difference. The as-published form "
        "(f^λ)²/[n]_q! is NOT a probability measure — it sums to n!/[n]_q! "
        "(0.980/0.858/0.612/0.326 at n=3/6/9/12), so it rescales every "
        "cross-atom comparison by a factor that varies 3.0x across the "
        "light series; the two _selfnorm forms are measures at every n by "
        "construction (bean qou-uk8o)."
    )

    print(f"{'species':<6} {'n':>3} {'w_form':<10} {'m_q,X':>16}")
    full_mass = {}
    for w_form in WEIGHT_FORMS:
        full_mass[w_form] = {}
        for sp in ("p", "n", "D", "T", "3He", "4He"):
            m, n = unified_mass(sp, w_form)
            full_mass[w_form][sp] = m
            print(f"  {sp:<6} {n:>3} {w_form:<10} {float(m):>16.6f}")
        print()

    builder.add_data("full_mass_per_species", {
        wf: {sp: str(m) for sp, m in d.items()}
        for wf, d in full_mass.items()
    })

    # Compute B_pred(K) = m_K - Z·m_p - N·m_n per weight form
    print(f"{'atom':<6} {'w_form':<10} {'B_pred':>14} {'B_AME':>12} {'ratio':>10}")
    results = {}
    for w_form in WEIGHT_FORMS:
        mp_full = full_mass[w_form]
        results[w_form] = {}
        for atom in ("D", "T", "3He", "4He"):
            Z, N = ZN[atom]
            B_pred = mp_full[atom] - Z * mp_full["p"] - N * mp_full["n"]
            B_emp = B_AME[atom]
            ratio = mp.fabs(B_pred / B_emp) if B_emp != 0 else mp.mpf("nan")
            results[w_form][atom] = {
                "B_pred": str(B_pred),
                "B_AME": str(B_emp),
                # `ratio` is an mpf all the way from B_pred; float() here would
                # have written a binary64 value into the witness (NO-FLOAT64).
                "ratio": fmt(ratio),
            }
            print(f"  {atom:<6} {w_form:<10} {float(B_pred):>14.6f} "
                  f"{float(B_emp):>12.6f} {float(ratio):>10.4f}")
        print()

    builder.add_data("binding_by_difference", results)
    builder.add_data("canonical_status", "canonical-with-empirical-assignment")

    # Cross-atom variance
    print(f"{'w_form':<10} {'min ratio':>12} {'max ratio':>12} {'max/min':>10}")
    summary = {}
    for w_form, atoms in results.items():
        rs = [mp.mpf(r["ratio"]) for r in atoms.values()]
        rs = [r for r in rs if not mp.isnan(r)]
        if rs:
            rmin, rmax = min(rs), max(rs)
            mom = rmax / rmin if rmin > 0 else mp.inf
            # The heavy three alone. Recorded because the deuteron is the sole
            # outlier under the self-normalized forms and folding it into one
            # max/min hides that: it turns a tight T/³He/⁴He cluster plus one
            # miss into a single large "variance". This is a derived statistic,
            # NOT a re-tuned threshold — the verdict cut-offs below are left at
            # their historical values on purpose (bean qou-uk8o).
            rs_hv = [mp.mpf(atoms[a]["ratio"]) for a in ("T", "3He", "4He")
                     if a in atoms and not mp.isnan(mp.mpf(atoms[a]["ratio"]))]
            mom_hv = (max(rs_hv) / min(rs_hv)
                      if rs_hv and min(rs_hv) > 0 else mp.inf)
            summary[w_form] = {
                "min": fmt(rmin), "max": fmt(rmax),
                "max_over_min": fmt(mom),
                "max_over_min_heavy_three_no_deuteron": fmt(mom_hv),
            }
            print(f"  {w_form:<14} {float(rmin):>12.4f} {float(rmax):>12.4f} "
                  f"{float(mom):>10.4f}   (T/³He/⁴He only: {float(mom_hv):.4f})")
    builder.add_data("variance_summary", summary)

    # Verdict
    best = min(summary.keys(),
               key=lambda k: mp.mpf(summary[k]["max_over_min"]))
    best_mom = mp.mpf(summary[best]["max_over_min"])
    builder.add_data("best_form", best)
    builder.add_data("best_max_over_min", fmt(best_mom))
    if best_mom < 1.05:
        verdict = f"PASS — {best} gives max/min < 1.05 (universal categorical constant)"
    elif best_mom < 1.5:
        verdict = f"STRONG — {best} max/min = {best_mom:.3f} (under 1.5×, much better than direct 5.22×)"
    elif best_mom < 4.6:
        verdict = f"IMPROVES — {best} max/min = {best_mom:.3f} (better than identity-direct 4.6×)"
    elif best_mom < 5.22:
        verdict = f"MARGINAL — {best} max/min = {best_mom:.3f} (better than Phase 2's 5.22× but not by much)"
    else:
        verdict = f"NO IMPROVEMENT — {best} max/min = {best_mom:.3f} (≥ 5.22×)"
    builder.add_data("verdict", verdict)
    print(f"\n  Verdict: {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=B_AME["D"],
        # mpf, not a float literal: a binary64 `expected` is a raw-float64
        # field in the witness and cannot represent the value it asserts.
        expected=AME_B_DEUTERON_MEV_VALIDATION,
        tolerance=mp.mpf("1e-10"),
        unit="B(D) AME MeV",
        source="AME 2020 deuteron binding",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
