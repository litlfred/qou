# Covariance-kernel epic (`qou-x631`) — M₁ sub-result (1): RETRACTED (vacuous reduction)

**Date:** 2026-08-22 (retraction same day) · **Branch:** `claude/m1-effective-clt-project-2026-08-22` ·
**Tier:** corrected negative result · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2
unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## ⛔ RETRACTION

An earlier version of this audit claimed sub-result (1) as a *substantive reduction*:
"the `Λ*` part `p₂^#_sym` of `Σh` is `ω₃`-orthogonal (`Cov(p₂^#_sym, ω₃)=0`), hence `M₁ = Cov(T, ω₃)`
with `T` the non-`Λ*` co-content part." **That framing is vacuous and is withdrawn.** Two exact facts
(verified all `λ⊢n`, `n≤12`) collapse it:

1. **`p₂^#_sym ≡ 0` identically.** The degree-2 shifted power sum is transpose-**anti**symmetric:
   `p₂^#(λ) = −p₂^#(λ')`, so its symmetrization `p₂^#_sym = ½(p₂^#(λ)+p₂^#(λ')) = 0` for every `λ`.
   So `Cov(p₂^#_sym, ω₃) = 0` is trivially the covariance of the **zero function** — not an
   orthogonality that reduces anything.
2. **`T = Σh` identically.** `T := Σ□(i+j) − n` (1-indexed) equals `Σ□ h(□)` for every `λ`
   (difference set `= {0}`). So "`M₁ = Cov(T, ω₃)`" is just the definition `M₁ = Cov(Σh, ω₃)`
   rewritten — no reduction.

The decomposition `Σh = p₂^#_sym + T` is therefore `Σh = 0 + Σh`. **Sub-result (1) reduced nothing.**
This was a self-assuming/vacuous error (a trivial identity dressed as a reduction); flagged and
corrected here per the repo's zero-vacuity discipline.

## What is actually true (the honest residue)

- **The co-content identity `Σ□ h(□) = Σ□ (i+j) − n` is real and clean** (1-indexed `i,j`; verified
  `n≤11`). It *is* the antidiagonal reformulation (PR #5366) — an identity, restating `Σh`, not a
  reduction of `M₁`.
- **Transpose parity, correctly stated.** Under transpose, `χ^{λ'}(g) = sgn(g)χ^λ(g)`, so the 2-cycle
  central character `Σ₂` is transpose-**odd** and the 3-cycle `Σ₃` is transpose-**even**. `Σh` is
  transpose-even, so `Cov(Σh, Σ₂) = 0` (even × odd) — which is *why* the degree-2 shifted-power route
  finds nothing (its only non-constant piece `Σ₂` is transpose-odd). But `M₁ = Cov(Σh, ω₃) =
  ⅓Cov(Σh, Σ₃)` pairs `Σh` with the transpose-**even** `Σ₃`, which does **not** vanish. So the
  shifted-power / `Λ*`-peeling approach yields **no reduction of `M₁`** — an honest **negative**.

## Consequence

Sub-result (1) does **not** advance the effective bound: there is no `Λ*` piece to peel off `Σh`, and
`M₁` is unchanged. The Śniady-genus idea (which would only handle `Λ*`×`Λ*` covariances) has nothing
to act on here — confirmed, but as a dead end, not a win.

**Unaffected by this retraction** (independent of the peeling): the derived leading constant
`κ = 128/(225π²) > 0` ([derivation audit](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md))
and the one-sided reframing `κ_n ≥ κ` for `n ≥ 13`
([reframing audit](2026-08-22-covariance-kernel-M1-onesided-reframing.md)) — both concern `M₁`'s
*values*, not any decomposition, and stand.

## Compute

- Probe: [`wlambda_covariance_epic_M1_sniady_lambda_star_orthogonality.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_sniady_lambda_star_orthogonality.py)
  — RESULT lines corrected to report `p₂^#_sym ≡ 0` and `T = Σh` (the vacuity), not a reduction.

## Cross-references

- Workplan: [`2026-08-22-M1-effective-CLT-project.md`](../workplans/2026-08-22-M1-effective-CLT-project.md) (sub-result (1) marked RETRACTED).
- One-sided reframing (stands): [`2026-08-22-covariance-kernel-M1-onesided-reframing.md`](2026-08-22-covariance-kernel-M1-onesided-reframing.md).
- Gap bean `qou-k5r5`.
