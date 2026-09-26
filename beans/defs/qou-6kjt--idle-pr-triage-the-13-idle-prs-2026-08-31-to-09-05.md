---
# qou-6kjt
title: 'IDLE-PR TRIAGE: the 13 idle PRs (2026-08-31 to 09-05) the shallow clone could not merge-test — deepen, measure cleanliness, classify merge-ready vs needs-work'
status: completed
type: task
priority: normal
created_at: 2026-09-07T18:16:49Z
updated_at: 2026-09-07T18:26:27Z
parent: qou-6g7j
---

19 open PRs are idle > 3 h. Four were measured CLEAN (bean above), #7005 and #7093 are being extended. The remaining 13 had NO merge base in the shallow agent clone (git merge-tree could not run): #6359 #6878 #6758 #6807 #6853 #6816 #6804 #6818 #6681 #6744 #6342 #6361 #6353. Task: deepen the fetch (git fetch --deepen or --unshallow on origin/main + each head), run merge-tree, read each PR body's own verification claims, and classify: (i) clean + self-verified → merge-ready list for the owner, (ii) conflicts → name the files, (iii) red/unverified → what is missing. Do not merge; report as a numbered list the owner can pick from.

## Idle-PR triage — 13 PRs, measured 2026-09-07 ~18:30Z (bean `qou-6kjt`)

**Method.** Worktree clone deepened (`origin/main` 6 698 → 16 990 commits, shallow boundaries 37 → 5; head at `811839a3b`) until every PR had a genuine merge base; each head fetched at depth 60; verdict = `merge-tree --write-tree origin/main <head>`. Changed-file counts against the merge base match each PR's own `changed_files`, which is the check that the bases are real (a first pass through the shallow holes produced a false base for #6816/#6804/#6818 with 78/90/62 phantom files — discarded). `get_reviews` is empty on all 13; comments are sibling coordination only. Nothing was merged, commented on, or pushed on any of the 13. **Age** = time since the head commit; **behind** = main commits since the merge base.

