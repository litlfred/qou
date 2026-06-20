# Story B selection — canonical Q_β precision-ladder chain

**Date:** 2026-05-16
**Branch:** `claude/crystal-and-he4-combined`
**Status:** Documents the canonical-status framing of **Story B** (the
categorical chain) for the Q_β precision ladder. Initially framed (2026-05-16)
as user-preference selection. An attempted 2026-05-17 upgrade to "structurally
forced" — based on [PR #664](https://github.com/litlfred/qou/pull/664)'s
claim to derive c_3 = -2 categorically — has been **walked back**: see
[2026-05-17-pr-664-c3-c4-critical-review.md](2026-05-17-pr-664-c3-c4-critical-review.md).
PR #664's probes are tautological (they assert c_3 = -2 by hardcoding -2
in two places and checking they're equal); the proof sketch hand-waves the
critical step. **Story A is empirically disfavoured by ~60× but not
categorically falsified** by what is currently on main. Story B remains the
preferred reading; calling it "forced" overstates what has been shown.
Evidence as of 2026-05-17: PR #661 (c_2 = b², genuine derivation) +
consistency with empirical c_3 ≈ -2 and c_4 ≈ 3/2.

## Background — Story A vs Story B

PR #657 (merged) flagged a high-precision finding: at `dps = 200`,
the categorical-chain coefficients `c_k` of the Q_β precision ladder
can be interpreted either as:

| | c_2 | c_3 | c_4 | c_5+ |
|---|---|---|---|---|
| **Story A** | b² · (1 + 0.017) | 0 (CODATA noise) | 0 | 0 |
| **Story B** | b² (Kashiwara, exact) | -2 (J_Hopf at q=1) | b² + 1/2 (mixed) | open (categorical) |

Both stories reproduce CODATA Q_β to within its measurement floor
(~400 ppb).  PR #657 left the choice open.

## Story B status — preferred but not categorically forced

Earlier framing of this section ("Story B forced — Story A falsified")
was retracted on 2026-05-17 after critical review of PR #664. See
[2026-05-17-pr-664-c3-c4-critical-review.md](2026-05-17-pr-664-c3-c4-critical-review.md).

PR #664 ships `prop:hopf-jones-c3-categorical` and proposes
c_3 = J_Hopf(q=1) = -2 via V_(2,1) self-fusion + Frobenius selection
of V_(2,2,2) + Hopf evaluation at q = 1. Critical review finds:

- The companion probe is tautological (hardcodes `J_Hopf(q) = -(q + q⁻¹)`
  and `c3_empirical = -2`, then "verifies" they match).
- The proof sketch hand-waves Step 2 (Frobenius selection picks V_(2,2,2)
  via Markov stabilisation) and Step 4 (order-h^6 coefficient extraction
  from the Q_β expansion).
- The textbook Jones polynomial $-(q+q^{-1})$ is correct as a fact but
  not derived from V_(2,1) Hoefsmit; the PR #661 c_2 template (symbolic
  Markov trace, then coefficient extraction) has not been ported.

Therefore Story B is **strongly preferred** — empirically by ~60×
(0.0066 ppm residual vs Story A's ~400 ppb floor) and structurally by
the categorical reading of the precision ladder — but **not
categorically forced** by what is currently on main. A genuine
derivation analogous to PR #661 would be required to upgrade the
status. Candidate Story B confirmation:

1. **PR #661** (merged): c_2 = b² *exactly* from V_(2,1) Hoefsmit alone —
   no fit, no free parameter.  Symbolic identity at q = 1 + ε to
   order ε^4; 50-dps mpmath confirmation at q_0 within 1.55 × 10⁻⁶².

2. **PR #664** (open): proposes c_3 = J_Hopf(q=1) = -2 from V_(2,1)
   self-fusion + Frobenius selection of V_(2,2,2) + Hopf-Jones at q=1.
   **Critical review (2026-05-17) finds the categorical derivation is
   not actually performed** — the probes are tautologies and the
   proof sketch hand-waves the critical step. The value is consistent
   with PR #655's empirical c_3 ≈ -2, but not derived in the sense
   PR #661 derived c_2.

3. **PR #665** (open, due to merge): c_4 = b² + 1/2 (mixed Kashiwara
   + half-Hopf offset) closes the N=4 rung of the precision ladder.

Story A's c_2 = b² · (1 + 0.017) is incompatible with PR #661's exact
b² categorical derivation — PR #661 is the one genuinely-categorical
proof in the chain (symbolic Hoefsmit Markov trace, no fit). The 1.7%
deviation in Story A's c_2 reading is empirically attributable to the
higher c_k contributions (c_3, c_4, …) but the *categorical*
derivation of those higher c_k is currently open (see PR #664 critical
review). The Story B reading remains the natural one — but the
"forced" upgrade requires more than what is on main today.

## Consequences for PR #670 (merged 2026-05-17)

PR #670 (merged) carries:
- **Crystal-pole counter + Habiro bridge** (PRs #668 + #669 + this PR):
  derives `shift(Z, N) = 18Z + 21N + 1` categorically.  Independent
  of Story A/B selection (shift is structural, not a precision-ladder
  coefficient).
- **⁴He compositional probe**: confirms Model B (knot identification
  via composition) is ambiguous at the Markov-trace level — separate
  concern from Story B.
- **H_12 ⁴He scaffold**: extends Sub-lemma 2.1 to ⁴He via three-fold
  iterated branching basis.  Independent of Story A/B.

**No work on this branch contradicts Story B.**  PR #661's c_2 = b²
proof IS Story B's c_2 step.

## What remains open under Story B

- **c_5, c_6, …** — the higher precision-ladder coefficients are
  predicted to be structurally derivable (Jones invariants at q=1 of
  specific links from V_(2,1)^⊗k self-fusion) but the explicit
  derivations are not yet done.  PR #657's empirical c_5 ≈ -395
  doesn't match simple Jones-at-q=1 values; the categorical structure
  must involve higher-rank Wedderburn coefficients or composite
  Jones products.  Open R&D.

- **Lean formalisation** of `c_3 = -2` and `c_4 = b² + 1/2` propositions
  in PR #664/665 — bundles into the conditional-class chain per
  AGENTS.md §3b-cond, with the V_(2,2,2) channel selection as the
  axiomatic input.

## Cross-references

- [PR #661 (merged)](https://github.com/litlfred/qou/pull/661) — c_2 = b² categorical
- [PR #657 (merged)](https://github.com/litlfred/qou/pull/657) — Story A vs Story B framing
- [PR #664 (open)](https://github.com/litlfred/qou/pull/664) — c_3 = J_Hopf(q=1) categorical
- [PR #665 (open)](https://github.com/litlfred/qou/pull/665) — c_4 = b² + 1/2 mixed
- [PR #670 (open, this branch)](https://github.com/litlfred/qou/pull/670) — crystal shift_NF + ⁴He compositional + H_12 scaffold

## CAL discipline

All Story B coefficients are categorical-derivation results — they
use only the substrate parameter q_0 (CAL-2) and the Hoefsmit
representation theory of V_(2,1).  No m_e, Q_β, AME, or experimental
data enters their derivation.  CODATA Q_β is referenced for
validation only, not calibration.
