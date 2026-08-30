---
# qou-mtcx
title: 'TASK: MarkovTraceContext generic base ring — 16 extenders'
status: completed
type: task
priority: medium
tags:
    - lean
    - wall-side
    - 7c
    - refactor
created_at: 2026-08-08T13:00:00Z
updated_at: 2026-08-15T14:43:47Z
---

`lean/QOU/BraidsAndKnots/qmn_recursive_memoized.lean` is a genuine base-ring
candidate that **cannot be ported in isolation**: its class
`QmnRecursiveMemoizedContext extends QOU.Shared.MarkovTraceContext`, so the `ℝ`
would have to be threaded through that shared parent — which **16 classes
extend**.

```
grep -rl "extends QOU.Shared.MarkovTraceContext\|extends MarkovTraceContext" \
  --include=*.lean content/     # -> 16
```

## Why it is worth doing

The Markov trace is the Jones invariant; its algebraic home is `ℤ[q, q⁻¹]`, not
`ℝ`. A generic parent would let every one of the 16 descendants state its
content over the right ring and would take a whole family off the wall-side
queue at once, rather than one block at a time.

## Method

1. Read `lean/QOU/Shared/MarkovTraceClaim.lean` first — it may already be
   `ℝ`-free, in which case the work is only in the descendants.
2. Parameterise the parent, then fix descendants in dependency order.
3. `scripts/lean-direct-cone.sh` per module, `-DautoImplicit=false`. Never
   `lake build`.
4. This is a refactor, not a drain — land it as its own PR with the 16-file
   list in the body.

## Trap recorded

A consumer count of *"appears in 1 `.lean` file"* is what hid this. **A file
count does not measure blast radius when the dependency runs through class
inheritance rather than imports.** Check `extends` edges explicitly.

---

## CORRECTION (2026-08-08) — the premise above is wrong; the parent is already generic

**Step 1 of the Method resolves affirmatively: `MarkovTraceClaim.lean` is
already `ℝ`-free.** There is nothing to parameterise in the parent, and step 2
("parameterise the parent, then fix descendants in dependency order") does not
apply. The parent already bundles the coefficient ring as class fields:

```lean
class MarkovTraceContext where
  R : Type u
  ringR : CommRing R
  invR : Inv R
  q : R
  n : ℕ
  A : Type u
  …
```

So the feared *"the `ℝ` would have to be threaded through that shared parent —
which 16 classes extend"* **does not describe the code**. The `ℝ` lives only in
the descendants: each inherits a perfectly good generic `R` and then ignores it,
declaring its own fields at `ℝ` — and several additionally declare a redundant
`q_real : ℝ` that shadows the inherited `q : R` and is tied to it by nothing.

**Consequence for scoping.** This is a set of independent per-file refactors,
not a signature-threading change. No edit crosses a file boundary; each
descendant is fixable and verifiable on its own.

### The "trap recorded" is half right and half wrong

*Right:* a file count does not measure blast radius when the dependency runs
through `extends`. *Wrong:* here the inheritance edge is what makes the change
**cheap**, not expensive — the parent hands every descendant a generic ring for
free. The blast radius of a *parent* change would indeed have been 15 files; the
blast radius of the change actually needed is one file at a time. The lesson to
keep is narrower than the one recorded: **an `extends` edge is a dependency you
must trace, but tracing it can shrink the estimate as easily as grow it — read
the parent before costing the work.**

### Measured scope (15 descendants, not 16)

The grep matches 16 paths because `MarkovTraceClaim.lean` matches its own usage
example in the module docstring. The parent is not a descendant of itself.

| Verdict | Files |
|---|---|
| already generic (no change) | `explicit_alpha_k_h4`, `pentagon_uv_commutation`, `curvature_rank_gb_stratification`, `exterior_square_borromean` |
| ported to the inherited `R` | `qmn_recursive_memoized`, `y_lambda_recipe_from_partition`, `confinement_categorical`, `antiparticle_crossing_reversal`, `wenzl_qmn_synergy` (partial), `mobius_energy` (`q` only), `wedderburn_bratteli_recursion` (dead fields only) |
| legitimately `ℝ` (§7c wall) | `deuteron_binding_energy`, `reeb_operations_per_planck`, `toffoli_transfer_matrix`, `strangelet_crossing_energy` |

