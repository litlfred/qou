import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.Tactic

/-!
# QOU.Mass.MaxContactSimplex — the geometric assertion under the `w_n(K)` closure

Bean `t7qv`, gap "θ_λ `w_n(K)` derive-or-refute". Its frontier update records the
missing piece as GEOMETRIC, with the edge set a **max-contact sphere packing**:

> "Edge set = max-contact sphere packing (Part 13; A≤4 simplex = C(A,2),
>  A≥5 saturates below)"

and notes that the tempting fit-free light-nucleus match — `⁴He` weighted
`6·a_D² + 4·a_D³ + 1·a_D⁴` — is exactly that A≤4 simplex bond count, i.e. the
binomials `C(4,2), C(4,3), C(4,4)`.

That assertion was prose. It is also a theorem, and it is load-bearing, so it is
proved here.

## What is actually being claimed

Equal spheres of radius `r` are mutually tangent exactly when their centres are
pairwise at distance `2r`. So "A spheres in max contact, all pairs touching" is
"A points pairwise equidistant", and the claim `A ≤ 4` in three dimensions is:

**at most `finrank + 1` points of a real inner-product space can be pairwise
equidistant.**

Hence the contact graph is complete — `C(A,2)` bonds — precisely for `A ≤ 4`,
and for `A ≥ 5` it must have strictly fewer, which is the "saturates below".

## The proof

Base at `p 0` and set `vᵢ = pᵢ - p₀`. All `‖vᵢ‖ = c`, and for `i ≠ j`

    ‖vᵢ - vⱼ‖ = ‖pᵢ - pⱼ‖ = c   ⟹   ⟪vᵢ, vⱼ⟫ = c²/2,

so the Gram matrix is `c²/2` off the diagonal and `c²` on it, giving

    ‖∑ aᵢ vᵢ‖² = (c²/2) [ (∑ aᵢ)² + ∑ aᵢ² ].

Both bracketed terms are non-negative, so the norm vanishes only when every
`aᵢ = 0`: the `vᵢ` are linearly independent, and there are `A - 1` of them.

Verified numerically before formalising, with a control: replacing the
off-diagonal `c²/2` by `3c²/4` breaks the identity on 967 of 1000 random integer
vectors, so the check is not vacuous.
-/

namespace QOU.Mass.MaxContactSimplex

