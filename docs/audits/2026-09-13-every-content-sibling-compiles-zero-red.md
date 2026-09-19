# Every content-block `.lean` sibling compiles: 938/938, 0 RED

**Date:** 2026-09-13
**Beans:** `cscb` (EPIC), `qou-e7xv`, `qou-xdwp` — and companion to `qou-g5sp`
**Branch:** `claude/orphan-premise-drain-2026-09-13`

## The result

```
=== swept 938, RED 0 ===
```

`scripts/lean-content-sweep.sh` over every content-block `.lean` sibling —
every `content/**/*.lean` outside the `lean/` package trees. **938 targets,
every one `exit 0` with zero `: error:` lines.**

| paper | targets |
|---|---|
| quantum-observable-universe | 902 |
| unital-groebner-bases | 22 |
| fred2005-formal-groups | 12 |
| visualizer | 2 |
| **total** | **938** |

Note the last three rows: this sweep covers the **UGB and fred2005 content
siblings**, which `scripts/lean-library-sweep.py` does not reach (AGENTS.md
records that limit). No previous count in the corpus spans them — `qou-e7xv`
measured 908 and `cscb` 892, both QOU-only.

## What settles

Three open beans assert a failing population in this exact corpus, and they
disagree with each other by two orders of magnitude.

| bean | status before | asserts | measured 2026-09-13 |
|---|---|---|---|
| `cscb` (EPIC, **priority high**) | in-progress | **~57 %, ~300+ of 892** do not compile standalone | **0** |
| `qou-e7xv` | todo | 38 of 908 (4.2 %), driven to **1** | **0** |
| `qou-xdwp` | todo | 2 files, architectural blockers behind the parse errors | **0**, and both blockers resolved — see below |

Also confirmed green, each named explicitly in a bean that has since been
closed by someone else, so this is independent corroboration rather than news:

- `spin-involution-lp-dual-invariance` — `qou-e7xv`'s single survivor, 22–24
  errors, left alone as an author judgement call (`qou-0xrn`).
- The four `qou-isps` reds outside `qou-e7xv`'s list — `confinement-level-exists`,
  `euler-char-stability`, `localized-knot`, `qz-bicompletion`.
- `qou-29pv`'s two knot-factor files — `knot-factor-borromean-composite` (its
  prescribed one-line `import Mathlib.Data.Real.Basic` is in place at line 1)
  and `knot-factor-shell-closed`.

## `cscb`'s 57 % is NOT shown to have been wrong — say which claim you mean

This sweep establishes that the population is green **now**. It does **not**
re-run `cscb`'s June measurement, and nothing here is evidence that ~57 % was
wrong on 2026-06-28. The likeliest reading is the boring one: `cscb` was right,
and the intervening 2.5 months of repair work — `qou-e7xv`'s five passes,
`qou-0xrn`, `qou-8qby`, `qou-xdwp`, `qou-isps`, `qou-29pv` and their siblings —
closed it.

The defect is not the measurement, it is the **title**: an EPIC at
`priority: high` whose one-line summary still reads *"~300+ files, ~57%"*, which
is what an agent triaging the backlog sees. Its own "Done when" is
*"Every content-sibling `.lean` compiles standalone (`lake env lean` exit 0), or
the residue is a small, documented set of genuinely-hard cases tracked as child
beans."* The first disjunct is met, with no residue.

## `qou-xdwp`'s two architectural items — verified at the files, not from a bean

That bean explicitly separates its mechanical fixes from what it calls the
architectural blockers, one per file. Both are resolved, and I checked the
source rather than trusting `qou-e7xv`'s account of having fixed them (AGENTS.md:
*"a sibling's bean is not a primary source either"*).

