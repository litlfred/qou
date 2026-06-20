# Gap-2 (periodic-table ordering) synthesis — the ℓ-coefficient `a` is bracketed, never `+1`

**Date:** 2026-06-20
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Combines:** #2348 (this, `[2ℓ+1]_q` penetration) + **#2531 (merged)** (eigenvalue-split
ℓ-grading). **Class:** structural synthesis (formalize-first, decisive negative).

## The reduction

Both probes converge on a single dimensionless number — the **ℓ-coefficient `a`**
in the filling key `K(n,ℓ) = n + a·ℓ`. The 3d/4s crossover (the Ar→Kr
discriminator) needs `a > 1/2`; Madelung (`n+ℓ`) is `a = +1`. The canonical
structure offers **two gradings of opposite sign, neither equal to `+1`**:

| grading | object | ℓ-coeff `a` | sign | 3d/4s crossover |
|---|---|---:|:--:|:--|
| eigenvalue split (**#2531**, merged) | `|λ₋|^ℓ ~ q₀^{−2ℓ}` (sub-dominant transfer magnitude) | **−2** | wrong | no (high-ℓ fills *earlier*) |
| **Madelung target** | — | **+1** | — | yes (4s before 3d) |
| angular q-dim (**#2348**, this) | `[2ℓ+1]_q` (bar-even Markov loop weight) | **> +1** (overshoots) | right | over-separates |

## What each probe established

- **#2531 (merged):** the eigenvalue split — the same object that yields the
  `2(2ℓ+1)` capacity — gives `a = −2`, fixed by `|λ₋|/λ₊ = 1/q₀²`. Wrong sign
  (anti-penetration). So **penetration is not the eigenvalue split.**
- **#2348 (this):** the bar-even q-dimension `[2ℓ+1]_q` gives `a > 0` — the
  **right** sign — but overshoots `+1` at canonical scales (my earlier "~8.5×"
  was the `z²` convention; the robust facts are *sign positive*, *magnitude
  > Madelung*). Crucially, `[2ℓ+1]_q` is **also** the capacity object (the
  self-square `[n]_q² = Σ[2ℓ+1]_q` gives `2n²`). So **capacity *and* the
  penetration *sign* are both bar-even (cosh)** — one object — while the
  eigensplit *magnitude* (the other real form) carries the wrong sign.

## Verdict (decisive, sharply localized)

The structure **brackets** Madelung's `a = +1` — `−2` below (eigensplit),
`> +1` above (q-dim) — but does **not pin** it. Hitting `a = +1` means
interpolating/tuning between the two structural gradings, i.e. **fitting** (the
discipline-forbidden move). Therefore:

> **Periodic-table ordering (Gap 2) is not derivable from the canonical
> structure without a tuned ℓ-coefficient.** It is localized to the single
> number `a`: the structure gives `{−2, >+1}`, Madelung needs `+1`.

This is a *clean* negative, not a vague gap. It also dovetails with the
bar-parity picture: the bar-even (cosh) sector carries capacity + penetration
sign; the magnitude/`a=+1` balance is the one un-derived input. (Consistent with
Madelung being semi-empirical even in standard QM.)

## Status of the two gaps (combined, this session)

| | gap | verdict |
|---|---|---|
| **capacity** `2n²` | Gap 1 | self-square `[n]_q²` of the bar-even element — **essentially derived** (no second SU(2); owner-corrected) |
| **ordering** (Madelung) | Gap 2 | reduced to the single ℓ-coefficient `a`; structure brackets `{−2, >+1}`, Madelung needs `+1` — **not derivable without tuning** (this synthesis + #2531) |

## Correction to my earlier framing

My `2026-06-20-madelung-from-sdp-falsifiable-test.md` framed the open piece as
"the radial:angular scale *balance*." #2531's sign analysis sharpens it: the
issue is the **ℓ-coefficient `a`** (sign + magnitude), and the structure offers
`−2` and `>+1` but not `+1`. The "balance" is the magnitude half; #2531 added the
decisive sign half. (My "~8.5× overshoot" was the `z²` convention — convention-
dependent in magnitude, but the *sign-positive, >+1* conclusion is robust.)
