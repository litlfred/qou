import QOU.BraidKnot.KeystoneG2Gate
import QOU.BraidKnot.WLambdaDefectSubleadingD
import QOU.BraidKnot.WLambdaDefectLadderE

/-!
# Keystone G2 — the full heat-kernel **ladder** gate (C / D / E)

Strengthens the single-order G2 gate (`KeystoneG2Gate`: the 2nd heat-kernel coefficient `a₂(n)` must
equal the proved cubic `n144C`) to the **full proved ladder**: a candidate equivariant index
reproduces the `W_λ` defect only if its cleared heat-kernel coefficient at *every* derived order `k`
equals the proved value —

| order `k` | h-power | cleared coefficient | clearing factor |
|---|---|---|---|
| 1 | h² | `n144C` (= 144·C) | `1·144¹` |
| 2 | h⁴ | `n1036800D` (= 1036800·D) | `50·144²` |
| 3 | h⁶ | `n21946982400E` (= 21946982400·E) | `7350·144³` |

The teeth: the gate is **unique** on the derived orders, **subsumes** the single-order G2 gate, and
forces the universal **`n(n−1)` vanishing at every order** (every heat-kernel coefficient vanishes at
the single box, since `Z(0) = Z(1) = 1` exactly). The clearing factors follow the proved `m_k·144^k`
ladder (`WLambdaDefect.denom_ladder`, `denom_E`).

Base ring `ℤ`; no `q₀`, no fit. Distinct from the sibling z2bn target `a_D = lw` (#2800): this is
**target-1**, the defect-cubic ladder, not the prolongation period.
-/

namespace QOU.BraidKnot.KeystoneG2Gate

open QOU.BraidKnot.WLambdaDefect

/-- The canonical cleared heat-kernel coefficient at order `k` (the `m_k·144^k`-cleared `h^{2k}`
coefficient): `k=1 → n144C`, `k=2 → n1036800D`, `k=3 → n21946982400E`; higher orders are not yet
derived (placeholder `0`). -/
def canonicalLadder : ℕ → ℤ → ℤ
  | 1 => n144C
  | 2 => n1036800D
  | 3 => n21946982400E
  | _ => fun _ => 0

/-- A candidate index's full cleared heat-kernel ladder — its cleared coefficient at each order. -/
structure HeatKernelLadderCandidate where
  /-- The cleared coefficient at order `k` (the `m_k·144^k`-cleared `h^{2k}` coefficient). -/
  coeff : ℕ → ℤ → ℤ

/-- **The full-ladder gate.** A candidate passes iff its cleared coefficient matches the proved
ladder at every derived order `k ∈ {1,2,3}`. -/
def PassesLadderGate (I : HeatKernelLadderCandidate) : Prop :=
  ∀ k, 1 ≤ k → k ≤ 3 → ∀ n, I.coeff k n = canonicalLadder k n

/-- **Uniqueness on the derived orders.** Two indices that pass the ladder gate agree at every
derived order — the gate leaves no free coefficient. -/
theorem ladderGate_unique {I J : HeatKernelLadderCandidate}
    (hI : PassesLadderGate I) (hJ : PassesLadderGate J) :
    ∀ k, 1 ≤ k → k ≤ 3 → I.coeff k = J.coeff k := by
  intro k hk1 hk3; funext n; rw [hI k hk1 hk3, hJ k hk1 hk3]

/-- **The full ladder subsumes the single-order G2 gate.** Passing the ladder gate ⇒ passing the
`KeystoneG2Gate` defect gate (the `C(n)` cubic at order `h²`) — so all of G2's teeth (the n=7 sign
flip, the cubic) apply to any ladder-passing index. -/
theorem ladderGate_subsumes_G2 {I : HeatKernelLadderCandidate} (hI : PassesLadderGate I) :
    PassesDefectGate ⟨I.coeff 1⟩ := by
  intro n
  show I.coeff 1 n = n144C n
  exact hI 1 (by norm_num) (by norm_num) n

/-- **Universal `n(n−1)` vanishing.** Any index passing the ladder gate has every derived-order
coefficient vanishing at `n = 0` and `n = 1` — each heat-kernel coefficient carries the `n(n−1)`
factor (since the partition function is exactly `Z(0) = Z(1) = 1`, no defect at the single box). -/
theorem ladderGate_forces_vanishing {I : HeatKernelLadderCandidate} (hI : PassesLadderGate I)
    {k : ℕ} (hk1 : 1 ≤ k) (hk3 : k ≤ 3) :
    I.coeff k 0 = 0 ∧ I.coeff k 1 = 0 := by
  rw [hI k hk1 hk3, hI k hk1 hk3]
  interval_cases k
  · exact ⟨by decide, by decide⟩
  · exact ⟨n1036800D_vanishes.1, n1036800D_vanishes.2⟩
  · exact ⟨n21946982400E_vanishes.1, n21946982400E_vanishes.2⟩

/-- **The clearing-factor ladder** `m_k·144^k` (`m₁=1, m₂=50, m₃=7350`): the proved structural law the
gate's cleared coefficients follow (cf. `WLambdaDefect.denom_ladder`, `denom_E`). The recurrence of
`144^k` is the keystone's Identity-I `144` raised to the order. -/
theorem ladder_clearing_factors :
    (144 : ℤ) = 1 * 144 ^ 1 ∧ (1036800 : ℤ) = 50 * 144 ^ 2 ∧
      (21946982400 : ℤ) = 7350 * 144 ^ 3 := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- The framework's own proved ladder, packaged as a candidate. -/
def canonicalLadderCandidate : HeatKernelLadderCandidate := ⟨canonicalLadder⟩

/-- **The ladder gate is satisfiable (non-vacuous).** The proved ladder is itself a passing
candidate, so the strengthened specification is consistent. The open question (G1) is whether a
*geometric* (Seifert–CS) index realizes the whole heat-kernel ladder. -/
theorem canonicalLadderCandidate_passes : PassesLadderGate canonicalLadderCandidate :=
  fun _ _ _ _ => rfl

end QOU.BraidKnot.KeystoneG2Gate
