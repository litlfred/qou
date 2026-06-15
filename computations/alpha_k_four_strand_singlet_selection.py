#!/usr/bin/env python3
# polynomial_q_not_applicable: the singlet multiplicities are INTEGERS (exact,
# pre-archimedean) and the Gram data is symbolic in delta = [2]_q; the only
# archimedean evaluation is the reference value of the Gram eigenvalues at q_0.
"""
alpha_{basis-knot} per-force SELECTION — the even-strand singlet ladder (no pi).

Owner directive (alpha_{basis-knot} program, step-3 continuation): derive the
per-force coupling selection structurally; NO carrier-pair-vs-measured-coupling
enumeration (anti-fishing, per alpha_k_per_force_assembly.py scope note).

WHAT IS ESTABLISHED (corpus, cited).
  thm:em-spectral-completeness — the 2-strand sector E = End(A (x) A) is free of
  R-rank 2 with exactly two central idempotents e_+, e_-; V_- ~ unit object 1
  (the UNKNOT closure), and cor:gauge-coupling-uniqueness — up to normalisation
  there is EXACTLY ONE braid-invariant scalar coupling A (x) A -> 1 (the e_-
  channel).  That unique 2-strand singlet IS the EM slot: 1/alpha_EM =
  q [9]_q [10]_q via the genus-4 carrier pair (prop:alpha-em-categorical-
  trace-ratio).  The 7 force operators (identity/unknot + 6 cohomological basis
  knots) and their roles are prop:cohomological-embedding consequence 3 +
  force-knot-identification.

WHAT THIS PROBE DERIVES (forced, zero free choices).
  The same Schur-Weyl/Temperley-Lieb structure fixes the number of independent
  braid-invariant scalar couplings on EVERY strand count:
      dim Hom(1, A^{(x) n}) = 0            (n odd; no scalar coupling)
      dim Hom(1, A^{(x) 2m}) = Catalan(m)  (generic q, |q| > 1 real substrate
                                            regime; A = fundamental, dim_q = [2]_q)
  giving the ladder 1, 2, 5, 14, ... at n = 2, 4, 6, 8.  So:
    - n = 2: ONE coupling slot  — EM (theorem above; the unknot/trivial channel).
    - n = 4: TWO coupling slots — the unique next sector; exactly as many
      independent scalar couplings as there are remaining knot-mediated
      short-range forces (strong T_{2,9}, weak T_{3,5}) in the established role
      table.  STRUCTURAL OBSERVATION (tier: structural; selection rule
      candidate), NOT an identification of coupling values.
    - n = 6: FIVE slots (would-be sub-subshell sector; fiber degree >= 3 does
      not embed on Sigma_4 — prop:cohomological-embedding (ii) — consistent
      with no further fundamental forces).
  The n = 4 multiplicity space carries a FORCED Frobenius/TL Gram matrix in the
  cup-diagram basis {u1 = cups(12)(34), u2 = nested cups(14)(23)}:
      G = [[delta^2, delta], [delta, delta^2]],   delta = [2]_q = q + q^{-1},
  with eigenvalues delta(delta +/- 1) on the symmetric/antisymmetric
  combinations (u1 +/- u2)/sqrt(2).  This is the 4-strand analogue of the
  e_+/e_- split: the antisymmetric eigenvector is the bar-odd channel.

WHAT REMAINS OPEN (honest scope; NOT computed here).
  Mapping the two n = 4 singlet slots to (alpha_s, alpha_W) VALUES requires the
  archimedean trace-ratio functor on this 2-dim multiplicity space — the
  analogue of tr_tau(e_-) — which is gated on conj:e-hartree-categorical-
  derivation (round-18 state: intertwining correspondence; final symbolic-q
  character identity outstanding).  No coupling values are proposed and nothing
  is compared against measured alpha_s / alpha_W.

Refs: thm:em-spectral-completeness; cor:gauge-coupling-uniqueness;
prop:cohomological-embedding (consequence 3: the 7 force operators);
force-knot-identification (roles); prop:force-carrier-intertwining-
correspondence (conditional assembly mechanism);
prop:torus-knot-delta-q-writhe (delta_q = h[(m-1)k]_q).
"""
from __future__ import annotations

