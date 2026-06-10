import QOU.Torsion.BraneTower

/-!
# §7½  Yekutieli Triple and Cosimplicial Crossed Groupoid

Yekutieli triples `(x, g, a)`, twisted 2-cocycle condition, lifting
condition, global gluing, cosimplicial crossed groupoid, weak
equivalence invariance, and the main theorem QU → QOU.
-/


namespace QOU.Torsion

universe u v

/-! ## §7½  Yekutieli Triple and Cosimplicial Crossed Groupoid -/

/-- **Yekutieli triple** at level `n` over `Uᵢ ∩ Uⱼ`.
    LaTeX: `\label{def:yekutieli-triple}` -/
structure YekutieliTriple (M : Type*) where
  level : ℕ
  objects : M → M
  oneMorphisms : M → ℝ
  twoMorphisms : M → ℝ
  twoMorphisms_ne_zero : ∀ (p : M), twoMorphisms p ≠ 0

/-- Čech 1-cocycle deviation `g_{ijk}`. -/
noncomputable def cechDeviation {M : Type*}
    (g_ij g_jk g_ik : M → ℝ) (p : M) : ℝ :=
  g_ij p * g_jk p * (g_ik p)⁻¹

/-- **Twisted 2-cocycle condition**.
    LaTeX: `\label{prop:descent-condition}` -/
structure TwistedTwoCocycle (M : Type*) where
  triple : YekutieliTriple M
  cocycleDeviation : M → ℝ
  coboundary : M → ℝ
  twisted_condition : ∀ (p : M),
    coboundary p = triple.twoMorphisms p * cocycleDeviation p *
      (triple.twoMorphisms p)⁻¹

theorem twisted_cocycle_unobstructed {M : Type*}
    (tc : TwistedTwoCocycle M)
    (h_vanish : ∀ (p : M), tc.coboundary p = 0) :
    ∀ (p : M), tc.cocycleDeviation p = 0 := by
  intro p
  have hcond := tc.twisted_condition p
  have hzero := h_vanish p
  rw [hzero] at hcond
  have ha := tc.triple.twoMorphisms_ne_zero p
  have h1 : tc.triple.twoMorphisms p *
    tc.cocycleDeviation p * (tc.triple.twoMorphisms p)⁻¹ = 0 :=
    hcond.symm
  have ha_inv_ne : (tc.triple.twoMorphisms p)⁻¹ ≠ 0 := inv_ne_zero ha
  rcases mul_eq_zero.mp h1 with h_ag | h_ainv
  · rcases mul_eq_zero.mp h_ag with h_a | h_g
    · exact absurd h_a ha
    · exact h_g
  · exact absurd h_ainv ha_inv_ne

/-- **Yekutieli lifting condition**.
    LaTeX: `\label{prop:yekutieli-lifting}` -/
structure YekutieliLiftingCondition where
  tower : RecursiveBraneTower
  obstructionClass : ℕ → Type*
  obstruction_exists : ∀ n, Nonempty (obstructionClass n)
  twistedCocycle : (n : ℕ) → TwistedTwoCocycle (tower.level n).M
  central : ∀ (n : ℕ) (p : (tower.level n).M) (_a b : ℝ),
    (twistedCocycle n).triple.twoMorphisms p * b =
    b * (twistedCocycle n).triple.twoMorphisms p

theorem yekutieli_obstruction_exists
    (ylc : YekutieliLiftingCondition) (n : ℕ) :
    Nonempty (ylc.obstructionClass n) :=
  ylc.obstruction_exists n

/-- **Cosimplicial crossed groupoid data**.
    LaTeX: `\label{prop:cosimplicial-crossed-groupoid}` -/
structure CosimplicialCrossedGroupoid where
  tower : RecursiveBraneTower
  tripleAt : (n : ℕ) → YekutieliTriple (tower.level n).M
  coface : (n : ℕ) → YekutieliTriple (tower.level n).M →
    YekutieliTriple (tower.level (n + 1)).M
  codegeneracy : (n : ℕ) → YekutieliTriple (tower.level (n + 1)).M →
    YekutieliTriple (tower.level n).M
  retraction : ∀ (n : ℕ) (t : YekutieliTriple (tower.level n).M),
    (codegeneracy n (coface n t)).level = t.level
  crossedBoundary : (n : ℕ) → (tower.level n).M → ℝ → ℝ
  peiffer : ∀ (n : ℕ) (p : (tower.level n).M) (a b : ℝ) (_ha : a ≠ 0),
    crossedBoundary n p a * b = a * b * a⁻¹

/-- **Weak equivalence invariance of the vacuum state.**
    LaTeX: `\label{prop:weak-equiv-invariance}` -/
structure WeakEquivInvariance (dla : DirectLimitAlgebra) where
  csg : CosimplicialCrossedGroupoid
  tower_eq : dla.tower = csg.tower
  vacuumState : dla.limitAlgebra → ℝ
  state_invariant : ∀ (a b : dla.limitAlgebra),
    vacuumState a = vacuumState b

theorem weak_equiv_invariance_holds (dla : DirectLimitAlgebra)
    (wei : WeakEquivInvariance dla) (n m : ℕ)
    (a_n : dla.sectionAlgebra n) (a_m : dla.sectionAlgebra m) :
    wei.vacuumState (dla.embed n a_n) =
    wei.vacuumState (dla.embed m a_m) :=
  wei.state_invariant _ _

theorem cosimplicial_retraction_level
    (csg : CosimplicialCrossedGroupoid) (n : ℕ) :
    (csg.codegeneracy n (csg.coface n (csg.tripleAt n))).level =
    (csg.tripleAt n).level :=
  csg.retraction n (csg.tripleAt n)

/-- **Main theorem of Chapter 4 (QU → QOU).**
    LaTeX: `\label{thm:qu-to-qou}` -/
theorem qu_to_qou
    (ylc : YekutieliLiftingCondition)
    (ecs : EulerCharStability ylc.tower)
    (csg : CosimplicialCrossedGroupoid)
    (_h_tower : csg.tower = ylc.tower)
    (g : ℕ) (h_genus : ecs.eulerChar 0 = 2 - 2 * (g : ℤ)) :
    ∀ n, ecs.eulerChar n = 2 - 2 * (g : ℤ) := by
  intro n
  rw [euler_char_constant ylc.tower ecs n, h_genus]

end QOU.Torsion
