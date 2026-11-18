---
# qou-d9wf
title: chi_via_rust_lossless documents ~4 s for 5Li and is still running at 10 min — the cost model is off by >150x, with no progress output
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T13:29:22Z
updated_at: 2026-10-04T15:16:56Z
parent: qou-trd0
---

## The claim, and the measurement

`computations/chi_via_rust_lossless.py` documents its own cost in its module
docstring:

> The canonical Rust `pyhecke_native.chi_q_via_gp` returns the exact Laurent
> character per λ in ~20 ms **independent of dim V_λ**, so a whole nucleus is
> seconds:
>
>     ⁴He H₁₂ (77 λ) ≈ 2 s · ⁵Li H₁₅ (176 λ) ≈ 4 s · ⁶Li H₁₈ (385 λ) ≈ 8 s

Measured 2026-09-07, `--fresh 5Li 6Li`, PID pegged at 100 % CPU throughout:
**⁵Li alone exceeded 10 minutes and had not finished**, against a documented
4 s. That is **>150×**, and it is a *lower bound* — the run had not completed
when this was opened.

## It is NOT the y_λ tower extension, which is the obvious explanation

`_ensure_y_lambda(n)` prints `(y_λ tower has no H{n}; extending closed-form,
gated)` when it has to extend. That string appears **0 times** in the run log,
so the tower already covered H₁₅ and no extension was paid for. The time is the
χ computation itself.

What that puts in doubt is specifically the **"independent of dim V_λ"** clause.
⁴He (H₁₂, 77 λ) really does complete in seconds; ⁵Li is H₁₅ with dims into the
hundreds. If the per-λ cost were dim-independent, 176 λ would be ~2.3× ⁴He's 77 λ.

## Why it is worth a bean rather than a shrug

**The estimate is load-bearing for planning.** It is the reason an agent reaches
for this producer to regenerate a stale cache — the whole appeal is "seconds, so
just re-run it". At the real cost, regenerating ⁵Li + ⁶Li is a long-compute and
has to be budgeted and logged as one.

**It has no progress output**, which is the second half of the defect.
`AGENTS.md` §"Long-compute logging discipline" requires any script expected to
run > 5 min to emit progress every ~10 s or ~5 % of work with wall elapsed + ETA.
This one prints `176 partitions via Rust chi_q_via_gp` and then nothing at all
for ten minutes. Combined with the 4 s estimate, an agent has every reason to
conclude it has hung — and the documented response to a silent long-runner is to
assume it crashed. I had to check `%CPU` and `RSS` on the PID to establish it was
alive.

**And the PID check is its own trap.** `pgrep -f chi_via_rust_lossless | head -1`
returns the *wrapper shell* (0.0 % CPU, 6 MB RSS), which reads exactly like a
hung process. The real worker was two levels down at 100 % CPU / 217 MB. Use
`ps -eo pid,ppid,etime,%cpu,rss --sort=-%cpu`, not `pgrep | head -1`.

## What would settle it

Time ⁴He, ⁵Li and ⁶Li separately with `time` and record λ-count against wall
seconds. Three points separate "the estimate is uniformly optimistic" from "the
cost grows with dim and the docstring's independence claim is wrong" — and only
the second is a defect in the Rust path rather than in the prose.

Do **not** fix this by editing the docstring's numbers alone. If the cost does
grow with dim, the sentence that needs changing is *"independent of dim V_λ"*,
not the three timings that follow from it.

## Context

Found while regenerating the ⁵Li/⁶Li chi caches under `qou-k54t` — they were
last touched 2026-08-15, before the intra-ordering ruling (`qou-hu1f`,
2026-09-05), so `carrier_band_ratio_pinned` was straddling two braid words.

## Related: the write is safe against a mid-compute kill, but not against a mid-write one

Checked while deciding whether a `timeout` kill could corrupt a cache. The
producer accumulates in memory and writes **once**, at
`chi_via_rust_lossless.py:238`, after the whole partition loop:

```python
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
```

So a kill **during the computation** is harmless — the file keeps its previous
contents, and the run is simply lost. That is the case that matters here and it
is fine.

The residual gap is that this is **not an atomic write**: there is no
`tmp + os.replace`. A kill landing inside `write_text` itself truncates the
witness to whatever bytes reached disk, producing a JSON that no consumer can
parse and that no staleness check will recognise as a cache at all. The window
is small for ⁵Li and larger for ⁶Li (385 partitions at 50 dps is megabytes), and
it is exactly the window a `timeout` is most likely to land in for a long run —
because the run ends at the write.

Cheap fix if anyone is in the file: write to `out.with_suffix('.tmp')` then
`os.replace`. Not done here — it is a different concern from the cost model this
bean is about, and this producer's caches are load-bearing enough that a
drive-by change to their write path deserves its own review.

**This also explains the in-memory growth** noted above (RSS 198 MB at 7:45 →
247 MB at 15:37 on a single atom): every partition's result is held until the
single write at the end. That is a plausible contributor to the cost not being
"independent of dim V_λ" as documented, though it is not established as *the*
cause.

## HARD BOUND: >30 minutes, i.e. >450× — the run hit its timeout unfinished

`EXIT=124`. The `timeout 1800` fired with ⁵Li **still on its first atom**, having
never printed a second line. So the earlier ">150×" is superseded by a measured
lower bound of **>450×** against the documented 4 s, and ⁶Li — 385 partitions to
⁵Li's 176 — was never reached at all.

Two figures for the record, both wall clock at 100 % CPU throughout:

    documented   5Li H15 (176 λ)   ~4 s
    measured     5Li H15 (176 λ)   >1800 s, did not complete

Per-λ that is **>10 s**, against a documented **~20 ms** — and the docstring
attributes the 20 ms to `chi_q_via_gp` being *"independent of dim V_λ"*, which is
the clause the measurement is pointed at.

**RSS grew monotonically the whole time**: 198 MB at 7:45 → 310 MB at 29:36,
~5 MB/min, on a single atom. Consistent with every partition's result being held
until the single write at the end (see the write-path note above), and a
plausible contributor to the cost — not established as the cause.

## The kill was clean, as predicted, and that is worth having confirmed

The write-path analysis above said a mid-compute kill would leave the caches
untouched because the producer writes once at the end. Verified after `EXIT=124`:
`git status computations/` is empty, and both files still parse with their full
partition counts (176 and 385). So a `timeout` on this producer costs the run and
nothing else — useful to know before committing to a multi-hour budget.

## Restarted at `timeout 14400`

Four hours, both atoms in one invocation. ⁵Li's result is written before ⁶Li
begins, so an interruption during ⁶Li still banks ⁵Li. Extrapolating the >10 s/λ
rate, ⁶Li's 385 λ is on the order of an hour by itself; the 4 h budget is sized so
the pair is not the binding constraint again.
