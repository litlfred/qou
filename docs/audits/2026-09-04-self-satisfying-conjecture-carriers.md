# Ten classes named `BorromeanQuark`, and every one of them is inhabited

*2026-09-04. Bean `qou-7yj0`. Evidence file:
[`2026-09-04-borromean-quark-carriers-trivial.lean`](2026-09-04-borromean-quark-carriers-trivial.lean)
— `lean`-direct **exit 0**, zero `sorryAx`.*

## The claim

The corpus contains **ten separate `class BorromeanQuark` declarations**. No two
have the same fields. Nine of them are file-local, in the **root namespace**, and
each supports at least one theorem whose docstring says the result is
*"conditional on `BorromeanQuark`"* or *"conditional on `conj:borromean-quark`"*.

**All ten are trivially inhabited.** Each was replicated faithfully in a single
Lean file and handed an instance built from nothing but its own field types. Every
one typechecks. So every theorem in the corpus marked *conditional on
`[BorromeanQuark]`* is, as a matter of Lean, **unconditional**: its hypothesis is
discharged with no mathematical input at all.

This is not a claim that those theorems are wrong. Most of them are correct
algebraic derivations. It is a claim about what the word *conditional* is doing:
nothing.

## The ten

`n` is the field count. **Verdict** is the compiler's, not mine.

| # | file:line | fields | inhabited by |
|---|---|---|---|
| T1 | `brings-surface/orbital-fourier-decomposition.lean:180` | `orbitalDim`, `decomposition_law` | `orbitalDim := fun n => (range n).sum modeSpaceDim`, law by `rfl` |
| T2 | `brings-surface/orbital-space-normal-bundle.lean:204` | `orbitalDim`, `so3_decomposition` | same shape |
| T3 | `observations/borromean-quark.lean:87` — **the canonical one** | `bare_mass`, `volume_calibrates_mass`, `is_baryon_realisation`, `is_baryon_realisation_holds` | `bare_mass := fun q => borromean_volume / (1-1/q)²`; `is_baryon_realisation := True` |
| T4 | `mass-theory/reidemeister-mass-invariance.lean:157` | `volume_calibrates_mass` (an `∃ V m, …`) | `⟨1, fun q => 1/(1-1/q)², one_pos, rfl⟩` |
| T5 | `mass-theory/hecke-1d-irrep-closed-form-character.lean:305` | `pairwise_unlinked : ∃ pairLink, ∀ i j, pairLink i j = 0` | `pairLink := fun _ _ => 0` |
| T6 | `lean/QOU/ParticleInteractions/neutron_qvalue_symbolic.lean:39` | 12, incl. `qvalue_ansatz` | `q := 2`, `h := 3/2`, `m_e := 0`, the rest by `rfl` |
| T7 | `lean/QOU/Conjectures/ShellTransitionKnot.lean:70` | `crossingNumber`, `crossingNumber_eq : … = 3` | `crossingNumber := 3` |
| T8 | `predicted-spectra/shell-structure-eigenvalues.lean:156` | `E0`, `shellEnergy`, `energy_law` | `E0 := 1`, `shellEnergy := shellVolume` |
| T9 | `predicted-spectra/hydrogen-shell-writhe.lean:58` | `bareMass`, `bareMass_pos` | `bareMass := fun _ => 1` |
| T10 | `nuclear-interactions/q-beta-spectral-bridge.lean:286` | `Q_beta_A`, `Q_beta_B`, `forms_agree` | both `:= 0` |

T5 and T7 do not depend on **any** axioms at all — not even `propext`.

## The root cause, stated precisely

> **A carrier whose constraining fields relate only its own data fields is a
> definition of a structure, not a statement of a conjecture.**

A group is a carrier whose axioms constrain its own operation, and that is
correct — a group is a *structure*. A conjecture is different in kind: it is a
claim about objects that are **already fixed elsewhere**. If the carrier gets to
choose the objects it constrains, it can always satisfy itself, and inhabiting it
costs nothing.

