import QOU.Hecke.Algebra
import Mathlib.Tactic.Module

/-!
# QOU.Braiding.HeckeGenPolyReduction — single-generator Hecke polynomial
reduction `∏ⱼ (σ + dⱼ·1) = α·σ + β·1` (Cayley–Hamilton).

**Proposition** ([`prop:hecke-generator-poly-reduction`](../../../quantum-observable-universe/braids-and-knots/hecke-generator-poly-reduction.md)).

Any product of factors `(σ_i + dⱼ·1)` in a *single* Hecke generator `σ_i`
collapses to an `R`-linear combination `α·σ_i + β·1`, with `(α, β)` given
by a DIVISION-FREE recursion driven only by the Hecke quadratic relation
`σ_i² = (q − q⁻¹)·σ_i + 1`:

```
  (α, β) for []      = (0, 1)
  (α, β) for d :: ds = (α'·(h+d) + β',  α' + β'·d)   where (α',β') = rec ds,  h = q−q⁻¹.
```

This is the algebraic core of the monotone-word fine-Bratteli transfer
matrix for the atom character (`computations/chi_monotone_transfer.py`).
The atom braid word has a monotone generator sequence, so each
per-generator operator `O_g = ∏ⱼ(σ_g + dⱼ·1)` is a single-generator
polynomial; by this reduction its seminormal *diagonal* entry is
`α·D(δ′) + β` — a function of the content gap `δ′` of the two added boxes
alone. That is what removes the `d_λ`-dimensional Hoefsmit matrix from the
χ compute (⁶Li/⁷Li in sub-second time, no `n!` wall).

The reduction holds over ANY `CommRing R` — no archimedean / `q+q⁻¹ ≠ 0`
hypothesis (per AGENTS.md §7c the structural fact is stated generically).
The eigenvalue closed form `α = (E₁−E₂)/(q+q⁻¹)`, `E₁=∏(q+dⱼ)`,
`E₂=∏(−q⁻¹+dⱼ)` used in the compute for speed is a corollary that DOES
need `2`-invertibility; only the division-free `heckeAB` recursion is
formalised here, and it suffices for correctness.

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/hecke-generator-poly-reduction.md
-/

namespace QOU.Braiding

universe u

variable {R : Type u} {A : Type u} [CommRing R] [Ring A] [Algebra R A]

/-- Division-free reduction coefficients `(α, β)` for `∏ⱼ (σ + dⱼ•1)`,
driven by the Hecke quadratic `σ*σ = h•σ + 1` with `h = q − q⁻¹`.
Empty list ↦ `(0, 1)` (the empty product is `1 = 0•σ + 1•1`). -/
def heckeAB (h : R) : List R → R × R
  | [] => (0, 1)
  | d :: ds =>
      let p := heckeAB h ds
      (p.1 * (h + d) + p.2, p.1 + p.2 * d)

@[simp] theorem heckeAB_nil (h : R) : heckeAB h ([] : List R) = (0, 1) := rfl

theorem heckeAB_cons (h d : R) (ds : List R) :
    heckeAB h (d :: ds)
      = ((heckeAB h ds).1 * (h + d) + (heckeAB h ds).2,
         (heckeAB h ds).1 + (heckeAB h ds).2 * d) := rfl

@[simp] theorem heckeAB_cons_fst (h d : R) (ds : List R) :
    (heckeAB h (d :: ds)).1 = (heckeAB h ds).1 * (h + d) + (heckeAB h ds).2 := rfl

@[simp] theorem heckeAB_cons_snd (h d : R) (ds : List R) :
    (heckeAB h (d :: ds)).2 = (heckeAB h ds).1 + (heckeAB h ds).2 * d := rfl

/-- **Single-generator Hecke polynomial reduction** (Cayley–Hamilton).

For `σ : A` satisfying the Hecke quadratic `σ * σ = h • σ + 1`, every
product `∏ⱼ (σ + dⱼ • 1)` equals `α • σ + β • 1` with `(α, β) = heckeAB h ds`.
Proof: induction on `ds`, using only the quadratic relation (no division).

This makes the per-generator block of the transfer-matrix χ a single
`α·D(δ′) + β` evaluation; see the module docstring. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/hecke-generator-poly-reduction.md
theorem hecke_gen_poly_reduction (σ : A) (h : R) (hq : σ * σ = h • σ + 1)
    (ds : List R) :
    (ds.map (fun d => σ + d • (1 : A))).prod
      = (heckeAB h ds).1 • σ + (heckeAB h ds).2 • (1 : A) := by
  induction ds with
  | nil => simp
  | cons d ds ih =>
      -- (σ + d•1)·(α•σ + β•1) with α,β = heckeAB h ds; expand, sub hq, collect
      rw [List.map_cons, List.prod_cons, ih, heckeAB_cons_fst, heckeAB_cons_snd]
      simp only [add_mul, mul_add, mul_smul_comm, smul_mul_assoc, one_mul, mul_one]
      rw [hq]
      module

end QOU.Braiding
