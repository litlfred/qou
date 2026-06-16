# Q_β 1ppQ closure — three-step plan

**Date:** 2026-06-02
**Branch:** `claude/qbeta-1ppq-closure-2026-06-02`
**Trigger:** Owner directive "do all 3" — execute the three next-steps identified at PR #1713's close: singularity-type ID, cross-anchor validation, dashboard wiring.

> **Notation.** `u_subst` is shorthand for `u_substrate = b · ℏ_q²` ≈ 0.00852 at q_0 throughout this document.

> **Math correction (per Gemini review of PR #1727).** Distinguish two objects built from the ladder coefficients c_k:
> - **`g(u) = Σ_k c_k u^k`** — the log-correction *generating function* (≈ `log Π(1 + c_k u^k)` to leading order). The asymptote `c_k · u_subst^k → A_const` (the test below) means `g(u) → Σ A_const (u/u_subst)^k = A_const · u_subst / (u_subst − u)` — i.e. **`g(u)` has a SIMPLE POLE** at u_subst with residue `A`. This is the object the discriminator characterizes, and the categorically-meaningful one (it is the log-derivative quantity).
> - **`F(u) = Π_k (1 + c_k u^k)`** — the *product* correction factor itself. Since `F(u) = exp(g(u) + …)`, a simple pole of `g` makes `F` have an **essential singularity** (`F ~ exp(C/(u_subst − u))`). So "simple pole" refers to `g(u) = Σ c_k u^k`, NOT to the product `F`.
>
> Earlier drafts wrote "F(u) = Π(1+c_k u^k) has a simple pole" — that was a sum/product conflation; the precise statement is "the generating function `g(u) = Σ c_k u^k` has a simple pole, equivalently the product `F` has an essential singularity (exp of that pole)".

## Background

PR #1713 (merged `a99493e20c`) established that the Q_β precision-ladder generating function `g(u) = Σ c_k u^k` has **radius of convergence exactly equal to u_substrate** at q_0 (asymptotic `c_{k+1}/c_k → 1/u = 117.41` matched to 4 sig figs at k=8,9,10). `g(u)` has a singularity at the very evaluation point u_substrate ≈ 0.00852.

The radius-of-convergence finding alone does NOT discriminate among singularity types (simple pole / branch point of fractional order / essential). Identifying the type bounds the categorical-ID search drastically — which is the prerequisite for 1ppQ closure.

## Step 1 — Identify the singularity type at u = u_substrate

Discriminate the singularity of `g(u) = Σ c_k u^k` via three measurements, all tractable with existing SDP infrastructure:

| candidate (for `g(u) = Σ c_k u^k`) | c_k asymptote signature | g(u) asymptote |
|---|---|---|
| Simple pole `A/(u_subst − u)` | `c_k → A · u_subst^(−k−1)` (constant prefactor) | `A · u_subst/(u_subst − u)` |
| Branch point order β | `c_k → C · k^(β−1) · u_subst^(−k)` | `(u_subst − u)^(−β) · h(u)` analytic h |
| Essential (of g itself) | `c_k` grows faster than any geometric | `g` has exp(1/(u_subst−u)) singularity |

**Test:** the c_2..c_10 already extracted ([`qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py)) suffice — the k=8,9,10 asymptote is already clean. (Extending to c_11..c_15 is NOT possible without postulating canonical forms per rung, which would be an ansatz fit — see the Step 1 method note in the audit.) Check:
1. Is `c_k · u_subst^k` constant at large k? → simple pole.
2. Is `c_k · u_subst^k / k^β` constant for some non-integer β? → branch point.
3. Does the ratio grow super-geometrically? → essential.

Reports tiered (PROVED if constant within 1 ppm; NEAR-MATCH within 1%; REFUTED otherwise).

## Step 2 — Cross-anchor validation at q_muon

PR #1713's radius-of-convergence finding was measured at the m_p-anchored q_0 (CAL-2 = 1.10997858...). Per CLAUDE.md §"Im(q) fibre vs observable" (2026-06-01), the c_k coefficients live in the FIBRE; their archimedean evaluation at q_0 hits a singularity of F. The fibre-level F(q) should produce DIFFERENT c_k swings at different anchors.

**Test:** repeat step 1 at q_muon (the alternative anchor mentioned in the 2026-05-31 c_3 verdict audit). If the singularity type is the SAME at both anchors but the residue/exponent values differ, that's the fibre-vs-observable signature. If the type differs, the analytic structure is anchor-dependent (more pathological; would constrain the categorical search differently).

Out-of-scope per CLAUDE.md "no production wiring before cross-anchor validation".

## Step 3 — Wire converged form through to dashboard

If steps 1 + 2 converge on a categorical singularity-type + matching residue:

- Replace the empirically-extracted c_3..c_10 in [`qbeta_ladder_verification_1ppq.py`](../../computations/qbeta/qbeta_ladder_verification_1ppq.py) with the derived formula
- Re-run the L1 dashboard `onepb-status-dashboard.witness.json` — should show the new derived tier
- Append to `1ppq-qbeta.md` ledger
- Reports tiered per the canonical-derivation-cheat-sheet TRUNCATION ORDER framing

If steps 1 + 2 do NOT converge (e.g. step 1 produces fractional β that doesn't match the m_p chain), report tiered NEAR-MATCH and document why; NO production wiring without convergent categorical ID.

## Forbidden (CLAUDE.md)

- No c_k ansatz fits (4-session flip-flop is cautionary).
- No binary wired/dropped: tiered reports only.
- No production wiring before cross-anchor (q_proton + q_muon) validation passes.

## Coordination

Builds on PR #1713 (just merged). Sibling #1521 (α_em Habiro categorical ID) is the methodology-dependency PR. No new sibling overlap expected — Δ_λ binding work (PR #1709 area + the `a06f0cc120` landing) is a parallel observable, not in conflict.

## Cross-references

- PR #1713 audit: [`docs/audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md`](../audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](1ppq-qbeta.md)
- c_3 settled verdict: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md)
- Canonical framing: [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