T10 is the clearest case. `conj:q-beta-spectral-bridge` says that two
*specific, independently defined* presentations of the free-neutron Q-value —
Form A in the NF-counit basis, Form B in the transfer-matrix eigenfunction basis —
give the same number. The carrier encodes this as two **free reals** asserted
equal. Everything that made the conjecture a conjecture, namely that those reals
are *those two forms*, is absent, and `⟨0, 0, rfl⟩` inhabits it.

T3, the canonical carrier, is the closest to right: `volume_calibrates_mass` pins
`bare_mass` to `borromean_volume / (1 − 1/q)²`, and `borromean_volume` is a named
external constant. But `bare_mass` is still a **field**, so the class supplies its
own subject — and the file's own `instance canonical` inhabits it exactly that
way. Its `is_baryon_realisation : Prop` + `is_baryon_realisation_holds :
is_baryon_realisation` pair is separately the self-nominating shape recorded in
[`2026-09-03-prop-field-implication-inversion.md`](2026-09-03-prop-field-implication-inversion.md):
taking the `Prop` to be `True` satisfies it.

## The fix pattern

Make the subject a **parameter**, not a field:

```lean
-- self-satisfying: the class chooses its own bare_mass
class BorromeanQuark where
  bare_mass : ℝ → ℝ
  volume_calibrates_mass : ∀ q > 1, bare_mass q = borromean_volume / (1 - 1/q)^2

-- a real constraint on a GIVEN functional
class BorromeanQuark (bareMass : ℝ → ℝ) : Prop where
  volume_calibrates_mass : ∀ q > 1, bareMass q = borromean_volume / (1 - 1/q)^2
```

The second is refutable — `¬ BorromeanQuark (fun _ => 0)` is provable — and a
downstream `[BorromeanQuark f]` binder then means something. The first is not.

The same move fixes T10: parametrise on the two Q-value definitions rather than
declaring them as fields.

## What this does *not* say

- **Not** that the theorems are false. T6's `neutron_qvalue_symbolic` is a
  correct closed-form derivation by ring algebra from its field equations; it is
  an honest implication. The defect is the framing — it is an algebraic identity
  over unconstrained parameters, not a result gated by a physical conjecture.
- **Not** that structures constraining their own data are wrong in general. That
  is what a structure is for. The defect is confined to carriers that stand in
  for an **open conjecture**.
- **Not** a corpus-wide count. Only these ten were measured.

## Scope of the wider surface — measured, and deliberately not extrapolated

**169 theorems** in `content/**/*.lean` have a docstring saying *"conditional
on"* and carry an instance binder. Their carriers include 18 `CommRing` and other
ordinary Mathlib classes (not conjecture carriers). The conjecture-shaped ones,
by binder count:

    8  BorromeanQuark          3  QouObstructionReductionContext
    6  TrefoilElectronMassConj 3  CarlemanDeterminacyStieltjes
    5  HypMinimizerUnique      3  CrystalGraphRealization
    3  CanonicalMarkovWeightsH3   3  QIntegerMassFormula
    3  CoGroundStateSelection  3  IsOcneanuWeightSystem
    3  MatrixFarkas            3  HasFiniteLPDuality

**Only `BorromeanQuark` has been measured.** The others are named here as the
remainder, not as findings — the check is cheap and mechanical (replicate the
class, attempt an instance from its own field types, run `lean`-direct) and it
should be run per carrier before any of them is described either way.

A blunter shape scan over the whole corpus reports **874 of 1450** carriers with
at least one Prop-ish field whose Prop fields all mention one of the carrier's own
data fields. That number is an **upper bound on nothing useful** — the large
majority are ordinary algebraic structures, where the shape is correct. It is
recorded only so that a future reader does not mistake it for the finding.

## A methodological note worth keeping

The first run of the evidence file reported `T6.triv depends on axioms: [propext,
sorryAx, …]`, which reads exactly like *"this carrier is not trivially
inhabited"*. It was not: `norm_num` had failed on `3/2 < 2` because the scratch
file imported `Mathlib.Data.Real.Basic` without `Mathlib.Tactic`, so the division
extension was absent. Adding the import turned it green.

**A `sorryAx` in `#print axioms` after a tactic failure is evidence about the
tactic environment, not about the proposition.** Read the error, not the axiom
list.

## Applied here: T4, plus two axioms that were always theorems

