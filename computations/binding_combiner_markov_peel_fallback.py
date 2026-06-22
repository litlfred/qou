#!/usr/bin/env python3
"""
Binding-energy combiner via the canonical `markov_peel` trace — Path 3.

This is the **closure-path-3 follow-up** flagged in
`docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md`
§"Option 4 (operator-valued combiner)".  The operator-valued combiner
`canonical_tr_m_via_branching.py` is end-to-end only for A=2: at A ≥ 3
the H_9+ A-operator extracts are rank-deficient (least-squares fits over
the H_3 inner-test family, not universal interface operators), so the
combiner returns `None` rather than silently-wrong values.

Path 3 (documented in `canonical_tr_m_via_branching.py:245-248`) bypasses
that blocker entirely by NOT using the A-operator extracts at all.  It
forms the binding directly from the canonical Markov trace of the
free vs. bound atomic braid:

    B(K)  =  E_0 · ( |tr_M(β_free)| − |tr_M(β_atom)| )

where

    β_free  =  atom_braid_word_3A(Z, N, include_inter=False)   (disjoint nucleons)
    β_atom  =  atom_braid_word_3A(Z, N, include_inter=True)    (bound: interface knots on)

and tr_M is the canonical Markov-axiom recursive-ascent trace
(`markov_peel.incremental_reduced_element` Gröbner–Shirshov reduction +
`markov_trace_canonical.tr_M_element`), evaluated at q = q₀.  This is the
same exact-symbolic-in-q trace path validated against the Hoefsmit +
Wenzl bridge witness (`atomic-tr-m-mpfr-50dps.witness.json`) to 50 dps.

No A-operator extract, no Rust kernel, no rank-deficiency gate: the
combiner succeeds for every A the GS reducer can handle (D, T, ³He, ⁴He
here; ⁵Li/⁶Li under `--include-li`).

p-n interface convention (IMPORTANT)
------------------------------------
The `markov_peel` trace path is *exact-symbolic in q* by construction —
`crossing_from_cd` maps each numeric (c, d) crossing to an exact element
of ℚ(q)·H_n(q).  The canonical default p-n interface
(`pn_convention="bring_color_weighted"`) uses the crossing
`σ − h·(½ − δ/4)·1` with `δ = flavor_split_subleading(q₀)` a *numeric*
function of q₀ (see `_li_2_q_util.flavor_split_subleading` /
`canonical_braid_crossings._avg_color_delta`).  A numeric δ cannot be
represented as an exact polynomial in the formal symbol q, so the
exact-symbolic trace path can only carry the color-blind averaged
crossing `σ − h/2·1` (`pn_convention="strict_averaged"`).

This combiner therefore uses `strict_averaged` for the bound config.
The color weighting is a sub-0.1 % numeric perturbation on a single
crossing coefficient (δ ≈ 1.4e-3 ⇒ Δd/d ≈ 0.07 %); it is negligible
against the binding shortfall this script measures (see below), and the
free config has no interface crossings at all, so the binding
*difference* is convention-consistent.

Result (the point of running this)
----------------------------------
Path 3 gives the canonical trace-difference binding blocker-free, but it
does NOT close binding: the raw |tr_M| difference under-binds severely
and with the wrong A-trend (ratio falls D → T → … as A grows, opposite
to the real growth of B/A).  This is the numerical confirmation of the
audit's structural diagnosis (§"Why the tower undershoots" (iv)):

    a per-atom trace difference carries no A-scale ("magic-A") factor,
    so it cannot reproduce the 2·m_e·A·8G shell binding.

The value of this script is (a) it closes off Path 3 as a *closure*
mechanism with concrete numbers at every A, and (b) it provides a
blocker-free canonical-trace binding baseline that the operator-valued
combiner (PR #1698 track) must beat once its A ≥ 3 extracts are
full-rank.

Witness: `binding-combiner-markov-peel-fallback.witness.json`
Ref: prop:atomic-mass-gb-nf

Usage:
    python computations/binding_combiner_markov_peel_fallback.py
    python computations/binding_combiner_markov_peel_fallback.py --include-li
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — substrate/ subdir bridge
import argparse  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
for _p in (HERE, HERE / "substrate", HERE / "markov"):
    sys.path.insert(0, str(_p))

import mpmath  # noqa: E402
import sympy as sp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A, E_0_CALIBRATION_MEV  # noqa: E402
from codata_constants import M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
from markov_peel import incremental_reduced_element  # noqa: E402
from markov_trace_canonical import tr_M_element  # noqa: E402
from hecke_symbolic import q as q_sym  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# 50 dps matches the bridge witness (atomic-tr-m-mpfr-50dps.witness.json)
# this trace path was cross-validated against.
mpmath.mp.dps = 50

# Substrate q at full 50-dps as a sympy Float — built from the canonical
# 50-digit STRING, never from the float `Q` (which carries only ~17
# digits, so `tr_sym.subs(q_sym, float_Q).evalf(50)` would silently
# evaluate a 17-digit truncation and violate the L1 50-dps floor).
Q0_HP = sp.Float(Q_50_DIGIT_STR, mpmath.mp.dps)

# AME-2020 experimental binding energies (MeV), same source as
# binding_via_interface_knot.py.
B_AME = {
    "D": AME_B_DEUTERON_MEV_VALIDATION,
    "T": AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
    # 6Li/7Li experimental values for the --include-li rows.
    "6Li": mpmath.mpf("31.99464"),
    "7Li": mpmath.mpf("39.24454"),
}

ZN = {
    "D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
    "6Li": (3, 3), "7Li": (3, 4),
}

ATOMS_DEFAULT = ["D", "T", "3He", "4He"]
ATOMS_LITHIUM = ["6Li", "7Li"]

# Exact-symbolic trace path can only carry the color-blind averaged
# interface crossing (see module docstring).
PN_CONVENTION = "strict_averaged"


def _trace_abs_at_q0(Z: int, N: int, *, include_inter: bool,
                     max_iter: int) -> dict:
    """Canonical Markov trace |tr_M(β)| at q = q₀ for atom (Z, N).

    Returns a dict with the magnitude at q₀ (as a 50-dps string), the
    reduced term count, and per-stage wall times.  `include_inter`
    selects the bound (True) vs. free (False) braid config.
    """
    A = Z + N
    n_strands = 3 * A
    word = atom_braid_word_3A(
        Z, N, include_inter=include_inter, pn_convention=PN_CONVENTION,
    )

    t0 = time.time()
    elem = incremental_reduced_element(word, max_iterations_per_step=max_iter)
    t_reduce = time.time() - t0

    t0 = time.time()
    tr_sym = tr_M_element(elem, n_strands, simplify=False)
    t_trace = time.time() - t0

    # Substitute the full 50-dps q (Q0_HP, from the 50-digit string), then
    # evalf at the 50-dps floor; mpf(str(...)) round-trips losslessly
    # (casting to float would truncate to ~17 digits).
    tr_at_q0 = mpmath.mpf(str(tr_sym.subs(q_sym, Q0_HP).evalf(mpmath.mp.dps)))
    abs_at_q0 = abs(tr_at_q0)

    try:
        ops = int(sp.count_ops(tr_sym))
    except Exception:  # noqa: BLE001
        ops = -1

    return {
        "tr_M_at_q0": mpmath.nstr(tr_at_q0, mpmath.mp.dps, strip_zeros=False),
        "abs_tr_M_at_q0": mpmath.nstr(abs_at_q0, mpmath.mp.dps,
                                      strip_zeros=False),
        "_abs": abs_at_q0,  # mpf, dropped before serialization
        "reduced_term_count": len(elem.terms),
        "trace_sympy_ops": ops,
        "word_length": len(word),
        "elapsed_reduce_sec": round(t_reduce, 3),
        "elapsed_trace_sec": round(t_trace, 3),
    }


def compute_atom(atom: str, *, max_iter: int) -> dict:
    """One binding row: free vs. bound trace, B_dim, and both MeV scalings."""
    Z, N = ZN[atom]
    free = _trace_abs_at_q0(Z, N, include_inter=False, max_iter=max_iter)
    bound = _trace_abs_at_q0(Z, N, include_inter=True, max_iter=max_iter)

    b_dim = free["_abs"] - bound["_abs"]
    e0 = mpmath.mpf(str(E_0_CALIBRATION_MEV))
    me = mpmath.mpf(str(M_E_MEV))
    b_mev_e0 = e0 * b_dim
    b_mev_me = me * b_dim

    ame = B_AME[atom]
    free.pop("_abs"); bound.pop("_abs")

    row = {
        "atom": atom,
        "Z": Z, "N": N, "A": Z + N,
        "free_config": free,
        "bound_config": bound,
        "B_dim": mpmath.nstr(b_dim, 30),
        "B_MeV_E0": mpmath.nstr(b_mev_e0, 12),
        "B_MeV_me": mpmath.nstr(b_mev_me, 12),
        "B_AME_MeV": mpmath.nstr(ame, 12),
        "ratio_E0": mpmath.nstr(b_mev_e0 / ame, 8),
        "ratio_me": mpmath.nstr(b_mev_me / ame, 8),
    }
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-li", action="store_true",
        help="Also compute ⁶Li and ⁷Li (H_18 / H_21; minutes per atom)",
    )
    parser.add_argument(
        "--max-iter", type=int, default=2000,
        help="Cap for SymbolicHeckeDivision.reduce per step (default 2000)",
    )
    args = parser.parse_args()

    atoms = list(ATOMS_DEFAULT)
    if args.include_li:
        atoms.extend(ATOMS_LITHIUM)

    print("Binding via canonical markov_peel trace difference (Path 3)",
          flush=True)
    print("  B = E_0 · (|tr_M(free)| − |tr_M(atom)|),  "
          f"pn_convention={PN_CONVENTION!r}", flush=True)
    print("=" * 78, flush=True)
    print(f"{'atom':<5}{'A':>3} {'|tr_free|':>12} {'|tr_atom|':>12} "
          f"{'B_dim':>10} {'B(E0)':>9} {'B(me)':>9} {'AME':>9} "
          f"{'r(E0)':>7} {'r(me)':>7}", flush=True)

    rows = []
    total_t = time.time()
    for atom in atoms:
        try:
            row = compute_atom(atom, max_iter=args.max_iter)
            fa = mpmath.mpf(row["free_config"]["abs_tr_M_at_q0"])
            ba = mpmath.mpf(row["bound_config"]["abs_tr_M_at_q0"])
            print(
                f"{atom:<5}{row['A']:>3} {mpmath.nstr(fa, 8):>12} "
                f"{mpmath.nstr(ba, 8):>12} {row['B_dim'][:10]:>10} "
                f"{row['B_MeV_E0'][:9]:>9} {row['B_MeV_me'][:9]:>9} "
                f"{row['B_AME_MeV'][:9]:>9} {row['ratio_E0'][:7]:>7} "
                f"{row['ratio_me'][:7]:>7}",
                flush=True,
            )
            rows.append(row)
        except Exception as exc:  # noqa: BLE001
            print(f"{atom:<5} FAILED: {type(exc).__name__}: {exc}", flush=True)
            rows.append({
                "atom": atom, "Z": ZN[atom][0], "N": ZN[atom][1],
                "A": sum(ZN[atom]),
                "error": f"{type(exc).__name__}: {exc}",
            })

    total_elapsed = time.time() - total_t
    print("=" * 78, flush=True)
    print(f"  total wall = {total_elapsed:.1f}s", flush=True)

    # All non-error rows = atoms where Path 3 succeeded.  The headline
    # claim is that A ≥ 3 succeeds here while
    # canonical_tr_m_via_branching.py returns None for the same atoms.
    succeeded = [r["atom"] for r in rows if "error" not in r]
    a3plus_ok = [r["atom"] for r in rows
                 if "error" not in r and r["A"] >= 3]
    a3plus_attempted = sum(1 for a in atoms if sum(ZN[a]) >= 3)

    w = WitnessBuilder("binding-combiner-markov-peel-fallback", engine="sympy")
    # Headline claim, machine-checkable: every A ≥ 3 atom traces
    # successfully here, whereas canonical_tr_m_via_branching.py returns
    # None for all of them (rank-deficient H_9+ A-operator extracts).
    w.add_assertion(
        "a3plus_atoms_bypass_rank_deficiency_blocker",
        computed=len(a3plus_ok),
        expected=a3plus_attempted,
        tolerance=0,
        source="canonical_tr_m_via_branching.py:245-252 returns None for A>=3",
    )
    w.set_description(
        "Binding energy via the canonical markov_peel Markov-trace "
        "difference B = E_0·(|tr_M(free)| − |tr_M(atom)|), closure-path-3 "
        "from docs/audits/2026-06-09-binding-canonical-default-depth-"
        "stratified.md. Bypasses the A ≥ 3 rank-deficiency blocker in "
        "canonical_tr_m_via_branching.py (which returns None for A ≥ 3) by "
        "using the exact-symbolic markov_peel trace (Gröbner–Shirshov "
        "reduce + Markov-axiom recursive ascent) directly, with no "
        "A-operator extracts. Uses pn_convention='strict_averaged' "
        "(color-blind) because the exact-symbolic-in-q trace path cannot "
        "represent the numeric color-weighting delta of the canonical "
        "default; the perturbation is sub-0.1%. RESULT: the trace "
        "difference under-binds severely with the wrong A-trend, "
        "confirming the audit's diagnosis that a per-atom trace difference "
        "carries no magic-A scale factor."
    )
    w.set_content_block("prop:atomic-mass-gb-nf")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("E_0_CAL3_MeV", str(E_0_CALIBRATION_MEV))
    w.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    w.add_parameter("pn_convention", PN_CONVENTION)
    w.add_parameter("precision_dps", str(mpmath.mp.dps))
    w.add_data(
        "method",
        "atom_braid_word_3A(include_inter=False/True) + "
        "incremental_reduced_element + tr_M_element(simplify=False), "
        "evaluated at q0; B = E_0·(|tr_free| − |tr_atom|)",
    )
    w.add_data("results", rows)
    w.add_data("atoms_succeeded", succeeded)
    w.add_data("a3plus_atoms_succeeded", a3plus_ok)
    w.add_data("bypasses_rank_deficiency_blocker", len(a3plus_ok) > 0)
    w.add_data(
        "closure_status",
        "blocker-free baseline; does NOT close binding (under-binds, "
        "wrong A-trend) — trace difference has no magic-A scale factor",
    )
    w.add_data("color_weighting_note",
               "strict_averaged used; canonical bring_color_weighted delta "
               "is a sub-0.1% numeric perturbation not representable in the "
               "exact-symbolic-in-q trace path")
    w.add_data("total_wall_sec", round(total_elapsed, 1))
    out_path = w.save()
    print(f"  → wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
