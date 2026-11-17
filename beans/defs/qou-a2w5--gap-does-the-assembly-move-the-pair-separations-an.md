---
# qou-a2w5
title: 'GAP: does the assembly move the pair separations, and by how much — route (2)''s entire many-body content, unmeasurable until a nucleus has a derived geometry'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T19:14:01Z
updated_at: 2026-10-04T15:19:57Z
parent: qou-v2om
---

Extracted from `qou-o6ml` §"CONSTRAINT 3b" (2026-09-13, MobiusMutualChannel.lean
section 9g), which names this in one sentence and gives it no tracker. It is the
arc's one precisely-stated open problem and it was sitting in a 1,856-line bean.

## The statement, and it is a theorem not a hope

`mobius_b3_ne_zero_forces_moved_sep` (sorry-free, `[propext, Classical.choice,
Quot.sound]`; file 52/52, `lean -DautoImplicit=false -s 65536` exit 0):

> Any nonzero `b_3` from the Mobius mutual channel is **entirely** the
> assembly's effect on the pair separations.

Contrapositive of `mobius_b3_eq_zero_of_sep_eq`, which routes through
`b3_eq_zero_of_pairLocal`: if the assemblies do not move the pair's
separations, `b_3` vanishes identically.

AME2020 gives `b_3 = +1.4262225` MeV (`AmeBindingNotPairwise.ame_b3_eq`) — the
**isospin average** of the A = 3 doublet, and specifically the *strong* channel's
half of the charge split; see the CORRECTION section below, which also retracts
this paragraph's original second sentence. Since that figure is **nonzero**, the
`sep_eq` hypothesis is refuted for the physical system: something must move, or
route (2) contributes nothing to the extensive term. The channel itself supplies
**no number** — `mobius_b3_eq_zero_of_sep_eq` is conditional and its antecedent
is exactly what is open.

**THE OPEN QUESTION, verbatim from section 9g:** *"NOT CLAIMED: that the
assemblies DO move the separations in this framework, nor by how much. That is
a geometric measurement section 9g does not make, and it is the open thing."*

## WHY IT CANNOT BE MEASURED TODAY — checked, not assumed

`sep` is a **bare field** of `LinkEmbedding` (`MobiusEnergy.lean:228`):

    sep : Fin n -> Real -> Fin n -> Real -> Real

carrying only axioms — `sep_symm`, `sep_nonneg`, `disjoint`, `sep_self`. No
derivation. To ask whether an assembly moves the separations you need a
**concrete configuration per assembly**, and the corpus has none.

Measured: every concrete `LinkEmbedding` in the tree is a synthetic test family.

  shrinkingLink      MobiusMutualChannel.lean:165   a COUNTEREXAMPLE (no uniform
                                                    separation exists for it)
  separatedLink m R  MobiusMutualChannel.lean:1025  a PARAMETERISED family, used
                                                    to prove no positive uniform
                                                    lower bound exists
  Nonempty (LinkEmbedding M n)  MobiusEnergy.lean:323   an existence witness

**None of them is a nucleus.** Nothing in the corpus says "this is 3He's
geometry".

## SO THIS IS THE SIXTH RELOCATION TO THE SAME BLOCKER — but its SHAPE changed

Routes (1), (2), (4), the flux leg and the upper-bound leg all terminate at
"the framework has no derived geometric realisation of a nucleus". This makes
six. Recording that plainly so nobody reads this bean as an independent front.

**But what is needed is NOT what the volume route needed, and that difference is
the actionable part.** The carrier blocker was *which census link is the nucleus*
— a **topological type**, for a hyperbolic-volume lookup. This needs a canonical
**metric configuration**: separations, not volume. Two consequences:

1. **The `A+1` closure being non-geometric does NOT disqualify it here**
   (`qou-mbbf`: every atom non-hyperbolic, volume exactly 0, all six
   word/averaging settings). A non-hyperbolic link still embeds in `R^3` with
   perfectly good separations; it just carries no canonical hyperbolic metric.
   So the measurement that closed the *volume* route does not close this one.
2. **The requirement is strictly weaker than the volume route's** — and that is
   the one direction this arc has not been pushed.

## WHOSE IT IS

Section 9g's own conclusion: *"the route's deliverable is the same object
`qou-ales` is deriving (gamma-gamma + the confinement SDP at q_0), not a separate
one."* That matches `qou-mbbf`'s independent arrival from the carrier side — two
routes, one conclusion, reached the same day without contact.

`qou-ales` selects **words** (`beta_Bor`, the H_6 bond `G^3`) and has never been
asked for a **geometry**. Whether it can be is a framing question for that bean,
not this one.

## NOT CLAIMED

That the assemblies do or do not move the separations (unmeasured — that IS the
gap); that a geometry is derivable from a gamma-gamma-selected word; that route
(2) is dead (it is not — section 9g is a specification of what it owes, not a
refutation); or that this bean is independently workable today (it is not, and
the "why" above is the point).

