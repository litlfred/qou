# Dangling in-progress claims — proposal (2026-11-20)

**Propose-only.** No bean status was changed. Each batch below waits on the owner's approval, relayed by the coordinator. Machine-readable list: [`2026-11-20-dangling-claims-proposal.json`](2026-11-20-dangling-claims-proposal.json) (one row per bean, with verdict, reason, cited commits and PRs). Tracking beans: `qou-s6pv` (this finding), `qou-bstl` (stale-open beans), epic `qou-w3yy`.

## The decision

Session review decision **D1** (PR #8527) assumed 590 `in-progress` beans were claims nobody holds. **Measured, that is not what they are.** 558 of the 590 (and 947 of the 1,017 beans that match the same date filter) are named by one of **223 open PRs opened 2026-11-16..18** by a batch agent (branches `feat/round<N>-…`, `feat/qou-<ids>-roundN`, `cat/round<N>-…`; PR bodies list ~5 bean ids each). That agent appended progress notes to the beans on the beans branch without bumping `updated_at` (982 of the 1,017 files had a content change on `cat/cat-harness/beans` between 2026-11-15 and 2026-11-18), which is why a front-matter date filter reads them as abandoned.

So the bean status question for 95 % of the population **is the batch-PR question**: each bean should follow its PR — merged ⇒ completed (unless it is an open conjecture), closed ⇒ back to `todo`. Changing those statuses now, ahead of the PR decision, would put the tracker out of step with the PRs in the other direction.

What is decidable today is small: **3 DONE, 6 TODO, 8 CONJECTURE-OPEN** (never completed), 2 KEEP.

## Counts

| verdict | all 1,017 | the 590 of PR #8527 | proposed action |
|---|---:|---:|---|
| DONE | 3 | 3 | `in-progress → completed`, commit cited |
| TODO | 6 | 6 | `in-progress → todo` (body unchanged) |
| CONJECTURE-OPEN | 8 | 4 | never `completed` (AGENTS.md 13a); `→ todo` allowed, as an unclaimed open problem |
| KEEP | 2 | 0 | leave |
| LIVE-WS | 47 | 17 | leave — under live fronts `qou-6qbv` (W8, 43) and `qou-c8p8` (W10, 4) |
| PR-PENDING-OLDER | 4 | 2 | leave until PR #8082 is decided |
| PR-PENDING-BATCH | 947 | 558 | status follows the batch PR; nothing to do until the PR outcome |

Of the 947 batch-held beans: **319 must never be auto-completed** even if their PR merges (`never_complete: true` — under the open-conjectures umbrella `b9cj`, or titled as a conjecture / GAP). **393** are named in a PR body but their own bean body does not record that PR (`bean_body_records_pr: false`), so the bean alone does not tell the next agent a PR exists.

Population: status `in-progress` and front-matter `updated_at` < 2026-11-13 on the mounted tree (5,781 beans). The PR #8527 figure of 590 is the subset tied to a session id; the 427 others are the same kind of bean.

## Batches for approval

- **Batch A — DONE (3):** `qou-4tui`, `qou-58w3`, `qou-byzu`. Each has a work commit that is an ancestor of `origin/main` (checked with `git merge-base --is-ancestor`).
- **Batch B — TODO (6):** `qou-p6tm`, `qou-533l`, `qou-ocof`, `qou-0ueg`, `qou-lpio`, `qou-vo9t`. All belong to sessions that ended; the bodies keep their progress notes.
- **Batch C — CONJECTURE-OPEN → todo (8):** `cj7c`, `cj52`, `cj05`, `cj8c`, `hypr`, `qou-0xk8`, `qou-bvxd`, `qou-m535`. Status `todo` marks them unclaimed; never `completed`. Two of them (`hypr`, `cj8c`) already carry a *"Claim reset 2026-10-04"* note whose status change never happened.
- **Batch D — batch-held (947):** no status change now. Recommended rule (my judgement): when the batch-PR workstream decides a PR, the same change sets the PR's beans — merged ⇒ `completed` except `never_complete` rows, which stay open; closed unmerged ⇒ `todo`. The JSON gives the PR → bean map.

## What each batch means (six-part frame)

**Batch A–C (17 beans).** *Means:* 17 status lines change; bodies untouched. *Costs:* one beans-branch push. *Risks:* a wrong DONE hides open work — guarded by citing a main commit for each; the conjecture rows are never completed. Fully reversible (one line per bean). *Commits to:* nothing beyond these 17. *Default if nobody answers:* nothing changes. *Recommendation (judgement):* approve A–C together.

**Batch D (947 beans).** *Means:* bean status is tied to the batch-PR outcome instead of being edited now. *Costs:* nothing now; later, one bean edit per decided PR. *Risks:* if the batch PRs stay undecided, 947 beans stay `in-progress`, so "in-progress" still carries little information. *Commits to:* the merge/close of a batch PR also settles its beans. *Default:* nothing changes. *Recommendation (judgement):* adopt the rule; it adds no work today.

## Per milestone / epic

| milestone | epic | verdicts |
|---|---|---|
| `qou-5vkl` | `qou-5vkl` | TODO 1, PR-PENDING-BATCH 167 |
| `qou-10v9` | `qou-v2om` | PR-PENDING-BATCH 164 |
| `qou-lpep` | `qou-mub3` | PR-PENDING-BATCH 91 |
| `qou-0uga` | `qou-8lxd` | PR-PENDING-BATCH 90 |
| `qou-lpep` | `qou-1qhv` | PR-PENDING-BATCH 58 |
| `qou-rtxm` | `qou-6qbv` | LIVE-WS 43 |
| `qou-10v9` | `qou-9nnz` | PR-PENDING-OLDER 2, PR-PENDING-BATCH 38 |
| `qou-10v9` | `qou-10v9` | PR-PENDING-BATCH 39 |
| `b9cj` | `qou-frzo` | PR-PENDING-BATCH 32 |
| `b9cj` | `qou-n4nr` | PR-PENDING-BATCH 29 |
| `b9cj` | `b9cj` | PR-PENDING-BATCH 26 |
| `qou-10v9` | `qou-cdx1` | DONE 2, PR-PENDING-BATCH 22 |
| `b9cj` | `qou-r9ih` | PR-PENDING-BATCH 24 |
| `qou-5vkl` | `qou-trd0` | PR-PENDING-BATCH 21 |
| `b9cj` | `qou-5p7n` | PR-PENDING-BATCH 15 |
| `b9cj` | `qou-m6dn` | PR-PENDING-BATCH 13 |
| `qou-0uga` | `qou-ddmn` | PR-PENDING-BATCH 13 |
| `qou-rtxm` | `qou-rtxm` | KEEP 1, PR-PENDING-BATCH 11 |
| `qou-10v9` | `qou-2002` | PR-PENDING-OLDER 2, PR-PENDING-BATCH 10 |
| `qou-10v9` | `qou-wp3h` | PR-PENDING-BATCH 12 |
| `qou-lpep` | `qou-q4oa` | PR-PENDING-BATCH 12 |
| `qou-vo9t` | `qou-vo9t` | DONE 1, TODO 4, CONJECTURE-OPEN 3 |
| `qou-10v9` | `qou-avtq` | KEEP 1, PR-PENDING-BATCH 6 |
| `b9cj` | `c7vs` | PR-PENDING-BATCH 6 |
| `qou-d8c7` | `qou-d8c7` | PR-PENDING-BATCH 6 |
| `b9cj` | `qou-b1je` | PR-PENDING-BATCH 5 |
| `b9cj` | `qou-3kkl` | CONJECTURE-OPEN 2, PR-PENDING-BATCH 2 |
| `b9cj` | `qou-m9o4` | CONJECTURE-OPEN 2, PR-PENDING-BATCH 2 |
| `qou-rtxm` | `qou-c8p8` | LIVE-WS 4 |
| `b9cj` | `qou-a3n3` | PR-PENDING-BATCH 4 |
| `b9cj` | `qou-cv7z` | PR-PENDING-BATCH 4 |
| `qou-rtxm` | `qou-o9ge` | PR-PENDING-BATCH 4 |
| `qou-10v9` | `qou-4cu3` | PR-PENDING-BATCH 3 |
| `qou-rtxm` | `qou-59vq` | PR-PENDING-BATCH 3 |
| `qou-10v9` | `qou-3e6w` | PR-PENDING-BATCH 2 |
| `qou-10v9` | `qou-3l2l` | PR-PENDING-BATCH 2 |
| `qou-rtxm` | `08a2` | PR-PENDING-BATCH 2 |
| `qou-rtxm` | `qou-0cyu` | PR-PENDING-BATCH 2 |
| `qou-rtxm` | `qou-1oif` | PR-PENDING-BATCH 2 |
| `qou-vo9t` | `-` | TODO 1 |
| `b9cj` | `qou-j5ch` | CONJECTURE-OPEN 1 |
| `b9cj` | `qcz14` | PR-PENDING-BATCH 1 |
| `b9cj` | `qou-4fqg` | PR-PENDING-BATCH 1 |
| `b9cj` | `qou-d1td` | PR-PENDING-BATCH 1 |
| `b9cj` | `qou-gwte` | PR-PENDING-BATCH 1 |
| `qou-5vkl` | `-` | PR-PENDING-BATCH 1 |

## Decidable rows

### DONE

| bean | title | reason | main commits |
|---|---|---|---|
| `qou-4tui` | Pass the 50-digit q into the branching route; the D row is 16 digits, not 50 | PR #7995 merged 2026-11-15; work commit 4552d3620d0 on main; body records the 50-dps lift as delivered | `4552d3620d0`, `d1536c5f036` |
| `qou-58w3` | he4-two-row-dominance pins a convention-C 866/1000 that D makes exactly 1 | PR #7986 merged 2026-11-15; work commit fd12a6522e4 on main retires the convention-C 866/1000 pin (ratio = 1), lean-direct exit 0 recorded in body | `fd12a6522e4`, `05005d77682` |
| `qou-byzu` | NS vector 5: contact topology / Beltrami flows — the regular Reeb solution and its scope | body: "proposition fully proved modulo standard [S] steps ... No conjecture is closed or introduced. The bean stays in-progress for the owner to close"; commits 4daa381f5c7, 258e9121366 on main | `4daa381f5c7`, `258e9121366`, `ae7c5121470` |

### TODO

| bean | title | reason | main commits |
|---|---|---|---|
| `qou-lpio` | Null-dual witnesses: 9 carry LP-dual field names with empty values — track the drain | partial: PR #8058 (cc8046889bb, merged) stripped the stub keys from confinement-operator-selection only; bean tracks nine witnesses — read before closing | — |
| `qou-vo9t` | Session: Bring obstruction coefficients + Yekutieli gerbe infrastructure | session epic of an ended session (PR #7747 merged 2026-10-12); open children remain | — |
| `qou-0ueg` | NS attack vectors: topological/geometric obstructions for unforced NS, mapped to QOU | body lists still-open questions; owner decisions Q1/Q2 framed with no-op default; no live session | — |
| `qou-533l` | Formalize Yekutieli central-extension-of-gerbes theorem for the brane tower (tiered) | tiered plan T1-T5; parent session claude/bold-gates (PR #7747 merged) ended; children open | — |
| `qou-ocof` | NS rescue: explore honest reformulations of an NS-singularity statement on Bring | exploratory; body names a prerequisite (ingest Fefferman PDF) not done; no live session | — |
| `qou-p6tm` | NS vector 2: vortex-line topology (helicity, linking, reconnection) via braid machinery | Q2 landed (b413a89fce1, e100f50d7e2) but body: "Still open, so the bean stays open: Markov-I / non-pure component linking"; no live session | — |

### CONJECTURE-OPEN

| bean | title | reason | main commits |
|---|---|---|---|
| `cj52` | Conjecture carrier: LocalInfinitesimalField (LocalInfinitesimalField.lean) — §3b, framewor | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |
| `hypr` | Discharge conj:surreal-limit-transfer from Mathlib Hyperreal (ℝ* is a SurrealField) | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |
| `cj8c` | Conjecture carrier: jet_convergence_classical_limit (jet_convergence_classical_limit.lean) | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |
| `cj05` | Conjecture carrier: q_gl_kummer_filtration (q_gl_kummer_filtration.lean) — §3b, framework/ | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |
| `cj7c` | Conjecture carrier: q_oper_hecke (q_oper_hecke.lean) — §3b, framework/substrate §3b carrie | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |
| `qou-0xk8` | T3/D2: Čech-cocycle gerbes and cocycle-level Yekutieli Thm 4.17 | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |
| `qou-bvxd` | T3/D1: instantiate T2b on continuous-function sheaves + Čech first Chern class infrastruct | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |
| `qou-m535` | NS vector K: knot convolution (#) as the external force — forced-NS reformulation via ILP/ | subject is an open conjecture / open identification (rule 13a: never close); no claimant — may go to todo, never to completed | — |

### KEEP

| bean | title | reason | main commits |
|---|---|---|---|
| `qou-5wuz` | DEFECT: neither qbeta-decay-sdp-extended-ck.witness.json nor qbeta-closed-form-wiring-n4-t | open PR #7610; body: "Verdict: OPEN ... Open step (needs owner OK)"; #7995 fixed half | — |
| `qou-jc9f` | Missing-hypotheses queue (P3) | grouping container for the P3 missing-hypotheses queue; owner decision 4 (2026-10-04): "group, do not close" | — |

### PR-PENDING-OLDER

| bean | title | reason | main commits |
|---|---|---|---|
| `qou-7vm4` | alpha_k_per_force_assembly bypasses q_parameter: manifest says ideal_muon, code imports q_ | named only by older open PR(s) [8082] | — |
| `qou-khmj` | GAP: gen_q0_anchor_manifest.py does not detect three proton-pinned producers — fbor_normal | named only by older open PR(s) [8082] | — |
| `qou-f8lit` | MostowRigidity.figureEight carries a truncated literal, not the exact Vol(4_1) | named only by older open PR(s) [8082] | — |
| `qou-pgdw` | precision-gates.sh runs the raw-float64 audit twice and the advisory run overwrites the ga | named only by older open PR(s) [8082] | — |

## Method

1. Front matter parsed from `/home/claude/qou/beans/defs` (5,781 beans; beans branch `0ce236e6f5f`).
2. `git log origin/main` back to 2026-06-03 (28,773 commits, main `917b6939954`); bean ids matched as whole tokens in subject and body.
3. All 8,125 PRs via REST (`state=all`): title, head ref, first 3,000 characters of body, state, `merged_at`; bean ids matched as whole tokens. PRs #8526/#8527 (coordination docs) excluded.
4. Beans-branch content history (607 commits since 2026-10-10; three commits touching > 200 files ignored as bulk refreshes).
5. Every bean not held by a PR or a live front (18) read by hand. A DONE verdict needs a work commit that is an ancestor of `origin/main`.

**Not done, and why.** The 947 batch-held beans were not read one by one: their status is set by the PR, and reading them would duplicate the batch-PR review. `qou-bstl` measured that commit-subject heuristics for "done" are 2-in-12 precise, so no row here is marked DONE from a heuristic alone.

## Addendum — platform/tooling triage (epics `qou-5vkl`, `qou-n4r9`)

Measured 2026-11-20. **No fix was made.** None of the seven items has a change that increases precision or is fixed by a corpus artifact, so under the ask-owner rule each is reported here.

| bean | state now (measured) | proposal |
|---|---|---|
| `qou-4jhp` qa-sweep cannot load at pin b61e856 | **Fixed on main:** `a3d3aec2c27` (2026-11-15) bumps the pin to `82b389982` on owner ruling P1 = B. `bun …/qa-sweep.ts --help` exits 0 here (lite platform mount). The `publish.yml` break the bean also records is the subject of `qou-w5av` / `qou-pwp9`. | DONE candidate (cite `a3d3aec2c27`). The open batch PR naming it decides the timing (batch D). |
| `qou-cvx9` uploads→library key divergence | Part A merged (#6978, #7041). The INDEX damage the bean records is **gone**: 793 dirs − 769 index rows = 24 = 22 `duplicate_of` + 1 container (`ant-v14-n7-s`) + `codata-2022`, a dataset dir with no `structure.json`. What remains is the bean's own "claim mechanism" process proposal. | Close after the process proposal is either filed as its own bean or dropped (owner). Held by batch PR #8453. |
| `qou-99fk` qa-sweep writes into tracked `test/attestations` | Owner decision 6a (2026-10-10): leave as is. | DONE-by-ruling candidate. Held by batch PR #8442. |
| `qou-grph` qa-staleness never computes the `graph` hash | The fix is in `qa-staleness.ts` in `litlfred/folio-assistant`. The mount here (`folio-assistant-lite`) is not a git repo. | Needs that repo attached. Nothing to do in qou. |
| `qou-r13s` root `lake build` evicts a restored cache | Still a deliberate non-measurement. Testing it means a root `lake build` against the **shared** cache six children use today. | Do not test this session. Keep `todo`. |
| `qou-sogb` r5 solver: scriptHash matches but 733 fields move | A changed search result (winner L 4→6), not precision. This is research on a producer. | Not mechanical. Keep open. |
| `qou-6cm9` setsid/nohup jobs die at session boundaries | A harness-behaviour finding; "survives a resume" is still unmeasured. | Keep open. The coordinator contract already says to use `run_in_background`. |
