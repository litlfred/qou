---
# qou-0hu2
title: 15 stalled PRs carry live unlanded work — needs per-PR disposition (not supersession)
status: todo
type: task
priority: normal
created_at: 2026-08-10T03:05:31Z
updated_at: 2026-08-10T04:23:14Z
parent: qou-531z
---

METHOD CONSTRAINT (learned from #4834): the unique-lines heuristic is UNSOUND for disposition. It measures textual difference, not unlanded substance - when main rewrites the same claim better, every rewritten line counts as branch-unique and a fully-superseded PR scores 'live'. #4834 scored 29/29 files live and was totally superseded. So '15 live' is an UPPER BOUND. Per-PR disposition must read content, not count lines. Blob-hash identity (used for #4589) remains sound.

DISPOSITION ANALYSIS DONE (sound method: explicit origin/<branch> refs, main deepened to 1500 so merge-bases resolve; classify each file absent/identical/differs vs main).

STRONG LIVE (files absent from main - cannot be a rewrite artifact): #4600 absent=26 (7 Lean modules incl HeckeAlgebra, HoefsmitRep, QSchurWeyl, QExpEntire, VirtualProjection, YoungTableaux, QBetaEnergyDictionary); #4584 absent=8 (charm probes+witnesses, complex-mass-constituent-functional); #4614 absent=5; #4656 absent=5; #4684 absent=4 (BalancedThetaLimit.lean, baldfn_theta_limit_probe.py); #4617 absent=3; #4618 absent=3; #4561 absent=2; #4588 absent=2; #4562 absent=1; #4564 absent=1 (ColourHeckeRegularHost.lean); #4682 absent=1.
MOSTLY LANDED: #4565 identical=46 differs=31 absent=5 - narrow to the 5 absent before doing anything.
PARTIAL: #4608 identical=2 differs=2 absent=0.
LIVE BY CONTENT READ despite absent=0: #4582 - main still says T_{3,5} 'mediates the weak interaction'; branch disfavours that via W=T_{2,4} collision. Branch is AHEAD of main. Flagged, incl. an internal inconsistency (branch writes 'muon, bottom' where its own prose implies second-generation = charm).

METHOD, distilled: only two signals are sound - IDENTICAL blob => landed; ABSENT file => unlanded. Both 'many unique lines' (#4834: 29/29 live, actually superseded) and 'zero absent files' (#4582: looked superseded, actually ahead of main) are UNRELIABLE. Anything in between needs a content read.