## CROSS-LINKS

  qou-o6ml   the arc; CONSTRAINT 3 and 3b are its two newest entries
  qou-dux3   completed — the FHW route end to end, "empty where we need it"
  qou-mbbf   the A+1 component law + the non-geometricity measurement
  qou-ales   gamma-gamma + confinement SDP; owns the derived-object question
  qou-brng / qou-rwhv / qou-eptr   the b_3 extensive-term front (all in-progress)


---

## CORRECTION 2026-09-13 — "the model gives exactly 0" was WRONG, and it is the conditional-proved defect

**What I asserted**, above and in issue #7338 and PR #7339: *"AME2020 gives
`b_3 = +1.4262225` MeV; the model gives exactly **0**."*

**What is actually true.** The Mobius mutual channel produces **no number at
all**. `mobius_b3_eq_zero_of_sep_eq` is a **conditional** vanishing — its
hypotheses are `h3` and `h4`, that the triple and quad assemblies agree with the
isolated pair on the separations, pointwise. Nothing in the corpus establishes
those hypotheses; section 9g says so in the sentence this bean already quotes
verbatim: *"NOT CLAIMED: that the assemblies DO move the separations."*

So I restated a conditional lemma's antecedent as an established model fact.
That is exactly the **"Conditional-proved != premise-established"** defect
AGENTS.md carries a STRICT section for, committed in the bean that exists to
record a conditional result.

**Consequences that also have to go.**

* There is **no 1.43 MeV discrepancy** in this channel. 1.4262225 is the AME
  side; the model side of *this* channel is **undetermined**, not zero. A
  discrepancy needs two numbers.
* The framing "converts a 1.43 MeV discrepancy into a well-posed question" is
  wrong in the same way. What section 9g actually converts is the **nonzero-ness**
  of the measured `b_3` into a **refutation of the `sep_eq` hypothesis for the
  physical system** — the measurement tells you the separations *must* move; it
  does not tell you the model says they do not.

**A DIFFERENT model channel does give a number, and I should not have implied
it was this one.** The multiplicative assembly (Mayer/Ursell, `qou-rwhv` /
`qou-rraz`) gives, at the live chain bonds, `b_3 = -1.2277` MeV (3H) and
`-0.7973` MeV (3He) — isospin average **`-1.0125`** MeV. Nonzero, and with the
**wrong sign** against AME's `+1.4262225`. Two channels, two different `b_3`
behaviours; conflating them under "the model" is the overloaded-symbol trap.

## PROVENANCE OF 1.4262225 — say it when you quote it

It is **not** a single nucleus. It is the **isospin average / charge-symmetric
part** of the A = 3 doublet:

    b_3(3H)  = 8.481798 - 3*e_2 = 1.808100
    b_3(3He) = 7.718058 - 3*e_2 = 1.044360   (e_2 = B(2H) = 2.224566)
    mean                        = 1.426230

matching the quoted `1.4262225` to 8e-6 MeV (the residual is AME input
precision — it implies `B(2H) = 2.2245687` vs `2.2245660`, 2.7 eV). Verified by
recomputation this session. Each single-nucleus alternative is 26.8% away, so
the identification is not a coincidence. Recorded independently in
`PairwiseCumulantVanishing.lean:68-104`.

**Do not compare it to a triton-pinned `e_3`**: the body-order tower pins
`e_3 = 1.808100` on 3H alone. The two differ by 27% by convention, not by error.

## AND THE SPLIT MATTERS TO THIS ARC SPECIFICALLY

`qou-9v7t` (2026-08-29, PR #5990,
`computations/b3-charge-decomposition-a3.witness.json`) had already split the
A = 3 doublet and named the halves:

| part | value (MeV) | named |
|---|---|---|
| `b3_sym`  | 1.4262225 | *"the strong channel's obligation"* |
| `b3_asym` | 0.3818775 | *"the EM channel's"* |

`qou-o6ml` is the **EM-linking** arc. So the figure this arc owes is plausibly
`b3_asym = 0.3818775`, **not** the 1.4262225 quoted above — which belongs to the
strong channel. Flagged, not concluded: whether route (2)'s `b_3` is the sym
part, the asym part, or neither is a further read of `mobiusCrossingModel`, and
I have not made it. Followed up on `qou-o6ml`.

## ONE SHARPENING THAT SURVIVES, and it is stronger than what I wrote

I wrote that all three concrete `LinkEmbedding`s are synthetic. True, and the
arity is the sharper fact: section 9g needs `LinkEmbedding M 4` — **six** of
them (`Lpair`, `Ltriple k` for `k : Fin 4`, `Lquad`) — and both named concrete
families are `LinkEmbedding M 2`:

