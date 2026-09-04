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
*same class with the same field name* and carries `[IsAMEValue Z N B_AME]`, which
is exactly the restriction the other one is missing. So the fix is a one-binder
change, and the correct form is already in the tree.

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
