#!/usr/bin/env python3
"""
Atomic-braid mass-table compute (Strategy 3 — knot operator + Δ_n full-twist).

⚠ DEPRECATION NOTICE (2026-05-08, AUDIT-DEEP-2026-05.md §3.3a, PR #564).
  ───────────────────────────────────────────────────────────────────────
  The single-anchor proton-only `E_0` calibration in this script is
  KNOWN BROKEN: it propagates 8–54 % errors to D, T, ³He, ⁴He via
  the jet-knot a_k coupling.  See the side-by-side comparison
  emitted by `atomic_mass_via_rho_k.py` (mean |err%| 36 % legacy
  vs 0.23 % rho_K on D, T, ³He).

  CANONICAL going-forward path: `atomic_mass_via_rho_k.py`, which
  uses the resolved formula `M(K) = ρ_K · m_e · |tr_M(K)|` (Options
  A + C in PR #564 — no additive T6, Mittag-Leffler complementarity).

  This script is RETAINED ONLY for downstream-witness compatibility.
  Downstream consumers (atomic_braid_mass_table_modes_sweep.py,
  mass_formula_6term_mpfr_50dps.py, paper_six_term_isotope_sweep.py)
  should migrate to `atomic-mass-via-rho-k.witness.json`.

  Migration tracker: `docs/coordination/1ppb.md` §Open phases · P4‴.

Re-derives the six-term mass formula using:

  • Per-carrier (proton/neutron) atomic-braid Markov traces
    (PR #534/#547, recursive axiomatic reducer).
  • Inter-nucleon Δ_I coupling via the quotient-braid Jones-
    polynomial factor a(Z, N) = J_{\bar\beta}(q)
    (per `prop:jet-filtered-knot-factor` and the H_3(R,q)
    crossing-balance identity δV_pn = h/2).
  • Full-twist Δ_n² action at saturated shells
    (per `conj:categorical-neutrality-saturated-shells`):
    Δ_n²·Φ_n = Φ_n at every magic n ∈ {2, 8, 20, 28, 50, 82, 126},
    so the saturated-shell mass is a fixed point of the
    full-twist scalar action.

The compound-atom Markov-trace anchor reads:

  |tr_M_atomic(K)| = |tr_M(p)|^Z · |tr_M(n)|^N · |a(Z, N)|

with the quotient-braid table:

  | A | quotient braid       | J(q)        |
  |---|----------------------|-------------|
  | 1 | trivial              | 1           |
  | 2 | single pn crossing   | 1           |
  | 3 | figure-eight 4₁      | 1 − h²      |
  | 4 | Borromean B₃²        | (1 − h²)²   |
  | 5+ | open — placeholder  | (1 − h²)^A−2 |

The ⁴He value (1 − h²)² is the genuine Borromean Jones polynomial.
For A ≥ 5 we extrapolate the (1 − h²) per nucleon-pair structure
pending a closed-form quotient-braid derivation.

Tower terms (T2, T3, T4, T6) follow the legacy paper-six-term-isotope
formula but use the Markov-axiom-derived single-/pair-generator
expressions for atomic-braid (n_gens = 3A - 1 in H_{3A}).

Calibration: proton-only.

Output: atomic-braid-mass-table.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from markov_trace_recursive import markov_trace_of_word, q as _q  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

q = _q
Q0 = mp.mpf(str(Q_MP))
H_VAL = Q0 - 1 / Q0
Z_MARK = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))


# ── Magic numbers (saturated shells) ───────────────────────────
# Empirical nuclear-physics shell closures.  The categorical
# derivation from Bring's surface is open
# (`conj:magic-numbers-bring`); until that conjecture is class-
# axiomatised these counts are an external input, not derived.
# Used here only as a structural placeholder for the full-twist
# scalar (atom is "magic" → full_twist_scalar(A) = 1).
MAGIC_NUCLEON_COUNTS = {2, 8, 20, 28, 50, 82, 126}


# ── Nucleon atomic-braid words (PR #534/#547) ──────────────────
PROTON_WORD = [1] * 7 + [2] * 4
NEUTRON_WORD = [1] * 6 + [2] * 4 + [-1]


# ── CODATA reference data ──────────────────────────────────────
M_E_MEV = mp.mpf("0.51099895")

ATOMS_CODATA = {
    "p":   {"Z": 1, "N": 0, "M_MeV": "938.27208816"},
    "n":   {"Z": 0, "N": 1, "M_MeV": "939.56542052"},
    "D":   {"Z": 1, "N": 1, "M_MeV": "1875.61294257"},
    "T":   {"Z": 1, "N": 2, "M_MeV": "2808.92113298"},
    "3He": {"Z": 2, "N": 1, "M_MeV": "2808.39160743"},
    "4He": {"Z": 2, "N": 2, "M_MeV": "3727.379378"},
}


# ── Quotient-braid Jones-polynomial factor a(Z, N) ─────────────
# Two sources for a(Z, N):
#   (a) Canonical: jet-knot-invariants.witness.json — per-level
#       convergent ratios a_k(Z,N) from Wedderburn-weighted
#       characters, computed by jet_knot_invariants.py.  Atoms
#       covered: ³H, ³He, ⁴He, ⁶Li, ⁷Li, ⁹Be, ¹²C, ¹⁶O.
#   (b) Fallback (Jones-quotient): for atoms not in the witness
#       (p, n, D, ⁵Li, ...), use the structural quotient-braid
#       Jones polynomial table from prop:jet-filtered-knot-factor:
#         A=1: 1   (trivial; no inter-nucleon structure)
#         A=2: 1   (single pn crossing, trivial Jones)
#         A=3+: 1 - h^2 (figure-eight) extrapolated as (1-h²)^(A-2)
_JET_KNOT_CACHE: dict[str, mp.mpf] | None = None
_ATOM_LABEL_TO_JET = {  # mass-table label → jet-knot key
    "T":   "³H",
    "3He": "³He",
    "4He": "⁴He",
    "6Li": "⁶Li",
    "7Li": "⁷Li",
    "9Be": "⁹Be",
    "12C": "¹²C",
    "16O": "¹⁶O",
}


def _load_canonical_a_jet() -> dict[str, mp.mpf]:
    """Load convergent a_k from jet-knot-invariants.witness.json.

    For each atom, returns the largest-k a_k (convergent value, per
    `prop:jet-filtered-knot-factor` Part 1: 'a_k converges by k=4').
    """
    global _JET_KNOT_CACHE
    if _JET_KNOT_CACHE is not None:
        return _JET_KNOT_CACHE
    path = HERE / "jet-knot-invariants.witness.json"
    out: dict[str, mp.mpf] = {}
    if not path.exists():
        _JET_KNOT_CACHE = out
        return out
    d = json.loads(path.read_text())
    for atom, info in d.get("data", {}).items():
        levels = info.get("levels", [])
        if not levels:
            continue
        # Use the highest-k entry (most converged).
        best = max(levels, key=lambda lvl: int(lvl.get("k", 0)))
        a_val = best.get("a_k")
        if a_val is None:
            continue
        out[atom] = mp.mpf(str(a_val))
    _JET_KNOT_CACHE = out
    return out


def jones_quotient_factor_fallback(Z: int, N: int) -> mp.mpf:
    """Structural quotient-braid Jones-polynomial factor.

    Per `prop:jet-filtered-knot-factor` Part 4 table:
      A = 1: trivial → 1
      A = 2: single pn crossing → 1
      A = 3: figure-eight 4_1 → 1 - h²
      A = 4: Borromean B_3² → (1 - h²)²
      A ≥ 5: open; extrapolate (1 - h²)^(A-2) as a placeholder.
    """
    A = Z + N
    h2 = H_VAL ** 2
    one_minus_h2 = 1 - h2
    if A <= 2:
        return mp.mpf(1)
    if A == 3:
        return one_minus_h2
    if A == 4:
        return one_minus_h2 ** 2
    return one_minus_h2 ** (A - 2)


def jones_quotient_factor(atom_label: str, Z: int, N: int) -> tuple[mp.mpf, str]:
    """Return (a_factor, source) — canonical convergent a_k from
    jet-knot-invariants when available, else Jones-quotient
    fallback."""
    canonical = _load_canonical_a_jet()
    jet_key = _ATOM_LABEL_TO_JET.get(atom_label)
    if jet_key is not None and jet_key in canonical:
        return canonical[jet_key], f"canonical_a_k(jet-knot:{jet_key})"
    return jones_quotient_factor_fallback(Z, N), "jones_quotient_fallback"


# ── Full-twist Δ_n² scalar at shell-saturation ─────────────────
def full_twist_scalar(A: int) -> mp.mpf:
    """Δ_n² scalar action at the categorical level n = 3A.

    Per `conj:categorical-neutrality-saturated-shells`,
    Δ_n² · Φ_n = Φ_n at magic n ∈ {2, 8, 20, 28, 50, 82, 126},
    i.e. the action is the IDENTITY (scalar 1) at saturation.

    For non-saturated shells, Δ_n² acts on each Wedderburn block
    V_λ by q^{c(λ)} where c(λ) is the content sum; the trace-level
    effect is a polynomial correction that we set to 1 here as a
    structural placeholder (the physical correction is absorbed
    into the tower terms T2, T3 in the six-term decomposition).
    """
    if A in MAGIC_NUCLEON_COUNTS:
        return mp.mpf(1)  # Categorical neutrality: trivial action
    return mp.mpf(1)      # Placeholder for non-magic; corrections via T2-T3


# ── Term 1 (atomic-braid + Δ_I + Δ_n²) ─────────────────────────
def t1_atomic_with_coupling(atom_label: str, Z: int, N: int,
                             tr_p: mp.mpf, tr_n: mp.mpf) -> tuple:
    """Return (|tr_M_atomic|, factors) where:

      |tr_M_atomic(K)| = |tr_M(p)|^Z · |tr_M(n)|^N · |a(Z, N)| · Δ_n²-scalar

    The disjoint-product piece is the per-carrier base; the
    multiplicative knot factor a(Z, N) couples the carriers via
    the Δ_I inter-nucleon interface knot.  When the atom is
    covered by `jet-knot-invariants.witness.json`, the canonical
    convergent a_k is used; otherwise the Jones-quotient fallback.
    Δ_n² adds the saturated-shell scalar.
    """
    A = Z + N
    base = abs(tr_p) ** Z * abs(tr_n) ** N
    a_ZN, a_source = jones_quotient_factor(atom_label, Z, N)
    delta_n2 = full_twist_scalar(A)
    t1 = base * a_ZN * delta_n2
    return t1, {
        "base_disjoint": base,
        "a_ZN": a_ZN,
        "a_ZN_source": a_source,
        "full_twist_delta_n2": delta_n2,
    }


# ── Tower terms (Markov-axiom values in atomic H_{3A}) ─────────
def t2_markov(n_gens: int) -> mp.mpf:
    return mp.mpf(n_gens) * Z_MARK ** 2


def t3_markov(n_gens: int) -> mp.mpf:
    return mp.mpf(n_gens * (n_gens - 1) // 2) * Z_MARK ** 4


# T4, T6: shared with atomic_braid_mass_table_modes_sweep via
# atomic_braid_mass_terms (consolidated per Gemini PR #548 medium-pri).
from atomic_braid_mass_terms import (  # noqa: E402
    t4_raw as _t4_raw,
    t6_canonical_MeV,
)


def t4_raw(A: int) -> mp.mpf:
    return _t4_raw(A, Q0)


# ── Assembly ───────────────────────────────────────────────────
def six_term_atomic(atom_label: str, Z: int, N: int,
                    tr_p: mp.mpf, tr_n: mp.mpf,
                    m_e_hecke: mp.mpf = mp.mpf(1)) -> dict:
    A = Z + N
    n_gens = max(3 * A - 1, 0)
    t1, t1_factors = t1_atomic_with_coupling(atom_label, Z, N, tr_p, tr_n)
    t2 = t2_markov(n_gens)
    t3 = t3_markov(n_gens)
    t4r = t4_raw(A)
    t4 = m_e_hecke * t4r
    t6_MeV = t6_canonical_MeV(A)
    total_hecke = t1 + t2 + t3 + t4
    return {
        "Z": Z, "N": N, "A": A, "n_gens": n_gens,
        "t1": t1, "t1_factors": t1_factors,
        "t2": t2, "t3": t3,
        "t4_raw": t4r, "t4": t4,
        "total_hecke": total_hecke,
        "t6_MeV": t6_MeV,
        "is_magic": A in MAGIC_NUCLEON_COUNTS,
    }


def main() -> int:
    print("=" * 96)
    print("  Atomic-braid mass-table — Strategy 3:")
    print("    knot-operator Δ_I (quotient-braid Jones factor)")
    print("    + full-twist Δ_n² (saturated-shell scalar)")
    print("=" * 96)

    print(f"\n  Substrate q_0 = {Q0}")
    print(f"  h = q − q⁻¹ = {mp.nstr(H_VAL, 12)}")
    print(f"  z = 1/(q^½+q⁻^½) = {mp.nstr(Z_MARK, 12)}")

    # Per-carrier Markov traces via recursive axiomatic reducer
    print(f"\n  Per-carrier |tr_M_atomic| via PR #547 recursive reducer:")
    tr_p_sym = markov_trace_of_word(3, PROTON_WORD)
    tr_n_sym = markov_trace_of_word(3, NEUTRON_WORD)

    def evaluate_at_q0(expr: sp.Expr) -> mp.mpf:
        return mp.mpf(str(expr.subs(q, sp.sympify(str(Q_MP))).evalf(mp.mp.dps)))

    tr_p = abs(evaluate_at_q0(tr_p_sym))
    tr_n = abs(evaluate_at_q0(tr_n_sym))
    print(f"    |tr_M(p)|_atomic = {mp.nstr(tr_p, 14)}")
    print(f"    |tr_M(n)|_atomic = {mp.nstr(tr_n, 14)}")

    # Quotient-braid Jones factors
    print(f"\n  Quotient-braid Jones factors a(Z,N) at q_0 (Δ_I coupling):")
    for atom, info in ATOMS_CODATA.items():
        a_ZN, a_src = jones_quotient_factor(atom, info["Z"], info["N"])
        print(f"    {atom:<5} (A={info['Z']+info['N']}): a = {mp.nstr(a_ZN, 14)}  [{a_src}]")

    # Per-atom assembly
    raw_terms = {}
    for atom, info in ATOMS_CODATA.items():
        terms = six_term_atomic(atom, info["Z"], info["N"], tr_p, tr_n)
        raw_terms[atom] = terms

    # Proton calibration
    M_p = mp.mpf(ATOMS_CODATA["p"]["M_MeV"])
    p_terms = raw_terms["p"]
    E_0 = (M_p - p_terms["t6_MeV"]) / p_terms["total_hecke"]
    print(f"\n  Proton calibration: E_0 = {mp.nstr(E_0, 14)} MeV/cat-unit")

    # Predict + report
    print(f"\n  {'atom':<6}{'M_codata':>12}{'M_pred':>12}{'err%':>9}"
          f"{'T1_total':>12}{'a(Z,N)':>10}{'T2':>10}{'T3':>10}"
          f"{'T4':>10}{'T6 MeV':>10}")
    print("  " + "-" * 102)

    rows = []
    err_atomic = []
    for atom, info in ATOMS_CODATA.items():
        terms = raw_terms[atom]
        M_codata = mp.mpf(info["M_MeV"])
        M_pred = E_0 * terms["total_hecke"] + terms["t6_MeV"]
        err_pct = (M_pred - M_codata) / M_codata * 100
        a_ZN = terms["t1_factors"]["a_ZN"]
        print(f"  {atom:<6}{float(M_codata):>12.4f}{float(M_pred):>12.4f}"
              f"{float(err_pct):>8.3f}%"
              f"{float(terms['t1']):>12.6f}{float(a_ZN):>10.6f}"
              f"{float(terms['t2']):>10.4f}{float(terms['t3']):>10.4f}"
              f"{float(terms['t4']):>10.4f}{float(terms['t6_MeV']):>10.4f}")
        rows.append({
            "atom": atom, "Z": terms["Z"], "N": terms["N"], "A": terms["A"],
            "is_magic": terms["is_magic"],
            "M_codata_MeV": str(M_codata),
            "M_pred_MeV": str(M_pred),
            "err_pct": str(err_pct),
            "term1_atomic_total": str(terms["t1"]),
            "term1_factor_disjoint_base": str(terms["t1_factors"]["base_disjoint"]),
            "term1_factor_a_ZN": str(a_ZN),
            "term1_factor_a_ZN_source": terms["t1_factors"]["a_ZN_source"],
            "term1_factor_full_twist_delta_n2": str(terms["t1_factors"]["full_twist_delta_n2"]),
            "term2_markov_z2": str(terms["t2"]),
            "term3_markov_z4": str(terms["t3"]),
            "term4_frobenius_codim": str(terms["t4"]),
            "term6_cyclotomic_tail_MeV": str(terms["t6_MeV"]),
            "total_hecke": str(terms["total_hecke"]),
            "n_gens": terms["n_gens"],
        })
        if atom != "p":
            err_atomic.append(abs(float(err_pct)))

    # Compare to legacy GS-NF + disjoint-product (if present)
    legacy_summary = {}
    legacy_path = HERE / "paper-six-term-isotope-sweep.witness.json"
    if legacy_path.exists():
        legacy = json.loads(legacy_path.read_text())
        for r in legacy.get("rows", []):
            label = r.get("isotope")
            if label and "M_predicted" in r:
                legacy_summary[label] = {
                    "M_pred": r["M_predicted"], "err_pct": r["err_pct"]
                }

    mean_atomic = sum(err_atomic) / len(err_atomic) if err_atomic else 0
    print(f"\n  Mean |err%| (atoms ≠ p) — Strategy 3 (knot-op + Δ_n): "
          f"{mean_atomic:.4f}%")
    legacy_mean = None
    if legacy_summary:
        leg_errs = [abs(v["err_pct"]) for k, v in legacy_summary.items()
                    if k != "p" and k in {r["atom"] for r in rows}]
        if leg_errs:
            legacy_mean = sum(leg_errs) / len(leg_errs)
            print(f"  Mean |err%| (atoms ≠ p) — legacy GS-NF (paper-six-term): "
                  f"{legacy_mean:.4f}%")

    print(f"\n  Comparison: Strategy 3 vs legacy GS-NF six-term:")
    print(f"  {'atom':<6}{'codata':>12}{'S3 pred':>12}{'S3 err%':>10}"
          f"{'GS_NF pred':>14}{'GS_NF err%':>14}")
    print("  " + "-" * 78)
    for row in rows:
        atom = row["atom"]
        M_pred = float(row["M_pred_MeV"])
        err = float(row["err_pct"])
        leg = legacy_summary.get(atom, {})
        leg_pred = leg.get("M_pred", float("nan"))
        leg_err = leg.get("err_pct", float("nan"))
        print(f"  {atom:<6}{float(row['M_codata_MeV']):>12.3f}"
              f"{M_pred:>12.3f}{err:>9.3f}%"
              f"{leg_pred:>14.3f}{leg_err:>13.3f}%")

    # Emit witness via WitnessBuilder (canonical schema; staleness
    # detection via scriptHash).  Per Copilot PR #548 medium-pri
    # comments on schema compliance.
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("atomic-braid-mass-table", engine="mpmath")
         .set_description(
            "Six-term mass formula re-derived using the atomic-braid "
            "Markov-trace anchor (PR #534/#547) with inter-carrier "
            "coupling via the quotient-braid Jones-polynomial factor "
            "a(Z, N) = J_{bar β}(q) (Δ_I knot operator, per "
            "prop:jet-filtered-knot-factor) and the full-twist Δ_n² "
            "saturated-shell scalar (per "
            "conj:categorical-neutrality-saturated-shells). "
            "T1 = |tr_M(p)|^Z · |tr_M(n)|^N · |a(Z, N)| · Δ_n²-scalar. "
            "T2, T3 are Markov-axiom values for n_gens = 3A-1. "
            "T4 = Frobenius codim. T6 = cyclotomic tail. "
            "Calibration: proton-only."
         )
         .set_content_block("prop:atomic-mass-gb-nf"))
    w.parameters.update({
        "q_0": str(Q0),
        "h": str(H_VAL),
        "z": str(Z_MARK),
        "m_e_MeV": str(M_E_MEV),
        "E_0_MeV_proton_anchored": str(E_0),
        "abs_tr_M_atomic_p": str(tr_p),
        "abs_tr_M_atomic_n": str(tr_n),
        "magic_shells_used": sorted(MAGIC_NUCLEON_COUNTS),
        "jones_quotient_table": {
            "A=1": "1",
            "A=2": "1",
            "A=3": "1 - h^2",
            "A=4": "(1 - h^2)^2",
            "A>=5": "(1 - h^2)^(A-2) [extrapolation, open]",
        },
    })
    w.add_data("reference_blocks", [
        "thm:knot-mass-formula-unified",
        "prop:markov-trace-axiomatic-closed-form",
        "prop:markov-trace-recursive-reducer",
        "prop:jet-filtered-knot-factor",
        "conj:categorical-neutrality-saturated-shells",
        "prop:knot-operator-transition",
        "prop:categorical-mass-markov",
    ])
    w.add_data("rows", rows)
    w.add_data("summary", {
        "mean_abs_err_pct_strategy3": str(mean_atomic),
        "mean_abs_err_pct_legacy_GS_NF": (
            str(legacy_mean) if legacy_mean is not None else None
        ),
    })
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
