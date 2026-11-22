/-
# c₃ bar-odd residual `S_leak` — the sign-flip zero-crossing prune

Sharpens the `SRigidityPrune` (`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`)
structural exclusion of the c₃ bar-odd carrier. That file proves the carrier is not
an anchor-*invariant* datum; this file adds the stronger constraint forced by the
**sign flip** of the residual across the two substrate anchors.

## The object (notation-collision guard, AGENTS.md §"attributes do not transfer")

`S_leak(q₀) := c₃(q₀) + Vol(4₁)` — a **definition**, not a derived decomposition
(AGENTS.md §"Defined residual ≠ derived decomposition", 2026-08-08). Reading it as
"the bar-odd residual after removing the bar-even amphichiral `−Vol(4₁)` face"
asserts `c₃^even = −Vol(4₁)` exactly, which is **not** established:

* the bar-split is **not empirically accessible** here — `c₃^even(q) =
  (c₃(q) + c₃(1/q))/2` needs `c₃` at `q ≈ 0.901`, and both anchors sit at
  `q ≈ 1.10998`;
* the sign flip is **offset-generic** — it holds for any constant in a window of
  width `0.0491` (`Vol(4₁)`, `2+1/36`, `63/31`, … all flip), so it is not evidence
  about `Vol(4₁)` (`computations/qbeta/sleak_offset_genericity_check.py`);
