---
# qou-d9wf
title: chi_via_rust_lossless documents ~4 s for 5Li and is still running at 10 min — the cost model is off by >150x, with no progress output
status: todo
type: task
priority: normal
created_at: 2026-09-07T13:29:22Z
updated_at: 2026-09-07T13:29:22Z
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
