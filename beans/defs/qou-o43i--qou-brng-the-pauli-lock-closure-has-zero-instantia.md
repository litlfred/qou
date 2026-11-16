---
# qou-o43i
title: 'qou-brng: the Pauli-lock closure has ZERO instantiation sites — its equal-scalars hypothesis is not a corpus claim a D9 witness could settle'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T20:22:33Z
updated_at: 2026-10-04T15:13:38Z
parent: qou-10v9
---

Follows `qou-brng`'s 2026-09-04 entry, which named `separable_interface_degenerate`'s
equal-scalars hypothesis as *"where the residue actually is"* and set the next step as
*"a witness for D9 would make the equal-scalars question decidable for the first time."*

**Both halves need correcting, and the correction is measured rather than argued.**

## 1. The theorem has ZERO instantiation sites — measured, and now guarded

`scripts/separable-interface-instantiation-audit.py` (new; `--selftest` 5/5, `--strict`
gates) strips Lean comments — nested block comments included — and only then searches.
Over every tracked file: **1 declaration, 0 applications, 28 prose citations in 13 files**
(16 `.md`, 8 `.py` docstrings, 2 JSON, 2 Lean *docstrings*).

That matters because `fSpin : Sp → R` and `fIso : Is → R` are **arbitrary functions on
arbitrary types**. `hplus`/`hminus` are the antecedent of a statement quantified over
every possible pair of scalar assignments — not a claim about anything in this corpus.
They become a corpus claim only when the theorem is *instantiated* at the corpus's own
constructions, and nothing does that.

The `μ₊ = (z + q⁻¹)/(q + q⁻¹)`, `μ₋ = (q − z)/(q + q⁻¹)` identification lives in the
theorem's **docstring**, never in its statement. The `y₂`/`y₁₁` link is a different
section of the same file (`weight_eq_proj_scalar`, `WeightsDetermineZ`, lines 355–394),
about different variables. `qou-brng` cites `InterfaceScalar.lean:365–384` for the
identification and that citation is to a docstring-adjacent theorem, not to the one that
closes the channel — the same name-vs-content class as `markovZ`/`markovZc`.

## 2. A D9 witness cannot settle it, because D9's carrier was rebuilt around a different claim

