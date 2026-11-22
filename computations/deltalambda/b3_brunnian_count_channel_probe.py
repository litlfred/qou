#!/usr/bin/env python3
"""The count channel gives the triple mutual energy the WRONG SIGN -- and the first
version of this probe reached that conclusion through a hypothesis its carrier fails.

Bean `qou-ix0x` (its FIRST BRICK RUN entry), companion `qou-brng`. Under `qou-x631`.

===============================================================================
CORRECTION, 2026-09-12, TO THIS PROBE'S OWN FIRST VERSION -- read this first
===============================================================================

The first version concluded "predicted b_3 = -0.627 against AME +1.4262" by citing

    QOU.Mass.CrossingModelPairLocality.b3_eq_neg_tripleMutual_of_brunnian

as though its hypothesis held for L6a4.  **It does not**, and the corpus had already
said so four days earlier.  That theorem's hypothesis was RENAMED on 2026-09-07 from
`Brunnian` to `NoIsolatedPairEnergy` precisely because two unrelated properties shared
one name.  `QOU.Mass.BrunnianTierDisambiguation` lists four tiers:

    T1  TRUE BRUNNIAN           every proper sub-link is the UNLINK
    T2  LINKING VANISHES        every pairwise Gauss linking number is 0
    T3  LINKING VANISHES AT k   the same, localised at one component
    T4  NO ISOLATED PAIR ENERGY a pair carries no mutual ENERGY in isolation

L6a4 satisfies T1 and T2.  The theorem's hypothesis is **T4**, and
`QOU.Mass.BrunnianHypothesisNotSatisfied` proves L6a4 fails it, twice over: the
corpus's own `brunnian_binding_survives` gives `0 < countChannel m m q`, and the
measured `b_2 = 2.2245662` MeV is a nonzero isolated-pair binding outright.

That file's own words: *"a correct theorem whose hypothesis L6a4 does not satisfy"*,
and the tier file's: *"on 2026-09-07 that cost a wrong reading of the three-body
binding channel: a theorem whose hypothesis is tier 4 was applied to a carrier that
satisfies only tier 2, on the strength of the shared name."*  The first version of
this probe is a second instance of the identical error, committed after the fix was
on `main` and reachable by a corpus-grep of the theorem name.

**The conclusion survives the correction and gets STRONGER, which is why the
correction is worth making carefully rather than quietly.**  Dropping T4 does not
weaken the negative -- it raises the target the count channel has to hit, from
1.4262 MeV to 8.0999 MeV, and leaves the sign failure untouched.

===============================================================================
WHAT THIS PROBE NOW DOES -- no T4 anywhere
===============================================================================

The connected cumulant is defined without any hypothesis
(`QOU.Mass.PairwiseCumulantVanishing.BindingMap.b3`):

    b_3(i,j,k) = triple(i,j,k) - ( pair(i,j) + pair(i,k) + pair(j,k) )

and the crossing model's `toBindingMap` sets `pair = -w2`, `triple = -tripleMutual`.
Substituting, with no hypothesis at all:

    b_3 = -tripleMutual + ( w2_ij + w2_ik + w2_jk )

T4 is the special case `w2 = 0`, which collapses this to `b_3 = -tripleMutual`.  We
do not need it: the corpus MEASURES both cumulants, in one witness
(`computations/probes/pair-locality-shortfall.witness.json`):

    b_2 = 2.2245662   MeV      (the isolated-pair binding; this is what refutes T4)
    b_3 = 1.42622016  MeV      (A=3 shortfall: B_AME 8.09991876 - 3 x b_2 6.6736986)

so `pair = b_2` gives `w2 = -b_2`, and the triple's TOTAL mutual energy is fixed:

    tripleMutual = -( b_3 + 3 b_2 ) = -8.09991876 MeV

which is just `-B_AME(A=3)`, as it must be.  **The corpus's own data therefore
requires a strongly ATTRACTIVE (negative) triple mutual channel**, and says how
negative.  Nothing here is fitted: both cumulants are measured, and the relation is
the definition of the cumulant.

===============================================================================
THE RESULT
===============================================================================

The count channel is strictly POSITIVE for q > 1 -- `q - q^-1 > 0` -- so under the
identification `w3 = countChannel` every `w3 > 0` and `tripleMutual > 0`.  The
requirement is `tripleMutual = -8.09991876` MeV.  **Sign wrong**, and the sign is
independent of any positive energy scale.

The magnitude misses too, and by more than the first version reported, because the
target moved up: `countChannel` is dimensionless, and the nearest candidate scale
(CAL-1 `m_e`) gives `|tripleMutual| = 0.3205` MeV against `8.0999` -- about 25x
short, where the T4 reading made it look like 4.5x.  The scale is NOT derived by
this construction; `m_e` is a candidate, not a result, and is reported so the sign
is not mistaken for the only gap.

===============================================================================
SCOPE -- read before citing
===============================================================================

Scope (a), a scope-limited negative.  UNTOUCHED: the Lean channel decomposition;
`b3_eq_neg_tripleMutual_of_brunnian` (a correct theorem, simply not applicable here);
`brunnian_binding_survives`; that L6a4 is T1/T2; that its signed channel is empty;
`countChannel` as a TERM in some other combination.  EXCLUDED: the identification
`w3 = countChannel` at `q > 1`, for this carrier.

NO FLOAT64: mpmath at 50 dps throughout; `float()` appears only inside f-strings.
"""
import sys
from pathlib import Path

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP), str(_COMP / "substrate")]

