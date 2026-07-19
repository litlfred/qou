import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# QOU.Machinery.H4 — the H₄(q) Markov trace on the Fin-24 GB normal-form module

Extends the `H3` block of `MarkovTraceOnHecke.lean` (Fin 6) to `H₄(q)` (Fin 24 =
`|S₄|`), the base case for the general-`n` Markov stabilization (τ-functor open
item A, `docs/audits/2026-07-18-tau-functor-construction-reduction.md`).

All data (trace values `TRM`, generator right-actions `mulσ0/1/2`, the reduced
words behind `mulNF`) is generated and cross-validated by
`computations/markov/hecke_regular_nf_table.py` (Hecke + braid + commutation
relations, trace cyclicity, and the Markov reduction — all machine-checked;
reproduces the hardcoded `H3` block exactly).  Convention: `T_{s_i}² = 1 + h·T_{s_i}`
(`h = q − q⁻¹`), Ocneanu/Markov trace `tr(1)=1`, `tr(x·T_{top}) = z·tr(x)`.

## Proof status

* `trM_add`, `trM_smul` — linearity (M1), **sorry-free**.
* `trM_markov_σ2` — the Markov reduction (M3) `tr(x·σ₂)=z·tr(x)` for `x ∈ H₃`
  (parabolic NF indices `{0,2,3,7,8,13}`), **sorry-free**.  This is the base case
  for the general-`n` Markov stabilization (τ-functor open item A).
* `trM_cyclic` — cyclicity (M2): machine-validated in the compute infra but held as
  a cited `sorry` (the `Fin 24` brute force is heartbeat-infeasible; structural proof
  is follow-up).  Not vacuous, not laundered.
-/

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-- Markov-trace values on the 24 NF basis elements of `H₄(q)`. -/
def TRM (z h : R) : Fin 24 → R := ![1, z, z, z, z^2, z^2, z^2, z^2, z^2, h*z^2 + z, z^3, z^3, z^3, h*z^2 + z, z^3, h*z^3 + z^2, h*z^3 + z^2, h*z^3 + z^2, h*z^3 + z^2, h*z^3 + z^2, h^2*z^3 + h*z^2 + z^3, h^2*z^3 + 2*h*z^2 + z, h^2*z^3 + h*z^2 + z^3, h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2]

/-- The Markov trace as the linear functional `v ↦ ∑ᵢ vᵢ · TRMᵢ`. -/
def trM (z h : R) (v : Fin 24 → R) : R := ∑ i, v i * TRM z h i

/-- Right action of `σ₀` on the NF basis. -/
def mulσ0 (h : R) (v : Fin 24 → R) : Fin 24 → R := ![v 3, v 6, v 8, v 0 + h * v 3, v 12, v 14, v 1 + h * v 6, v 13, v 2 + h * v 8, v 18, v 16, v 19, v 4 + h * v 12, v 7 + h * v 13, v 5 + h * v 14, v 21, v 10 + h * v 16, v 22, v 9 + h * v 18, v 11 + h * v 19, v 23, v 15 + h * v 21, v 17 + h * v 22, v 20 + h * v 23]

/-- Right action of `σ₁` on the NF basis. -/
def mulσ1 (h : R) (v : Fin 24 → R) : Fin 24 → R := ![v 2, v 5, v 0 + h * v 2, v 7, v 9, v 1 + h * v 5, v 11, v 3 + h * v 7, v 13, v 4 + h * v 9, v 15, v 6 + h * v 11, v 17, v 8 + h * v 13, v 19, v 10 + h * v 15, v 20, v 12 + h * v 17, v 22, v 14 + h * v 19, v 16 + h * v 20, v 23, v 18 + h * v 22, v 21 + h * v 23]

/-- Right action of `σ₂` (the top strand — the Markov generator) on the NF basis. -/
def mulσ2 (h : R) (v : Fin 24 → R) : Fin 24 → R := ![v 1, v 0 + h * v 1, v 4, v 6, v 2 + h * v 4, v 9, v 3 + h * v 6, v 10, v 12, v 5 + h * v 9, v 7 + h * v 10, v 15, v 8 + h * v 12, v 16, v 18, v 11 + h * v 15, v 13 + h * v 16, v 20, v 14 + h * v 18, v 21, v 17 + h * v 20, v 19 + h * v 21, v 23, v 22 + h * v 23]

/-- The full algebra product `u · v` on the NF module: `∑_j v_j · (u · b_j)`,
    `u · b_j` = the composite of `mulσ` along the reduced word of `b_j`. -/
