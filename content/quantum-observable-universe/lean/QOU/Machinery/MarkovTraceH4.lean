import Mathlib.Algebra.BigOperators.Fin
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

/-- **(M2) Trace cyclicity** `tr_M(u·v) = tr_M(v·u)` — the defining trace property.
    Machine-validated in the compute infra
    (`computations/markov/hecke_regular_nf_table.py`, `self_validate`: cyclicity holds
    on all sampled pairs, alongside the Hecke + braid + commutation relations).  The
    brute-force `simp`/`ring` expansion is infeasible at `Fin 24` (48 variables,
    depth-6 `mulσ` compositions — heartbeat timeout); a structural proof (bilinearity
    ⇒ reduce to the `24²` basis identities, or an abstract trace argument) is the
    follow-up.  Held as an honest `sorry`, not a vacuous `True`. -/
-- Ref: [manuscript] §mass-theory (H₄ Markov trace); compute hecke_regular_nf_table.py self_validate
theorem trM_cyclic (z h : R) (u v : Fin 24 → R) :
    trM z h (mulNF h u v) = trM z h (mulNF h v u) := by
  sorry

end QOU.Machinery.H4
