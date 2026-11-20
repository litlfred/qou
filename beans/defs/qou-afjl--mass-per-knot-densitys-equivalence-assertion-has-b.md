---
# qou-afjl
title: mass_per_knot_density's equivalence assertion has been RED on main since 2026-08-21 — a commit called it a rename, but the old name now means a different density
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T04:49:12Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

## The claim

`computations/mass-per-knot-density.witness.json` has carried
`allPassed: false` on `main` since **2026-08-21**, on one assertion,
`per_knot_density_equiv_per_knot_density`, at a byte-identical
**`|Δ| = 1139.0`** against a tolerance of `1e-40`. It passed at
**`2.737e-48`** on 2026-06-28. Nobody has looked at it in the seventeen days
since.

**It is NOT a consequence of the 2026-09-06 chi-cache regeneration** — the
figure is identical before and after (`git show 3cc4b2aab1~1:<witness>` and
`origin/main:<witness>` both read `1139.0`). It was found while triaging the
24 witnesses that fail after that regeneration, and it does not belong to that
population.

## What the assertion compares, measured today

```
eq = abs(vol_density_borromean(q) - per_knot_density_vd(vol_borromean(), q))
```

| side | value at the proton q₀ | what it is |
|---|---|---|
| `vol_density_borromean(q)` | **1890.512344814298** | `Vol(𝓑₃)/ℏ_q²` × the **GLOBAL scalar** `linking_weight_family_a(q) = (3q²+4+3q⁻²)/4 ≈ 2.53` |
| `per_knot_density_vd(vol, q)` | **751.4417392804925** | `Vol(𝓑₃)·ρ/ℏ_q²` with `ρ` defaulting to `borromean_markov_trace_h2` — the **PER-BLOCK** H₃ Markov trace |
| ratio | **2.5158468660850124** | |

`_li_2_q_util.py:545`'s own docstring says these two differ **by design**:

> *"This routine multiplies the bare hyperbolic `Geom_leading = Vol(𝓑₃)/ℏ_q²`
> by a GLOBAL scalar … it is NOT the paper's Stage-4 per-block character sum …
> The two differ by ≈ 2.38×; this routine therefore does NOT compute the
> formula in `prop:hoefsmit-scattering-pipeline` Stage 4."*

So the assertion asserts an equality the module's own documentation denies. The
measured 2.5158 against the docstring's "≈ 2.38" is a second, smaller
discrepancy that this bean does not resolve.

## The cause, and why the commit message is misleading

