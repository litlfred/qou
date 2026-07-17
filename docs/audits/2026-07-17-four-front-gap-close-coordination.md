# Four-front L2 gap-close: coordination reassessment (all four fronts are sibling-owned; one unowned piece remains)

**Date:** 2026-07-17 · **Branch:** `claude/gap-close-four-front-2026-07-17` (PR #3844) ·
**Tier:** coordination / assessment (no new compute; no `c_k` wired; no fit; no tier change).
**Supersedes-in-scope:** my session's plan to *drive* F1 — the sibling landings below overtook it.

## Why this note

Owner picked all four gap-close directions from the
[07-17 1ppQ path reassessment](2026-07-17-1ppq-path-reassessment.md). Between that
reassessment and this session's start, **main advanced 48 commits and three active
sibling PRs took up all four fronts.** Writing more compute on any of them would
duplicate or race. This note records the consolidated post-advance state, so the owner
and siblings share one picture, and names the single genuinely-unowned decidable piece.

## Four-front status (post 48-commit advance)

| Front | L2 targets | Status | Owner |
|---|---|---|---|
| **F1 — odd D-ladder Écalle acceleration** | Q_β, m_n, Δ_pn (3 obs, c₃) | **acceleration machinery built + run; MERGED.** Gate-fails at k=21 (dlog-Padé ρ≈0.156 vs root-test ≈0.32, 2× estimator gap); extension arm reached k=31, q-Gevrey drift **persists** (not a finite-k shadow). Machinery accepts any-length exact `(a_k,b_k)` lists — built to take more terms. My W9 parity-split was consumed as its "K2 Borel-plane grading". | merged (`2ece28dcb2`/`20a5dfdcd0`/`d2d53c5266`/`aa7f7e165f`) |
| **F2 — Lawrence–Rozansky modulus** | m_p, m_μ | **scope-(a) EXCLUDED** at Σ(2,3,5): the SU(2)-fibre / McKay-mark coloring route gives a D=2 collapse (`|S_{0λ}|` degenerate). Refuted, not closed. | PR #3823 (+ merged `5bc75b908b`/`5766bb6c32`) |
| **F3 — α_EM photon determinant** | α_EM headline | advanced: per-loop integer `8 = dim H¹(Bring)` is **uniquely data-selected** (forcedness, scope-(a)); the Front-3 lead `ζ_{Δ₁}(0) = −b₁` (area-free) is the ζ-regularized home of the bare `b₁` count. Reframed via the shared Bring period matrix τ (keystone link). | PR #3814 (+ merged `2e263ac45d`/`074dfccb4a`) |
| **F4 — GGM Stokes constant A_ω** | feeds F1 (even channel) | active: deriving A_ω via the **GGM 3d-index** of the geometric connection. This is the *monodromy datum* the resummation needs. | PR #3805 |

## The one genuinely-unowned decidable piece

Per the [bar-odd three-routes audit](2026-07-12-bar-odd-s-three-routes.md) §"What route 2
still needs": the odd-channel resummation needs the **deformed b-dictionary
normalization**, which **#3596's Φ_b (Faddeev quantum dilogarithm) construction supplies
once its saddle expansion is pushed to 2-loop at `m = q₀`.** F1's merged machinery is
built to consume more terms, and #3805 owns the *even*-channel GGM A_ω — but the
**odd-channel Φ_b 2-loop b-dictionary itself is unowned.** It is the concrete input that
would let the merged F1 acceleration convert its (gate-failing) numerical singularity
locator into a *derived* Stokes datum.

**Recommendation (owner decision):** rather than race the merged F1 machinery or #3805,
the non-duplicative high-leverage move is the **Φ_b 2-loop saddle b-dictionary at
`m = q₀`** — feeding F1's odd channel. It should be coordinated with #3805 (adjacent:
even-channel A_ω via GGM) to avoid a second Stokes-datum collision. Alternatively, feed
the merged F1 machinery **more terms** (ORD > 63, k > 31) to test whether the estimator
gate closes with order alone — but the persistent q-Gevrey drift suggests order alone
will not resolve it (the honest 07-13 boundary), so the Φ_b route is the better bet.

## Discipline

No new compute in this note; it consolidates sibling landings + reads. The anti-fit /
anti-laundering rules stand: any Φ_b 2-loop result is a *derived* normalization or it is
not wired. L2 count unchanged (2/7). Scoping of F2/F3/F4 was cross-checked against the
active sibling PRs (#3823/#3814/#3805) to confirm non-duplication.

## Cross-references

- Reassessment: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)
- F1 machinery + verdict: [`2026-07-17-dladder-ecalle-acceleration.md`](2026-07-17-dladder-ecalle-acceleration.md), [`2026-07-17-dladder-qborel-acceleration.md`](2026-07-17-dladder-qborel-acceleration.md)
- Bar-odd routes + the Φ_b-2-loop open item: [`2026-07-12-bar-odd-s-three-routes.md`](2026-07-12-bar-odd-s-three-routes.md)
- My merged parity-split (F1's K2): [`2026-07-17-dladder-parity-split-arithmetic-normalized.md`](2026-07-17-dladder-parity-split-arithmetic-normalized.md)
