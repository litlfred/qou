# Lean environment probes

Probes that answer *"does Mathlib have X?"* by **enumerating the Lean environment**,
not by grepping source.

## Why this directory exists

In this sandbox `.lake/packages/mathlib` holds **6990 oleans and zero `.lean` files** —
the toolchain is restored from the `lake-cache/*` orphan branch, which carries compiled
artifacts only. So

```sh
grep -r "Bruhat" .lake/packages/mathlib/Mathlib/     # ← ALWAYS returns nothing
```

returns nothing **whatever the answer is**, and `ls` on a Mathlib source path likewise
prints nothing rather than erroring. A negative from either is **silence, not evidence**.

An agent that greps Mathlib source here and reports "not in Mathlib" has measured its own
checkout. That happened on 2026-09-05 (bean `qou-phir`): a "Mathlib has no Bruhat order"
claim reached an audit doc and a commit message on the strength of a grep over
`Mathlib/GroupTheory/Coxeter/`, a directory that does not exist in this tree.

## The method that does work

Import the relevant modules and enumerate `env.constants` by name:

```sh
export PATH="$HOME/.elan/bin:$PATH"
LP=""; for d in .lake/packages/*/.lake/build/lib/lean \
                folio/quantum-observable-universe/lean/.lake/build/lib/lean; do
  [ -d "$d" ] && LP="$LP:$d"; done
LEAN_PATH="$LP" lean scripts/lean-probes/mathlib-bruhat-absence-probe.lean
```

`mathlib-bruhat-absence-probe.lean` reports, as of 2026-09-05 / Mathlib on toolchain
`lean-v4.24.0`:

```
Coxeter constants reachable: 439
  containing 'ruhat' : 0
  containing 'ubword': 0
```

Corroborated independently by a **filename** check, which is valid because the olean tree
is real: `find .lake/packages/mathlib -iname '*bruhat*'` returns nothing, and the only
Coxeter oleans are `Matrix`, `Inversion`, `Basic`, `Length`.

**Scope of that negative.** It covers what is reachable from the two Coxeter imports
(their whole transitive closure). A Bruhat order in some module neither imports would not
be seen — but it would also have an olean, and there is none.

## Reusing this

Copy the probe and change the two substrings. Report the *reachable* count alongside the
hit count: `439` is what tells a reader the probe was looking at a populated environment
rather than an empty one.
