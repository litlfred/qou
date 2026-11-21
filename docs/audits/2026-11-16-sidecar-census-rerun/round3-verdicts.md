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

## Re-grade (owner question, 2026-11-17)

Rule applied from here on: if a statement claims more than its Lean, or more
than its own proof shows, it is a **fail**; a statement that is fully backed
but relies on a cited step it does not flag stays a **warn**.

Moved warn → fail (major): cellular-depth-filtration (statement-vs-Lean),
order-of-magnitude-screen (statement-vs-Lean), pieri-photon-shift (proof),
topological-mass-formula-algebraic (proof).

## Re-read of the hash-less verdicts (owner chose "re-read all")

The "48" was a count of verdict *entries*; the latest verdict per block lacked
a Lean hash on **27** blocks. All 27 were re-read. Each new verdict carries a
lean hash; the remaining hash-less count is 0.

| block | verdict | note |
|---|---|---|
| hecke-satisfies-blitvic-hypothesis | fail critical | md claim false: third central moment at q=2 is −1.428, not 0 |
| trace-locality-meets-gs-nonlocality | fail major | locality assumed as a class field, and stated without the H_n index (false as written) |
| photon-threading-mass | fail major | formula assumed via two context fields |
| two-filtration-bridge-small-cases | fail major | self-assuming; md Result still says "verified" |
| frobenius-self-duality-forces-lp-dual-extraction | fail major | non-degeneracy assumed |
| feynman-eigenbasis-decomposition | fail major | returns a structure field |
| em-spectral-completeness | fail major (was warn) | Lean is a 2×2 diagonal toy |
| wedderburn-trace-identity | fail major | identity assumed |
| cyclotomic-depth3-dimension-synthesis | fail major | lean.ref dangling; md says unconditional |
| tmli-constituent-composite-agreement | fail major (was warn) | multiplicativity assumed; counterexample checked |
| skein-generation | fail major (was warn) | freeness not in Lean |
| t-beta-markov-frobenius-collapse-general | fail major | self-assuming; claim is true and easy to prove |
| unit-modulus-eigenvalue | warn minor | formula proved; det and |χ|≤2 criterion elementary, unformalised |
| knot-factor-spectral-derivation | fail major | rfl over data; identity checked true by hand |
| operator-selection-lp | pass | |
| feynman-trace-collapse | fail major | partition-count bound only |
| corrected-markov-trace | pass | |
| feynman-categorical-trace | fail major | **content errors:** tr(xσ⁻¹)=z⁻¹tr(x) is wrong (it is (z−h)tr(x)); w_λ has an extra dim S_λ |
| feynman-markov-identification | fail major | same w_λ error; identity assumed |
| s4-s3-half-symmetric-projection | pass | |
| six-term-per-derivation-weights | warn major | conjecture block whose Lean is the defining formula |
| 6 conjecture blocks | n/a | mass-categorical-descent carrier is weaker than the md |