from mpmath import mp, mpf, nstr  # noqa: E402

mp.dps = 50

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV as _M_E_MEV_REGISTRY  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402  (AME registry)

# Substrate q0, proton pin (AGENTS.md owner directive 2026-08-07: proton is the default).
# Read BY NAME (reference-literal ratchet): the 17-digit literal truncated the pin.
Q0 = mpf(Q_50_DIGIT_STR)

# CAL-1 electron scale, CODATA 2022, MeV -- read from the registry. The literal
# 0.51099895000 was the CODATA-2018 value (1.35 ppb off; reference-literal ratchet).
M_E_MEV = _M_E_MEV_REGISTRY

# Both cumulants, MeV, from computations/probes/pair-locality-shortfall.witness.json.
# b_2 is the one that refutes T4; b_3 is the A=3 shortfall.
AME_B2 = AME_B_DEUTERON_MEV_VALIDATION
AME_B3 = mpf("1.42622016")
AME_B_A3 = mpf("8.09991876")            # B_AME(A=3) = b_3 + 3 b_2, checked below

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

    # -- CONTROL 2: vanishing pairwise linking (T2) empties the signed channel -----------
    sc = signed_channel(N_PLUS, N_MINUS, q)
    checks.append(("CONTROL 2: T2 (n+ = n-) => signedChannel == 0 exactly",
                   sc == 0,
                   f"signedChannel(1,1,q0) = {nstr(sc, 3)} -- so the mutual energy of a "
                   f"pair IS its count channel. This is tier T2, NOT tier T4."))

    # -- CONTROL 3: q0 > 1, so the count channel is strictly positive --------------------
    cc = count_channel(N_PLUS, N_MINUS, q)
    checks.append(("CONTROL 3: q0 > 1 => countChannel > 0",
                   q > 1 and cc > 0,
                   f"q0 = {nstr(q, 12)}, q0 - 1/q0 = {nstr(q - 1/q, 12)}, "
                   f"countChannel(1,1,q0) = {nstr(cc, 12)}. This is the corpus's own "
                   f"brunnian_binding_survives, and it is exactly why L6a4 FAILS T4."))

    # -- CONTROL 4: the cumulant arithmetic is consistent, so b_2/b_3 are usable ---------
    # B_AME(A=3) must equal b_3 + 3 b_2 -- if it does not, the two cumulants are not the
    # same decomposition and nothing below is licensed.
    recon = AME_B3 + 3 * AME_B2
    checks.append(("CONTROL 4: the witness's own cumulants reconstruct B_AME(A=3)",
                   abs(recon - AME_B_A3) < mpf("1e-8"),
                   f"b_3 + 3 b_2 = {nstr(recon, 10)} vs B_AME(A=3) = "
                   f"{nstr(AME_B_A3, 10)}, |diff| = {nstr(abs(recon - AME_B_A3), 3)}"))

    # -- WHAT THE DATA REQUIRES, with NO T4 hypothesis -----------------------------------
    # b_3 = -tripleMutual + 3 w2  and  pair = -w2 = b_2  =>  tripleMutual = -(b_3 + 3 b_2)
    w2_required = -AME_B2
    triple_mutual_required = -(AME_B3 + 3 * AME_B2)

    # -- WHAT THE COUNT-CHANNEL IDENTIFICATION GIVES -------------------------------------
    w3 = cc
    triple_mutual_pred = N_PAIRS * w3
    triple_mutual_pred_mev = triple_mutual_pred * M_E_MEV

    # -- FINDING 1: the sign is wrong, and no positive scale repairs it ------------------
    checks.append(("FINDING 1: required tripleMutual is NEGATIVE; countChannel gives POSITIVE",
                   triple_mutual_pred > 0 > triple_mutual_required,
                   f"required tripleMutual = -(b_3 + 3 b_2) = "
                   f"{nstr(triple_mutual_required, 12)} MeV (attractive); count-channel "
                   f"tripleMutual = 3(q0 - 1/q0) = {nstr(triple_mutual_pred, 12)} "
                   f"(dimensionless, repulsive). Every w3 > 0 because q0 > 1. "
                   f"SCALE-INDEPENDENT: no positive energy scale flips a sign."))

    # -- FINDING 1b: the sign failure does NOT depend on the crossing count ---------------
    # The bean asked for w3 measured INSIDE the triple, and this probe used the isolated
    # pair's numbers. That looks like the escape hatch, and it is NOT one: T2 means every
    # pairwise linking number is zero, so n+ - n- = 2 lk = 0 forces n+ = n- = m for
    # WHATEVER m the inside-the-triple count turns out to be, and
    #     countChannel(m, m, q) = m (q - 1/q) > 0  for every m >= 1.
    # Sweeping m here is not a search for a value that works -- it is a check that NO value
    # works, which is the opposite move and is what makes the negative robust.
    ms = [1, 2, 3, 5, 8, 13, 100]
    m_all_pos = all(count_channel(m, m, q) > 0 for m in ms)
    checks.append(("FINDING 1b: no crossing count repairs the sign",
                   m_all_pos,
                   f"countChannel(m,m,q0) = m(q0 - 1/q0) > 0 for every m in {ms} "
                   f"(smallest {nstr(count_channel(min(ms), min(ms), q), 9)}, largest "
                   f"{nstr(count_channel(max(ms), max(ms), q), 9)}). T2 forces "
                   f"n+ = n- = m, so re-counting crossings inside the triple cannot flip "
                   f"the sign -- it only rescales it. The residual escape is NOT the count: "
                   f"it is whether w3 has the pairEnergy shape at all."))

    # -- FINDING 2: dropping T4 RAISES the target, so the magnitude gap grows -------------
    ratio_t4 = abs(triple_mutual_pred_mev) / AME_B3          # what the first version compared
    ratio_true = abs(triple_mutual_pred_mev) / abs(triple_mutual_required)
    checks.append(("FINDING 2: dropping the T4 hypothesis makes the magnitude gap WORSE",
                   ratio_true < ratio_t4,
                   f"countChannel is DIMENSIONLESS; the nearest candidate scale is CAL-1 "
                   f"m_e = {nstr(M_E_MEV, 9)} MeV, giving |tripleMutual| = "
                   f"{nstr(abs(triple_mutual_pred_mev), 9)} MeV. Under the (inapplicable) "
                   f"T4 reading the target was b_3 = {nstr(AME_B3, 9)}, a factor "
                   f"{nstr(1/ratio_t4, 6)} short. Without T4 the target is "
                   f"{nstr(abs(triple_mutual_required), 9)} MeV, a factor "
                   f"{nstr(1/ratio_true, 6)} short. The correction costs the framework "
                   f"{nstr((1/ratio_true)/(1/ratio_t4), 4)}x more, not less. m_e is a "
                   f"candidate, not a derived scale."))

    # -- FINDING 3: T4 is refuted for this carrier, which is why the above is needed ------
    checks.append(("FINDING 3: L6a4 fails T4 (NoIsolatedPairEnergy), so b_3 = -tripleMutual "
                   "is NOT available here",
                   AME_B2 != 0 and cc > 0,
                   f"Two independent refutations, both already in the corpus: the measured "
                   f"isolated-pair binding b_2 = {nstr(AME_B2, 9)} MeV is nonzero, and "
                   f"brunnian_binding_survives gives countChannel(m,m,q0) = "
                   f"{nstr(cc, 9)} > 0. L6a4 is T1/T2, not T4 "
                   f"(QOU.Mass.BrunnianTierDisambiguation). The first version of this "
                   f"probe cited b3_eq_neg_tripleMutual_of_brunnian as if T4 held -- the "
                   f"same conflation the corpus fixed on 2026-09-07."))

    print("The triple mutual channel: what the data requires vs what the count channel gives")
    print(f"  carrier          L6a4 (Borromean rings), 3 pairs, n+ = n- = {N_PLUS} per pair")
    print(f"  tier             T1 + T2 (true Brunnian, linking 0). NOT T4.")
    print(f"  q0 (proton pin)  {nstr(q, 20)}")
    print()
    print(f"  b_2 (measured)   {nstr(AME_B2, 12):>18}   MeV   -- nonzero, so T4 FAILS")
    print(f"  b_3 (measured)   {nstr(AME_B3, 12):>18}   MeV")
    print(f"  w2 = -b_2        {nstr(w2_required, 12):>18}   MeV   -- attractive")
    print()
    print(f"  tripleMutual REQUIRED  {nstr(triple_mutual_required, 12):>12}   MeV  <-- NEGATIVE")
    print(f"  tripleMutual from cc   {nstr(triple_mutual_pred, 12):>12}   (dimensionless)")
    print(f"    ... scaled by m_e    {nstr(triple_mutual_pred_mev, 12):>12}   MeV  <-- POSITIVE")
    print()

    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"        {detail}")
    npass = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{npass}/{len(checks)} checks pass")

    print("""
VERDICT -- scope (a), and read the scope line before citing this.

REFUTED, as an identification: w3 = countChannel predicts a POSITIVE (repulsive)
triple mutual channel where the corpus's own measured cumulants require a strongly
NEGATIVE (attractive) one, -8.09991876 MeV. The failure is on the SIGN and is
therefore independent of the undetermined energy scale.

NOT refuted, and none of it is touched: the Lean channel decomposition;
b3_eq_neg_tripleMutual_of_brunnian (a correct theorem, simply not applicable to this
carrier); brunnian_binding_survives; that L6a4 is T1/T2; that its signed channel is
empty; or the count channel as one TERM in some other combination. A compositional
object is not excluded by one term of it failing alone (AGENTS.md "Before declaring
refuted"). What IS excluded is this one identification at q > 1.

WHERE THE SIGN COULD COME FROM -- stated as open questions, not as candidates to try
until one works, which would be fitting:
  (i)  the requirement is now explicit and quantitative: an ATTRACTIVE three-body
       mutual channel of -8.09991876 MeV. countChannel at q > 1 is repulsive by
       construction, so the question is what supplies attraction, not what supplies
       magnitude.
  (ii) the q < 1 branch would flip it, but the substrate pin is q0 > 1 and is not
       free (and deriving q0 is forever-gated). Not a route.
  (iii) re-counting crossings inside the triple cannot help -- FINDING 1b.

SO WHAT ACTUALLY SURVIVES: the identification presumes w3 has the PAIR-ENERGY SHAPE
n+ q - n- q^-1, i.e. that the irreducibly three-body channel is built from pairwise
crossing energies with triple-adjusted counts. If w3 is instead a genuinely 3-body
object not of that form, nothing above applies to it and the framework's 3-body
channel is simply not yet computed. That is a question about the FORM of w3, not
about its numbers. qou-ix0x stays OPEN, with the open question changed, not answered.

A NOTE ON THE TIER TRAP, because it cost this probe a wrong conclusion: the corpus
now carries QOU.Mass.BrunnianTierDisambiguation precisely so this cannot happen
again, and it happened anyway, four days after that file landed. Its rule for
authors is worth repeating here -- use "Brunnian" ONLY for T1; say "vanishing
pairwise linking" for T2/T3; say NoIsolatedPairEnergy for T4, and expect it to be
FALSE on any carrier with crossings.""")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
