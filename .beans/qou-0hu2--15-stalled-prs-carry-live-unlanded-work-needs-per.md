---
# qou-0hu2
title: 15 stalled PRs carry live unlanded work — needs per-PR disposition (not supersession)
status: todo
type: task
priority: normal
created_at: 2026-08-10T03:05:31Z
updated_at: 2026-08-10T12:05:17Z
parent: qou-531z
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
