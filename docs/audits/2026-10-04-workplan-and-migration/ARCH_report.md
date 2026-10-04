# ARCH — how work is coordinated across the qou store (branches, duplicates, parent graph, churn, open PRs)

This was read-only. Nothing was deleted, nothing was written to `/home/user/qou`, and no `beans` writes were made.
Data: `origin/main` at `348e299` (2026-10-03), 6,480 remote branches, 5,371 beans, and 49 open PRs (`open_prs.txt` says 50, but it lists 49 and the REST API returns 49).
Side files in the scratchpad: `branch_status_arch.tsv` (one row per branch, with its disposition) and `arch/*.json`.

## 1. Branch census [M]

Method: one `git log --remotes --not origin/main` pass (22,461 commits that are not on main). For each branch I walked its own commits that are not on main. A branch counts as "landed-by-cherry" when the subject of every non-merge commit (with `(#N)` stripped) also appears on main. For every commit that is still unlanded (4,644 of them) I fetched the list of changed files.

| class | branches |
|---|---|
| ancestor of main (merged) | 1,395 (+1 with merge commits only) |
| landed by cherry-pick or rebase (matched on subject) | 4,398 |
| partial: some commits landed, some did not | 167 |
| unlanded | 518 |
| open-PR heads (excluded from what follows) | 49 |

Age of the 685 partial or unlanded branches: 543 are 60 days or older, 95 are 30–60 days, 45 are 7–30 days, and 2 are under 7 days.
**637 of these are orphaned**, meaning they have no open PR. 263 of the orphans carry just 1 commit that is not on main, and 94 carry 10 or more.

The owner's rule is applied: an unlanded diff that touches math or physics content is never a delete candidate. Disposition of all 6,480 branches:

| disposition | n | basis |
|---|---|---|
| **salvage-review (content not on main)** | **461** | touches `.lean`, `content/`, `folio/`, `papers/`, witnesses, `computations/`, `library/`, `uploads/`, `.tex`, `qou-mass/`. 174 of them touch `.lean`. 406 are 60 days or older |
| infra-review | 68 | only scripts, tools or config |
| delete-candidate: beans, docs or memory only | 76 | every unlanded file is under `beans/`, `.beans/`, `docs/`, agent memory or `todos/` |
| delete-candidate: empty diff | 32 | |
| delete-candidate: merged | 1,396 | |
| delete-candidate: cherry, high confidence | 4,200 | every subject is unique on main |
| delete-candidate: cherry, **low confidence** | 198 | at least one subject is generic and appears 3 or more times on main (for example "post-rebase drift refresh" ×238, "review 5 more blocks" ×220) |

**Caveat:** "landed-by-cherry" compares subjects, not diffs. An upper bound on what could be deleted is **5,704 branches (merged + cherry + docs-only + empty)**. Only the merged 1,396 are certain. The 198 low-confidence ones should be read as salvage-review. All of this is a report for the owner; no action was taken.

Topics of the orphaned work (coarse keyword buckets over branch name plus tip subject):

