# ⁴He absolute binding — canonical magic-A vs full-θ_λ comparison

**Date:** 2026-06-02
**Branch:** `claude/he4-jsj-binding-link-2026-06-02`
**Status:** Open investigation; not closure.

## What this branch investigates

The ⁴He binding has TWO substrate-derived formulae yielding different
residuals:

### Canonical (already on `main`)

`magic_A_formula.py` + `binding_ladder_catalog.py:65`:

  B(⁴He) = 2 · m_e · A · Vol(L6a4) = 2 · m_e · 4 · 8G

With m_e = 0.510999 MeV and Vol(L6a4) = 7.327724800... (= 8G = 8 · Catalan):

  B_pred = 29.9557 MeV
  B_AME  = 28.2957 MeV
  rel_err = **+5.87 %** (overshoot)

ρ_F = 2 is treated as structural (per `binding_ladder_catalog.py:63`).
α-series corrections at rank r ∈ {2..8} would fit α_r = -668.6, -976.3,
-1121.9, … — all per-isotope fitted, NOT a single derived series
(α_4 values across D/T/³He/⁴He are -9.77 / +5.32 / +92.29 / -668.63;
inconsistent in sign and magnitude → fitted-per-isotope, not derived).

### PR #1726 V3 (cosh-of-growth)

`binding_a3plus_arccosh_growth_split.py`:

  B(⁴He) = μ₀ · Vol_provisional · Σ_λ y_λ · dim_λ · (|Δθ_rot| + (cosh|Δθ_growth| − 1))

With μ₀ = 1.6295 MeV, Vol_provisional = 2·Vol(𝓑₃) = 14.655, and the
per-λ θ split from `binding-reeb-phase-decomposition.witness.json`:

  B_pred = 27.51 MeV
  B_AME  = 28.30 MeV
  rel_err = **+2.7 %**

## Why this discrepancy matters

V3 (+2.7 %) beats canonical magic-A (+5.87 %) — but V3 uses a structurally
different formula:

| factor | magic-A | V3 |
|--------|---------|----|
| scale  | m_e     | μ₀ = m_e / (3·(q − q⁻¹)/2) ≈ 3.19 · m_e |
| volume | Vol(L6a4) = 8G | 2·Vol(𝓑₃) (= 2·8G, same numeric) |
| structure | A factor | Σ y · dim · cosh(growth) per-λ |

The V3 numeric closeness might be:

- (a) **Genuine** — μ₀ · Σ y · dim · cosh-of-growth captures the
  doubly-magic shell-closure structure that magic-A's `A` factor
  approximates. The factor `(2·Vol(𝓑₃) · Σ) / (A · Vol(L6a4)) =
  (Σ · 2) / 4` ≈ Σ/2 is structural if Σ ≈ 4/2 = 2 (per-isotope sum
  ≈ 2 at doubly-magic).
- (b) **Coincidence** — the cosh-extension happens to land in the
  right neighbourhood without representing the same structure.

The investigation is open.

## Open levers (this branch will NOT close them in one PR)

1. **Trace `2 / μ₀ ratio = 0.314 ≈ (q − q⁻¹)/2 × constant?`** — if
   V3 reduces to magic-A under a substrate identity, the +2.7 %
   becomes a structural restatement of the canonical chain at 5.87 %
   (i.e. both are the same number with rounding noise).

2. **⁴He-specific Σ y · dim · cosh(...) value**: numerically check
   if Σ_λ y_λ · dim_λ · (cosh(arccosh(|r_λ|))−1) reduces to 4 (= A)
   by a Wedderburn identity at doubly-magic.  This would CONFIRM
   the V3 formula is equivalent to magic-A in structure.

3. **Substrate-derive α_r per isotope** (replacing the fitted α-
   ladder): the canonical chain's higher-order corrections come
   from `binding-ladder-catalog.py`'s q-Pochhammer terms.  Per
   `binding-endomorphism-deuteron.witness.json` + `prop:six-term-
   per-derivation-weights`, the series may be substrate-derived if
   we extract from the GS-NF jet tower.

## Scope of this PR

**This PR is design-only / scaffold-only**.  Opens the investigation
with a clear comparison statement so the next session has the right
context.  No closure attempt.

## Cross-refs

- `folio-assistant/computations/magic_A_formula.py`
- `folio-assistant/computations/binding_ladder_catalog.py`
- `folio-assistant/computations/binding_a3plus_arccosh_growth_split.py` (PR #1726)
- `docs/canonical-derivation-cheat-sheet.md` §9.3 line 411
- `docs/audits/2026-06-02-binding-A3plus-full-theta-verdict.md` (PR #1726)
