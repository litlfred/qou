import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.Algebra.BigOperators.Finsupp.Basic

/-!
# The Grothendieck group of a quantum universe and its Chern character

Carrier for `def:grothendieck-group-of-a-qou` and `def:chern-character`, and the
Lean half of the factorisation recorded in
`docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §2.1:

    K₀(𝐂)  ──ch──▶  HH₀(𝐂)  ──ev──▶  R,        dim_q = ev ∘ ch.

Axiom 4 of a quantum universe (`QuantumUniverse.centralIdem_*`) makes the
Frobenius–Hopf object a finite orthogonal sum of blocks, so the split
Grothendieck group is the free abelian group on the block set and the degree-zero
Hochschild homology of the (semisimple) category is the free `R`-module on the
central idempotents. In that presentation:

* `K0 U = U.blocks →₀ ℤ`, with `blockClass U b = [b]`;
* `HH0 U = U.blocks → R`, the coordinates along the central idempotents;
* `chernCharacter U : K0 U → HH0 U` sends `Σ n_b [b]` to `Σ n_b [p_b]`
  (Beliakova–Guliyev–Habiro–Lauda §3.5.1: `[x] ↦ [1_x]`);
* `evDimQ U : HH0 U → R` evaluates a class against the quantum dimensions,
  `φ ↦ Σ_b φ(b) · dim_q(b)`;
* `dimQK0 U : K0 U → R` is the quantum dimension extended additively.

**Theorem** `dimQK0_eq_evDimQ_chernCharacter`: `dim_q = ev ∘ ch` on `K₀`. This is
the precise sense in which the quantum dimension of an object is one evaluation
of its character, and it is the item "K₀ → HH₀ → k factorisation" of bean
`qou-mjt3`. The identification of `HH₀` of the category with `R^{blocks}` is the
semisimplicity of axiom 4, used as the presentation; nothing here is an axiom
beyond the structure `QuantumUniverse`.

Base ring generic `{R} [CommRing R]` (§7c). No `sorry`.

-- Ref: [bghl-2017] https://doi.org/10.4171/QT/92
-/

namespace QOU.GrothendieckChern

open QOU

noncomputable section

variable {R : Type*} [CommRing R]

/-- **The split Grothendieck group** of a quantum universe: the free abelian group on
its Wedderburn blocks. -/
abbrev K0 (U : QuantumUniverse R) : Type _ := U.blocks →₀ ℤ

/-- The class `[b]` of a block. -/
def blockClass (U : QuantumUniverse R) (b : U.blocks) : K0 U :=
  Finsupp.single b 1

/-- **Degree-zero Hochschild homology** of the semisimple category, presented on the
central idempotents: coordinates `U.blocks → R`. -/
abbrev HH0 (U : QuantumUniverse R) : Type _ := U.blocks → R

/-- **The Chern character** `K₀ → HH₀`: `Σ n_b [b] ↦ Σ n_b [p_b]`. -/
def chernCharacter (U : QuantumUniverse R) (x : K0 U) : HH0 U :=
  fun b => (x b : R)

/-- Evaluation of a degree-zero class against the quantum dimensions. -/
def evDimQ (U : QuantumUniverse R) (φ : HH0 U) : R :=
  haveI := U.blocksFintype
  ∑ b, φ b * U.dimQ b

/-- The quantum dimension extended additively to `K₀`. -/
def dimQK0 (U : QuantumUniverse R) (x : K0 U) : R :=
  x.sum (fun b n => n • U.dimQ b)

/-- The rank: the augmentation `K₀ → ℤ`, `Σ n_b [b] ↦ Σ n_b`. -/
def rank (U : QuantumUniverse R) (x : K0 U) : ℤ :=
  x.sum (fun _ n => n)

theorem chernCharacter_add (U : QuantumUniverse R) (x y : K0 U) :
    chernCharacter U (x + y) = chernCharacter U x + chernCharacter U y := by
  funext b; simp [chernCharacter]

theorem chernCharacter_blockClass (U : QuantumUniverse R) [DecidableEq U.blocks] (b b' : U.blocks) :
    chernCharacter U (blockClass U b) b' = if b = b' then 1 else 0 := by
  simp [chernCharacter, blockClass, Finsupp.single_apply]

theorem dimQK0_add (U : QuantumUniverse R) (x y : K0 U) :
    dimQK0 U (x + y) = dimQK0 U x + dimQK0 U y := by
  unfold dimQK0
  rw [Finsupp.sum_add_index']
  · intro b; simp
  · intro b m n; rw [add_smul]

theorem dimQK0_blockClass (U : QuantumUniverse R) (b : U.blocks) :
    dimQK0 U (blockClass U b) = U.dimQ b := by
  unfold dimQK0 blockClass
  rw [Finsupp.sum_single_index]
  · simp
  · simp

theorem rank_blockClass (U : QuantumUniverse R) (b : U.blocks) :
    rank U (blockClass U b) = 1 := by
  unfold rank blockClass
  rw [Finsupp.sum_single_index]
  rfl

/-- **`dim_q` factors through the Chern character (sorry-free):** `dim_q = ev ∘ ch`
on `K₀`. -/
theorem dimQK0_eq_evDimQ_chernCharacter (U : QuantumUniverse R) (x : K0 U) :
    dimQK0 U x = evDimQ U (chernCharacter U x) := by
  letI := U.blocksFintype
  unfold dimQK0 evDimQ chernCharacter
  rw [Finsupp.sum_fintype _ _ (fun b => by simp)]
  simp only [zsmul_eq_mul]

end

end QOU.GrothendieckChern
