import QOU.Machinery.HeckeTowerBasicConstruction
import QOU.Machinery.MarkovInductiveCyclicity
import QOU.Machinery.MarkovCosetLift
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

/-!
# Discharging the cyclicity bricks against the Ocneanu tower

`QOU.Machinery.MarkovInductive.cyclic_two_g` proves the two-generator Ocneanu
cyclicity step from **seven** hypotheses about an abstract `(memB, E, tr)`.
Seven assumed hypotheses is a weak result: the more a conditional theorem
assumes, the less its conclusion says, and nothing in that file forces the
hypotheses to describe a Hecke tower rather than an arbitrary triple that
happens to satisfy them.

This file supplies the tower and **derives four of the seven** from the W2
interface (`QOU.Machinery.HeckeTower.HeckeConditionalExpectation`, bean
`qou-2017`), leaving `hIH` — the induction hypothesis, which is what an
induction is *for* — and `hgwg`, the Markov reduction of a two-generator word.

The instantiation is the obvious one:

| brick | tower |
|---|---|
| `A` | `Hn1`, the level-`n+1` algebra |
| `memB x` | `∃ y, x = ι y` — the image of `Hn` under the tower inclusion |
| `E` | `ι ∘ ε` — conditional expectation, viewed back inside `Hn1` |
| `tr` | `trn ∘ ε` — a level-`n` trace pulled up through `ε` |
| `memBlow` | `memB` (see the note below) |

## What is actually derived, and what is not

`hCE` is the one with content. Everything else is bookkeeping about the image
of an algebra map; `hCE` says the trace cannot distinguish `a * x` from
`a * E x` for `a` in the subalgebra, which is the property that makes `ε` a
*conditional expectation* rather than an arbitrary retraction. It follows from
`bimodule` and `retract` together, and `towerTrace_mul_eq_of_memB` is the proof.

Note that it is derived **only because `tr` was defined as `trn ∘ ε`**. For a
trace not of that form `hCE` is a genuine assumption, and this file would not
apply — which is the honest content of the reduction: it converts "assume the
trace is compatible with `ε`" into "define the trace through `ε`".

## Scope — what this does NOT close

`HeckeConditionalExpectation` **has no instance**, and this file does not build
one. It is a §3b dependent conjecture carrier, so every result here is
conditional on it in exactly the way its own file says. **Conditional-proved is
not premise-established.** What changed is the size of the conditional: four
hypotheses that were free parameters are now consequences of one named,
content-bearing class.

`memBlow` is instantiated as `memB`, not as a genuinely lower level. That is
sound — `cyclic_two_g` uses `memBlow` only through `hElow`/`hlowB`/`hCE`, and
all three hold — but it means this file does not exercise the two-level
structure the abstract statement allows. A tower with `H_{n-1} ⊊ H_n` would
need a second `ε`; nothing here depends on the difference.
-/

namespace QOU.Machinery.MarkovTowerBridge

open QOU.Machinery.HeckeTower QOU.Machinery.HeckeBraidedCategory