| # | PR | title | age | behind | class | reason |
|---|---|---|---|---|---|---|
| 1 | #6853 | Frame the promotion instead of starting it — three shapes | 2.0 d | 1195 | **A** | CLEAN. Docs-only (1 audit doc). No Lean / compute / content touched; body claims render-QA clean. Nothing to re-run. |
| 2 | #6816 | Close the pass-2 blind spot: tolerance passed as a variable | 2.4 d | 1350 | **A** | CLEAN. 1 audit script + bean; body claims `tolerance_guard_bypass_audit --strict` + `--selftest` + `witness_raw_float64_audit --strict` all exit 0; no witness changed. |
| 3 | #6353 | L2 option 1: the Q_β k=3 spec — `c_3 = −2` fails it by 5.5× | 7.6 d | 3673 | **B** | CLEAN. Single new probe (`qbeta_k3_rung_spec_and_candidate_test_probe.py`, 6/6 claimed, no witness). Body does not say `precision-gates.sh --changed` ran → run it (probes are not exempt). |
| 4 | #6804 | beans: eight normal-priority beans closed on measurement | 2.4 d | 1350 | **B** | CLEAN. 13 files: 10 beans + 1 harness + 2 regenerated witnesses; body claims raw-float64 NEW 0 / REGRESSED 0. Re-run `precision-gates.sh --changed` on the final head (main moved 1350 commits since its rebase). |
| 5 | #6744 | perf(qou-i7ju): closed form replaces factorial SYT enumeration | 2.5 d | 1632 | **B** | CLEAN. `hecke_core_legacy.py` + `hadron_knot_table.py` + probe + witness; body claims 138/138 bit-identical but never names `precision-gates.sh` → run it. Note: #6807 edits the same file and conflicts; land this one first. |
| 6 | #6818 | obtuse assembly: the affine-chord null set | 2.4 d | 1358 | **B** | CLEAN. 1 new library `.lean` (`Archimedean/ObtuseTiling.lean`); lean-direct exit 0 claimed on a 2-day-old cache. Needs `scripts/lean-library-sweep.py` on the final head (the `descartesWtrace` precedent: exit 0 against a snapshot ≠ green against main). |
| 7 | #6758 | lean(qou-kwoa): Geck–Pfeiffer derived — τ, Gram det, Schur elements | 1.9 d | 1583 | **B** | CLEAN. 7 library `.lean` (62 decls, sorry-free claimed) + 1 exact probe + bean. Same as row 6: library sweep on the final head; probe claims float64-guard clean. |
| 8 | #6361 | qou-cds1: the negative (1³) weight is an INTERVAL fact | 7.6 d | 3645 | **C** | Conflict in **`.beans/qou-cds1…md` only** (mechanical). Also carries `QBeta/ConventionDAdmissibleRoots.lean` (auto-merged, but 7 days stale → library sweep after resolve) + 2 probes + 2 witnesses. |
| 9 | #6359 | Route 3 closed: Milnor-DEFINED triples are exactly the TRIVIAL ones | 7.6 d | 3627 | **C** | Conflict in **`.beans/qou-768r…md` only** (mechanical). Also 1 new library `.lean` (`Mass/MilnorDefinedTriplesVanish.lean`) + 2 probes, no witness → library sweep after resolve. |
| 10 | #6342 | qou-cds1 entries 9+15+16: the c_4 threshold, pinning sweep, gates | 7.6 d | 3664 | **C** | Conflicts: `.beans/qou-cds1…md` (mechanical) + `docs/audits/convention-c-comparison-ledger.json` (adjudication ledger — hand-check entries). **Open ask** (sibling comment 2026-08-31): renumber its bean entries 15/16 → 18/19 on rebase, since #6264 took those numbers on main. 4 witnesses + 4 probes → precision gates after resolve. |
| 11 | #6807 | fix(qou-sv7h): #6794's exactness stopped at the builder | 1.9 d | 1017 | **C** | **Logic conflict** in `computations/hecke_core_legacy.py` (plus `.beans/qou-sv7h…md` and `.claude/agent-memory/…/measurement-hygiene-traps.md`, mechanical). Same file as #6744; expect to re-resolve after #6744 lands. Then re-run `ysn_braid_relation_audit` + `precision-gates.sh --changed`. |
| 12 | #6878 | The witness on main raced a merge by 13 seconds — regenerate | 1.5 d | 863 | **D** | **Draft**; body says "still not authorised to merge". Conflict in the **generated** `docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` — regenerate with the producer, never hand-merge; sibling notes main's detector changed (#6699), so the witness must be re-run anyway. |
| 13 | #6681 | §3b-cond item 5: all eight adjudicated — two empty classes | 2.4 d | 1445 | **D** | **Draft**, 51 files. **Logic conflicts**: `AlgebraicSubstrate/MetallicLPIdentities.lean`, `IwahoriHecke/Tw.lean`, `sigma-shell-from-beta-chain-derivation.md` + `.qa.json`, plus `witness-raw-float64-audit.witness.json` and the generated vacuity-audit JSON (both regenerate). Needs content sweep + library sweep + validate + render-QA after resolve. |

**Summary.** 2 merge-ready (A), 5 clean-but-verify (B: 2 need a Lean sweep, 3 need `precision-gates.sh --changed`), 4 conflicting (C: 2 bean-only, 1 bean+ledger with an open renumbering ask, 1 logic), 2 drafts (D, both with logic/generated-file conflicts).

**Suggested order if picking:** rows 1–2 as-is; rows 3–7 after their named check on the final head; row 5 before row 11; rows 8–9 are one-file mechanical resolves.

**Caveats.** The "behind" counts are large because `main` takes ~1000 commits/day; a CLEAN merge-tree today can turn dirty within hours, so re-measure right before merging. All verification claims in the reason column are the PR bodies' own; none were re-run here.
