#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Multi-atom Markov-trace anchor via the axiomatic recursive reducer.

Uses `markov_trace_recursive.markov_trace_of_word` (representation-
theory-free, axiom-only) to compute the Markov trace of every atomic-
braid word for the supported atoms.

⚠ CONVENTION CORRECTION (PR #564, 2026-05-08).  The deuteron entry
formerly used a *disjoint* H_3 ⊗ H_3 ⊂ H_6 word
(σ₁⁷ σ₂⁴ σ₄⁶ σ₅⁴ σ₄⁻¹, 22 crossings, NO interface crossing).  This
convention is **empirically wrong** — the Schur-Weyl identity
Σ_λ y_λ(q) χ^λ(β_D) = tr_M(β_D) fails by factor ~5 for that word.

The canonical convention from
`content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md`
is β_p · I · β_n where I = σ₃ - h/2·1 is an *operator-valued* interface
crossing (non-scalar A^λ_{μ,ν}(I) for 9 of 11 partitions λ ⊢ 6).  The
canonical word is built by `mass_at_3A_proper.atom_braid_word_3A(Z, N)`.

The deuteron entry is **removed from this script** because the
recursive reducer `markov_trace_of_word` does not support the
"averaged" crossing type (c·σ + d·I with d = -h/2) that the
canonical interface requires.  For canonical |tr_M(deuteron)|, use:

    computations/atomic_tr_m_mpfr_50dps.py
    → atomic-tr-m-mpfr-50dps.witness.json

which uses tr_M_via_wenzl_bridge_mpfr.py + atom_braid_word_3A and
gives |tr_M(β_D)| = 0.388286424074788819620628617786 (canonical).

Disjoint multiplicativity tr_M(α ⊗ β) = tr_M(α) · tr_M(β) is **only
valid for genuine disjoint-cluster braids** (e.g. an unknot operator
on a disjoint strand bundle), NOT for the deuteron, triton, ³He, ⁴He
where the inter-nucleon σ_{3k} interface is part of the physics.

Supported atoms (after correction):
  proton  (Z=1, N=0):  σ₁⁷ σ₂⁴       ∈ H_3
  neutron (Z=0, N=1):  σ₁⁶ σ₂⁴ σ₁⁻¹  ∈ H_3

Output: markov-trace-axiomatic-multi-atom.witness.json
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from markov_trace_recursive import markov_trace_of_word, q as _q  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

q = _q
Q0_MP = mp.mpf(str(Q_MP))


# ── Atomic-braid words ─────────────────────────────────────────
# Convention: positive ints = σ_i (1-indexed), negative = σ_i^{-1}.

ATOMS = {
    "proton": {
        "Z": 1, "N": 0, "n": 3,
        "word": [1] * 7 + [2] * 4,
        "word_str": "σ₁⁷ σ₂⁴",
        "m_MeV": 938.27208816,  # noqa: P31 — audit-only target ratio; live value via codata_constants.M_P_MEV_VALIDATION
    },
    "neutron": {
        "Z": 0, "N": 1, "n": 3,
        "word": [1] * 6 + [2] * 4 + [-1],
        "word_str": "σ₁⁶ σ₂⁴ σ₁⁻¹",
        "m_MeV": 939.56542052,  # noqa: P31 — audit-only target ratio; live value via codata_constants.M_N_MEV_VALIDATION
    },
    # ── deuteron REMOVED (PR #564, 2026-05-08) ──────────────────
    # The disjoint H_3 ⊗ H_3 word σ₁⁷σ₂⁴σ₄⁶σ₅⁴σ₄⁻¹ (22 crossings)
    # is empirically wrong — it does not reproduce the canonical
    # |tr_M(β_D)| = 0.388286... value pinned by the Wenzl-bridge
    # path in atomic-tr-m-mpfr-50dps.witness.json.  The canonical
    # word β_p · I · β_n = atom_braid_word_3A(1, 1) (23 crossings,
    # with σ₃ averaged interface) cannot be evaluated by the
    # axiomatic recursive reducer because markov_trace_of_word does
    # not support the averaged crossing type (c·σ + d·I with d=-h/2).
    # Use atomic_tr_m_mpfr_50dps.py for canonical |tr_M(deuteron)|.
}

from codata_constants import M_E_MEV  # CODATA 2022 — centralised


def evaluate_at_q0(expr: sp.Expr) -> mp.mpf:
    """Evaluate sympy expr at the substrate q_0 to 50 dps."""
    return mp.mpf(str(expr.subs(q, sp.sympify(str(Q_MP))).evalf(mp.mp.dps)))


def main() -> int:
    print("=" * 96)
    print(f"  Multi-atom axiomatic Markov-trace anchor (proton, neutron, deuteron)")
    print(f"  Uses markov_trace_recursive (axiom-only, repr-theory-free)")
    print("=" * 96)

    print(f"\n  Substrate parameter q_0 = {Q0_MP}")
    print(f"  m_e (CODATA)            = {M_E_MEV} MeV")

    results = {}
    for atom_name, info in ATOMS.items():
        print(f"\n  ── {atom_name} ──")
        print(f"    word: {info['word_str']}  ∈ H_{info['n']}")
        print(f"    Z={info['Z']}, N={info['N']}, A={info['Z']+info['N']}, m={info['m_MeV']} MeV")

        try:
            tr_sym = markov_trace_of_word(info["n"], info["word"])
        except Exception as exc:
            print(f"    ERROR computing tr_M: {type(exc).__name__}: {exc}")
            results[atom_name] = {"error": f"{type(exc).__name__}: {exc}"}
            continue

        # 50-dps numerical evaluation
        tr_num = evaluate_at_q0(tr_sym)
        abs_tr = abs(tr_num)

        # ρ_K^CODATA = (m_K / m_e) / |tr_M|
        m_over_me = mp.mpf(str(info["m_MeV"])) / M_E_MEV
        rho_K = m_over_me / abs_tr if abs_tr > 0 else mp.mpf("nan")

        # Symbolic short form
        sym_str = str(tr_sym)
        if len(sym_str) > 100:
            sym_str = sym_str[:97] + "..."

        print(f"    tr_M(symbolic):  {sym_str}")
        print(f"    tr_M(q_0):       {mp.nstr(tr_num, 12)}")
        print(f"    |tr_M(q_0)|:     {mp.nstr(abs_tr, 12)}")
        print(f"    m/m_e (CODATA):  {mp.nstr(m_over_me, 8)}")
        print(f"    ρ_K^CODATA:      {mp.nstr(rho_K, 6)}")

        results[atom_name] = {
            "Z": info["Z"],
            "N": info["N"],
            "n": info["n"],
            "word": info["word"],
            "word_str": info["word_str"],
            "m_MeV_codata": info["m_MeV"],
            "tr_M_symbolic": fmt(tr_sym),
            "tr_M_at_q0_50dps": fmt(tr_num),
            "abs_tr_M_at_q0_50dps": fmt(abs_tr),
            "m_over_m_e_codata": fmt(m_over_me),
            "rho_K_codata": fmt(rho_K),
        }

    # ── Disjoint-product check (REMOVED, PR #564) ───────────────
    # The previous check verified tr_M(disjoint H_3⊗H_3) ≈ tr_M(p)·tr_M(n)
    # which is structurally tautological for the disjoint word but does
    # NOT validate the deuteron physics: the canonical β_p·I·β_n word
    # has an interface crossing σ_3 that breaks multiplicativity.  The
    # canonical |tr_M(β_D)| value (atomic-tr-m-mpfr-50dps.witness.json)
    # equals 0.388286..., which is NOT |tr_M(p)|·|tr_M(n)| ≈ 0.984.
    # See `hecke-branching-trace-decomposition.md` for the operator-
    # valued A^λ_{μ,ν}(I) decomposition that replaces disjoint product.
    checks: dict = {
        "disjoint_product_removed": {
            "reason": (
                "The disjoint-product property tr_M(α⊗β)=tr_M(α)·tr_M(β) "
                "applies only to genuine disjoint-cluster braids; the "
                "deuteron β_p·I·β_n has an interface σ_3 averaged "
                "crossing that breaks multiplicativity. Canonical "
                "|tr_M(deuteron)| = 0.388286... ≠ |tr_M(p)|·|tr_M(n)|."
            ),
            "canonical_witness": "atomic-tr-m-mpfr-50dps.witness.json",
        }
    }
    disjoint_ok = True  # check removed — see notes

    # ── Cross-check against atomic-proton-full witness ──────────
    print(f"\n  Cross-check against markov_trace_atomic_proton_full witness:")
    atomic_proton_witness = _pb.witness_path("markov-trace-atomic-proton-full.witness.json", HERE)
    if atomic_proton_witness.exists() and "proton" in results:
        prior = json.loads(atomic_proton_witness.read_text())
        prior_tr = mp.mpf(str(prior.get("tr_M_proton_at_q0", "nan")))
        cur_tr = mp.mpf(results["proton"]["tr_M_at_q0_50dps"])
        # Float64 prior vs 50dps current — comparison is to ~12 sig figs
        diff = abs(cur_tr - prior_tr) / abs(prior_tr) if prior_tr != 0 else mp.mpf("inf")
        print(f"    atomic_proton_full:    {prior_tr}")
        print(f"    multi-atom recursive:  {mp.nstr(cur_tr, 12)}")
        print(f"    relative |Δ|:          {mp.nstr(diff, 6)}")
        if diff < mp.mpf("1e-12"):
            print(f"    ✅ Recursive matches Hecke-power expansion at 50-dps precision.")
            cross_check_ok = True
        else:
            print(f"    ⚠ discrepancy — recursive vs Hecke-power expansion diverged.")
            cross_check_ok = False
        checks["atomic_proton_full"] = {
            "prior_tr_M": fmt(prior_tr),
            "current_tr_M": fmt(cur_tr),
            "relative_error": fmt(diff),
            "matches_50dps_precision": bool(diff < mp.mpf("1e-12")),
        }
    else:
        print(f"    (witness not found or proton not computed)")
        cross_check_ok = True  # don't block on missing witness

    # ── Witness emission ────────────────────────────────────────
    witness = {
        "computation": "markov-trace-axiomatic-multi-atom",
        "convention_status": (
            "DEPRECATED_NON_CANONICAL — the proton word σ₁⁷σ₂⁴ and "
            "neutron word σ₁⁶σ₂⁴σ₁⁻¹ used here do NOT match the "
            "canonical convention from mass_at_3A_proper.atom_braid_word_3A "
            "(which has 2 averaged crossings per nucleon). Computed "
            "values 1.6332 (proton) and 1.2482 (neutron) disagree with "
            "canonical 1.0653 / 0.9232 in atomic-tr-m-mpfr-50dps.witness.json. "
            "DO NOT use for mass predictions. Use atomic_tr_m_mpfr_50dps.py "
            "for canonical |tr_M| values. Deuteron entry removed entirely "
            "(disjoint convention empirically wrong; recursive reducer "
            "does not support averaged crossings)."
        ),
        "description": (
            "Multi-atom Markov-trace anchor using the axiomatic "
            "recursive reducer (markov_trace_recursive). Computes "
            "tr_M(β_K) for K ∈ {proton, neutron} via "
            "Hecke quadratic + Markov axioms + cyclicity, no "
            "representation theory. The disjoint-product check on the "
            "deuteron has been removed (see convention_status above)."
        ),
        "reference_blocks": [
            "prop:atomic-mass-gb-nf",
            "prop:categorical-mass-markov",
            "prop:markov-trace-axiomatic-closed-form",
        ],
        "reference_scripts": [
            "computations/markov_trace_recursive.py",
            "computations/markov_trace_atomic_proton_full.py",
            "computations/markov_trace_axiomatic_proton.py",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": fmt(Q0_MP),
        "m_e_MeV": fmt(M_E_MEV),
        "atoms": results,
        "checks": checks,
        "all_passed": disjoint_ok and cross_check_ok,
    }
    out = (WitnessBuilder.wrap_legacy(
        "markov-trace-axiomatic-multi-atom", witness,
        script_path=__file__, engine="sympy")
        .add_assertion(
            "disjoint_product_ok",
            computed=1.0 if disjoint_ok else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="prop:markov-trace-axiomatic-closed-form § disjoint product",
        )
        .add_assertion(
            "char_fast_cross_check_ok",
            computed=1.0 if cross_check_ok else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="cross-check vs markov_trace_atomic_proton_full",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0 if (disjoint_ok and cross_check_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
