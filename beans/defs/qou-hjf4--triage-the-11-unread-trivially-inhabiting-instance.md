---
# qou-hjf4
title: Triage the 11 unread trivially-inhabiting-instance candidates
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:36:01Z
updated_at: 2026-10-10T07:01:39Z
parent: qou-6qbv
---

From `scripts/trivially-inhabiting-instance-census.py` (PR #5621, audit
`docs/audits/2026-08-24-vacuity-detector-gap-five-files.md`).

The shape: an **unguarded** global `instance` filling a **data** field with
constant content, where the class it inhabits is consumed as a `[C …]`
hypothesis somewhere. That combination silently satisfies every such binder —
the `triv_hecke` / `triv_wedderburn` shape demoted in PR #5581.

`3112 .lean → 37 constant data field → 23 unguarded → 14 actionable.`

**Three hand-read, three confirmed harmful:**

- `mass-theory/phi-q-tower-jsj-bridge.lean:114` `TowerSummandRealization` —
  **FIXED** in `4204be07ed2` (demoted to `def`; the file also had never
  compiled, 6 errors → 0).
- `lean/QOU/MassEndomorphism/MassEndomorphismTrivial.lean:28` `MassEndomorphism`
  — global zero instance over an **arbitrary** `β`. Its docstring claims it
  "shows the conditional theorems are discharged non-vacuously", which is true
  of the *inhabitation* but not of the *global instance*: as an instance it also
  preempts resolution everywhere. Same disposition as `triv_hecke` — `def`.
- `lean/QOU/Interactions/QIntegerMassFormula.lean:185` `QIntegerMassFormula` —
  `f_magic := fun _ => 0` discharging the `[QIntegerMassFormula]` of
  `fits_AME_conditional`, making a §3b-cond conditional theorem unconditional at
  a degenerate magic-number correction.

**The 11 unread — candidates, NOT findings.** Each needs the same hand-read the
three above got; do not bulk-demote.

    he4-channel-active-set.lean:129            HasHe4ChannelActiveSet     c=12
    BraidKnot/Helium3Witness.lean:100          R5FullWitness              c=10
    Interactions/WedderburnMassFormula.lean:125 HasHoefsmitData           c=10
    Encounter/MostowRigidity.lean:200          MostowRigidity             c=4
    mass-endomorphism/topological-mass-conjecture.lean:180
                                               TopologicalDecompositionMass c=4
    AppendixSurreals/ClassicalLimitStpart.lean:75  ClassicalLimitStpart    c=2
    Molecular/ShellClosureNfTermCount.lean:399 ShellClosureNFTermCount    c=2
    mass-theory/jet-tower-uniform-delta-max.lean:82  JetTowerUniformDeltaMax c=2
    molecular-construction/shell-closure-nf-term-count.lean:381
                                               ShellClosureNFTermCount    c=2
    Infra/Polylogarithm.lean:107               TheoremA                   c=1
    mass-theory/lifted-crossing-locality.lean:67  LiftedCrossingLocality  c=1

**Read the instance body before deciding.** The discriminator recorded on
`qou-lo1t`: `he4_strong_duality_value` has exactly this shape yet is `legit`,
because its field reads `strong_duality := by norm_num` over concrete rationals
— a checked certificate, not a constant. Inhabitation alone never decides it.
Note `he4-channel-active-set` is in the list above and may be the same story.

Two of the eleven are the **same class in two files**
(`ShellClosureNFTermCount`), so a single verdict likely covers both.



---

## Cross-reference added 2026-08-24

`QOU/Interactions/QIntegerMassFormula.lean:185` — third of the three
"confirmed harmful" above — has a **second** defect this bean does not name, now
filed as `qou-tpt6`: `fits_AME` is not discharged by the instance at all, it is
forwarded to `IsAMEValue.fits_bound`, a field whose own docstring reads
"Trivialized bound hypothesis to close sorry". `IsAMEValue` has **zero instances
corpus-wide**, so `fits_AME_conditional` is unsatisfiable-as-stated rather than
vacuously true. Fix them together — the `f_magic := fun _ => 0` verdict this
bean owns and the laundering `qou-tpt6` owns are the same edit.


---

