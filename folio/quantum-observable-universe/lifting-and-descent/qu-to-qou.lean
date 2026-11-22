import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Order.Basic


/-!
# QOU.QuToQou — Main theorem: quantum universe → QOU

A quantum universe with observability and the Yekutieli lifting condition
is a quantum observable universe with five structural properties:
1. Descent terminates (bounded by Krull dimension).
2. First obstruction = Euler class.
3. Perpetual obstruction (if κ₀ is non-torsion).
4. Branch point formula (Riemann–Hurwitz).
5. Terminal fiber data (involution at branch points).

## References

- [yekutieli2010] Central Extensions of Gerbes
- [leitner2026] §3 Theorem: QU to QOU
-/

namespace QOU

/-- **Descent tower data**: the geometric descent terminates in finitely
    many steps, bounded by the Krull dimension. -/
structure DescentTower where
  /-- Krull dimension of the centre Z(End_C(A)). -/
  krullDim : ℕ
  /-- The dimension at step n of the descent. -/
  dimAtStep : ℕ → ℕ
  /-- Initial dimension equals Krull dimension. -/
  initial_dim : dimAtStep 0 = krullDim
  /-- Each step strictly reduces dimension (observability ⇒ faithful action). -/
  strict_descent : ∀ n, dimAtStep n > 0 → dimAtStep (n + 1) < dimAtStep n
  /-- Termination: dimension reaches 0 in at most krullDim steps. -/
  terminates : dimAtStep krullDim = 0

/-- **Branch point data** from the Riemann–Hurwitz formula. -/
structure BranchData where
  /-- Degree of the branched covering π : S → P(V). -/
  degree : ℕ
  /-- Euler characteristic χ(A) = tr(id_A). -/
  eulerChar : ℤ
  /-- Number of branch points. -/
  numBranchPoints : ℕ
  /-- Total ramification R_tot = 2d + |χ(A)| (Riemann–Hurwitz). -/
  totalRamification : ℕ
  /-- The Riemann–Hurwitz identity. -/
  riemann_hurwitz : totalRamification = 2 * degree + eulerChar.natAbs

/-- **Terminal fiber data** at a branch point. -/
structure TerminalFiber where
  /-- The branch point index. -/
  branchIndex : ℕ
  /-- The Krull dimension at the branch point is 0 (discrete/Artinian).
      Encoded: the dimension of the descent tower at this point. -/
  krullDimAtPoint : ℕ
  /-- The Krull dimension is 0 at the branch point. -/
  krull_zero : krullDimAtPoint = 0
  /-- The involution σ : P(V) ↪ Ad(A) exists at this fiber.
      Encoded: the involution is an involution (σ² = id). -/
  involution_exists : ∃ (σ : ℤ → ℤ), ∀ x, σ (σ x) = x

/-- The **main theorem**: packaging all five structural properties of a QOU.

    Given a quantum universe (C, A, ω) with observability and the Yekutieli
    lifting condition, it is a QOU with descent, obstruction, and fiber data.

    LaTeX: `\label{thm:qu-to-qou}`
    Ref: [leitner2026] §3 -/
