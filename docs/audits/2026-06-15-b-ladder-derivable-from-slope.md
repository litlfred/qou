# Can we do the b ladder? YES — it is fixed by the derived slope, not the open offset (2026-06-15)

**Branch:** `claude/vigilant-brown-x0tzat` (PR #2325)
**Owner ask:** *"I want to prove we can do the b ladder."*
**Verdict:** **the b ladder is derivable** — its recurrence coefficient
`b = q₀¹⁰+q₀⁻¹⁰ = 2cosh(10η₀)` follows from the exponent **slope alone** (derived,
now verified A=2..12), and the open keystone (the exponent **offset**) provably
cannot affect it. Gate-respecting (no fit). **Not wired** (the binding *production*
formula stays gated on the absolute scale + nucleon gap — a different question).

> **⚠ Significance caveat — the ladder describes the `B_pred` residual, which the
> better `B_sym` form dissolves (2026-06-15, added same day).** Everything below is
> mathematically correct and Lean-verified, but it rests on `Δ_λ = B_AME/B_pred ≈
> q₀^(10A−5)`. Direct measurement shows this exponent (per-site 5.00) is exact
> **only against `B_pred`** (the weaker binding prediction); against `B_sym` (the
> exact log-trace) the per-site exponent collapses to ≈0–1 (D over-binds). So the
> slope-10 / b coefficient describe `B_pred`'s exp-vs-linear gap, **not** a
> fundamental q₀-power — consistent with this PR's item-3 (`B_sym` already realizes
> the exponential) and the sibling refutation
> ([`2026-06-15-delta-lambda-offset-open-chain-boundary.md`](2026-06-15-delta-lambda-offset-open-chain-boundary.md) ⚠).
> The Lean lemma, the `double_root_linear` fix, the A=2..12 slope verification, and
> the offset-independence all stand; what is downgraded is the claim that this is
> the *fundamental* binding law.

## The argument in one line

`Δ_λ(A) ≈ q₀^(10A−5) = q₀^(−5)·(q₀¹⁰)^A` is geometric in A with ratio `r = q₀¹⁰`;
the order recurrence `Δ_{A+1} = b·Δ_A − Δ_{A−1}` has `b = r + r⁻¹ = q₀¹⁰+q₀⁻¹⁰`,
set **only by the slope**. The unresolved offset `−5` is the prefactor `q₀⁻⁵` = the
constant `C` in `Δ_λ = C·r^A` — it folds into the two seeds and **never enters `b`**.

## Why this dissolves the keystone blocker (for the ladder)

The keystone was stated as "derive `10A−5 = 5(2A−1)` from Bring-surface crossings."
That splits into two independent parts:

| part | status | gates the b ladder? |
|---|---|---|
| **slope 10** (per-A growth) | **DERIVED** — `σ+σ⁻¹ = 10A−2` (Z,N cancel ⇒ A-only) | **YES** → and it's done |
| **offset −5** (absolute scale; the `−3` crossing-vs-site puzzle, "why 5/site") | **open** | **NO** → it's the prefactor `C`, fixed by seeds |

The whole "near-match, not derivable" framing conflated these. The b *recurrence*
needs only the slope. The offset is a *normalization* question.

## Evidence (this PR, gate-respecting)

1. **Slope derived + EXTENDED to the untested tower** —
   [`qlommel_b_ladder_slope_derivation.py`](../../computations/qbeta/qlommel_b_ladder_slope_derivation.py)
   (witness, 3 green). `σ+σ⁻¹ = 10A−2` now verified for D, T, ³He, ⁴He, **⁶Li, ⁷Li,
   ⁸Be, ¹²C** (A=2..12) — the exact derive-or-refute the 2026-06-09 residual audit
   said the data-gate awaited. All hold; the slope is structural, not a 4-point fit.
2. **Offset-independence demonstrated** — for `C ∈ {1, 7.3, q₀⁻⁵, q₀⁻³}` the
   recurrence residual `|b·Δ_A − Δ_{A−1} − Δ_{A+1}|` over A=2..11 is `~10⁻³⁸`
   (machine precision). `b` is identical for every `C` ⇒ depends only on `r=q₀^slope`.
3. **Lean (sorry-free): `first_kind_geometric_b`** —
   [`QLommelOrderRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QLommelOrderRecurrence.lean):
   `∀ r C, r ≠ 0 → IsOrderThreeTermRec (fun _ => r + r⁻¹) (fun A => C·rᴬ)`. The
   universal `C` IS the offset-independence; reuses the existing `two_root_geometric`.
   With `two_seed_unique` (already proved) this is the full bridge: derived slope ⇒
   derived `b` ⇒ two seeds determine the ladder.
4. **Bootstrap recap** — seeds D,T + derived `b` predict ⁴He to −3.5% (companion
   `qlommel_delta_lambda_two_seed_test.py`); the residual is second-kind admixture
   (β·s^A), not a `b` error.

## What remains open (and why it does not block the b ladder)

The **absolute Δ_λ scale** — the offset `−5`, i.e. *why 5 per chain-site* (Bring
quintic? the Borromean 3-component / 3-strand Markov normalization, since
`σ+σ⁻¹ − 3 = 10A−5` with the same `−3` at every A?) and the **Z-correction**
coefficient (³He). These set the seed values `α, β`, which the two seeds supply
empirically. They are a *normalization* problem, decoupled from the recurrence.

## Status

**Not wired.** The b ladder being *derivable* does not promote the binding
*production* formula: absolute binding still needs the offset (open) and rides the
+2.89% nucleon-mass gap (Subgoal-2, declined). What this PR establishes is the
*structural* result the owner asked for — the b ladder is a derived consequence of
the (now A=12-verified) slope, not a fit.
