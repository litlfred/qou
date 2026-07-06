# Q_β / precision thread — workplan (2026-06-09 post-week review)

**Author away ~1 week from 2026-06-09.** This workplan situates the
merged Q_β c_k/d_k thread (#1479, #1574) inside the cross-thread state
after ~2480 commits landed in a week, and sets the prioritized queue for
when this thread resumes. Companion to the broad
[`2026-06-09-session-handover.md`](../handover/2026-06-09-session-handover.md)
(surreal/bib thread) and
[`2026-06-09-qou-lean-v424-repair-and-cache.md`](../handover/2026-06-09-qou-lean-v424-repair-and-cache.md)
(Lean repair).

## 1. Cross-thread state (where this thread sits)

| Thread | Status (2026-06-09) | Open PRs |
|--------|---------------------|----------|
| **α_EM** | Habiro element merged (#1511); #1521 IDs it as the **fundamental-rep closed fermion loop (unknot), NOT an H₃ Hecke word**; RT shadow-world Phases 1–4 scaffolded (#1527/#1538/#1549/#1552); #1503 closes subgoal-1 to the CAL-2 floor. Rigorous RT 2-loop (subgoal-2) is multi-week and dormant. | #1480 #1477 #1484 #1503 #1505 #1508 #1521 #1523 #1527 #1538 #1549 #1552 #1495 |
| **GAP-A-4 / Δ_λ binding** | Active probe sweep T9–T18. **T18 closes the within-H₃ categorical chain** for χ^λ(β_Bor) (Borromean per-irrep characters confirmed to 1e-50). But the **Δ_λ gate is still open** — six closure ansätze (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel/Frobenius, crystal-graph, augmented Markov) all fail at the deuteron. A≥3 binding is fully derived to **−13%** (uniform bond under-strength). Single win this week: magic-A ⁴He wireup (#1778 merged, 13.5× on ⁴He). **2026-06-09 retraction (main commit `d7f9749470`):** the earlier-cited "Option E v9 mirror-pair CLOSED to 0.11%" win was RETRACTED as a CAL-4 (fourth-calibration discipline violation); the bond-sum direction is the new open lead. | #1778 #1789 #1784 #1808 #1933 #1765 #1742 |
| **Lean v4.24.0 repair** | Substantially closed (#2001 merged, 29 commits). Module-green for the 6 red modules (λ→lam, maxRecDepth, division-free restates). Whole-library `lake build QOU` gate is post-merge CI (Mathlib `cache get` 403 blocks local full build). ~215 `sorry` in `BringShellBinding` (Ref-cited). | — |
| **My Q_β thread** | **#1479 + #1574 merged.** Two-tier cal-anchored cache + §3b-cond bridge classes + 9-block paper cleanup + `canonical-no-negative-result-in-paper` checker (live on main). Bridge still open; Q_β floor 1279 ppb. | — |
| **Surreal/bib + organic-chem** | Separate streams. #2024/#2011 ready-to-merge (author authorized `/prepare-merge` 2026-06-09, was rate-limited). #2014/#2003/#2013 working organic. | #2024 #2011 #2014 #2003 #2013 |

## 2. What changed *for this thread* this week

1. **α_EM #1521 is a directly transferable bridge hint.** The α_EM
   resolution found the Habiro element `[2]_q·(1−h²α)` is the
   **fundamental-rep (SU_q(2), N=2) closed fermion-loop unknot** —
   explicitly NOT any H₃ Hecke word (#1466 proved H₃ candidates
   insufficient). This independently confirms the Q_β bridge-narrowing
   verdict ([`2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md)):
   the per-block H₃ route was ruled out (mechanisms #5–6). The α_EM
   thread's positive resolution says **look at a simpler/other rep, not
   the H₃ block decomposition** — the same direction my KR/KLR scoping
   ([`2026-05-31-qbeta-bridge-kr-klr-scoping.md`](2026-05-31-qbeta-bridge-kr-klr-scoping.md))
   pointed at the link-Markov-closure level.

2. **L1 precision floor is 1 ppb, not 1 ppQ.** `markov_peel`'s fast
   path casts to float64 (`cf, df = float(c), float(d)`), injecting
   ~2.7×10⁻¹⁶ noise. The L1 "1 ppQ" goal is not actually met at the
   compute level until peel routes through exact-mpf. Concrete,
   deferred-not-blocked.

3. **Q_β prediction unchanged at 1279 ppb.** The Habiro-precision-ladder
   Lean work this week moved Q_β *certainty* (exact M=8 Habiro
   evaluation, no truncation) but not the *prediction error* — the
   ladder rungs were artifacts of the derivation, not the observable.
   The c_k tier vocab (`derived`/`cal-anchored`) and the truncation-order
   reporting vocab (`proved`/`near-match`/`fitted`,
   [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md))
   are reconciled and now canonical (AGENTS.md red-banner).

4. **m_μ is at 210 ppb (≈9.5σ tension), not ~0.** This is the honest
   post-canonical-pin state (confirmed: borromean witness at m_p-pin q₀
   predicts m_μ=105.65839781 vs CODATA 105.6583755). Dashboard 3/7.

## 3. Prioritized queue (this thread, when it resumes)

1. **[cheap, decisive — ~1 day] Q_β bridge experiment #3.**
   Run the multi-block eigenphase test from
   [`2026-05-31-qbeta-bridge-kr-klr-scoping.md`](2026-05-31-qbeta-bridge-kr-klr-scoping.md)
   §"cheap intermediate experiments", **now informed by #1521's
   fundamental-rep lesson**: test whether the Q_β eigenphase closes when
   the matter content is taken in the fundamental rep (à la α_EM's
   unknot) rather than the H₃ block sum. Pass (q₀-stable, Taylor-exact)
   ⟹ commit to formalisation; fail (q₀-drift) ⟹ bridge ruled out by the
   same criterion as mechanisms 1–6, and Q_β is documented as
   floor-limited with finality.

2. **[concrete precision win] L1 1 ppb → 1 ppQ.** Route `markov_peel`'s
   fast path through exact-mpf (drop the `float(c), float(d)` cast).
   Verify L1 cross-method agreement tightens below 1 ppQ on the 8-atom
   Layer-2 cross-check. This is a real L1-leg win independent of the
   open bridge.

3. **[coordinate] #1839 (cleaner-c_k re-run) + #1521 (Habiro element).**
   Both are bridge-adjacent and bridge-relevant. Post the §3b-cond
   cal-anchored pattern handoff if not already consumed; pull any
   cleaner-c_k findings that sharpen the bridge experiment.

4. **[watcher follow-up] verify `canonical-no-negative-result-in-paper`
   catches new offenders.** Run `qa-sweep --only
   canonical-no-negative-result-in-paper` across the full paper (not
   just mass-theory) and triage any blocks authored this week that trip
   it — the 270-commit binding probe sweep likely added falsified-probe
   blocks that should move to `docs/audits/`.

## 4. Highest-value lever (flag — owned by the binding thread)

The survey identifies the **A≥3 binding joint-trace correlation**
(−13% uniform bond under-strength) as the *only* gap closable at the
100× standard without owner-declined work. It is owned by GAP-A-4 /
#1778 / #1789 / #1784, not this thread. If this thread wants the highest
precision payoff, the move is to **join GAP-A-4** rather than push the
Q_β bridge (research-grade, skeptical odds). Decision deferred to the
author.

## 5. Out of scope (owner declined / deferred)

- **q₀ substrate-derivation** (Subgoal-2) — declined 2026-05-08. Absolute
  L2 targets (<ppt for m_p/m_n/⁴He) are out of scope.
- **Upper-q regime** (golden-ratio λ→φ² candidate) — deferred to a
  follow-up branch per
  [`2026-06-08-q-regime-map-coordination.md`](2026-06-08-q-regime-map-coordination.md).
- **The α_EM rigorous RT 2-loop** (subgoal-2) — multi-week, owned by the
  α_EM thread, dormant.

## 6. Cross-thread immediate (not this thread, flagged for visibility)

Per [`2026-06-09-session-handover.md`](../handover/2026-06-09-session-handover.md),
the surreal/bib thread has #2024 + #2011 ready-to-merge with standing
author authorization (was GitHub-rate-limited). That is the *continuing
surreal/bib agent's* action, not this thread's — flagged here only so a
resuming agent doesn't lose it.
