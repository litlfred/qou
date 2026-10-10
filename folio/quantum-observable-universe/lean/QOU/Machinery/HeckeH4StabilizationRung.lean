/-
# H₄(q) NF tables + the H₃ ↪ H₄ Markov stabilization rung — Lean-grade

Closes the item `MarkovTraceOnHecke` §"Extending past H₃" left open: *"the
`n = 4` case is numerically confirmed … the Lean-grade proof still awaits
ingredient (1) [the H₄ NF table]"*. The table is here, and the rung is
proved.

Provenance (ingredient 1, per the file's own discipline): the 24-word S₄
GB-NF basis — ordered with the H₃ Lean basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]` as
its prefix — and the generator right-actions by the exact Iwahori–Hecke
length rule, pinned and cross-verified over `ℚ(z,h)` by the symbolic
preflight `computations/probes/hecke_h4_nf_table_preflight.py` (which also
derives the 24 trace weights as the UNIQUE solution of cyclicity +
Markov-σ₂ reduction + `tr(1) = 1` — the weights below are derived data, not
choices).

Proved here (sorry-free):

* the three generator actions satisfy the Hecke quadratic; both adjacent
  braid relations hold; and **far commutation σ₀σ₂ = σ₂σ₀** — non-vacuous
  for the first time at n = 4 (the F1 monoidal-interchange shadow, until
  now only a class field);
* `iota34` (the H₃ ↪ H₄ inclusion on NF coordinates) **intertwines** the
  σ₀/σ₁ actions;
* **`trM4_iota34_stabilizes`** — `tr₄(ι x) = tr₃ x`: the H₃ ↪ H₄ Markov
  stabilization, Lean-grade (was numerically-confirmed only);
* **`trM4_markov_σ₂`** — `tr₄((ι x)·σ₂) = z·tr₃ x`: the (M3) Markov
  reduction at the new rung.

HONESTY (STRICT): this is the concrete `n = 3 → 4` rung; the general-n
`MarkovStabilization` class instance stays OPEN (its `HeckeBraidedPresentation`
binders quantify the H_∞ generator family; see `HeckeH3AlgebraLaws`).
Nothing wired; `1/(8π)` stays phase-4.

Base ring (§7c): generic `[CommRing R]` — no `ℝ`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.MarkovTraceOnHecke

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-- Right action of `σ₀` on the 24-element S₄ NF basis (preflight-pinned). -/
def mulσ₀ (h : R) (v : Fin 24 → R) : Fin 24 → R := ![
  v 1, v 0 + h * v 1, v 3, v 2 + h * v 3,
  v 5, v 4 + h * v 5, v 8, v 11,
  v 6 + h * v 8, v 14, v 15, v 7 + h * v 11,
  v 18, v 19, v 9 + h * v 14, v 10 + h * v 15,
  v 21, v 22, v 12 + h * v 18, v 13 + h * v 19,
  v 23, v 16 + h * v 21, v 17 + h * v 22, v 20 + h * v 23]

/-- Right action of `σ₁` on the 24-element S₄ NF basis (preflight-pinned). -/
def mulσ₁ (h : R) (v : Fin 24 → R) : Fin 24 → R := ![
  v 2, v 4, v 0 + h * v 2, v 5,
  v 1 + h * v 4, v 3 + h * v 5, v 9, v 12,
  v 13, v 6 + h * v 9, v 16, v 17,
  v 7 + h * v 12, v 8 + h * v 13, v 19, v 20,
  v 10 + h * v 16, v 11 + h * v 17, v 22, v 14 + h * v 19,
  v 15 + h * v 20, v 23, v 18 + h * v 22, v 21 + h * v 23]

/-- Right action of `σ₂` on the 24-element S₄ NF basis (preflight-pinned). -/
def mulσ₂ (h : R) (v : Fin 24 → R) : Fin 24 → R := ![
  v 6, v 8, v 7, v 11,
  v 10, v 15, v 0 + h * v 6, v 2 + h * v 7,
  v 1 + h * v 8, v 12, v 4 + h * v 10, v 3 + h * v 11,
  v 9 + h * v 12, v 16, v 18, v 5 + h * v 15,
  v 13 + h * v 16, v 20, v 14 + h * v 18, v 21,
  v 17 + h * v 20, v 19 + h * v 21, v 23, v 22 + h * v 23]

/-- Markov–Ocneanu–Wenzl weights on the 24-element basis — the UNIQUE
solution of cyclicity + Markov-σ₂ reduction + `tr(1)=1` (preflight-derived;
first six = the H₃ weights). -/
def TRM4 (z h : R) : Fin 24 → R := ![
  1, z, z, z ^ 2,
  z ^ 2, h * z ^ 2 + z, z, z ^ 2,
  z ^ 2, z ^ 2, z ^ 3, z ^ 3,
  h * z ^ 2 + z, z ^ 3, z ^ 3, h * z ^ 3 + z ^ 2,
  h * z ^ 3 + z ^ 2, h * z ^ 3 + z ^ 2, h * z ^ 3 + z ^ 2, h * z ^ 3 + z ^ 2,
  h ^ 2 * z ^ 3 + h * z ^ 2 + z ^ 3, h ^ 2 * z ^ 3 + 2 * h * z ^ 2 + z,
  h ^ 2 * z ^ 3 + h * z ^ 2 + z ^ 3,
  h ^ 3 * z ^ 3 + h ^ 2 * z ^ 2 + 2 * h * z ^ 3 + z ^ 2]

/-- The level-4 Markov trace: `v ↦ ∑ᵢ vᵢ · TRM4ᵢ`. -/
def trM4 (z h : R) (v : Fin 24 → R) : R := ∑ i, v i * TRM4 z h i

/-- (M1) Additivity — the `trM4` counterpart of `MarkovTraceH4.trM_add`. -/
theorem trM4_add (z h : R) (u v : Fin 24 → R) :
    trM4 z h (u + v) = trM4 z h u + trM4 z h v := by
  simp only [trM4, Pi.add_apply, add_mul, Finset.sum_add_distrib]

/-- (M1) Homogeneity — the `trM4` counterpart of `MarkovTraceH4.trM_smul`. -/
theorem trM4_smul (z h c : R) (v : Fin 24 → R) :
    trM4 z h (c • v) = c * trM4 z h v := by
  simp only [trM4, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  ring_nf

/-- Hecke quadratic for σ₀ at level 4: `σ₀² = h·σ₀ + 1`. -/
theorem mulσ₀_hecke (h : R) (v : Fin 24 → R) :
    mulσ₀ h (mulσ₀ h v) = h • mulσ₀ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₀, Pi.add_apply, Pi.smul_apply, smul_eq_mul] <;> ring

/-- Hecke quadratic for σ₁ at level 4. -/
theorem mulσ₁_hecke (h : R) (v : Fin 24 → R) :
    mulσ₁ h (mulσ₁ h v) = h • mulσ₁ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₁, Pi.add_apply, Pi.smul_apply, smul_eq_mul] <;> ring

/-- Hecke quadratic for σ₂ at level 4. -/
theorem mulσ₂_hecke (h : R) (v : Fin 24 → R) :
    mulσ₂ h (mulσ₂ h v) = h • mulσ₂ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₂, Pi.add_apply, Pi.smul_apply, smul_eq_mul] <;> ring

/-- Braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁` at level 4. -/
theorem braid_σ₀σ₁ (h : R) (v : Fin 24 → R) :
    mulσ₀ h (mulσ₁ h (mulσ₀ h v)) = mulσ₁ h (mulσ₀ h (mulσ₁ h v)) := by
  funext i
  fin_cases i <;> simp [mulσ₀, mulσ₁] <;> ring

