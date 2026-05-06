#!/usr/bin/env python3
"""
Atomic-braid mass-table compute (Strategy 2 from PR #547 follow-up).

Re-derives the six-term mass formula using the **atomic-braid
representation** for the canonical Markov-trace anchor (Term 1),
in place of the GS-NF representation used by
`paper_six_term_isotope_sweep.py`.

Two key structural differences from the legacy six-term:

  1. **Term 1**:  canonical |tr_M| is computed via the
     representation-theory-free recursive reducer on the
     atomic-braid word in H_n (per `prop:markov-trace-axiomatic-
     closed-form` and `prop:markov-trace-recursive-reducer`).
     For compound atoms (A ≥ 2) the atom is realised as a
     disjoint product of nucleon clusters in H_{3A}, so

         |tr_M_atomic(K)|  =  |tr_M(p)|^Z · |tr_M(n)|^N

     by the empirically-verified disjoint-product property
     (mpmath-exact at 50 dps for the H_6 deuteron).

  2. **Tower terms (T2, T3)**:  evaluated in the larger ambient
     algebra H_{3A} corresponding to the disjoint cluster
     embedding.  For the atomic-braid setting we use the
     Markov-axiom values of single-generator and pair-generator
     traces directly (mode `r-side-bare` from the legacy script):

         T2(A)  =  n_gens(A) · z²
         T3(A)  =  C(n_gens(A), 2) · z⁴

     where `n_gens(A) = 3·A - 1` (= number of σ-generators in
     the H_{3A} embedding with one slot per nucleon-pair gluon
     coupling kept disjoint).

Terms 4-6 follow the legacy convention:
  - T4 = m_e · τ(C_dim_q) at A=Z+N (Frobenius codim).
  - T5 = chirality factor (multiplicative on T1 for back-compat).
  - T6 = canonical cyclotomic residue tail (per-A, in MeV).

Calibration:  proton-only.  E_0 = (M_p^CODATA - T6_p) / total_hecke(p).

Output: atomic-braid-mass-table.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from itertools import combinations
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

# Hecke quadratic h, Markov parameter z evaluated at q_0.
H_VAL = Q0 - 1 / Q0
Z_MARK = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))


# ── Nucleon atomic-braid words (PR #534 / #547) ────────────────
PROTON_WORD = [1] * 7 + [2] * 4
NEUTRON_WORD = [1] * 6 + [2] * 4 + [-1]

# ── Reference data ─────────────────────────────────────────────
M_E_MEV = mp.mpf("0.51099895")

ATOMS_CODATA = {
    "p":   {"Z": 1, "N": 0, "M_MeV": "938.27208816"},
    "n":   {"Z": 0, "N": 1, "M_MeV": "939.56542052"},
    "D":   {"Z": 1, "N": 1, "M_MeV": "1875.61294257"},
    "T":   {"Z": 1, "N": 2, "M_MeV": "2808.92113298"},
    "3He": {"Z": 2, "N": 1, "M_MeV": "2808.39160743"},
    "4He": {"Z": 2, "N": 2, "M_MeV": "3727.379378"},
}


# ── Term 1: |tr_M_atomic| via disjoint-product ─────────────────
def t1_atomic(Z: int, N: int, tr_p: mp.mpf, tr_n: mp.mpf) -> mp.mpf:
    """|tr_M(atomic-braid(Z, N))| via disjoint-product property.

    By prop:markov-trace-recursive-reducer (disjoint-product
    property), embedding Z protons + N neutrons on disjoint H_3
    clusters in H_{3·(Z+N)} gives

      tr_M_atomic = tr_M(p)^Z · tr_M(n)^N.

    Verified empirically to 1e-50 for D = p ⊗ n on H_6.
    """
    return abs(tr_p) ** Z * abs(tr_n) ** N


# ── Term 2, T3: Markov-axiom-derived (r-side-bare equivalent) ──
def t2_markov(n_gens: int) -> mp.mpf:
    """T2 = n_gens · z² (Markov axiom: tr_M(σ_i) = z, then × z multiplier)."""
    return mp.mpf(n_gens) * Z_MARK ** 2


def t3_markov(n_gens: int) -> mp.mpf:
    """T3 = C(n_gens, 2) · z⁴ (Markov pair-z² axiom)."""
    return mp.mpf(n_gens * (n_gens - 1) // 2) * Z_MARK ** 4


# ── Term 4: Frobenius codim (cached from legacy table) ─────────
# τ(C_dim_q) for n = 3A.  Imported from the existing implementation.
def t4_raw(A: int) -> mp.mpf:
    if A < 1:
        return mp.mpf(0)
    from schur_weyl_symbolic import partitions_of
    from hecke_characters import young_hooks, qfac
    n = 3 * A
    nfac_val = mp.mpf(qfac(n))
    denom = Q0 - 1 / Q0
    total = mp.mpf(0)
    for lam in partitions_of(n):
        hooks = young_hooks(lam)
        # dim_q(λ) = [n]_q! / Π_{x∈λ} [h(x)]_q
        dim_q = nfac_val
        for h in hooks:
            qh = (Q0 ** h - 1 / Q0 ** h) / denom
            dim_q = dim_q / qh
        total += 1 / dim_q
    return total


# ── Term 6: cyclotomic tail per A (MeV-valued, from witness) ───
def t6_canonical_MeV(A: int) -> mp.mpf:
    """Canonical T6 tail per A (loaded once from the existing
    Habiro-residue witness; falls back to 0 if absent)."""
    cache_path = HERE / "habiro_residue.witness.json"
    candidates = [
        HERE / "habiro-residue.witness.json",
        HERE / "habiro_residue.witness.json",
    ]
    data = None
    for p in candidates:
        if p.exists():
            try:
                data = json.loads(p.read_text())
                break
            except json.JSONDecodeError:
                continue
    if data is None:
        return mp.mpf(0)
    by_A = data.get("residue_per_A_MeV", data.get("rows", {}))
    if isinstance(by_A, dict):
        return mp.mpf(str(by_A.get(str(A), by_A.get(A, "0"))))
    if isinstance(by_A, list):
        for row in by_A:
            if int(row.get("A", -1)) == A:
                return mp.mpf(str(row.get("residue_MeV", 0)))
    return mp.mpf(0)


# ── Six-term assembly (atomic-braid edition) ───────────────────
def six_term_atomic(Z: int, N: int, tr_p: mp.mpf, tr_n: mp.mpf,
                    m_e_hecke: mp.mpf = mp.mpf(1)) -> dict:
    """Atomic-braid six-term formula in Hecke units (T1+T2+T3+T4)
    plus T6 (in MeV)."""
    A = Z + N
    n_gens = max(3 * A - 1, 0)  # H_{3A} has 3A−1 generators
    t1 = t1_atomic(Z, N, tr_p, tr_n)
    t2 = t2_markov(n_gens)
    t3 = t3_markov(n_gens)
    t4r = t4_raw(A)
    t4 = m_e_hecke * t4r
    t6_MeV = t6_canonical_MeV(A)
    total_hecke = t1 + t2 + t3 + t4
    return {
        "Z": Z, "N": N, "A": A, "n_gens": n_gens,
        "t1": t1, "t2": t2, "t3": t3,
        "t4_raw": t4r, "t4": t4,
        "total_hecke": total_hecke,
        "t6_MeV": t6_MeV,
    }


def main() -> int:
    print("=" * 96)
    print("  Atomic-braid mass-table — six-term formula re-derived using")
    print("  the recursive axiomatic Markov-trace reducer (Strategy 2).")
    print("=" * 96)

    # ── Compute |tr_M| of nucleons via the recursive reducer ────
    print(f"\n  Substrate q_0 = {Q0}")
    print(f"  Computing |tr_M_atomic(p)| and |tr_M_atomic(n)| ...")
    tr_p_sym = markov_trace_of_word(3, PROTON_WORD)
    tr_n_sym = markov_trace_of_word(3, NEUTRON_WORD)

    def evaluate_at_q0(expr: sp.Expr) -> mp.mpf:
        return mp.mpf(str(expr.subs(q, sp.sympify(str(Q_MP))).evalf(mp.mp.dps)))

    tr_p = abs(evaluate_at_q0(tr_p_sym))
    tr_n = abs(evaluate_at_q0(tr_n_sym))
    print(f"    |tr_M(p)|_atomic = {mp.nstr(tr_p, 16)}")
    print(f"    |tr_M(n)|_atomic = {mp.nstr(tr_n, 16)}")

    # ── Per-atom six-term assembly ──────────────────────────────
    raw_terms = {}
    for atom, info in ATOMS_CODATA.items():
        terms = six_term_atomic(info["Z"], info["N"], tr_p, tr_n)
        raw_terms[atom] = terms

    # ── Proton calibration: E_0 = (M_p^CODATA - t6_p) / total(p) ─
    M_p = mp.mpf(ATOMS_CODATA["p"]["M_MeV"])
    p_terms = raw_terms["p"]
    E_0 = (M_p - p_terms["t6_MeV"]) / p_terms["total_hecke"]
    print(f"\n  Proton calibration: E_0 = {mp.nstr(E_0, 12)} MeV/cat-unit")

    # ── Predict masses + report ─────────────────────────────────
    print(f"\n  {'atom':<6}{'M_codata':>12}{'M_pred':>12}{'err%':>10}"
          f"{'T1':>14}{'T2':>10}{'T3':>10}{'T4':>10}{'T6 (MeV)':>12}")
    print("  " + "-" * 96)

    rows = []
    for atom, info in ATOMS_CODATA.items():
        terms = raw_terms[atom]
        M_codata = mp.mpf(info["M_MeV"])
        M_pred = E_0 * terms["total_hecke"] + terms["t6_MeV"]
        err_pct = (M_pred - M_codata) / M_codata * 100
        print(f"  {atom:<6}{float(M_codata):>12.4f}{float(M_pred):>12.4f}"
              f"{float(err_pct):>9.3f}%"
              f"{float(terms['t1']):>14.6f}{float(terms['t2']):>10.4f}"
              f"{float(terms['t3']):>10.4f}{float(terms['t4']):>10.4f}"
              f"{float(terms['t6_MeV']):>12.4f}")
        rows.append({
            "atom": atom, "Z": terms["Z"], "N": terms["N"], "A": terms["A"],
            "M_codata_MeV": str(M_codata),
            "M_pred_MeV": str(M_pred),
            "err_pct": str(err_pct),
            "term1_atomic_tr_M": str(terms["t1"]),
            "term2_markov_z2": str(terms["t2"]),
            "term3_markov_z4": str(terms["t3"]),
            "term4_frobenius_codim": str(terms["t4"]),
            "term6_cyclotomic_tail_MeV": str(terms["t6_MeV"]),
            "total_hecke": str(terms["total_hecke"]),
            "n_gens": terms["n_gens"],
        })

    # ── Comparison summary vs legacy GS-NF six-term ─────────────
    legacy_path = HERE / "paper-six-term-isotope-sweep.witness.json"
    legacy_summary = {}
    if legacy_path.exists():
        legacy = json.loads(legacy_path.read_text())
        for r in legacy.get("rows", []):
            label = r.get("isotope")
            if label and "M_predicted" in r and "M_codata" in r:
                legacy_summary[label] = {
                    "M_pred": r["M_predicted"], "err_pct": r["err_pct"]
                }

    print(f"\n  Comparison: atomic-braid vs legacy GS-NF six-term:")
    print(f"  {'atom':<6}{'codata':>12}{'atomic_pred':>14}{'atomic_err%':>14}"
          f"{'GS_NF_pred':>14}{'GS_NF_err%':>14}")
    print("  " + "-" * 80)
    mean_abs_atomic = mp.mpf(0)
    n = 0
    for row in rows:
        atom = row["atom"]
        M_pred = mp.mpf(row["M_pred_MeV"])
        err = mp.mpf(row["err_pct"])
        leg = legacy_summary.get(atom, {})
        leg_pred = leg.get("M_pred", float("nan"))
        leg_err = leg.get("err_pct", float("nan"))
        print(f"  {atom:<6}{float(row['M_codata_MeV']):>12.3f}"
              f"{float(M_pred):>14.3f}{float(err):>13.3f}%"
              f"{leg_pred:>14.3f}{leg_err:>13.3f}%")
        if atom != "p":
            mean_abs_atomic += abs(err)
            n += 1
    if n > 0:
        mean_abs_atomic /= n
        print(f"\n  Mean |err%| (atoms ≠ p) — atomic-braid: {mp.nstr(mean_abs_atomic, 6)}%")

    legacy_mean = None
    if legacy_summary:
        legacy_errs = [abs(v["err_pct"]) for k, v in legacy_summary.items()
                       if k != "p" and k in {r["atom"] for r in rows}]
        if legacy_errs:
            legacy_mean = sum(legacy_errs) / len(legacy_errs)
            print(f"  Mean |err%| (atoms ≠ p) — legacy GS-NF:  {legacy_mean:.4f}%")

    witness = {
        "computation": "atomic-braid-mass-table",
        "description": (
            "Six-term mass formula re-derived using atomic-braid "
            "Markov-trace anchor (PR #534/#547). Term 1 is computed via "
            "the recursive axiomatic reducer on σ_1^7σ_2^4 (proton) and "
            "σ_1^6σ_2^4σ_1^{-1} (neutron); compound atoms use the "
            "empirically-verified disjoint-product property "
            "tr_M_atomic(K) = tr_M(p)^Z · tr_M(n)^N. T2,T3 are the "
            "Markov-axiom-derived single-/pair-generator tower values "
            "for n_gens = 3A-1. T4 = m_e·τ(C_dim_q) (Frobenius codim). "
            "T6 = canonical cyclotomic residue tail. Calibration: "
            "E_0 from proton-only anchor."
        ),
        "reference_blocks": [
            "thm:knot-mass-formula-unified",
            "prop:markov-trace-axiomatic-closed-form",
            "prop:markov-trace-recursive-reducer",
            "prop:categorical-mass-markov",
            "prop:atomic-mass-gb-nf",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(Q0),
            "m_e_MeV": str(M_E_MEV),
            "E_0_MeV_proton_anchored": str(E_0),
            "abs_tr_M_atomic_p": str(tr_p),
            "abs_tr_M_atomic_n": str(tr_n),
        },
        "rows": rows,
        "summary": {
            "mean_abs_err_pct_atomic_excl_p": str(mean_abs_atomic),
            "mean_abs_err_pct_legacy_GS_NF": (
                str(legacy_mean) if legacy_mean is not None else None
            ),
        },
    }
    out = HERE / "atomic-braid-mass-table.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
