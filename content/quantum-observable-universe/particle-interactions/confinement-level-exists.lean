import QOU.BraidKnot.ConfinementLevel


/-!
# confinement-level-exists — sibling stub

The canonical Lean source for `prop:confinement-level-exists` lives at
`content/quantum-observable-universe/lean/QOU/BraidKnot/ConfinementLevel.lean`,
which is Lake-built under the `qou` package and declares the structure
`QOU.BraidKnot.ConfinementLevel` together with the theorem
`QOU.BraidKnot.ConfinementLevel.exists`.

This sibling re-exports that module (via `import`) so the content-block
manifest's `lean.ref` (`qou:QOU.BraidKnot.ConfinementLevel.exists`)
resolves cleanly against the Lake tree, without shadowing the real
declaration with a duplicate stub (per AGENTS.md §"No shadowing stubs").

The theorem itself: the set `{ ℓ : T_w ∈ J^ℓ(q) }` is finite,
upward-closed, and nonempty (since `T_w ∈ J^0(q) = H_n(R, q)`
trivially), so its minimum exists.

Ref: [manuscript] braids-and-knots/confinement-level
-/
