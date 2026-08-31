---
# qou-zrx2
title: 'GAP: the signed trace difference has an hbar_q^0 classical floor -- it is not a pure deformation observable'
status: in-progress
type: bug
priority: high
created_at: 2026-08-31T10:13:14Z
updated_at: 2026-08-31T10:15:23Z
---


## What was measured

Probe: `computations/probes/hbar_q_order_of_binding_observables_probe.py`
(5 assertions, all passing). Sweep in the substrate's own parameter,
`q = exp(η)`, `η = 1e-3 … 1e-6` — `exp(η)` is a genuine 60-dps value, so
`reject_float64_q` is satisfied rather than bypassed; no `allow_float64`
override is used anywhere.

| observable | classical floor | deformation order | verdict |
|---|---|---|---|
| `Δ(net) = h(h−2)/2`, `h = q − 1/q` | `0` exact | `0.99993` → **ℏ_q¹** | PASSES |
| Plancherel block sum (D, ⁴He, ¹²C) | `0` exact | `2.00021` → **ℏ_q²** | PASSES |
| `tr_M(W_free) − tr_M(W_atom)` | **`1/8` (D), `7/128` (⁴He)** | `1.0008`, `1.0021` → ℏ_q¹ | **FAILS** |

The floors extrapolate to `0.124999999874` and `0.054687499701` — `1/8` to
`1.3e-10` and `7/128` to `3.0e-10`. Simple dyadic rationals, which is not what a
numerical artefact looks like.

## Why it matters

At `q = 1` the Hecke algebra degenerates to `ℂ[S_n]` and no deformation remains.
`Δ(net)` and the block sum both vanish there — they are pure deformation
observables and they are the right kind of object. **The trace difference does
not vanish.** It returns a topological remainder: the free word and the atom word
close to different links whatever `q` is.

So it is two quantities at different orders,

    tr_M(W_free) − tr_M(W_atom) = c₀ + c₁·ℏ_q + O(ℏ_q²)

and at `q₀` the classical part is **22.46 %** of it for the deuteron, **4.88 %**
for ⁴He. That fraction of any binding read off this observable is present in a
framework with the braiding switched off.

## The registry's ℏ_q index is wrong for it

`derivation_chain.E_0_CONVENTIONS["B_q_value_absorbed"]` states:

> "Atom-level binding `B(Z,N) = E_0·(|tr_M(W_free)| − |tr_M(W_atom)|)` at
> `H_{3A}`. **The trace-difference operator carries the ℏ_q² scaling**; `E_0` is
> the unit-action scale."

Measured, it carries neither an `ℏ_q²` leading term nor a vanishing limit. This
matters because the `ℏ_q` index is exactly what selects the `E_0` convention, and
it is what the "≈ 102× error" warning is computed from (`qou-59j5`).

1. `B = E_0^{(B)}·Δtr` totals `ℏ_q⁰`, not `ℏ_q²`. It predicts nonzero deuteron
   binding at `q = 1`: `0.78233 × 1/8 = 0.0978 MeV`.
2. Strip the floor and the deformation part is `ℏ_q¹`, which pairs with
   convention **A** (`ℏ_q¹`) to total `ℏ_q²` — the same total as `Δ(net)×A`.
   The registry's rule says atom level MUST use **B**.
3. Neither pairs consistently with the observable *as a whole*, because its two
   parts sit at different orders. **No single scale can.**

## Two live producers already disagree, by exactly the convention ratio

On the identical deuteron trace difference `0.556544660404`:

| producer | convention | scale | binding | vs AME 2.22456637 |
|---|---|---|---|---|
| `binding_canonical.binding_canonical` | B | `Q_β = 0.78233340931` | **0.4354 MeV** | 5.11× short |
| `derive_binding_chain_cooperative.bond_binding` | A | `E₀ = 4.18598136` | **2.3297 MeV** | 1.047× |

`4.18598/0.78233 = 5.35` — the `E₀` convention ratio, exactly. This is the
collision `qou-59j5` catalogued in the registry, found in the wild.

⚠ **The A row lands within 4.7 % of AME and that is NOT evidence for A.**
Choosing the convention that lands closest to the target is precisely the fit
this lane has walked into three times (`qou-78pt`'s withdrawn refutation,
`qou-59j5`'s scale artefact, the six Δ_λ ansätze). The inconsistency is recorded,
not resolved. Resolving it needs the `ℏ_q` index fixed first, and the index is
what this bean shows is wrong.

## Correcting my own claim

I closed the previous turn recommending this lane with:

> "the **ℏ_q-suppressed** observables — `Δ(net)`, the trace differences — which
> do vanish classically and do pair with `E₀` consistently. Those are the right
> kind of thing to carry a binding magnitude."

**Half wrong, and the wrong half is the one the binding chain actually uses.**
`Δ(net)` does vanish classically and does pair consistently. The trace
differences do neither. I asserted it from the registry's prose instead of
measuring it — the same failure that produced the `m_e`-vs-`E₀` artefact earlier
in the session.

## What is NOT concluded

That the ℏ_q-suppressed route is refuted. `Δ(net)` and the Plancherel block sum
pass cleanly, and `Δ(net) × A` still predicts `Q_β` to 0.168 %. What is removed
is the assumption that the trace difference belongs to that category.

## Follow-ups worth opening

1. **Is the floor derivable?** `1/8 = 2⁻³` at `n_strands = 6`, `7/128 = 7·2⁻⁷` at
   `n_strands = 12`. Both dyadic. If the floor has a closed form in `n` it can be
   subtracted exactly, leaving a clean `ℏ_q¹` deformation observable that pairs
   with convention A — which would repair the construction rather than only
   diagnosing it. This is the highest-value next step.
2. **Fix the registry entry.** `E_0_CONVENTIONS["B_q_value_absorbed"]`'s operator
   class should record `ℏ_q⁰ + ℏ_q¹`, not `ℏ_q²`, and the "≈ 102×" warning
   recomputed from the corrected index.
3. **Adjudicate the two producers** — but only after (1) and (2).