/-- Braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` at level 4. -/
theorem braid_σ₁σ₂ (h : R) (v : Fin 24 → R) :
    mulσ₁ h (mulσ₂ h (mulσ₁ h v)) = mulσ₂ h (mulσ₁ h (mulσ₂ h v)) := by
  funext i
  fin_cases i <;> simp [mulσ₁, mulσ₂] <;> ring

/-- **Far commutation `σ₀σ₂ = σ₂σ₀`** — the F1 monoidal-interchange shadow,
non-vacuous for the FIRST time at n = 4 (at n ≤ 3 there is no non-adjacent
pair). Until now this presentation law existed only as a class field. -/
theorem far_commute_σ₀σ₂ (h : R) (v : Fin 24 → R) :
    mulσ₀ h (mulσ₂ h v) = mulσ₂ h (mulσ₀ h v) := by
  funext i
  fin_cases i <;> simp [mulσ₀, mulσ₂] <;> try ring

/-! ## The H₃ ↪ H₄ stabilization rung -/

/-- The `H₃ ↪ H₄` inclusion on NF coordinates: the 24-basis is ordered with
the H₃ Lean basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]` as its prefix, so the inclusion
extends by zero. -/
def iota34 (v : Fin 6 → R) : Fin 24 → R := ![
  v 0, v 1, v 2, v 3, v 4, v 5,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

/-- The inclusion intertwines the σ₀ actions: `ι(x)·σ₀ = ι(x·σ₀)`. -/
theorem iota34_mulσ₀ (h : R) (v : Fin 6 → R) :
    mulσ₀ h (iota34 v) = iota34 (H3.mulσ₀ h v) := by
  funext i
  fin_cases i <;> simp [mulσ₀, H3.mulσ₀, iota34]

/-- The inclusion intertwines the σ₁ actions: `ι(x)·σ₁ = ι(x·σ₁)`. -/
theorem iota34_mulσ₁ (h : R) (v : Fin 6 → R) :
    mulσ₁ h (iota34 v) = iota34 (H3.mulσ₁ h v) := by
  funext i
  fin_cases i <;> simp [mulσ₁, H3.mulσ₁, iota34]

/-- **The H₃ ↪ H₄ Markov stabilization, Lean-grade**: `tr₄(ι x) = tr₃ x`.
This is the `n = 3 → 4` case `MarkovTraceOnHecke` recorded as numerically
confirmed and Lean-blocked on the H₄ table — now proved. -/
theorem trM4_iota34_stabilizes (z h : R) (v : Fin 6 → R) :
    trM4 z h (iota34 v) = H3.trM z h v := by
  simp [trM4, H3.trM, TRM4, H3.TRM, iota34, Fin.sum_univ_succ]
  try ring

/-- **The (M3) Markov reduction at the new rung**: `tr₄((ι x)·σ₂) = z·tr₃ x`
for every `x ∈ H₃`. Together with `trM4_iota34_stabilizes` this is the
complete concrete content of the `n = 3 → 4` stabilization step. -/
theorem trM4_markov_σ₂ (z h : R) (v : Fin 6 → R) :
    trM4 z h (mulσ₂ h (iota34 v)) = z * H3.trM z h v := by
  simp [trM4, H3.trM, TRM4, H3.TRM, iota34, mulσ₂, Fin.sum_univ_succ]
  try ring

end QOU.Machinery.H4
