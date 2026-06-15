#!/usr/bin/env python3
# polynomial_q_not_applicable: pre-archimedean delta_q decorations + the FSC
# coupling, in q-data (no pi); the Jones evaluation is upstream.
"""
The alpha_{basis-knot} coupling family — PRE-ARCHIMEDEAN foundation (no pi).

Owner directive: take up + finish the alpha_{basis-knot} work (alpha_EM :=
alpha_{T_{2,3}}); write up in paper, prove in Lean, use in compute to
optimize/reduce error. "I don't like to see pi ... should be pre-archimedean."

THE 6 COHOMOLOGICAL FORCE-KNOTS on Sigma_4 (cohomological-embedding):
  {T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}} — the complete set of
  cohomological/dimensional invariants (H^1(Sigma_4)=Z^8, chi=-6). Each is a
  force operator; alpha_EM = the trefoil T_{2,3} (electromagnetic).

PRE-ARCHIMEDEAN BUILDING BLOCK — the q-dimension decoration (no pi):
  delta_q(T_{2,k}) = q^k - q^{-k} = h*[k]_q,  h = q - q^{-1},
  [k]_q = (q^k - q^{-k})/(q - q^{-1}) = sinh(k*lambda)/sinh(lambda), lambda=ln q.
  These live in R = Z[q^{+-1/2}, h^{-1}] — purely q-rational, NO pi.

THE FSC, PRE-ARCHIMEDEAN (prop:alpha-em-categorical-trace-ratio):
  alpha_EM = h^2 / (q * delta_q(T_{2,9}) * delta_q(T_{3,5}))
           = 1 / (q * [9]_q * [10]_q)     (delta_q(T_{3,5}) = h*[10]_q, Rosso-Jones)
  — the antisymmetric e_- (sinh) coupling of the Hopf 2-strand operation. NO pi.

THE pi PROBLEM (to push pre-archimedean): the corrections 2/(3pi) and alpha/(4pi)
(em-coupling-bring-zero-mode) are the ARCHIMEDEAN images of a Hopf fibration
S^1->S^3->S^2 (the block's own suggestion) = the same Hopf/e_-/sinh channel as
van der Waals (prop:vdw-pskew-isolation, bar-odd sinh(2lambda)(e+-e-)). The
program's optimization target: replace the pi-corrections by their PRE-archimedean
sinh/q-source whose tau_arch-image is the pi-form — reducing the residual without
ever writing pi in the derivation.

This script establishes the pre-archimedean foundation (the 6 delta_q + the bare
FSC, no pi) and frames the per-force alpha_K assembly + the no-pi correction as
the next steps. Nothing fitted.

Refs: cohomological-embedding (6 force-knots); prop:alpha-em-categorical-trace-ratio
(alpha_EM = e_- trace, no pi); prop:force-carrier-bring-uniqueness (T_{2,9},T_{3,5});
em-coupling-bring-zero-mode (the pi corrections); prop:vdw-pskew-isolation (Hopf sinh).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

try:
    import mpmath as mp
    mp.mp.dps = 50
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099780333553254"

CODATA_INV_ALPHA = "137.035999177"   # CODATA 2022 1/alpha_EM


def qbracket(q, k):
    """[k]_q = (q^k - q^{-k})/(q - q^{-1})."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def delta_q(q, k):
    """delta_q(T_{2,k}) = q^k - q^{-k} = h*[k]_q (pre-archimedean, no pi)."""
    return q ** k - q ** (-k)


