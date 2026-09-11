#!/usr/bin/env python3
"""b_3 from the Brunnian count channel: the framework's own prediction, and it FAILS ON SIGN.

Bean `qou-ix0x` (its FIRST BRICK RUN entry), companion `qou-brng`. Under `qou-x631`.

WHAT THE BEAN ASKED FOR, verbatim:

    compute `w3` for L6a4 -- the mutual crossing energy of a pair measured *inside the
    triple* -- and check `-(w3 ijk + w3 ikj + w3 jki)` against `+1.4262225 MeV`.

and calls it "a PREDICTION, not a fit ... `w3` is determined by the carrier's crossing
structure, and `b_3` is measured. Nothing is tuned."  That is right, and it is exactly why
the result below is worth recording: the prediction is falsifiable and it is falsified, on
a sign, before any question of magnitude arises.

THE INPUTS, none of them chosen here.

  * The carrier is `L6a4` = the Borromean rings (`computations/binding_link_volumes.py`:
    "L6a4 IS the Borromean link", Vol = 8G = 7.3277248), the 3He/4He building block.
  * It is BRUNNIAN: every pairwise Gauss linking number is zero. In the standard 6-crossing
    diagram each of the 3 component pairs carries 2 inter-component crossings, and lk = 0
    forces n_+ = n_- = 1 on each pair.
  * The channel split is PROVED in Lean, sorry-free
    (`QOU.Mass.BrunnianBindingChannel`, mirroring `QOU.Braiding.CrossingEnergy.decomposition`):

        pairEnergy(n+,n-,q)    = n+ q - n- q^-1
        signedChannel(n+,n-,q) = (n+ - n-)(q + q^-1)/2      <- writhe = 2 lk
        countChannel(n+,n-,q)  = (n+ + n-)(q - q^-1)/2      <- crossing COUNT

    and `brunnian_signedChannel_zero` gives signedChannel(m,m,q) = 0, so on a Brunnian pair
    the mutual energy IS the count channel.
  * `b_3 = -tripleMutual` on a Brunnian carrier is likewise PROVED
    (`QOU.Mass.CrossingModelPairLocality.b3_eq_neg_tripleMutual_of_brunnian`), with its own
    docstring: "No pair contamination and no free constant".
  * The target is AME2020's `b_3 = +1.4262225` MeV (`AmeBindingNotPairwise.ame_b3_eq`).

THE RESULT.  The count channel is strictly POSITIVE for q > 1 -- `q - q^-1 > 0` -- so every
`w3` is positive, `tripleMutual` is positive, and `b_3 = -tripleMutual` is NEGATIVE.  AME
measures it POSITIVE.  The disagreement is in the sign and is independent of any energy
scale: no positive scale factor can repair it.

That is a scope-(a) negative about THIS construction -- `b_3 = -(unsigned count channel)`
on the Brunnian carrier -- and it is NOT a structural exclusion of the count channel, of
the Brunnian carrier, or of `b3_eq_neg_tripleMutual_of_brunnian`, which is a theorem and
stays true.  What it excludes is the identification of `w3` with `countChannel` at q > 1.

AND THE MAGNITUDE WAS NEVER DETERMINED ANYWAY -- report this too, or the sign result reads
as the only problem.  `countChannel` is DIMENSIONLESS; turning it into MeV needs a scale
this construction does not supply.  The probe prints the two obvious candidates (the CAL-1
electron scale `m_e`, and `m_e` times nothing else) and shows the |b_3| they give, so the
size of the second gap is on the record alongside the first.  A probe that reported only
"sign wrong" would hide that even the sign-corrected magnitude misses by ~4.5x.

NO FLOAT64: mpmath at 50 dps throughout; `float()` appears only inside f-strings.
"""
import sys

from mpmath import mp, mpf, nstr

mp.dps = 50

# Substrate q0, proton pin (AGENTS.md owner directive 2026-08-07: proton is the default).
Q0 = mpf("1.1099785827513808")

# CAL-1 electron scale, CODATA, MeV.
M_E_MEV = mpf("0.51099895000")

# AME2020 connected 3-body cumulant, MeV (QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq).
AME_B3 = mpf("1.4262225")

