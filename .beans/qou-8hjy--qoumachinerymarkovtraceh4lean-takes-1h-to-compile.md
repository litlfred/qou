---
# qou-8hjy
title: QOU/Machinery/MarkovTraceH4.lean takes >1h to compile — now the critical path of every full build
status: todo
type: task
created_at: 2026-08-08T23:12:53Z
updated_at: 2026-08-08T23:12:53Z
---


Surfaced by the build-coverage drain (bean qou-rc7b). This module was one of
the 766 that `lake build` never reached; now that `globs = ["QOU", "QOU.+"]`
is flipped, it is in the default target and it **dominates the wall clock of
every full build** — over an hour, single-threaded at the tail, while all
1651 other modules are already done.

## Shape of the problem

    6541 lines
     603 declarations
    3474 `simp` invocations
    2316 `ring` invocations

No `decide`, no `native_decide`, no obvious runaway — it is not pathological,
just very large and written in the most expensive style available. The cost
is ~10 tactic calls per declaration across 603 declarations, each `simp`
paying full discrimination-tree setup.

## Why it matters now, not before

It was free while it sat outside the build. It is not free now: it sets the
floor on CI turnaround and on any local `lake build`, and it is the last
thing running so it parallelises with nothing.

## Options (not yet costed)

- **Split the module.** 603 declarations in one file is the immediate cause
  of the serial tail; several files would parallelise.
- **Replace `simp` with `simp only [...]`** at the hot sites. Mechanical,
  measurable, no claim change. Profile first (`set_option profiler true`)
  rather than guessing which of the 3474 dominate.
- **Check for a generated origin.** The uniformity (603 declarations, an
  even ~5.7 `simp` + 3.8 `ring` each) reads machine-authored; if there is a
  generator, fix the emitted tactic style at the source rather than the
  output.

## Not urgent, but do not lose it

Nothing is wrong with the mathematics and nothing is blocked. This is a
build-economics bean: it will quietly tax every future session until someone
spends an hour on it.
