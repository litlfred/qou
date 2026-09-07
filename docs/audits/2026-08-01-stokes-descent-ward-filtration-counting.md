# Stokes-matrix categorical descent + Ward↔filtration counting — verdict

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-08-01  **Bean:** qou-yju0  **PR:** #4525
**Branch:** `claude/stokes-descent-ward-filtration-scaffold-2026-08-01`
**Scope:** structure-side complement to the resurgence numerics
(PR #4521 qou-fgte `A_ω=3` identification; PR #4519 qou-dri7 resummation).
This is **analysis + scaffold, NOT a claimed closure.** No `Δ_λ` / `c_k`
wired to production.

## TL;DR verdict

The Ward↔filtration viewpoint **does not close** the `Δ_λ` derivation gap by
counting alone. It **proves a genuine partial closure** — the gauge-invariant
Markov trace forces the magnitude pairing `|Δ_λ| = |Δ_{λ'}|` (over-determined)
— and **relocates** the residual gap, *sharply*, to two categoricity questions,
both open:

1. Is the chirality **sign** forced (the imaginary Stokes phase `±i`)?
2. Are the bar-orbit **magnitudes** categorical `q`-dims/integers (the
   `A_ω = 3` question qou-fgte probes)?

A rigorous "it relocates, doesn't close" is the honest result. The relocation
is exact and machine-checked.

## (A) Stokes-matrix descent — proved sorry-free (generic `[CommRing R]`)

Lean: [`StokesMatrixDescent.lean`](../../content/quantum-observable-universe/lean/QOU/Resurgence/StokesMatrixDescent.lean).
The resurgent Stokes/connection matrix `S` transforms by conjugation
`S ↦ g S g⁻¹` under a gauge/basis change.

| Claim | Lean decl | Status |
|---|---|---|
| A.ii — trace conjugacy-invariance `tr(g S g⁻¹) = tr S` (the gauge-invariant Markov trace `tr_M(S)`) | `stokes_trace_conj_invariant` | **proved sorry-free** (trace cyclicity, `Matrix.trace_mul_comm`) |
| A.i — `Sₙ`/Wedderburn equivariance ⇒ block-diagonal `S = Σ_λ e_λ S e_λ` | `stokes_block_diagonal` (+ `offblock_zero`) | **proved sorry-free** (orthogonality + completeness of the central idempotents; general `[Ring A]`, subsumes `Mat_n(R)`) |
| trace = sum of per-partition block traces `tr_M(S) = Σ_λ tr(e_λ S e_λ)` | `stokes_trace_block_sum` | **proved sorry-free** |

The archimedean summation choice (median vs lateral) is the *only* `ℝ`-part;
it stays **outside** the generic-ring scaffold (§7c) and is listed open below.

## (B) The Ward↔filtration counting probe — decidable, proved

Lean: [`WardFiltrationCounting.lean`](../../content/quantum-observable-universe/lean/QOU/Resurgence/WardFiltrationCounting.lean).

**Model.** Gauge invariance order-by-order (Slavnov–Taylor/Ward) gives linear
relations among the Stokes constants. The bar-/gauge-invariant observable is
the conjugacy invariant `tr_M(S)`, which — being constant on bar-orbits
(`λ ↔ λ'` conjugate partitions) — supplies exactly one datum per **bar-orbit**.
So at body/jet order `n`:

* `#(Ward-free bar-invariant Stokes constants)` `= barOrbits(n) = (p(n)+sc(n))/2`
  (self-conjugate fixed points + chiral pairs),
* `#(Δ_λ to fix)` `= deltaCount(n) = p(n)` (one per partition),

with `p(n)` = partitions of `n`, `sc(n)` = self-conjugate partitions
(= partitions into distinct odd parts, the bar-involution fixed points).

**The counts (proved by `decide`, `delta_split`/`overdetermined`):**

| `n` | `p(n)` (`#Δ_λ`) | `sc(n)` | `barOrbits` (Ward-free) | `chiralPairs` (deficit) | verdict |
|----|----|----|----|----|----|
| 2 | 2 | 0 | 1 | 1 | free < needed ⇒ **over-determined** |
| 3 | 3 | 1 | 2 | 1 | over-determined |
| 4 | 5 | 1 | 3 | 2 | over-determined |
| 5 | 7 | 1 | 4 | 3 | over-determined |
| 6 | 11 | 1 | 6 | 5 | over-determined |
| 7 | 15 | 1 | 8 | 7 | over-determined |
| 8 | 22 | 2 | 12 | 10 | over-determined |

Exact accounting (proved): `p(n) = barOrbits(n) + chiralPairs(n)`.
`barOrbits(n) < deltaCount(n)` for every `2 ≤ n ≤ 8` (`overdetermined`), and the
deficit is exactly `chiralPairs(n) > 0` (`deficit_eq_chiralPairs`,
`chiralPairs_pos`).

**Reading (honest, two-part).**

* **Over-determined on the magnitudes ⇒ a real partial closure.** The
  bar-invariant trace supplies fewer independent data (`barOrbits`) than there
  are `Δ_λ` (`p(n)`). The system is over-determined, so the `Δ_λ` are *forced*
  to satisfy `chiralPairs(n)` relations — the magnitude pairing
  `|Δ_λ| = |Δ_{λ'}|`. This is a genuine, machine-checked structural constraint
  the viewpoint delivers.
* **The deficit is exactly the SIGN.** The `chiralPairs(n)` degrees of freedom
  the trace cannot see are precisely the chirality signs — the mixed-sign
  structure of `Δ_λ` (n=3: 1+/2−) that the **PROBE-4 KL-positivity prune**
  already showed the non-negative KL weights cannot supply. So counting closes
  the magnitudes and leaves the signs open; it does **not** close the full
  `Δ_λ`.

## (B.2) Filtration-coincidence carrier — conditional on `[TwoFiltrationBridge]` (§3b-cond)

`WardFiltrationCoincidence` (OPEN, content-bearing, no instance): posits the
perturbative (Ward) order coincides with the bridge's jet/iterated-integral
depth `dII` on every partition. It **assumes** `[TwoFiltrationBridge]` (the
`dGB = jet` bridge is itself conditional — no global instance in the corpus)
and threads it as an instance hypothesis. From the two hypotheses,
`selfconj_pertOrder_two` is **derived sorry-free** (self-conjugate cell ⇒
perturbative order 2), demonstrating §3b-cond non-degeneracy. What it assumes:
that dGB = jet = perturbative-order actually coincide — the open conjecture.

## (Sign source, PROBE-4) The imaginary Stokes phase supplies the sign

`StokesPhaseSign` (OPEN carrier, generic `[CommRing R]`, no instance): the
`±i` Stokes discontinuity's real shadow is a sign `sign μ` that **squares to
`1`** (`sq_one` — not literal `∈ {±1}`, which is strictly stronger over a
generic `[CommRing R]`; PR #4540 identifies the concrete sign as the a-function
parity `(-1)^{n(λ)}`, genuinely `±1`) and **flips under the bar-involution** on
chiral pairs. `chiral_sign_cancels` is
**proved sorry-free**: `sign μ + sign(conj μ) = 0`, i.e. the bar-invariant
trace cannot see the sign — matching the `chiralPairs` deficit exactly. This
scaffolds the sign source (does not assert the physics forces it).

## Proved / open split (auditable boundary)

| Assertion | Disposition |
|---|---|
| `tr(gSg⁻¹) = tr S` (A.ii) | **proved sorry-free** — `stokes_trace_conj_invariant` |
| Wedderburn-equivariance ⇒ block-diagonal (A.i) | **proved sorry-free** — `stokes_block_diagonal` |
| `tr_M(S) = Σ_λ tr(e_λ S e_λ)` | **proved sorry-free** — `stokes_trace_block_sum` |
| counting verdict `barOrbits < p(n)` (over-determined), `2≤n≤8` | **proved sorry-free** — `overdetermined` (`decide`) |
| deficit = `chiralPairs(n)` = uncaptured sign DOF | **proved sorry-free** — `deficit_eq_chiralPairs`, `delta_split` |
| bar-invariant trace cannot see the sign | **proved sorry-free** — `chiral_sign_cancels` |
| `dGB = jet = perturbative-order` coincidence | **conditional-on-[TwoFiltrationBridge]** carrier (open; no instance) — `WardFiltrationCoincidence` |
| Stokes-phase sign is forced `±i` (sign categoricity) | **OPEN carrier** (bean qou-yju0) — `StokesPhaseSign`, no instance |
| bar-orbit magnitudes are categorical `q`-dims (`A_ω=3`?) | **OPEN** — relocated to qou-fgte (PR #4521) |
| archimedean summation-independence (median vs lateral) | **OPEN**, archimedean (outside generic-`R` scaffold) |

## Why this is a win, not a dead end

The counting is genuinely over-determined (`decide`-proved), so the viewpoint
is *not* vacuous: it forces the `|Δ_λ|=|Δ_{λ'}|` magnitude relations. But the
uncaptured DOF are exactly `chiralPairs(n)` **signs**, and the bar-invariant
trace provably cannot see them (`chiral_sign_cancels`). So the gap does not
close — it **relocates** to: (1) is the Stokes phase forced `±i` (sign)? (2)
are the orbit magnitudes categorical (`A_ω`)? A fit of either would still be a
fit (anti-fit / "no seventh ansatz" discipline stands); only a *derivation*
closes it. The relocation is the real structural content.