`dfc1cfcde2` (2026-08-21, *"fix: three deferred breaks — a **documented
rename**, and a NameError tested not guessed"*) changed the left side:

```diff
-    eq = abs(per_knot_density_borromean(q) - per_knot_density_vd(...))
+    eq = abs(vol_density_borromean(q)      - per_knot_density_vd(...))
```

**That is not a rename.** Verified at that commit: `_li_2_q_util.py` defines
`vol_density_borromean` at line 402 with the global-scalar docstring, and
`per_knot_density_borromean` **does not exist in the file at all**. The old
name was re-added later as an alias — today
`per_knot_density_borromean is vol_density_borromean` returns `True`, one
function object, and calling the old name emits a `DeprecationWarning` naming
it "the λ_A fit".

So a name that produced the per-block value on 2026-06-28 produces the
global-scalar value today. The rename was semantics-preserving *for the new
name*; it was not semantics-preserving *for the old one*.

## What I did NOT establish, and it matters

I have **not** shown what `per_knot_density_borromean` returned on 2026-06-28.
The measured facts are: the two sides agreed to `2.737e-48` then, differ by
`2.5158×` now, and the only edit to the assertion in between is which function
the left side names. That the old name *meant* the per-block density is the
natural reading and is **inferred, not measured** — checking it needs the
2026-06-28 `_li_2_q_util.py`, which I did not read.

## Blast radius — flagged, not asserted

**29 tracked `.py` files** import or call `per_knot_density_borromean`
(`git grep -ln`, excluding `_deprecated`), among them `canonical_mass.py`,
`canonical_mass_status_guard.py`, `build_proton_mass_50dps_chain.py`,
`m_p_borromean_verification_50dps.py` and `mass_vol_density.py`.

**Do not read that as 29 defects.** Files written *after* the meaning changed
may want the global scalar, and AGENTS.md's own mass banner deprecates
`vol_density_borromean` / `linking_weight_family_a` for absolute mass while
keeping `vol_density_per_block` valid for binding ratios — so several callers
are plausibly correct as they stand. The count is the surface to triage, not a
finding.

## Dispositions

1. **Re-scope the assertion to the ratio.** Assert
   `vol_density_borromean / per_knot_density_vd` against a recorded value with
   a real tolerance, turning a permanently-red equality into a live guard on
   the SU(2) density gap — which is what `compare_density_readings`, already in
   this module, exists to measure. Also settles whether the gap is 2.38 or
   2.5158.
2. **Restore the comparison.** Point the left side back at the per-block
   density, if that is what the assertion was for.
3. **Delete it.** It asserts something the docstring denies.
4. **Leave it red** as a marker.

**Recommendation (judgement, not a finding): 1.** It is the only option that
converts the red into information, it needs no decision about what the old name
should mean, and it forces the 2.38-vs-2.5158 question into the open. What it
does not do is address the 29 callers, which is the larger and separate
question of whether the alias should exist at all.

**Default if nothing is done:** the witness stays red on `main`, and
`check-sidecars.sh` keeps reporting `mass-per-knot-density` for anyone who
touches a file near it — which is how this was found.



## APPLIED 2026-09-07 — owner disposition: re-scope to the ratio

Witness green for the first time since 2026-08-21: **8 assertions, all
passed**.

### Asserted STRUCTURALLY, not against a pinned numeral

`Vol(𝓑₃)/ℏ_q²` is common to both readings and cancels, so the gap is
**exactly**

    global / per-block  =  linking_weight_family_a(q) / borromean_markov_trace_h2(q)

Verified at 60 dps: residual **6.2e-61**. The new assertion
`su2_density_gap_eq_lw_over_trM` checks that identity rather than a recorded
constant — nothing is fitted, it holds for every `q`, and a change in
**either** density function breaks it. That is a strictly stronger guard than
pinning 2.5158 would have been, and it needs no tolerance argument.

The assertion was **renamed**: `per_knot_density_equiv_per_knot_density` no
longer exists, because what it asserted was false and keeping the name over a
different claim is how this arc started.

### The second discrepancy is now IN the witness, not buried

New `su2_density_gap` data block records the measured **2.515846866085011803**
beside the docstring's claimed **≈ 2.38**, with a note saying the two disagree
and are **UNRESOLVED**. Both figures are in the corpus and neither cites the
other; that is left open deliberately rather than silently reconciled.

### Also fixed

A `print` at line 378 still computed the old equality and reported
`|Δ| = 1.14e+3` on every run — the same stale-literal class this bean is
about. It now prints the gap.

### NOT done, and still open

The **29 callers** of `per_knot_density_borromean`. The name resolves to the
global-scalar function and emits a `DeprecationWarning`; whether each caller
wants that reading is untriaged, and files written after the meaning changed
may be correct as they stand.

## The 29 callers are 17, and my own first classification of them was wrong (2026-09-07)

Two corrections, both to figures I was carrying.

**"29 callers" is 29 files MENTIONING THE NAME.** By an AST test — an
`ImportFrom` of the name, a `Call` on it, or a `FunctionDef` of it — the real
figure is **17**. The other **12** carry the name only in a docstring or a
comment, and several do so *precisely because they are documenting that it is
deprecated for absolute mass*: `canonical_mass.py`,
`noncanonical_reentry_audit.py`, `canonical_mass_status_guard.py`. Counting
those as callers inverts what they are. Checked for the forms a bare-name AST
test would miss — attribute calls (`mod.per_knot_density_borromean(...)`),
aliased imports, `getattr` — and there are **0**, so 17 is not an undercount
from that direction.

**My first classification of the 29 was a regex, and it over-flagged.** It put
5 in an "absolute-mass, deprecated route" bucket. Spot-checking three of them
dissolved the bucket:

| flagged file | what it actually is |
|---|---|
| `entanglement_emitted_energy.py` | **self-declaring** — its own header says "DEPRECATED for absolute mass by the 2026-06-24 ruling … it is not the framework's live m_p". Not a defect; the file is honest about exactly this. |
| `casimir_hoefsmit_additivity_probe.py` | **not a caller at all** — the name appears once, in a docstring. |
| `per_knot_density_borromean_q_locality_probe.py` | divides it out: `per_knot_density_borromean(q) / geom_leading`. That is a **ratio**, extracting the linking weight. Flagged only because the file mentions MeV. |
| `vol_density_borromean_q_locality_probe.py` | same shape, same division. |

So the "5 on the deprecated absolute-mass route" figure is **withdrawn**. What
the classifier keyed on was the *word* MeV, not the *use*, which is the same
name-versus-use error as the paragraph above, one level up.

**What remains genuinely open is unchanged and is not a caller question.** The
docstring asserts the global and per-block readings differ by "≈ 2.38×"; the
measured ratio is **2.515846866085011803**
(`su2_density_gap_eq_lw_over_trM` in `mass_per_knot_density.py`, recorded in the
`su2_density_gap` data block, 8/8). That 5.7 % disagreement between a docstring
and its own function is UNRESOLVED and is the substance of this bean. Re-triaging
callers does not touch it.

## The 2.38 is `lw / 1.065` — and naming it does not close the question (2026-09-07)

Measured at the proton q₀, 50 dps. The docstring's "≈ 2.38×" is exactly
`linking_weight_family_a / 1.065 = 2.37819686`. So it is not a bad
approximation of the measured 2.5158 — it is quoting a **different tr_M(𝓑₃)**,
namely **1.065**, which is claimant #4 in the `qou-soj6` tr_M census, recorded
there as UNEXPLAINED and not matched by the cache since 2026-08-29.

**That does not settle which tr_M is right, because there are four computed
candidates and no two agree.** All four come from the *same* Jones polynomial
`V(q²)` of the Borromean rings, over four different normalisers:

| normalisation | tr_M(𝓑₃) | lw / tr_M |
|---|---|---|
| jones `q+2+q⁻¹` = `1/z_C²` | 1.0067304535 | 2.5158468661 |
| wenzl `[2]_q²` | 0.9985621638 | 2.5364266223 |
| `1/z_D²` = `(q²+1)²/q⁶` | 1.5157706817 | 1.6709517389 |
| Lean `trM_borromean(h)`, sorry-free closed form | 0.9999276581 | 2.5329630470 |
| *docstring's quoted value* | *1.065* | *2.3781968605* |

### A defect in my own re-scoping, found by checking the name

`mass_per_knot_density`'s `su2_gap_closed_form` uses **the first row**, and that
is the **excised convention C**. `borromean_markov_trace_h2`'s own docstring
says so and says it is kept **deliberately** as "the ALTERNATIVE-normalisation
comparison column … this function's job IS to be the non-canonical column."
I reached for it last session because the name contains `borromean_markov_trace`
and did not read past that.

**The identity itself is sound** — both sides call the same function, so
`per_knot_density_borromean/per_knot_density_vd == lw/trM` holds under any
normalisation. What inherits convention C is its *interpretation* as "the SU(2)
density gap".

**Not switched to wenzl.** That would swap one unexplained value for another,
and would be exactly the "closest wins" move the anti-fit discipline forbids.
Recorded instead, with the normalisation named in the witness.

### The Lean row is why "wenzl is canonical" is not the answer either

`QOU.BraidsAndKnots.trM_borromean` is **sorry-free** and closed-form,
`(4 + h² − 3h⁴ − h⁶)/(h² + 4)` at `h = 1 − 1/q`. It agrees with **none** of the
three numerically. Wenzl is merely *closest*, at **0.137 %** relative. A
sorry-free closed form sitting 0.137 % from the evaluation it is supposed to be
a closed form **of** is a finding, not a rounding.

All five coincide at `q = 1` — every normaliser equals 4 there and `V(1) = 4` —
so the entire disagreement is an **O(h²) effect** with `h ≈ 0.0991`. That is
consistent with a genuine normalisation difference rather than an arithmetic
slip in any one of them, and it means the discriminator has to be structural,
not numerical.

**Still open**, and now sharper than "a docstring disagrees with its function":
which normaliser does `tr_M(𝓑₃)` take in the canonical chain, and why does the
sorry-free Lean closed form not reproduce it? The table is computed in
`mass_per_knot_density.py` rather than quoted, so it cannot go stale against the
functions it describes.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8319, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