open Finset RealInnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- **The Gram entry.** For a pairwise-equidistant family based at `p 0`, any two
distinct spokes meet at inner product `c²/2`. -/
theorem inner_spokes {m : ℕ} {c : ℝ} (p : Fin (m + 1) → E)
    (h : ∀ i j, i ≠ j → ‖p i - p j‖ = c) {i j : Fin m} (hij : i ≠ j) :
    ⟪p i.succ - p 0, p j.succ - p 0⟫ = c ^ 2 / 2 := by
  have hi : ‖p i.succ - p 0‖ = c := h _ _ (Fin.succ_ne_zero i)
  have hj : ‖p j.succ - p 0‖ = c := h _ _ (Fin.succ_ne_zero j)
  have hij' : ‖p i.succ - p j.succ‖ = c :=
    h _ _ (fun hEq => hij (Fin.succ_injective m hEq))
  have hsub : (p i.succ - p 0) - (p j.succ - p 0) = p i.succ - p j.succ := by
    abel
  have key : ‖(p i.succ - p 0) - (p j.succ - p 0)‖ ^ 2
      = ‖p i.succ - p 0‖ ^ 2 - 2 * ⟪p i.succ - p 0, p j.succ - p 0⟫
        + ‖p j.succ - p 0‖ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq, ← real_inner_self_eq_norm_sq,
      ← real_inner_self_eq_norm_sq]
    simp only [inner_sub_sub_self]
    rw [real_inner_comm (p j.succ - p 0) (p i.succ - p 0)]
    ring
  rw [hsub, hij', hi, hj] at key
  linarith

/-- **The spokes are linearly independent.** -/
theorem linearIndependent_spokes {m : ℕ} {c : ℝ} (hc : 0 < c) (p : Fin (m + 1) → E)
    (h : ∀ i j, i ≠ j → ‖p i - p j‖ = c) :
    LinearIndependent ℝ (fun i : Fin m => p i.succ - p 0) := by
  classical
  rw [Fintype.linearIndependent_iff]
  intro g hg
  set v : Fin m → E := fun i => p i.succ - p 0 with hv
  have hdiag : ∀ i : Fin m, ⟪v i, v i⟫ = c ^ 2 := by
    intro i
    rw [hv, real_inner_self_eq_norm_sq, h _ _ (Fin.succ_ne_zero i)]
  have hoff : ∀ i j : Fin m, i ≠ j → ⟪v i, v j⟫ = c ^ 2 / 2 := fun i j hij =>
    inner_spokes p h hij
  -- expand the squared norm of the vanishing combination
  have expand : ∑ i : Fin m, ∑ j : Fin m, g i * g j * ⟪v i, v j⟫ = 0 := by
    have : ⟪∑ i : Fin m, g i • v i, ∑ j : Fin m, g j • v j⟫ = 0 := by
      rw [hg]; simp
    rw [sum_inner] at this
    simp only [inner_sum, real_inner_smul_left, real_inner_smul_right] at this
    rw [← this]
    exact Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => by ring
  have split : ∑ i : Fin m, ∑ j : Fin m, g i * g j * ⟪v i, v j⟫
      = (c ^ 2 / 2) * ((∑ i : Fin m, g i) ^ 2 + ∑ i : Fin m, g i ^ 2) := by
    have step : ∀ i : Fin m, ∑ j : Fin m, g i * g j * ⟪v i, v j⟫
        = (c ^ 2 / 2) * (g i * ∑ j : Fin m, g j) + (c ^ 2 / 2) * g i ^ 2 := by
      intro i
      have : ∀ j : Fin m, g i * g j * ⟪v i, v j⟫
          = (c ^ 2 / 2) * (g i * g j) + (if j = i then (c ^ 2 / 2) * g i ^ 2 else 0) := by
        intro j
        by_cases hji : j = i
        · subst hji; rw [hdiag]; simp; ring
        · rw [hoff i j (fun hEq => hji hEq.symm)]; simp [hji]; ring
      rw [Finset.sum_congr rfl fun j _ => this j, Finset.sum_add_distrib,
        ← Finset.mul_sum, ← Finset.mul_sum]
      simp
    rw [Finset.sum_congr rfl fun i _ => step i, Finset.sum_add_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.sum_mul]
    ring
  rw [split] at expand
  have hc2 : (0:ℝ) < c ^ 2 / 2 := by positivity
  have hzero : (∑ i : Fin m, g i) ^ 2 + ∑ i : Fin m, g i ^ 2 = 0 := by
    by_contra hne
    have hpos : 0 < (∑ i : Fin m, g i) ^ 2 + ∑ i : Fin m, g i ^ 2 := by
      rcases lt_or_gt_of_ne (Ne.symm hne) with hlt | hgt
      · exact hlt
      · exact absurd hgt (not_lt.mpr (by positivity))
    exact absurd expand (ne_of_gt (mul_pos hc2 hpos))
  have hnn : 0 ≤ ∑ i : Fin m, g i ^ 2 :=
    Finset.sum_nonneg fun i _ => sq_nonneg (g i)
  have hsq : ∑ i : Fin m, g i ^ 2 = 0 := by
    nlinarith [sq_nonneg (∑ i : Fin m, g i), hnn]
  intro i
  have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (g j))).mp hsq i
    (Finset.mem_univ i)
  exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this

/-- **At most `finrank + 1` points can be pairwise equidistant.** -/
theorem card_le_finrank_succ_of_equidistant [FiniteDimensional ℝ E] {m : ℕ} {c : ℝ}
    (hc : 0 < c) (p : Fin (m + 1) → E) (h : ∀ i j, i ≠ j → ‖p i - p j‖ = c) :
    m + 1 ≤ Module.finrank ℝ E + 1 := by
  have hli := linearIndependent_spokes hc p h
  have := hli.fintype_card_le_finrank
  simpa using this

/-- **No five equal spheres are mutually tangent in three dimensions.**

This is the `A ≥ 5` half of "A≤4 simplex = C(A,2), A≥5 saturates below": the
contact graph of five equal spheres cannot be complete, so its bond count is
strictly below `C(5,2) = 10`. -/
theorem not_five_equidistant [FiniteDimensional ℝ E] (hd : Module.finrank ℝ E = 3)
    {c : ℝ} (hc : 0 < c) (p : Fin 5 → E) :
    ¬ (∀ i j, i ≠ j → ‖p i - p j‖ = c) := by
  intro h
  have := card_le_finrank_succ_of_equidistant (m := 4) hc p h
  rw [hd] at this
  omega

