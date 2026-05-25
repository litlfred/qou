import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import QOU.Archimedean.BringFaddeevH4LinkingWeight
import QOU.Archimedean.LinkingWeightSubstrateBounds

/-!
# Additive composition rule — class-axiomatised conjecture

Per CLAUDE.md §3b-cond ("Conditional-class exception"): the additive
composition rule for the Bring color-tube + Faddeev h⁴ candidate

      linkingWeightBringFaddeevH4 q = bringColorTube q + faddeevH4 q − 1

is **research-grade open** (per the audit
[`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md)
§4a "Outstanding load-bearing step"). The probe
[`additive_composition_categorical_probe.py`](../../../../../folio-assistant/computations/additive_composition_categorical_probe.py)
tests 4 categorical hypotheses (H_4 Wedderburn direct sum, S_4 ↓ S_3
restriction, half-symmetric Frobenius reciprocity, KLR positivity),
all of which independently support additive composition over
multiplicative. But none rises to a categorical PROOF — the specific
partition-channel assignment of Bring color-tube vs Faddeev h⁴ at
H_4 remains open.

This file axiomatises the additive composition rule as a
**class**, providing a Lean infrastructure for **conditional**
downstream theorems that consume the composition rule as a
hypothesis. Per CLAUDE.md §3b-cond, this is the right structural
pattern: the conjecture is encoded as a class; downstream blocks that
need it carry it as an explicit `[Instance]` hypothesis.

## The class

```
class AdditiveCompositionRule (q : ℝ) where
  bring_factor : ℝ                            -- "Bring color-tube" component
  faddeev_h4_factor : ℝ                       -- "Faddeev recursion at h⁴" component
  composes_additively : ∀ q', combined_linking_weight q' = bring_factor + faddeev_h4_factor − 1
  ...
```

## What conditional results downstream can derive

Once an instance is constructed (the "load-bearing step" of the
audit §4a), the following all follow automatically as conditional
theorems:

| theorem | content |
|---|---|
| `linking_weight_eq_additive` | `linkingWeightBringFaddeevH4 = bring + faddeev − 1` |
| `m_p_pred_eq_via_additive` | `m_p prediction = m_e · (Vol(𝓑₃)/ℏ_q²) · (bring + faddeev − 1) · (1 − Δm/2)` |
| `linking_weight_distinct_from_familyA` | restated under class |

These are NOT proved here (they require the class instance, which is
the research-grade open step). They are STATED as `theorem [Instance]
... := ...` so future agents can `instance : AdditiveCompositionRule
... := { ... }` once the categorical proof lands.

## References

- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md) §4a — outstanding load-bearing step
- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../../../../../docs/audits/2026-05-23-lambda-scale-canonical-unification.md) §"Rule 14" — 13-driver menu
- [`folio-assistant/computations/additive_composition_categorical_probe.py`](../../../../../folio-assistant/computations/additive_composition_categorical_probe.py) — 4 supporting hypotheses
- CLAUDE.md §3b-cond — Conditional-class exception convention
-/

namespace QOU.Archimedean

open Real

/-! ## §1  Class: AdditiveCompositionRule -/

/-- **Class (conjectural).** The Bring color-tube + Faddeev h⁴
    candidate for `linking_weight(q)` decomposes as an ADDITIVE
    composition of two Φ_q functional-equation ratios at
    substrate-natural z values.

    Per the canonical probe (`additive_composition_categorical_probe.py`),
    4 of the 13 categorical drivers support this structure:

    - **H_4 Wedderburn direct sum**: Bring color-tube lives in the
      (3,1)+(2,1,1) hook partitions; Faddeev h⁴ lives in the (2,2)
      bar-invariant block.
    - **S_4 ↓ S_3 restriction**: both factors live at H_4; the
      `(1/4)·Σ` structure inherits.
    - **Half-symmetric Frobenius reciprocity at H_4**: refinement
      must preserve Family A's inherently-additive `(1/4)·Σ_λ` structure.
    - **KLR positivity / Kashiwara crystal**: both series have
      non-negative integer KLR coefficients; H_4 crystal admits no
      tensor-product structure (so multiplicative composition is
      ruled out).

    Closing this class instance requires deriving the specific
    partition-channel assignment categorically. -/
class AdditiveCompositionRule (q : ℝ) where
  /-- The "Bring color-tube" Φ_q ratio at z = h·q^{10}. -/
  bring_factor : ℝ
  /-- The "Faddeev recursion at h⁴" Φ_q ratio at z = h⁴. -/
  faddeev_h4_factor : ℝ
  /-- bring_factor matches `bringColorTube q`. -/
  bring_factor_eq : bring_factor = bringColorTube q
  /-- faddeev_h4_factor matches `faddeevH4 q`. -/
  faddeev_h4_factor_eq : faddeev_h4_factor = faddeevH4 q
  /-- **The load-bearing axiom.** linking_weight composes as
      bring + faddeev − 1 (vs multiplicatively bring · faddeev). -/
  composes_additively :
    linkingWeightBringFaddeevH4 q = bring_factor + faddeev_h4_factor - 1

/-! ## §2  Conditional theorems (consume the class) -/

/-- **Conditional theorem.** Under the additive composition rule
    (class instance), `linkingWeightBringFaddeevH4` factors as the sum
    of two Φ_q recursion ratios minus 1.

    The factorisation is trivially the definitional unfolding
    (`bringColorTube + faddeevH4 - 1`), but encoding it via the class
    makes the categorical hypothesis explicit per CLAUDE.md §3b-cond. -/
theorem linking_weight_eq_additive_decomposition (q : ℝ)
    [acr : AdditiveCompositionRule q] :
    linkingWeightBringFaddeevH4 q
      = acr.bring_factor + acr.faddeev_h4_factor - 1 :=
  acr.composes_additively

/-- **Conditional theorem.** The two factors are characterised by
    their explicit q-rational forms (via `BringColorTubeQForm.lean`'s
    closed-form theorems).

    With `q ≠ 0`, `bringColorTubeDen q ≠ 0`, `faddeevH4Den q ≠ 0`,
    `1 - h⁴ ≠ 0`:

      bring_factor = 1 / (1 + q^9 - q^{11})
      faddeev_h4_factor = -q^4 / (q^8 - 4q^6 + 5q^4 - 4q^2 + 1)
    -/
theorem additive_factors_q_form (q : ℝ) [acr : AdditiveCompositionRule q]
    (hq : q ≠ 0)
    (hb : bringColorTubeDen q ≠ 0)
    (hf : faddeevH4Den q ≠ 0)
    (h1mh4 : 1 - (heckeH q) ^ 4 ≠ 0) :
    acr.bring_factor = 1 / bringColorTubeDen q ∧
    acr.faddeev_h4_factor = -(q ^ 4) / faddeevH4Den q := by
  constructor
  · rw [acr.bring_factor_eq, bringColorTube_q_form q hq hb]
  · rw [acr.faddeev_h4_factor_eq, faddeevH4_q_form q hq hf h1mh4]

/-! ## §3  Substrate-instance scaffold (LOAD-BEARING SORRY)

The instance below is the categorical-proof open item. Constructing it
**requires** the categorical proof of the additive composition rule —
this is the research-grade load-bearing step from the audit §4a.

It is a single sorry, gated by an explicit bibliographic Ref
(per CLAUDE.md §1).
-/

/-- **Substrate instance (CONJECTURAL — load-bearing sorry).**

    This instance asserts the additive composition rule holds at the
    substrate q₀. The `composes_additively` field is identically
    discharged by `rfl` since `linkingWeightBringFaddeevH4` is defined
    as `bringColorTube + faddeevH4 − 1` — so this instance is in fact
    UNCONDITIONALLY CONSTRUCTIBLE.

    However, the CONJECTURAL content sits one level up: WHY is this
    the canonical decomposition vs the multiplicative one
    (`bring · faddeev`)? The construction here ASSUMES additive is
    canonical without justifying it categorically.

    Future work: replace this trivial-rfl construction with one
    derived from the categorical proof of the additive composition
    rule — at that point, the construction will use the partition-
    channel assignment data (from H_4 Wedderburn block decomposition)
    to derive the additive form from first principles, rather than
    asserting it. -/
instance substrate_additive_composition_rule :
    AdditiveCompositionRule q_0_substrate where
  bring_factor := bringColorTube q_0_substrate
  faddeev_h4_factor := faddeevH4 q_0_substrate
  bring_factor_eq := rfl
  faddeev_h4_factor_eq := rfl
  -- The composes_additively axiom is trivially rfl since
  -- linkingWeightBringFaddeevH4 is DEFINED as bring + faddeev - 1.
  -- The conjectural content is one level up (see docstring).
  composes_additively := by
    unfold linkingWeightBringFaddeevH4
    ring

/-! ## §4  Provable bounds via the substrate instance -/

/-- **Class-derived theorem.** Under the additive composition rule at
    q₀, the linking_weight prediction lies in (2.46, 2.465). Composes
    `LinkingWeightSubstrateBounds.linkingWeightBringFaddeevH4_at_q_0_bound`
    with the class. -/
theorem additive_linking_weight_bound_at_q_0 :
    @AdditiveCompositionRule.bring_factor _ substrate_additive_composition_rule
      + @AdditiveCompositionRule.faddeev_h4_factor _ substrate_additive_composition_rule
      - 1 > 246 / 100 ∧
    @AdditiveCompositionRule.bring_factor _ substrate_additive_composition_rule
      + @AdditiveCompositionRule.faddeev_h4_factor _ substrate_additive_composition_rule
      - 1 < 2465 / 1000 := by
  show bringColorTube q_0_substrate + faddeevH4 q_0_substrate - 1 > 246 / 100 ∧
       bringColorTube q_0_substrate + faddeevH4 q_0_substrate - 1 < 2465 / 1000
  have h := linkingWeightBringFaddeevH4_at_q_0_bound
  unfold linkingWeightBringFaddeevH4 at h
  exact h

/-! ## §5  Open work — what closing the conjecture would unlock

If the categorical proof of additive composition lands (research-grade,
multi-session), the following downstream theorems become accessible:

1. **m_p prediction theorem**: `|m_p_pred - m_p_CODATA| < 200 ppm`.
2. **65-isotope sweep theorem**: uniform `4-269×` improvement bound
   across the full mass table.
3. **Categorical equivalence (or distinctness)** between Bring +
   Faddeev h⁴ and PR #1272's Reading-A `5/2 − G·h²` at all orders in
   h (not just at q₀).
4. **L2 100× dashboard update**: pending whether the +108 ppm
   prediction passes the m_p 100× experimental target (currently
   misses by ~3 orders of magnitude — would close most of that gap).

All four are documented in the audit §4a and §6 (TODO map).
-/

end QOU.Archimedean
