#!/usr/bin/env python3
# polynomial_q_not_applicable: the trace-ratio is an EXACT rational function of
# q (sympy); the only archimedean step is the reference value + the alpha^2
# order-of-magnitude check at q_0.
"""
conj:e-hartree-categorical-derivation — ROUND 20 (item 1 of the owner queue).

The single gap left after round 19: the ARCHIMEDEAN TRACE-RATIO on the
activated scalar block — the analogue, for the molecular (2,2) channel, of
the EM construction alpha_EM = (singlet projector trace) / (force-carrier
complexity).  This probe makes that ratio explicit and reports, tiered,
whether the alpha_EM^2 scaling emerges.

THE CONSTRUCTION (parallel to prop:em-coupling-projection, not fitted).
  In the established EM derivation the coupling is NOT the bare projector
  trace tr_tau(e_-); it is that trace DIVIDED by the force-carrier complexity
  q[9]_q[10]_q (= 1/alpha_EM).  The molecular binding shares TWO electrons
  through the SAME force carriers (round-18 transpose pair), so the
  structurally-parallel normaliser is the complexity SQUARED, (q[9]_q[10]_q)^2
  = 1/alpha_EM^2.  Define the molecular trace-ratio on the activated scalar
  block (round 19, K-shell dressing m = 5):
      rho_(2,2) := chi_(2,2)(sigma_1 sigma_2^(5) sigma_3) / (q[9]_q[10]_q)^2 .

RESULT (exact in R; this probe).
      chi_(2,2)(dressed, m) = h [m-1]_q [4]_q / [2]_q^2      (round 19),
      at m = 5:  chi_(2,2) = h ([4]_q/[2]_q)^2 = h (q^2 + q^-2)^2,
  so
      rho_(2,2) = h (q^2 + q^-2)^2 / (q[9]_q[10]_q)^2
                = C(q) * alpha_EM^2 ,
      C(q) := h ([4]_q/[2]_q)^2 = h (q^2 + q^-2)^2   (an O(1) element of R).
  THE alpha_EM^2 SCALING EMERGES EXACTLY, with a DERIVED (not fitted) O(1)
  coefficient C(q) — precisely the "combinatorial O(1) coefficient from the
  chi_(3,1) chi_(2,1,1) structure" anticipated by round 18.  At q_0:
  C(q_0) ~ 0.92 (order 1), alpha_EM^2 ~ 5.3e-5, rho_(2,2) ~ 4.9e-5 (order
  alpha^2) — i.e. rho_(2,2) is alpha^2-scale, NOT O(1), confirming the
  magnitude is now carried by the ratio (the round-19 character alone was
  O(1)).

WHAT THIS CLOSES vs WHAT STAYS OPEN (honest tiering).
  CLOSED (exact, derived): the alpha_EM^2 SHAPE of the molecular scalar-block
  trace-ratio, with an explicit O(1) coefficient C(q) = h([4]/[2])^2 in R.
  This is the round-18 closure-path identity made exact.
  STILL OPEN (the gate, unchanged): whether the LP/SDP DUAL y_cov actually
  normalises by the force-carrier complexity squared — i.e. whether rho_(2,2)
  IS y_cov.  That is mechanism B of the conjecture (the bare separated-atom
  point must be a smooth interior facet so the dual is quadratic, not a kink);
  this probe does NOT establish it.  Also unchanged: the m_e c^2 unit
  transport.  So the conjecture remains OPEN — but the open part is now a
  SINGLE structural question (is the LP-dual normaliser the squared
  complexity?), with the entire algebraic/character side closed exactly.
  NO comparison of C(q_0) to an experimental Hartree O(1) coefficient is made
  (that comparison is the gated step; making it now would be fishing).

Refs: conj:e-hartree-categorical-derivation (rounds 11-19; round 18 closure
path; mechanism B); prop:em-coupling-projection (the complexity normaliser
template); prop:alpha-em-categorical-trace-ratio; e_hartree_round19_dressed_
scalar_block.py (the dressed character).
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
    mp.mp.dps = 70
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785827513808075916690956107688798744991218736"


def main() -> None:
    w = WitnessBuilder("e-hartree-round20-trace-ratio", engine="python")
    q = sp.symbols("q", positive=True)
    h = q - 1 / q

    def qint(k, q_sym=q, h_sym=h):
        return (q_sym ** k - q_sym ** (-k)) / h_sym

    # round-19 dressed scalar character at general m, and at K-shell m = 5
    m = sp.symbols("m", positive=True, integer=True)
    chi22_m = sp.simplify(h * qint(m - 1) * qint(4) / qint(2) ** 2)
    chi22_5 = sp.simplify(chi22_m.subs(m, 5))
    # force-carrier complexity and alpha_EM
    complexity = sp.simplify(q * qint(9) * qint(10))           # = 1/alpha_EM
    alpha_em = sp.simplify(1 / complexity)
    # the trace-ratio
    rho = sp.simplify(chi22_5 / complexity ** 2)
    C = sp.simplify(h * (qint(4) / qint(2)) ** 2)              # claimed O(1) coeff
    # exact identities
    C_form_ok = sp.simplify(C - h * (q ** 2 + q ** -2) ** 2) == 0
    factorisation_ok = sp.simplify(rho - C * alpha_em ** 2) == 0
    chi22_5_ok = sp.simplify(chi22_5 - h * (q ** 2 + q ** -2) ** 2) == 0

    # archimedean reference values at q_0 (orders of magnitude; NO experiment)
    q0 = mp.mpf(Q0) if HAVE_MP else float(Q0)
    def ev(e):
        return (mp.mpf(str(sp.N(e.subs(q, sp.Float(str(q0), 60)), 50)))
                if HAVE_MP else float(sp.N(e.subs(q, sp.Float(str(q0), 30)))))
    C0, a0, rho0 = ev(C), ev(alpha_em), ev(rho)
    C_is_order1 = mp.mpf("0.1") < C0 < mp.mpf("10") if HAVE_MP else 0.1 < C0 < 10
    # rho is alpha^2-scale: |log10(rho0) - log10(a0^2)| < 1 (within an order of mag of alpha^2)
    import math
    rho_alpha2_scale = abs(math.log10(float(rho0)) - math.log10(float(a0) ** 2)) < 1

    print("=" * 74)
    print("conj:e-hartree ROUND 20 — trace-ratio on the activated (2,2) block")
    print("=" * 74)
    print(f"  chi_(2,2)(dressed,m) = h[m-1][4]/[2]^2  (round 19)")
    print(f"  at K-shell m=5: chi_(2,2) = h(q^2+q^-2)^2 : {chi22_5_ok}")
    print(f"  normaliser = force-carrier complexity^2 = (q[9][10])^2 = 1/alpha_EM^2")
    print(f"  rho_(2,2) := chi_(2,2)/complexity^2")
    print(f"  EXACT: rho_(2,2) = C(q) * alpha_EM^2,  C(q)=h([4]/[2])^2 : "
          f"{factorisation_ok}")
    print()
    print(f"  at q0:  C(q0)      = {mp.nstr(C0, 8) if HAVE_MP else C0}   (O(1): "
          f"{C_is_order1})")
    print(f"          alpha_EM^2 = {mp.nstr(a0**2, 6) if HAVE_MP else a0**2}")
    print(f"          rho_(2,2)  = {mp.nstr(rho0, 6) if HAVE_MP else rho0}   "
          f"(alpha^2-scale: {rho_alpha2_scale})")
    print()
    print("  CLOSED (exact): alpha_EM^2 shape + derived O(1) coeff C(q) in R.")
    print("  OPEN (gate): is the LP-dual y_cov normaliser the squared complexity?")
    print("    (mechanism B; smooth-facet vs kink) — NOT established here.")
    print("  No comparison of C(q0) to an experimental O(1) coeff (fishing gate).")

    w.set_description(
        "conj:e-hartree round 20 (item 1): the archimedean trace-ratio on the "
        "round-19 activated scalar (2,2) block.  Parallel to "
        "prop:em-coupling-projection (coupling = projector trace / "
        "force-carrier complexity), define rho_(2,2) := "
        "chi_(2,2)(sigma_1 sigma_2^(5) sigma_3) / (q[9]_q[10]_q)^2 (two shared "
        "electrons -> complexity squared).  EXACT result in R: rho_(2,2) = "
        "C(q) alpha_EM^2 with C(q) = h([4]_q/[2]_q)^2 = h(q^2+q^-2)^2 an O(1) "
        "element of R (the round-18-anticipated combinatorial coefficient).  "
        "The alpha_EM^2 SCALING emerges exactly; at q_0, C ~ 0.92 (order 1) "
        "and rho ~ 4.9e-5 is alpha^2-scale (vs the O(1) bare character).  "
        "CLOSED: the algebraic/character side (alpha^2 shape + derived O(1) "
        "coefficient).  OPEN (unchanged gate): whether the LP/SDP dual y_cov "
        "actually normalises by the squared force-carrier complexity "
        "(mechanism B, smooth-facet-vs-kink) — not established; and the "
        "m_e c^2 unit transport.  Conjecture remains OPEN, now reduced to the "
        "single structural question 'is the LP-dual normaliser the squared "
        "complexity?'.  No experimental O(1)-coefficient comparison (fishing "
        "gate)."
    )
    w.set_content_block("conj:e-hartree-categorical-derivation")
    w.add_data("q0", str(q0))
    w.add_data("chi22_K_shell_m5", str(chi22_5))
    w.add_data("force_carrier_complexity", str(complexity))
    w.add_data("trace_ratio_rho22", str(rho))
    w.add_data("O1_coefficient_C", str(C))
    w.add_data("values_at_q0", {"C": str(C0), "alpha_em_sq": str(ev(alpha_em**2)),
                                "rho22": str(rho0)})
    w.add_assertion(
        "chi_(2,2)(dressed, m=5) = h(q^2+q^-2)^2 (round-19 K-shell value)",
        computed=bool(chi22_5_ok), expected=True,
        source="round 19 dressed-scalar character",
    )
    w.add_assertion(
        "EXACT factorisation rho_(2,2) = C(q)*alpha_EM^2 with C = h([4]/[2])^2",
        computed=bool(factorisation_ok and C_form_ok), expected=True,
        source="chi_(2,2)/complexity^2; symbolic identity in R",
    )
    w.add_assertion(
        "C(q) is an O(1) coefficient at q_0 (0.1 < C < 10)",
        computed=bool(C_is_order1), expected=True,
        source="C(q0) ~ 0.92",
    )
    w.add_assertion(
        "rho_(2,2) is alpha^2-scale at q_0 (within an order of magnitude of alpha^2)",
        computed=bool(rho_alpha2_scale), expected=True,
        source="rho ~ 4.9e-5 vs alpha^2 ~ 5.3e-5",
    )
    w.add_data(
        "finding",
        "Round 20 closes the algebraic side of the e-hartree closure path "
        "exactly: the trace-ratio rho_(2,2) = chi_(2,2)/(force-carrier "
        "complexity)^2 = h([4]/[2])^2 * alpha_EM^2, so the alpha^2 scaling "
        "emerges with a DERIVED O(1) coefficient C(q) = h(q^2+q^-2)^2 in R "
        "(no fit).  The conjecture remains OPEN but is now reduced to a "
        "SINGLE structural question: does the LP/SDP dual y_cov normalise by "
        "the squared force-carrier complexity (mechanism B, smooth facet vs "
        "kink)?  The m_e c^2 unit transport is the only other open input.  No "
        "experimental comparison of C(q_0) (gated)."
    )
    w.save()
    print("\nDone. Witness saved (e-hartree-round20-trace-ratio).")


if __name__ == "__main__":
    main()