def main() -> None:
    w = WitnessBuilder("alpha-basis-knot-couplings", engine="python")
    q = mp.mpf(Q0) if HAVE_MP else float(Q0)
    h = q - 1 / q

    # The 6 cohomological force-knots and their effective delta_q exponent.
    # 2-strand T_{2,k}: exponent k. 3-strand via Rosso-Jones: T_{3,5}->10
    # (prop:alpha-em-categorical-trace-ratio); T_{3,4} effective exponent is
    # the open 3-strand Rosso-Jones evaluation (flagged below, not guessed).
    knots = [
        ("T_2_3", 2, 3, 3, "electromagnetic (= alpha_EM particle, trefoil)"),
        ("T_2_5", 2, 5, 5, "2nd generation"),
        ("T_2_7", 2, 7, 7, "charm / 3rd generation"),
        ("T_2_9", 2, 9, 9, "strong binding (force-carrier)"),
        ("T_3_5", 3, 5, 10, "weak / beta-decay (force-carrier; Rosso-Jones->[10])"),
        ("T_3_4", 3, 4, None, "Hopf-squared (top); 3-strand Rosso-Jones exponent OPEN"),
    ]

    print("=" * 74)
    print("alpha_{basis-knot} couplings — PRE-ARCHIMEDEAN foundation (no pi)")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q, 12) if HAVE_MP else q}   h = q - 1/q = "
          f"{mp.nstr(h, 8) if HAVE_MP else h}")
    print(f"  delta_q(T_{{2,k}}) = q^k - q^-k = h*[k]_q  (in Z[q^+-1/2, h^-1], NO pi)")
    print()
    print(f"  {'knot':6s} {'strand':>6s} {'k_eff':>6s} {'[k]_q':>14s} "
          f"{'delta_q':>14s}  force")
    data = {}
    for name, strand, s, keff, force in knots:
        if keff is None:
            print(f"  {name:6s} {strand:>6d} {'OPEN':>6s} {'(Rosso-Jones)':>14s} "
                  f"{'(open)':>14s}  {force}")
            data[name] = {"strand": strand, "k_eff": None, "force": force,
                          "status": "open-3strand-rosso-jones"}
            continue
        bk = qbracket(q, keff)
        dq = delta_q(q, keff)
        bks = mp.nstr(bk, 10) if HAVE_MP else f"{bk:.6f}"
        dqs = mp.nstr(dq, 10) if HAVE_MP else f"{dq:.6f}"
        print(f"  {name:6s} {strand:>6d} {keff:>6d} {bks:>14s} {dqs:>14s}  {force}")
        data[name] = {"strand": strand, "k_eff": keff, "force": force,
                      "qbracket": str(bk), "delta_q": str(dq)}

    # alpha_EM, pre-archimedean: 1/alpha = q*[9]_q*[10]_q (= h^2/(q dq9 dq10)).
    inv_alpha = q * qbracket(q, 9) * qbracket(q, 10)
    # cross-check the trace-ratio identity h^2/(q dq9 dq10) = 1/(q[9][10]):
    alt = h ** 2 / (q * delta_q(q, 9) * delta_q(q, 10))
    codata = mp.mpf(CODATA_INV_ALPHA) if HAVE_MP else float(CODATA_INV_ALPHA)
    resid = (inv_alpha - codata) / codata
    print()
    print(f"  alpha_EM := alpha_{{T_2_3}} (electromagnetic). PRE-ARCHIMEDEAN bare:")
    print(f"    1/alpha_EM = q*[9]_q*[10]_q = "
          f"{mp.nstr(inv_alpha, 12) if HAVE_MP else inv_alpha}")
    print(f"    trace-ratio h^2/(q*dq9*dq10) = "
          f"{mp.nstr(alt, 12) if HAVE_MP else alt}  (identity check)")
    print(f"    CODATA 1/alpha = {CODATA_INV_ALPHA}")
    print(f"    bare residual  = {mp.nstr(resid, 4) if HAVE_MP else resid}  "
          f"(-1.55e-3; the pi-corrections close this — to be pushed pre-arch)")
    print()
    print("  NEXT (no pi): the 2/(3pi)+alpha/(4pi) corrections are the archimedean")
    print("    image of the Hopf S^1->S^3->S^2 / e_- sinh channel (= vdW channel).")
    print("    Optimization target: their PRE-archimedean sinh/q source.")

    w.set_description(
        "Pre-archimedean foundation of the alpha_{basis-knot} coupling family "
        "(owner: take up + finish; no pi). The 6 cohomological force-knots on "
        "Sigma_4 each carry the q-dimension decoration delta_q(T_{2,k}) = "
        "q^k-q^-k = h[k]_q in R=Z[q^+-1/2,h^-1] (no pi). alpha_EM := alpha_{T_2_3} "
        "(trefoil, electromagnetic) has the pre-archimedean bare form 1/alpha_EM = "
        "q[9]_q[10]_q = h^2/(q delta_q(T_{2,9}) delta_q(T_{3,5})) (the antisymmetric "
        "e_- / sinh Hopf coupling, prop:alpha-em-categorical-trace-ratio), bare "
        "residual -1.55e-3 vs CODATA. The pi-carrying corrections 2/(3pi)+alpha/(4pi) "
        "are the archimedean image of the Hopf S^1->S^3->S^2 / e_- sinh channel (the "
        "SAME channel as van der Waals, prop:vdw-pskew-isolation); the program's "
        "optimization is to express them by their pre-archimedean sinh/q source. The "
        "3-strand T_{3,4} delta_q (Rosso-Jones) and the per-force alpha_K assembly are "
        "the open next steps. Nothing fitted."
    )
    w.set_content_block("prop:alpha-em-categorical-trace-ratio")
    w.add_data("q0", str(q))
    w.add_data("h", str(h))
    w.add_data("basis_knots", data)
    w.add_data("inv_alpha_em_bare", str(inv_alpha))
    w.add_data("trace_ratio_check", str(alt))
    w.add_data("codata_inv_alpha", CODATA_INV_ALPHA)
    w.add_data("bare_residual_rel", str(resid))
    w.add_assertion(
        "trace-ratio identity: alpha_EM=h^2/(q dq9 dq10) is 1/(q[9]_q[10]_q)",
        computed=bool(abs(alt * inv_alpha - 1) < (mp.mpf(10) ** -30 if HAVE_MP else 1e-12)),
        expected=True, source="delta_q(T_{2,k}) = h[k]_q; algebraic identity in R",
    )
    w.add_assertion(
        "bare 1/alpha_EM is q-rational (no pi) and within 0.2% of CODATA",
        computed=bool(abs(resid) < mp.mpf("2e-3") if HAVE_MP else abs(resid) < 2e-3),
        expected=True, source="q[9]_q[10]_q at q0 vs CODATA 137.036",
    )
    w.add_data(
        "finding",
        "The alpha_{basis-knot} family is founded on the pre-archimedean q-dimension "
        "decorations delta_q(T_{2,k}) = q^k-q^-k = h[k]_q (no pi). alpha_EM := "
        "alpha_{T_2_3} bare = 1/(q[9]_q[10]_q) (the e_- sinh Hopf coupling), residual "
        "-1.55e-3. The pi corrections are the archimedean image of the Hopf/e_-/sinh "
        "channel (= the van der Waals channel); the no-pi optimization is their "
        "pre-archimedean sinh/q source. Open: 3-strand T_{3,4} Rosso-Jones exponent; "
        "the per-force alpha_K assembly (which carriers mediate which force)."
    )
    w.save()
    print("\nDone. Witness saved (alpha-basis-knot-couplings).")


if __name__ == "__main__":
    main()