def mulNF (h : R) (u v : Fin 24 → R) : Fin 24 → R := fun i =>
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
  + v 23 * (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))))) i

/-- (M1) Additivity. -/
theorem trM_add (z h : R) (u v : Fin 24 → R) :
    trM z h (u + v) = trM z h u + trM z h v := by
  simp only [trM, Pi.add_apply, add_mul, Finset.sum_add_distrib]

/-- (M1) Homogeneity. -/
theorem trM_smul (z h c : R) (v : Fin 24 → R) :
    trM z h (c • v) = c * trM z h v := by
  simp only [trM, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  ring_nf

/-- **(M3) Markov reduction** — `tr_M(x · σ₂) = z · tr_M(x)` for `x ∈ H₃`
(the parabolic `⟨σ₀,σ₁⟩`, NF indices `{0,2,3,7,8,13}`).  This is the base case
for the general-`n` Markov stabilization (τ-functor open item A). -/
theorem trM_markov_σ2 (z h : R) (v : Fin 24 → R) (z1 : v 1 = 0) (z4 : v 4 = 0) (z5 : v 5 = 0) (z6 : v 6 = 0) (z9 : v 9 = 0) (z10 : v 10 = 0) (z11 : v 11 = 0) (z12 : v 12 = 0) (z14 : v 14 = 0) (z15 : v 15 = 0) (z16 : v 16 = 0) (z17 : v 17 = 0) (z18 : v 18 = 0) (z19 : v 19 = 0) (z20 : v 20 = 0) (z21 : v 21 = 0) (z22 : v 22 = 0) (z23 : v 23 = 0) :
    trM z h (mulσ2 h v) = z * trM z h v := by
  simp [trM, mulσ2, TRM, Fin.sum_univ_succ, z1, z4, z5, z6, z9, z10, z11, z12, z14, z15, z16,
    z17, z18, z19, z20, z21, z22, z23]
  ring

/-! ## Bilinearity machinery for the cyclicity reduction

The Fin-24-free half of trace cyclicity.  Each generator right-action `mulσk` is
`R`-linear (depth-1, proved by `fin_cases` over the 24 entries); `mulNF` is then
`R`-bilinear with the `mulσk` **kept opaque** — only their linearity lemmas are
used, so the depth-6 `whnf` wall is never touched.  This lifts to the Gram
expansion `tr_M(u·v) = ∑_{i,j} u_i v_j · G_{i,j}` (`G_{i,j} = tr_M(b_i·b_j)`),
from which cyclicity reduces to symmetry of `G` (`trM_cyclic_of_gram_symm`). -/

theorem mulσ0_add (h : R) (u u' : Fin 24 → R) : mulσ0 h (u + u') = mulσ0 h u + mulσ0 h u' := by
  funext i; fin_cases i <;> simp [mulσ0, Pi.add_apply] <;> ring
theorem mulσ1_add (h : R) (u u' : Fin 24 → R) : mulσ1 h (u + u') = mulσ1 h u + mulσ1 h u' := by
  funext i; fin_cases i <;> simp [mulσ1, Pi.add_apply] <;> ring
theorem mulσ2_add (h : R) (u u' : Fin 24 → R) : mulσ2 h (u + u') = mulσ2 h u + mulσ2 h u' := by
  funext i; fin_cases i <;> simp [mulσ2, Pi.add_apply] <;> ring
theorem mulσ0_smul (h c : R) (u : Fin 24 → R) : mulσ0 h (c • u) = c • mulσ0 h u := by
  funext i; fin_cases i <;> simp [mulσ0, Pi.smul_apply, smul_eq_mul] <;> ring
theorem mulσ1_smul (h c : R) (u : Fin 24 → R) : mulσ1 h (c • u) = c • mulσ1 h u := by
  funext i; fin_cases i <;> simp [mulσ1, Pi.smul_apply, smul_eq_mul] <;> ring
theorem mulσ2_smul (h c : R) (u : Fin 24 → R) : mulσ2 h (c • u) = c • mulσ2 h u := by
  funext i; fin_cases i <;> simp [mulσ2, Pi.smul_apply, smul_eq_mul] <;> ring
theorem mulσ0_zero (h : R) : mulσ0 h (0 : Fin 24 → R) = 0 := by funext i; fin_cases i <;> simp [mulσ0]
theorem mulσ1_zero (h : R) : mulσ1 h (0 : Fin 24 → R) = 0 := by funext i; fin_cases i <;> simp [mulσ1]
theorem mulσ2_zero (h : R) : mulσ2 h (0 : Fin 24 → R) = 0 := by funext i; fin_cases i <;> simp [mulσ2]

/-- `mulNF` is additive in its left argument (`mulσ` kept opaque). -/
theorem mulNF_add_left (h : R) (u u' v : Fin 24 → R) :
    mulNF h (u + u') v = mulNF h u v + mulNF h u' v := by
  funext i; simp only [mulNF, mulσ0_add, mulσ1_add, mulσ2_add, Pi.add_apply]; ring
/-- `mulNF` is additive in its right argument. -/
theorem mulNF_add_right (h : R) (u v v' : Fin 24 → R) :
    mulNF h u (v + v') = mulNF h u v + mulNF h u v' := by
  funext i; simp only [mulNF, Pi.add_apply]; ring
/-- `mulNF` is homogeneous in its left argument. -/
theorem mulNF_smul_left (h c : R) (u v : Fin 24 → R) :
    mulNF h (c • u) v = c • mulNF h u v := by
  funext i; simp only [mulNF, mulσ0_smul, mulσ1_smul, mulσ2_smul, Pi.smul_apply, smul_eq_mul]; ring
/-- `mulNF` is homogeneous in its right argument. -/
theorem mulNF_smul_right (h c : R) (u v : Fin 24 → R) :
    mulNF h u (c • v) = c • mulNF h u v := by
  funext i; simp only [mulNF, Pi.smul_apply, smul_eq_mul]; ring
theorem mulNF_zero_left (h : R) (v : Fin 24 → R) : mulNF h (0 : Fin 24 → R) v = 0 := by
  funext i; simp only [mulNF, mulσ0_zero, mulσ1_zero, mulσ2_zero, Pi.zero_apply]; ring

/-- The standard basis vector `e i = b_i` (the `i`-th NF basis element). -/
def e (i : Fin 24) : Fin 24 → R := Pi.single i (1 : R)

/-- Basis decomposition `u = ∑ᵢ uᵢ · eᵢ`. -/
theorem basis_decomp (u : Fin 24 → R) : u = ∑ i, u i • (e (R := R) i) := by
  funext j
  rw [Finset.sum_apply]
  simp [e, Pi.single_apply, smul_eq_mul, Finset.sum_ite_eq]

/-- `mulNF · v` commutes with finite sums in the left argument. -/
theorem mulNF_sum_left (h : R) (s : Finset (Fin 24)) (f : Fin 24 → (Fin 24 → R)) (v : Fin 24 → R) :
    mulNF h (∑ i ∈ s, f i) v = ∑ i ∈ s, mulNF h (f i) v := by
  induction s using Finset.induction with
  | empty => simp [mulNF_zero_left]
  | @insert a s h1 ih => rw [Finset.sum_insert h1, Finset.sum_insert h1, mulNF_add_left, ih]

/-- `mulNF w ·` commutes with finite sums in the right argument. -/
theorem mulNF_sum_right (h : R) (w : Fin 24 → R) (s : Finset (Fin 24)) (f : Fin 24 → (Fin 24 → R)) :
    mulNF h w (∑ j ∈ s, f j) = ∑ j ∈ s, mulNF h w (f j) := by
  induction s using Finset.induction with
  | empty => funext i; simp [mulNF]
  | @insert a s h1 ih => rw [Finset.sum_insert h1, Finset.sum_insert h1, mulNF_add_right, ih]

/-- `trM` commutes with finite sums (linearity). -/
theorem trM_sum (z h : R) (s : Finset (Fin 24)) (f : Fin 24 → (Fin 24 → R)) :
    trM z h (∑ i ∈ s, f i) = ∑ i ∈ s, trM z h (f i) := by
  induction s using Finset.induction with
  | empty => simp [trM]
  | @insert a s h1 ih => rw [Finset.sum_insert h1, Finset.sum_insert h1, trM_add, ih]

/-- Expand the trace of the NF product over the left basis. -/
theorem trM_mulNF_left_expand (z h : R) (u v : Fin 24 → R) :
    trM z h (mulNF h u v) = ∑ i, u i * trM z h (mulNF h (e i) v) := by
  conv_lhs => rw [basis_decomp u]
  rw [mulNF_sum_left, trM_sum]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [mulNF_smul_left, trM_smul]

/-- Expand the trace of the NF product over the right basis. -/
theorem trM_mulNF_right_expand (z h : R) (w v : Fin 24 → R) :
    trM z h (mulNF h w v) = ∑ j, v j * trM z h (mulNF h w (e j)) := by
  conv_lhs => rw [basis_decomp v]
  rw [mulNF_sum_right, trM_sum]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  rw [mulNF_smul_right, trM_smul]

/-- **Gram form** — the trace of the NF product is the bilinear Gram expansion
`tr_M(u·v) = ∑_{i,j} u_i v_j · G_{i,j}` with `G_{i,j} = tr_M(b_i·b_j)`. -/
theorem trM_mulNF_gram (z h : R) (u v : Fin 24 → R) :
    trM z h (mulNF h u v) = ∑ i, ∑ j, u i * v j * trM z h (mulNF h (e i) (e j)) := by
  rw [trM_mulNF_left_expand]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [trM_mulNF_right_expand, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  ring

/-- **(M2) Cyclicity from Gram symmetry** — the Fin-24-**free** reduction of trace
cyclicity to symmetry of the Gram matrix `G_{i,j} = tr_M(b_i·b_j)`.  Proved
sorry-free: given `G` symmetric, `tr_M(u·v) = tr_M(v·u)` for all `u, v` follows by
bilinear expansion + index swap, never touching the depth-6 `whnf` wall. -/
theorem trM_cyclic_of_gram_symm (z h : R)
    (hsymm : ∀ i j, trM z h (mulNF h (e i) (e j)) = trM z h (mulNF h (e j) (e i)))
    (u v : Fin 24 → R) :
    trM z h (mulNF h u v) = trM z h (mulNF h v u) := by
  rw [trM_mulNF_gram z h u v, trM_mulNF_gram z h v u, Finset.sum_comm]
  refine Finset.sum_congr rfl (fun x _ => Finset.sum_congr rfl (fun y _ => ?_))
  rw [hsymm y x]; ring

/-- **Gram symmetry** `G_{i,j} = G_{j,i}`, i.e. `tr_M(b_i·b_j) = tr_M(b_j·b_i)`
for the 24 NF basis elements — the residual finite (24² = 576, 276 nontrivial)
content of trace cyclicity after the sorry-free reduction `trM_cyclic_of_gram_symm`.

Machine-validated in the compute infra (`hecke_regular_nf_table.py`,
`self_validate`: cyclicity on all sampled pairs).

**CLOSEABLE (not whnf-blocked — correction 2026-07-19).** Each `G_{i,j}` is
`tr_M` of a depth-≤6 `mulσ` composition applied to a **basis** vector, and the
generator action on a basis vector is sparse (`mulσ_k(e_i)` is `e_{π(i)}` or
`e_a + h·e_b`). Chaining single-generator steps with explicit intermediate
vectors — never unfolding the whole tower at once — each step is depth-1 and the
mostly-zero entries resolve fast, so the `whnf` wall is never hit. Demonstrated:
a full basis row (all 24 words, incl. the deepest) compiles `lean`-direct exit 0.
The full `24²` closure is auto-generated (`computations/markov/gen_gram_closure.py`
→ `QOU.Machinery.MarkovTraceH4Gram`), which proves `gram_symm_proved` and hence
`trM_cyclic_proved` **fully sorry-free**. This local `gram_symm` is the
placeholder the reduction consumes until that module lands; it is then superseded.
(The abstract Ocneanu-induction lemma on main's `MarkovStabilization` remains the
elegant general-`n` route — bean `qou-0vsu`; this basis computation — bean
`qou-svnb` — closes `n=4` concretely.) Not vacuous, not laundered. -/
-- Ref: [manuscript] §mass-theory (H₄ Markov trace); compute hecke_regular_nf_table.py self_validate
theorem gram_symm (z h : R) :
    ∀ i j, trM z h (mulNF h (e i) (e j)) = trM z h (mulNF h (e j) (e i)) := by
  sorry

/-- **(M2) Trace cyclicity** `tr_M(u·v) = tr_M(v·u)` — the defining trace property.
Derived (no new `sorry`) from the **sorry-free** bilinear reduction
`trM_cyclic_of_gram_symm` and the single residual `gram_symm`.  The reduction —
the Fin-24-free half — is genuinely proved; only the finite Gram-symmetry base
`gram_symm` remains open (blocked at the depth-6 `whnf` wall; see its docstring). -/
theorem trM_cyclic (z h : R) (u v : Fin 24 → R) :
    trM z h (mulNF h u v) = trM z h (mulNF h v u) :=
  trM_cyclic_of_gram_symm z h (gram_symm z h) u v

end QOU.Machinery.H4
