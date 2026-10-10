import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

/-!
# Unified iterative (2,2) correction

Formalises prop:unified-iterative-correction:

The dedicated D-binding formula at A=2, the knot factor at A=3,4,
and the Wigner energy at Hecke level k≥5 are all specializations
of a single iterative mechanism — the per-step Wedderburn projection
of the NF transition onto the (2,2) ⊢ 4 partition, accumulated
from A=1.

The categorical Wigner energy scale is the q-hook product of (2,2):

  Δ_(2,2) = m_e · H_q((2,2)) = m_e · [3]_q · [2]_q²

Hook lengths of the 2×2 Young diagram: {3, 2, 2, 1}.  The product
[3]_q · [2]_q · [2]_q · [1]_q is exactly the (2,2) q-hook product.

## References

- Kerov 1996, q-hook walk on Young diagrams [kerov1996]
- Féray-Méliot 2010, q-Plancherel CLT [feray-meliot2012]
- Satuła et al. 1997, empirical Wigner energy [satula1997]
-/

namespace QOU.Archimedean.ConfinedKnotBinding.Unified

open scoped BigOperators

/-! ## §1  q-integers and q-hook product -/

variable {F : Type*} [Field F]

open scoped Classical in
/-- Quantum integer [n]_q = (q^n - q^(-n)) / (q - q^(-1)) over a field F. -/
noncomputable def qInt (q : F) (n : ℕ) : F :=
  if hq : q - q⁻¹ = 0 then n
  else (q ^ n - q⁻¹ ^ n) / (q - q⁻¹)

/-- **Bridge to the canonical singular-locus-guarded bracket.**

This site is *not* `qIntBalCl`: it guards the whole singular locus
`q − q⁻¹ = 0`, so it returns `n` at `q = −1` where the one-sided `qIntBalCl`
falls through to `0`.  `qIntBalClSing` is the canonical form with that guard;
the agreement is definitional. -/
theorem qInt_eq_canonical (q : F) (n : ℕ) :
    qInt q n = QOU.QInteger.qIntBalClSing q n := by
  unfold qInt QOU.QInteger.qIntBalClSing
  split_ifs with h
  · rfl
  · rfl

/-- The q-hook product of the (2,2) partition is [3]_q · [2]_q²,
    obtained from the four hook lengths {3, 2, 2, 1} of the 2×2
    Young diagram (since [1]_q = 1). -/
noncomputable def qHookProduct22 (q : F) : F :=
  qInt q 3 * (qInt q 2) ^ 2

/-- The (2,2) Wigner energy scale: Δ_(2,2) = m_e · H_q((2,2)). -/
noncomputable def Delta22 (q m_e : F) : F :=
  m_e * qHookProduct22 q

/-! ## §2  YSN representation of (2,2) — generator characters -/

/-- The (2,2) partition has dimension 2 (two standard Young
    tableaux: [[1,2],[3,4]] and [[1,3],[2,4]]). -/
def dim22 : ℕ := 2

/-- Character χ_{(2,2)}(σ_j) = q − q⁻¹ for every Hecke generator σ_j,
    j ∈ {1,2,3}.  This is a class-function fact: the eigenvalues of
    σ_1 and σ_3 are (q, −q⁻¹) (diagonal) and tr(σ_2) = sum of the
    two diagonal entries of the mixing matrix, which also equals h.

    For the purposes of the unified accumulator, only the value h
    matters; the proof reduces to algebra. -/
noncomputable def chi22_generator (q : F) : F := q - q⁻¹

/-! ## §3  Wedderburn-Artin weight of (2,2) -/

/-- [4]_q! = [1]·[2]·[3]·[4]. -/
noncomputable def qFact4 (q : F) : F :=
  qInt q 1 * qInt q 2 * qInt q 3 * qInt q 4

/-- The q-dimension of (2,2) is d_q = [4]_q! / H_q((2,2))
    = ([1]·[2]·[3]·[4]) / ([3]·[2]²)
    = [4] · [1] / [2] = [4] / [2] = q² + q⁻²  (when [2] ≠ 0). -/
noncomputable def dq22 (q : F) : F :=
  qFact4 q / qHookProduct22 q

/-- Wedderburn weight w_{(2,2)} = d_q² / [4]_q!. -/
noncomputable def w22 (q : F) : F := (dq22 q) ^ 2 / qFact4 q

/-! ## §4  Per-partition LP-dual shadow price + telescoping -/

