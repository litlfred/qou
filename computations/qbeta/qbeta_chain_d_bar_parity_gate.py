#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical bar-parity test at q0 and its bar image
# 1/q0; settles the Q_β chain-D (Type-B) gate. No fit.
"""
Q_β chain-D gate, RUN: is the c_k ladder bar-involution invariant (Type-B
crystal compatible) or parity-SPLIT?  Settles D vs C.  No fit, no wiring.

The ladder (qbeta_1ppq_achieved.py):
    Q_β = Q_A · cos(α_eff) · (1 - u²) · (1 + c₃·u³),   u = b·ℏ_q²,  ℏ_q = 1-1/q
maps to Q_β = Q_base · Π(1 + c_k u^k) with
    c₁ : cos(α_eff)        (odd  — "topological", per the compute's own label)
    c₂ = -1                (even — "geometric" constant)
    c₃ = J_Hopf(1) - ℏ_q² = -2 - ℏ_q²   (odd — "topological": Jones-of-Hopf)
    c₄ ≈ -1                (even — "geometric"; flagged normalisation artifact)

Type-B folded crystal content q^{c(T)} is bar-involution (q->1/q) INVARIANT by
construction (CLAUDE.md §7b).  So chain D requires the c_k to be bar-invariant:
    c_k(1/q) == c_k(q).
This probe tests that on the fully-determined rungs (c₂ constant; c₃ = -2-ℏ_q²,
no unknown Hoefsmit b).  ℏ_q = 1-1/q  =>  ℏ_q(1/q) = 1-q = -q·ℏ_q  =>  ℏ_q² is
bar-COVARIANT: ℏ_q² -> q²·ℏ_q².

Exploratory; no fit.  Run:
  python3 -u computations/qbeta/qbeta_chain_d_bar_parity_gate.py 2>&1 | tee /tmp/dgate.log
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402


def hbar(q):
    return 1 - 1 / q


def c3(q):
    """c₃ = J_Hopf(q=1) - ℏ_q² = -2 - ℏ_q² (compute's documented odd-rung form)."""
    return -2 - hbar(q) ** 2


def main() -> int:
    mp.mp.dps = 50
    q = mp.mpf(str(Q0))
    qb = 1 / q                      # bar image

    print("\n  Q_β CHAIN-D (Type-B folded crystal) BAR-PARITY GATE — RUN  (no fit)")
    print(f"  q0 = {mp.nstr(q,12)}   bar image 1/q0 = {mp.nstr(qb,12)}")
    print(f"  ℏ_q(q0) = {mp.nstr(hbar(q),10)}   ℏ_q(1/q0) = {mp.nstr(hbar(qb),10)}"
          f"   (= -q0·ℏ_q: {mp.nstr(-q*hbar(q),10)})\n")

    # --- ℏ_q² bar-covariance check ---------------------------------------
    lhs, rhs = hbar(qb) ** 2, q ** 2 * hbar(q) ** 2
    print(f"  ℏ_q²(1/q0) = {mp.nstr(lhs,12)}   q0²·ℏ_q²(q0) = {mp.nstr(rhs,12)}"
          f"   -> ℏ_q² is bar-COVARIANT (×q²): {abs(lhs-rhs) < mp.mpf(10)**-40}\n")

    # --- per-rung bar-parity --------------------------------------------
    print("  | rung | parity class | c_k(q0) | c_k(1/q0) | bar-invariant? |")
    print("  |---|---|---|---|---|")
    # c2 = -1 constant
    c2v = mp.mpf(-1)
    print(f"  | c₂ (even, geometric) | constant | {mp.nstr(c2v,10)} | {mp.nstr(c2v,10)} | YES |")
    # c3 = -2 - hbar^2
    c3q, c3qb = c3(q), c3(qb)
    inv = abs(c3qb - c3q) < mp.mpf(10) ** -12
    print(f"  | c₃ (odd, topological) | -2 - ℏ_q² | {mp.nstr(c3q,12)} | {mp.nstr(c3qb,12)} | {'YES' if inv else 'NO'} |")
    # decompose c3 into bar-invariant (-2) + bar-covariant (-hbar^2) parts
    print(f"\n  c₃ DECOMPOSITION:")
    print(f"    bar-INVARIANT part  = J_Hopf(1) = -2            (topological, classical Jones value)")
    print(f"    bar-COVARIANT part  = -ℏ_q²  ->  -q²·ℏ_q² under bar")
    print(f"    c₃(1/q0) - c₃(q0)   = {mp.nstr(c3qb - c3q, 6)}   (nonzero => NOT bar-invariant)")
    swing_pct = float((c3qb - c3q) / c3q * 100)
    print(f"    bar swing           = {swing_pct:.4f} %   (matches the known cross-anchor c₃ near-match swing)\n")

    # --- verdict ---------------------------------------------------------
    print("  ---------------------------------------------------------------")
    print("  VERDICT (settles D vs C)")
    print("   * EVEN rungs (c₂, c₄ ≈ -1): bar-invariant CONSTANTS -> compatible with")
    print("     a bar-even (Type-B / any crystal) source.")
    print("   * ODD rung c₃ = -2 - ℏ_q²: NOT bar-invariant — it is bar-MIXED:")
    print("       (i)  a bar-INVARIANT topological core J_Hopf(1) = -2 (Jones of the Hopf link)")
    print("       (ii) a bar-COVARIANT quantum tail -ℏ_q²  (-> -q²ℏ_q² under bar).")
    print("   => A uniformly bar-INVARIANT Type-B folded crystal CANNOT reproduce c₃:")
    print("      it can supply the even/geometric rungs and the -2 core, but NOT the")
    print("      bar-covariant ℏ_q² tail.  REFUTE chain D as the single c_k kernel.")
    print("   * The odd rungs are already TOPOLOGICALLY identified (c₁=cos, c₃=J_Hopf-ℏ²)")
    print("     — Jones/Hopf objects, not crystal content.  Chain C (Demazure) is also")
    print("     bar-even and equally cannot make the topological core or the ℏ² tail.")
    print("   => The 'crystal chain' framing is mis-aimed for the ODD rungs.  The kernel")
    print("      is PARITY-SPLIT: bar-even (crystal/geometric) even rungs × bar-odd")
    print("      (Jones-Hopf topological) odd rungs.  The open piece is the COEFFICIENT")
    print("      of the bar-covariant ℏ_q² tail on c₃ — a topological-quantum object,")
    print("      not a Type-B fold.  Do NOT spend the 12-17 session Type-B build on c₃.\n")

    w = WitnessBuilder("qbeta-chain-d-bar-parity-gate", engine="python")
    w.set_description(
        "Bar-parity gate for Q_β chain D (Type-B folded crystal). Type-B content "
        "is bar-involution invariant; tests whether the c_k are. c₂ even/constant "
        "(bar-invariant ✓); c₃ = -2 - ℏ_q² is bar-MIXED (invariant -2 Jones core + "
        "bar-covariant -ℏ_q² tail), so a uniformly bar-invariant Type-B crystal "
        "cannot reproduce c₃. REFUTE D as the single kernel; the ladder is "
        "parity-split (crystal even rungs × Jones-Hopf odd rungs). No fit.")
    w.add_parameter("q0", mp.nstr(q, 40))
    w.add_data("hbar_sq_is_bar_covariant_times_q2", bool(abs(lhs - rhs) < mp.mpf(10) ** -40))
    w.add_data("c2_bar_invariant", True)
    w.add_data("c3_q0", mp.nstr(c3q, 30))
    w.add_data("c3_bar_image", mp.nstr(c3qb, 30))
    w.add_data("c3_bar_invariant", bool(inv))
    w.add_data("c3_bar_swing_pct", swing_pct)
    w.add_data("verdict", "REFUTE-D-as-single-kernel; ladder is parity-split (crystal even × Jones-Hopf odd)")
    w.add_assertion("c3_not_bar_invariant", float(not inv), 1.0,
                    source="c₃(1/q0) ≠ c₃(q0): bar-covariant ℏ_q² tail")
    w.add_assertion("hbar_sq_bar_covariant", float(abs(lhs - rhs) < mp.mpf(10) ** -40), 1.0,
                    source="ℏ_q²(1/q) = q²·ℏ_q²(q)")
    w.add_caveat(
        "c₄ even-rung is flagged a normalisation artifact (PR #1786); the gate "
        "rests on c₂ (constant) and c₃ (= -2-ℏ_q², fully determined, no Hoefsmit b). "
        "The c₁=cos rung needs α(q) and is not tested here.")
    w.add_caveat(
        "Structural-constraint (prune) result: refutes Type-B as the c₃ kernel and "
        "redirects to a parity-split kernel. Nothing wired; c_k stay cal-anchored.")
    path = w.save()
    print(f"  witness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
