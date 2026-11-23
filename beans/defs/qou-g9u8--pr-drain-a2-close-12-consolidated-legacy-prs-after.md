---
# qou-g9u8
title: 'PR-Drain-A2: Close 12 Consolidated Legacy PRs After Parent Queue PRs (#9189, #9191, #9200) Merge (Preserve Branches)'
status: in-progress
type: task
priority: high
created_at: 2026-11-23T20:55:53Z
updated_at: 2026-11-23T20:55:53Z
parent: qou-xip2
---

### Safety Protocol for `(A2)` Consolidated Legacy PRs
- **NEVER** close any `(A2)` PR until `gh pr view <queued_pr> --repo litlfred/qou --json state,mergeCommit` confirms `"state": "MERGED"`!
- **NEVER** pass `--delete-branch` or `-d` to `gh pr close`!

### All `12` `(A2)` PRs
- **`#9151`** (`claude/archimedean-limit-endpoints-2026-11-22`) -> Parent **`#9189`** [CLOSED (parent MERGED)]: ArchimedeanLimit at x = ±1; Route 9 identities from #8193; the Λ-sum gives D below the axis — Consolidated in #9189 item 3 (ArchimedeanLimit endpoints x=±1, Route 9 identities, lower-half-plane Λ-sum).
- **`#9133`** (`claude/riemann-identity-theorem-2026-11-22`) -> Parent **`#9189`** [CLOSED (parent MERGED)]: Identity theorem on a connected Riemann surface; cyclic point stabilisers without hloc (qou-4xht) — Consolidated in #9189 item 1 (Riemann surface identity theorem & cyclic stabilisers without hloc).
- **`#9132`** (`claude/hecke-sw-bean-drain-2026-11-22`) -> Parent **`#9189`** [CLOSED (parent MERGED)]: Lean: S_n Poincaré polynomial for every n; Gaussian binomial symmetry and q = 1 limit — Consolidated in #9189 item 2 (S_n Poincaré polynomial & Gaussian binomial symmetry).
- **`#9114`** (`claude/pl-isotopy-exact-image-2026-11-22`) -> Parent **`#9200`** [OPEN (gated on `#9200` MERGED)]: PL isotopy ⇒ Δ-equivalence: general position (#8902, stage 2) — Stage-2 general-position corner perturbation / PLDeltaEquiv consolidated in #9200.
- **`#9072`** (`claude/pl-alexander-trick-2026-11-22`) -> Parent **`#9200`** [OPEN (gated on `#9200` MERGED)]: PL Alexander trick, PL isotopy to the identity, and hyperplane slices (#8902 part A) — PL knot topology Part A (PLAlexanderTrick, PLSlice, etc.) consolidated in #9200.
- **`#8761`** (`claude/batch-merge-g8-2026-11-21`) -> Parent **`#9191`** [CLOSED (parent MERGED)]: W4 batch merge group 8 (Lean only): #8274 #8153 #8218 #8189 #8225 — memory-blocked and conflicting ports, resolved — Consolidated in #9191 item 2 (Group 8 batch Lean ports rebased onto main).
- **`#8750`** (`claude/bring-chart-step-2026-11-21`) -> Parent **`#9189`** [CLOSED (parent MERGED)]: M2 chart step: point stabilisers of a holomorphic action are cyclic (qou-mq3p) — Consolidated in #9189 item 1 (M2 chart step cyclic point stabilisers).
- **`#8748`** (`claude/class-debt-fixes-2026-11-21`) -> Parent **`#9189`** [CLOSED (parent MERGED)]: Fix 4 defective Mathlib-debt classes: TransferLemmas (L-length), JonesBasicConstruction (3 levels), JonesWenzlProjector (strand-killing), drop vacuous KLR — Consolidated in #9189 item 4 (3 remaining defective Machinery class fixes; TransferLemmas already on main).
- **`#8531`** (`claude/batch-pr-triage-2026-11-20`) -> Parent **`#9191`** [CLOSED (parent MERGED)]: W4: batch-formalization PR triage — 351 PRs classified (script + table) — Consolidated in #9191 item 1 (W4 batch-pr-triage.py + 351-PR triage ledger).
- **`#8274`** (`feat/round66-young-alien-lp-dt-spectral-43c1`) -> Parent **`#9191`** [CLOSED (parent MERGED)]: feat(lean,probes): even hook-power moment ratio, 2-slope isoformal dim, zero-residual LP duality gap, even-shift DT family, and spectral residue isolation (qou-2fdj, qou-dk8a, qou-fr4d, qou-nmpr, qou-rdg8) — Lean modules consolidated via Group 8 (#8761 -> #9191).
- **`#8193`** (`feat/round53-wpdb-staircase-route89-stargram-43c1`) -> Parent **`#9189`** [CLOSED (parent MERGED)]: feat(lean,qbeta,hecke): formalize wpdb, qou-4qno, qou-8v3k, qou-b7cy, qou-018h + 80-dps witness — Route 8/9 FiveTwoCyclotomicBloch identities consolidated via #9151 -> #9189.
- **`#8153`** (`claude/round47-xbl8-depth1`) -> Parent **`#9191`** [CLOSED (parent MERGED)]: feat(lean,computations): derive Xbot tail-lemma per-row bracket bound and D1/D3/D4/D5 depth-1 hook classification (qou-xbl8, qou-ckyw, qou-x3u6, qou-q621, qou-amf8, qou-g937) — Lean modules consolidated via Group 8 (#8761 -> #9191).
