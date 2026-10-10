#!/usr/bin/env python3
"""Which third coefficient of thm:wedderburn-mass-formula is derivable?

The published formula reads

    m(Z,N) = Z*m_p + N*m_n + Z*m_e + alpha*( Phi_1 - 2[3]_q*Phi_2 + h_A^2*Phi_3 )

The recovered witness `atom-mass-complete-wedderburn` (added 2026-04-10 in
1359fe23ac under folio-assistant/computations/, recovered 2026-08-25) records
`beta3 = 0.0499` where the formula says `h_A^2 = 0.043707282` -- 14.2 % apart.
docs/audits/2026-08-25-...-witness-recovered.md left which of the two is
correct as an open authoring question, on the ground that "the artifact cannot
distinguish the two".

The artifact is not the only evidence.  DERIVABILITY distinguishes them, and
that is measurable without fitting anything.  This probe measures it.

The one surviving producer of `0.0499` is
fsh-guts/deprecated/computations/next_partition_levels.py, which hardcodes

    BETA3 = 0.0499        # comment: "(from Wedderburn weights)"

while the sibling coefficients in the SAME block are genuinely computed:

    BETA4 = -0.5 * wedderburn_weight((2,2))
    BETA5 = -0.5 * (w((3,2)) + w((3,1,1)) + w((2,2,1)))

with `wedderburn_weight(lam) = dim_q(lam)^2 / [n]_q!`.  So that comment makes a
checkable claim: 0.0499 should be reachable from the n=3 Wedderburn weights by
the same construction its own siblings use.

ANTI-FIT DISCIPLINE.  A wide enough search finds a 3-digit match by chance, so
the candidate set here is PRE-DECLARED and CLOSED: exactly the forms the file's
own sibling coefficients use, applied at n=3.  Nothing is added after seeing a
miss.  The chance-match probability of the set is reported alongside the result.

RESULT (measured, this file, 50 dps):

1. h_A^2 IS DERIVED, and it is a q-integer expression.  The identity
   (q - 1/q)^2 = q^2 + q^-2 - 2 = [3]_q - 3 is exact, so the formula's second
   and third coefficients are BOTH built from [3]_q:  -2[3]_q  and  [3]_q - 3.

2. THE PUBLISHED DIGITS WERE COMPUTED AT A ROUNDED q0, and this is worth
   separating from (1).  `0.043707282` is (q-1/q)^2 at q = 1.10998 exactly --
   agreeing to 2.05e-9, i.e. to all nine published digits.  At either real pin
   it is 0.04370621 (proton) or 0.04370622 (muon), both 2.4e-5 away.  The
   mu-p gap is 1.2e-8 in q and cannot account for that; five-decimal rounding
   can and does.  So the published NUMBER carries a 2.4e-5 precision defect
   while the published CONSTRUCTION is exact.  A rounded input is not a fit.

3. beta3 = 0.0499 IS UNATTRIBUTED.  None of the 16 pre-declared candidates
   reaches it; the closest misses by 63.7 % against a 0.1 % acceptance window
   for a 3-digit literal.  The comment "(from Wedderburn weights)" in
   next_partition_levels.py is not supported by the construction its own
   sibling coefficients use.

4. CONTROLS BOTH PASS, so the recorded parameters are being read correctly:
   beta2 = -2[3]_q matches to 4.2e-7, and Vol_B3 = 8G matches to 1.6e-17.

   On Vol_B3: docs/audits/2026-08-25-...-witness-recovered.md calls this field
   "mislabelled: this is exactly 8G, not a volume".  THAT IS WRONG.
   Vol(Borromean) = 2*V_oct = 8G is an identity, and the corpus's own
   binding_link_volumes.py:112 sets VOL_B3 = 8*catalan under the comment
   "Vol(L6a4) = 8G = Vol(Borromean)".  The field is correctly labelled.

WHAT THIS SETTLES.  The audit doc left "either the published h_A^2 is wrong or
beta3 is an undocumented parameter" open on the ground that the artifact cannot
distinguish them.  Derivability distinguishes them: one coefficient has an
exact construction and the other has none.  The published formula is the
derivable one, and the table was not its output.

SCOPE (a), not (b): the pre-declared set does not reach 0.0499.  Some other
construction might; nothing is excluded.  What is established is the asymmetry.

NOT DONE, deliberately: no reconstruction of beta3, no adjustment of the
published formula, no re-derivation of the table.  Owner directive 2026-08-25
("no fitting!!!") forbids the fit; it does not license a replacement invented
here.  Re-publishing h_A^2 at an unrounded q0 is an authoring change and is
left to the author.
"""

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))

