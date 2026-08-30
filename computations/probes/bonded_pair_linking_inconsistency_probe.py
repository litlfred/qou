#!/usr/bin/env python3
"""The link model is inconsistent, and it undercuts a scope-(b) claim of MY OWN.

WHAT I CLAIMED, AND WHERE IT IS. `gap2_he4_borromean_mu_bar.py` (bean qou-klgu,
merged to main in 84f9d1c0a) argues:

    "For a cluster in which every bonded pair is Hopf-linked (lk = 1) -- which
     is exactly the max-contact nuclear contact graph -- the indeterminacy
     modulus is gcd(lk) = 1, so every higher mu-bar lives in Z/1 = 0."

and concludes, as a scope-(b) STRUCTURAL EXCLUSION with the Milnor
indeterminacy invariant cited, that the mu-bar realisation of M_n CANNOT carry
the 4He magic surplus. I extended the same argument to the A >= 5 deltahedra in
`gap2_irreducible_triple_bracket_probe.py` (qou-izah).

THE PREMISE IS CONTRADICTED BY THE CORPUS ITSELF, ONE FILE OVER.
`binding_mn_milnor_linking.py:188` models the TRITON as `BORROMEAN`:

    m3T, _ = analyse("triton T (Borromean 3-core)", BOR)

and BORROMEAN has pairwise lk = [0, 0, 0] (computed below, not quoted). But the
triton's contact graph is the 3-clique -- `gap2_borromean_triple_count.py` gives
it M_2 = 3, i.e. all three pairs BONDED. So the corpus models three BONDED pairs
with lk = 0, while the 4He argument requires every BONDED pair to have lk = 1.

Both cannot hold. The relation "bonded" is being assigned two different link
values in two places, and the 4He exclusion depends on which one is right.

THE DICHOTOMY, and neither branch leaves the exclusion standing:

  BRANCH 1 -- the triton model is right, bonded pairs can have lk = 0.
      Then "max-contact => all lk = 1" is false, 4He's K_4 may equally have
      lk = 0 pairs, mu-bar is determinate there, and M_3 / M_4 need NOT vanish.
      The exclusion does not follow, and the July 3-clique overshoot stands as
      the live problem.

  BRANCH 2 -- bonded really does imply lk = 1.
      Then the TRITON's triple is indeterminate too, so M_3(T) = 0, and the
      corpus's own 3-body calibration e_3 = (B(T) - 3 e_2) / M_3(T) is a
      DIVISION BY ZERO with a nonzero numerator (computed below) -- not 0/0,
      simply undefined. The 3-body energy cannot be pinned at all.

WHAT SURVIVES, PRECISELY. Milnor's indeterminacy theorem is untouched; it is a
theorem. The CONDITIONAL survives: IF every bonded pair in a cluster has
lk = 1, THEN every higher mu-bar on it is content-free. What fails is the
assertion of the HYPOTHESIS -- the corpus does not establish "max-contact =>
all bonded lk = 1", it contradicts it at the triton.

CONSEQUENCE: both qou-klgu and qou-izah must be RE-SCOPED from (b) to (a),
conditional on the link model. This is the "conditional-proved != premise-
established" failure mode in AGENTS.md, committed by me while citing an
invariant, which is exactly the case that rule exists for: the invariant was
real and its applicability was not.

Discipline: exact integer Magnus arithmetic via the corpus's own validated
module -- no floats in the topology. mpmath for the MeV arithmetic. No fit, no
witness, nothing wired. Beans qou-izah / parent qou-y2l3; corrects qou-klgu.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import mpmath as mp  # noqa: E402

import ame_2020_binding_energies as ame  # noqa: E402
import binding_mn_milnor_linking as mil  # noqa: E402

mp.mp.dps = 60


def _B(Z: int, A: int) -> mp.mpf:
    return mp.mpf(str(ame._binding_mev_exact(Z, A)))


def main() -> int:
    print("== the two link assignments, from the corpus's own machinery ==")
    bor_lk = [mil.mu(mil.BORROMEAN, s) for s in [(1, 2), (1, 3), (2, 3)]]
    bor_mu = mil.mu(mil.BORROMEAN, (1, 2, 3))
    hopf_lk = mil.mu(mil.HOPF, (1, 2))
    print(f"  BORROMEAN pairwise lk = {bor_lk}   mu-bar_123 = {bor_mu}")
    print(f"  HOPF          lk      = {hopf_lk}")
    assert bor_lk == [0, 0, 0], "Borromean pairwise lk must vanish"
    assert hopf_lk == 1, "Hopf lk must be 1"

    print()
    print("== the contradiction ==")
    print("  binding_mn_milnor_linking.py:188 models the TRITON as BORROMEAN,")
    print(f"  whose pairwise lk are {bor_lk}.")
    print("  gap2_borromean_triple_count.py gives the triton M_2 = 3, i.e. all")
    print("  three of its pairs are BONDED.")
    print("  => the corpus models 3 BONDED pairs with lk = 0.")
    print()
    print("  gap2_he4_borromean_mu_bar.py requires every BONDED pair to have")
    print("  lk = 1, and derives its scope-(b) exclusion from that.")
    print("  => 'bonded' carries two different link values in two files.")

    print()
    print("== BRANCH 2 costed: if bonded really implies lk = 1 ==")
    e2 = _B(1, 2)
    numerator = _B(1, 3) - 3 * e2
    print(f"  e_2 = B(D)          = {mp.nstr(e2, 12)} MeV")
    print(f"  B(T) - 3 e_2        = {mp.nstr(numerator, 12)} MeV  (nonzero)")
    print("  M_3(T) would be 0 (the triton triple indeterminate, like every")
    print("  other bonded triple), so")
    print("      e_3 = (B(T) - 3 e_2) / M_3(T) = nonzero / 0  -- UNDEFINED.")
    print("  Not 0/0. The corpus's 3-body calibration does not exist on this")
    print("  branch, so the branch that would save the exclusion destroys the")
    print("  quantity the exclusion is compared against.")
    assert numerator != 0, "branch-2 argument needs a nonzero numerator"

    print()
    print("== VERDICT — a correction against my own merged result ==")
    print("  Milnor indeterminacy is a THEOREM and is untouched. The")
    print("  CONDITIONAL survives: if every bonded pair has lk = 1, every")
    print("  higher mu-bar on that cluster is content-free.")
    print()
    print("  What fails is asserting the HYPOTHESIS. The corpus does not")
    print("  establish 'max-contact => all bonded lk = 1'; it contradicts it")
    print("  at the triton, which is the very nucleus e_3 is pinned on.")
    print()
    print("  So qou-klgu (4He, merged) and qou-izah (A >= 5) are RE-SCOPED")
    print("  from (b) to (a): conditional on the link model, not structural")
    print("  exclusions. This is 'conditional-proved != premise-established',")
    print("  committed by me while citing a real invariant whose applicability")
    print("  I did not check.")
    print()
    print("  The open question this promotes: WHAT FIXES THE LINKING NUMBER")
    print("  OF A BONDED PAIR?")
    print()
    print("  ANSWERED, same day, by bonded_pair_linking_from_canonical_braid")
    print("  _probe.py (qou-k12x): the CANONICAL BRAID WORD fixes it, and it")
    print("  fixes it NON-UNIFORMLY. 4He's three interfaces are sigma (+1),")
    print("  averaged_weighted (no sign), sigma_inv (-1). So BRANCH 1 and")
    print("  BRANCH 2 above are BOTH false -- neither uniform model is what")
    print("  the canonical word contains -- and the p-n interface")
    print("  sigma - h(1/2-delta/4).1 is not in the braid group at all, so it")
    print("  has no classical linking number. The unforced choice is the")
    print("  CLASSICALISATION, not the value.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
