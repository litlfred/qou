---
# qou-sidu
title: 'DESTRUCTIVE: 228 producers truncate their own witness before an import that can raise — one audit run emptied 22'
status: in-progress
type: bug
priority: normal
created_at: 2026-09-05T06:27:27Z
updated_at: 2026-09-05T06:27:57Z
---


Found while draining `qou-qe81`'s error-row item. Not a precision or a
correctness bug — a **data-loss** bug, and it fired during this session.

## What happened

Running `computations/audits/producer_importability_audit.py` once emptied
**22 committed witnesses to zero bytes**. All 22 are `computations/probes/`
files, mostly the `gswz_*` family. Restored from HEAD by explicit single path
(never a glob).

## Root cause

The pattern, present verbatim in 228 producers:

    with open(<witness path>, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(witness, script_path=__file__, ...)
        json.dump(witness, f, indent=1)

`open(path, "w")` **truncates immediately**. The very next statement is an
import that CAN raise. When it does, the `with` block unwinds, the file closes
having never been written, and the witness is gone.

Measured, not inferred:

    $ cd computations/probes && python3 -c "from qou_substrate.witness import WitnessBuilder"
    ModuleNotFoundError: No module named 'qou_substrate'

`qou_substrate` lives under `tools/qou-substrate/python/` and is reachable only
via the sys.path scaffolding a producer sets up when RUN from the right place.
Imported bare, it is not importable.

## Why the audit is what triggered it

The trigger is the audit's own subject matter, which is the sharp part:
`producer_importability_audit` exists to find producers that cannot be
imported. It imports every producer to find out. These probes have no
`if __name__ == "__main__":` guard, so importing them runs their module-scope
body — including the truncating `open` — in exactly the bare context where
`qou_substrate` is NOT importable. The audit destroys witnesses by doing the
one thing it exists to do.

Worse, it is silent: the 22 destroyed probes are **not** listed among the
audit's reported import failures, so nothing in its output says this happened.
It was noticed only because `git status` showed 130 modified witnesses and 22
of them diffed to git's empty blob `e69de29bb2`.

## Blast radius

* **22 fired** this run.
* **228 with-blocks across 228 producers carry the pattern** and are latent.
  Any of them, imported or run in a context where `qou_substrate` is not on
  the path, empties its own witness.
* The window is not import-specific. ANY exception between the `open` and the
  `json.dump` — a KeyError in `stamp_staleness_metadata`, an interrupt, a
  disk error — has the same effect.

## Fix applied

Hoisted the imports ABOVE the `with open(...)` in all 228, with a comment at
each site saying why they must stay there, so a later tidy-up does not move
them back inside. Nothing that can raise now sits between truncation and
write.

Verified on the failure path rather than the happy one: importing
`gswz_52_galois_norm_probe.py` bare still raises `ModuleNotFoundError` — that
environment condition is unchanged and is the audit's real finding — but the
witness stays at its full 1363 bytes instead of going to 0.

## Not fixed, and worth a decision

- [x] The write is now **atomic**, in two commits. `WitnessBuilder.save()`
      first — one block covering every producer that goes through it — then
      374 direct-writing producers that bypass it. Each writes to a SIBLING
      temp file and `os.replace`s it into position (sibling, because
      `os.replace` is atomic on POSIX only within one filesystem).

      Demonstrated A/B on the library fix, under a `json.dump` that writes a
      partial object and then raises:

          new pattern:  raised, witness INTACT     56 -> 56 bytes, no debris
          old pattern:  raised, witness CORRUPTED  31 -> 12 bytes

      The producer pass took three attempts, and the corrections are worth
      recording because each was found by checking rather than by assuming:

        1. 270 sites, regex on `open(path, "w")`.
        2. My "0 missed" verification was itself broken — its pattern did not
           match the common `as f:` form. A line-based recheck found 84 real
           misses: pass 1's regex required `"w")` immediately, so it skipped
           every `open(path, "w", encoding="utf-8")` and every multi-line
           `open()`. A paren-matching scan got 98 more.
        3. Inserting the `os` import after the last line starting with
           `import`/`from` landed INSIDE a multi-line `from x import (` list
           and broke 15 files. `ast.parse` caught all 15 and none was written;
           AST-based placement fixed 13, and the last was a false positive —
           a `with open(...)` inside a string literal in
           `witness_provenance_audit.py`'s test fixtures.

      Final: 374 files atomic, 0 syntax errors tree-wide, 0 genuine sites
      left.
- [ ] **An audit should not be able to mutate the corpus it audits.**
      Importing arbitrary producers to test importability is inherently
      side-effecting; the probes' missing `__main__` guards are what let it
      reach their writes. Either the audit imports in a throwaway copy /
      subprocess with a read-only checkout, or the producers grow guards. The
      hoist makes the current failure harmless but does not remove the
      capability.

## 2026-09-05 — the second item, and what the atomic fix already bought

### The destructive CAPABILITY is largely gone, as a side effect

The remaining open item reads "an audit should not be able to mutate the corpus
it audits". Worth stating precisely what changed: with atomic writes in place,
the original failure can no longer occur. An import that raises now dies before
`os.replace`, so the committed witness is never touched — it is not truncated,
not partially written, not modified at all. The 22-witness wipe is not merely
less likely; that specific path is closed.

What is NOT closed is the capability. Importing a producer still executes its
module-scope body, and a producer can do things other than write its witness.

### A trade-off my own fix introduced, recorded rather than hidden

The library (`WitnessBuilder.save()`) unlinks its temp file on failure. The 374
direct-writer transform does NOT — it emits

    _wpath_sidu = <path>
    _wtmp_sidu  = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, ...) as f:
        ...
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)

with no `try`/`except` around it. So a producer that fails mid-write now leaves
`<name>.witness.json.tmp` behind. That is a strict improvement over destroying
the witness, but it is debris.

Deliberately not fixed by a third mechanical pass over the same 374 files:
wrapping each block in `try`/`except` re-indents every body, which is a
materially riskier transform than the two already done, for a failure mode that
is cosmetic. Two of the three passes so far needed correction, and the risk of
a bad edit exceeds the cost of a stray file.

Mitigated instead: `*.witness.json.tmp` is now in `.gitignore`, so debris
cannot be committed by an incautious `git add` and cannot be mistaken for an
artifact. Reassess if debris is ever observed in practice — as of this commit
there is none.

### The remaining item, with options rather than a guess

- [ ] An audit should not be able to mutate the corpus it audits.
      `producer_importability_audit` imports ~4000 producers in-process to test
      importability, and the missing `if __name__ == "__main__":` guards on the
      probe family are what let it reach their module-scope work.

      Options, cheapest first:

      1. **Add the missing `__main__` guards** to the probes that execute work
         at import. Fixes the cause rather than the symptom, and helps every
         other importer too. Mechanical but needs care: some producers are
         MEANT to run on import, and turning that off changes what they do.
      2. **Import under a write guard** — patch `builtins.open` for the
         duration of each import so a `"w"`/`"a"` mode raises. Contained, cheap,
         and turns any attempted mutation into exactly the finding the audit
         wants to report.
      3. **Subprocess per import.** Fully isolating, and the honest answer, but
         ~4000 process spawns on an audit that already runs over ten minutes.

      Recommend 2, with 1 as the real fix where a guard is simply missing.
      Do NOT do 3 without measuring the cost first.
