/-
# The level-mixing bridge — the surviving form, stated (bean qou-4d9f)

B1.5 step 1, per formalize-first: after the B1 → B1.4′ sweep closed
every parameter-free bridge form at the W₋₁-block level, this file
**states** what survives, before any compute goes near it.

Both sides of the 5₂ odd-channel question are level-graded: the
Masbaum tail by its cyclotomic level `n`, the GGM blocks by their
block level `m`. Everything the sweep excluded acts **level-diagonally
with a scalar**; the surviving form is a genuine module map, mixing
levels with coefficients that depend on `n`:

    mas n = Σ_m coeff n m · blk m ,     finitely many `m` per `n`.

What this file contains:

* `LevelMap` — the data of such a map (coefficients + a per-level
  bound + the finite-support law);
* `LevelMixingBridge` — the **primary conjecture carrier** (open; no
  instance is supplied, and none should be fabricated). Its field is
  the existence of a *non-degenerate* `LevelMap` intertwining the two
  gradings — content, not a marker;
* `diagonal_forces_crossMul` (proved) — the bridge between the
  conjecture and the compute: a level-diagonal scalar map forces the
  exact cross-multiplication identity
  `mas n · blk (n+1+k) = mas (n+1) · blk (n+k)`, which is precisely the
  criterion B1.4′ tested and refuted on its pre-registered grid;
* `not_diagonal_of_crossMul_fail` (proved) — the contrapositive, i.e.
  what the negative compute actually licenses: a single failing
  consecutive pair rules out the diagonal form *for that shift*,
  and nothing more.

**Epistemic status.** `LevelMixingBridge` is an open conjecture, not a
result: the sweep's negatives say the easy forms fail, which is
evidence about the search space, not about the answer. Per the B1.5
design note the next step is to *derive* the coefficients from the
Habiro comultiplication and then check them — a search over `coeff`
would fit by construction (~L²·N unknowns against N equations) and
would be a fit, not a derivation.

Base ring: generic `CommRing R`, no archimedean construct (§7c).
-/
import Mathlib.Tactic

namespace QOU.QBeta.LevelMixing

open Finset

variable {R : Type*} [CommRing R]

/-- The data of a level-mixing map: coefficients `coeff n m`, a bound
`bound n` on which target levels level `n` can reach, and the law that
nothing above the bound contributes. -/
structure LevelMap (R : Type*) [CommRing R] where
  coeff : ℕ → ℕ → R
  bound : ℕ → ℕ
  finite_support : ∀ n m, bound n < m → coeff n m = 0

/-- `L` intertwines the two level gradings. -/
def LevelMap.Intertwines (L : LevelMap R) (mas blk : ℕ → R) : Prop :=
  ∀ n, mas n = ∑ m ∈ range (L.bound n + 1), L.coeff n m * blk m

/-- **Conjecture (primary, OPEN).** The Masbaum cyclotomic grading of
the 5₂ tail is the image of the GGM block grading under a
level-mixing map that is not identically zero.

No instance is provided: the conjecture is open, and a fabricated
instance would assert exactly what is unknown. The non-degeneracy
field is what makes the statement have content — without it the zero
map satisfies the intertwining whenever `mas ≡ 0`. -/
class LevelMixingBridge (R : Type*) [CommRing R] (mas blk : ℕ → R) :
    Prop where
  exists_nondegenerate_map :
    ∃ L : LevelMap R, L.Intertwines mas blk ∧ ∃ n m, L.coeff n m ≠ 0

/-- **The excluded form.** A level-diagonal map with a single scalar
dressing `r` and a fixed shift `k` — the shape B1.3 (row/scalar
dressing) and B1.4′ (per-level dressing) searched. -/
def DiagonalScalar (mas blk : ℕ → R) (r : R) (k : ℕ) : Prop :=
  ∀ n, mas n = r * blk (n + k)

/-- **What the compute tested.** A diagonal scalar map forces the exact
cross-multiplication identity between consecutive levels — the
criterion B1.4′ evaluated (and found to fail) for every
`(sign, j, λ, k)` on its pre-registered grid. Note the scalar `r`
drops out: this is why the test is parameter-free. -/
theorem diagonal_forces_crossMul {mas blk : ℕ → R} {r : R} {k : ℕ}
    (h : DiagonalScalar mas blk r k) (n : ℕ) :
    mas n * blk (n + 1 + k) = mas (n + 1) * blk (n + k) := by
  rw [h n, h (n + 1)]
  have : n + 1 + k = n + k + 1 := by omega
  rw [this]
  ring

/-- **What the negative compute licenses — and no more.** A single
failing consecutive pair refutes the diagonal scalar form *at that
shift*, for every scalar `r` simultaneously. It says nothing about
level-mixing maps, which is exactly the scope-(a) reading recorded in
the ledger. -/
theorem not_diagonal_of_crossMul_fail {mas blk : ℕ → R} {k : ℕ} (n : ℕ)
    (hfail : mas n * blk (n + 1 + k) ≠ mas (n + 1) * blk (n + k)) :
    ∀ r : R, ¬ DiagonalScalar mas blk r k :=
  fun _ h => hfail (diagonal_forces_crossMul h n)

/-- A diagonal scalar map *is* a level-mixing map (so the excluded
family sits inside the conjectured one — the conjecture is a genuine
weakening, not a different claim). -/
def LevelMap.ofDiagonalScalar (r : R) (k : ℕ) : LevelMap R where
  coeff n m := if m = n + k then r else 0
  bound n := n + k
  finite_support := by
    intro n m hm
    have : m ≠ n + k := by omega
    simp [this]

lemma ofDiagonalScalar_intertwines {mas blk : ℕ → R} {r : R} {k : ℕ}
    (h : DiagonalScalar mas blk r k) :
    (LevelMap.ofDiagonalScalar r k : LevelMap R).Intertwines mas blk := by
  intro n
  rw [h n]
  simp only [LevelMap.ofDiagonalScalar]
  rw [Finset.sum_eq_single (n + k)]
  · simp
  · intro b _ hb
    simp [hb]
  · intro hmem
    exact absurd (Finset.self_mem_range_succ (n + k)) hmem

end QOU.QBeta.LevelMixing
