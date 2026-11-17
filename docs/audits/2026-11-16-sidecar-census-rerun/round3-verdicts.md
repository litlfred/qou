# Sidecar review, round 3 (2026-11-16/17)

Branch `claude/sidecar-review-round3-2026-11-16`, issue #8174, PR #8175.

## Writer fix

`folio/pipeline/qa-agent-entry.ts` never installed the Lean layer, so for a
block whose Lean is a library declaration (no sibling `.lean`) the verdict was
written without a `lean` hash. 48 verdicts from the 2026-11-15/16 review lack
one (26 dated 11-15, 22 dated 11-16), plus 5 older drain entries. They read as
stale. They are left as they are pending an owner decision (re-read each, or
re-stamp only those whose Lean is unchanged since `reviewed_sha`).

A further 29 stale verdicts are on sibling-Lean blocks whose Lean changed after
review. They need a real re-review.

## New verdicts: the six #8095 blocks (all now carry a lean hash)

| block | statement vs Lean | proof |
|---|---|---|
| centre-cocentre-descent | warn: item 7 rests on an unformalised H_3(q) presentation, unflagged in the statement | pass |
| pair-graph-regime-trichotomy | warn: "every integer A" vs `A : ℕ` | pass |
| h3-frobenius-casimir-markov-trace | warn: c_λd_λ only checked; K⁶ associativity unformalised | pass |
| order-of-magnitude-screen | warn: `screen_mul` has `0 ≤ lam`, item 1 does not | pass |
| cellular-depth-filtration | warn: item 2 equality proved as ⊆; iff proved one way; item 3 count unformalised | pass |
| cell-depth-truncation | warn: Lean is over an abstract depth function; τ(E_k x) link and item 4 KL facts cited | pass |

## Re-review of the five #8138 proofs (da-non-sequitur)

| proof | verdict | residual |
|---|---|---|
| pieri-photon-shift | warn | Schur–Weyl for SU_q(2) covers two-row λ only; the statement does not restrict λ |
| t-beta-markov-frobenius-collapse | pass | — |
| hecke-markov-transition | warn | (iv) needs cyclicity of tr_M; proof ends with ∏V̂_i, statement says z^ℓ |
| groebner-shirshov-energy | pass | — |
| topological-mass-formula-algebraic | warn | ln needs Vol_{q0}(β) ≠ 0, not stated |

All are findings. No content was changed.
