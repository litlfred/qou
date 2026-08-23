---
# qou-z36p
title: 'PR #5517 follow-through: attribute every further sublemma-2-1 witness move to the PR or to pre-existing staleness'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T13:22:15Z
updated_at: 2026-08-23T14:56:19Z
---

Continues the stalled #5517 session (container reclaimed; the diagnostics were
never committed). Two further `sublemma-2-1-*` witnesses sit downstream of
`char_fast._compiled_sigmas` and neither was covered by the PR.

Method: three-way — committed blob vs a fresh run at the PR's BRANCH POINT
(9e85a43628) vs a fresh run at the PR head (ed36cf64c1), same venv, both in
detached worktrees restored after every run. Comparing against `origin/main`'s
tip would have been wrong: main has moved 5 commits since the branch point,
two of them on adjacent compute.

Findings recorded on the branch; see the audit doc.


## H12 phase25 — first attempt OOM-killed; attribution NOT established

Ran `sublemma_2_1_h12_he4_phase25.py` at the branch point and at #5517's head
**concurrently**, on a 4-core / 16 GB box. That was a mistake in harness design
and it cost the measurement:

    after  (#5517 head)     Killed, exit=137, wall 2756s (46 min)
    before (branch point)   still running at 70+ min, RSS 4.17 GB

dmesg names it precisely — a **memcg** OOM, not the host:

    Memory cgroup out of memory: Killed process 30394 (python)
    anon-rss:9855784kB   (9.86 GB)

**Do not read this as "#5517 raises H12 memory."** The two runs shared one
cgroup budget and the kernel kills the largest RSS, so the kill selects for
size without establishing that the symbolic path *needs* more. The before-run
may well reach the same peak later — it is only ~4.1 GB at a *later* wall time
than the point at which the other died. I have spot readings, not a growth
curve, for either run: successive samples of the survivor read 4.17 then 4.09
GB, so it is not even monotonic, and no shape should be inferred from two
numbers.

What is worth noting either way: #5517's cost evidence is a **speed** claim at
n=6 / dim 132 (7.5s -> 3.6s). Memory is unexamined, and at H12 the working set
is ~10 GB, so a 2.5x memory factor would matter operationally even though the
time got better. That is a question, not a finding.

**Decisive test, in progress:** peak-RSS sampler armed on the live before-run;
then re-run the head ALONE and compare peaks. Serial, not concurrent.

**Second finding, independent of the above.** This producer emits nothing after
`β_⁴He: 47 generators` — no progress line, no elapsed, no ETA — across 46+
minutes. AGENTS.md §Long-compute logging discipline requires periodic progress
for anything past 5 minutes. From outside, "computing" and "wedged" are
indistinguishable, which is exactly why the OOM went unnoticed for 46 min.