## One candidate removed 2026-08-24 — 11 -> 10, bean stays open

`QIntegerMassFormula.canonical`'s `f_magic := fun _ => 0` is gone: the whole
module `QOU/Interactions/QIntegerMassFormula.lean` was deleted as unneeded
(bean `qou-tpt6`). It had no consumers in the compiled tree and duplicated the
fully-qualified name of an honest sibling under `content/…/mass-theory/` that
states the conjecture directly and supplies no instance.

So this candidate is not *triaged*, it is **withdrawn** — there is no longer a
declaration to judge. The remaining ten still need reading.
## 2026-08-24 — triaged, and the count was wrong: 17 actionable, not 14

PR #5686. Findings recorded, no `content/` Lean changed.

### The pattern the 11 turned out to share

13 files carry the same boilerplate on a global `instance`: *"**Faithful
instance.** Carries the explicit research-grade conjecture as a sorry."*
Measured with the census's own comment-stripper: **34 occurrences of `sorry`,
0 of them a `sorry` term.** All prose. The conjectures are discharged by
collapsing the model (`PUnit` / `0` / `none` in the data fields), and the
instances are unconditional, so downstream `#print axioms` shows no `sorryAx`.

- **`CrystalGraphRealization`** — 39 consumers, the largest in the corpus.
  `NormalForm := PUnit`, `CrystalNode := PUnit`, both crystal operators
  `none`. Same carrier shape as `triv_hecke`.
- **`QIntegerMassFormula`** — 13 consumers, split across two declarations.
  `IsAMEValue`'s third field is the conjecture and says so in its own
  docstring ("Trivialized bound hypothesis to close sorry");
  `f_magic := fun _ => 0` is load-bearing for the type match. Verified by
  `#synth` / `rfl` / `#print axioms`, not by reading.
- **`MassEndomorphism`** — NOT new. `VolumeBridge.lean` already records it
  correctly and calls the demotion "tracked separately". It has not landed.

### Two benign, and the discriminator they establish

`HasHe4ChannelActiveSet` (zeros are the inactive channels' real LP values,
pinned by four `by norm_num` fields) and `hasHoefsmitData_vacuum` (indexed AT
the vacuum). **A constant is content-free only when the carrier is generic AND
nothing constrains it** — not merely when a field holds a constant.

### Three defects in my own detector

1. **It hid its worst cases.** Every `[…]` binder counted as a guard, so
   `instance canonical {R} [CommRing R] {β} : MassEndomorphism R β` read as
   "guarded by CommRing" and vanished, while the milder `trivial_int_zero`
   stayed visible only because concrete `ℤ` needs no such binder.
   23 unguarded / 14 actionable → **30 / 17**.
2. **ASCII `->` contains `>`**, a `PROP_MARKERS` entry, so a plain data field
   read as a proof obligation. Fails in the safe direction — which is why it
   would never have surfaced on its own. 4 such declarations under `content/`.
3. **The self-test deleted itself on success.** Its positive case was
   `skeletonRealisation`, which #5621 correctly demoted, so the test failed
   *because the corpus was repaired*. Now pinned against an inline fixture.

### Next

Measure the blast radius of demoting `CrystalGraphRealization.canonical`
(39 consumers) before touching it — same discipline #5581/#5621 used for their
one-file demotions. The 11 lower-consumer rows are cheaper and could go first.


## A 12th candidate, from a different detector — and the census gate cannot see it (2026-09-14)

`mass-endomorphism/conj-qbeta-c-k-closed-forms.lean:82`
`noncomputable instance defaultQBetaCKClosedForms : QBetaCKClosedForms`.