`mass-theory/reidemeister-mass-invariance.lean` carried T4 and is fully
self-contained (its own docstring says downstream consumers should use the
canonical class), so it is the worked fix.

**T4 parametrised.** `class BorromeanQuark (bareMass : ℝ → ℝ) : Prop` with
`volume_calibrates_mass : ∀ q > 1, bareMass q = borromeanVolume / (1 − 1/q)²`,
pinned to a locally declared named constant rather than an existentially bound
`V`. The carrier is now refutable, and that refutation is proved:
`not_borromeanQuark_const_zero : ¬ BorromeanQuark (fun _ => 0)`. The old form
admitted no refutation, because it quantified over the very functional it
constrained. `calibrated_mass_pos_of_borromeanQuark` keeps its name and its
`_of_` shape and is now genuinely conditional.

**Two axioms in the same file were provable all along.** `applyR3 K := K`, so
`f (applyR3 K) = f K` is `rfl` for *every* `f` — nothing about mass or binding
energy is involved. `axiom bareMass_R3_invariant` and `axiom
bindingEnergy_R3_invariant` are replaced by one theorem,

```lean
theorem invariant_under_R3 {γ : Type*} (f : KnotDiagram → γ) (K : KnotDiagram) :
    f (applyR3 K) = f K := rfl
```

which `#print axioms` reports as depending on **no axioms at all**, plus two
corollaries that depend only on the *data* axioms `bareMass` / `bindingEnergy`
— not on any invariance assumption. File axiom count **8 → 6**.

Verification: `lean`-direct **exit 0** against the real import cone.
`Mathlib.Tactic` had to be added to the imports — `norm_num` cannot normalise
the decimal literal `7.32772` without its `OfScientific` extension, which is the
same missing-import trap that produced the spurious `sorryAx` recorded above.

The remaining six axioms in that file are the genuine R-I/R-II invariance
claims and the two data declarations. It is a `conjecture` block, where an
axiom carrier is the sanctioned form (§3b), so those are **not** defects — only
the two `rfl`-provable ones were.

---

# Round two: the rest of the "conditional on" population

*Added the same day, after the section above named these as unmeasured. Evidence:
[`2026-09-04-conjecture-carriers-round-two.lean`](2026-09-04-conjecture-carriers-round-two.lean)
— `lean`-direct **exit 0**.*

The picture is more interesting than "all vacuous", and the difference is the
useful part: **the corpus already contains the correct pattern.** Five of these
carriers are well-formed. The defect is confined to the ones whose subject is a
*field*.

## Well-formed — the subject is a parameter, or entirely external

| carrier | why it is fine |
|---|---|
| `HypMinimizerUnique : Prop` (`lean/QOU/Archimedean/HyperbolicGeodesic.lean:109`) | one field, quantified entirely over external `IsHypMinimizer` / `upperH`. No data of its own at all — the ideal shape. |
| `CarlemanDeterminacyStieltjes : Prop` (`lean/QOU/MathlibExt/FrechetShohat.lean:232`) | same: `∀ M, … → CarlemanCondition M → StieltjesDeterminate M`, all external. |
| `IsOcneanuWeightSystem (Q z : R) (r : ℕ) (y : YoungDiagram → R) : Prop` | every subject is a **parameter**; the fields constrain them against the external `schurPrincipal`. |
| `CoGroundStateSelection (ctx : CoLpDualBindingContext R) : Prop` | constrains `ctx.Phi_1_k`, and `ctx` is a parameter. |
| `TrefoilElectronMassConj (T) (rho) (m_e_cat) : Prop` | subjects are parameters; the field pins `categoricalMassMeV rho m_e_cat T` to the external `m_e_MeV_codata`. |

`TrefoilElectronMassConj` is worth reading in full, because its own docstring
records that **this exact defect was already found and fixed there**: the trefoil's
strand and crossing counts *"were previously free fields of the conjecture class
beside equations naming their values, which is why they are stated here instead."*
So the fix proposed above is not a novel suggestion — it is the repo's own better
practice, applied to the carriers that have not had it applied yet.

