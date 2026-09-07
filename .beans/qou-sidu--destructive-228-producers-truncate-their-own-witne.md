---
# qou-sidu
title: 'DESTRUCTIVE: 228 producers truncate their own witness before an import that can raise — one audit run emptied 22'
status: completed
type: bug
priority: normal
created_at: 2026-09-05T06:27:27Z
updated_at: 2026-09-06T03:15:52Z
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

## 2026-09-05 — write guard landed, and a correction to how I framed this bean

### Correction: the mutation was ALREADY KNOWN and documented

I have been reporting "an audit can mutate the corpus it audits" as though it
were a discovery. It was not. `producer_importability_audit.py`'s own docstring
has carried this for some time:

    ⚠ SIDE EFFECT — READ BEFORE RUNNING. Importing a module runs its top level,
    and some producers here DO REAL WORK (and write their witness) at module
    level rather than inside `main()`. A full run therefore rewrites those
    witnesses as a side effect. The first full run modified **111** of them,
    4343 insertions, and they were nearly committed inside the detector's own
    commit. Either run this in a throwaway `git worktree`, or afterwards
    restore everything except this audit's own witness

So the REWRITING was known, measured (111 files), and mitigated by a documented
procedure. What was new in this bean is narrower and worth stating precisely:
those rewrites could **empty a witness to zero bytes**, because the write
truncated before an import that then raised. That is the truncate-then-import
defect, and it is fixed. The general capability was never a secret.

### The guard

`QOU_IMPORT_WRITE_GUARD=1` replaces `builtins.open` inside the loader
subprocess for the duration of each import, refusing any mode containing
`w`, `a`, `x` or `+`.

The audit already runs each import in a SUBPROCESS, so it was process-isolated
all along — it is just that a subprocess shares the filesystem, which is the
whole point of the guard.

Verified in isolation on the failure path rather than the happy one:

    WITHOUT guard  exit=0  file='CLOBBERED'
    WITH guard     exit=1  file='PRECIOUS'   PermissionError
    read under guard -> 'PRECIOUS'           (reads still work)

`set(mode) & set("wax+")`, not `"w" in mode`: `"rb"` must stay readable and
`"r+"` must not, and a substring test gets both wrong.

OFF by default, deliberately. A producer that legitimately writes at import
would start failing under it, which would change what this audit reports and
move its baseline silently. On, it converts "this producer writes when merely
imported" into a greppable finding — i.e. the list of files that want a
`__main__` guard, which is option 1 of the three recorded above.

- [x] An audit should not be able to mutate the corpus it audits — addressed
      as an opt-in, with the default behaviour and baseline unchanged.
- [ ] Run with the guard on to enumerate the import-time writers, then add
      `__main__` guards where the write is not intended. Deferred: a full run
      of this audit is ~20 min and the `qou-uiut` table holds the checkout.

### 2026-09-05, later — the guard as first written did NOT work, and my test was why

Ran it for real and it did not hold: the audit still modified 5 witnesses with
`QOU_IMPORT_WRITE_GUARD=1` set. Restored them from HEAD by explicit path.

**Cause.** `pathlib.Path.write_text` bypasses a `builtins.open` patch.
`Path.write_text` calls `self.open`, which reaches `io.open`; and although
`builtins.open is io.open` is True, REBINDING one name does not rebind the
other. `computations/entanglement_orders.py:178` is exactly this:

    out.write_text(json.dumps(witness, indent=2, default=str))

**Why I did not catch it.** My isolation test wrote its victim file with
`open(...)` — the one form the guard covered. It passed, and it proved only
that the guard blocks what I had already assumed it blocks. Same methodological
error as the warm-cache measurement earlier in this session: testing the happy
path of my own assumption rather than the thing it could get wrong.

**Fixed** by patching all four routes — `builtins.open`, `io.open`,
`pathlib.Path.open`, and `Path.write_text` / `Path.write_bytes` directly, since
`write_text` resolves `io.open` at call time and patching the module names is
not reliably enough across CPython versions. Re-verified against every form:

    builtins open    -> PRECIOUS   BLOCKED
    Path.write_text  -> PRECIOUS   BLOCKED
    Path.open        -> PRECIOUS   BLOCKED
    io.open          -> PRECIOUS   BLOCKED
    read (Path.read_text)          -> PRECIOUS   (reads still work)

### 2026-09-05 — enumeration run: the guard holds, and it names the 95

Ran the full audit with `QOU_IMPORT_WRITE_GUARD=1` on the fixed guard.

**It held.** Tree dirty afterwards: **1 file** — the audit's own witness. The
docstring records that an unguarded full run modified **111**. So the guard
turns a run that rewrites a hundred committed witnesses into one that rewrites
its own output and nothing else, which is what makes this audit safe to run in
a working checkout at all.

**And it produced the list this item wanted.** Of 2644 producers checked, 164
unimportable, and the top cause is now the guard itself:

    other:PermissionError            95   <- writes at import
    in-repo-wiring:qou_substrate     36
    in-repo-wiring:_path_bridge      18
    other:SyntaxError                 9
    optional-dep:matplotlib           1