| topic | branches |
|---|---|
| L2 mass/binding (Δλ, Q_β, α, deuteron, 4π) | 139 |
| exposition drain (Milnor, clarity, rhetorical, batch) | 130 |
| Lean/Mathlib | 88 |
| other | 84 |
| precision/witness | 59 |
| work-plan/handover | 50 |
| review-response | 28 |
| copilot/* | 26 |
| lake-cache/backup | 16 |
| conjectures | 8 |
| SM | 6 |
| library | 3 |

The most common tip-subject tokens are chore, lean, review, audit, witness, drain, beans, batch, gemini and copilot.

## 2. Duplicate work [M]

Title near-duplicates are **rare once templated families are excluded**. Among non-template titles, token Jaccard ≥ 0.6 gives only 15 pairs; dropping the threshold to 0.45 gives 49 pairs.

The raw Jaccard clusters are dominated by templates that are *not* duplicates:
- "Conjecture carrier: X": 28 beans
- "PROVE(lean): instance/file"
- `Cite` / `Add reference for` / `Remark interpreting` / `Cross-check X at Y`: 464 beans, 301 of them open

`Cite` and `Add reference` are **distinct steps by design**: qou-fc7k's body says so and leaves the 81 `Cite` siblings open on purpose. They are not duplicates.

The real duplication is **structural, between two families**: 15 Lean classes each have both a §3b `Conjecture carrier` bean (under `b9cj`) and a `PROVE(lean): instance:` bean (under `qou-k1mq`).

The top clusters, with the proposed survivor first (all are in the TSV):

1–15. **Carrier ↔ instance**: qou-r3vt, 9595, 4z73, lmr1, 16ph, p4c4, 78xv, 3opz, puqo, fsqp, ylxw, xt9z, 93fi, ap4g, 50gf → each is a dup of its `cj*` carrier.
   - **Flag:** qou-lmr1, "instance: ClassicalRiemannHypothesis", amounts to a task to prove RH. It must stay an open-conjecture carrier.
   - **Flag:** qou-ap4g, TorusKnotMass, is a mass carrier. Check that no empirical mass value enters the class statement.

16. **Twin milestone** `qou-c8p8` ← `qou-vkmt`: same title, same day, both in-progress, 8 and 13 children. 5 of vkmt's children duplicate c8p8's: nkzs→gzgi (done), nntw→f6bb, h8rx→7crn, qk5b→z4jb, 5rr4→yc05.
17. qou-ty08 → qou-r3vt (identical title).
18. qou-0xmm → 9552 (done).
19. qou-uts1 → ml55 (done).
20. qou-1lh4 → rcgi (done).
21. qou-v266 → 1fv0 (done, names v266).
22. qou-ii3w → csdp.
23. qou-dqhd → 4pmk (same float64 regression).
24. qou-cr3v → scrx (scratch_*.lean collisions).
25. qou-7aum → 2r42 (witness provenance at 55).
26. qou-c0yc → 07vh (NF q-degree).
27. qou-50a7 → j1bs.
28. qou-ntef → 4iy0.
29. qou-1tne → tcre (done, superset); qou-oifd → tcfb (done).
30. qou-tsnp ↔ qou-hprp ("12" vs "23" carriers that assert nothing): **needs-owner**, low confidence.

Duplicate effort is better measured from the agents' own admissions than from titles:
- **104 main commit subjects** say a sibling had already landed the work, it was prior art, or it was "already a corpus theorem". This peaks in W35–W37 (30, 24 and 18 per week).
- 24 subjects admit duplicating or redoing work, and 71 are takeover or salvage commits.
- In bean bodies: 436 mention "sibling landed" or prior art, 94 mention takeover, and 59 mention duplication.
- 96 beans have takeover, stalled or pickup titles (56 completed, 39 open). They peaked in W29–W33.

Hotspots where several beans point at one object. These are convergence points rather than duplicates; each should become *one* story:
- Lean `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`: **12 open beans**. It is a convention-C object, so it belongs to the excision epic.
- `QOU.Hecke.IwahoriHecke`: 6 open beans.
- `QOU.HeckeAlgebra.MarkovTrace` and `QOU.Mathlib.RamifiedShiftCalculus`: 5 each.
- Blocks: `qdifference-kernel-prolongation-symbol` (19), `stokes-dt-bps-bridge` (16), `operator-selection-lp` (15), `q-geometric-langlands` (15).

## 3. Parent-graph health [M]

- Parent links: 1,003, with **0 dangling parents and 0 cycles**.
- Depth: 4,368 roots, 960 at depth 1, 32 at depth 2, 11 at depth 3. **2,050 of the 2,466 open beans have no parent.**
- Parent types include 34 tasks and 24 features acting as parents, besides epics and milestones.
- Epics and milestones: 402.
  - 270 have **no children**, and 96 of those are open. 204 of the 270 are titled Session, Handoff or Arc (46 of those open); they should be **demote-log**.
  - 6 are open but all their children are closed: qou-rgiz (owner-gated α_EM arc), qou-a3n3 (q-NS Gevrey; a body note says it stays open for GP2/GP3, so **keep**), qou-koce, qou-tonv and qou-0wj8 (sessions → close), and qcz15 (q-Collatz tier C).
- 38 open beans sit under **closed** parents. They are mostly under scrapped Session epics: qou-89f9 (8), qou-kk96 (7), qou-k42c (3), uudc (3). Reparent them.
- In-progress beans by month of last update: Jun 6, Jul 74, Aug 228, Sep 276, Oct 0. **567 of the 584 have had no update for more than 14 days**, and 86 have an empty body.
- Claim notes naming a branch ("claimed … on/by `claude/…`"): 42 notes on 40 beans. Only 1 of the branches is gone. The 41 others are 30 landed-by-cherry, 5 merged, 4 unlanded and 2 partial. Of the 19 in-progress beans that carry a claim note, most point at **landed** branches, so the claims are stale rather than orphaned.
- 157 in-progress beans mention some branch; 36 of those mentions point at branches that no longer exist.

Close evidence. Open beans whose closing commit is on main but whose status is still open:
- **6 with high or medium confidence**, where the bean was not touched after the closing commit: qou-0z7n, 40kk, 92u9, brg3, i7ju and b2ie (b2ie is m).
- **12 with low confidence**, where the bean was re-touched after the closing commit. Many were touched on 2026-09-08, the day of the owner rule-13a reopen sweep (`qou-7sin`, commit a61496d "reopen 18 beans whose own body says they are open"). Excluded on purpose: qou-oots (explicitly reopened) and qou-qexu (in the 7sin list).
- These go in the TSV as `close-evidence`.

## 4. Churn timeline [M] (ISO week: beans created / beans completed, by update week / PRs merged / commits on main)

| week | created | completed | PRs | commits |
|---|---|---|---|---|
| W21 | 0 | 0 | 239 | 1,980 |
| W26 | 253 | 185 | 30 | 1,478 |
| W29 | 411 | 259 | 77 | 1,415 |
| W31 | 453 | 147 | 5 | 956 |
| **W32** | **1,017** | 152 | 67 | 2,062 |
| W33 | 562 | 272 | 50 | 1,848 |
| W35 | 639 | 324 | **139** | **4,420** |
| W36 | 434 | 247 | 49 | 3,130 |
| W37 | 195 | 99 | 35 | 1,675 |
| W38 | 91 | 27 | 13 | 612 |
| W39 | 42 | 52 | 1 | 142 |
| W40 | 5 | 3 | 5 | 21 |

The full series is in the run log. Overall: 1,565 PR numbers were detected on main, across 38,954 main commits since 2026-03-12.

Bean creation outran completion in every week from W26 to W37. W32 alone created 1,017 beans, which was the bulk filing of the templated `Cite …` and `PROVE(lean) …` families. Activity has nearly stopped since W38.

## 5. The 49 open PRs

**34 of the 49 PRs touch pre-migration paths** (`.beans/` or `content/`). Those paths were moved by `58a1f32` (2026-09-26, `.beans/`→`beans/defs/`) and #7485 (2026-09-27, `content/`→`folio/`). None of the 34 can merge as they stand; each has to be **ported**. GitHub reports mergeability as unknown for 47 of the PRs and "dirty" for 2 (#5338, #5352).

Key:
- **MERGE** = current layout and small; review, then merge.
- **PORT** = re-apply the change on the new paths, then close the PR.
- **SALVAGE** = math or physics content that is not on main; it needs owner or reviewer judgement and must not be closed unread.
- **OWNER** = the decision is the owner's.

| PR | age | linked bean (status) | not-on-main commits | recommendation |
|---|---|---|---|---|
| 7482 | 7d | qou-306p (todo) | 1 | MERGE (beans only, new layout) |
| 7483 | 7d | — | 1 | MERGE (docs/audits) |
| 7477 | 7d | — | 10 | MERGE after review (precision triage, new layout) |
| 7401 | 20d (updated 4d ago) | — | 10 | MERGE after review (pole-to-cusp, folio/) |
| 7453 | 10d | — | 2 | MERGE (blueprint import, new files) |
| **7418** | 19d | qou-ales | 8 | **PRIORITY**: main's audit (qou-ales) already cites "#7418 discharge MACHINE-CHECKED", but the commits are not on main. Main depends on an unmerged result. PORT and merge. |
| 7481 | 7d | — | 10 | SALVAGE→PORT (TL/Hecke arc, 18 content files) |
| 7443 / 7440 | 15d | qou-oiz3 (in-progress) | 5 / 3 | 7443 is OWNER (global `_DPS_DEFAULT` 50→70). 7440 (staging measurement) is superseded by 7443; close it after 7443 lands |
| 7441 | 15d | qou-pdix (in-progress) | 2 | PORT (small sorry-free Lean) |
| 7136 | 27d | qou-kwoa (in-progress) | 17 | SALVAGE (Lean Geck–Pfeiffer, partly landed) |
| 6681 D | 30d | §3b-cond | 37 | SALVAGE (8 conjecture classes adjudicated; P2) |
| 7180 | 23d | qou-c98z | 3 | PORT (187 conjecture classes with no instance; evidence for the P2 umbrella) |
| 7170 | 26d | qou-bstl (todo) | 48 | PORT: it touches 45 beans and its 18 closes **never reached main** |
| 7318 | 21d | 17 beans | 47 | SALVAGE (precision; overlaps 7443) |
| 6178 | 35d | — | 22 | OWNER (AME→registry, 93 content files; the 2026-09-30 m_n AME-2020 ruling may supersede it) |
| 7205 | 22d | CAL-2 | 5 | OWNER (AME-2020→CODATA-2022 dataset; same ruling) |
| 6342, 6361, 7123 | 27–34d | qou-cds1 (in-progress) | 12 / 2 / 3 | SALVAGE into the Q_β-under-D epic |
| 6358, 7216, 7407 | 20–34d | qou-brng (in-progress) | 2 / 5 / 2 | SALVAGE into the binding-term epic |
| 7218 | 22d | qou-gba1 (in-progress) / za3q (done) | 7 | SALVAGE (Ω₂ pairing forced at z_D) |
| 7225 D | 22d | qou-ix0x | 2 | SALVAGE (Habiro ring-hom question) |
| 7229 | 22d | qou-sv7h | 5 | SALVAGE→PORT |
| 7419 | 19d | — | 5 | SALVAGE (Xbot bound, 9.6× loose) |
| 6359 | 34d | — | 2 | SALVAGE (Milnor-defined triples trivial) |
| 5402 | 44d | qou-j4mn (todo) | 3 | SALVAGE (min degree 7 is a convention-C artefact) |
| 5352 | 44d | tl-arc | 3 | SALVAGE; likely superseded by #7481. Dirty |
| 6350 | 34d | L2 option 3 | 1 | PORT |
| 6307 | 35d | — | 3 | PORT (perf 240 s→0.024 s; check output equality) |
| 5861 | 39d | — | 3 | PORT (barrett1993 citation) |
| 7146 | 27d | qou-qspu | 1 | MERGE after review (library ingest; `library/` path unchanged) |
| 7439 | 15d | — | 6 | PORT the remainder (partly landed) |
| 7402, 7406 | 20d | qou-oots, qou-5jqv | 2 / 1 | PORT |
| 5338, 6357, 7210, 7392 | 20–46d | vy77, vbyi, vyvt, a3qo | 1 each | PORT the bean edit (beans only), then close |
| 6025 | 36d | — | 0 | Superseded (landed-by-cherry; main cites it), so close |
| 6878 D | 29d | — | 4 | Probably superseded (witness race); close after reading |
| 4845 D, 5330 D | 46–56d | stale-PR triage | 1 each | SALVAGE the 1–2 content files, then close |
| 7435 | 18d | — | 2 | MERGE or close (agent memory only) |
| 7484 | 7d | qou-8321 (done) / utbr | 5 | OWNER: it deletes `folio.config.json`, which main still carries |
| 7451, 7494 D | 2–11d | — | 1 | OWNER (removes or moves upload PDFs) |

## Owner decisions needed

1. Approve the branch-deletion tiers. The merged 1,396 are certain. The cherry 4,200 rest on subject matching. Never the 461 salvage-review branches.
2. #7418, because main already depends on it.
3. AME vs CODATA (#6178, #7205).
4. Global dps change (#7443).
5. qou-tsnp vs qou-hprp.
6. The carrier-vs-instance policy: one bean per Lean class.
7. Whether "PROVE instance: ClassicalRiemannHypothesis" should exist at all as a task.

## Skill gaps

- **No branch-sweep skill.** Nothing classifies a branch as landed by subject versus content and checks it against the owner's no-delete-content rule. I had to build it by hand, and on a treeless clone the file lists cost about 1 s per commit.
- **No layout-migration PR porter.** Every PR opened before 09-26 now targets dead paths, and nothing flags this.
- **No duplicate guard at `beans create` that knows template families.** Within families it raises false positives; across families (carrier vs PROVE instance) it misses the real duplicates.
- **No "close-evidence" reconciler** that matches `close(qou-x)` commits on main against the bean's status while respecting rule-13a reopens.
- **No stale-claim sweeper.** 567 in-progress beans have gone more than 14 days without an update.