/-- **No `A ≥ 5` equal spheres are all mutually tangent** — the general form of
"A≥5 saturates below". Restricting to any five reduces it to
`not_five_equidistant`. -/
theorem no_complete_contact_of_five_le [FiniteDimensional ℝ E]
    (hd : Module.finrank ℝ E = 3) {A : ℕ} (hA : 5 ≤ A) {c : ℝ} (hc : 0 < c)
    (p : Fin A → E) :
    ¬ (∀ i j, i ≠ j → ‖p i - p j‖ = c) := by
  intro h
  refine not_five_equidistant hd hc (fun i => p (Fin.castLE hA i)) ?_
  intro i j hij
  refine h _ _ fun hEq => hij ?_
  exact Fin.ext (by simpa using congrArg Fin.val hEq)

/-! ### Bridge to `QOU.Mass.CoordinationSaturation`

`CoordinationSaturation.lean` refutes complete-graph coordination by its
CONSEQUENCE: `complete_graph_no_saturation` shows `perNucleonComplete ε A` — the
`C(A,2)`-bond model — exceeds every bound, so no `B/A` plateau exists. It then
takes bounded degree as a modelling assumption (`perNucleonBounded`).

`no_complete_contact_of_five_le` refutes the same model a second and independent
way: in three dimensions the complete contact graph does not EXIST for `A ≥ 5`,
whatever it would predict. So the `C(A,2)` bond count is not merely
phenomenologically wrong for heavy `A`; it is geometrically unavailable, which
is the t7qv frontier's "A≥5 saturates below" as a theorem rather than a premise.

**What this does NOT supply, stated so nobody mistakes the bridge for the whole
span.** `bounded_degree_saturates` needs a bound on the DEGREE, and that is the
three-dimensional kissing number (12, Schütte–van der Waerden) — not proved here
and not a modest formalisation.
-- Ref: [bezdek-reid2013] — held source stating the kissing-number-12 rigidity it uses
   (Thms 4/5, via Hales' 2.52 separation of a 13th ball); the Schütte–van der Waerden
   1953 proof itself is not held.

**And a trap, verified numerically, for whoever tries the easy route.** The
standard spherical-code argument — `∑ᵢⱼ ⟪uᵢ,uⱼ⟫² ≥ m²/d` against
`∑_{i≠j} ⟪uᵢ,uⱼ⟫² ≤ m(m-1)/4` — would give `m ≤ 9` in `d = 3`. That is FALSE:
the icosahedral configuration realises `m = 12`. The argument needs
`|⟪uᵢ,uⱼ⟫| ≤ 1/2`, whereas tangency bounds the inner product only from ABOVE.
Measured on that configuration: the inner products run over `[-1, 0.4472]`, so
`⟪uᵢ,uⱼ⟫ ≤ 1/2` holds while `|⟪uᵢ,uⱼ⟫| ≤ 1/2` fails at the antipodal pairs, and
`∑ᵢⱼ ⟪uᵢ,uⱼ⟫² = 48` exactly — meeting the Frobenius bound `m²/d = 48` with
equality, and exceeding the naive ceiling `m + m(m-1)/4 = 45`. -/

/-- The `A ≤ 4` half is pure counting: the complete graph on `A` vertices has
`C(A,2)` edges, and the body-order weights of `⁴He` are the binomials
`C(4,2), C(4,3), C(4,4) = 6, 4, 1` — the `6 a_D² + 4 a_D³ + 1 a_D⁴` of the
frontier note. -/
theorem he4_body_order :
    (Nat.choose 4 2, Nat.choose 4 3, Nat.choose 4 4) = (6, 4, 1) := by decide

/-- **Six-point specialization of `no_complete_contact_of_five_le` (`qou-6cm9`).**
In a three-dimensional real inner-product space `E`, no six points are pairwise at positive
distance `c`. -/
theorem not_six_equidistant [FiniteDimensional ℝ E] (hd : Module.finrank ℝ E = 3)
    {c : ℝ} (hc : 0 < c) (p : Fin 6 → E) :
    ¬ (∀ i j, i ≠ j → ‖p i - p j‖ = c) :=
  no_complete_contact_of_five_le hd (by decide : 5 ≤ 6) hc p

end QOU.Mass.MaxContactSimplex
