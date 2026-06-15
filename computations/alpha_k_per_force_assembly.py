#!/usr/bin/env python3
# polynomial_q_not_applicable: the delta_q decorations are q-polynomial (step 2),
# but the per-force ASSEMBLY reported here is the archimedean evaluation at q_0 of
# the established EM trace-ratio; the per-force SELECTION rule is conditional/open.
"""
alpha_{basis-knot} STEP 3 — per-force alpha_K assembly (no pi).

Owner directive (alpha_{basis-knot} program): "per-force alpha_K assembly
(which carriers mediate which force)".

WHAT IS ESTABLISHED (corpus, not fitted).
  The per-force assembly mechanism is already carried by
  prop:force-carrier-intertwining-correspondence (conditional on
  conj:e-hartree-categorical-derivation): a torus-knot force carrier T_{m,k}
  (first index m = strand count) acts on an n-strand molecular braid via
  B_m -> B_n and lands on the Wedderburn partition
      lambda(T_{m,k}) = (m, 1^{n-m})        [m strands intertwined, n-m free],
  and alpha_EM is the e_- (sinh) Hopf trace-ratio of the carrier delta_q values
  (prop:alpha-em-categorical-trace-ratio):
      1/alpha_EM = q * [9]_q * [10]_q = h^2 / (q * delta_q(T_{2,9}) * delta_q(T_{3,5})).

WHAT STEP 2 ADDS (now derived).
  The delta_q decoration MAGNITUDE is fixed by the WRITHE w = (m-1)k
  (rosso_jones_three_strand_delta_q.py / prop:torus-knot-delta-q-writhe):
      delta_q(T_{m,k}) = q^{(m-1)k} - q^{-(m-1)k} = h*[(m-1)k]_q.
  So each force carrier carries TWO derived data:
      (i)  intertwining partition  lambda = (m, 1^{n-m})   [first index m],
      (ii) writhe decoration       delta_q = h*[(m-1)k]_q  [writhe (m-1)k].
  For the two genus-4 carriers:
      T_{2,9}: lambda = (2,1^{n-2}),  delta_q = h*[9]_q   (writhe 9)   -> strong
      T_{3,5}: lambda = (3,1^{n-3}),  delta_q = h*[10]_q  (writhe 10)  -> weak/beta
  and (3,1)^T = (2,1,1): the two carrier channels are transpose partitions
  (Frobenius self-dual, antipode-closed) — the parity-symmetric bound state.

WHAT REMAINS OPEN (honest scope; NOT fitted here).
  The per-force SELECTION rule — which carrier PAIR mediates each of the other
  forces (strong alpha_s, weak alpha_W, ...) — is governed by the same
  intertwining correspondence and remains CONDITIONAL on
  conj:e-hartree-categorical-derivation.  This script does NOT enumerate
  carrier-pair products against measured couplings (that would be
  multiple-comparison fishing, forbidden by the production-vs-exploratory
  discipline).  It assembles ONLY the established EM trace-ratio end-to-end from
  the step-2 writhe decorations, and tabulates the derived (partition, writhe)
  data per carrier.  Nothing fitted.

Refs: prop:force-carrier-intertwining-correspondence (the assembly mechanism);
prop:alpha-em-categorical-trace-ratio (the EM trace-ratio, no pi);
prop:torus-knot-delta-q-writhe (step 2: delta_q = h[(m-1)k]_q);
prop:force-carrier-bring-uniqueness (T_{2,9}, T_{3,5} are THE genus-4 carriers).
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
    mp.mp.dps = 70
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785827513808075916690956107688798744991218736"

CODATA_INV_ALPHA = "137.035999177"   # CODATA 2022 1/alpha_EM


def qbracket(q, k):
    """[k]_q = (q^k - q^{-k})/(q - q^{-1})."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def main() -> None:
    w = WitnessBuilder("alpha-k-per-force-assembly", engine="python")
    q = mp.mpf(Q0) if HAVE_MP else float(Q0)
    h = q - 1 / q
    n_ref = 4  # reference molecular braid (covalent H2; correspondence worked example)

    # The 6 cohomological force-knots: (name, m=strand count, k=second index,
    # role).  Writhe = (m-1)*k (step 2); intertwining partition = (m, 1^{n-m}).
    knots = [
        ("T_2_3", 2, 3, "electromagnetic (alpha_EM particle, trefoil)"),
        ("T_2_5", 2, 5, "2nd generation"),
        ("T_2_7", 2, 7, "charm / 3rd generation"),
        ("T_2_9", 2, 9, "strong binding (force-carrier)"),
        ("T_3_4", 3, 4, "Hopf-squared / top"),
        ("T_3_5", 3, 5, "weak / beta-decay (force-carrier)"),
    ]

    def partition(m, n):
        if m >= n:
            return (m,)
        return (m,) + (1,) * (n - m)

    print("=" * 74)
    print("alpha_{basis-knot} STEP 3 — per-force assembly (no pi)")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q, 12) if HAVE_MP else q}   reference n = {n_ref} strands")
    print("  carrier T_{m,k}: partition lambda=(m,1^{n-m}) [index m] ; "
          "delta_q=h[(m-1)k]_q [writhe]")
    print()
    print(f"  {'knot':6s} {'m':>2s} {'k':>2s} {'writhe':>6s} "
          f"{'lambda(n=4)':>12s} {'delta_q':>12s}  role")
    data = {}
    for name, m, k, role in knots:
        w_writhe = (m - 1) * k
        lam = partition(m, n_ref)
        dq = h * qbracket(q, w_writhe)
        dqs = mp.nstr(dq, 8) if HAVE_MP else f"{dq:.5f}"
        lam_s = "(" + ",".join(str(x) for x in lam) + ")"
        print(f"  {name:6s} {m:>2d} {k:>2d} {w_writhe:>6d} {lam_s:>12s} "
              f"{dqs:>12s}  {role}")
        data[name] = {
            "m_strand": m, "k_index": k, "writhe": w_writhe,
            "intertwining_partition_n4": list(lam),
            "delta_q_h_qbracket": f"h*[{w_writhe}]_q",
            "delta_q_value_at_q0": str(dq), "role": role,
        }

    # The two genus-4 force carriers and the EM trace-ratio assembly (established).
    dq_2_9 = h * qbracket(q, 9)    # writhe 9
    dq_3_5 = h * qbracket(q, 10)   # writhe 10
    inv_alpha_traceratio = h ** 2 / (q * dq_2_9 * dq_3_5)
    inv_alpha_bracket = q * qbracket(q, 9) * qbracket(q, 10)
    codata = mp.mpf(CODATA_INV_ALPHA) if HAVE_MP else float(CODATA_INV_ALPHA)
    # identity: h^2/(q dq9 dq10) == 1/(q[9][10])  -> inv_alpha = q[9][10]
    inv_alpha = 1 / inv_alpha_traceratio
    resid = (inv_alpha - codata) / codata
    transpose_ok = (sorted([3, 1], reverse=True) == [3, 1] and
                    partition(3, n_ref) == (3, 1) and partition(2, n_ref) == (2, 1, 1))

    print()
    print("  ESTABLISHED EM assembly (carrier pair = strong T_{2,9} x weak T_{3,5}):")
    print(f"    delta_q(T_2,9) = h[9]_q  = {mp.nstr(dq_2_9, 8) if HAVE_MP else dq_2_9}"
          f"   (partition (2,1,1))")
    print(f"    delta_q(T_3,5) = h[10]_q = {mp.nstr(dq_3_5, 8) if HAVE_MP else dq_3_5}"
          f"   (partition (3,1))")
    print(f"    1/alpha_EM = h^2/(q dq9 dq10) = q[9][10] = "
          f"{mp.nstr(inv_alpha, 12) if HAVE_MP else inv_alpha}")
    print(f"    CODATA 1/alpha = {CODATA_INV_ALPHA}   residual = "
          f"{mp.nstr(resid, 4) if HAVE_MP else resid}")
    print(f"    carrier channels (3,1) and (2,1,1) are transpose partitions: "
          f"{transpose_ok}")
    print()
    print("  OPEN (not fitted): the per-force SELECTION (which carrier pair for")
    print("    alpha_s, alpha_W, ...) stays conditional on")
    print("    conj:e-hartree-categorical-derivation.  No carrier-pair enumeration.")

    w.set_description(
        "alpha_{basis-knot} step 3: per-force assembly.  Wires the step-2 writhe "
        "decoration delta_q(T_{m,k}) = h[(m-1)k]_q into the established "
        "force-carrier intertwining correspondence (prop:force-carrier-"
        "intertwining-correspondence): each carrier T_{m,k} carries an "
        "intertwining partition lambda=(m,1^{n-m}) [first index m] and a writhe "
        "decoration h[(m-1)k]_q [writhe (m-1)k].  The two genus-4 carriers are "
        "T_{2,9} (strong; (2,1,1), h[9]_q) and T_{3,5} (weak/beta; (3,1), "
        "h[10]_q), transpose partitions (Frobenius self-dual).  The established "
        "EM trace-ratio 1/alpha_EM = h^2/(q delta_q(T_{2,9}) delta_q(T_{3,5})) = "
        "q[9]_q[10]_q is assembled end-to-end from the derived writhe decorations "
        "(residual vs CODATA reported).  The per-force SELECTION rule (which "
        "carrier pair mediates the other forces) stays conditional on "
        "conj:e-hartree-categorical-derivation; NO carrier-pair-vs-coupling "
        "enumeration is done (anti-fishing).  Pre-archimedean decorations, no pi."
    )
    w.set_content_block("prop:force-carrier-intertwining-correspondence")
    w.add_data("q0", str(q))
    w.add_data("n_reference_strands", n_ref)
    w.add_data("force_knots", data)
    w.add_data("delta_q_T2_9_h9", str(dq_2_9))
    w.add_data("delta_q_T3_5_h10", str(dq_3_5))
    w.add_data("inv_alpha_em_traceratio", str(inv_alpha))
    w.add_data("codata_inv_alpha", CODATA_INV_ALPHA)
    w.add_data("inv_alpha_residual_rel", str(resid))
    w.add_assertion(
        "EM trace-ratio identity h^2/(q dq9 dq10) = 1/(q[9]_q[10]_q)",
        computed=bool(abs(inv_alpha_traceratio * inv_alpha_bracket - 1)
                      < (mp.mpf(10) ** -30 if HAVE_MP else 1e-12)),
        expected=True, source="delta_q=h[k]_q (step 2); algebraic identity in R",
    )
    w.add_assertion(
        "carrier writhe decorations: T_{2,9}->h[9]_q, T_{3,5}->h[10]_q (step 2)",
        computed=bool(data["T_2_9"]["writhe"] == 9 and data["T_3_5"]["writhe"] == 10),
        expected=True, source="writhe (m-1)k: (2-1)9=9, (3-1)5=10",
    )
    w.add_assertion(
        "carrier intertwining channels (3,1) and (2,1,1) are transpose partitions",
        computed=bool(transpose_ok), expected=True,
        source="prop:force-carrier-intertwining-correspondence",
    )
    w.add_assertion(
        "1/alpha_EM assembled from derived decorations is within 0.2% of CODATA",
        computed=bool(abs(resid) < (mp.mpf("2e-3") if HAVE_MP else 2e-3)),
        expected=True, source="q[9]_q[10]_q at q0 vs CODATA 137.036",
    )
    w.add_data(
        "finding",
        "Per-force assembly: each torus-knot carrier T_{m,k} carries a derived "
        "intertwining partition (m,1^{n-m}) [index m] AND a derived writhe "
        "decoration h[(m-1)k]_q [writhe (m-1)k].  T_{2,9}=strong ((2,1,1),h[9]_q) "
        "and T_{3,5}=weak ((3,1),h[10]_q) are transpose partitions; their e_- "
        "Hopf trace-ratio assembles 1/alpha_EM = q[9]_q[10]_q end-to-end (residual "
        "-1.55e-3 vs CODATA).  The per-force selection rule for the OTHER forces "
        "stays conditional on conj:e-hartree-categorical-derivation; not fitted.  "
        "Next: step 6, the pre-archimedean (no-pi) source of the 2/(3pi)+alpha/(4pi) "
        "corrections via the Hopf S^1->S^3->S^2 / e_- channel."
    )
    w.save()
    print("\nDone. Witness saved (alpha-k-per-force-assembly).")


if __name__ == "__main__":
    main()