import sys
from fractions import Fraction
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


def trivial_multiplicity(n: int) -> int:
    """dim Hom(1, A^{(x) n}) for the SU_q(2) fundamental at generic q.

    Exact integer Clebsch-Gordan walk: m_j(k+1) = m_{j-1/2}(k) + m_{j+1/2}(k)
    on half-integer spins j >= 0 (multiplicities of V_j in A^{(x) k}).  Generic
    q (substrate regime: real q > 1, no root of unity) keeps the classical
    fusion multiplicities.  Pre-archimedean: pure integers.
    """
    if n == 0:
        return 1  # A^{(x)0} = 1, dim Hom(1, 1) = 1
    # spins stored as multiples of 1/2: index s means j = s/2
    mult = {1: 1}  # A^{(x)1} = V_{1/2}
    for _ in range(n - 1):
        nxt: dict[int, int] = {}
        for s, m in mult.items():
            for t in ((s - 1, s + 1) if s > 0 else (s + 1,)):
                nxt[t] = nxt.get(t, 0) + m
        mult = nxt
    return mult.get(0, 0)


def catalan(m: int) -> int:
    c = Fraction(1)
    for i in range(m):
        c = c * Fraction(2 * (2 * i + 1), i + 2)
    assert c.denominator == 1
    return int(c)


