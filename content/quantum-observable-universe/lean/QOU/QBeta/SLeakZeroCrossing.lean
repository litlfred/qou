/-
# c₃ bar-odd residual `S_leak` — the sign-flip zero-crossing prune

Sharpens the `SRigidityPrune` (`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`)
structural exclusion of the c₃ bar-odd carrier. That file proves the carrier is not
an anchor-*invariant* datum; this file adds the stronger constraint forced by the
**sign flip** of the residual across the two substrate anchors.

## The object (notation-collision guard, AGENTS.md §"attributes do not transfer")

`S_leak(q₀) := c₃(q₀) + Vol(4₁)` — the **bar-odd residual** of the Q_β `c₃`
coefficient after removing the bar-even amphichiral `−Vol(4₁)` (`4₁`) face. This is
`O(0.01)` and **sign-flips** across anchors. It is **distinct** from
`QOU.QBeta.SRigidity.S = Q_β/E₀`, which is `O(900)` and does **not** sign-flip
(`S_p/S_μ ≈ 1.024 > 0`). Do not conflate the two symbols.

Documented anchor values (50 dps, `computations/qbeta/qbeta_c3_barodd_sleak_probe.py`;
`Vol(4₁) = 2.02988321`):

| anchor | `c₃` | `S_leak = c₃ + Vol(4₁)` |
|--------|------|-------------------------|
| muon   | −2.02020024 | **+0.00968298** |
| proton | −2.06934258 | **−0.03945936** |

`S_leak(muon) > 0 > S_leak(proton)`: a genuine sign change, `S_p/S_μ ≈ −4.08`.

## The result (formalize-first; the anchor signs are the only empirical input)

* `sleak_zero_between_anchors` — any *continuous* `S_leak` reproducing the two
  anchor signs vanishes at some substrate `q*` strictly between the anchors, where
  `c₃ = −Vol(4₁)` **exactly** (the residual is purely bar-even — the amphichiral
  `4₁` face, with the `Φ_b` bar-odd decay face vanishing).
* `sign_definite_carrier_excluded` — **scope-(b) exclusion**: no continuous
  *nowhere-zero* (sign-definite) carrier on the anchor interval can realize
  `S_leak`, because `S_leak` changes sign. This strictly sharpens
  `SRigidityPrune`: the carrier is not merely non-constant/anchor-dependent, it
  must **cross zero** — so any `e^{g(q₀)}`, `|·|`, or sum-of-squares form is
  excluded, independently of the `dc₃/dq` magnitude obstruction.

The theorems are stated for a *generic* continuous `S_leak`/carrier; the two anchor
signs enter only as hypotheses (the empirical facts above), never as fitted
constants. This is the invariant that justifies the (b) exclusion, per the
anti-laundering "prove the invariant" discipline. No `c_k` wired.

Archimedean by necessity (ordering + continuity + IVT), so `ℝ` per §7c.

-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md
-/
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Topology.Instances.Real.Lemmas

namespace QOU.QBeta.SLeakZeroCrossing

open Set

/-- **Sign-flip ⇒ zero-crossing.** A continuous `S_leak` on the closed anchor
interval `[a, b]` with `S_leak a < 0 < S_leak b` vanishes at some `q*` strictly
inside `(a, b)`. Applied to the c₃ bar-odd residual (with `a` = proton anchor,
`b` = muon anchor, per the documented signs), this is the substrate `q*` where
`c₃ = −Vol(4₁)` exactly — the residual is purely bar-even. -/
theorem sleak_zero_between_anchors
    {Sleak : ℝ → ℝ} {a b : ℝ} (hab : a ≤ b)
    (hcont : ContinuousOn Sleak (Icc a b))
    (ha : Sleak a < 0) (hb : 0 < Sleak b) :
    ∃ q ∈ Ioo a b, Sleak q = 0 := by
  have hmem : (0 : ℝ) ∈ Ioo (Sleak a) (Sleak b) := ⟨ha, hb⟩
  obtain ⟨q, hq, hq0⟩ := intermediate_value_Ioo hab hcont hmem
  exact ⟨q, hq, hq0⟩

/-- **Scope-(b) exclusion of any sign-definite carrier.** No continuous,
*nowhere-zero* function `g` on the anchor interval `[a, b]` can agree with a carrier
that changes sign across the anchors (`g a < 0 < g b`): its intermediate zero
contradicts nonvanishing. This sharpens `SRigidityPrune`'s "not anchor-invariant"
to "must cross zero", excluding every sign-definite form (`exp∘·`, `|·|`,
sum-of-squares) regardless of magnitude. -/
theorem sign_definite_carrier_excluded
    {g : ℝ → ℝ} {a b : ℝ} (hab : a ≤ b)
    (hcont : ContinuousOn g (Icc a b))
    (hnz : ∀ q ∈ Icc a b, g q ≠ 0)
    (ha : g a < 0) (hb : 0 < g b) : False := by
  obtain ⟨q, hq, hq0⟩ := sleak_zero_between_anchors hab hcont ha hb
  exact hnz q (Ioo_subset_Icc_self hq) hq0

end QOU.QBeta.SLeakZeroCrossing
