---
# qou-3kni
title: 'Two conj: labels named by the pole-to-cusp producers have no carrier -- and neither producer can be re-run here to fix the docstring'
status: todo
type: task
priority: normal
created_at: 2026-09-14T19:57:29Z
updated_at: 2026-10-10T06:43:35Z
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
