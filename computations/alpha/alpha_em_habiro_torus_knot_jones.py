#!/usr/bin/env python3
"""
alpha_em_habiro_torus_knot_jones.py — option (1) Habiro-at-roots-of-unity
for α_EM: test the EXACT closed-form Jones polynomials of T(2,9) and
T(3,5) (the Habiro element at generic q) against the framework's
[9]_q·[10]_q ansatz, then add the Bring zero-mode shift and compare to
CODATA. (Derive-or-refute; no fit.)

CONTEXT. After option (2) (`alpha_em_categorical_reidentification.py`):
 - Tree A:  q·[9]_q·[10]_q                = 136.8232    (−1552.7 ppm)
 - +Bring shift 2/(3π):                   = 137.03543   (−4.18 ppm)
 - +tentative α/(4π) (CODATA comparator): = 137.03601   (+57 ppb)

The remaining ~57 ppb is the OPEN derived form for the next-order term.
The Habiro element gives the canonical closed-form quantum invariant of
each torus knot. Evaluating it at q₀ tests whether [n]_q is even the
right tree quantum object, or if the proper Jones polynomial differs.

CLOSED-FORM JONES POLYNOMIALS (standard torus-knot formula):
   V(T(p,k))(t) = t^{(p-1)(k-1)/2} · (1 − t^{p+1} − t^{k+1} + t^{p+k}) / (1 − t²)

WHAT THIS PROBE DOES (derive-or-refute):
   1. Evaluate V(T(2,9))(q₀) and V(T(3,5))(q₀) exactly at the substrate q₀.
   2. Compare to [9]_q, [10]_q.
   3. Test α_EM⁻¹ candidates built from full Jones (with and without Bring
      shift) against CODATA.
   4. Honest: does the Habiro / full-Jones identification improve over
      [n]_q? If yes — that's the next-layer derivation. If no — the
      [n]_q identification stands and the residual lives elsewhere.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf, pi

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def jones_torus(p: int, k: int, t):
    """V(T(p,k))(t) closed-form (standard torus-knot Jones polynomial)."""
    pre = t ** ((p - 1) * (k - 1) // 2 if ((p - 1) * (k - 1)) % 2 == 0
                else mpf((p - 1) * (k - 1)) / 2)
    num = 1 - t ** (p + 1) - t ** (k + 1) + t ** (p + k)
    den = 1 - t ** 2
    return pre * num / den


def main():
    set_compute_dps()
    wb = WitnessBuilder("alpha-em-habiro-torus-knot-jones", engine="mpmath")

    q = Q_MP
    qbra = lambda n: (q**n - q**(-n)) / (q - q**(-1))  # noqa: E731

    CODATA_alpha_inv = mpf("137.035999084")

    # ─── q-brackets (tree ansatz factors) ────────────────────────────────
    bra9, bra10 = qbra(9), qbra(10)
    tree = q * bra9 * bra10

    # ─── Bring zero-mode shift at g = 4 ─────────────────────────────────
    bring_shift = mpf(8) / (12 * pi)   # 2g/(4π(g-1)) at g=4 = 2/(3π)

    # ─── Exact closed-form Jones polynomials at t = q₀ ──────────────────
    V_T29 = jones_torus(2, 9, q)
    V_T35 = jones_torus(3, 5, q)

    # ─── α_EM⁻¹ candidates ──────────────────────────────────────────────
    # Note: framework's α⁻¹ = q·[9]_q·[10]_q means the per-knot factor
    # corresponds to α_shift, not to V_K directly. We test multiple
    # plausible identifications honestly:
    candidates = {
        "(A) q·[9]_q·[10]_q  (framework tree)":
            q * bra9 * bra10,
        "(B) q·V(T29)·V(T35)  (full Jones product)":
            q * V_T29 * V_T35,
        "(C) q·|V(T29)·V(T35)|  (abs Jones product)":
            q * abs(V_T29 * V_T35),
        "(D) q·[9]_q·V(T35)  (mixed: [n]_q for T29, full V for T35)":
            q * bra9 * V_T35,
        "(E) q·V(T29)·[10]_q  (mixed: full V for T29, [n]_q for T35)":
            q * V_T29 * bra10,
    }

    print("=" * 72)
    print(" α_EM⁻¹ HABIRO / FULL-JONES candidates  vs  CODATA 137.035999084")
    print("=" * 72)
    print(f"  q₀ = {float(q):.14f}")
    print(f"  [9]_q  = {float(bra9):.8f}    V(T(2,9))(q₀) = {float(V_T29):.8f}")
    print(f"  [10]_q = {float(bra10):.8f}    V(T(3,5))(q₀) = {float(V_T35):.8f}")
    print(f"  Bring shift 2/(3π) = {float(bring_shift):.10f}")
    print()
    print(f"  {'identification':52s} {'α⁻¹':>12s} {'no-shift Δ':>12s} {'+Bring Δ':>12s}")
    results = {}
    for name, alpha_inv in candidates.items():
        err_noshift_ppm = float((alpha_inv - CODATA_alpha_inv) / CODATA_alpha_inv * 1e6)
        with_shift = alpha_inv + bring_shift
        err_shift_ppm = float((with_shift - CODATA_alpha_inv) / CODATA_alpha_inv * 1e6)
        results[name] = {
            "alpha_inv": mp.nstr(alpha_inv, 12),
            "alpha_inv_plus_bring": mp.nstr(with_shift, 12),
            "err_no_shift_ppm": err_noshift_ppm,
            "err_with_bring_ppm": err_shift_ppm,
        }
        print(f"  {name:52s} {float(alpha_inv):>12.6f} "
              f"{err_noshift_ppm:>+10.2f} ppm {err_shift_ppm:>+10.4f} ppm")

    # ─── Honest read ────────────────────────────────────────────────────
    best_no_shift = min(results, key=lambda k: abs(results[k]["err_no_shift_ppm"]))
    best_with_shift = min(results, key=lambda k: abs(results[k]["err_with_bring_ppm"]))
    print()
    print(f"Best (no Bring shift)     : {best_no_shift}")
    print(f"  → {results[best_no_shift]['err_no_shift_ppm']:+.2f} ppm")
    print(f"Best (+Bring shift)       : {best_with_shift}")
    print(f"  → {results[best_with_shift]['err_with_bring_ppm']:+.4f} ppm")
    print()
    print("Interpretation:")
    print("  • If (B) full-Jones product matches CODATA better than (A) [n]_q,")
    print("    the Habiro/Jones identification IS the canonical α_EM tree.")
    print("  • If (A) [n]_q wins, the framework's identification is the right")
    print("    quantum object (q-bracket = q-quantum-dim of fundamental rep,")
    print("    not full Jones polynomial).")
    print("  • The Bring shift is additive on top of EITHER; it's a separate")
    print("    structural correction (Hodge / Gauss-Bonnet), not a Jones term.")
    print()
    print("Honest derive-or-refute conclusion in witness.")

    # ── Witness ──────────────────────────────────────────────────────────
    wb.set_description(
        "Option (1): Habiro-at-roots-of-unity for α_EM. Tests whether the "
        "EXACT closed-form Jones polynomials of T(2,9) and T(3,5) (the "
        "Habiro element at generic q) outperform the framework's [9]_q·[10]_q "
        "tree ansatz. Includes five candidate identifications + Bring zero-"
        "mode shift comparison. No fit; closed-form Jones from standard "
        "torus-knot formula V(T(p,k))(t) = t^((p-1)(k-1)/2)·(1−t^(p+1)−"
        "t^(k+1)+t^(p+k))/(1−t²)."
    )
    wb.add_data("inputs", {
        "q0": mp.nstr(q, 30),
        "CODATA_alpha_inv": "137.035999084",
        "Bring_shift_2_over_3pi": mp.nstr(bring_shift, 14),
    })
    wb.add_data("q_brackets", {
        "[9]_q": mp.nstr(bra9, 12),
        "[10]_q": mp.nstr(bra10, 12),
    })
    wb.add_data("full_jones_at_q0", {
        "V_T29_jones": mp.nstr(V_T29, 12),
        "V_T35_jones": mp.nstr(V_T35, 12),
    })
    wb.add_data("candidates_vs_CODATA", results)
    wb.add_data("best", {
        "no_shift": {"id": best_no_shift,
                     "residual_ppm": results[best_no_shift]["err_no_shift_ppm"]},
        "with_bring_shift": {"id": best_with_shift,
                             "residual_ppm": results[best_with_shift]["err_with_bring_ppm"]},
    })
    wb.add_assertion(
        "all_five_candidates_evaluated",
        computed=len(results),
        expected=5,
        tolerance=0,
        source="Five α_EM⁻¹ identifications evaluated against CODATA at "
               "q₀ (50 dps): framework tree, full-Jones product, abs Jones, "
               "and two mixed identifications.",
    )
    wb.save()


if __name__ == "__main__":
    main()
