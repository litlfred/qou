# Coordination ledger — Story B c_3/c_4/κ categorical derivation

**Goal:** establish whether Story B (categorical chain for Q_β
precision-ladder coefficients) is structurally forced or merely
preferred. Critical for the 1-ppb mass program's claim that the
0.0066 ppm Q_β residual is a *prediction* of QOU rather than a fit.

## Scope (as of 2026-05-17)

| PR | Title | State | Role |
|---|---|---|---|
| #670 | Crystal-bases shift_NF + ⁴He JSJ + ordering-invariance | merged | upstream — assumed Story B as user-direction selection |
| **#671** (this branch) | docs: Story B forced + m_p chain closure gap analysis | open | **walking back** the "structurally forced" framing after PR #664 critical review |
| #664 | prop:hopf-jones-c3-categorical (Story A falsified) | open | claims c_3 = -2 categorically; **critical-review-flagged** |
| #665 | N=4 + σ_1 eigenstructure + n-strand BraidGroup | open | downstream of c_4; same template question |
| #663 | isotope-mass-table honest no-cal regen + anti-staleness | open | parallel; not on Story B critical path |
| #661 | c_2 = b² categorical | merged | the TEMPLATE for a genuine categorical proof |

## Classification

- **Overlap (high)**: #671 ↔ #664 — my critical review and genuine
  Markov-trace probe directly address PR #664's claims.
- **Dependency**: #671's Story B audit was upgraded based on #664,
  then walked back after critical review of #664's probes.
- **Cherry-pick potential**: PR #664 author could integrate my
  genuine probe + critical-review audit doc to fix the gaps; in
  exchange, PR #664's structural framing of V_(2,2,2) → Hopf could
  be ported into #671's audit if rigorised.

## Critical-review findings (2026-05-17)

PR #664 ships three categorical claims:

1. **c_3 = J_Hopf(q=1) = -2** — probe is tautological (hardcodes -2
   in two places). Proof sketch hand-waves Step 2 (V_(2,2,2) → Hopf
   via Markov stabilisation) and Step 4 (order-h⁶ extraction).
2. **c_4 = b² + 1/2 = 3/2** — probe computes `c4 - c4 == 0` (same
   expression in both sides) with `b = 1` asserted.
3. **κ = -E_0·log(1/h)/([2]_q·[3]_q)** — formula was "identified
   empirically in PR #645", then interpreted; 0.035% numerical
   match is suggestive but not symbolic equality (cf. PR #661's exact
   c_2 = b² template).

Additional infrastructure finding:

- The codebase has TWO different tr_M implementations
  (`hoefsmit_symbolic.tr_M_symbolic` and
  `markov_weights_symbolic.tr_M_canonical`) that produce *different*
  symbolic answers for σ_1² in H_2 (both give +1 at q=1, but
  different rational functions). Neither equals the textbook Jones
  polynomial -(q+q⁻¹) directly. The Story B coefficient extraction
  needs an explicit convention choice the PR doesn't make.
- Writhe correction is required to go from Markov trace to Jones
  polynomial. tr_M_QOU(σ_1^odd)|_{q=1} = 0 always (Markov-parameter
  factor); J_knot(t=1) = 1 always — no single multiplicative
  normalization reconciles them.

## Actions taken on this branch (#671)

| Action | Commit |
|---|---|
| Audit doc: critical review of PR #664 | `26f677677` |
| Walk-back of "Story B structurally forced" in story-b-canonical-chain audit | `26f677677` |
| Genuine V_(2,1) seminormal Markov-trace probe for σ_1² in H_2 | `7f06e0bef` |
| Probe extended with tr_M_canonical comparison + dual-implementation finding | (this commit) |
| Coordination comment on PR #664 | (link below) |

## Coordination posts

