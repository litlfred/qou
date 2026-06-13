#!/usr/bin/env python3
# polynomial_q_not_applicable: C(q) is an exact rational function of q; tau_arch
# on this depth-0 object is q_0-evaluation (the Bloch-Suslin regulator applies to
# depth-2 dilog objects, which C(q) is not). Archimedean value reported at q_0.
"""
conj:e-hartree-categorical-derivation — ROUND 22 (the δ_q → archimedean bridge).

Round 21 refuted Mechanism B (the Markov-layer LP route is a kink) and showed the
α² lives in the q-dimension layer (round-20 trace-ratio ρ_(2,2) = C(q)·α²,
C(q) = h(q²+q⁻²)²).  The remaining gap was named "the δ_q-decoration →
archimedean functor".  This probe SHARPENS that gap to a single, decided
functor-image question, using the EXISTING archimedean functor τ_arch — not a
new unknown.

THE FUNCTOR (corpus, prop:depth-2-identification-bloch-suslin).
  τ_arch lands substrate/fibre objects in the archimedean world.  Its
  transcendental action — the Bloch–Suslin regulator K_3^ind(F)⊗ℚ → ℝ/π²ℚ —
  applies to the DEPTH-2 (dilogarithmic) part G^(2)(H_q)/P_1.  The round-20
  coefficient C(q) = h(q²+q⁻²)² is a DEPTH-0 object: a rational function of q in
  R = ℤ[q^{±1/2},(q−q⁻¹)⁻¹], no dilog.  On depth-0 objects τ_arch is plain
  evaluation at the substrate q_0 (no regulator).  Hence:
        τ_arch(C(q)) = C(q_0)   — a determined real number, NOT 1.

RESULT (this probe, exact then evaluated).
  C(q_0) = h(q²+q⁻²)²|_{q_0} ≈ 0.873  (computed; ≠ 1).  Therefore the bridge
  gives, under the established τ_arch,
        τ_arch(ρ_(2,2)) = C(q_0) · α²   (≈ 0.873 α²),
  i.e. the q-dimension-layer trace-ratio's archimedean image is α² times an
  EXPLICIT, DERIVED O(1) categorical coefficient C(q_0) — it does NOT trivially
  reproduce the bare Hartree unit (which would need the coefficient = 1).

WHAT THIS SETTLES vs WHAT STAYS OPEN (honest, no fishing).
  SETTLED: the bridge is NOT new infrastructure (round 11 feared a whole new
  functor layer).  τ_arch on the relevant (depth-0) object is q_0-evaluation;
  the α² scaling is structural (rounds 20/21); the archimedean image is
  C(q_0)·α² with C(q_0) explicit.  The Bloch–Suslin regulator is NOT needed for
  this coefficient (it governs the depth-2 dilog sector, e.g. the hyperbolic-
  volume masses, not the rational q-dimension ratio).
  OPEN (now a single gated comparison, not infrastructure): is the derived O(1)
  coefficient C(q_0) ≈ 0.873 the PHYSICAL molecular-to-Hartree ratio?  Answering
  that requires comparing to the measured H₂ binding / Hartree unit — a
  multiple-comparison-sensitive step deliberately NOT taken here (fishing gate;
  production-vs-exploratory discipline).  Plus the standing m_e c² CAL-1 unit.

So round 22 converts "the δ_q→archimedean bridge is missing infrastructure"
(round 11) into "the bridge is q_0-evaluation; the residual is a single,
explicit, derived O(1) coefficient C(q_0) whose physical interpretation is the
one gated comparison."  No fit; no experimental number used.

Refs: conj:e-hartree-categorical-derivation (rounds 11/20/21);
def:delta-q-decoration; prop:alpha-em-categorical-trace-ratio;
prop:depth-2-identification-bloch-suslin (τ_arch / Bloch–Suslin, depth-2 only);
e_hartree_round20_trace_ratio.py (the C(q)·α² ratio).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

import sympy as sp

try:
    import mpmath as mp
    mp.dps = 60
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785827513808075916690956107688798744991218736"


def main() -> None:
    w = WitnessBuilder("e-hartree-round22-arch-bridge", engine="python")
    q = sp.symbols("q", positive=True)
    h = q - 1 / q

    # round-20 coefficient C(q) = h (q^2 + q^-2)^2, a depth-0 rational function
    C = sp.simplify(h * (q ** 2 + q ** -2) ** 2)
    # depth-0 ⇒ tau_arch = q_0-evaluation (no Bloch–Suslin regulator)
    q0 = mp.mpf(Q0) if HAVE_MP else float(Q0)
    C0 = (mp.mpf(str(sp.N(C.subs(q, sp.Float(str(q0), 55)), 50))) if HAVE_MP
          else float(sp.N(C.subs(q, q0))))
    # is C(q) free of dilog / transcendental structure? (depth-0 check: rational)
    is_rational = C.is_rational_function(q)
    coeff_ne_one = abs(C0 - 1) > mp.mpf("1e-3") if HAVE_MP else abs(C0 - 1) > 1e-3

    # the bridge image: tau_arch(rho_(2,2)) = C(q0) * alpha^2 (alpha factored out)
    print("=" * 74)
    print("conj:e-hartree ROUND 22 — the δ_q → archimedean bridge")
    print("=" * 74)
    print(f"  C(q) = h(q^2+q^-2)^2  rational-in-q (depth-0): {is_rational}")
    print(f"  τ_arch on depth-0 = q_0-evaluation (Bloch–Suslin is depth-2 only)")
    print(f"  C(q_0) = τ_arch(C(q)) = {mp.nstr(C0,10) if HAVE_MP else C0}")
    print(f"  C(q_0) ≠ 1 : {coeff_ne_one}  ⇒ bridge gives C(q_0)·α², not bare α²")
    print()
    print("  SETTLED: bridge = q_0-evaluation (not new infrastructure); α² scaling")
    print("           structural (rounds 20/21); archimedean image = C(q_0)·α².")
    print("  OPEN (single gated comparison, NOT infra): is C(q_0)≈0.873 the")
    print("           physical molecular/Hartree O(1) ratio? + m_e c² CAL-1 unit.")
    print("  No experimental number used (fishing gate).")

    w.set_description(
        "conj:e-hartree round 22: sharpens the δ_q→archimedean bridge (the gap "
        "left by round 21's Mechanism-B refutation) to a single decided "
        "functor-image question, using the EXISTING τ_arch.  Per "
        "prop:depth-2-identification-bloch-suslin, τ_arch's Bloch–Suslin "
        "regulator (K_3^ind→ℝ/π²ℚ) governs the DEPTH-2 dilog sector; the "
        "round-20 coefficient C(q)=h(q²+q⁻²)² is DEPTH-0 (rational in q), so "
        "τ_arch(C(q)) is plain q_0-evaluation = C(q_0) ≈ 0.873 (≠ 1).  Hence the "
        "bridge gives τ_arch(ρ_(2,2)) = C(q_0)·α² — the α² scaling (structural, "
        "rounds 20/21) times an EXPLICIT derived O(1) categorical coefficient, "
        "NOT new infrastructure (contra round 11's fear).  Remaining gap is now "
        "a single GATED comparison — is C(q_0) the physical molecular/Hartree "
        "ratio? — deliberately not taken (fishing gate), plus the m_e c² CAL-1 "
        "unit.  No fit, no experimental number."
    )
    w.set_content_block("conj:e-hartree-categorical-derivation")
    w.add_data("q0", str(q0))
    w.add_data("C_q_symbolic", str(C))
    w.add_data("C_q0_archimedean_image", str(C0))
    w.add_data("C_is_rational_depth0", bool(is_rational))
    w.add_assertion(
        "C(q) is rational in q (depth-0 ⇒ τ_arch = q_0-evaluation, no regulator)",
        computed=bool(is_rational), expected=True,
        source="C(q)=h(q^2+q^-2)^2 ∈ R; Bloch–Suslin is depth-2 only",
    )
    w.add_assertion(
        "τ_arch(C(q)) = C(q_0) ≠ 1 (bridge yields C(q_0)·α², not bare α²)",
        computed=bool(coeff_ne_one), expected=True,
        source="q_0-evaluation of the depth-0 coefficient",
    )
    w.add_data(
        "finding",
        "Round 22 converts the δ_q→archimedean bridge from 'missing "
        "infrastructure' (round 11) to 'q_0-evaluation of a depth-0 "
        "coefficient'.  τ_arch(ρ_(2,2)) = C(q_0)·α² with C(q_0)=h(q²+q⁻²)²|_q0 "
        "≈ 0.873 explicit and ≠ 1; the α² scaling is structural; the "
        "Bloch–Suslin regulator does not enter (depth-2 only).  The sole "
        "remaining open item is the GATED comparison of the derived O(1) "
        "coefficient C(q_0) to the physical molecular/Hartree ratio (not taken "
        "— fishing gate), plus the standing m_e c² CAL-1 unit transport."
    )
    w.save()
    print("\nDone. Witness saved (e-hartree-round22-arch-bridge).")


if __name__ == "__main__":
    main()
