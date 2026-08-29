# What adopting `lean_decl_scan` changed, measured

Bean `qou-rfq9`. Baselines taken on `main` at `9a52c26c4`, 2026-08-27, before
any edit. Re-measure with `--json` on both detectors and diff by
`(file, decl)`; the selftest (`test_lean_decl_scan.py`) pins every regression
found along the way.

## Headline

| detector | before | after |
|---|---|---|
| `lean-definition-collapsed-audit.py` | 1 CRITICAL / 2047 advisory | **1 CRITICAL / 2100 advisory** |
| `lean-borrowed-name-audit.py` | 19 CRITICAL / 115 major | **25 CRITICAL / 145 major** |

**The borrowed-name figures 19 / 115 were UNDER-COUNTS caused by a bug, and
25 / 145 are the corrected numbers.** They were published in PR #5875, which
has merged; the correction is recorded there and in the audit trail. The
*adjudications* made under the old counts all remain valid — every verdict is
about a named declaration and none of them changed. Only the denominator grew.

Exactly one previously-flagged declaration is no longer flagged and therefore
has an orphaned ledger verdict: `euler_machinery_misses_dt_count`, recorded
`legit`. Harmless — the verdict says the declaration is fine — and kept rather
than deleted, since re-flagging it later should not lose the reading.

## Why the counts moved

### 1. A body ended at the next declaration head, swallowing `end` / `omit`

The single largest effect, and it cuts both ways depending on which detector
you look at.

```lean
theorem trefoil_knot_nontrivial :
    jones trefoil ≠ jones [(1, true), (2, true)] := by decide

end Trefoil          ← was being read as part of the proof
```

With `end Trefoil` inside the body, the proof text is `by decide\n\nend
Trefoil`, which fails both a `proof == "rfl"` test and a "proof is ≤ N steps"
test. `decl_spans` now ends a body at whichever comes first: the next
declaration head, **or** a column-0 line that closes the current one.

Both bounds are needed. Next-decl-head alone swallowed `end`; column-0 alone
truncates a proof whose tactic block is unindented.

`omit [Inst] in` is the same failure in a keyword that is easy to miss: Lean
4's per-declaration instance suppression sits at column 0 *immediately before*
the declaration it modifies, so it lands inside the **preceding** one's body.
Measured: without `omit` in the structural set, `conjOp_apply` and `gram_apply`
— both bare `:= rfl` — stopped being flagged.

Intermediate measurements while getting this right, kept because they show the
size of the effect: next-decl-head alone dropped **163** definition-collapsed
findings; adding column-0 structural keywords brought that to **10**; adding
`omit` brought it to **3**.

### 2. Comments were never blanked in `definition-collapsed`

It parsed raw lines. Two consequences, both real:

- **A declaration quoted inside a docstring was scanned as code.**
  `blochWignerD_real_pos` **does not exist** — it is quoted in a module
  docstring recording that it was *removed* on 2026-08-07 (bean `qou-ir1l`)
  for being exactly the banned tautology pattern. The detector was flagging a
  theorem from its own obituary. Same for
  `strong_duality_axiom_is_inconsistent`, quoted inside a markdown fence in a
  docstring.
- **Comments *inside* a declaration hid its proof.**
  `b3_nf_wedderburn_uniqueness` carries comment lines between its name and its
  statement, and between its statement and its proof. Unblanked, the collapse
  test cannot see `:= rfl`. This one is already adjudicated **genuine** in the
  vacuity ledger by the other detector — so blanking recovers a known true
  positive that `definition-collapsed` structurally could not see.

### 3. The exclusion fired on dot-notation over a value binder

`discharges_via_binder_field` looks for `binder.field` in the proof, to skip
proofs that discharge from a *stated assumption*. Fed **every** binder it also
fires on ordinary dot-notation over a value: `A.choose` where `A : ℕ`,
`l.length`, `n.succ`.

Measured instance: `mu4_unconstrained_below_four` has `{A : ℕ}` and a proof
using `A.choose 4`. The exclusion suppressed it — the right outcome (its real
hypothesis `hA : A < 4` *is* used) for the wrong reason, and over-suppression
anywhere the shape recurs without that luck.

`assumption_binders` now restricts the exclusion to binders that state
something: instance brackets, Prop-ish types (`=`, `≠`, `<`, `∈`, `∀`, `→`, …),
and the `h`-prefix convention. Applying it to the borrowed-name detector moved
**8** items from advisory to `major` (137 → 145) with CRITICAL unchanged.

Both detectors now use the same exclusion semantics. Leaving one on the buggy
version would have defeated the point of sharing the code.

### 4. Anonymous `example` was never scanned

The old `THM` regex required a name after the keyword, so `example : … := rfl`
never matched. 9 of the new definition-collapsed advisories are these. Low
value individually — an anonymous `example` cannot be cited — but it was a
silent blind spot, not a decision.

## What did NOT change

- **The CRITICAL count of `definition-collapsed` is 1 before and after.** Its
  actionable tier is untouched.
- **No verdict flipped.** No finding changed severity in either detector; the
  movement is entirely findings entering or leaving the set.
- The discriminating signals — OPEN-CLAIM and BORROWED/OVERCLAIM — are
  untouched. Only the substrate is shared.

## Known, measured, deliberately NOT applied

**Signal B should probably read `--` comment blocks, not just `/--`
docstrings.** `b3_nf_wedderburn_uniqueness`'s prose says *"Full proof requires
Wedderburn-Artin over R_q"* — a textbook OPEN-CLAIM — but it is in `--`
comments, so signal B cannot see it. Making it visible would change the
`definition-collapsed` **CRITICAL** count, which is the one published tier this
change leaves alone. It should be its own measured decision.
