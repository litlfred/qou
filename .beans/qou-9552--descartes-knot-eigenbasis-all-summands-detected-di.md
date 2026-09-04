---
# qou-9552
title: 'Descartes knot eigenbasis: all_summands_detected discards the summand index'
status: completed
type: task
priority: normal
created_at: 2026-09-03T21:19:44Z
updated_at: 2026-09-04T02:16:55Z
---

Found while repairing `braids-and-knots/knot-eigenbasis-complete.lean` on
`claude/sap-sibling-tree-2026-09-03` (PR #6539). Recorded rather than fixed:
different block, and its own docstring already discloses the gap.

**Where.** `content/quantum-observable-universe/brings-surface/descartes-knot-eigenbasis.lean:215`

```lean
  all_summands_detected : ∀ (n : ℕ) (hn : n ≥ 1),
    let sw := schurWeyl n hn
    ∀ (_ : Fin sw.numSummands),
    ∃ (jonesVal : ℝ), jonesVal ≠ 0
```

**What is wrong.** Two things, and the second is worse than the one fixed next door:

1. The summand index is bound as `_` — explicitly discarded, so nothing is said *per summand*.
2. `jonesVal` is a **free real** tied to no trace, no braid and no character. So the field asserts that `ℝ` has a non-zero element. Any instance discharges it with `⟨1, one_ne_zero⟩` — and `descartes_knot_eigenbasis` at line 246 does exactly that for the trace it constructs (`tr := fun _ _ => 1`).

The sibling defect in `knot-eigenbasis-complete.lean::summands_detected` was milder: `μ` was bound and unused, but the detected quantity was at least the real `markov.tr (braid_rep β)`.

**What the file already admits.** `descartes_knot_eigenbasis`'s docstring is honest that the detector is one constant for every summand: *"Full per-summand completeness — the distinct character value on each irreducible for general `n` — is the concrete `n = 3` content of `descartes_n3_both_detected` below; the general-`n` character formula is upstream."* So this is a known gap the *type* does not reflect, not a hidden one.

**Shape of the fix**, mirroring what landed next door (commit `c85cd09a591`): give `DescartesMarkovTrace` a per-summand component and quantify detection over it, so the `Fin sw.numSummands` argument occurs in the body. That will make `descartes_knot_eigenbasis`'s current proof (`⟨-(D.q + D.q⁻¹), _⟩`, the same value for every index) fail — which is the point: the general-`n` character formula is what is missing, and it is upstream.

**Not urgent.** Nothing downstream depends on the vacuous field being true, because it is true of everything.


## 2026-09-04 — done, and it grew (PR #6547)

Both fields repaired as scoped: `trSummand` component constrained by
`tr_eq_sum_summands`, detection restated over it, index occurs in every body.
Plus `schurWeyl_level`, a missing consistency field — `DescartesSchurWeyl`
carries its own `n` and nothing tied it to the level it was requested at.

**The scope note above was wrong in the direction that matters.** It said the
gap was "known" because `descartes_knot_eigenbasis`'s docstring pointed at
`descartes_n3_both_detected` as the concrete `n = 3` content. That theorem was
`∃ (j_sym j_mix : ℝ), j_sym ≠ 0 ∧ j_mix ≠ 0` — the same defect, in the file's
own designated fallback. So the disclosure I cited as the reason not to touch
the file was itself resting on a vacuous statement.

**Naming the two values exposed a negative.** With `jonesSymmetric = -(q+q⁻¹)`
and `jonesMixed = -q⁻⁴(1-q²+q⁴)` written down, equality reduces over `q > 0`
to `q⁵ - q⁴ + q³ + q² - 1 = 0`, which has a root in `[7/10, 4/5]`. Hence
`jones_channels_not_separating`: **a Descartes universe exists in which the
two `n = 3` channel values are the same number** — `q ≈
0.779544663820934968877573423932`, both `≈ -2.0623447988`, measured at 50 dps
before any Lean was written, and `0 < q`, `q ≠ 1`.

So exhibiting two non-zero values does not establish the summands are
distinguished. Scope-(a): a negative about this pair as a separator, not about
eigenbasis completeness — separation may hold via `trSummand`, whose
general-`n` character values are upstream.

Three theorems carry it: `jonesSymmetric_eq_jonesMixed_iff` (the reduction,
proved), `jones_channels_coincide` (IVT), `jones_channels_not_separating`.
The first exists because the draft stated the reduction in prose only — the
same defect class, inside the commit repairing it.

**Left open, and it is the real one:** the per-summand character values for
general `n`. Not opened as a bean — it is the upstream gap the file has always
named, not a defect introduced by anything here.