* what **is** established is *motivation, not identity*: the Φ_b state-integral
  saddle gives `Im 𝔙 = 0` at the real substrate meridian and a volume deficit
  `0.0094 ≈ |S_leak(muon)| = 0.00968` — fit-free and anchor-blind, but a **~2.9%
  scale agreement**, with the exact normalisation open and
  `conj:im-q-physical-role` still a conjecture (PR #3654; KC21).

The theorems below are unaffected: each is stated for a **generic** function with
the anchor signs as **hypotheses**, so none depends on the identification.

`S_leak` is `O(0.01)` and **sign-flips** across anchors. It is **distinct** from
`QOU.QBeta.SRigidity.S = Q_β/E₀`, which is `O(900)` and does **not** sign-flip
(`S_p/S_μ ≈ 1.024 > 0`). Do not conflate the two symbols. Note also that `S`
itself is *defined* as `a₁/κ_(2,1)` with `a₁ = −c₃`, so it too is a
reparametrisation of `c₃` and carries no independent information about the split.

-- Ref: [leitner2026] docs/audits/2026-08-08-c3-even-vol41-contradicts-canonical-split.md

Documented anchor values (50 dps, `computations/qbeta/qbeta_c3_barodd_sleak_probe.py`;
`Vol(4₁) = 2.02988321`):

| anchor | `c₃` | `S_leak = c₃ + Vol(4₁)` |
|--------|------|-------------------------|
| muon (CODATA 2022) | −2.01986031 | **+0.01002290** |
| muon (CODATA 2018, superseded) | −2.02020024 | +0.00968298 |
| proton | −2.06934258 | **−0.03945936** |

> **🛑 THE MUON ROW IS ANCHOR-QUALIFIED, AND THAT IS LOAD-BEARING (2026-08-31,
> beans `qou-cds1` / `qou-t39x`).** There is no single "muon `c₃`": the
> extractor returns a different value at each muon pin in use and they differ
> in the *fourth* significant figure. `fca08de7d2` (2026-08-22, owner ruling)
> moved the pin to CODATA 2022; the `−2.02020024` this table carried is the
> CODATA-2018 extraction. The lever is `1/u³ ≈ 1.6×10⁶`, so a **1.451 ppb**
> step on `m_μ/m_e` is `1.7×10⁻⁴` on `c₃` — "far below the 11.5 ppb μ–p
> tension" does not imply below the resolution of what divides by `u³`.
>
> **Consequence for KC21, stated here because this table is where it is read
> off:** the Φ_b state-integral volume deficit `0.0094` matches `|S_leak(muon)|`
> to **6.63 %** at the live pin, not the **3.01 %** the registry quotes. The
> deficit is anchor-blind to sub-ppm, so all of that movement is on the `|S|`
> side — the quoted margin was never a property of the saddle.
>
> None of the theorems below move: they are generic in `S_leak` and
> hypothesis-carrying, and the sign flip `S_leak(muon) > 0 > S_leak(proton)`
> holds at every pin in the table.

`S_leak(muon) > 0 > S_leak(proton)`
> **🛑 CONVENTION-C SCOPE (added 2026-08-31).** The `c₃` values quoted here —
> `−2.01986031` (muon, CODATA-2022 pin) and `−2.06934258` (proton) — are
> **C-frame extractions**.
> Owner ruling 2026-08-09 excised convention C at the `z` level (production uses
> `z_D = q³/(q²+1)`), but the `c_k` **ladder** has not been re-derived under D:
> bean `qou-cds1` states it "must be re-derived, not re-evaluated", and the
> `c₃ ≈ −974` obtained by feeding `z_D` to the current extractor is a
> sensitivity measurement, **not** a proposed value. So every value-level `c₃`
> fact below is C-conditional and moves if `qou-cds1` lands.
>
> **No theorem in this file depends on it** — the values appear in this
> docstring only, verified by AST scan in
> `computations/deltalambda/wlambda_binding_c_frame_conditionality_audit.py`.: a genuine sign change, `S_p/S_μ ≈ −4.08`.

## ⚠ APPLICABILITY (2026-08-08): the anchor signs are NOT resolved by the data

The theorems below are correct and unaffected — they are *conditional* on the two
anchor signs. But that hypothesis is **not established**, and the table above
overstates what is known. Two corrections:

1. **"50 dps" above is wrong.** The upstream keystone witness carries the `c₃`
   values as **12**-significant-digit strings, and `qbeta_c3_barodd_sleak_probe.py`
   computed in float64 until it was ported. It now emits
   `computations/qbeta/qbeta-c3-barodd-sleak.witness.json` as the canonical
   source; read the values there rather than copying this table.

2. **`c₃` is an inversion, and the inversion amplifies.** It is not measured:
   `c₃ = (Q_codata / Q_N2 − 1) / u³` with `u = b·ℏ_q² ≈ 8.5e−3`
   (`qbeta_utils.c3_target_at`), so `1/u³ ≈ 1.6e6` multiplies the CAL-3 input
   error. `Q_β(n) = 0.78233341(61) MeV` (PDG 2024) therefore gives

   ```
   S_leak(muon)   =  +0.00968298 ± 1.26      (uncertainty 130× the value)
   S_leak(proton) =  −0.03945936 ± 1.26      (uncertainty  32× the value)
   ```

   The same `Q_β(n)` enters at both anchors, so the error is **fully correlated**
   and cancels in the difference but not in the values:

   ```
   S_leak(muon) − S_leak(proton) = 0.0491423421 ± 7.6e−7   (rel 1.5e−5)
   ```

   **So the 2.43% SWING is a real, resolved feature — and the SIGN FLIP is not.**
   At `Q_β + 1σ` both `S_leak` are positive; at `Q_β − 1σ` both are negative. The
   zero crossing between the anchors is a property of the central value, not of
   the data.

Consequence for this file: `sleak_zero_between_anchors` and
`sign_definite_carrier_excluded` stay *proved*, and their scope-(b) exclusion of
sign-definite carriers stays *valid as an implication*. What is open is whether
the antecedent holds. Do not cite either theorem as excluding a carrier until the
anchor signs are established by something other than the central values —
tightening `Q_β(n)`, or a determination of `c₃` that does not divide by `u³`.

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

-- Ref: [leitner2026] docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md
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

/-- Reversed-sign zero-crossing: a continuous `Sleak` on `[a, b]` with
`0 < Sleak a` and `Sleak b < 0` also vanishes strictly inside `(a, b)`. -/
theorem sleak_zero_between_anchors_rev
    {Sleak : ℝ → ℝ} {a b : ℝ} (hab : a ≤ b)
    (hcont : ContinuousOn Sleak (Icc a b))
    (ha : 0 < Sleak a) (hb : Sleak b < 0) :
    ∃ q ∈ Ioo a b, Sleak q = 0 := by
  obtain ⟨q, hq, hq0⟩ :=
    sleak_zero_between_anchors hab hcont.neg (neg_lt_zero.mpr ha) (neg_pos.mpr hb)
  exact ⟨q, hq, neg_eq_zero.mp hq0⟩

end QOU.QBeta.SLeakZeroCrossing
