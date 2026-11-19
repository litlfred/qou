import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.Algebra.BigOperators.Finsupp.Basic

/-!
# The Grothendieck group of a semisimple block decomposition and its Chern character

Carrier for `def:grothendieck-group-of-a-qou` and `def:chern-character`, and the
Lean half of the factorisation recorded in
`docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §2.1:

    K₀(𝐂)  ──ch──▶  HH₀(𝐂)  ──ev──▶  R,        dim_q = ev ∘ ch.

When a quantum universe `U : QuantumUniverse R` (or a finite-strand Hecke
quotient slice in Chapter 5) carries finite Wedderburn block decomposition data
`W : SemisimpleBlockData U`, the split Grothendieck group is presented as the
free abelian group on `W.blocks` and the degree-zero Hochschild homology on that
semisimple slice is the free `R`-module on the central idempotents. In that
presentation:

* `K0 W = W.blocks →₀ ℤ`, with `blockClass W b = [b]`;
* `HH0 W = W.blocks → R`, the coordinates along the central idempotents;
* `chernCharacter W : K0 W → HH0 W` sends `Σ n_b [b]` to `Σ n_b [p_b]`
  (Beliakova–Guliyev–Habiro–Lauda §3.5.1: `[x] ↦ [1_x]`);
* `evDimQ W : HH0 W → R` evaluates a class against the quantum dimensions,
  `φ ↦ Σ_b φ(b) · dim_q(b)`;
* `dimQK0 W : K0 W → R` is the quantum dimension extended additively.

**Theorem** `dimQK0_eq_evDimQ_chernCharacter`: `dim_q = ev ∘ ch` on `K₀`. This is
the precise sense in which the quantum dimension of an object is one evaluation
of its character, and it is the item "K₀ → HH₀ → k factorisation" of bean
`qou-mjt3`. Per the 2026-11-19 architectural ruling (`qou-ig2d`), the finite
Wedderburn block presentation is carried by `W : SemisimpleBlockData U` rather
than imposed globally on `QuantumUniverse`.

Base ring generic `{R} [CommRing R]` (§7c). No `sorry`.

-- Ref: [bghl-2017] https://doi.org/10.4171/QT/92
-/

namespace QOU.GrothendieckChern

open QOU

noncomputable section

variable {R : Type*} [CommRing R] {U : QuantumUniverse R}

/-- **The split Grothendieck group** on a semisimple block decomposition `W`:
the free abelian group on its Wedderburn blocks `W.blocks`. -/
abbrev K0 (W : SemisimpleBlockData U) : Type _ := W.blocks →₀ ℤ

/-- The class `[b]` of a block. -/
def blockClass (W : SemisimpleBlockData U) (b : W.blocks) : K0 W :=
  Finsupp.single b 1

/-- **Degree-zero Hochschild homology** on the semisimple block decomposition `W`,
presented on the central idempotents: coordinates `W.blocks → R`. -/
abbrev HH0 (W : SemisimpleBlockData U) : Type _ := W.blocks → R

/-- **The Chern character** `K₀ → HH₀`: `Σ n_b [b] ↦ Σ n_b [p_b]`. -/
def chernCharacter (W : SemisimpleBlockData U) (x : K0 W) : HH0 W :=
  fun b => (x b : R)

/-- Evaluation of a degree-zero class against the quantum dimensions. -/
def evDimQ (W : SemisimpleBlockData U) (φ : HH0 W) : R :=
  haveI := W.blocksFintype
  ∑ b, φ b * W.dimQ b

/-- The quantum dimension extended additively to `K₀`. -/
def dimQK0 (W : SemisimpleBlockData U) (x : K0 W) : R :=
  x.sum (fun b n => n • W.dimQ b)

/-- The rank: the augmentation `K₀ → ℤ`, `Σ n_b [b] ↦ Σ n_b`. -/
def rank (W : SemisimpleBlockData U) (x : K0 W) : ℤ :=
  x.sum (fun _ n => n)

theorem chernCharacter_add (W : SemisimpleBlockData U) (x y : K0 W) :
    chernCharacter W (x + y) = chernCharacter W x + chernCharacter W y := by
  funext b; simp [chernCharacter]

theorem chernCharacter_blockClass (W : SemisimpleBlockData U) [DecidableEq W.blocks]
    (b b' : W.blocks) :
    chernCharacter W (blockClass W b) b' = if b = b' then 1 else 0 := by
  simp [chernCharacter, blockClass, Finsupp.single_apply]

theorem dimQK0_add (W : SemisimpleBlockData U) (x y : K0 W) :
    dimQK0 W (x + y) = dimQK0 W x + dimQK0 W y := by
  unfold dimQK0
  rw [Finsupp.sum_add_index']
  · intro b; simp
  · intro b m n; rw [add_smul]

theorem dimQK0_blockClass (W : SemisimpleBlockData U) (b : W.blocks) :
    dimQK0 W (blockClass W b) = W.dimQ b := by
  unfold dimQK0 blockClass
  rw [Finsupp.sum_single_index]
  · simp
  · simp

theorem rank_blockClass (W : SemisimpleBlockData U) (b : W.blocks) :
    rank W (blockClass W b) = 1 := by
  unfold rank blockClass
  rw [Finsupp.sum_single_index]
  rfl

/-- **`dim_q` factors through the Chern character (sorry-free):** `dim_q = ev ∘ ch`
on `K₀`. -/
theorem dimQK0_eq_evDimQ_chernCharacter (W : SemisimpleBlockData U) (x : K0 W) :
    dimQK0 W x = evDimQ W (chernCharacter W x) := by
  letI := W.blocksFintype
  unfold dimQK0 evDimQ chernCharacter
  rw [Finsupp.sum_fintype _ _ (fun b => by simp)]
  simp only [zsmul_eq_mul]

end

end QOU.GrothendieckChern
