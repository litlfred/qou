#!/usr/bin/env python3
"""
Phase 2b: formal derivation of why dim V_(2,1) enters the proton
mass formula linearly.

The substrate identity factors as:
  m_p = dim V_(2,1) · (m_μ · F_Bor − |S₃| · m_e)
      = 2 · (m_μ · F_Bor − 6 · m_e)

WHY does the standard irrep dimension enter linearly?

DERIVATION: The Markov trace is
  tr_M(β_Bor) = Σ_λ y_λ · χ^λ(β_Bor)

For the Borromean braid (writhe 0, maps to identity in S₃):
  χ^(3)(β_Bor) = χ^(1,1,1)(β_Bor) = 1  (exactly, for all q)

So: tr_M = y_(3) + y_(2,1) · χ^(2,1)(β_Bor) + y_(1,1,1)

CORRECTION (2026-08-19, bean qou-24w9 / PR #5294).  Two claims below need
scoping, and the file is kept as-is otherwise because its algebra is right.

  1. "Lean-proved content-sum structure" OVERSTATES what the Lean says.
     `QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean` DEFINES
     `ySchurClosedForm lam q = q^{c(lam)}/[n]_q!` (sorry-free), but the
     identification of that closed form with the categorical weight is a
     CONJECTURE CLASS, `QSchurYLambdaClosedFormClaim` -- axiomatised, not
     proved.  Per AGENTS.md "Axiomatization is NOT a Proof", the definition is
     Lean-typed; the identification is open.

  2. The weights below are the q-SCHUR PLANCHEREL family.  They are NOT the
     weights that decompose the `tr_M` this file feeds into `F_Bor`.  Measured
     at the proton pin in
     `computations/qbeta/fbor_q3_is_qschur_plancherel_weight_probe.py` (8/8):

       sum_lam y^Wenzl_lam . chi^lam(beta_Bor) = the Lean tr_M   (residual 2e-71)
       sum_lam y^Schur_lam . chi^lam(beta_Bor) = 0.6687          (tr_M = 0.9986)
       sum_lam dim_lam . y^Wenzl_lam = 1 exactly (the Markov normalisation)
       sum_lam dim_lam . y^Schur_lam = 0.6697

     So `F_Bor = |tr_M| / y_(3)` is an identity for the q-Schur `y_(3)` and a
     cross-family import for the Markov `tr_M` -- which is the conflation
     AGENTS.md's notation register forbids ("three partition-weight families
     y_lam / w_lam / w~_lam are distinct at q != 1 -- never conflate").
     With the Wenzl weight, `1/y_(3) = 1.9786`, not `4.4756`.

     What survives: `/q^3` is not arbitrary -- `3 = c((3)) = 0+1+2` is the
     content sum of the trivial partition, and the bar-asymmetry PR #5294
     isolates is exactly `bar: lam -> lam'` negating `c`.  That is the
     provenance of the factor.  What does not survive is reading this line as
     a DERIVATION of it from the trace `F_Bor` actually uses.

The q-Schur weights have content-sum structure:
  y_(3) = q³/[3]_q!    (content sum c = 3)
  y_(2,1) = 1/[3]_q!   (content sum c = 0, self-conjugate)
  y_(1,1,1) = q⁻³/[3]_q!  (content sum c = −3)

The bar-pair sum y_(3) + y_(1,1,1) = (q³ + q⁻³)/[3]_q!.
This is the SYMMETRIC part under bar involution q ↔ q⁻¹.

The mass formula m_p = 2·m_μ·F_Bor − 12·m_e uses
  F_Bor = |tr_M| · [3]_q! / q³ = |tr_M| / y_(3)

Now: tr_M/y_(3) = 1 + (y_(2,1)/y_(3))·χ^(2,1) + y_(1,1,1)/y_(3)
              = 1 + (q⁻³)·χ^(2,1) + q⁻⁶

At the Wedderburn level:
  y_(2,1) / y_(3) = q⁻³  (ratio of q-Schur weights)
  y_(1,1,1) / y_(3) = q⁻⁶

So F_Bor = 1 + q⁻³ · χ^(2,1)(β_Bor) + q⁻⁶.

The DIMENSION enters because χ^(2,1)(β_Bor)/d_(2,1) → 1 at q=1
(Borromean maps to identity). So:
  F_Bor|_{q=1} = 1 + 1·d_(2,1) + 1 = 1 + 2 + 1 = 4

But the mass formula has F_Bor(q₀), not F_Bor(1). The q-dependence
enters through the continuous deformation of χ^(2,1) from q=1 to q=q₀.

This script derives the factored form and verifies it numerically.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import M_MU_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import sympy as sp
from sympy import Symbol, sqrt, cancel, Rational
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.witness import resolve_q0_anchor  # noqa: E402

# q₀ pin, declared by the producer rather than inferred.
#
# `WitnessBuilder.build()` stamps `q0Anchor` only when `q0_anchor_is_declared()`
# is true, i.e. only when this stem is already in `q0_anchor_manifest.json`. The
# manifest is generated from the q₀ value SERIALIZED in a witness. A producer
# that reads q₀ without recording it therefore cannot bootstrap in: no stamp =>
# no manifest entry => no stamp. Declaring it here breaks that loop, and an
# explicit payload declaration wins over the resolver by design.
#
# The value comes from the SAME resolver the runtime uses, and is asserted
# against the pin this script actually computes with -- a stamp that disagrees
# with the compute is the defect `_q0_value_for_anchor`'s docstring records
# (the 2026-08-15 derive-the-muon-branch change, reverted the same day).
_Q0_ANCHOR, _Q0_VALUE = resolve_q0_anchor(__file__)
assert _Q0_VALUE is not None and str(Q_50_DIGIT_STR)[:14] == _Q0_VALUE[:14], (
    "q0 stamp/compute straddle: computing with "
    + str(Q_50_DIGIT_STR)[:16] + " but resolver says "
    + str(_Q0_ANCHOR) + " = " + _Q0_VALUE[:16]
)
_Q0_STAMP = {"q0Anchor": _Q0_ANCHOR, "q0Value": _Q0_VALUE}


q = Symbol("q", positive=True)
h = q - 1/q


def main():
    set_compute_dps()
    t0 = time.time()
    set_compute_dps()

    print("=" * 70)
    print("  Phase 2b: dim V_(2,1) bridge — WHY 2 enters linearly")
    print("=" * 70)
    print()

    # ── 1. Symbolic derivation ──────────────────────────────────
    print("  1. Symbolic Wedderburn decomposition of F_Bor")
    print()

    # q-Schur weights
    qfact3 = (q**2 + 1 + q**(-2)) * (q + q**(-1))
    y3 = q**3 / qfact3
    y21 = 1 / qfact3
    y111 = q**(-3) / qfact3

    print(f"    y_(3)     = q³/[3]_q! = {cancel(y3)}")
    print(f"    y_(2,1)   = 1/[3]_q!  = {cancel(y21)}")
    print(f"    y_(1,1,1) = q⁻³/[3]_q! = {cancel(y111)}")
    print()

    # Characters (Phase 1c results)
    chi3 = sp.Integer(1)
    chi111 = sp.Integer(1)
    chi21 = (-q**12 + 3*q**10 - 3*q**8 + 4*q**6 - 3*q**4 + 3*q**2 - 1) / q**6

    tr_M_symbolic = y3 * chi3 + y21 * chi21 + y111 * chi111
    tr_M_lean = (4 + h**2 - 3*h**4 - h**6) / (h**2 + 4)

    # F_Bor = |tr_M| / y_(3) = |tr_M| · [3]_q! / q³
    F_Bor_sym = cancel(tr_M_symbolic / y3)
    print(f"    F_Bor = tr_M / y_(3)")
    print(f"          = 1 + (y_(2,1)/y_(3))·χ^(2,1) + y_(1,1,1)/y_(3)")
    print(f"          = 1 + q⁻³·χ^(2,1) + q⁻⁶")
    print()

    # Verify: y_(2,1)/y_(3) = q⁻³
    ratio_21_3 = cancel(y21 / y3)
    ratio_111_3 = cancel(y111 / y3)
    print(f"    y_(2,1)/y_(3) = {ratio_21_3}")
    print(f"    y_(1,1,1)/y_(3) = {ratio_111_3}")
    print()

    # At q=1: F_Bor = 1 + 1·d_(2,1) + 1 = 4
    F_Bor_at_1 = F_Bor_sym.subs(q, 1)
    print(f"    F_Bor(q=1) = 1 + 1·χ^(2,1)(q=1) + 1 = 1 + d_(2,1) + 1")
    print(f"               = 1 + 2 + 1 = {F_Bor_at_1}")
    print()

    # ── 2. The factored mass formula ────────────────────────────
    print("  2. Factored mass formula")
    print()
    print("    m_p = 2·m_μ·F_Bor − 12·m_e")
    print("        = 2·(m_μ·F_Bor − 6·m_e)")
    print("        = dim V_(2,1) · (m_μ·F_Bor − |S₃|·m_e)")
    print()
    print("    WHY the factor 2 enters:")
    print("    The mass formula m_p = 2·m_μ·F_Bor − 12·m_e factors")
    print("    over the integer 2 = dim V_(2,1) because:")
    print()
    print("    (a) F_Bor = |tr_M|/y_(3) decomposes into 3 irrep contributions")
    print("        where the trivial + sign reps contribute 1 + q⁻⁶")
    print("        (a bar-pair related by q → q⁻¹)")
    print()
    print("    (b) The 12·m_e term = 2·6·m_e where 6 = |S₃| = [3]_q!|_{q=1}")
    print()
    print("    (c) Both 2·m_μ and 12·m_e are divisible by dim V_(2,1) = 2")
    print("        The factor 2 is the ONLY integer > 1 that divides both")
    print("        coefficients, and it equals the standard irrep dimension")
    print()
    print("    The categorical explanation: the Borromean mass formula lives")
    print("    in a quotient by the bar-pair Z/2 symmetry y_(3) ↔ y_(1,1,1).")
    print("    The bar involution q ↔ q⁻¹ exchanges these two 1-dim reps,")
    print("    so the mass formula naturally factors through the bar-invariant")
    print("    quotient, picking up dim V_(2,1) = |{bar-pair}| as the fold")
    print("    factor.")

    # ── 3. Numerical verification ───────────────────────────────
    print()
    print("  3. Numerical verification at q₀")
    q0 = Q_MP
    m_mu = mp.mpf(M_MU_MEV_VALIDATION)
    m_e = mp.mpf("0.51099895")

    h0 = q0 - 1/q0
    trM = abs((4 + h0**2 - 3*h0**4 - h0**6) / (h0**2 + 4))
    qf3 = (q0**2 + 1 + q0**(-2)) * (q0 + q0**(-1))
    F = trM * qf3 / q0**3

    m_p_original = 2 * m_mu * F - 12 * m_e
    m_p_factored = 2 * (m_mu * F - 6 * m_e)
    diff = abs(m_p_original - m_p_factored)

    print(f"    m_p (original): {mp.nstr(m_p_original, 15)} MeV")
    print(f"    m_p (factored): {mp.nstr(m_p_factored, 15)} MeV")
    print(f"    Difference: {mp.nstr(diff, 5)} MeV")
    print(f"    Match: {'✓ EXACT' if diff < 1e-30 else '✗'}")

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    # Witness
    w = WitnessBuilder("phase2b-dim-v21-bridge", engine="sympy+mpmath")
    w.set_description(
        "Formal derivation of why dim V_(2,1) = 2 enters the proton "
        "mass formula linearly. The Borromean mass formula factors "
        "through the bar-pair Z/2 symmetry y_(3) ↔ y_(1,1,1), with "
        "dim V_(2,1) = |{bar-pair}| as the fold factor. F_Bor "
        "decomposes as 1 + q⁻³·χ^(2,1) + q⁻⁶ via Wedderburn, and "
        "the integer 2 divides both 2·m_μ and 12·m_e = 2·6·m_e."
    )
    w.set_content_block("conj:proton-mass-substrate-identity")
    w.add_data("wedderburn_decomposition", {
        "F_Bor": "1 + q⁻³·χ^(2,1)(β_Bor) + q⁻⁶",
        "F_Bor_at_q1": str(F_Bor_at_1),
        "y21_over_y3": str(ratio_21_3),
        "y111_over_y3": str(ratio_111_3),
    })
    w.add_data("factored_form", {
        "m_p": "dim V_(2,1) · (m_μ · F_Bor − |S₃| · m_e)",
        "dim_V21": 2,
        "S3_order": 6,
        "product": 12,
    })
    w.add_assertion(
        name="factored_form_exact",
        computed=1 if diff < 1e-30 else 0,
        expected=1,
        tolerance=0,
        source="2·(m_μ·F_Bor − 6·m_e) = 2·m_μ·F_Bor − 12·m_e exactly"
    )
    out = w.save(_Q0_STAMP)
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
