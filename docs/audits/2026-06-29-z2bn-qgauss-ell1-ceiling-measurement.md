# z2bn binding q-Gaussian ℓ¹-ceiling measurement (2026-06-29)

**Branch:** `claude/z2bn-qgauss-ell1-ceiling-2026-06-29`
**Probe:** `computations/probes/binding_qgaussian_ell1_ceiling_measurement.py` (+ witness)
**Companion to:** `computations/delta_lambda_l1_ceiling_sign_prune.py`
(the classical sign-only prune) and the z2bn fibre-kernel lever
(`BindingQGaussianHabiro.lean`, sorry-free).

## Question

The per-block binding closure is `B(K)/m_e = Σ_λ y_λ χ^λ Δ_λ`. The
**sign-only prune** proved a (b) STRUCTURAL exclusion: with the *classical*
integer magnitude `|Δ_λ| = dim_λ` held fixed, the ℓ¹ ceiling
`‖c_cl‖₁ = Σ_λ |y_λ χ^λ dim_λ|` is only **36–59 %** of target, so no
sign/chirality reassignment closes the deficit — a 41–64 % *magnitude-adding*
ingredient is required.

The **z2bn fibre-kernel lever** offers a candidate magnitude: replace the
classical Wedderburn dimension by the **symmetric quantum dimension**
`dim_q(λ) = [n]_q! / ∏_c [h_c]_q` at the substrate anchor `q_0 ≈ 1.110`
(the BindingQGaussianHabiro magnitude, `S(m) = Σ_{λ⊢m} dim_q(λ)`). Since
`q_0 > 1` every q-integer `[k]_q > k`, so `dim_q(λ) ≥ dim_λ`. **Does the
q-deformed magnitude breach the classical ceiling?**

## Result — q-inflation is real but INSUFFICIENT

Holding `{y_λ, χ^λ}` at canonical pinned values and swapping `dim_λ → dim_q(λ)`
at `q_0` (proton anchor; muon anchor identical to 7e-11):

| iso | classical `‖c_cl‖₁/tgt` | q-Gauss `‖c_q‖₁/tgt` | q-inflation | signed `qnet/tgt` | breach? |
|-----|---:|---:|---:|---:|:--:|
| D   | 0.516 | 0.548 | 1.061× | 0.180 | no |
| T   | 0.358 | 0.465 | 1.299× | 0.295 | no |
| ³He | 0.592 | 0.767 | 1.296× | 0.402 | no |
| ⁴He | 0.406 | **0.795** | **1.958×** | 0.206 | no |

Two structural observations:

1. **The q-inflation scales with A.** D (A=2) inflates 1.06×, the A=3
   isotopes ~1.30×, and ⁴He (A=4, n=3A=12, the richest hook structure)
   nearly **doubles** at 1.96×. More cells ⇒ more q-integers `[k]_q > k` ⇒
   more inflation. This is the correct *qualitative* direction for the
   z2bn lever.

2. **It still does not reach target.** Even ⁴He's q-inflated ℓ¹
   *ceiling* — the best magnitude reachable over **every** sign assignment,
   by the triangle inequality — tops out at **0.795 < 1**. The signed net
   (with the proven `sgn(w_0^{S_{λ'}})` twist) stays at 0.18–0.40: sign
   cancellation still removes most of the q-inflated magnitude.

## Scope — (b) structural extension (invariant: ℓ¹/triangle bound)

For every sign assignment `s_λ ∈ {±1}`,
`|Σ_λ s_λ y_λ χ^λ dim_q(λ)| ≤ Σ_λ |y_λ χ^λ dim_q(λ)| = ‖c_q‖₁`. Measured
`‖c_q‖₁/|target| ≤ 0.795 < 1` for all of D/T/³He/⁴He. Hence:

> **(b) STRUCTURAL EXCLUSION.** The symmetric q-Gaussian magnitude
> `dim_q(λ)` at `q_0`, even optimally signed, does **not** close the binding
> deficit on the existing `{y_λ, χ^λ}` term set. The classical sign-only
> prune extends to the **`dim_q`-magnitude-only** sub-class.

This is a narrow (b): it excludes the *single-term `Σ_λ` closure with the
`dim_q` magnitude*. It does **not** exclude a magnitude-adding ingredient in
general — the **many-body terms (T2–T6 / the A=4 interface operator)** remain
the open productive direction, and a *different* per-block magnitude is not
ruled out. Per anti-flip-flop discipline nothing here is fitted; the
inflation factor is read off the canonical witnesses.

## Why this is useful

The measurement narrows the z2bn search **before** the expensive,
owner-gated Seiberg–Witten-period keystone is built: the fibre q-difference
kernel will have to supply magnitude **beyond** the bare `dim_q` inflation
(which buys at most 1.96× and still leaves ⁴He 20 % short) — e.g. via the
many-body / interface-operator structure, not a single-sum q-dimension
reweight. Formalize-first: a one-script ℓ¹ bound prunes a sub-class the
keystone would otherwise have to rule out empirically.

## Reproduce
```bash
python3 computations/probes/binding_qgaussian_ell1_ceiling_measurement.py
```
