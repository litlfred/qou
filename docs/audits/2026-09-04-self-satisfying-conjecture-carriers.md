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
