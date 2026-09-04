# `conj:shell-transition-knot`: the ref pointed at a namespace that does not exist, and the sibling is the anti-pattern its own library file forbids

**Date:** 2026-09-03 · **Beans:** `qou-prop3b`, `qou-hprp` · **PR:** litlfred/qou#6426

## 1. The fix that landed: a wrong `lean.ref`

`knots-particles-confinement/shell-transition-knot.ts` declared

```ts
lean: { ref: "qou:QOU.Braiding.stability_pairs_correct" }
```

**There is no `QOU.Braiding` namespace anywhere in the sibling** — the file
declares no `namespace` at all, so `stability_pairs_correct` and its fifteen
companions sit in the **root** namespace. The ref named a path that does not
exist.

Meanwhile the real axiomatisation was already in the library, at
[`lean/QOU/Conjectures/ShellTransitionKnot.lean`](../../content/quantum-observable-universe/lean/QOU/Conjectures/ShellTransitionKnot.lean):
`class BorromeanQuark` (line 70, field `crossingNumber = 3`) and
`class ShellTransitionKnot [BorromeanQuark]` (line 88, field `closures_match`),
with the dependency threaded through the type and **no instance supplied**.

Repointing the ref to `qou:QOU.Conjectures.ShellTransitionKnot` lets the
propagation audit's route (b) resolve it. Measured, whole-corpus:

| | before | after |
|---|---:|---:|
| violators | 29 | **25** |
| conditional-on-class | 135 | 138 |

The four that cleared are `prop:hook-weight-derivation`,
`prop:mass-formula-regime-switching`, `thm:frobenius-codim-universal` and
`thm:knot-mass-formula-unified` — exactly the blocks `conj:shell-transition-knot`
was blocking. They clear **honestly**: the class genuinely exists, its fields
carry content, and it has no instance, so the conjecture is still open and the
four are correctly *conditional*.

**Accounting note, because the axiomatised count did not move.** It reads 165
both times, because in the same window a sibling agent promoted
`conj:tower-geometric-lower-bound` to `prop:tower-geometric-lower-bound`
(commit `53945eef2c`, *"TowerGeometricLowerBound carries a threshold, and is
inhabited"*), which removed it from the conjecture population entirely and took
its one violator with it. So **this repoint accounts for 4 of the 29 → 25**, and
the rest of the bookkeeping is someone else's progress. Do not read the whole
delta as this change.

## 2. What was found on the way, and NOT fixed here

The sibling `shell-transition-knot.lean` does the exact thing the library file's
own closing comment forbids.

**The library file (correct):**

> *"A `mockCorrectedClosure` that hardcodes `{2,8,20,28,50,82,126}` and
> discharges `closures_match` by `decide` is FITTING the answer into a lookup
> table, not deriving the spin–orbit correction from the three Borromean
> crossings — precisely the anti-laundering pattern the rule forbids."*

**The sibling (lines 66–82):**

```lean
def stabilityPair : ℕ → ℕ
  | 0 => 2 | 1 => 8 | 2 => 20 | 3 => 28 | 4 => 50 | 5 => 82 | 6 => 126 | _ => 0

theorem stability_pairs_correct :
    [stabilityPair 0, …, stabilityPair 6] = [2, 8, 20, 28, 50, 82, 126] := by
  decide
```

The seven magic numbers are **hard-coded into the definition** and the "theorem"
reads them back. `decide` closes it because it is `rfl` in disguise. This is
AGENTS.md §"Derive, then check — never fit" and §5's ban on tautological
conclusions: *"the Lean statement must derive the value from upstream axioms /
proved lemmas, not assert the value and prove `rfl`."*

Only the first four values are linked to anything (`first_three_eq_ho`,
`fourth_pair`). **`50`, `82` and `126` — the three that would actually test the
mechanism — are connected to nothing.** `observedStabilityPairs` then stores the
same list a second time.

**And the file does not establish its own headline.** Its header comment asserts
*"The 3 crossings of B_3 set the shell-transition threshold at N ≥ 3"*, and the
`.md` says *"The empirical threshold is N ≥ 3, matching the 3 Borromean
crossings."* The only theorem about the criterion is

```lean
theorem so_exceeds_spacing (N : ℕ) (hN : N ≥ 1) : soStrength 3 N > 2 * (N + 1)
```

— the criterion is satisfied from **N ≥ 1**, and the docstring concedes it:
*"(but empirical threshold is N ≥ 3 due to gap structure)"*, a gap structure
formalised nowhere. The `3` enters only as `def borromeanCrossingNumber := 3`
inside `def isShellTransition N := N ≥ 3`. It is a definition, not a derivation.

## 3. Disposition

**Not done here, deliberately.** The sibling duplicates the library file's HO
content (`hoShellSize`, `hoCumulative`/`hoClosure` and the closure theorems exist
in both) while adding the lookup table the library file refuses. AGENTS.md §0a
*"🚫 No shadowing stubs"* covers exactly this shape — when the real formalisation
lives at the Lake path, do not keep a sibling that shadows it — so the indicated
move is to preserve what is genuinely new (`ho_spacing`, `so_exceeds_spacing`,
`shellTransition_threshold`) into the library file and delete the sibling, the
way `qou-scrx` handled `scratch_skein.lean`.

That is a content decision with a visible blast radius (the block's rendering
resolves through the sibling first), and it removes a `theorem` some reader may
be citing. It is left for the owner rather than taken unilaterally. Note the ref
repoint above stands on its own and does not depend on it: route (a) finds no
class in the sibling and falls through to the library either way.
