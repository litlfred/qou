# The Δ_λ growth sub-lemma (D) reduces to a Plancherel covariance: Cov(f^λ, Σ_□c(□)²) ≤ 0

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-D-reduction-content-covariance-2026-07-18` ·
**Tier:** rigorous reduction (exact character/content identities, positive-controlled) ·
**Discipline:** scope-(a); no fit; no scale; nothing wired; no `c_k`; L2 unchanged (2/7).
**Follows:** #3939 (whose only open input was (D)).

## What this reduces

The rigorous super-exponential lower bound on the GAP-A-3 tower weight (#3939) rested on one
verified-not-proved sub-lemma:

> **(D)**  `w_std(k) = E_Planch[f^{λ/(2,1)}] ≥ E_Planch[f^{λ/(3)}]`,
> i.e. `Σ_{λ⊢k} (f^λ)² (f^{λ/(2,1)} − f^{λ/(3)}) ≥ 0`.

This note reduces (D) — rigorously, through exact `S_k` character and Jucys–Murphy content-formula
identities — to a **single clean covariance inequality**.

## The reduction (each step exact, per λ)

Restricting `V_λ` to the `S_3` on the first three strands gives `χ^λ(g) = Σ_{μ⊢3} f^{λ/μ} χ^μ(g)`;
solving the 3×3 system on the classes `{1³, transposition, 3-cycle}` yields, with `χ₂ = χ^λ(2,1^{k-2})`,
`χ₃ = χ^λ(3,1^{k-3})`,

    f^{λ/(2,1)} = (f^λ − χ₃)/3,      f^{λ/(3)} = (f^λ + 3χ₂ + 2χ₃)/6.

Hence, with `T₁ = Σ(f^λ)³`, `T₂ = Σ(f^λ)²χ₂`, `T₃ = Σ(f^λ)²χ₃`:

    Σ_λ (f^λ)²(f^{λ/(2,1)} − f^{λ/(3)}) = (T₁ − 4T₃ − 3T₂)/6.

- **`T₂ = 0` exactly** (conjugation `χ^{λ'} = sgn·χ^λ`, `sgn(transposition) = −1`, `(f^{λ'})² = (f^λ)²` — pairs cancel).
- So **(D) ⇔ `4T₃ ≤ T₁`**, and since `T₁ > 0`, **(D) follows from `T₃ ≤ 0`**.

**Jucys–Murphy content bridge.** From `Σ_i X_i² = \binom{k}{2}·1 + K₃` (a central-element identity),
the eigenvalue on `V_λ` gives

    χ^λ(3-cycle) = 3 f^λ (C₂(λ) − \binom{k}{2}) / (k(k−1)(k−2)),   C₂(λ) = Σ_□ c(□)².

Substituting, `T₃ ≤ 0 ⇔ Σ_λ (f^λ)³ (Σ_□c(□)² − \binom{k}{2}) ≤ 0`, i.e. (using
`E_Planch[Σ_□c(□)²] = \binom{k}{2}`, the same conjugation cancellation)

> **(D) is EQUIVALENT to  `Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`** — dimension and content-spread are
> non-positively correlated under Plancherel measure.

## Status

- **Reduction: rigorous.** Every step is a proven identity, **positive-controlled** in the probe:
  the per-λ character identities `(f^λ−χ₃)/3` and `(f^λ+3χ₂+2χ₃)/6` are asserted equal to the direct
  Aitken-determinant skew counts `f^{λ/(2,1)}`, `f^{λ/(3)}` for every λ (validating the content-formula
  `χ₂, χ₃`).
- **Kernel: verified, not proved.** `T₃ < 0` strictly for `k = 3..20` here (agent-verified `k ≤ 32`);
  the margin is **stronger** than (D) needs — `E[f^{λ/(2,1)}]/E[f^λ] → 1/3⁺`, so `w_std ≥ ⅓·E[f^λ]`,
  not merely `¼`.
- **No closed form exists** for `E_Planch[f^{λ/μ}]` or for `T₃` (Morales–Pak–Panova, arXiv:1610.07561;
  the `Σ sₘ⊗sₘ⊗sₘ` object has no product formula). So the covariance must be proved **as an
  anti-correlation**, not by comparing closed forms — the natural machinery is the Kerov CLT /
  character-ratio moments (Fulman, arXiv:math/0305423).

## The residual open kernel + next step

> **Open:** `Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`.

Two concrete attack lines (agent-identified): (1) monotonicity in `β` of `E_β[C₂]` on `[2,3]` (via
`ln f^λ = ln k! − Σ ln h(□)` and an FKG/rearrangement argument relating hook-smallness to
content-concentration); (2) a sign-controlling injection on the RSK form `T₃ = Σ_{w∈S_k} χ^{sh(w)}(3-cycle)`
— now with the correct target (the sign is controlled **on Plancherel average**, not per-λ: the row
shape gives `χ = +1`).

## What this does NOT do

Sets no scale; closes no binding. It converts the one open input of #3939's growth bound from an
opaque skew-tableau inequality into a named, well-studied covariance kernel — a genuine
sharpening, not a closure.

## Compute

- Probe: [`computations/deltalambda/wlambda_D_reduction_content_covariance.py`](../../computations/deltalambda/wlambda_D_reduction_content_covariance.py) (exit 0, positive-controlled)
- Witness: `computations/deltalambda/wlambda-D-reduction-content-covariance.witness.json`

## Cross-references

- The growth bound this feeds: [`2026-07-18-wstd-superexp-lower-bound.md`](2026-07-18-wstd-superexp-lower-bound.md) (#3939)
- GAP-A-3 gate-open ruling: [`2026-07-13-delta-lambda-gate-open-for-all.md`](2026-07-13-delta-lambda-gate-open-for-all.md)
- Adjacent binding-frontier work: PR #3808
