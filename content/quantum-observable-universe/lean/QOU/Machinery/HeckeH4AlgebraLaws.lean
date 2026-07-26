/-
# H₄(q) NF module is an algebra object — unit laws, generator commutation, associativity

Categorical tranche, the n=4 mirror of `HeckeH3AlgebraLaws` (W4 slice 1 of the
epic `qou-utb3`; route (b) of
`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md` §3).  The `H4`
block (`MarkovTraceH4.lean`) carries the trace laws (M1/M3 proved; M2 closed by
the generated `MarkovTraceH4Gram`) and the bilinearity of `mulNF`; this file
adds the remaining *algebra-object* laws needed to package the Fin-24 NF module
as an honest `Ring`/`Algebra` (in `HeckeH4AlgebraInstance`):

* **Unit laws** — `unitNF = e₀ = ![1,0,…,0]` is a two-sided unit
  (`mulNF_one_left`, `mulNF_one_right`), plus `mulNF_zero_right`.
* **Generator commutation** — `mulσk (u·v) = u·(v·σk)` for each of the three
  generators (`mulσ0_mulNF`, `mulσ1_mulNF`, `mulσ2_mulNF`): associativity with a
  single generator as the right factor.  Each is a per-entry polynomial identity
  at composition depth ≤ 7 (one `mulσ` over one `mulNF`), closed by
  `fin_cases <;> simp <;> ring` — the depth-6 `whnf` wall (which blocks the
  *double*-`mulNF` brute force, depth 12) is never hit.
* **Associativity** (`mulNF_assoc`) — derived from the three generator
  commutations by the same atom-level bilinear-expansion discipline as
  `trM_cyclic_of_gram_symm`: unfold only the outer `mulNF` applications, chain
  the generator commutations along each basis word, and close by `ring` with
  the word actions `(W_j v) m`, `(W_m u) i` kept opaque as atoms.  No deep
  unfolding, no 24³ enumeration.

Proof-technique note (why this file does not copy `HeckeH3AlgebraLaws`
line-for-line): at n=3 associativity was a direct
`fin_cases <;> simp [mulNF, mulσ₀, mulσ₁] <;> ring` (depth ≤ 3, 6 entries);
at n=4 that direct unfold is the depth-12 double-`mulNF` blow-up the H4 module
docstring documents as heartbeat-infeasible.  The generator-commutation
factoring is the same statement, reached wall-free.

All data is generated and cross-validated by
`computations/markov/hecke_regular_nf_table.py` (Hecke + braid + commutation
relations machine-checked; reproduces the hardcoded `H3` block exactly).

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): everything here is proved
content over generic `[CommRing R]` — no class discharge, no conjecture input.
The general-`n` classes (`HeckeBraidedPresentation`, `MarkovStabilization`)
stay OPEN; the Ocneanu conditional-expectation tower (W2/W3, beans `qou-2017` /
`qou-r765`) remains the general-`n` route.

Base ring (§7c): generic `[CommRing R]` throughout — no `ℝ`, no ordering,
no archimedean construct.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-/
import QOU.Machinery.MarkovTraceH4

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-! ## Applied form of `mulNF` -/

/-- Applied form of `mulNF` (β-reduction), used to unfold *only* the outer
product while the word actions stay opaque (unit laws, associativity). -/
theorem mulNF_apply (h : R) (u v : Fin 24 → R) (i : Fin 24) :
    mulNF h u v i =
      v 0 * u i
    + v 1 * (mulσ2 h (u)) i
    + v 2 * (mulσ1 h (u)) i
    + v 3 * (mulσ0 h (u)) i
    + v 4 * (mulσ2 h (mulσ1 h (u))) i
    + v 5 * (mulσ1 h (mulσ2 h (u))) i
    + v 6 * (mulσ0 h (mulσ2 h (u))) i
    + v 7 * (mulσ1 h (mulσ0 h (u))) i
    + v 8 * (mulσ0 h (mulσ1 h (u))) i
    + v 9 * (mulσ1 h (mulσ2 h (mulσ1 h (u)))) i
    + v 10 * (mulσ2 h (mulσ1 h (mulσ0 h (u)))) i
    + v 11 * (mulσ1 h (mulσ0 h (mulσ2 h (u)))) i
    + v 12 * (mulσ0 h (mulσ2 h (mulσ1 h (u)))) i
    + v 13 * (mulσ0 h (mulσ1 h (mulσ0 h (u)))) i
    + v 14 * (mulσ0 h (mulσ1 h (mulσ2 h (u)))) i
    + v 15 * (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))) i
    + v 16 * (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))) i
    + v 17 * (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (u))))) i
    + v 18 * (mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (u))))) i
    + v 19 * (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (u))))) i
    + v 20 * (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u)))))) i
    + v 21 * (mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (u)))))) i
    + v 22 * (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (u)))))) i
    + v 23 * (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))))) i :=
  rfl

