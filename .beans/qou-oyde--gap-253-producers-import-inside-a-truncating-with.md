---
# qou-oyde
title: 'GAP: 253 producers import inside a truncating with-open(w); one has already destroyed its witness on main'
status: todo
type: task
priority: normal
created_at: 2026-09-08T04:25:11Z
updated_at: 2026-09-12T07:04:20Z
---

FOUND 2026-09-08 by triage, then verified independently. Priority: the CLASS is latent; ONE member has already fired and is RED on main.

## The instance that fired (FIXED in this PR)

computations/qbeta/qbeta-chain-closed-form.witness.json is **0 BYTES on main** and is the ONLY unparseable witness of 3702 (verified: json.load over the whole tree, exactly 1 JSONDecodeError). Byte history on that path: 5930 -> 6016 -> 6018 -> **0**, truncated by 36501d7b01 (2026-09-07, 'sweep(qou-4383): re-run all 74 candidate producers'), whose own --numstat records it as pure deletion (0+ 176-) while the message asserts no regression. The loss was not noticed.

## Mechanism

open(path, 'w') TRUNCATES AT OPEN. The producer did the import and the provenance stamp INSIDE the with-block:

    with open(out_p, 'w') as f:          # <- truncates here
        from qou_substrate.witness import WitnessBuilder as _WB   # <- can raise
        _WB.stamp_staleness_metadata(...)                          # <- can raise
        json.dump(witness, f, ...)                                 # first byte only here

Anything raising between the truncation and the dump destroys the committed witness and writes nothing back. qou_substrate is NOT on PyPI, so a bare container is the DEFAULT and that import is the likely raiser.

Reproduced deterministically: with a shim making qou_substrate unimportable, the witness went 6018 -> 0. After the fix, the same forced failure leaves it at 6018.

## Why this is a defect, not a by-design refusal

- A 0-byte JSON is never a refusal; the documented refusing producers explain themselves on stdout and LEAVE THE PRIOR ARTIFACT INTACT.
- The exception is ModuleNotFoundError on a third-party import, not a corpus-defined domain guard (contrast AmDifferenceInvalid).
- The producer PASSES: exit 0, ALL PASSED, 0.83 s, and regenerates the destroyed content with a provenance-ONLY diff (4 leaves: commitSha, computedAt, gitCommit, scriptCommitSha). NO number moved -- so this is restoration, not re-derivation.
- The canonical writer already does it correctly: WitnessBuilder.save runs its checks BEFORE the open and puts only json.dump inside. This producer deviated from house style.

## The corpus PREDICTED this and chose the wrong remedy

Bean qou-m549 (status: **completed**, 2026-09-04) records it verbatim as a TRAP: the producer 'crashed ... and TRUNCATED its own witness (175 lines -> nothing) on the way out ... Restore the witness from git before re-running, or the crash looks like a drain.' That is an instruction to the AGENT instead of a fix to the PRODUCER. Three days later a sweep hit it and committed the zero to main. This bean is the fix that was declined.

## Why it reached main unseen (also fixed in this PR)

computations/audits/q0_anchor_consistency_audit.py tallied Q0_PARSE_ERROR into the counter table and did NOTHING else: no print block naming the file (unlike Q0_FLIP and Q0_ANCHOR_UNRECOGNISED), and the --strict gate was 'if args.strict and (n_flip or n_unrec)' -- parse errors could not fail it. An unparseable witness was a bare integer on a console with no filename and a green gate.

## THE CLASS -- DO NOT SWEEP IT

MEASURED independently (AST: an Import/ImportFrom anywhere inside a with-block whose context is a truncating open(...,'w')): **252 files in computations/ still carry the identical template**, after my fix removed the 253rd. This is corpus-wide and is emphatically NOT a one-PR job -- a 252-file mechanical sweep needs its own scoped decision and one owner.

Only ONE member has actually fired. That one is fixed. The other 252 are latent: each destroys its witness only if something raises between its open() and its dump.

## Next honest step for whoever takes the class

