---
# qou-hdyp
title: 'GAP: Lean the Markov normalisation and trace identity that gate y_lambda'
status: todo
type: task
created_at: 2026-08-10T19:36:18Z
updated_at: 2026-08-10T19:36:18Z
---


## Why this is a GAP bean and not a Lean file

Per AGENTS.md §"When you can't close it — bean the gap": I could not write,
build and verify this Lean inside the remaining session context, and a file
that does not build — or that carries an uncited `sorry`, or concludes `True`
— violates §Strict Lean Discipline. Beaning is the sanctioned exit.

## What to state

Two theorems, the first strictly weaker and already symbolically confirmed.

**1. Markov normalisation** (verified symbolically, n = 2..6, exactly and
identically in q — see `qou-8x1l`):

    ∑ λ ⊢ n, y_λ(q) * dim V_λ = 1

**2. The trace identity** (the real gate; NOT yet verified):

    ∑ λ ⊢ n, y_λ(q) * χ^λ(β, q) = tr_M(β, q)      for every braid β ∈ B_n

Theorem 1 is the β = identity case of theorem 2, since `χ^λ(1) = dim V_λ`.

## Existing infrastructure to extend (do not start fresh)

    QOU/MathlibExt/MarkovTrace.lean          namespace QOU.MathlibExt.MarkovTrace
    QOU.Mathlib.HeckeAlgebra.MarkovTrace     abstract uniqueness class
    QOU.Braiding.HnMarkovTrace.MarkovTraceTower

Base ring: state over generic `{R : Type*} [CommRing R]` / `[Field R]` per
§7c — this is q-deformation combinatorics with no archimedean content, so ℝ
would be a gratuitous specialisation.

## Why it matters (the argument for formalize-first)

The convention-D `y_λ` were validated three ways — Rust `trace_weights_n` at
1.2e-15, all 3+-row weights vanishing, both table evaluations at ~1e-50 — and
**none of those tests the defining property**. Each compares the weights
against another implementation or a shared convention. Eight hypotheses were
raised and refuted chasing an 8.71e-8 Schur-Weyl residual before anyone
checked whether `Σ y_λ·dim = 1` at all. It does. Had theorem 1 been Lean from
the start, seven of those eight rounds were unnecessary.

Theorem 2 is where the surviving 8.71e-8 lives: with the weights now
vindicated, the residual must be in `χ^λ(β_D)` or in the peel recursion on
that specific braid.

## Note on process

The pre-create existence check returned a non-zero match count and I created
the bean before inspecting it. The two matches turned out to be unrelated
(`qou-78pt` A1 volume term, `qou-840k` float64 excision — my grep hit body
text, not titles), so this is not a duplicate. Wrong order all the same; the
check exists to be read, not counted.

## Build infra RESTORED and verified (2026-08-10)

`lake-cache/qou-v4-24-0` restored: 1.65 GB, **6990 oleans** (well above the
~2919 the skill doc cites). Toolchain `leanprover/lean4:v4.24.0` already
present. Total ~3 min, against a 30-60 min from-source Mathlib build.

**Working `lean`-direct recipe — note the `lean/` component:**

```bash
export PATH="$HOME/.elan/bin:$PATH"
LP=$(ls -d .lake/packages/*/.lake/build/lib/lean | tr '\n' ':')   # 8 dirs
LEAN_PATH="$LP" lean <file>        # exit 0 = checks, sorry-free
```

`lean-environment-setup.md` implies `.lake/build/lib`; on v4.24.0 the oleans
are under `.lake/build/lib/**lean**/Mathlib/...`. Using the documented path
fails with *"unknown module prefix 'Mathlib'"* even though 6990 oleans are
present — a confusing failure that looks like a bad restore rather than a bad
search path. Smoke-tested: a `CommRing` lemma importing
`Mathlib.Algebra.Ring.Defs` compiles, exit 0.

**Do NOT `lake build` to verify.** It re-resolves the dep graph, rebuilds
Mathlib from source, and drops the restored oleans (~40 min lost, per the
skill doc's own history note). `lean`-direct is the verification path.

Next agent: environment is ready; write theorem 1 and check it with the
recipe above. Re-seed the cache branch if a build materially extends it.
