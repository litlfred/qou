---
# qou-8hjy
title: QOU/Machinery/MarkovTraceH4.lean takes >1h to compile — now the critical path of every full build
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:12:53Z
updated_at: 2026-09-26T11:03:20Z
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

---

## RESOLVED 2026-08-09 — and the diagnosis in the title was wrong twice

**Not a heartbeat/flag problem, and not "just slow".** Two corrections to what
this bean said when it was filed:

1. **Single-threading does not help.** Peak memory grows *linearly in the
   number of Gram entries* — ~28 MB each, ~4 GB per 144 — so it is accumulated
   environment, not per-thread elaboration state. Measured: `-j 1` reached the
   same trajectory, only slower. The multithreaded run pinned at **14.79 GB of
   a 15 GB container** with 0 GB free after 1h50m, still computing at ~30%
   efficiency. It was never going to finish here.

2. **The module was not supposed to contain the closure at all.** Its own
   docstring said the 576-entry Gram closure was *"not committed"* and that
   `gram_symm` *"stays a cited `sorry` — the honest state"*, because ~6.3k
   generated lines were too heavy a permanent build cost. It **was**
   committed — every entry was there and `gram_symm` was proved from them. The
   module had never compiled (one of the 785 outside the import closure, bean
   qou-rc7b), so a docstring contradicting the code directly beneath it went
   unnoticed. Third instance of that class in this sweep.

### The fix

`computations/markov/gen_gram_closure.py` already intended two modules — it
emits a standalone Gram module importing the base — and someone folded its
output into the base. The split restores that and goes further:

    MarkovTraceH4          base defs, 161 lines
    MarkovTraceH4Gram0..7  72 entries each, chained
    MarkovTraceH4Gram      gram_symm + trM_cyclic

**The chaining is load-bearing.** Independent chunks would be elaborated in
parallel by Lake and peak at (cores x chunk) — the same wall on a bigger
machine. Chained, each waits for the last and peak is one chunk: measured flat
at **~4.3 GB across the whole chain**, not growing with depth. Chain builds in
54 min; the full tree then completes in 20 s from cache.

Generator updated to emit the split, so regeneration does not undo it.

### `gram_symm` had never compiled — two real defects

- `fin_cases i <;> fin_cases j` yields `Fin.mk` indices (`⟨3, _⟩`) while the
  entries are stated with `OfNat` numerals (`(3 : Fin 24)`). Definitionally
  equal, but `simp` matches on **syntax**: the dispatch rewrote nothing and
  left 552 of 576 goals open (the 24 diagonal ones closed by `rfl`, which is
  why the failure looked partial). Added 24 `finMk` bridges, each `rfl`.
- 576 goals against a 576-lemma `simp only` set blows the default heartbeat
  budget. Raised to 4e6 — finite terminating computation; budget raised, not
  removed.

`#print axioms` on both `gram_symm` and `trM_cyclic`: `[propext,
Classical.choice, Quot.sound]`. H4 trace cyclicity is genuinely closed, which
the file previously only claimed to be *closeable*.

### Still worth doing

`qou-0vsu`'s abstract Ocneanu-induction lemma on `MarkovStabilization`
discharges cyclicity for every `n` at once. When that lands, this entire
generated chain can be deleted and the 54 min with it.
