# ⁴He absolute binding — canonical magic-A residual investigation

**Date:** 2026-06-02
**Branch:** `claude/he4-jsj-binding-link-2026-06-02`
**Status:** Open investigation; not closure.

## ⚠ Retraction (post-Copilot review on PR #1726)

**The earlier comparison "V3 +2.7 % beats canonical magic-A +5.87 %"
is RETRACTED.**  The V3 +2.7 % number was the output of an assembly
that silently substituted `y_λ = 0` for 53 of the 77 partitions of
12 (because `chi-helium-4-h12-at-q0-50dps.witness.json` is marked
`partial: true`, 24/77 partitions covered).  The +2.7 % therefore
does not reflect a real ⁴He computation and cannot be compared to
the canonical magic-A residual.

What stands: the canonical magic-A residual itself (+5.87 %) and the
fitted nature of `binding_ladder_catalog.py`'s α-ladder.

## What this branch investigates

The ⁴He binding has a canonical substrate-derived formula on `main`:

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

## What this branch does NOT investigate

The PR #1726 V3 cosh-of-growth comparison (originally
"⁴He +2.7 %") is **NOT** a real comparison — V3's ⁴He value is
based on incomplete data.  Until the
`chi-helium-4-h12-at-q0-50dps.witness.json` is regenerated to full
77 partitions, no claim about V3 vs canonical magic-A on ⁴He is
meaningful.

The comparative-formula table below is preserved for reference
(documenting the structural difference between magic-A and V3
shapes) but is **NOT** a claim that V3 is closer at this resolution.

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

1. **Regenerate `chi-helium-4-h12-at-q0-50dps.witness.json` to
   full 77 partitions** (currently `partial: true`, 24/77).
   Without this, no per-block ⁴He claim from any assembly is
   meaningful.  This is the precondition for the levers below.

2. **Substrate-derive α_r per isotope** (replacing the fitted α-
   ladder): the canonical chain's higher-order corrections come
   from `binding_ladder_catalog.py`'s q-Pochhammer terms.  Per
   `binding-endomorphism-deuteron.witness.json` +
   `prop:six-term-per-derivation-weights`, the series may be
   substrate-derived if we extract from the GS-NF jet tower.
   This is the closure mechanism that does NOT depend on the
   partial ⁴He chi witness (it operates on the leading magic-A
   residual + the q-Pochhammer structure, both of which are
   already on `main`).

3. **Re-run PR #1726 V3 on the full ⁴He chi witness** once
   regenerated; only then is a V3-vs-magic-A comparison meaningful.

## Scope of this PR

**This PR is design-only / scaffold-only**.  Opens the investigation
with a clear comparison statement so the next session has the right
context.  No closure attempt.

## Cross-refs

- `computations/magic_A_formula.py`
- `computations/binding_ladder_catalog.py`
- `computations/binding_a3plus_arccosh_growth_split.py` (PR #1726)
- `docs/canonical-derivation-cheat-sheet.md` §9.3 line 411
- `docs/audits/2026-06-02-binding-A3plus-full-theta-verdict.md` (PR #1726)
