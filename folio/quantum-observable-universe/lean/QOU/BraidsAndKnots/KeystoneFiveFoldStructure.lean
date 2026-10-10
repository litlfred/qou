import QOU.BraidsAndKnots.S5SO3FiberAction

/-!
# The keystone five-fold: `1 + 1 + 1 + 2 = 5`, and the electron as the fifth element

The s5-so3 keystone (`bean s5bb`) rests on a **five-fold**: the W_λ index runs over the five A₅
irreps `{A, T₁, T₂, G, H}` (`A5Irrep`, dims 1,3,3,4,5). This file formalizes the *structure* of that
five — how the seven `S₅` partitions of 5 produce exactly five A₅ irreps — and records the resonance
with the confinement-SDP operator basis surfaced 2026-06-29.

**The decomposition.** Conjugation pairs the seven partitions of 5 into three conjugate pairs plus
one self-conjugate:

* `(5) ↔ (1⁵)`, `(4,1) ↔ (2,1³)`, `(3,2) ↔ (2,2,1)` — three pairs, each collapsing to ONE A₅ irrep
  (`A`, `G`, `H` resp., via `PartitionOf5.toA5Irrep`; the sign character is trivial on A₅);
* `(3,1,1)` self-conjugate — the **electron block** — which does NOT collapse but **splits** into the
  chirality pair `T₁ ⊕ T₂`.

So `toA5Irrep` (the partition restriction) hits only FOUR irreps `{A, T₁, G, H}`; the fifth, `T₂`, is
supplied *only* by the chirality split of the self-conjugate electron block. The count is

    1 (A) + 1 (G) + 1 (H) + 2 (T₁ ⊕ T₂ from the electron block)  =  5  =  #A₅ irreps.

**The electron resonance (2026-06-29).** This `4 + 1`-by-the-electron structure matches the nucleus
**confinement SDP** operator basis
([`computations/nucleus_operator_selection_sdp.py`](../../../../../computations/nucleus_operator_selection_sdp.py)):
the basis is the **six Bring generators** `(γ, σ₀, σ₁, L₊, L₋, e⁻)` (`χ(Bring) = −6`), of which **five
are strong-sector** (all but the electron `e⁻`). In both places the **electron is the distinguishing
fifth element**: the A₅ five-fold completes only through the electron-block chirality split `T₁ ⊕ T₂`,
and the strong confinement five is the six Bring generators minus the electron. This is the candidate
structural origin of the per-unit `5` in the binding residual `10A − 5 = 5(2A−1)` (a grouped-word near-match, not supported on the canonical interleaved word — bean `qou-zf9n`)
([`QOU/Mass/BindingResidualExponent.lean`](../Mass/BindingResidualExponent.lean), the `5` open there).
The identification of the binding `5` with this A₅ five-fold is **near-match tier** (not asserted as a
theorem here); what is proved below is the partition→irrep five-fold structure itself.

Base ring: pure finite combinatorics over the inductive `PartitionOf5` / `A5Irrep` (DecidableEq); no
archimedean construct, no fit.
-/

namespace QOU.BraidsAndKnots

/-- **The unique self-conjugate partition of 5 is `(3,1,1)`** — the electron block. Every other
partition of 5 is paired with a distinct conjugate. -/
theorem self_conjugate_iff_threeOneOne (p : PartitionOf5) :
    p.conjugate = p ↔ p = .threeOneOne := by
  cases p <;> decide

/-- **`toA5Irrep` misses `T₂`.** The partition→A₅-irrep restriction hits only four of the five irreps
(`{A, T₁, G, H}`); `T₂` is absent — it is the chirality partner of `T₁`, supplied only by the
self-conjugate `(3,1,1)` electron block's split `T₁ ⊕ T₂`. -/
theorem toA5Irrep_ne_T2 (p : PartitionOf5) : p.toA5Irrep ≠ A5Irrep.T₂ := by
  cases p <;> decide

/-- **`T₁` is reached only by the self-conjugate `(3,1,1)`.** The three conjugate *pairs* land on
`A`, `G`, `H`; `T₁` (and its chirality partner `T₂`) come exclusively from the electron block. -/
theorem toA5Irrep_eq_T1_iff_threeOneOne (p : PartitionOf5) :
    p.toA5Irrep = A5Irrep.T₁ ↔ p = .threeOneOne := by
  cases p <;> decide

/-- **The five-fold count `1 + 1 + 1 + 2 = 5`.** Three conjugate-pair irreps (`A`, `G`, `H`) plus the
electron-block chirality pair (`T₁ ⊕ T₂`) exhaust the five A₅ irreps. -/
theorem five_fold_count : A5Irrep.allList.length = 1 + 1 + 1 + 2 := by decide

/-- **Four partition-image irreps + one chirality completion.** The image of `toA5Irrep` over the
seven partitions has exactly four elements `{A, T₁, G, H}`; adjoining the missing chirality partner
`T₂` (from the electron block) completes the five. -/
theorem image_card_four_plus_T2 :
    (PartitionOf5.allList.map PartitionOf5.toA5Irrep).dedup.length = 4
    ∧ A5Irrep.T₂ ∉ PartitionOf5.allList.map PartitionOf5.toA5Irrep := by
  decide

end QOU.BraidsAndKnots