- 2026-05-17 — comment on [PR #664](https://github.com/litlfred/qou/pull/664#issuecomment-4468992940) summarising critical-review findings and proposing the PR #661 template as the path forward.
- 2026-05-17 — follow-up coordination comment on PR #664 with dual-implementation finding (this round).

## What would close this

A genuine c_3 = -2 derivation needs:

1. Decide which tr_M is canonical (`tr_M_symbolic` or `tr_M_canonical`).
2. Compute the symbolic Markov trace of σ_1² (or the relevant
   V_(2,2,2)-projected object in H_6) via that canonical tr_M.
3. Verify it equals the textbook Jones value (or doesn't, with a
   stated writhe-correction factor).
4. Extract c_3 from the order-h⁶ Taylor expansion of Q_β around
   q=1 (not q=1 evaluation, which loses Taylor information).
5. Verify no other order-h⁶ contribution survives Frobenius selection.

The PR #661 template does steps 1–3 for c_2 = b². The analogous work
for c_3 is the proper closure of Story B at N=3.

## Next concrete task on the queue

Currently working PR #671. After this coordination cycle:

- (optional) implement the "tr_M_canonical contribution to σ_1²
  expanded around q=1+ε to order ε^6, with c_3 coefficient extracted"
  — this would be the genuine c_3 derivation, ~PR #661-scale work.
- Decide with the user whether to merge PR #671 now (audit-only,
  walk-back + critical review) or expand it with the genuine c_3
  computation.

## 2026-05-17 update — H_3 numerical comparison

User asked: "can we compare tr_M_canonical in mass scripts vs symbolic/production?"

Ran a side-by-side comparison on H_3 braids that production
mass-derivation chains evaluate. **The two implementations differ by
57–99% on the proton's intra-nucleon Hecke word.**

| Braid in H_3 | `tr_M_symbolic` | `tr_M_canonical` | rel |Δ| |
|---|---:|---:|---:|
| σ_1 | 0.1032 | 0.4993 | **79%** |
| σ_1·σ_2 | 0.00357 | 0.2493 | **99%** |
| σ_1³ (proton intra) | 0.3142 | 0.7302 | **57%** |
| σ_1³·σ_2³ (proton-like) | 0.09209 | 0.5332 | **83%** |

The 8% discrepancy on σ_1² in H_2 was the lower bound. On the
braids actually consumed by mass scripts, the discrepancy is 57-99%.

User asked: "is either proved to be derived from Cat Action?"

Answer (in dual-tr-m-discrepancy.md):
- `tr_M_canonical` (Wenzl y_λ) **YES** — Ocneanu/Wenzl categorical
  derivation, computes Jones polynomial of braid closure.
- `tr_M_symbolic` (dim_q²/[n]_q!/f^λ) **NO** documented Markov-trace
  derivation. Computes a different invariant (q-Plancherel expectation
  of normalized character), not the Jones polynomial.

So production scripts use a non-canonical tr_M whose categorical
derivation is undocumented, while the framework's `thm:jones-markov-trace`
cites the canonical one.

## §6 escalation candidates

This finding has cross-cutting implications beyond PR #664:

- PR #663 (m_p chain) uses `tr_M_symbolic` for the proton-mass
  derivation — the chain may be computing the wrong invariant for its
  own claimed identification.
- PR #661 (c_2 = b² categorical, merged) — needs cross-check: which
  tr_M did its symbolic derivation use? If `tr_M_symbolic`, its claim
  of "Markov trace of V_(2,1) Hoefsmit" is in the same non-canonical
  category.
- 1-ppb dashboard Layer 1/2 is internally consistent within
  `tr_M_symbolic` (Hoefsmit ↔ markov_peel both use it), but its claim
  of computing the Jones polynomial requires reframing.

Recommended owner adjudication:

1. Was the choice of `tr_M_symbolic` deliberate (e.g. a different
   well-defined invariant the framework wants to compute) or
   accidental (the name overloads with the literature-canonical
   Jones-Markov)?
2. If accidental: rename + audit + replace. ~15 scripts affected.
3. If deliberate: document the choice; update `thm:jones-markov-trace`
   in CLAUDE.md §7a to reflect the actual computed invariant.