def main() -> None:
    w = WitnessBuilder("alpha-k-four-strand-singlet-selection", engine="python")
    q = mp.mpf(Q0) if HAVE_MP else float(Q0)
    delta = q + 1 / q  # [2]_q, the q-dimension of A

    ladder = {n: trivial_multiplicity(n) for n in range(1, 9)}
    cat_ok = all(ladder[2 * m] == catalan(m) for m in (1, 2, 3, 4))
    odd_ok = all(ladder[n] == 0 for n in (1, 3, 5, 7))

    # Forced TL Gram matrix on the n=4 multiplicity space (cup-diagram basis).
    g_diag = delta ** 2
    g_off = delta
    eig_plus = delta * (delta + 1)   # symmetric combination (u1 + u2)
    eig_minus = delta * (delta - 1)  # antisymmetric / bar-odd combination
    det_g = g_diag ** 2 - g_off ** 2
    det_ok = abs(det_g - eig_plus * eig_minus) < (mp.mpf(10) ** -40 if HAVE_MP else 1e-12)

    print("=" * 74)
    print("alpha_{basis-knot} per-force SELECTION — even-strand singlet ladder")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q, 12) if HAVE_MP else q}   delta = [2]_q = "
          f"{mp.nstr(delta, 12) if HAVE_MP else delta}")
    print()
    print("  n  dim Hom(1, A^n)   reading")
    readings = {
        2: "EM slot (thm:em-spectral-completeness — UNIQUE; the unknot channel)",
        4: "TWO slots — candidate selection space for strong + weak (structural)",
        6: "five slots (degree>=3 does not embed on Sigma_4; no further forces)",
        8: "Catalan(4) = 14 (beyond embeddability)",
    }
    for n in range(1, 9):
        note = readings.get(n, "")
        print(f"  {n}  {ladder[n]:>15d}   {note}")
    print()
    print("  Forced n=4 Gram matrix (cup basis): [[d^2, d], [d, d^2]], d = [2]_q")
    print(f"    eigen(sym)  = d(d+1) = {mp.nstr(eig_plus, 12) if HAVE_MP else eig_plus}")
    print(f"    eigen(anti) = d(d-1) = {mp.nstr(eig_minus, 12) if HAVE_MP else eig_minus}")
    print()
    print("  OPEN (not computed, gated on conj:e-hartree-categorical-derivation):")
    print("    the archimedean trace-ratio on the 2-dim n=4 slot space — the")
    print("    analogue of tr_tau(e_-) — that would yield alpha_s / alpha_W values.")
    print("    NO comparison against measured couplings is made here.")

    w.set_description(
        "alpha_{basis-knot} per-force selection scoping: the even-strand singlet "
        "ladder dim Hom(1, A^{(x) n}) = 0 (n odd) / Catalan(n/2) (n even) for the "
        "SU_q(2) fundamental at generic q (exact integer Clebsch-Gordan walk; "
        "pre-archimedean).  n=2 gives the UNIQUE EM coupling slot (matches "
        "thm:em-spectral-completeness / cor:gauge-coupling-uniqueness, the "
        "trivial/unknot channel V_- ~ 1); n=4 gives exactly TWO independent "
        "scalar-coupling slots — the same count as the remaining knot-mediated "
        "short-range forces (strong T_{2,9}, weak T_{3,5}) in the established "
        "role table (prop:cohomological-embedding consequence 3).  The forced "
        "TL Gram matrix [[d^2,d],[d,d^2]] (d=[2]_q) on the n=4 slot space has "
        "eigenvalues d(d+/-1) on the symmetric/antisymmetric (bar-odd) "
        "combinations.  Tier: structural observation / selection-rule candidate; "
        "coupling VALUES not derived (gated on conj:e-hartree-categorical-"
        "derivation); nothing compared to measured alpha_s/alpha_W (anti-fishing)."
    )
    w.set_content_block("thm:em-spectral-completeness")
    w.add_data("q0", str(q))
    w.add_data("delta_2q", str(delta))
    w.add_data("singlet_ladder", {str(n): ladder[n] for n in range(1, 9)})
    w.add_data("gram_n4_cup_basis", {
        "diag": str(g_diag), "off": str(g_off),
        "eig_symmetric_d_dplus1": str(eig_plus),
        "eig_antisymmetric_d_dminus1": str(eig_minus),
    })
    w.add_assertion(
        "n=2 singlet multiplicity = 1 (EM uniqueness, cor:gauge-coupling-uniqueness)",
        computed=bool(ladder[2] == 1), expected=True,
        source="thm:em-spectral-completeness (V_- ~ 1 unique)",
    )
    w.add_assertion(
        "n=4 singlet multiplicity = 2 (two coupling slots = two remaining knot forces)",
        computed=bool(ladder[4] == 2), expected=True,
        source="integer CG walk; Catalan(2)",
    )
    w.add_assertion(
        "even-strand ladder matches Catalan(m) for m=1..4",
        computed=bool(cat_ok), expected=True,
        source="dim Hom(1, V^{2m}) = Catalan(m), generic q",
    )
    w.add_assertion(
        "odd strand counts carry NO scalar coupling (multiplicity 0)",
        computed=bool(odd_ok), expected=True,
        source="half-integer total spin; parity obstruction",
    )
    w.add_assertion(
        "n=4 Gram det identity d^2(d^2-1) = product of eigenvalues d(d+1)d(d-1)",
        computed=bool(det_ok), expected=True,
        source="TL cup-diagram pairing, forced",
    )
    w.add_data(
        "finding",
        "Selection-rule candidate (structural, conditional): braid-invariant "
        "scalar couplings exist only at even strand counts, with multiplicity "
        "1, 2, 5 at n = 2, 4, 6.  The unique n=2 slot is the established EM "
        "coupling (the trivial/unknot channel).  The n=4 sector provides exactly "
        "two independent slots — matching the two remaining knot-mediated forces "
        "(strong T_{2,9}, weak T_{3,5}); their forced Gram structure "
        "[[d^2,d],[d,d^2]] splits into symmetric/antisymmetric channels with "
        "eigenvalues d(d+/-1).  Deriving alpha_s/alpha_W VALUES from these slots "
        "requires the archimedean trace-ratio functor on the slot space and "
        "stays gated on conj:e-hartree-categorical-derivation.  No fitting; no "
        "comparison to experiment."
    )
    w.save()
    print("\nDone. Witness saved (alpha-k-four-strand-singlet-selection).")


if __name__ == "__main__":
    main()