-- Ref: [leitner2026] §3
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
structure QuToQou where
  /-- (1) The descent tower terminates. -/
  descent : DescentTower
  /-- (2) The first obstruction κ₀ is the Euler class. -/
  kappa_zero_obstruction : ℤ  -- κ₀ in H²(S, B), identified with Euler class
  /-- The Euler characteristic χ(A). -/
  eulerChar : ℤ
  /-- κ₀ maps to χ(A) under the trace. -/
  trace_map : kappa_zero_obstruction = eulerChar
  /-- (3) Kummer persistence (degree condition): the level-`n` obstruction
      vanishes exactly when `n` divides `χ(A)`. Restated 2026-11-15 (owner
      decision, PR #7747, bean `qou-lx8f`); the former field
      `perpetual : κ₀ ≠ 0 → ∀ n, κₙ ≠ 0` is false on Bring's surface, where
      `κₙ = 0` for `n ∈ {1, 2, 3, 6}`. -/
  kappa : ℕ → ℤ
  kappa_at_zero : kappa 0 = kappa_zero_obstruction
  kummer_persistence : ∀ n, 0 < n → (kappa n = 0 ↔ (n : ℤ) ∣ eulerChar)
  /-- (4) Branch point formula (Riemann–Hurwitz). -/
  branchData : BranchData
  /-- (5) Terminal fiber data at each branch point. -/
  terminalFibers : Fin branchData.numBranchPoints → TerminalFiber

/-- The five structural properties package into a QOU: given descent,
    obstruction, branch and terminal-fibre data satisfying their coherences,
    they assemble into a `QuToQou`, and the assembled structure carries the
    supplied descent and branch data. This formalises the *packaging* of the
    QU→QOU theorem (Properties 1–5); the derivation of these ingredients from
    a quantum universe with observability and the quantum lifting condition is
    the narrative content of §3. -/
-- Ref: [leitner2026] §3
theorem qu_to_qou_exists
    (descent : DescentTower) (branchData : BranchData)
    (kappa0 eulerChar : ℤ) (htrace : kappa0 = eulerChar)
    (kappa : ℕ → ℤ) (hkappa0 : kappa 0 = kappa0)
    (hkummer : ∀ n, 0 < n → (kappa n = 0 ↔ (n : ℤ) ∣ eulerChar))
    (terminalFibers : Fin branchData.numBranchPoints → TerminalFiber) :
    ∃ X : QuToQou, X.descent = descent ∧ X.branchData = branchData :=
  ⟨{ descent := descent
     kappa_zero_obstruction := kappa0
     eulerChar := eulerChar
     trace_map := htrace
     kappa := kappa
     kappa_at_zero := hkappa0
     kummer_persistence := hkummer
     branchData := branchData
     terminalFibers := terminalFibers }, rfl, rfl⟩

/-- Property (1): the geometric descent terminates. -/
theorem qu_to_qou_descent_terminates (X : QuToQou) :
    X.descent.dimAtStep X.descent.krullDim = 0 :=
  X.descent.terminates

/-- Property (2): the first obstruction κ₀ equals the Euler class χ(A). -/
theorem qu_to_qou_first_obstruction_eq_euler (X : QuToQou) :
    X.kappa_zero_obstruction = X.eulerChar :=
  X.trace_map

/-- Property (3): the level-`n` obstruction persists exactly when `n ∤ χ(A)`. -/
theorem qu_to_qou_obstruction_persists_iff (X : QuToQou) (n : ℕ) (hn : 0 < n) :
    X.kappa n ≠ 0 ↔ ¬ (n : ℤ) ∣ X.eulerChar :=
  not_congr (X.kummer_persistence n hn)

/-- On a surface with `χ(A) = -6`, the obstruction vanishes at levels `1, 2, 3, 6`
    and persists at every level `n` coprime to `6`: it is not perpetual. -/
theorem qu_to_qou_chi_neg_six (X : QuToQou) (hχ : X.eulerChar = -6) :
    X.kappa 6 = 0 ∧ ∀ n, 0 < n → Nat.Coprime n 6 → n ≠ 1 → X.kappa n ≠ 0 := by
  refine ⟨(X.kummer_persistence 6 (by norm_num)).mpr (by rw [hχ]; norm_num), ?_⟩
  intro n hn hcop hn1 hzero
  have hdvd := (X.kummer_persistence n hn).mp hzero
  rw [hχ] at hdvd
  have h6 : (n : ℤ) ∣ 6 := by
    have := hdvd.neg_right; simpa using this
  have h6' : n ∣ 6 := by exact_mod_cast h6
  exact hn1 (Nat.Coprime.eq_one_of_dvd hcop h6')

/-- Property (4): the Riemann–Hurwitz branch-point identity. -/
theorem qu_to_qou_riemann_hurwitz (X : QuToQou) :
    X.branchData.totalRamification
      = 2 * X.branchData.degree + X.branchData.eulerChar.natAbs :=
  X.branchData.riemann_hurwitz

end QOU