variable {R : Type*} [Field R] {q : R}
variable {Hn Hn1 : Type*} [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
variable {σn : ℕ → Hn} {σn1 : ℕ → Hn1}
variable {rankHi : ℕ} [HeckeBraidedPresentationOfRank q rankHi Hn1 σn1]

/-- `memB ι x` — "`x` lies in the level-`n` subalgebra", i.e. in the image of
the tower inclusion. This is the concrete reading of `MarkovInductive`'s
abstract `memB`. -/
def memB (ι : Hn →ₐ[R] Hn1) (x : Hn1) : Prop := ∃ y : Hn, x = ι y

/-- `towerE ι ε` — the conditional expectation viewed as an endomorphism of
`Hn1`, which is the shape `MarkovInductive.cyclic_two_g` expects of `E`. -/
def towerE (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn) (x : Hn1) : Hn1 := ι (ε x)

/-- `towerTrace trn ε` — a level-`n` trace pulled up through the conditional
expectation. Defining the level-`(n+1)` trace this way is what makes `hCE`
derivable rather than assumed; see the module docstring. -/
def towerTrace (trn : Hn → R) (ε : Hn1 →ₗ[R] Hn) (x : Hn1) : R := trn (ε x)

section

variable (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn)

/-- The subalgebra is closed under multiplication — `hmul`. -/
theorem memB_mul : ∀ x y : Hn1, memB ι x → memB ι y → memB ι (x * y) := by
  rintro _ _ ⟨a, rfl⟩ ⟨b, rfl⟩
  exact ⟨a * b, (map_mul ι a b).symm⟩

/-- The subalgebra contains `1`. -/
theorem memB_one : memB ι (1 : Hn1) := ⟨1, (map_one ι).symm⟩

/-- `E` lands in the subalgebra — `hElow` (and, with `memBlow := memB`,
`hlowB` is `id`). -/
theorem memB_towerE (x : Hn1) : memB ι (towerE ι ε x) := ⟨ε x, rfl⟩

/-- **The bimodule law at `z = 1`**: `ε (ι y * x) = y * ε x`.

This is `bimodule` with the right factor trivialised, and it is the step that
carries the weight in `towerTrace_mul_eq_of_memB` below.

The conditional-expectation instance is bound by NAME rather than left to
instance search: `q`, `σn` and `σn1` appear nowhere else in this statement, so
they are pinned only by unification against `inst`. -/
theorem epsilon_inclusion_mul
    (inst : HeckeConditionalExpectation R q rankHi Hn Hn1 σn1 ι ε)
    (y : Hn) (x : Hn1) : ε (ι y * x) = y * ε x := by
  have h := inst.bimodule y 1 x
  rwa [map_one, mul_one, mul_one] at h

/-- **`hCE`, derived.** For `a` in the level-`n` subalgebra the trace cannot
tell `a * x` from `a * E x`.

Both sides evaluate to `trn (y * ε x)` where `a = ι y`: the left by the
bimodule law, the right because `ι y * ι (ε x) = ι (y * ε x)` and `ε` retracts
`ι`. This is the only one of the four discharged bricks with mathematical
content — the other three are facts about the image of an algebra map. -/
theorem towerTrace_mul_eq_of_memB
    (inst : HeckeConditionalExpectation R q rankHi Hn Hn1 σn1 ι ε)
    (trn : Hn → R) :
    ∀ a x : Hn1, memB ι a → memB ι x →
      towerTrace trn ε (a * x) = towerTrace trn ε (a * towerE ι ε x) := by
  rintro _ x ⟨y, rfl⟩ -
  have hL : ε (ι y * x) = y * ε x := epsilon_inclusion_mul ι ε inst y x
  have hR : ε (ι y * towerE ι ε x) = y * ε x := by
    rw [towerE, ← map_mul ι, inst.retract (y * ε x)]
  simp only [towerTrace, hL, hR]

/-- **The reduction.** Ocneanu two-generator cyclicity on the tower, from the
induction hypothesis and the Markov reduction ALONE — the other five arguments
of `MarkovInductive.cyclic_two_g` are discharged above.

Still conditional on `HeckeConditionalExpectation`, which has no instance. -/
theorem cyclic_two_g_of_tower
    (inst : HeckeConditionalExpectation R q rankHi Hn Hn1 σn1 ι ε)
    (trn : Hn → R) (g : Hn1) (z hbar : R)
    (hIH : ∀ x y : Hn1, memB ι x → memB ι y →
      towerTrace trn ε (x * y) = towerTrace trn ε (y * x))
    (hgwg : ∀ x w y : Hn1, memB ι x → memB ι w → memB ι y →
      towerTrace trn ε (x * g * w * g * y)
        = towerTrace trn ε (x * towerE ι ε w * y)
          + z * hbar * towerTrace trn ε (x * w * y))
    (u v p r : Hn1) (hu : memB ι u) (hv : memB ι v)
    (hp : memB ι p) (hr : memB ι r) :
    towerTrace trn ε ((u * g * v) * (p * g * r))
      = towerTrace trn ε ((p * g * r) * (u * g * v)) :=
  MarkovInductive.cyclic_two_g (memB ι) (memB ι) (towerTrace trn ε) g z hbar
    (towerE ι ε) hIH (memB_mul ι)
    (fun w _ => memB_towerE ι ε w) (fun _ h => h) hgwg
    (fun a x ha hx => towerTrace_mul_eq_of_memB ι ε inst trn a x ha hx)
    u v p r hu hv hp hr

/-! ## Arbitrary `w`, via the spanning decomposition

`cyclic_two_g`'s `hgwg` is stated for a `w` the caller has ALREADY put into
coset-sum form. That is the weaker half of the assumption: it silently requires
the caller to know a decomposition exists. `HeckeCosetSpanning` supplies exactly
that, so the reduction below runs on an ARBITRARY `w : Hn`.

What it yields is the `hgwg` equation with the expectation `Ew` **exhibited**,
built from the decomposition, rather than assumed equal to `ι (ε w)`. Closing
that last gap — `Ew = ι (ε w)` — needs the Markov property of the conditional
expectation, `ε (b · σₙ · c) = z • (b·c)`, which is NOT a field of
`HeckeConditionalExpectation` (it has exactly `retract` and `bimodule`). So this
section does not close it, and says so rather than adding a field and calling
the assumption discharged. -/

section Spanning

open QOU.Machinery.MarkovInductive

variable {Hlow : Type*} [Ring Hlow] [Algebra R Hlow] {σlow : ℕ → Hlow}
variable {rank : ℕ} [HeckeBraidedPresentationOfRank q rank Hn σn]

/-- **The `hgwg` reduction for an arbitrary `w`.** Given the spanning
decomposition and the two grounding shape lemmas — one for the lower-coset
summand, one for the middle — the two-generator Markov reduction holds for
EVERY `w : Hn`.

The conclusion **pins the witness to the decomposition**: it asserts both that
`w` splits and that the reduction holds with the expectation built from *that*
split. A bare `∃ Ew, …` would have been weaker in a way that matters here — a
degenerate trace (`tr = 0`, the case `markov_axioms_vacuous_of_weight_zero`
already records upstream) satisfies `∃ Ew` for any `Ew` at all, so the
existential alone would carry no information about the coset structure. Tying
the two conjuncts together is what stops the statement being satisfiable by a
lucky witness.

The grounding hypotheses are the genuine mathematical input; the decomposition
is what lets them cover every `w` rather than only pre-decomposed ones. -/
theorem gwg_trace_of_spanning
    (ιlow : Hlow →ₐ[R] Hn) (n : ℕ)
    (inst : HeckeCosetSpanning R q rank Hlow Hn σn ιlow n)
    (tr : Hn → R) (g : Hn) (z hbar : R)
    (htr_add : ∀ p r : Hn, tr (p + r) = tr p + tr r) (htr_zero : tr 0 = 0)
    (x y : Hn)
    (hlow : ∀ a : Hlow, tr (x * (g * ιlow a * g) * y)
              = tr (x * ιlow a * y) + z * hbar * tr (x * ιlow a * y))
    (hmid : ∀ b c : Hlow,
      tr (x * (g * (ιlow b * σn n * ιlow c) * g) * y)
        = tr (x * (z • (ιlow b * ιlow c)) * y)
          + z * hbar * tr (x * (ιlow b * σn n * ιlow c) * y))
    (w : Hn) :
    ∃ (a : Hlow) (s : Finset ℕ) (b c : ℕ → Hlow),
      w = ιlow a + ∑ i ∈ s, ιlow (b i) * σn n * ιlow (c i) ∧
      tr (x * g * w * g * y)
        = tr (x * (ιlow a + ∑ i ∈ s, z • (ιlow (b i) * ιlow (c i))) * y)
          + z * hbar * tr (x * w * y) := by
  obtain ⟨a, s, b, c, hw⟩ := inst.spanning w
  refine ⟨a, s, b, c, hw, ?_⟩
  subst hw
  exact gwg_trace_cosetSum tr g (σn n) z hbar s (ιlow a)
    (fun i => ιlow (b i)) (fun i => ιlow (c i)) x y htr_add htr_zero
    (hlow a) (fun i _ => hmid (b i) (c i))

/-- **`ε` computed on an arbitrary element.** Spanning gives the decomposition;
the Markov property evaluates `ε` on each piece. Together they determine
`ι (ε w)` outright:

  `ιlow (εlow w) = ιlow a + Σᵢ z • (ιlow (b i) · ιlow (c i))`

which is precisely the expectation `gwg_trace_of_spanning` exhibits. This is the
composition the two classes exist to enable — neither alone says what `ε` does
to a general element. -/
theorem towerE_eq_of_spanning
    (ιlow : Hlow →ₐ[R] Hn) (εlow : Hn →ₗ[R] Hlow) (n : ℕ) (z : R)
    (instCE : HeckeConditionalExpectation R q rank Hlow Hn σn ιlow εlow)
    (instMk : @HeckeMarkovExpectation R _ q rank Hlow Hn _ _ _ _ σn _
      ιlow εlow instCE n z)
    (a : Hlow) (s : Finset ℕ) (b c : ℕ → Hlow) :
    ιlow (εlow (ιlow a + ∑ i ∈ s, ιlow (b i) * σn n * ιlow (c i)))
      = ιlow a + ∑ i ∈ s, z • (ιlow (b i) * ιlow (c i)) := by
  classical
  rw [map_add, map_sum]
  rw [instCE.retract a]
  simp only [instMk.markov]
  rw [map_add, map_sum]
  simp only [map_smul, map_mul]

/-- **`hgwg` in the shape `cyclic_two_g` wants, for an arbitrary `w`.**
`gwg_trace_of_spanning` exhibits the expectation as a decomposition sum;
`towerE_eq_of_spanning` identifies that sum with `ι (ε w)`. Composing them gives
the reduction stated against `towerE` itself, with no residual `∃`.

Conditional on BOTH `HeckeCosetSpanning` and `HeckeMarkovExpectation`, neither
of which has an instance. -/
theorem gwg_trace_towerE_of_spanning
    (ιlow : Hlow →ₐ[R] Hn) (εlow : Hn →ₗ[R] Hlow) (n : ℕ) (z hbar : R)
    (instCE : HeckeConditionalExpectation R q rank Hlow Hn σn ιlow εlow)
    (instMk : @HeckeMarkovExpectation R _ q rank Hlow Hn _ _ _ _ σn _
      ιlow εlow instCE n z)
    (instSp : HeckeCosetSpanning R q rank Hlow Hn σn ιlow n)
    (tr : Hn → R) (g : Hn)
    (htr_add : ∀ p r : Hn, tr (p + r) = tr p + tr r) (htr_zero : tr 0 = 0)
    (x y : Hn)
    (hlow : ∀ a : Hlow, tr (x * (g * ιlow a * g) * y)
              = tr (x * ιlow a * y) + z * hbar * tr (x * ιlow a * y))
    (hmid : ∀ b c : Hlow,
      tr (x * (g * (ιlow b * σn n * ιlow c) * g) * y)
        = tr (x * (z • (ιlow b * ιlow c)) * y)
          + z * hbar * tr (x * (ιlow b * σn n * ιlow c) * y))
    (w : Hn) :
    tr (x * g * w * g * y)
      = tr (x * towerE ιlow εlow w * y) + z * hbar * tr (x * w * y) := by
  obtain ⟨a, s, b, c, hw, heq⟩ :=
    gwg_trace_of_spanning ιlow n instSp tr g z hbar htr_add htr_zero x y
      hlow hmid w
  rw [heq, towerE, hw,
      towerE_eq_of_spanning ιlow εlow n z instCE instMk a s b c]

end Spanning

end

/-! ## The conditional-expectation instance is load-bearing

A "reduction" that quietly assumed its conclusion would compile exactly as
happily as this one, so the claim is checked rather than asserted. `simp` fails
to close `hCE` with the instance removed, which is weak evidence; the section
below is the decisive form — with a linear `ε` that is NOT a conditional
expectation, the `hCE` identity is **false**, not merely unproved.

Keep this section. It is what stops a later reader "simplifying" the theorem by
dropping an instance that looks decorative in the statement. -/

section Necessity

/-- `ε` = "scale by 2" on `ℚ`: `ℚ`-linear, but neither a retraction of the
identity inclusion nor an `(Hn, Hn)`-bimodule map, so every field of
`HeckeConditionalExpectation` fails. -/
noncomputable def scaleTwo : ℚ →ₗ[ℚ] ℚ := (2 : ℚ) • LinearMap.id

/-- **The `hCE` identity FAILS for a retraction that is not a conditional
expectation.** With `Hn = Hn1 = R = ℚ`, `ι = id` and `ε` = scaling by 2, the
left side is `2ax` and the right is `4ax`; at `a = x = 1` that reads `2 = 4`.

So `towerTrace_mul_eq_of_memB` genuinely consumes its instance. -/
theorem hCE_fails_without_conditional_expectation :
    ¬ (∀ a x : ℚ, memB (AlgHom.id ℚ ℚ) a → memB (AlgHom.id ℚ ℚ) x →
        towerTrace id scaleTwo (a * x)
          = towerTrace id scaleTwo (a * towerE (AlgHom.id ℚ ℚ) scaleTwo x)) := by
  intro h
  have hx := h 1 1 ⟨1, by simp⟩ ⟨1, by simp⟩
  simp only [towerTrace, towerE, scaleTwo, AlgHom.coe_id, id_eq,
    LinearMap.smul_apply, LinearMap.id_coe, smul_eq_mul] at hx
  norm_num at hx

/-- **The spanning shape does NOT force a proper tower.** With `ιlow` the
identity, every `w` splits trivially — take `a := w` and an empty sum.

So `HeckeCosetSpanning` is consistent (it has a degenerate model, which is what
makes results conditional on it non-vacuous), and it is also *weaker than a
proper inclusion*: an instance of it carries no information that `Hlow` is a
strict subalgebra. Anything needing properness must say so separately.

Stated over a bare `Ring` because the Hecke presentation binders carry no force
here — the observation is about the shape of the decomposition, not about
Hecke. -/
theorem spanning_shape_holds_for_identity_inclusion
    {A : Type*} [Ring A] [Algebra R A] (f w : A) :
    ∃ (a : A) (s : Finset ℕ) (b c : ℕ → A),
      w = (AlgHom.id R A) a
        + ∑ i ∈ s, (AlgHom.id R A) (b i) * f * (AlgHom.id R A) (c i) :=
  ⟨w, ∅, fun _ => 0, fun _ => 0, by simp⟩

end Necessity

end QOU.Machinery.MarkovTowerBridge