`CrystalGraphRealization (n : ℕ) (q : ℝ)` in
`knots-particles-confinement/confinement-grading-correspondence-conditional.lean:76`
is a middle case: `klr_lift` is a field, but the constraint relates the two
*external* functions `confinementLevel` and `KLRTopDegree` through it, so it is
not free. Not measured either way; left as such.

## Self-satisfying — the subject is a field

All four verified by instance, `lean`-direct exit 0.

| # | carrier | inhabited by |
|---|---|---|
| C1 | `CrystalGraphRealization (R) (q)` — `lean/QOU/BraidKnot/CrystalGraphRealization.lean:45`, **and** an identical copy at `mass-theory/crystal-r-matrix-sub-lemma.lean:60` | `raising := fun _ _ => none`. The field's docstring calls it *"the conjecture itself … plays the role of `sorry`"*; it does not. |
| C2 | `CrystalGraphRealization : Prop` — `mass-theory/transfer-matrix-level-independence.lean:120` | `highest_weight : ∃ raise : ℕ → ℤ, ∀ i, raise i = 0` → `fun _ => 0`. **Depends on no axioms at all**; the field is a theorem of arithmetic. |
| C3 | `CanonicalMarkovWeightsH3` — `lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean:1075`, identical copy at `mass-endomorphism/qbeta-per-block-chi-closed-forms.lean:399` | `y3 := 1`, `y21 = y111 := 0`. |
| C4 | `QIntegerMassFormula : Prop` — `mass-theory/wigner-coefficient-derivation.lean:70` | `∃ r ≥ 0, ∃ value, value = r * m_e` — `value` is existentially bound and constrained only by the equation defining it, so the field reduces to `True`. |

## The opposite defect: one carrier that is UNINHABITABLE

`QIntegerMassFormula` at `mass-theory/q-integer-mass-formula.lean:150` cannot be
instantiated, so **every `[QIntegerMassFormula]`-conditional theorem in that file
is vacuously true**. Proved: `C5.not_inhabited : ¬ Nonempty QIntegerMassFormula`.

The reason is quantifier scope, not physics. `fits_AME` reads

```lean
∀ (q m_e : ℝ) (Z N : ℕ) (B_AME : ℝ),
  ∃ δ : ℝ, |δ| ≤ tolerance ∧ B_AME = (1 + δ) * binding_energy_bw q m_e Z N …
```

with `B_AME` ranging over **every real**, while `{(1+δ)·X : |δ| ≤ tolerance}` is a
bounded interval around the single fixed `X`. Take `B_AME = 0`: since
`tolerance ≤ 1/100 < 1`, `1 + δ > 0`, so `X = 0`. Take `B_AME = 1`: it now demands
`1 = 0`. The argument holds for **any** `binding_energy_bw`.

The sibling copy at `lean/QOU/Interactions/QIntegerMassFormula.lean:178` is the
*same class with the same field name* and carries `[IsAMEValue Z N B_AME]`.

**🛑 I first wrote here that this makes the fix "a one-binder change, and the
correct form is already in the tree". That is wrong, and I retract it — see the
next section.**

## Name collisions

These are distinct classes sharing a name, in the root namespace or in namespaces
that do not disambiguate them at a reading glance — the `markovZ` overload defect
recorded in `AGENTS.md`, one level up:

    BorromeanQuark              10 declarations, no two with the same fields
    CrystalGraphRealization      4 (two identical, one Prop-only vacuous, one parametrised)
    QIntegerMassFormula          3 (one vacuous, one uninhabitable, one correct)
    CanonicalMarkovWeightsH3     2 (identical)

`QIntegerMassFormula` is the sharpest: three classes, one name, and the three are
**vacuous**, **uninhabitable**, and **correct** respectively. A reader who meets
"conditional on `[QIntegerMassFormula]`" cannot tell which they have without
resolving the declaration.

---

# 🛑 Retraction, and the prior work I should have found first

*Added within the hour, after reading `lean/QOU/Interactions/QIntegerMassFormula.lean`
in full rather than at the class declaration.*

## What I got wrong

I recommended porting the `[IsAMEValue Z N B_AME]` binder into
`mass-theory/q-integer-mass-formula.lean`, calling it "a one-binder fix" and the
gated version "the correct form already in the tree". **Do not do that.** The
gated version is laundered, and a prior agent measured and documented exactly
that on 2026-08-24 — in the file itself, on bean `qou-hjf4`, and as **Finding B**
of [`2026-08-24-faithful-instance-family.md`](2026-08-24-faithful-instance-family.md),
which even carries the same two-file side-by-side comparison I made.

