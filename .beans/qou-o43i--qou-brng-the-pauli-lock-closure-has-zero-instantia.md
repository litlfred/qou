---
# qou-o43i
title: 'qou-brng: the Pauli-lock closure has ZERO instantiation sites — its equal-scalars hypothesis is not a corpus claim a D9 witness could settle'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T20:22:33Z
updated_at: 2026-09-06T03:57:26Z
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