**`vertex-operator.lean` — "`ReebBundle` is not in scope", a sibling this file
structurally cannot import.** Resolved by carrying it as a **type parameter
`B`**. The file's own docstring (lines 45–59) records the §7c wall issue the
bean predicted would bite on a naive promotion: `structure ReebBundle (q : ℝ)`
is archimedean while this file is categorical over `R_q = ℤ[q, q⁻¹]`, so
`B := ReebBundle q₀` is the instantiation *after* the τ functor. And
`ope_is_skein` is a `theorem` at line 102 — the bean recorded it as a bare
`axiom`.

**`categorical-transfer-matrix.lean` — "an undetermined implicit",
`base : ExceptionalDivisor` not a parameter of the structure.** Resolved the
same way, a type parameter `B`, with the rationale at lines 84–89.

**And the axiom question the bean asked to settle in the same pass, was.**
It flagged that the blocked declaration is `axiom
transfer_matrix_level_independence`, one of four provable-kind blocks whose Lean
is a bare `axiom`. The file now carries `level_independence_false_as_stated`
(line 153) — a *refutation* — and `transfer_matrix_level_independence` as a
`theorem` (line 183). The bean asked for "not two passes"; it got one.

## Method, and why this green is not a silent skip

- **Flags.** `LEAN_OPTS="-DautoImplicit=false -s 65536"`, set by the script
  itself. A bare `lean` is a strictly weaker check than Lake — it does not read
  the lakefile, and `autoImplicit` defaults *true* in `lean` and *false* in both
  lakefiles, so an unbound identifier is silently auto-bound rather than
  erroring (`qou-56qy`). This sweep does not have that hole.
- **Positive control.** A deliberately false `theorem bogus : 1 = 2 := rfl`
  compiled through the identical command and `LEAN_PATH` returns **exit 1, 2
  errors**. So the harness reports RED when RED exists, and 938/0 is a measured
  green rather than an invocation that did nothing. Every target also produced
  its own log file (939 logs for 938 targets).
- **No `lake`.** The sweep hardlinks the olean tree into a shadow and compiles
  into it, so the restored cache cannot be evicted.
- **Timing.** 260-module shadow rebuild (serial), then the 938 targets in
  **~24 minutes** at `-j 2`.

## Scope — the one real conditionality, and what removes it

The shadow rebuilds from source only the modules whose own olean predates their
own last source commit: **260 rebuilt, ~2532 trusted**. So a trusted module's
correctness is assumed from the snapshot, which is the standing
snapshot-conditionality of `qou-56qy`.

**The companion run removes it.** Earlier the same day, on the same container,
`scripts/lean-library-sweep.py --all` judged **2836 of 2836** library modules
with *nothing* trusted — every module rebuilt from source — at **0 RED**
(`docs/audits/2026-09-13-every-library-module-compiles-zero-defects.md`). That
is exactly the population this sweep trusts. Taken together the two runs leave
no library module assumed rather than compiled.

Residual conditionality is against **Mathlib** only, and the eight
`missing Mathlib olean` reds AGENTS.md records for the full content sweep did
**not** occur here — this container has the gap oleans restored from
`lake-cache/qou-v4-24-0-mathlib-gap-modules`.

**Branch, stated because the sweep ran on it:** the tree differs from `main`
`16ccc3f7e2` only by a docstring in `QOU/Mathlib/Summary.lean` plus bean and
audit-doc text. No declaration, statement or proof term differs.

**Container-scoped, as always.** The dirty closure was **260** here against the
**74** AGENTS.md quotes for a different container — a second data point for its
own note that the closure is a property of the container, not of the corpus.

## One thing found in passing, worth its own bean

The shadow-rebuild phase of `scripts/lean-shadow-verify.sh` is **serial** — one
`lean` at a time — while the target-compile phase that follows it is parallel.
On this 4-core container that left 3 cores idle for the whole rebuild. Not
fixed here (it is someone's arc, and a parallel topological rebuild wants care
about ordering), and not urgent: the rebuild is a one-off per shadow, and
`SHADOW=` reuses it across runs.
