---
# qou-w6tr
title: 'Triage 590 dangling in-progress bean claims (propose-only; proposed W7)'
status: todo
type: task
priority: normal
created_at: 2026-11-20T07:50:00Z
updated_at: 2026-11-20T08:10:00Z
parent: qou-c20n
---

Found by W6 (session review, `docs/coordination/2026-11-20-session-review.{md,json}` on
`claude/session-review-2026-11-20`). Of 1,242 open beans last touched by an older session,
590 are `in-progress` with `updated_at` before 2026-11-13 and no open PR: nobody is working them.
Overall 1,814 of 5,779 beans say `in-progress`, so the status carries no information.

Task: for each, propose keep / back-to-`todo` / completed-with-commit. Propose only; the owner
or coordinator approves closures in batches. Never close a bean whose subject is an open
conjecture (AGENTS.md 13a). List: JSON `items[]` with `claim == "dangling-claim"`.
Owner decision D1 in the review doc (whether to stand up W7 for this).

Claude-Session: https://claude.ai/code/session_01VQDpPcM7ZXURrKoeUaqZaF

**Note 2026-11-20 (W6 scheduled run, https://claude.ai/code/session_01VQDpPgX3UVCddvq75ab4EV):** a narrower sub-list for the first pass. 72 `in-progress` beans whose every referenced PR is merged and none open (detection by `#N` mentions, so some links are loose). Skip any whose title names a conjecture, derivation or gap. Also `qou-y48h` (status lags recorded outcome) belongs here. Beans: `qou-1inh`, `qou-21oc`, `qou-3nva`, `qou-4jhp`, `qou-6p3b`, `qou-6tdg`, `qou-7ylg`, `qou-840k`, `qou-85o2`, `qou-86p5`, `qou-8dlq`, `qou-9w89`, `qou-abd7`, `qou-ar7f`, `qou-avtq`, `qou-b7cf`, `qou-brkp`, `qou-cb3r`, `qou-cds2`, `qou-citp`, `qou-dke6`, `qou-e9pp`, `qou-eggf`, `qou-ekgf`, `qou-epxx`, `qou-fd2u`, `qou-fi93`, `qou-g4x1`, `qou-gjkv`, `qou-gwe9`, `qou-hlx7`, `qou-hlxt`, `qou-j16x`, `qou-j540`, `qou-jgg0`, `qou-k448`, `qou-ldwx`, `qou-lvx7`, `qou-m7py`, `qou-nmuz`, `qou-nxjw`, `qou-o6ml`, `qou-pc85`, `qou-pdgc`, `qou-pg2r`, `qou-puwe`, `qou-pwut`, `qou-q0rf`, `qou-q425`, `qou-qs1d`, `qou-qs1x`, `qou-r4w5`, `qou-r9a6`, `qou-s4xb`, `qou-skn4`, `qou-sl3f`, `qou-t1dx`, `qou-t28w`, `qou-tmmt`, `qou-vu19`, `qou-vuaj`, `qou-wc8f`, `qou-wkcd`, `qou-wkcj`, `qou-wlnx`, `qou-wsha`, `qou-yvyd`, `qou-ywie`, `qou-z08b`, `qou-z23u`, `qou-z3k1`, `qou-z9fx`