# L6a4 = Borromean: 3 component pairs, 2 inter-component crossings each, lk = 0 => n+ = n- = 1.
N_PLUS, N_MINUS = 1, 1
N_PAIRS = 3


def pair_energy(np_, nn, q):
    return mpf(np_) * q - mpf(nn) / q


def signed_channel(np_, nn, q):
    return (mpf(np_) - mpf(nn)) * (q + 1 / q) / 2


def count_channel(np_, nn, q):
    return (mpf(np_) + mpf(nn)) * (q - 1 / q) / 2


def main():
    checks = []
    q = Q0

    # -- CONTROL 1: the Lean decomposition identity, re-derived numerically --------------
    lhs = pair_energy(N_PLUS, N_MINUS, q)
    rhs = signed_channel(N_PLUS, N_MINUS, q) + count_channel(N_PLUS, N_MINUS, q)
    checks.append(("CONTROL 1: pairEnergy == signedChannel + countChannel",
                   abs(lhs - rhs) < mpf(10) ** -45,
                   f"|lhs - rhs| = {nstr(abs(lhs - rhs), 3)} at q0"))

    # -- CONTROL 2: Brunnian empties the signed channel ----------------------------------
    sc = signed_channel(N_PLUS, N_MINUS, q)
    checks.append(("CONTROL 2: Brunnian (n+ = n-) => signedChannel == 0 exactly",
                   sc == 0,
                   f"signedChannel(1,1,q0) = {nstr(sc, 3)} -- so the mutual energy IS the "
                   f"count channel, which is the whole premise"))

    # -- CONTROL 3: q0 > 1, so the count channel is strictly positive --------------------
    cc = count_channel(N_PLUS, N_MINUS, q)
    checks.append(("CONTROL 3: q0 > 1 => countChannel > 0",
                   q > 1 and cc > 0,
                   f"q0 = {nstr(q, 12)}, q0 - 1/q0 = {nstr(q - 1/q, 12)}, "
                   f"countChannel(1,1,q0) = {nstr(cc, 12)}"))

    # -- THE PREDICTION ------------------------------------------------------------------
    w3 = cc                                   # one pair's mutual energy inside the triple
    triple_mutual = N_PAIRS * w3              # w3 ijk + w3 ikj + w3 jki, equal by symmetry
    b3_dimensionless = -triple_mutual         # b3_eq_neg_tripleMutual_of_brunnian
    b3_me_scaled = b3_dimensionless * M_E_MEV

    # -- FINDING 1: the sign is wrong, and no positive scale repairs it ------------------
    checks.append(("FINDING 1: predicted b_3 is NEGATIVE; AME measures it POSITIVE",
                   b3_dimensionless < 0 < AME_B3,
                   f"b_3(pred, dimensionless) = -3(q0 - 1/q0) = {nstr(b3_dimensionless, 12)}; "
                   f"AME b_3 = +{nstr(AME_B3, 8)} MeV. Every w3 > 0 because q0 > 1, so "
                   f"tripleMutual > 0 and b_3 = -tripleMutual < 0. SCALE-INDEPENDENT: no "
                   f"positive energy scale can flip it."))

    # -- FINDING 1b: the sign failure does NOT depend on the crossing count ---------------
    # The bean asked for w3 measured INSIDE the triple, and this probe used the isolated
    # pair's numbers.  That looks like the escape hatch, and it is NOT one: Brunnian means
    # every pairwise linking number is zero, so n+ - n- = 2 lk = 0 forces n+ = n- = m for
    # WHATEVER m the inside-the-triple count turns out to be, and
    #     countChannel(m, m, q) = m (q - 1/q) > 0  for every m >= 1.
    # Sweeping m here is not a search for a value that works -- it is a check that NO value
    # works, which is the opposite move and is what makes the negative robust.
    ms = [1, 2, 3, 5, 8, 13, 100]
    m_all_pos = all(count_channel(m, m, q) > 0 for m in ms)
    checks.append(("FINDING 1b: no Brunnian crossing count repairs the sign",
                   m_all_pos,
                   f"countChannel(m,m,q0) = m(q0 - 1/q0) > 0 for every m in {ms} "
                   f"(smallest {nstr(count_channel(min(ms), min(ms), q), 9)}, largest "
                   f"{nstr(count_channel(max(ms), max(ms), q), 9)}). Brunnian forces "
                   f"n+ = n- = m, so re-counting crossings inside the triple cannot flip "
                   f"the sign -- it only rescales it. The residual escape is NOT the count: "
                   f"it is whether w3 has the pairEnergy shape at all."))

    # -- FINDING 2: the magnitude was never determined either ----------------------------
    ratio = abs(b3_me_scaled) / AME_B3
    checks.append(("FINDING 2: even |b_3| misses -- the construction supplies no MeV scale",
                   True,
                   f"countChannel is DIMENSIONLESS. Scaling by CAL-1 m_e = "
                   f"{nstr(M_E_MEV, 9)} MeV gives |b_3| = {nstr(abs(b3_me_scaled), 9)} MeV "
                   f"against AME {nstr(AME_B3, 8)} -- a factor {nstr(1/ratio, 6)} short. "
                   f"The scale is NOT derived by this construction; m_e is the nearest "
                   f"candidate, not a result. Reporting it so the sign is not the only "
                   f"gap on the record."))

    print("b_3 from the Brunnian unsigned count channel on L6a4 (= Borromean rings)")
    print(f"  carrier          L6a4, 3 pairs, n+ = n- = {N_PLUS} per pair (lk = 0, Brunnian)")
    print(f"  q0 (proton pin)  {nstr(q, 20)}")
    print()
    print(f"  signedChannel    {nstr(sc, 12):>18}   (zero: Brunnian)")
    print(f"  countChannel     {nstr(cc, 12):>18}   = w3 per pair")
    print(f"  tripleMutual     {nstr(triple_mutual, 12):>18}   = 3 * w3")
    print(f"  b_3 (predicted)  {nstr(b3_dimensionless, 12):>18}   = -tripleMutual   <-- NEGATIVE")
    print(f"  b_3 (AME2020)    {nstr(AME_B3, 12):>18}   MeV              <-- POSITIVE")
    print()

    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"        {detail}")
    npass = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{npass}/{len(checks)} checks pass")

    print("""
VERDICT -- scope (a), and read the scope line before citing this.

REFUTED, as an identification: w3 = countChannel on the Brunnian carrier predicts
b_3 < 0 where AME measures b_3 > 0. The failure is on the SIGN and is therefore
independent of the undetermined energy scale.

NOT refuted, and none of it is touched: the Lean channel decomposition; the theorem
b3_eq_neg_tripleMutual_of_brunnian; that L6a4 is Brunnian; that the signed channel is
empty on it; or the count channel as an ingredient in some other combination. A
compositional object is not excluded by one term of it failing alone (AGENTS.md
"Before declaring refuted"). What IS excluded is this one identification at q > 1.

WHERE THE SIGN COULD COME FROM -- stated as open questions, not as candidates to try
until one works, which would be fitting:
  (i)  b_3 = -tripleMutual carries a sign convention; if binding is -(mutual energy)
       then a POSITIVE b_3 needs a NEGATIVE mutual energy, i.e. an attractive channel,
       and countChannel at q > 1 is repulsive by construction.
  (ii) the q < 1 branch would flip it, but the substrate pin is q0 > 1 and is not free.
  (iii) w3 is the pair energy measured INSIDE the triple; this probe used the isolated
       pair's crossing numbers.  This is the obvious escape and FINDING 1b closes it:
       Brunnian forces n+ = n- = m, so any inside-the-triple count still gives
       m(q0 - 1/q0) > 0.  Re-counting rescales the answer; it cannot flip it.

SO WHAT ACTUALLY SURVIVES is narrower and sharper than "measure it inside the triple":
the identification w3 = countChannel presumes w3 has the PAIR-ENERGY SHAPE -- that the
irreducibly three-body channel is a sum of pairwise crossing energies with triple-adjusted
counts.  If w3 is instead a genuinely 3-body object not of the form n+ q - n- q^-1, then
nothing above applies to it and the framework's 3-body channel is simply not yet computed.
That is the real gap, and it is a question about the FORM of w3, not about its numbers.
qou-ix0x stays OPEN, with the open question changed, not answered.""")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