mp.mp.dps = 50

from q_parameter import q_at  # noqa: E402  (proton pin: standing directive)

Q = q_at(50)
QI = mp.mpf(1) / Q

# ---- published / recorded constants, as literal strings ----------------
PUB_HA2 = mp.mpf("0.043707282")          # h_A^2, published in the formula
REC_BETA3 = mp.mpf("0.0499")             # witness `beta3`
REC_BETA2 = mp.mpf("-6.087415")          # witness `beta2`
REC_VOL_B3 = mp.mpf("7.327724753417752")  # witness `Vol_B3`
Q_MUON = mp.mpf("1.10997859555733471")    # ideal/CAL-2 pin, for contrast only
Q_ROUNDED = mp.mpf("1.10998")             # q0 as the witness records it


def q_int(k):
    """[k]_q = (q^k - q^-k)/(q - q^-1)."""
    return (Q ** k - QI ** k) / (Q - QI)


def q_factorial(n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= q_int(k)
    return r


def hooks(partition):
    """Hook lengths of every cell of a Young diagram."""
    conj = [sum(1 for r in partition if r > c) for c in range(partition[0])]
    out = []
    for i, row in enumerate(partition):
        for j in range(row):
            out.append(row - j + conj[j] - i - 1)
    return out


def q_dim(partition):
    """dim_q(lam) = [n]_q! / prod_cells [hook]_q  (q-hook-length formula)."""
    n = sum(partition)
    d = q_factorial(n)
    for h in hooks(partition):
        d /= q_int(h)
    return d


def wedderburn_weight(partition):
    """w_lam = dim_q(lam)^2 / [n]_q!  -- verbatim from next_partition_levels.py."""
    return q_dim(partition) ** 2 / q_factorial(sum(partition))


def rel(a, b):
    return abs(a - b) / abs(b)


def main():
    print("=" * 72)
    print("beta3 vs h_A^2 -- which third coefficient is DERIVABLE?")
    print("=" * 72)
    print(f"q0 (proton pin) = {mp.nstr(Q, 20)}   [50 dps throughout]\n")

    # -- 1. is h_A^2 structural? -----------------------------------------
    ha = Q - QI
    ha2 = ha ** 2
    print("1. h_A^2 = (q - 1/q)^2 = [3]_q - 3, the skein parameter squared")
    print(f"   identity check   [3]_q - 3 - (q-1/q)^2 = {mp.nstr(q_int(3) - 3 - ha2, 3)}")
    print(f"   at proton pin          = {mp.nstr(ha2, 15)}   dev {mp.nstr(rel(ha2, PUB_HA2) * 100, 3)} %")
    ha2_muon = (Q_MUON - 1 / Q_MUON) ** 2
    print(f"   at muon pin            = {mp.nstr(ha2_muon, 15)}   dev {mp.nstr(rel(ha2_muon, PUB_HA2) * 100, 3)} %")
    ha2_round = (Q_ROUNDED - 1 / Q_ROUNDED) ** 2
    print(f"   at rounded q=1.10998   = {mp.nstr(ha2_round, 15)}   dev {mp.nstr(rel(ha2_round, PUB_HA2) * 100, 3)} %")
    print(f"   published              = {mp.nstr(PUB_HA2, 15)}")
    h = mp.sqrt(PUB_HA2)
    print(f"   -> q implied by the published digits = {mp.nstr((h + mp.sqrt(h ** 2 + 4)) / 2, 15)}")
    print("   -> the published DIGITS are (q-1/q)^2 at a 5-decimal-ROUNDED q0")
    print("      (2.05e-9, all 9 digits); the mu-p gap is 1.2e-8 in q and cannot")
    print("      explain a 2.4e-5 miss.  Construction exact, input rounded.")

    # -- 2. beta2 cross-check: the recorded params ARE being read right ---
    b2 = -2 * q_int(3)
    print("\n2. control: beta2 = -2[3]_q  (recorded -6.087415)")
    print(f"   computed  = {mp.nstr(b2, 15)}")
    print(f"   rel.dev   = {mp.nstr(rel(b2, REC_BETA2), 3)}"
          f"   -> {'MATCHES at the recorded 7 digits' if rel(b2, REC_BETA2) < mp.mpf('1e-6') else 'DOES NOT MATCH'}")

    # -- 3. Vol_B3: is the field mislabelled? ----------------------------
    vol_b3 = 8 * mp.catalan
    print("\n3. control: Vol_B3 = 8G  (recorded 7.327724753417752)")
    print(f"   8*Catalan = {mp.nstr(vol_b3, 17)}")
    print(f"   rel.dev   = {mp.nstr(rel(vol_b3, REC_VOL_B3), 3)}")
    print("   Vol(Borromean) = 2*V_oct = 8G is an identity, and the corpus's own")
    print("   binding_link_volumes.py:112 sets VOL_B3 = 8*catalan.  The field is")
    print("   CORRECTLY labelled: 8G IS the Borromean volume.")

    # -- 4. is 0.0499 reachable from n=3 Wedderburn weights? -------------
    print("\n4. is beta3 = 0.0499 a Wedderburn-weight construction at n=3?")
    parts3 = [(3,), (2, 1), (1, 1, 1)]
    weights = {p: wedderburn_weight(p) for p in parts3}
    print("   n=3 Wedderburn weights w_lam = dim_q(lam)^2 / [3]_q!:")
    for p, w in weights.items():
        print(f"     w_{str(p):<10} = {mp.nstr(w, 12)}")
    tot = sum(weights.values())
    print(f"     sum          = {mp.nstr(tot, 12)}")

    # PRE-DECLARED closed candidate set: exactly the forms BETA4/BETA5 use,
    # plus the bare weight and its sign flip.  Nothing added after the fact.
    candidates = []
    for p, w in weights.items():
        candidates.append((f"-0.5 * w_{p}", -w / 2))
        candidates.append((f"+0.5 * w_{p}", w / 2))
        candidates.append((f"      w_{p}", w))
        candidates.append((f"     -w_{p}", -w))
    candidates.append(("-0.5 * sum_lam w_lam", -tot / 2))
    candidates.append(("+0.5 * sum_lam w_lam", tot / 2))
    candidates.append(("      sum_lam w_lam", tot))
    candidates.append(("     -sum_lam w_lam", -tot))

    print("\n   pre-declared candidate set (the forms BETA4/BETA5 use, at n=3):")
    best = None
    for name, val in candidates:
        d = rel(val, REC_BETA3)
        if best is None or d < best[2]:
            best = (name, val, d)
        print(f"     {name:<22} = {mp.nstr(val, 10):>16}   dev vs 0.0499: {mp.nstr(d * 100, 4)} %")

    # a 3-digit literal accepts anything within +-0.5 in the last place
    window = mp.mpf("0.00005") / REC_BETA3
    print(f"\n   acceptance window for a 3-digit literal: +-{mp.nstr(window * 100, 3)} %")
    print(f"   candidates tested: {len(candidates)}")
    print(f"   closest candidate: {best[0].strip()} at {mp.nstr(best[2] * 100, 4)} % deviation")

    hit = best[2] < window
    print("\n" + "=" * 72)
    print("VERDICT")
    print("=" * 72)
    if hit:
        print("  0.0499 IS reachable in the pre-declared set -- see above.")
    else:
        print("  0.0499 is NOT reachable in the pre-declared set.  The closest of")
        print(f"  {len(candidates)} candidates misses by {mp.nstr(best[2] * 100, 4)} %, against a "
              f"{mp.nstr(window * 100, 3)} % window.")
        print("  So the comment '(from Wedderburn weights)' in next_partition_levels.py")
        print("  is not supported by the construction its own siblings use.")
    print()
    print("  h_A^2  : DERIVED -- exactly (q-1/q)^2 = [3]_q - 3.  Its published")
    print("           digits were evaluated at a rounded q0 (2.4e-5 precision")
    print("           defect); the construction itself is exact.")
    print(f"  0.0499 : UNATTRIBUTED -- 3 significant figures, no construction found,")
    print(f"           recorded beside \"fitted\": 0")
    print(f"  ratio beta3/h_A^2 = {mp.nstr(REC_BETA3 / ha2, 8)}")
    print()
    print("  SCOPE (a): this pre-declared set does not reach 0.0499.  Some other")
    print("  construction might; nothing is excluded.  What IS established is an")
    print("  asymmetry -- one coefficient has a derivation and the other has none.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
