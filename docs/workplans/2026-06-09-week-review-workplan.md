# Week-review workplan (2026-06-09)

**Trigger:** owner — "lots of work in a week; update workplan after reviewing
`main` + siblings for relevant commits and overall strategy."
**Reviewed:** ~2481 commits on `origin/main` (2026-06-02 → 06-08) + 51 open PRs.
**Supersedes the planning portion of**
[`2026-05-27-next-session-workplan.md`](2026-05-27-next-session-workplan.md).

## 0. Headline finding — heavy drift + a structural reorg

`main` moved **+2481 commits in 7 days** and underwent a **"phase 6: substrate/"
reorganisation** (compute modules relocated under `substrate/` with root-script
shims). Consequence: **any branch cut before ~2026-06-02 is structurally stale.**
In particular the in-flight q₀-regen sweep branch (`q0-regen-batch-cont`) is
**2974 commits behind** and operating on the pre-reorg file layout — it is
**superseded** and has been stopped (see §2). New work must branch off current
`main` and assume the `substrate/` layout.

## 1. What landed on main (past week)

Commit-type histogram (top): **qa 1114**, review 211, fix 173, probe 88,
audit 75, **lean 72**, docs 69, content 45, chore 44, scope 37, coord 30,
**witness 24**, feat 22, **compute 22**, phase 21, scaffold 17.

Reading: the week was **corpus-wide QA / voice / review drain heavy**
(qa+review+fix ≈ 60% of commits) layered over steady substantive progress in
α_EM, lean, witness infra, and the substrate reorg. Witness/staleness infra was
itself heavily reworked — staleness-gate fixes (#2011, #1774), SHA-based
staleness for lean diagnostics, and repeated "regenerate … at canonical
proton-pinned q₀" commits (the backlog is being drained on `main` directly).

## 2. This session's contributions + current status

| PR | What | Status now |
|----|------|------------|
| #1500 | q₀-staleness **detector** | merged; since **relocated** by the substrate reorg |
| #1501 | Tier 1.B orbit-reduction (illusory `|orbit|` multiplier retired) | merged |
| #1504 / #1550 | q₀-repin regen **checkpoints** (driver + 13 + 98 isotope shards) | merged |
| #1522 | Tier 1.B intermediate-state **memoisation** — RESOLVED (already in-Rust, capped ~1.08×) | merged |
| #1563 | **q₀-aware `_is_stale`** → re-pins self-heal via the existing auto-refresh (warn, never fails publish) | **merged + present on current main** ✓ |
| #1535 | q₀-regen sweep continuation | **SUPERSEDED** — 2974 behind + pre-reorg layout; nurse stopped; recommend **close** |
| #1558 | Tier 1.B Lean scaffold (Lemma 1 + interface-minimality, cited `sorry`s) | **draft**; verify path survives the reorg, then validate (§5 P4) |

**Net:** the stale-witness *prevention* (#1563) shipped and is live; the manual
*remediation* sweep (#1535) is now redundant because `main` drains the backlog
directly (sibling regen + the #1563 auto-refresh).

## 3. Sibling-PR landscape (51 open)

| Thread | ~PRs | Status |
|--------|------|--------|
| **α_EM derivation** | 14 — #1484 (0.31 ppb fixed-point), #1487/#1463/#1527/#1538/#1549/#1552 (RT 2-loop phases 1–4), #1508 (Lean conditional), #1495 (ledger) | **converging**, phased, coordinated — effort centre |
| **Precision L1/L2** | 5 — #1762 (master roadmap), #1768 (Option-E 6/6 negative), #1765 (Habiro λ(K)), #1808 (H₃→H₄), #1556 (m_μ shared-root) | methodical option-tree |
| **Witness / q₀ infra** | 3 — #1535 (superseded, §2), #1878 (drift audit), #1767 (engineVersion docs) | mostly absorbed into main |
| **Tier 1.B / Hecke** | 2 — #1558 (Lean draft), #1569 (avg-crossing identity) | sparse, low urgency |
| **Q_β / calibration** | 2 — #1742 (negative), #1741 (native chi-cache, unblocks ⁴He regen) | infra + negatives |
| **Lean** | 4 — #1562 (last sorry, near done), #1990 (rank-monotonicity), #1508, #1558 | incremental |
| **QA / probes / infra** | ~21 — **#1933 T17 first categorical χ^(2,1)**, #1975 T4–T12 refutation, QA drains #1918/#1941/#2006, voice #1976, skills #2008 | steady-state maintenance |

## 4. Strategy assessment

1. **α_EM is the critical path** — 14 coordinated PRs; empirical inverse locked
   at **0.31 ppb**; RT 2-loop structural derivation staged (Phase 1 done). This
   is the closest headline result. Protect the cluster's coordination (#1495).
2. **T17 (#1933) is the week's standout** — first *categorical* χ derivation
   (Schur-Weyl R-matrix), a genuine derivation vs. fit; unblocks GAP-A paths.
3. **Witness infra is now self-healing** — #1563 prevention on main + active
   staleness-gate work means re-pins no longer silently accumulate. The manual
   sweep is retired.
4. **Precision L1/L2 = disciplined option-elimination** — negatives (#1768
   Option-E 6/6) are progress. #1762 is authoritative.
5. **Lean is not the critical path** — incremental sorry-clearing (#1562 close).
6. **Churn flag:** 51 open PRs + 1114 qa-commits/week is heavy maintenance
   overhead. A PR-consolidation pass would cut review noise.

## 5. Prioritised next steps

**P0 — close the loop on superseded session work.**
- **Close #1535** (2974 behind + pre-reorg; backlog drained on main). Nurse stopped.
- Re-base **#1558** onto current `main` (substrate layout); confirm
  `QOU.BraidKnot.InterfaceComposition` path; then proceed to P4.

**P1 — α_EM critical path (highest leverage).** Keep the RT 2-loop phases
(#1538/#1549/#1552) unblocked; coordinate via #1495; do not fork the cluster.

**P2 — precision option-tree.** Continue past the Option-E negative (#1768) on
the #1762 roadmap; #1556 routes m_μ to the shared Q_β/m_n/Δm_pn root.

**P3 — witness-infra hardening (small, durable).** #1563 follow-up: make
`_is_stale` cover **multi-shard** producers (it checks one witness/producer
today) — re-target to the post-reorg `substrate/` path.

**P4 — Lean validation backlog.** Discharge #1558's 3 `sorry`s and #1562's last
`sorry` (needs a Lean-toolchain session: `lake` not installed in compute
sessions).

**P5 — PR consolidation.** Triage the 51 open PRs; close stalled/superseded
drafts (#650 q-CLT scope-conflict, #411 infra, refuted probes) to cut churn.

## 6. Loose ends / irreducible witness floor (from the drain probe)

- `snappy_cusp_seeding` — `ModuleNotFoundError: snappy` (install SnapPy in CI or accept as un-regenerable here).
- **`sigma_all_evaluator` — real `6.76e-7` closed-form mismatch** (asserts `< 1e-14`); not a dep — a genuine discrepancy to investigate (possible q₀-sensitivity). **File under P3.**
- `>240 s` heavy producers (canonical-mass-table-extended, A-operator extracts) — need a dedicated long-timeout run, not the per-PR batch.
- 15 manual no-`scriptFile` witnesses — owner triage.
