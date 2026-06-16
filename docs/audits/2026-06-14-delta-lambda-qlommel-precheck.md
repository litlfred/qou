# Binding Δ_λ ↔ q-Lommel recurrence — formalize-first pre-check (2026-06-14)

## Status: derive-first (no fit), DATA-LIMITED — decisive test gated on tower extension

Follow-up to PR #2305's lead-4 redirect (the q-Bessel/q-Lommel zero structure
lives in the `n→∞` brane-tower, where the binding `Δ_λ` ladder also lives) and
the #2078 coordination note. Per the owner steer *"derive/prove first, not
fit/probe"* and the CLAUDE.md `Δ_λ` gate (**no seventh fit-based ansatz**), the
cheap decisive question to ask *before* building any q-Lommel `Δ_λ` closure is:

> Do the canonical `Δ_λ` values lie on **any** three-term recurrence orbit
> `Δ_{ν+1} = b_ν Δ_ν − Δ_{ν-1}` with a smooth / substrate-shaped `b_ν`?

- **Compute:** [`computations/delta_lambda_qlommel_recurrence_precheck.py`](../../computations/delta_lambda_qlommel_recurrence_precheck.py) → witness (4/4, no fit).

## Finding

The canonical per-atom effective `Δ_λ`
([`delta-lambda-canonical-residual.witness.json`](../../computations/delta-lambda-canonical-residual.witness.json))
covers only the four light nuclei — **three distinct mass-number levels**:

| atom | A | Δ_λ |
|---|---|---|
| D | 2 | 4.7776 |
| T | 3 | 13.4855 |
| ³He | 3 | 11.7281 |
| ⁴He | 4 | 39.6597 |

A three-term recurrence needs **≥ 2 interior points** (≥ 4 distinct same-shape
levels) to test the *consistency* of `b_ν`. With one interior level per
single-isospin chain, the implied `b_ν` is a single number and **nothing is
falsified**. So the pre-check is **inconclusive on current data** — and that
data-gap *is* the gating result.

### Preliminary signal (one interior point — not decisive)

| chain | Δ sequence | consecutive ratios ρ_ν | spread |
|---|---|---|---|
| **T-chain** D→T→⁴He | 4.78, 13.49, 39.66 | 2.82, 2.94 | **4 %** (near-geometric → recurrence-compatible) |
| ³He-chain D→³He→⁴He | 4.78, 11.73, 39.66 | 2.46, 3.38 | 38 % (erratic) |

The T-chain's near-constant ratio (`ρ ≈ 2.88`, implied `b ≈ 3.30`) is a *weak*
hint that a constant-coefficient (C-finite) or smoothly-`q`-modulated recurrence
*might* fit — but a single interior point cannot distinguish that from
coincidence. The ³He-chain crossing the isospin pair is not even monotone in `ρ`.

## Verdict + what unblocks it

> **INCONCLUSIVE / DATA-LIMITED.** The q-Lommel `Δ_λ` route is neither supported
> nor refuted; building a closure now would be a fit. The decisive test is
> **gated on extending the same-shape `Δ_λ` tower** to ⁶Li, ⁷Li, ⁸Be, … — the
> **Subgoal-1 Borromean-tower extension** already named as the L2 closure path.
> With ≥ 4 same-shape levels one can test whether `b_ν` is constant (C-finite),
> q-Lommel-shaped (`q^{-ν}`-modulated), or erratic.

**Recommendation for #2078:** extend the tower **first**, then re-run this
pre-check. If `b_ν` is consistent, derive it from the substrate (q-Casimir /
contraction data) — **not** fitted — and require the deuteron to pass. If `b_ν`
is erratic across ≥ 4 levels, the q-Lommel route is refuted and the redirect is
closed.

## Cross-refs

- PR **#2305** (lead-4 redirect: q-Lommel is the tower object, not the finite-n spectrum).
- PR **#2078** (atom→V_hyp→Δ_λ closure — the tower-extension owner).
- CLAUDE.md §Precision goals (Subgoal-1 = per-isotope Borromean-tower extension).
- CLAUDE.md §Δ_λ gate (six failed ansätze; no seventh fit-based ansatz).
