---
# qou-7t1n
title: 'GAP: b1_hyperbolic_rows made the QOU library inconsistent (FIXED); audit the same shape elsewhere'
status: todo
type: task
created_at: 2026-08-08T17:15:19Z
updated_at: 2026-08-08T17:15:19Z
---


## The library was inconsistent

`QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean` carried

```lean
axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : ℕ)
    (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified
```

**Every binder is universally quantified, including the count.** So it
asserts `3 ≤ n` for *every* `n : ℕ`, given *any* two `Prop`s:

```lean
theorem b1_axiom_is_inconsistent : False := by
  have h : (3 : ℕ) ≤ 0 := b1_hyperbolic_rows 0 True True trivial trivial
  omega
```

Compiled, exit 0, `#print axioms` naming `b1_hyperbolic_rows` as the only
non-standard dependency. This is **not** the vacuity class — it is `False`.
Every statement in the import cone of `QOU.AppendixSurreals` was provable.

Blast radius: one importer, `QOU/AppendixSurreals.lean` (the aggregator), so
in practice everything that pulls in the AppendixSurreals module.

## Fixed (PR on branch claude/axiom-triage-batch3-2026-08-08)

Stop quantifying over what was meant to be fixed:

- `BlochSuslinRegulator`, `VanDerVeenVolumeConjecture` — named `opaque Prop`s,
  not bound `Prop` variables.
- `HyperbolicRow` — an enumerated type (`borromean | whitehead | twistKnot`)
  with `deriving Fintype`, not an anonymous numeral.
- `b1_holds_at_row` — the conjecture, per row: conditional on the two inputs,
  `B1HoldsAt r` for each `r`. This is where the content lives and it is
  falsifiable.
- `b1_hyperbolic_rows` — now a **theorem**, deriving
  `3 ≤ card {r | B1HoldsAt r}` from the per-row conjecture plus
  `Fintype.card HyperbolicRow = 3`.

Note the near-miss: defining `nVerified := 3` and keeping `3 ≤ nVerified`
would have traded unsoundness for vacuity (`3 ≤ 3` is `rfl`). The count has to
be *derived*, not named.

The exploit no longer typechecks. Verified with `scripts/lean-verify-cone.sh`:
the file and its importer exit 0.

## Detector extended — and three parsing bugs that each hid a real defect

`scripts/lean-one-sided-binder-audit.py` now reports two signals. Corpus is
clean (0 UNSOUND) after the fix; self-test 5/5 pins both real defects and both
false positives.

Getting it to catch B1 took three fixes, each worth remembering because each
one *silently* produced a confident wrong answer:

1. **Order relations.** The detector split only on `=`. A one-sided `=`
   collapses; a one-sided `≤` over an unconstrained numeric binder is
   *unsound*. Now splits on `≤ ≥ < > =`.
2. **Binder form.** It matched only `axiom f : ∀ (n : ℕ), …`. B1 used
   `axiom f (n : ℕ) : …` — binders before the colon — so the file was skipped
   outright. Both forms now handled.
3. **Name-length cap.** A `len(var) > 3` heuristic, tuned for the `z`/`q`
   collapse cases, excluded `n_hyperbolic_rows_verified` (26 chars). The cap
   now applies to the COLLAPSE signal only.

Plus a fourth, caught in review of my own output: without comment stripping,
the scanner read the *docstring* of the fixed file — which quotes the old
axiom in a ```lean fence — and re-reported it as live. Comments are stripped
before scanning.

## Follow-up

The corpus is clean for *this* shape, but the shape generalises past what the
detector covers:

- Non-relational conclusions with an unconstrained binder (`P n` for all `n`
  where only one `n` was meant).
- Conclusions behind `∃`, which the splitter does not descend into —
  `weierstrass_diff_eq_axiom` was that variant and needed a human read.
- Statements where the binder *is* constrained, but only vacuously.

More generally: **`#print axioms` is not a soundness check.** It reports which
axioms a proof depends on, not whether those axioms are jointly satisfiable.
Nothing in this repo checks the latter. A cheap partial guard would be a CI
declaration `example : False := by exact? ` — or simply attempting `False`
against each library module — but that is not currently done anywhere.
