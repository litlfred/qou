---
# qou-3kni
title: 'Two conj: labels named by the pole-to-cusp producers have no carrier -- and neither producer can be re-run here to fix the docstring'
status: todo
type: task
priority: normal
created_at: 2026-09-14T19:57:29Z
updated_at: 2026-10-10T07:58:22Z
parent: b9cj
---

Measured 2026-09-14 (PR #7401, issue #7400), while exploring `qou-mfdq` Finding 1.
**Nothing edited in `computations/` here** — the reason is below and it is not
caution, it is that the fix cannot be verified in this container.

## The finding

Both live producers of the pole-to-cusp arc declare, in their **Manuscript
references** docstrings, conjecture labels that have **no carrier file anywhere
in the tree**:

```
computations/q_pochhammer_seed.py:11-14     computations/snappy_cusp_seeding.py:26-28
  - def:q-pochhammer-partial-product   OK      - conj:shared-denominator-cusp-holonomy   OK
  - conj:shared-denominator-cusp-holonomy OK   - conj:pl-jsj-mass-integration-equivalence  DEAD
  - conj:denominator-zeros-as-sw-critical-points  DEAD   - conj:denominator-zeros-as-sw-critical-points  DEAD
  - conj:pl-jsj-mass-integration-equivalence      DEAD
```

Measured with `git ls-files | grep -c <label>`:

| label | carrier files |
|---|---|
| `shared-denominator-cusp-holonomy` | 5 |
| `algebraic-geometric-dilog-equivalence` | 5 |
| **`pl-jsj-mass-integration-equivalence`** | **0** |
| **`denominator-zeros-as-sw-critical-points`** | **0** |
| **`jet-gb-pl-correspondence`** | **0** |

`snappy_cusp_seeding.py:16-17` goes further than citing one: *"The output is a
witness for `conj:shared-denominator-cusp-holonomy` **and
`conj:pl-jsj-mass-integration-equivalence`**"* — a producer declaring itself the
witness for a conjecture that does not exist.

The third label, `prop:jet-gb-pl-correspondence`, is named in
`brings-surface/thurston-relaxation.md:9` as the carrier of the **"GB-PL
bijection"** — the corpus's only statement identifying Gröbner-Shirshov
reduction depth with the ideal-tetrahedron count. That identification is
load-bearing for the whole `n`-overload question (`qou-mfdq`, and the sixth
"depth" sense now registered in `notation-collisions.md`), and its carrier is
gone.

All three lived under `content/quantum-observable-universe/descartes-universe/`,
which no longer exists (`ls -d` → No such file or directory).

## Why no checker catches any of them

- `uses-resolve` reads **manifest `uses[]`**. Two of these are in **Python
  docstrings** and the third is **plain parenthetical prose**, not a
  `[...](#label)` link. None is a manifest edge.
- The witness validators read `contentBlock`, and both producers call
  `w.set_content_block("conj:shared-denominator-cusp-holonomy")` — a **live**
  label. So the machine-readable field is clean and the prose is not.

## Why the producer docstrings were NOT edited

`scriptHash` is a whole-file hash, so a docstring-only edit drifts it and the
witness goes stale. AGENTS.md's remedy is "just re-run the producer". **Neither
can be re-run in this container:**

- `snappy_cusp_seeding.py` — `import snappy` → `ModuleNotFoundError`. Not
  installed, not pip-installable here.
- `q_pochhammer_seed.py` — runs, but local `mpmath` is **1.3.0** against the
  witness's recorded **1.4.1**. Re-running would stamp an environment
  **downgrade** into the witness. (This is not hypothetical: a stray
  `qbeta-ck-basis-constrained-pslq.witness.json` in the working tree at the
  start of this session carried exactly that 1.4.1 → 1.3.0 regression, and was
  reverted rather than committed.)

So editing either docstring here buys a correct comment and a stale witness,
which is a worse trade than leaving the comment wrong and findable.

## What to do, and what it needs

1. **In a container with `snappy` and `mpmath 1.4.1`**: correct both Manuscript
   reference blocks (mark the two labels as having no carrier, naming the
   removed `descartes-universe/` chapter), then re-run both producers and commit
   the refreshed witnesses in the same commit. Cheap — recorded `durationMs` is
   **15** and **45**.
2. **Separately and independently**: decide what `prop:jet-gb-pl-correspondence`
   should be. Either the GB-PL bijection is restated somewhere live, or
   `thurston-relaxation.md:9` should stop asserting it. That is a mathematical
   call, not a bookkeeping one — see `qou-mfdq` and the "triangulation size"
   entry in `notation-collisions.md`, both of which record that the
   identification is currently *asserted* rather than supported.
3. **Worth considering, not proposed**: a checker for `conj:`/`prop:`/`def:`
   labels appearing in `computations/*.py` docstrings, which is a surface no
   existing gate reads. Three dead labels in two files is a small sample; the
   population is unmeasured.

## Default if nothing is done

The two producers keep declaring themselves witnesses for a non-existent
conjecture, and `thurston-relaxation` keeps citing a carrier that is not there.
No number moves; no witness is wrong; the cost is entirely that a reader
following those citations lands on nothing, and that the GB-PL identification
reads as backed when it is not.


---

## Re-checked 2026-10-10 — the producer half is MORE blocked, and this bean's third finding is misdescribed

**Environment, measured in a fresh container (not the one that wrote this bean):**
`snappy` absent as before, and so are **`mpmath`, `numpy`, `scipy` and `sympy`** —
all four. So the docstring half stays blocked and the block is wider than
recorded: the two producers cannot be imported here, let alone re-run to
re-stamp `scriptHash`. Nothing in `computations/` was edited.

**🛑 The third finding above is wrong about WHERE the label is named, and the
error propagated into `notation-collisions.md`.** This bean says
`prop:jet-gb-pl-correspondence` *"is named in
`brings-surface/thurston-relaxation.md:9` as the carrier of the GB-PL
bijection"*. It is not. The whole of line 9's claim is

> The Gröbner--Shirshov reduction depth maps to the number of ideal tetrahedra
> used in the triangulation (GB--PL bijection).

— a bare parenthetical with no label and no link. Measured: `jet-gb-pl`,
`GB-PL` and `GB--PL` together occur in that file **exactly once**, on that line.

That misdescription reached `notation-collisions.md` in PR #7401, whose
`n`-overload entry read *"the carrier it names for that … has no file in the
tree"*. Provenance checked, not assumed: main before #7401's merge had **0**
occurrences of that clause, the branch side **1**. Corrected in PR #7546.

**The correction makes the claim STRONGER.** "Cites a dead carrier" is a
dangling reference; "names no carrier" means the GB-PL assertion is
**unreachable by label at all** — an agent grepping the label to find the claim
lands only on the register entry recording its absence, never on the assertion.

**Carrier counts re-measured on `main` 77695711d2** (the 2026-09-14 figures
above are a month and ~500 commits old):

| label | carriers | was |
|---|---|---|
| `jet-gb-pl-correspondence` | 0 | 0 |
| `pl-jsj-mass-integration-equivalence` | 0 | 0 |
| `denominator-zeros-as-sw-critical-points` | 0 | 0 |
| `shared-denominator-cusp-holonomy` | **6** | 5 |
| `algebraic-geometric-dilog-equivalence` | 5 | 5 |

And **no witness either**: the `jet-gb-pl-correspondence.witness.json` that
`docs/audits/2026-05-18-compute-integration-sweep.md:145` lists does not exist.
Both dated audits place the block at
`content/quantum-observable-universe/descartes-universe/`, which the
`content/` -> `folio/` move left behind.

**Still open, and why it is not closeable here** (per the rule against closing a
bean whose subject is an open conjecture): the two *docstring* labels need a
container that can run the producers, and whether `thurston-relaxation.md:9`'s
uncited GB-PL identification should be scoped, retired, or given a carrier is a
mathematics decision for the owner — clause (1) of
`conj:algebraic-geometric-dilog-equivalence` defers to that line for the
depth-equals-tetrahedron-count identification, so changing it moves what the
conjecture is understood to rest on.

## 2026-10-10 — owner ruling on the GB–PL line: scope it

Owner chose "Scope it" on a decision card (scope / retire / give a carrier / leave).
`thurston-relaxation.md` line 9 now says the depth-equals-tetrahedron-count identification
is asserted, not established, names clause (1) of `conj:algebraic-geometric-dilog-equivalence`
as resting on it, and gives it that conjecture's tier. No mathematics was decided. A
carrier block is still possible later. This bean stays `todo`: the identification is
still open, and the producer re-run half is tracked separately.

## 2026-10-10 — producer half done: docstrings corrected, both re-run, payloads byte-identical

Installed snappy 3.3.2, mpmath 1.4.1, numpy 2.4.6, scipy 1.17.1, sympy 1.14.0 and
clarabel 0.11.1, which matches every recorded `environment` field except python
(3.11.15 recorded, 3.13.16 here) and `pyhecke_native_build`.

- **`snappy_cusp_seeding.py` was broken on main.** It imported `IM_PERTURBATION` from
  `q_pochhammer_seed`, which now exports only `IM_PERTURBATION_STR = "0.1"`, so it died
  with `ImportError` before computing anything. The fix uses the shared string constant
  (`complex(0, float(IM_PERTURBATION_STR))`, the same 0.1j kick).
- Both Manuscript-reference blocks now mark `conj:pl-jsj-mass-integration-equivalence`
  and `conj:denominator-zeros-as-sw-critical-points` as `[no carrier]`.
- Re-run with the volatile fields masked (computedAt, commitSha, scriptHash,
  scriptCommitSha, durationMs, invocation, environment): **0 payload differences in
  either witness.** A baseline run before the edit also reproduced q-pochhammer-seed
  unchanged.
- `precision-gates.sh`: the RED set is identical with and without these changes (10
  pre-existing ratchets), and no RED line names either file. snappy-cusp-seeding still
  carries 121 raw float64 fields. That is pre-existing, the values are unchanged, and the
  fix (carry mpf through SnapPy output) is not made here.

Stays `todo`: the GB–PL identification is still an open conjecture-tier claim (scoped
the same day), and the two dead labels still have no carrier.


## 2026-10-10 (later) — the environment blocker is GONE; the producer half has a DIFFERENT blocker

**Both environment claims above are now measurably false in this container**, and
one of them was never about the environment at all.

### `snappy` IS pip-installable

This bean says *"Not installed, not pip-installable here."* Measured:
`python3 -m pip install snappy` → **SnapPy 3.3.2, `snappy.Manifold` available**
(one harmless `Plink failed to import tkinter` warning; GUI only). `qou-m6gp`
independently recorded the same correction on 2026-09-07 — *"SnapPy 3.3.2 was
ALREADY present in this container; the absent-from-every-container premise does
not hold"* — so this is the second time the claim has been retracted, and the
first retraction was not propagated here.

**One trap worth recording, because `pip` reported success while doing nothing
useful:** this container has `python3` = `/usr/local/bin/python3` (3.11.17) and
`pip` = `/usr/bin/pip` (**python 3.13**). `pip install` exits 0 and installs into
an interpreter nothing here uses; `python3 -c "import mpmath"` still fails. Use
`python3 -m pip`. Same shape as every other finding in this session: a tool
reporting success for work done in the wrong place.

### The `mpmath` downgrade blocker is resolved, and the re-run is CLEAN

This bean correctly refused to re-run `q_pochhammer_seed.py` under local
`mpmath 1.3.0` against the witness's recorded **1.4.1**, since that stamps an
environment downgrade. `python3 -m pip install mpmath==1.4.1` installs
(sympy warns about its own `<1.4` pin; nothing here imports sympy on this path).

Full environment now stamped, against the recorded block:

| key | recorded | here | |
|---|---|---|---|
| `mpmath` | 1.4.1 | **1.4.1** | match |
| `numpy` / `scipy` / `sympy` | 2.4.6 / 1.17.1 / 1.14.0 | identical | match |
| `clarabel` | 0.11.1 | **0.11.1** | match |
| `pyhecke_native` | 0.9.0 | **0.9.0** | built from `tools/pyhecke-native` (`maturin build --release`, Cargo.toml says 0.9.0) |
| `python` | 3.11.15 | 3.11.17 | patch **upgrade** |
| `pyhecke_native_build` | `e3fab84c4c1df76a` | `f674395cadf67f1a` | **expected to differ** |

That last row is not a regression and must not be read as one:
`qou_substrate.witness` computes it as `sha256(<compiled .so>)[:16]` and its own
comment says the field *"is NOT a version and must never be ORDERED"*, with the
measured reason — ordering a hex digest makes the verdict depend on whether it
starts with a digit — and notes the corpus already carries **five distinct
values across 811 witnesses**.

**`q_pochhammer_seed.py` re-ran here and the producer's own guard said it:**

> `↑ environment: recording a STRONGER environment block than the copy on disk;
> rewriting provenance only (payload unchanged).`

The diff is **exactly five lines and every one is provenance** — `computedAt`,
`commitSha`, `scriptCommitSha`, the python patch bump, the build hash. Zero
payload change; `scriptHash` untouched. So the docstring edit this bean defers
is now safe for that producer. **The tree was restored afterwards**
(`git checkout -- computations/`) per the sibling-witness discipline; nothing was
committed, because the docstring edit itself has not been made.

### But `snappy_cusp_seeding.py` CANNOT RUN, for an unrelated reason

With `snappy` installed it gets two lines further and dies:

    File "computations/snappy_cusp_seeding.py", line 47
      from q_pochhammer_seed import IM_PERTURBATION
    ImportError: cannot import name 'IM_PERTURBATION' from 'q_pochhammer_seed'

`q_pochhammer_seed.py` carries `IM_PERTURBATION_STR = "0.1"` and reconstructs the
complex value as `mpc(0, mpf(IM_PERTURBATION_STR))` — the NO-FLOAT64 migration
dated **2026-09-13** in its own docstring. The consumer's import was never
updated. **Byte-identical on `origin/main`**, so this is pre-existing, not
branch damage.

And it is invisible to every staleness path: `snappy_cusp_seeding.py`'s
`scriptHash` is `f4733c216049`, its witness records `f4733c216049` — **IN
SYNC** — `computedAt 2026-08-28`, three weeks before the rename. A witness
claiming currency with a producer that cannot be imported.

**So item 1 of this bean has a second blocker its text does not name**, and the
first one is no longer the obstacle. Tracked as **`qou-2cz1`**, with a calibrated
AST audit ([`computations/audits/local_import_resolution_audit.py`](computations/audits/local_import_resolution_audit.py))
that finds this class corpus-wide: **4 unresolved bindings of 5935 checked**, of
which three have **no mechanical replacement** (`_dense_mul` has no candidate of
any name), so no fix is proposed here.

### Still blocked, and still nothing edited in `computations/`

The docstring correction for `snappy_cusp_seeding.py` would drift its
`scriptHash` and its witness cannot be regenerated until `qou-2cz1` is decided.
`q_pochhammer_seed.py`'s docstring half is now unblocked and could land alone —
but the two blocks name the same two dead labels, and splitting them leaves half
the finding wrong in the tree. Left as one unit.

Re-verified on this tree: `pl-jsj-mass-integration-equivalence` **0** carrier
files, `denominator-zeros-as-sw-critical-points` **0**,
`jet-gb-pl-correspondence` **0**, against
`shared-denominator-cusp-holonomy` **6** and
`algebraic-geometric-dilog-equivalence` **5**.