Same class of defect as the three confirmed above and the same disposition as
`ClassicalLimitStpart` (which is already in this bean's unread list): a
**parameterless global instance** that instance search resolves for the
`[inst : QBetaCKClosedForms]` of `qbeta_c_k_closed_forms_derived` (line 131),
making a 3b-cond "conditional" theorem unconditional.

**What makes it worse than a bookkeeping slip:** the instance's field values are
FITTED, and the file says so in terms — *"whose instance values are FIT, not
proved"*, residuals *"c_4 0.9%, c_5 2.4%, c_6 14%; c_7 signed-error +114%"*. So
the theorem is unconditional **on a fit**. AGENTS.md "Axiomatization is NOT a
Proof" rule 2 names exactly this.

The file also contradicts itself about it: the **class** docstring names the
instance (*"The instance `defaultQBetaCKClosedForms` axiomatises these"*), while
the **theorem** docstring 49 lines later says the openness *"is carried by that
class having no instance"*.

**Scope, measured, so this is not oversold:** `QBetaCKClosedForms` and
`qbeta_c_k_closed_forms_derived` are referenced by **no other file**. Nothing
downstream is currently laundered; what is wrong is the file's self-description
and the `instance`-vs-`def` declaration. Fix = the `ClassicalLimitStpart` one.

**Why the census missed it — a candidate detector-blindness row, deliberately
NOT written into the taxonomy here.** `trivially-inhabiting-instance-census.py`
gates on a **constant** data field. This instance's fields are
`fun q => -2 * (hoefsmitB q)^4` and siblings — *functions of `q`*, not
constants — so the gate structurally cannot see it, even though a fitted
closed form is no more derived than a constant is. The discriminator that would
catch both is "the field's content is not derived from anything in the class",
which is not mechanically checkable; a cheaper proxy is "parameterless global
instance + the class is consumed as a `[C]` binder", dropping the constancy
requirement entirely.

(Not added to `docs/audits/2026-08-15-detector-blindness-taxonomy.md`: PR #7342
is concurrently adding a row there and the row-count line is already contended —
see the coordination comment on that PR.)

Found by the `proof-no-self-assuming-projection` arm while adjudicating bean
`qou-vh1o`; ledgered `genuine` with disposition
`demote-instance-to-def-and-fix-docstring`.


## `defaultQBetaCKClosedForms` DEMOTED and VERIFIED — 2026-09-14 (PR #7364)

`noncomputable instance` -> `noncomputable def`, plus three docstring
corrections. `lean -DautoImplicit=false -s 65536` exit 0, zero diagnostics;
`#print axioms` on both theorems shows the three standard Mathlib axioms and
**no `sorryAx`**.

**The decisive check was two-sided, and that is the reusable part.** A one-sided
"instance search now fails" run cannot distinguish a working demotion from a
broken probe. Three cells:

| probe | declaration | `#synth QBetaCKClosedForms` |
|---|---|---|
| edited file | `def` | **fails to synthesize** |
| scratch copy, `instance` restored | `instance` | succeeds |
| **actual `HEAD`, pre-edit** | `instance` | succeeds |

The third row is what matters: this bean's premise is now **confirmed
empirically on the real pre-edit file** rather than inferred from reading. The
positive control's `sed` was guarded (exactly one line rewritten, asserted both
ways) — an unguarded `sed` that matches nothing is a known false green.

**A trap worth recording for the next demotion in this bean's list.** The
"nothing but the agent checks library Lean" exemption is scoped to
`content/<paper>/lean/QOU/**`. This file sits in a **chapter** directory beside
`.ts`/`.md` siblings, so it carries a `.qa.json`, and the edit made
`source_hashes.lean` stale (`866e46508f42` -> `bcd1a46140fd`). Refreshed via
`qa-sweep` in the same commit. Several of the 11 unread candidates in this bean
are in chapter directories too — check for a sidecar before assuming the
library exemption applies.

**Containment re-measured independently by the verifier**: no `.lean` outside
this file mentions `QBetaCKClosedForms`, `defaultQBetaCKClosedForms` or
`qbeta_c_k_closed_forms`; no importer; the content block's `lean.ref` points at
the CLASS, so the demotion cannot break it.

Remaining in this bean: the 11 unread trivially-inhabiting-instance candidates
(unchanged) and the detector-blindness note added 2026-09-14 (the census gates
on a CONSTANT data field, so a field that is a fitted FUNCTION of `q` is
structurally invisible to it).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carriers M2 and M10 of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## Round 57 Progress (PR litlfred/qou#8286)
- Status updated to `in-progress` (`litlfred/qou#8286`, C1 `6c7a20f3289e7e0671ce65ef402e1a06fd77c443`, C2 `dce9c51d4a6cd8f2253c078180b4b77a6f7c1ed0`).
