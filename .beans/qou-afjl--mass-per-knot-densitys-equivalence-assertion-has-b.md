---
# qou-afjl
title: mass_per_knot_density's equivalence assertion has been RED on main since 2026-08-21 — a commit called it a rename, but the old name now means a different density
status: todo
type: task
priority: normal
created_at: 2026-09-07T04:49:12Z
updated_at: 2026-09-07T04:50:02Z
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