The laundering is one level up, in the hypothesis class. `IsAMEValue` is
documented as recording *"the two physical invariants every real entry
satisfies"* — but it has a **third** field:

```lean
  /-- Trivialized bound hypothesis to close sorry -/
  fits_bound : ∀ (q m_e : ℝ), ∃ δ : ℝ, |δ| ≤ (1:ℝ)/100 ∧
    B_AME = (1 + δ) * binding_energy_bw q m_e Z N 0 0
```

which asserts the 1 % agreement outright. With it present, that file's
`fits_AME_conditional` reduces to `∀ …, [claim] → [claim]`, and `canonical`
discharges `fits_AME` by projecting it (`f_magic := fun _ => 0` is load-bearing:
it makes the two expressions definitionally equal).

So porting the binder would import a laundered hypothesis into a file that is at
least *honestly* uninhabited. That trades a vacuous-because-unsatisfiable
statement for a `claim → claim` one with a model available — **worse on the axis
this audit is about, not better.** The prior note says so in as many words:
*"deleting `fits_bound` here would move this file toward a statement that is
worse, not better … which of the two versions is the paper's claim is the
author's call."*

**Recommendation, replacing the retracted one:** do not touch either file. This
is the author's call, already framed on `qou-hjf4`, and it needs the paper's
claim decided before any Lean moves.

## How I missed it

The corpus-grep checklist has six paths and I ran none of them for
`QIntegerMassFormula` before recommending. Path 1 (`docs/audits/`) and path 6
(`.beans/`) each hold the answer on their own. This is the checklist's exact
failure mode, in a session whose own subject is claims that look established and
are not.

## What survives, and what is genuinely new here

