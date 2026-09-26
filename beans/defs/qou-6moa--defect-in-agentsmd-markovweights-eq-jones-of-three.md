---
# qou-6moa
title: 'DEFECT in AGENTS.md: markovWeights_eq_jones_of_threeRow_eq_zero is cited for its own HYPOTHESIS'
status: todo
type: task
priority: high
created_at: 2026-09-26T14:15:29Z
updated_at: 2026-09-26T14:16:21Z
---

## The mis-citation

AGENTS.md (§"q₀ anchor convention", R1 block) states that `y_(1³) = 0` holds *by
construction* under convention D, **citing
`markovWeights_eq_jones_of_threeRow_eq_zero`**. That declaration runs the other
way. Literal signature,
`content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean:119`,
context `variable {R : Type*} [CommRing R] [IsDomain R]`:

```lean
theorem markovWeights_eq_jones_of_threeRow_eq_zero (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hTL : y₁₃ = 0)          -- ← HYPOTHESIS
    (hfaith : y₂₁ ≠ 0) :     -- ← and faithfulness on the 2-row block is another
    (q + qi) ^ 2 * y₂₁ = 1 ∧ y₃ = 1 - 2 * y₂₁ ∧ z * (q + qi) = q ^ 2
```

So `y₁₃ = 0` is the **hypothesis** and **convention D is the conclusion** — the
implication the document wants is the exact reverse. And `hfaith` is
load-bearing, not decorative: the same file's `markovWeights_degenerate_root`
proves that dropping it makes the conclusion **false** (the `y = (1,0,0)` trivial
character at `z = q`), not merely unprovable. A declaration that *assumes* a form
of faithfulness cannot be evidence about faithfulness.

## The correct citations, both sorry-free on `main`

- `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser`
  (`TemperleyLiebTower.lean:368`) — `z·(q²+1) = q³` plus the three moment
  equations gives `y₁₃ = 0`. This is the forward direction.
- `QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu`
- and for general `n` on the actual weight,
  `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`
  (`OcneanuWeight.lean:142`), unconditional over any field with `q²+1 ≠ 0` —
  which is what PR #7458 uses.

## Why this is not fixed in #7458

It is a citation swap inside a STRICT document, and the standing rule is to ask
the owner before changing things unless the change increases precision or is
corpus-derived. It *is* corpus-derived (the Lean signature decides it and a
reviewer can check it by opening one file), so it qualifies — but a STRICT
document is where a wrong edit costs the most, so it was raised in the PR body
with the signature quoted rather than swept. **Blast radius**: the report that
found it counted ~35 corpus sites citing this declaration; whether any of them
repeat the reversal is NOT measured and is the first thing to do here.

Found by the corpus-grep for PR #7458 (bean `qou-r7kp`), 2026-09-26.