**Not every `ℝ` should go.** A descendant carrying a CODATA value, a
`Real.sqrt`/`Real.log`, or an ordering hypothesis sits *after* the
substrate→archimedean wall and is correctly on `ℝ`. Those four are recorded as
correct, not deferred.

### Method addendum — the idiom for arithmetic over the inherited `R`

`ringR`/`invR` are plain fields, not instances, so `*`, `+`, `1`, `⁻¹` do not
elaborate over `R` on their own. The working in-repo idiom is a `haveI` inside
the field type, already used by `pentagon_uv_commutation`:

```lean
  claim_pentagon_master :
    haveI := ringR; Phi_q v * Phi_q u = Phi_q u * Phi_q (u * v) * Phi_q v
```

`CommRing R` supplies no `Div`, so division is written `a * b⁻¹` through the
parent's `invR` — definitionally what `a / b` unfolds to at `R = ℝ`.

### Method addendum — `-DautoImplicit=false` is load-bearing, and is NOT missing

Without it a bare `chi : ℕ → ℕ → R` in a descendant **auto-binds `R` as a fresh
implicit**, compiles green, and never touches the inherited parent field — a
silent no-op refactor that looks fully verified. Step 3 above is right to
require the flag.

It was *reported* that `scripts/lean-direct-cone.sh` lost the flag in commit
`6d60eb3e2a`. **That report is wrong and should not be acted on.** The commit
moved the flag from the shell script into the Python driver, where it is still
hardcoded and unconditional:

```python
# scripts/lean_cone_build.py:183
["lean", "-DautoImplicit=false", *EXTRA_ARGS, "-o", str(ol), str(mods[m]["src"])]
```

`LEAN_CONE_EXTRA_ARGS` defaults to `-s 65536` and is *additional* to the flag,
not a replacement for it, so overriding the variable cannot switch
`autoImplicit` back on. No fix is required; a pointer comment was added to the
shell script so the next reader does not re-derive the false alarm.


## Verified complete + closed — stalled-claim takeover (2026-08-15)

Taken over per the stalled-claim policy (AGENTS.md work-plan §2, added today): this bean sat `in-progress` for a week with no live branch, and a PR search for MarkovTraceContext / wedderburn_bratteli / wenzl_qmn_synergy / mtcx returned **0 open PRs**. No sibling was on it.

**Finding: the §7c family is already complete; no code change is needed.** All 15 descendants of the (already-generic) parent are accounted for:

- **4 already generic** (no change): explicit_alpha_k_h4, pentagon_uv_commutation, curvature_rank_gb_stratification, exterior_square_borromean.
- **4 legitimately ℝ** (post-wall, recorded correct): deuteron_binding_energy, reeb_operations_per_planck, toffoli_transfer_matrix, strangelet_crossing_energy.
- **7 "port to inherited R" — all done on main:**
  - qmn_recursive_memoized, y_lambda_recipe_from_partition, confinement_categorical, antiparticle_crossing_reversal — no gratuitous ℝ remains (ℝ-hits=0).
  - wedderburn_bratteli_recursion — y_lambda over inherited R; remaining ℝ (ratio / q_content_sign / z_real / diagonal_ratio_n + the ε-N limit) is legitimately archimedean with a §7c banner; z_real is USED (claim_iii), not dead. COMPILE: lean-direct-cone → ok=5.
  - wenzl_qmn_synergy — z : R on inherited ring; the *_speedup : ℝ are measured wall-clock ratios with ≤-comparisons (archimedean, banner'd). COMPILE: ok.
  - mobius_energy — q on inherited R via `haveI := ringR` (q_real shadow removed); energies legit-ℝ (classical functional). COMPILE: ok.

The raw ℝ-hits (4/5/4) were the §7c false-positive trap (already-ported vs legit-archimedean). Content- + compile-verified, no mass-fix, per §7c discipline. Closing completed.