/-! ## Unit laws -/

/-- The unit of the H₄(q) NF algebra: γ = e₀ = `![1,0,…,0]`. -/
def unitNF : Fin 24 → R :=
  ![1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

set_option maxHeartbeats 1600000 in
/-- **Right unit law**: `u · γ = u` (the `j = 0` coefficient of `unitNF` is 1;
all other coefficients vanish, so the word actions stay opaque). -/
theorem mulNF_one_right (h : R) (u : Fin 24 → R) :
    mulNF h u unitNF = u := by
  funext i
  rw [mulNF_apply]
  simp [unitNF]

set_option maxHeartbeats 1600000 in
/-- **Left unit law**: `γ · v = v` — each basis word applied to γ reproduces
the corresponding NF basis element (`word_j(γ) = b_j`); sparse evaluation,
so the per-entry unfold resolves fast. -/
theorem mulNF_one_left (h : R) (v : Fin 24 → R) :
    mulNF h unitNF v = v := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ0, mulσ1, mulσ2, unitNF]

set_option maxHeartbeats 1600000 in
/-- `mulNF` kills a zero right factor. -/
theorem mulNF_zero_right (h : R) (u : Fin 24 → R) :
    mulNF h u (0 : Fin 24 → R) = 0 := by
  funext i
  rw [mulNF_apply]
  simp

/-! ## Generator commutation — associativity with a generator right factor

`(u·v)·σk = u·(v·σk)` at the coordinate level: the right action `mulσk` of a
single generator commutes past a full NF product.  Composition depth ≤ 7
(one `mulσ` over one `mulNF`), so the per-entry polynomial identities stay
below the depth-12 double-`mulNF` wall. -/

set_option maxHeartbeats 1600000 in
/-- `(u·v)·σ₀ = u·(v·σ₀)` on NF coordinates. -/
theorem mulσ0_mulNF (h : R) (u v : Fin 24 → R) :
    mulσ0 h (mulNF h u v) = mulNF h u (mulσ0 h v) := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ0, mulσ1, mulσ2] <;> ring

set_option maxHeartbeats 1600000 in
/-- `(u·v)·σ₁ = u·(v·σ₁)` on NF coordinates. -/
theorem mulσ1_mulNF (h : R) (u v : Fin 24 → R) :
    mulσ1 h (mulNF h u v) = mulNF h u (mulσ1 h v) := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ0, mulσ1, mulσ2] <;> ring

set_option maxHeartbeats 1600000 in
/-- `(u·v)·σ₂ = u·(v·σ₂)` on NF coordinates. -/
theorem mulσ2_mulNF (h : R) (u v : Fin 24 → R) :
    mulσ2 h (mulNF h u v) = mulNF h u (mulσ2 h v) := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ0, mulσ1, mulσ2] <;> ring

/-! ## Associativity -/

set_option maxHeartbeats 1600000 in
/-- **Associativity of the full H₄(q) NF product**: `(u·v)·w = u·(v·w)`.
Derived from the three generator commutations: unfold the outer `mulNF`
applications, chain `mulσk (mulNF u x) = mulNF u (mulσk x)` along each basis
word, then close by `ring` with the word actions kept opaque as atoms —
never unfolding the depth-12 double-`mulNF` tower.  With bilinearity and the
unit laws, the Fin-24 NF module is an associative unital `R`-algebra. -/
theorem mulNF_assoc (h : R) (u v w : Fin 24 → R) :
    mulNF h (mulNF h u v) w = mulNF h u (mulNF h v w) := by
  funext i
  simp only [mulNF_apply, mulσ0_mulNF, mulσ1_mulNF, mulσ2_mulNF]
  ring

end QOU.Machinery.H4