/-- Per-partition weight (prop:mass-coefficient-shadow-price):
    y_λ = w_λ / d_λ − 1/[k]_q!.
    The constant 1/[k]_q! is the SMALLEST w_λ/d_λ across partitions
    of k, attained by the trivial 1-dim sym/alt reps with
    w = 1/[k]_q! and d = 1.

    Docstring corrected 2026-09-05 (owner ruling; PR #6752): it called
    that constant "the LP normalisation dual".  It is not.  The
    net-constraint dual of prop:operator-selection-lp is identically
    zero — the NF basis contains the identity, so the first Frobenius
    row is the objective vector and the optimum is 0 for every
    n_target (commit 6b7d2ec4a8; Lean `y_0_eq_zero_of_radical`).
    Nothing below changes: `shadowPrice` is and was the displayed
    closed form, and no theorem in this file depends on the reading. -/
noncomputable def shadowPrice (w_lambda d_lambda qfac_k : F) : F :=
  w_lambda / d_lambda - 1 / qfac_k

/-- Per-partition per-step contribution:
    ΔB_λ = m_e · H_q(λ) · y_λ · (L_k − L_{k−1}),
    the log-derivative of the running YSN trace in λ. -/
noncomputable def stepDeltaPartition
    (m_e H_q_lambda y_lambda Lk Lk_prev : F) : F :=
  m_e * H_q_lambda * y_lambda * (Lk - Lk_prev)

/-- (2,2) instance of the per-partition step delta, at the **historical**
    Wedderburn-weighted scale `m_e · H_q((2,2)) · w_(2,2)`.

    This is neither of the two scales `hecke_core_legacy` carries: the
    superseded `C_lambda_kerov_MeV = w_λ · y_λ · H_q · m_e` (`:535`) nor the
    live `C_lambda_resolvent_MeV = H_q · y_λ · ρ_λ(s_*) · m_e` (`:548`) — it
    omits `y_λ` entirely.  Kept because the telescoping theorems stated about
    it are true of it; for the scale the producer actually applies, and which
    `prop:unified-iterative-correction` now states, use `stepDeltaResolvent`
    below.  (Resolved 2026-09-12 under the owner's ruling *"resolve functionals
    ... what lean provable"*; audit
    `docs/audits/2026-09-12-uic-functional-resolution.md`.) -/
noncomputable def stepDelta (q m_e Lk Lk_prev : F) : F :=
  Delta22 q m_e * w22 q * (Lk - Lk_prev)

/-- The accumulator telescopes: Σ_{k=1..A} (L_k − L_{k-1}) = L_A − L_0. -/
theorem step_telescope {A : ℕ} (L : ℕ → F) :
    (Finset.range A).sum (fun k => L (k + 1) - L k) = L A - L 0 := by
  induction A with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    ring

/-- Total unified correction: B_unified = Δ_(2,2) · w_(2,2) · (L_A − ln 2),
    where L_0 = ln |tr I| = ln dim((2,2)) = ln 2. -/
theorem unified_telescope {A : ℕ} (q m_e : F) (L : ℕ → F)
    (hL0 : L 0 = (2 : F)) :
    (Finset.range A).sum (fun k => stepDelta q m_e (L (k+1)) (L k))
    = Delta22 q m_e * w22 q * (L A - 2) := by
  unfold stepDelta
  rw [← Finset.mul_sum, step_telescope, hL0]

/-! ## §5  Categorical scale identity -/

/-- The (2,2) q-hook product equals [3]_q · [2]_q² (the hook lengths
    of the 2×2 Young diagram are {3, 2, 2, 1} — and [1]_q = 1). -/
theorem qHookProduct22_eq (q : F) :
    qHookProduct22 q = qInt q 3 * (qInt q 2) ^ 2 := rfl

/-- The categorical Wigner scale Δ_(2,2) = m_e · [3]_q · [2]_q². -/
theorem Delta22_eq (q m_e : F) :
    Delta22 q m_e = m_e * qInt q 3 * (qInt q 2) ^ 2 := by
  unfold Delta22 qHookProduct22
  ring

/-- Per-partition telescoping: total contribution of a single partition λ
    is m_e · H_q(λ) · y_λ · (L_A − L_0).  This holds for every λ, so the
    total unified correction is the sum over all enumerated partitions. -/
theorem unified_telescope_partition {A : ℕ}
    (m_e H_q_lambda y_lambda : F) (L : ℕ → F) (L0 : F)
    (hL0 : L 0 = L0) :
    (Finset.range A).sum
      (fun k => stepDeltaPartition m_e H_q_lambda y_lambda (L (k+1)) (L k))
    = m_e * H_q_lambda * y_lambda * (L A - L0) := by
  unfold stepDeltaPartition
  rw [← Finset.mul_sum, step_telescope, hL0]

/-! ## §6  The resolvent-damped scale — the live production convention

Added 2026-09-12 under the owner's ruling *"resolve functionals ... what lean
provable"*.  `prop:unified-iterative-correction` displayed
`m_e · H_q(λ) · u_λ` with no resolvent while the producer has applied
`m_e · H_q(λ) · y_λ · ρ_λ(s_*)` since the q-heat-spectrum derivation replaced
the ad-hoc Kerov multiplier (`hecke_core_legacy.py:545-548`).  Deleting `ρ_λ`
moves the accumulator's total by 4.12× at `A = 2` and 9.87× at `A = 4`
(`computations/probes/uic_functional_resolution_probe.py`), so the omission was
a factor, not a rounding.

The **gate** — the producer's former Pass-2 restriction to `tr M_λ ≤ 0` — is
deliberately NOT asserted here.  It was underived: see
`QOU.MassTheory.UICFunctionalSelection`, whose `uicGated_cs_eq` shows that
genuine complementary slackness collapses the functional to a constant carrying
no information about the atom.  The restriction was removed from the producer on
2026-09-12 (owner ruling, bean `qou-21oc`), so this file's unrestricted reading
and `hecke_core_legacy.unified_iterative_correction` now agree. -/

/-- The `q`-resolvent on the `λ`-block: `ρ_λ(s) = 1 / (μ_λ + s)`, with `μ_λ` the
    Jucys–Murphy `q`-Casimir eigenvalue.  The block-diagonal scalar of
    `def:q-resolvent`'s `R_q(s) = (s + Δ̂_q)⁻¹`. -/
noncomputable def qResolvent (mu s : F) : F := 1 / (mu + s)

/-- Per-partition per-step contribution at the **live** scale:
    `ΔB_λ = m_e · H_q(λ) · y_λ · ρ_λ(s_*) · (L_k − L_{k−1})`. -/
noncomputable def stepDeltaResolvent
    (m_e H_q_lambda y_lambda mu s Lk Lk_prev : F) : F :=
  m_e * H_q_lambda * y_lambda * qResolvent mu s * (Lk - Lk_prev)

/-- **The resolvent occupies the weight slot.**

The live scale is the general per-partition shape with `y_λ` replaced by
`y_λ · ρ_λ(s_*)`, so every structural result already proved about
`stepDeltaPartition` transfers verbatim.  This is why adding the omitted factor
to the content block is a restatement rather than a new derivation. -/
theorem stepDeltaResolvent_eq_partition
    (m_e H_q_lambda y_lambda mu s Lk Lk_prev : F) :
    stepDeltaResolvent m_e H_q_lambda y_lambda mu s Lk Lk_prev
      = stepDeltaPartition m_e H_q_lambda (y_lambda * qResolvent mu s)
          Lk Lk_prev := by
  unfold stepDeltaResolvent stepDeltaPartition
  ring

/-- **The resolvent-damped accumulator telescopes.**

The per-partition total is `m_e · H_q(λ) · y_λ · ρ_λ(s_*) · (L_A − ln d_λ)` —
exactly the closed form `prop:unified-iterative-correction` now displays, and
the identity that lets the producer's total be reconstructed from the final
trace alone (verified to rel 2.7e-63 in the probe). -/
theorem unified_telescope_resolvent {A : ℕ}
    (m_e H_q_lambda y_lambda mu s : F) (L : ℕ → F) (L0 : F)
    (hL0 : L 0 = L0) :
    (Finset.range A).sum
      (fun k => stepDeltaResolvent m_e H_q_lambda y_lambda mu s
                  (L (k + 1)) (L k))
    = m_e * H_q_lambda * y_lambda * qResolvent mu s * (L A - L0) := by
  simp only [stepDeltaResolvent_eq_partition]
  rw [unified_telescope_partition m_e H_q_lambda (y_lambda * qResolvent mu s)
        L L0 hL0]
  ring

/-- Convenience name matching the proposition label.
    Single-partition (2,2) instance at the historical `w_(2,2)` scale; see
    `stepDelta`'s docstring and `unified_telescope_resolvent` for the live one. -/
theorem unified_iterative_correction {A : ℕ} (q m_e : F) (L : ℕ → F)
    (hL0 : L 0 = (2 : F)) :
    (Finset.range A).sum (fun k => stepDelta q m_e (L (k+1)) (L k))
    = Delta22 q m_e * w22 q * (L A - 2) :=
  unified_telescope q m_e L hL0

/-! ## Axiom audit -/

#print axioms step_telescope
#print axioms unified_telescope
#print axioms unified_telescope_partition
#print axioms stepDeltaResolvent_eq_partition
#print axioms unified_telescope_resolvent
#print axioms unified_iterative_correction

end QOU.Archimedean.ConfinedKnotBinding.Unified