`class IsospinFromCanonicalBowtie` was repaired on 2026-09-04 (#6671) from the
content-free `holds : Prop` to a refutable class with three fields: `0 < q`, `q ≠ 1`, and
one real equation `ratio = (1−q⁻¹)²(q−q⁻¹)(q+q⁻¹)(1+(1−q⁻¹)³)/3`. Its own header states
that the categorical half — the crystal functional and the isospin swap — is **NOT
encoded**.

So an instance of D9 supplies a real-number identity. The equal-scalars question is about
projector scalars of a swap construction. **The two objects do not touch**: a D9 witness
in the carrier's current shape decides nothing here. That is worth knowing before someone
spends a tranche building one, which is what the bean's "Next" line invites.

Note `qou-brng`'s "D9 has no witness" is still literally true — no instance exists — but
its *reasoning* was superseded the same day by the carrier's own header, which records
that a witness under the old shape would have been trivial and proved nothing.

## 3. Formalised: the closure is carried entirely by its hypotheses

Two new sorry-free library files, `lean`-direct exit 0, standard three axioms
(`degeneracy_is_commutativity` has none), split per §7c into generic and archimedean:

* `QOU/QBeta/SeparableInterfaceHypothesesHaveContent.lean` (generic —
  `CommRing`/`CommMonoid`/`Field`, no `ℝ`)
  - `separability_hypotheses_have_content` — drop `hplus`/`hminus` and the conclusion is
    **false**: `5 ≠ 6` on a two-element index type. So the closure is not a tautology.
  - `degeneracy_is_commutativity` — with the hypotheses in force the residual mathematics
    is `mul_comm`. The theorem's proof *is* `rw [hplus, hminus, mul_comm …]`. Everything
    it asserts about physics is asserted by its antecedent.
  - `asymmetry_attainable_with_distinct_scalars` — if the two SU(2)s carry different
    pairs, the channel ratio is **any** field element. Not a weakened bound; none at all.
    Scope (b) on {separable interface, distinct scalar pairs}, invariant: a field has no
    nontrivial multiplicative constraint between two free elements.
* `QOU/QBeta/SeparableInterfaceHypothesesHaveContentReal.lean` (archimedean)
  - `distinct_positive_scalars_reach_any_ratio` — the escape survives positivity, so it is
    not an artefact of admitting negative or zero weights.
  - `measured_asymmetry_attainable` — the measured **33.7055** is one of the values
    reached. What the hypothesis excludes is not a correction; it is the whole effect.

## What this does NOT say

Not a refutation of `separable_interface_degenerate`, which is correct and sorry-free.
Not a claim that the two SU(2)s carry different scalars — that stays exactly as
unestablished as its converse; this is a statement about what the Lean asserts. Nothing
about the linking-matrix result (`lk` IS `I₃`, both channels at `I₃ = 0`, achievable
asymmetry exactly 1), which is untouched and rests on its own argument. Nothing about the
sibling's pair-layer obstruction, which remains a second independent reason the fifth
closure is weak.

## Detector observation, deliberately NOT swept

`scripts/check-sidecars.sh` counts the literal `(R :=` as evidence a file declares a
generic result (`GEN` regex, line 139). AGENTS.md §7c prescribes exactly that spelling for
the archimedean sibling — *"consumes the generic result via a `(R := ℝ)` instantiation"* —
so a correctly-split file gets reported as "§7c MIXED generic + archimedean". A
specialisation is the opposite of generic evidence.

**Left alone on purpose.** My first-pass measurement of the blast radius was noisy (the
grep matched Mathlib and used `\s` under BRE), and AGENTS.md's own rule is not to launch a
sweep off a shaky number. The file here uses `@f ℝ _` instead, and says so in its
docstring rather than sidestepping silently. A proper measurement of how many library
files this misclassifies is a follow-up, not this tranche.

## Verification

`lean -DautoImplicit=false -s 65536` exit 0 on both files; `#print axioms` on all six
declarations shows only `propext`/`Classical.choice`/`Quot.sound`, and none on
`degeneracy_is_commutativity`. `scripts/check-sidecars.sh` clean on both (`generic OK` /
`ℝ justified`), authors-note Lean-coverage refreshed (738/749 provable sorry-free, 98.5%).
`precision-gates.sh --changed` is RED — **pre-existing on main, not this tranche**: zero
`computations/` files are touched here, and the witnesses the gate regenerated were
reverted per its own instruction.


---
## 2026-09-06 — my own "Next" was wrong twice: the step is not executable, and the route it opens is already closed

Corrects this bean's own next line ("instantiate `separable_interface_degenerate` at the
corpus's real `fSpin`/`fIso`"). Same failure class I corrected in `qou-brng` four hours
earlier, now in my own bean.

**1. `fIso` is available; `fSpin` does not exist.** Read from the carriers' own field
lists, not their names:

* `fIso` — `μ₊ = (z+q⁻¹)/(q+q⁻¹)`, `μ₋ = (q−z)/(q+q⁻¹)` (`mu_sum_eq_one`,
  `mu_singlet_lt_mu_triplet`). At the proton pin under convention D these are
  `0.75270211325196540159377935162` and `0.24729788674803459840622064838` — to all 30
  digits the corpus's own `y₍₂₎`, `y₍₁,₁₎` at `n = 2` (`y-lambda-at-q0.witness.json`),
  exactly as `weight_eq_proj_scalar` requires. An independent check that the
  identification is the corpus's and not mine.
* `fSpin` — **nothing**. `BringFiberAction` (D10) builds `A5Irrep → IcosahedralRotation`
  plus an injectivity field; `SpinFromSo3Fiber` constrains `levelCoeff : ℕ → R`, the
  `h^(2n)` Wedderburn coefficients of the three-strand Borromean trace (`levelCoeff 1 = 0`,
  `levelCoeff 2 = −3/4`). Neither is a two-element scalar on the spin channel, and no
  other `.lean` in the tree carries one.

So the equal-scalars identification is **un-instantiable at present** — stronger than
un-instantiated. `hplus`/`hminus` equate a corpus object to one the corpus has not built.
That is a better handover than "go do it".

**2. The route it seems to open is CLOSED, by a stronger argument, since 2026-08-16.**
Dropping the missing spin factor and reading the asymmetry off the isospin scalars alone
gives `B(T=0)/B(T=1) = 4.9181` at the proton pin against a measured `33.7055`. The
shortfall is beside the point: the whole class is excluded without naming a candidate.
The *total* `B(T=1)+B(T=0) = −α·log(μ₊μ₋)` is invariant under every T-odd rescaling
`(μ₊,μ₋) ↦ (μ₊t, μ₋/t)`, and `μ₊+μ₋ = 1` floors it at `α·log 4 = 5.8030` against nature's
`2.1510` — route 7 of
`docs/audits/2026-08-16-two-nucleon-sector-final-state-eight-closures.md`, Lean,
scope-(b). The `4.9181` is recorded so the next reader does not re-derive it as news.

**Caught by the corpus-grep, before it reached a PR body.** My working thesis entering
this — "the isospin scalars separate the channels, so the degeneracy is manufactured by a
spin factor that does not exist" — is *true as stated* and *useless as a route*, because
the magnitude question it opens was settled a month ago by an argument that does not care
about the ratio. Path 1 (`docs/audits/`) is what found it.

**NOT claimed:** nothing about the linking-matrix result (`lk` IS `I₃`, achievable
asymmetry exactly 1) — that is a different object class and is untouched; the "exactly 1"
figure is about linking data and must not be read as covering the projector scalars, which
give 4.9181. Nothing refuted: `separable_interface_degenerate`, `mu_singlet_lt_mu_triplet`
and `singlet_binds_more` are all correct and sorry-free.

**Revised next.** Not this. The two-nucleon channel asymmetry has eight recorded closures;
adding a ninth candidate to that list is not the shape of progress. Anyone picking this up
should read `2026-08-16-two-nucleon-sector-final-state-eight-closures.md` first — routes 7
and 8 close classes rather than candidates, which is why they are the ones that bite.


---
## 2026-09-06, same hour — CORRECTING the entry above: "un-instantiable" is too strong, and the μ± = y_λ identity was already recorded

The beans path of the corpus-grep (path 6) returned **after** I had committed
`a1b3ba9a4b`. I ran it in the background and did not wait. Three fixes, one of them to
the load-bearing sentence.

**1. "Un-instantiable" is wrong. Someone instantiated it, by assuming it.** Bean
`qou-5d6k` (2026-08-25) evaluates the Pauli-locked interface at 50 dps using `μ±` for
**both** SU(2)s:

    μ(³S₁) = μ₊^spin · μ₋^iso = 0.18614164195799085217
    μ(¹S₀) = μ₋^spin · μ₊^iso = 0.18614164195799085217

That is `separable_interface_degenerate`'s conclusion, measured, to the last digit — and
I should have found it before writing that the identification could not be instantiated.

The Lean-level claim survives and is unchanged: **no corpus *construction* supplies
`fSpin`** (D10's `BringFiberAction` builds `A5Irrep → IcosahedralRotation`;
`SpinFromSo3Fiber` constrains `levelCoeff : ℕ → R`). What changes is the conclusion drawn
from it. The correct statement is not *"it cannot be instantiated"* but **"the only
instantiation that exists posits `μ±` on the spin side, which assumes `hplus`/`hminus`
rather than checking them."**

The two readings send a reader to different places, which is why the sloppy one matters:
"cannot be instantiated" invites building a spin scalar; "has only ever been instantiated
by assuming the answer" says the missing object is a *derivation* of the spin projector
weights on the D10 side — a statement about `BringFiberAction`, not about this theorem.

**2. The μ± = y_λ identity is a re-measurement, not a discovery.** Bean `qou-kj4v`
recorded it on 2026-08-09 at **50 dps** (agreement to `3.3e-52`); my run reproduces it at
30 digits. Worth having from two directions, but I presented it without the citation and
that reads as novelty.

**3. A second and sharper reason the isospin-scalar route is closed, which I missed.**
Bean `qou-4g4a` (in-progress, sibling branch `claude/anchor-followups-2026-08-08`,
sorry-free Lean in `GramSignature.lean` §BandSeparation) proves the admissible interface
band `[z−h, z] = [0.40362773835082593616, 0.61268803714646525160]` lies **strictly
between** the two isospin weights: `μ₋` 63.22 % below the floor, `μ₊` 22.85 % above the
ceiling, 7.56 % margin on the tighter `q` condition. Not a knife-edge, not fixable by a
better `q`. So using an isospin projector *as* the interface is **unavailable**, not
merely unmotivated — the two mechanisms compute on disjoint sets. Convention-dependence
stated rather than buried: the lower separation is a **D** phenomenon; under C,
`μ₋ = 0.303675` sits inside the band.

**The process lesson, which is the reusable part.** I backgrounded the corpus-grep and
committed a corpus-status claim while one of its six paths was still running. Paths 1–3
and 5 had returned and looked clean; path 6 held the correction. **Do not commit a
corpus-status claim while any checklist path is outstanding** — the whole point of the
six paths is that the one you skip is the one that bites, and backgrounding a path is a
way of skipping it that feels like diligence.

Unchanged: the `4.9181` is still not recorded anywhere (checked), and route 7 still
closes the class. Nothing refuted.


---
## 2026-09-06 — the deferred `(R :=` measurement, done; detector fixed; my own workaround removed

The entry above left this as *"a real measurement is a follow-up"* after a noisy
first pass. Done properly now.

**Measured** over the **3666** non-`.lake` `.lean` under `content/`, classifying each
twice with the script's exact §7c logic and diffing verdicts: **19** files have `hasGen`
set solely by `(R :=`; **15 change verdict, every one `MIXED(action)` → `R-JUSTIFIED`**;
and **0 of the 31 occurrences sit on a declaration line**.

**Two reasons the token never belonged in `GEN`.** `(R := ℝ)` is a *use* site, and it is
the spelling §7c PRESCRIBES for the archimedean sibling — so a correctly-split file was
told to split. And `R` is a parameter *name*: 9 of the 31 bind it to a **radius**
(`IdealTetEqChimney`, `BorelCaratheodory`, `C1ConnectionPoles`), to `ℂ`
(`RootsOfUnityProduct`), or to a **word** (UGB `HeckeCompletion`).

**Scope stated honestly:** `check-sidecars` scans only *changed* files, so these were
never 15 live flags — 15 files primed to mis-fire the moment anyone edits one. Which is
how it was found: by editing one.

**Fixed**, with the safety argument matching the three prior classes (`qou-mr3q`,
`qou-akb4`, `qou-aemx`): a genuine violation requires a *declaration*, declarations
require a *binder*, and all four binder forms stay in `GEN`. Zero false clears.

**And my own workaround is gone.** `…HaveContentReal.lean` had used `@f ℝ _` explicitly
to dodge this detector. It is back to the prescribed `(R := ℝ)`, and `check-sidecars` now
reports the pair `no ℝ, generic OK` / `ℝ justified`. Both files `lean`-direct exit 0.

Audit + reproduction script: `docs/audits/2026-09-06-check-sidecars-r-assign-false-positive.md`.

**Still NOT fixed, deliberately:** the content-block arm prints the qa-sweep suggestion
for every changed block with no staleness test. It produces no wrong *verdict*, only an
always-printed suggestion, and changing it needs its own measurement of what "stale"
should mean for a sidecar. Recorded so it is not mistaken for an oversight.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (Round 57)
- Round 57 (`litlfred/qou#8213`, commit `2301811899d7f5b7e6235c29e2d41d3e068ef89b`): Added `reciprocal_rescale_preserves_product`, `unit_sum_product_deficit_eq_sq_diff`, and `channel_product_diff_factor` in `SeparableInterfaceHypothesesHaveContent.lean` plus 80-dps mpmath witness.