The **measurement** stands and is not affected: `¬ Nonempty QIntegerMassFormula`
is a machine-checked proof of what the earlier note asserted in prose ("states
`fits_AME` over an **arbitrary real** `B_AME`, which is false as written"). A
proof is stronger than the assertion, and it is checkable by re-running the
evidence file.

The **carrier finding is not a duplicate of `qou-hjf4`**, and the difference is
mechanical rather than a matter of framing. That census
([`scripts/trivially-inhabiting-instance-census.py`](../../scripts/trivially-inhabiting-instance-census.py))
keys on `INSTANCE_HEAD` — an unguarded global `instance` filling a data field
with constant content. This audit is about the **class**, with no instance
required anywhere.

Measured: of the ten `class BorromeanQuark` declarations, exactly **one** has an
instance in the tree (`observations/borromean-quark.lean:120`). The other nine
have none, so an instance-keyed census is structurally blind to all nine — there
is nothing for it to match. The two detectors are complementary, and neither
subsumes the other.

---

# Prior work this sits next to — and the one place we disagree

*Added after merge, on a corpus-grep of `docs/audits/` and `.beans/` for each
carrier — the step whose omission produced the retraction above.*

The nearest prior work is
[`2026-08-23-free-prop-field-census.md`](2026-08-23-free-prop-field-census.md)
(PR #5562, beans `qou-lo1t` / `qou-tsnp`). It **already names
`BorromeanQuark`** — specifically that its `instance canonical` is declared
twice, in a chapter sibling and in the library, "the shadow-pair shape again".
Read it before this file.

## The questions are different, and the difference is mechanical

That census asks: *which carriers have a **free `Prop` field**?* — the
self-nominating `X : Prop` + `h_X : X` shape. This audit asks: *which carriers
**satisfy themselves**?*

Neither contains the other:

- `q-beta-spectral-bridge`'s carrier has **no `Prop`-typed field at all**
  (`Q_beta_A : ℝ`, `Q_beta_B : ℝ`, `forms_agree : Q_beta_A = Q_beta_B`), so the
  free-`Prop` census cannot see it. It is nonetheless inhabited by `⟨0, 0, rfl⟩`.
- Conversely a free `Prop` field can sit in a carrier whose *other* fields
  constrain something external, which the census flags and this audit would not.

Nor is either a duplicate of `qou-hjf4`'s
[`trivially-inhabiting-instance-census.py`](../../scripts/trivially-inhabiting-instance-census.py),
which keys on `INSTANCE_HEAD` — an unguarded global `instance` with constant
data content. Measured above: nine of the ten `BorromeanQuark` classes have no
instance anywhere, so that census has nothing to match on.

## Where this contradicts the census, and why it is worth saying

The census crosses its 122 free-`Prop` carriers against inhabitation and finds
**89 with no inhabitant at all**, then reads that as reassuring:

> The 89 are the §3b-tax **honest open state** — nothing inhabits them, so a
> downstream `[C] → P` can never be *applied*. Weak, but inert.

**For a self-satisfying carrier that reading does not hold.** "Nothing inhabits
it" is not evidence of an open state when inhabiting it costs one line that any
reader could write in seconds — it is evidence that nobody bothered. The
`[C] → P` theorem is not gated by an open problem; it is gated by a fact nobody
has typed. Every instance in the two evidence files here was written in one
line, and `T5`/`T7`/`C2` need no axioms at all.

So the census's "weak but inert" verdict is right for a carrier that is merely
*unproved*, and wrong for one that is *unprovable-to-fail*. Separating those two
is what the parametrise-don't-field fix is for, and the census's own count
cannot make the split, because inhabitation-in-the-tree is the wrong probe:
the question is whether an instance is **available**, not whether one is
**present**.

## A methodological warning from that same census, which applies here

> a `lean` run killed by a 2-minute command timeout leaves a log with zero
> errors in it, which reads as success

Both evidence files here were run to completion in the background with the exit
status captured *after* the process exited (`v_qcod exit=0`, `v_reid exit=0`,
and the two `#print axioms` batches), not read out of a truncated log. Worth
stating, because a clean-looking log is exactly what a killed run produces.

## C1 was a re-discovery — credit where it belongs, and what survives it

Reading `qou-4els` (completed 2026-08-24) rather than only seeing it in a grep
hit list: its table names the C1 vacuity in the same words I re-derived a week
and a half later.

| decl | what discharged the conjecture |
|---|---|
| `CrystalGraphRealization.canonical` | `CrystalNode := PUnit`, `raising _ _ := none` → `crystal_realises` is `none = none` |

That is exactly `C1.triv`. **The mechanism was known; I re-measured it without
citing it, in the round-two commit and PR comment.** This is the second
re-discovery in one session, and the first (`[IsAMEValue]`) was the more costly
one, so the pattern rather than either instance is the thing to record: seeing a
bean in a grep hit list is not reading it.

**What `qou-4els` fixed, verified still in place on `main`:** all six of its
`canonical`s are `def`, not `instance` — `CrystalGraphRealization`,
`KazhdanLusztigClassicalLimit`, `SymmetricCrystalPairProduction`,
`RootOfUnityMTCTruncation`, `CemeteryGroupEmergence`, `GSOrderMatch`. That is
real: `[CrystalGraphRealization R q]` in a theorem no longer resolves silently.

**What it does not fix, and this is the surviving finding.** Demoting the
instance removes the *automatic* resolution; it does not make the carrier
constrain anything. The class is still satisfied by

```lean
instance : CrystalGraphRealization ℤ 0 :=
  ⟨PUnit, PUnit, id, fun _ _ => none, fun _ _ => none, fun _ _ => rfl⟩
```

— one line, and `C1.triv` in the round-two evidence file is that line. So the
conditional theorems downstream are gated by **nobody having typed it**, not by
mathematics. That is the *available*-versus-*present* distinction drawn against
the free-`Prop` census above, applied now to a fix that was already made:
demotion moves a carrier from "inhabited" to "inhabitable", which is a smaller
step than it reads as.

`qou-09mr` reaches the same structural point from a different file, and adds a
detector caveat worth carrying: `checkNoVacuousInstanceData` requires a
degenerate *value* (`0`, `True`, `PUnit.unit`), so **definitional laundering** —
data that is a real non-degenerate function still chosen to make the claim
reflexive — is invisible to it, as are fields written inside a tactic
`exact { … }` rather than a `where`. Filed upstream as `folio-assistant-ilbh`.

**C2, C3 and C4 are not in `qou-4els`'s six** and are not covered by
`qou-tsnp`'s twelve (a third shape again: `holds : Prop`). Those three stand as
first measurements.

---

# 🛑 MAJOR CORRECTION — the headline over-claims, and the corpus had the right rule five days earlier

*Same day. The prior work is [`2026-08-30-the-remainder-is-vacuous-not-open.md`](2026-08-30-the-remainder-is-vacuous-not-open.md)
(bean `qou-z9ws`), its evidence file
[`2026-08-30-context-classes-are-inhabited-by-zero.lean`](2026-08-30-context-classes-are-inhabited-by-zero.lean),
and the tool [`scripts/lean-context-class-inhabitation-probe.py`](../../scripts/lean-context-class-inhabitation-probe.py).*

## What that audit already established

My thesis, stated more sharply and on a larger measured population — **52 of 79**
context classes inhabited by `Unit` and zero:

> A class inhabited that cheaply constrains nothing. A `[C]` binder on it assumes
> nothing, and the downstream `[C]`-conditional declaration is therefore not
> conditional on anything. **Constructing a witness for such a class is not
> progress — it is the defect.**

It also ships a probe. Mine was hand-built. **This audit is not the first
statement of its own thesis**, and both round-one and round-two were written
without citing it.

## And it corrects me on two points — both of which I accept

**1. Inhabitation does not decide it. The discriminator is what the downstream
declaration *does* with the field.**

> - **derives something from it** → §3b-cond working (`BorromeanQuark`);
> - **projects it verbatim** → §3b-cond item 5, and if the class is *also*
>   inhabited by zero, the declaration is conditional on nothing.

**2. "Inhabited ⇒ vacuous" holds only for an *unparameterised* class.** For
`C x`, a downstream `theorem foo [C x] : P x` quantifies over `x`; exhibiting
`C x₀` for one `x₀` shows the hypothesis is **satisfiable**, not that it assumes
nothing. My `C1.triv` inhabits `CrystalGraphRealization ℤ 0` — a *parameterised*
class — so it shows satisfiability, not vacuity.

## Re-classified under that discriminator — checked against the actual bodies

| | downstream body | verdict |
|---|---|---|
| **T1** `orbital_fourier_decomposition` | `rw [inst.decomposition_law, orbital_dim_eq_square]` | **DERIVES — not a defect** |
| **T2** `orbital_space_normal_bundle_conditional` | `rw [inst.so3_decomposition, QOU.orbital_space_dim]` | **DERIVES — not a defect** |
| **T6** `neutron_qvalue_symbolic` | closed form by ring algebra from the field equations | **DERIVES — not a defect** |
| **T8** `shell_eigenvalues_conditional` | `rw [energy_law ×3, chebyshev_recurrence]; ring` | **DERIVES — not a defect** |
| **T3** `baryon_mass_from_volume` | `:= inst.volume_calibrates_mass q hq` | **PROJECTS — defect stands** |
| **T10** `q_beta_spectral_conditional` | `:= inst.forms_agree` | **PROJECTS — defect stands** |
| **T4** reidemeister mirror | existential over its own `V` *and* `m` | **defect — fixed in #6657** |
| T5, T7, T9 | no `[inst]`-binding theorem found by the search | **not claimed either way** |
| **C1** | class is *parameterised* | shows **satisfiability**, not vacuity |

The Aug-30 audit names T1 explicitly as *the worked counter-example* — "that is
§3b-cond working exactly as intended". My table listed it as a defect.

**So the headline "all ten are trivially inhabited, therefore every
`[BorromeanQuark]`-conditional theorem is unconditional" is wrong.** The
inhabitation measurements are correct; the inference from them is not. The sharp
cases are **T3 and T10** — both pure projections — plus **T4**, which was a
defect of a kind the derives/projects rule does not even reach (its field
existentially bound *both* the volume and the mass functional, so even a
derivation would be a derivation from nothing).

## And round two was prior work in full

- **C1** — `qou-4els`, credited above.
- **C2, C4** — `docs/audits/2026-08-24-undecided-carrier-witnesses.lean` carries
  `w_crystalGraphRealization := ⟨⟨fun _ => 0, fun _ => rfl⟩⟩` and
  `w_qIntegerMassFormula`, **the identical witnesses**, from a probe
  (`scripts/vacuous-prop-carrier-probe.py`).
- **C3** — stood down: `CanonicalMarkovWeightsH3` was worked on **2026-09-03**
  with owner approval ("2y", `qou-6u92`), `canonicalInstance` promoted and
  `explicitInstance` demoted as a deliberate pair, the inhabitant **wired to the
  Markov-derived n=3 weights** (`qou-c35w`, landed via #6506), and guarded by
  `delta_tau_M_canonical_resolves_to_canonical`, which is `rfl`-provable *only
  because* resolution picks those weights. Parametrising it would break that
  guard by construction. My row "`y3 := 1`, rest `0`" is true of what the class
  *permits* and materially misleading about what the corpus *does*.

So **none of round two's four was a first measurement**, against my explicit
claim that three of them were.

## What survives

- **#6644 entirely** — the q-codifferential axiom work is a different subject.
- **The two `rfl` axioms** in `reidemeister-mass-invariance.lean`
  (`applyR3 K := K`), and the **T4 parametrisation** — both mine, both uncontested.
- **`¬ Nonempty QIntegerMassFormula`** — a machine-checked proof. The Aug-24 note
  asserted "false as written" in prose; the prior probe's uninhabitable seventh is
  `SeparateLambdaScale_Antipattern` (`is_antipattern : False`), a different
  declaration.
- **The name-collision counts** — 10 `BorromeanQuark`, 4 `CrystalGraphRealization`,
  3 `QIntegerMassFormula`, 2 `CanonicalMarkovWeightsH3`. No prior count found.

## The pattern, which is the durable part

Four re-discoveries in one session — `[IsAMEValue]`, C1, C2/C4, and this whole
thesis — each found *after* writing the claim rather than before. Three of the
four were in files a grep had already put in front of me. **A corpus this
heavily audited should be assumed to hold the finding already; the default
posture for a "new" vacuity result is to look for whose it is first.**

---

# Three independent routes to one discriminator (added at check-in)

While this correction was being written, a sibling session landed
[`b5a10c6a28`](https://github.com/litlfred/qou/commit/b5a10c6a28) on `main`
— *"a fourth carrier-vacuity shape — an unconsumed `holds : Prop` field"* — and
reached the same self-correction from a third direction:

> **A Prop-TYPED FIELD IS NOT VACUOUS ON ITS OWN, and my first rule
> over-reported 101 carriers by assuming it was.** Declaring an abstract
> predicate and then CONSUMING it in a sibling is the correct §3b-cond pattern.

Its worked counter-example is `QOU.Torsion.BraneBoundaryContext`, whose five
`Prop` fields are all consumed by `boundary_active` and
`impl_brane_boundary_structure` — so that carrier states a real implication and
the detector must stay silent on it. Its criterion is **UNCONSUMED**: a
`Prop`-typed field whose name appears in no other field's type in the same
carrier. `101 → 42` on that narrowing.

So three audits, three probes, three different shapes measured — and one rule
underneath:

| audit | shape measured | discriminator |
|---|---|---|
| `qou-z9ws` (2026-08-30) | context class inhabited by `Unit`/zero | downstream **derives** vs **projects** |
| `b5a10c6a28` (2026-09-04) | a bare `Prop`-typed field | the field is **consumed** by a sibling field |
| this one | the class satisfies itself | (adopted: the two above) |

**The convergence is the result, not any one count.** Each route began by
flagging on *shape* and each had to narrow to *use* — over-reporting first, in
the same direction, by roughly the same factor. A carrier's syntax does not
decide whether it asserts anything; what the rest of the file does with the
field does. Anyone building the next detector in this family should start from
the narrowed rule rather than re-deriving it, and should expect the first
version to over-report.

Note also that `b5a10c6a28`'s 42 and `qou-tsnp`'s 12 are **different
denominators** — corpus-wide unconsumed `Prop`-typed fields versus the
`holds : Prop` conjecture-sibling carriers specifically — and should not be
compared as though one supersedes the other.