* `MobiusMutualChannel.lean:165` `shrinkingLink (m : M) : LinkEmbedding M 2`
* `MobiusMutualChannel.lean:1025` `separatedLink (m : M) (R : Real) : LinkEmbedding M 2`

The only n-generic concrete one is the `Nonempty (LinkEmbedding M n)` instance
at `MobiusEnergy.lean:323`, whose `sep` is (line 335) `if i = j then ambientDist
else 1` — **constant off-diagonal**. That instance therefore satisfies `h3` and
`h4` trivially, so its `b_3` is 0 by the lemma. **The only 4-component
`LinkEmbedding` the corpus can produce is the degenerate one in the b_3 = 0
case** — which is a stronger statement of "not workable today" than "the
families are synthetic", and it is measured rather than asserted.

**Contamination check — run, with its result, because the bare grep MISLEADS.**
The wrong claim reached three artifacts and all three are corrected in the same
push: this bean, issue #7338's body, and PR #7339's body. It reached nothing
else — not `qou-o6ml`, no `.lean`, no witness, no content block.

`git grep -e "gives exactly 0" -e "1.43 MeV"` over tracked
`*.md *.lean *.py *.json *.ts` returns **12 hits and zero of them are this
claim**: `1.43 MeV` has **no hits at all**, and all 12 `gives exactly 0` are
unrelated subjects — the 4_1 order-2 Habiro tail (`qou-9ghx`,
`qbeta_5two_order3_barodd_tail_probe.py:207`), `y_lambda_at` on the ht6 stratum
(`qou-ftuv:2302`), adjacent-pair F (`qou-prjo:407`), the M = 3 Borromean
(`brunnian_triple_exhaustion_probe.py:107`), the Bernoulli tower
(`eunit_g2_derivation_probe.py:232`), Z = 0 or N = 0
(`nfold_ip_coupling_duality_gap_probe.py:386`), and n(3) = 3
(`ursell_chain_mismatch_probe.py:201`).

Recorded this way because the first run of this very check emitted the label
*"no lines above = no hits outside the bean"* over twelve printed lines — the
label was written into the command before the result was known. A grep whose
verdict is baked into its own invocation is not a check.


---

## 2026-09-13 — §9h LANDED: the charge-antisymmetric content is the configuration change TOO

`MobiusMutualChannel.lean` §9h, two theorems, both sorry-free
(`[propext, Classical.choice, Quot.sound]`; `lean -DautoImplicit=false -s 65536`
exit 0, no output):

* `mobius_b3_congr_of_sep_eq` — two instantiations agreeing on the **pair and
  triple** separations have equal `b_3`. `Lquad` is unconstrained: `b_3` is
  `triple - (pair + pair + pair)`, so the four-component assembly never enters.
* `mobius_b3_differs_forces_sep_differ` — contrapositive: **any** difference in
  `b_3` forces the separations to differ.

**The argument is one observation about the signature, not new machinery.**
`mobiusCrossingModel` takes **no charge argument**: its inputs are link
embeddings and the arclength `s`; `CrossingModel` carries `w2`/`w3`/`w4` and
nothing else; `toBindingMap` is built from those three. There is no point in the
chain where a proton differs from a neutron — **two nuclei are two
instantiations of one functional.**

**What it buys the arc.** `qou-9v7t` records that the framework has **no EM term
in any per-bond factor** (`f_pp = z`, `f_nn = z - h`,
`f_pn = z - h(1/2 - δ/4)` — charge-*labelled*, not charge-*coupled*). §9h says
route (2) **does not need one**: whatever charge-antisymmetric number this
channel can supply is a derived geometry, exactly as §9g found for the many-body
number. **One obligation, not two.** That is a narrowing of the arc — the EM
target and the many-body target collapse onto the same missing object — and it
is emphatically **not** a closure.

**NOT CLAIMED** (in the section docstring, not only here): that the mirror
partners' separations **do** differ in this framework, nor by how much. Same open
item as §9g, now reached from the charge side as well. §9h is **not** a
prediction of `b3_asym`; it says where any such prediction would have to come
from.

**Scope — the arity caveat is real.** `CrossingModel` is `Fin 4`-indexed, so
`b_3 i j k` is a triple's cumulant *inside a four-component model*, while the
mirror pair ³H/³He is A = 3. The theorems are stated for two **arbitrary**
instantiations, which is what is proved; reading them as ³H and ³He is an
interpretation that carries a spare fourth component with it.

**Lean caught the first attempt, which is the point of writing it in Lean.**
`BindingMap` is in namespace `QOU.Mass.PairwiseCumulantVanishing`, so the
unqualified `simp only [BindingMap.b3, …]` was an unknown identifier, the `b_3`
never unfolded, and the `rw` chain then reported "did not find an occurrence" —
an error that reads like a wrong lemma and was a wrong *name*. Rewritten to bind
the six `innerPairEnergy_congr_of_sep_eq` instances as `have`s and pass them to
`simp`, which is also robust to rewrite order.
