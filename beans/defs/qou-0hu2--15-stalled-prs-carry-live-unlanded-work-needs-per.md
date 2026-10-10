---
# qou-0hu2
title: 15 stalled PRs carry live unlanded work — needs per-PR disposition (not supersession)
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T03:05:31Z
updated_at: 2026-10-04T15:15:59Z
parent: qou-5vkl
---

METHOD CONSTRAINT (learned from #4834): the unique-lines heuristic is UNSOUND for disposition. It measures textual difference, not unlanded substance - when main rewrites the same claim better, every rewritten line counts as branch-unique and a fully-superseded PR scores 'live'. #4834 scored 29/29 files live and was totally superseded. So '15 live' is an UPPER BOUND. Per-PR disposition must read content, not count lines. Blob-hash identity (used for #4589) remains sound.

DISPOSITION ANALYSIS DONE (sound method: explicit origin/<branch> refs, main deepened to 1500 so merge-bases resolve; classify each file absent/identical/differs vs main).

STRONG LIVE (files absent from main - cannot be a rewrite artifact): #4600 absent=26 (7 Lean modules incl HeckeAlgebra, HoefsmitRep, QSchurWeyl, QExpEntire, VirtualProjection, YoungTableaux, QBetaEnergyDictionary); #4584 absent=8 (charm probes+witnesses, complex-mass-constituent-functional); #4614 absent=5; #4656 absent=5; #4684 absent=4 (BalancedThetaLimit.lean, baldfn_theta_limit_probe.py); #4617 absent=3; #4618 absent=3; #4561 absent=2; #4588 absent=2; #4562 absent=1; #4564 absent=1 (ColourHeckeRegularHost.lean); #4682 absent=1.
MOSTLY LANDED: #4565 identical=46 differs=31 absent=5 - narrow to the 5 absent before doing anything.
PARTIAL: #4608 identical=2 differs=2 absent=0.
LIVE BY CONTENT READ despite absent=0: #4582 - main still says T_{3,5} 'mediates the weak interaction'; branch disfavours that via W=T_{2,4} collision. Branch is AHEAD of main. Flagged, incl. an internal inconsistency (branch writes 'muon, bottom' where its own prose implies second-generation = charm).

METHOD, distilled: only two signals are sound - IDENTICAL blob => landed; ABSENT file => unlanded. Both 'many unique lines' (#4834: 29/29 live, actually superseded) and 'zero absent files' (#4582: looked superseded, actually ahead of main) are UNRELIABLE. Anything in between needs a content read.

METHOD CORRECTION 3 (from #4565): 'absent file => unlanded' is ALSO WRONG. #4565 scored absent=5; all five are landed or superseded. Three are byte-identical blobs at a renamed chapter path (particle-interactions/ -> knots-particles-confinement/). The headline Lean file lepton_continuant_divisibility_general.lean is absent BY FILENAME but its theorems (morganVoyceB_add, morganVoyceB_dvd_of_dvd) are verbatim on main inside lepton_continuant_divisibility_reverse.lean, which ALSO proves the converse (morganVoyceB_dvd_reverse) and the full equivalence morganVoyceB_dvd_iff. main is AHEAD. Only morganVoyceB_three_dvd_nine is novel - a one-line corollary.

CONTENT-HASH RE-RUN (31649 main blobs indexed, immune to relocation): #4565 content-on-main=49 novel=33 (headline superseded); #4608 2/2; #4600 novel=34; #4584 9; #4656 6; #4588 5; #4614 5; #4561 4; #4618 4; #4684 4; #4617 3; #4562 2; #4564 1; #4582 1; #4682 1. Upper bound only - content-hash does NOT catch rewrite-supersession.

FINAL METHOD STATE: three cheap proxies, three failures, three directions. many-unique-lines=>live failed on #4834; zero-absent=>superseded failed on #4582; absent=>unlanded failed on #4565. ONLY 'identical blob => landed' survives, and it undercounts unless hashed against the WHOLE tree. There is no cheap screen: each PR needs its novel files read, asking 'does main prove this under another name?' - i.e. the AGENTS.md corpus-grep discipline. NEXT: #4600 (34 novel, 7 Lean modules), least likely to be a relocation artifact.

#4600 DISPOSITIONED - the first sweep PR confirmed WORTH LANDING. 14 novel non-bean files (content-hashed vs 29424 main blobs), 7 Lean. Declaration-level check by NAME across all main .lean: ~32 of 53 decls have no name match. Breakdown: QSchurWeyl 4/4 novel (HeckeWedderburnData, markov_add/one_eq/smul); VirtualProjection 3/3 novel (pi0, pi0_offshell, pi0_eq_zero_iff); QExpEntire 8/10; QBetaEnergyDictionary 6/7; HoefsmitRep 8/13; YoungTableaux 2/9; HeckeAlgebra 1/7 (last two largely duplicative vs QOU/Hecke + QOU/Mathlib - check for redundancy). QUALITY: 1 tactic sorry across all 7 files, 0 trivial-True, 0 native_decide. The sorry (HoefsmitRep:247) is honest state-and-queue with 6 lines naming Hoefsmit's braid relation as the gap + beans SW-4/SW-5. NOT COMPILED - adds a new QOU/SchurWeyl/ dir and edits QOU.lean imports, so the cone does not exist on main; lean-direct pass is the gate before landing. Docstring-sorry trap hit a 4th time (grep -c sorry = 7 and 13 on two files, all prose).

## 2026-08-10 (evening) — the OLD PRs are not stale-and-landed. Measured.

Ten of the oldest undispositioned PRs (2026-06-19 .. 2026-08-02) tested by the
only method that has held up: rebase onto `main` and count surviving commits.
Zero surviving = the work landed (that is what closed #4608).

| PR | result | branch files |
|---|---|---|
| #2503 | rebases, **2 commits survive** | 1 |
| #3805 | rebases, **2 survive** | 2 |
| #3807 | 1-file conflict | 13 |
| #3808 | rebases, **1 survives** | 3 |
| #4133 | 1-file conflict | 110 |
| #4409 | 1-file conflict | 3 |
| #4451 | rebases, **6 survive** | 8 |
| #4515 | 1-file conflict | 3 |
| #4557 | rebases, **2 survive** | 7 |
| #4568 | rebases, **1 survives** | 1 |

**Not one rebased to zero.** Every one carries live unlanded work, and every
conflict is a *single file*. The intuition that months-old PRs are mostly
superseded is wrong for this corpus — the two supersessions found today
(#4565, #4608) were both from the *recent* cohort, not the old one.

Practical consequence: there is no bulk close available here. Each needs
verification and a 1-file conflict resolution, i.e. the same per-PR treatment
the recent cohort got. Budget accordingly rather than expecting a sweep.

### A method trap that cost two passes today

`--depth=100` is NOT enough to resolve merge-bases for June/July branches
against current `main`. The first run reported **CONFLICT on 10 of 12** with
`files=0` and `fatal: no merge base` — pure artifact. `--deepen=4000` fixed it
and the picture inverted (8 of 10 rebase cleanly).

This is the *third* form of the same underlying trap, and they should be read
as one rule: **a shallow clone cannot answer questions about branch
relationships.** It has now produced (1) `merge-tree` CONFLICT on every branch,
(2) unresolvable merge-bases in file classification, and (3) this. Deepen
first, then measure.
