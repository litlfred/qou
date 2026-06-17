# Chirality-Δ_λ binding wired all-A — the bare dim magnitude diverges (2026-06-17)

**Branch:** `claude/delta-lambda-bring-quadratic-2026-06-17` (PR #2417)
**Wires:** the PROVED per-block factor `Δ_λ = sgn(w₀^{S_λ'})·dim(V_λ)` (keystone
`S5SO3FiberAction.lean` / PR #1305 / audit
[`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md))
through the all-A χ^λ fine-Bratteli transfer (PR #2405, `tr_m_atom_via_transfer`).
**Discipline:** derive-or-refute; the FORMALIZED formula, no `C_knot` fit; no
production rewire, no witness.

## What was wired (the gap)

The categorical binding `B(K) = m_e·|Σ_{λ⊢3A} y_λ χ^λ(β_atom) Δ_λ|`
(`binding_energy_categorical_deuteron.py`, PR #1307) was only ever evaluated for
the **deuteron** (loaded from a precomputed sum: B(D)=0.380 MeV, −82.9 % vs AME).
[`computations/probes/chirality_delta_lambda_binding_sweep.py`](../../computations/probes/chirality_delta_lambda_binding_sweep.py)
extends that *exact* formula to D…⁷Li using the transfer χ^λ.

## Result — undershoot ≤⁴He, then divergent OVERSHOOT at A≥6

| iso | A | n | #λ | Σ_λ yχΔ | B_pred | B_AME | ratio AME/pred |
|---|---|---|---|--:|--:|--:|--:|
| D | 2 | 6 | 11 | −0.744 | 0.380 | 2.225 | 5.85 (under) |
| T | 3 | 9 | 30 | −3.735 | 1.909 | 8.482 | 4.44 (under) |
| ³He | 3 | 9 | 30 | −4.588 | 2.345 | 7.718 | 3.29 (under) |
| ⁴He | 4 | 12 | 77 | −5.946 | 3.038 | 28.296 | 9.31 (under) |
| ⁶Li | 6 | 18 | 385 | **+256.2** | 130.9 | 31.99 | **0.24 (4× over)** |
| ⁷Li | 7 | 21 | 792 | **+824.6** | 421.4 | 39.24 | **0.09 (10× over)** |

**Cross-check:** B(D)=0.3801 MeV reproduces the deuteron-only compute (0.380) to
the printed digits — the wiring is correct.

## What it shows (sharpens the Δ_λ gate)

The deuteron-only −82.9 % undershoot **masked** the real behaviour. Across A the
sum `Σ_λ y_λ χ^λ Δ_λ` runs −0.7 → −6 (A≤4) → **+256 → +825** (A≥6): it does not
merely undershoot, it **diverges into overshoot** because the magnitude factor
`dim(V_λ)` grows combinatorially (the high-dim deep partitions, ~hundreds of
blocks at n=18,21, dominate). So:

- The **sign** side is fine — `sgn(w₀^{S_λ'})` is the proved ±1 chirality
  (mixed `#sgn± ≈` balanced; bypasses the PROBE-4 KL wall, as designed).
- The **magnitude** side — bare `dim(V_λ)` — is the failure: it is **not** a
  viable all-A binding weight; it blows the sum up beyond A=4.

This is the precise numerical confirmation of the sibling template
([`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md)
§"Why this matters", PROBE 2 #2369/#2371/#2372): *"the interface operator should
supply the per-block magnitude (Wedderburn / quantum-dimension data), with the
sign factored as the chirality."* The bare `dim` magnitude diverges ⇒ the open
piece is **exactly** the interface-operator-corrected magnitude (not the sign,
which is proved, and not a global `C_knot` fit, which the deuteron retraction
already rejected).

## Net

The proved `Δ_λ = sgn·dim` factor is real, but as an all-A **binding sum** it is
refuted (divergent overshoot ≥⁶Li). The Δ_λ gate's open lever is sharpened to a
single target: a **magnitude** weight `w_λ` replacing bare `dim(V_λ)` that does
not diverge — the quantum-dimension / interface-operator data PROBE-2 is after.
Sign = chirality (closed); magnitude = open. No fit, not wired.

## Cross-links
- [`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md) — the proved sgn·dim decomposition + PROBE-2 template.
- `computations/binding_energy_categorical_deuteron.py` — the deuteron-only evaluation this extends.
- `computations/tr_m_atom_via_transfer.py` (PR #2405) — the all-A χ^λ transfer used here.
- [`2026-06-17-delta-lambda-master-formula-active-set-redesign.md`](2026-06-17-delta-lambda-master-formula-active-set-redesign.md) — the sibling Δ_λ-route finding (LP/quadratic refutations).
