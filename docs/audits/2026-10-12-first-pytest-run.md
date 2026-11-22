# The first `pytest` run on `computations/` — 100 collected, 9 errors, and a regression guard that has never executed

**Date:** 2026-10-12. **Tree:** `main` `ab86909398b`. **Beans:** `qou-47nf` (the
finding), `qou-wv8g` (how I got here).

## Why there is a "first"

`computations/conftest.py` landed 2026-08-08 to fix the fact that the test
modules there import siblings by bare name, which resolves when a script is run
directly from that directory and **not** under pytest. Before it, collection
died on `ModuleNotFoundError: No module named '_path_bridge'`.

It fixed collection. **Nobody then ran the suite.** `pytest` is not installed in
a default container here, and the PR that proposed the conftest said so
explicitly: *"pytest is not installed in this sandbox, so the collection run was
**not** executed."* The 2026-08-19 triage that re-proposed it (PR #5330) said
the same. So the file has been load-bearing for two months on a structural
argument, never a run.

## 1. Collection — measured

```
$ python3 -m pip install pytest        # 9.1.1
$ python3 -m pytest computations/ --collect-only -q
100 tests collected, 9 errors in 299.79s
```

**All nine errors diagnosed, and none is a corpus defect:**

| count | cause |
|---|---|
| 7 | `ModuleNotFoundError: No module named 'pyhecke_native'` |
| 1 | `ModuleNotFoundError: No module named 'snappy'` |
| 1 | `FileNotFoundError: 'L6a4_c1_q_sl5_P.res'` |

The seven are the documented default state, not a breakage: `pyhecke_native` is
**not on PyPI** (its wheel workflow is `workflow_dispatch`-only with no publish
step), so it must be built with `maturin` and is absent from a fresh container.
`snappy` is an external package. The ninth is §3.

## 2. The population figure has been wrong in every version of it

`conftest.py`'s docstring read *"59 of the 86 test files"*. PR #5330
"corrected" that to *"47 test files repo-wide, 24 under `computations/`"*.
**Both counted only `test_*.py`.** This tree uses both conventions and
`*_test.py` is a large share:

```
repo-wide    test_*.py  60    *_test.py  42    combined  102
computations/                              combined   64
```

So the original undercounted, and the correction undercounted further — the
same single-spelling blindness the detector-blindness taxonomy catalogues,
here in a count rather than a grep. Measure with
`find . \( -name 'test_*.py' -o -name '*_test.py' \)`.

## 3. 🛑 `ptolemy/test_guard_rejects_spurious.py` has never run, and bean `qou-47nf` cites it as a guard

Bean `qou-47nf` §(xliii), *"TWO SILENT BUGS, both caught by impossible
arithmetic"*, records the lesson —

> Neither tool errored; both exited 0 with a confident sentence. The calibration
> that should have caught the first (4_1) PASSED under the broken reduction,
> because 4_1's solutions avoid the spurious locus and because I only ever
> tested that the guard ACCEPTS good points.
> **`test_guard_rejects_spurious.py` now pins the rejecting direction.**

It does not. Line 13, at **module scope** so it executes at import:

```python
core = ast.literal_eval(open('L6a4_c1_q_sl5_P.res').read().strip().rstrip(':'))[1]
```

Measured:

- **`L6a4_c1_q_sl5_P.res` does not exist anywhere in the repository.** A
  corpus-wide grep finds that string in exactly **one** place — this `open()`
  call. Nothing generates it; nothing else references it.
- The `.res` files that do exist are hyphenated and written by two producers
  (`ptolemy_class_sweep.py:225`, `rur_exact_number_field.py:104`), **both** of
  which resolve through `HERE = pathlib.Path(__file__).resolve().parent`. This
  test is the only `.res` consumer in the tree using a **bare relative path**,
  so it would be cwd-dependent even if the file existed.

**So the guard written because a calibration gave false assurance is itself
giving false assurance.** That is §(xliii)'s own lesson one level up: a test
that cannot run reports nothing, and reads from the ledger as though it reports
something. A reader of `qou-47nf` — a `todo`, priority **high** — takes the
rejecting direction as pinned. It is not pinned by anything.

**Deliberately not fixed.** Which file was meant is not recoverable from the
corpus: the only other underscore-named `.res` present is `L6a4_c1_fkr_p.res`,
and the hyphenated RUR outputs are a different shape. Guessing is the
speculative repair §(xliii) warns about. What is needed is the author's answer
to *which `.res` holds the degree-18 RUR from the unsaturated reduction*; the
fix is then one line plus the `HERE /` idiom its two siblings already use.

## 4. Running the suite MUTATES COMMITTED WITNESSES

Within the first minutes of the run, `git status` showed four tracked
`*.witness.json` modified — `qbeta-habiro-integrality-kill-test`,
`binding-habiro-single-element-test`, `lever1-lw-depth2-recurrence-test`,
`lever1-qinvolution-kernel-test`. Several "tests" here are **producers**: they
compute and write their witness as a side effect of asserting on it.

Consequence for anyone running the suite: **revert `computations/` afterwards**,
exactly as for `precision-gates.sh` (bean `qou-v0t8`). A run leaves a dirty tree
that reads as real work. Whether a test ought to write a tracked artifact at all
is a design question, not settled here.

## 5. What is NOT established

**The 100 collected tests have not been reported pass/fail.** The run was
started and had not finished when this was written; some of these modules reach
long-compute producers (`binding_energy` alone is ~13.6 min on the kernel arm
and ~7.1 h on the fallback, which is the arm a container without
`pyhecke_native` gets). A wall-clock death is not a result — the figure is
owed by a later run with a real budget and `2>&1 | tee`, per the long-compute
logging discipline.

So this audit establishes: the suite **collects**, what the nine errors **are**,
that the population figure was wrong, that one cited regression guard **cannot
execute**, and that a run **dirties the tree**. It does not establish that the
suite passes.