Do not blanket-rewrite 252 files. Cheapest real reduction, in order:
1. Rank by BLAST RADIUS: a producer whose witness is expensive to regenerate (long compute) loses more than one that re-runs in 0.8 s. The 0.8 s case is the one that fired, which is luck, not design.
2. Prefer the one-line form out_p.write_text(json.dumps(...) + '\n') -- it builds the payload before the file is touched at all, so there is no window, and it reads as a simplification rather than a refactor.
3. Consider a shared helper in qou_substrate so the fix is one import rather than 252 edits, then migrate incrementally.

## Coordination

The truncating commit belongs to qou-4383 (in-progress, idle >24 h at the time of writing). Its SUBJECT is grouped-era |tr_M| by fingerprint, not witness I/O, and it did not notice the loss -- so scope does not overlap. But its sweep RE-RUNS PRODUCERS, so a re-run before this fix lands would re-truncate. Flagged on that PR.


## 2026-09-12 — class re-measured at 252 EXACTLY; and step 1 is NOT executable from the corpus as it stands

Off the `qou-bstl` queue, on a tree freshly rebased onto `main` (74 + 41
commits since this bean was written). **Nothing swept** — this bean says
`## THE CLASS -- DO NOT SWEEP IT` and the 2026-09-07 ask-first directive says
the same, so this is measurement only.

### The class reproduces exactly

Re-run with this bean's own AST criterion — an `Import`/`ImportFrom` anywhere
inside a `with` whose context is a truncating `open(…, 'w')`, excluding
`_deprecated` and `__pycache__`:

    252 producers   [bean recorded 252 after its own fix removed the 253rd]

Exact agreement across two months of `main` movement. The class is neither
growing nor being drained.

### 🛑 But this bean's step 1 cannot be run — 247 of 252 have no recorded cost

Step 1 asks to *"rank by BLAST RADIUS: a producer whose witness is expensive to
regenerate (long compute) loses more than one that re-runs in 0.8 s."* The only
corpus-visible proxy for that is the witness's own recorded runtime
(`durationMs` / `elapsed_seconds`, top level or under `summary`). Measured:

    >= 60 s recorded regeneration :   3
    >=  5 s recorded              :   4
    no runtime recorded at all    : 247
    no witness attributable       :  57

So **98 % of the class carries no cost signal**, and the ranking the bean
prescribes is not derivable without running 252 producers — which is precisely
the sweep it forbids. That is a finding about the bean's plan, not a criticism
of it: the plan was written before anyone checked whether the ranking input
exists.

### The head of the ranking, for the 5 that do carry one

    603.0 s   probes/qbeta_m1_rotated_index_from_blocks.py:304
    137.0 s   probes/qbeta_m1_index_stokes_dictionary.py:212
     65.0 s   qbeta/qbeta_kc21_parity_convention_immunity_probe.py:489
      7.0 s   probes/qbeta_phib_2loop_bdictionary_probe.py:353   (2 witnesses)
      4.9 s   probes/qbeta_qsqrt3_borel_pslq_probe.py:483

**These three over a minute are where a truncation actually costs something**,
and they are a tractable unit — three files, the one-line
`out_p.write_text(json.dumps(...) + "\n")` form this bean already recommends,
no shared helper needed, no migration. That is a far smaller ask than the
252-file decision the bean currently holds.

The contrast with the one that **fired** is worth keeping: it re-ran in 0.8 s,
which this bean already calls *"luck, not design"*. The three above are the
un-lucky cases.

### Two caveats on my own numbers, both load-bearing

- **`no witness attributable: 57` is not the same as "writes nothing".** My
  attribution is by `scriptFile` basename, so a producer whose witness records
  a different `scriptFile`, or which writes a non-witness JSON, counts as 0
  here. It bounds what I could see, not what those 57 stand to lose.
- **A recorded runtime is the cost of the LAST run, not of a cold one.** Three
  of the five are `qbeta` probes whose cost depends on `pyhecke_native` being
  built; a container without it may be far slower or refuse outright.

### What I did NOT do

No file was edited, no producer run, no sweep started, no shared helper
proposed. The 252 stay as they are.

Bean stays `todo`. If the owner wants a first cut, the three ≥ 60 s files above
are the defensible unit — everything beyond them needs the cost data that does
not currently exist.