**95 producers write a file during import.** That is the population that wants
an `if __name__ == "__main__":` guard, and it is now a concrete list rather
than a suspicion — written to `.work/import-time-writers.txt`. Sample:
`alpha_k_jones_markov_h3`, `basis_knot_tables`, `beta-decay-from-q`,
`binding_ladder_catalog`, `borromean-axial-coupling`, `channel_product_mass`,
`delta_lambda_dim_weight_proof`, …

Note what the number means, and what it does not. `PermissionError` here is the
guard reporting "this producer attempted a write while being imported" — it is
NOT a claim that the producer is broken. Several may write deliberately at
module scope. The list is the input to that judgement, not the judgement.

Also confirms the `expect_errors` declaration works end to end: the witness
carries 163 recorded exceptions and the error-row gate left the verdict alone,
reporting `allPassed: true` on its two real assertions.

- [x] Run with the guard on to enumerate the import-time writers — 95, listed.
- [x] Add `__main__` guards where the write is not intended — **RECOMMEND NOT
      DOING THIS**, on evidence. Classified all 95 by AST:

          95  NO `__main__` guard at all
           0  has a guard with the write accidentally outside it

      Not one is the accident I was expecting. They are top-level scripts,
      written to run as `python3 foo.py`, and they end like this:

          w.add_data("tables", all_tables)
          witness_path = w.save()
          print(f"\nWitness: {witness_path.name}")

      So "add a `__main__` guard" is not a one-line fix to 95 files. There is
      no `main()` to guard — each would need its body wrapped in a function,
      i.e. 95 refactors of working scripts, to satisfy one audit's choice of
      import as its probe. That is the tail wagging the dog, and it would touch
      far more producers than the defect ever did.

      The guard already reconciles it. The tension is between the audit's
      METHOD (import a module to see whether it imports) and a legitimate
      script style (do the work at top level), and `QOU_IMPORT_WRITE_GUARD`
      resolves that at the auditing end, where the problem actually lives —
      111 rewritten files become 1.

      Revisit ONLY if a specific producer is found where the top-level write is
      genuinely unintended. The list is kept at `.work/import-time-writers.txt`
      for exactly that lookup.

---

## 2026-09-07 — misfire #7, the fatal one, and the gate that ends the class

Status left **completed**: the original defect is fixed and this is fixed too.
Recorded here because it belongs to this transform and because the *class* is
the durable finding.

Six misfires were known (2 imports injected into module docstrings, 2 reads
wrapped as writes, 2 `X.tmp.tmp` double-temps). The seventh was found by
running a producer during the 435-commit main merge, not by reading a diff.

**The transform inserted `import os as _os_sidu` as LINE 1 — above the module
docstring — in 35 files.** Two consequences, and the second is fatal:

1. The docstring is no longer the first statement, so it stops being `__doc__`
   and becomes a bare string expression. (Measured: none of the 35 reference
   `__doc__`, so this alone cost only `help()`.)
2. Any `from __future__ import annotations` below it is then not at the
   beginning of the file — a **SyntaxError**. **Twelve producers could not be
   compiled or imported at all.**

### Why nothing caught it for weeks

**`ast.parse` accepts it. `compile` does not.** Future-statement placement is
enforced at compile time, not at parse time — and every static audit in this
corpus validates with `ast.parse`. All of them reported the twelve as fine.

`producer_importability_audit` would have caught all twelve, and did not, for
two reasons neither of which is fixed by pointing at it harder: it is **wired
into no gate array** (mentioned only inside a comment in
`scripts/precision-gates.sh` — the shape AGENTS.md records for
`witness_hollowness_audit.py`), and its own docstring records an earlier pass
that reported **24 bogus SyntaxErrors**. A check with a false-positive history
is one people learn to skim.

### What the twelve cost

`qbeta-row-cap-sweep-of-physical-numbers.witness.json` kept a committed
`allPassed: true` for 435 commits. Re-run, it reports `allPassed: false` with
three failing assertions. **It had not lied — it had become impossible to
ask.** That is a distinct failure mode from the one `qou-qe81` gates (a
witness that records a failure and serialises green), and no detector here
covers it: every staleness mechanism compares a witness to its producer's
HASH, and the hash was perfectly current on a file that could not run.

### The fix, and the gate

All 35 imports relocated below the docstring and below every `__future__`.
Verified across all 376 files containing `_os_sidu`: 0 fail to compile, 0
docstrings still demoted, 0 uses left unbound.

Then a corpus-wide sweep, because a transform that misfired seven times is
not evidence that only my files are affected: **5183 tracked `.py`, 0 files
where `ast.parse` and `compile` disagree.** So the blind spot is real but has
no other live instance — a negative result, and the reason the new gate is
blocking at zero rather than baselined.

`computations/audits/python_compile_gate.py`, wired into `precision-gates.sh`.
It runs `compile()`, imports nothing, executes nothing, reads no environment.
`compile()` failing IS the defect, so it has no judgement in it and therefore
no false positives — which is exactly what the importability audit could not
offer. Self-test 10/10, including the case that pins the boundary: a hoisted
import with no `__future__` below it demotes the docstring but is legal
Python, and this gate must not claim it. Verified to FIRE rather than assumed
to: a canary carrying the misfire shape exits 1 and is labelled as accepted by
`ast.parse`.
