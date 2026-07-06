# content-energy × phase — binding A-scaling is LINEAR content, but the factorization does not jointly close

**Date:** 2026-06-02
**Probe:** [`probe_content_energy_signed_phase.py`](../../computations/probe_content_energy_signed_phase.py)
→ `probe-content-energy-signed-phase.witness.json`
**Status:** EXPLORATORY; asserts the refutation. A≥3-absolute binding open.

Follows the binding-measure search
([2026-06-02-binding-measure-search.md](2026-06-02-binding-measure-search.md))
which flagged `abs_content` as matching the binding A-growth. Two questions:
**(1)** which content-ENERGY is the density; **(2)** does content × phase jointly
close absolute binding AND the T/³He difference.

## (1) The binding A-scaling is LINEAR content, not the quadratic Casimir

Weight-only A-growth `S(⁴He)/S(D)` (target = binding ratio 12.72):

| content-energy | `S(⁴He)/S(D)` |
|---|---|
| `|content|` (= L₀ / total content) | 22.54 |
| `content²` (= quadratic Casimir) | 36.75 |
| `Σ c(c+1)` (Casimir summand) | 36.75 |

The **quadratic** Casimir (`content²`, the "natural" energy) **overshoots** (36.75);
the **linear** `|content|` is closer (22.54), and with the phase modulation it lands
at 13.40 (prior probe) ≈ 12.72. **So the binding's extensive A-scaling tracks the
linear `L₀` grading (total content), not the quadratic Casimir energy.** That is a
real structural constraint on the "Hecke-energy density": linear in the
Jucys–Murphy content, not quadratic.

## (2) content × phase does NOT jointly close

`B = E·Σ_λ w_λ |Δθ_λ|`, worst absolute |err| AND T/³He difference:

| weight `w_λ` | abs worst \|err\| | T/³He diff err | **joint** |
|---|---|---|---|
| `|content|` | 19.9 % | −190.1 % | 190.1 % |
| `content²` | 46.5 % | −152.2 % | 152.2 % |
| `|content|·y_λ` | 339.8 % | −95.7 % | 339.8 % |
| `content²·y_λ` | 319.0 % | −75.2 % | 319.0 % |

**No combination jointly closes** (best joint 152 %). `abs_content` gets the
absolute to 20 % but the T/³He difference is badly wrong (−190 %), because
`|content|` is **transpose-symmetric** (identical for T and ³He, which share
`n=9`) and so cannot carry the mirror difference. Multiplying by `y_λ` to recover
the difference destroys the absolute scaling (→ 340 %).

## Verdict — the measure is NOT a separable scalar product

The absolute A-scaling wants the **content (`L₀`) weight**; the differences want
the **signed/isospin structure** — and a *simple scalar per-λ product*
`content × phase` cannot satisfy both (they pull in opposite directions). So
`w_λ^bind` is **not** a separable `content · phase` scalar; the reconciliation
needs a **non-separable, operator-valued** measure (the combiner #1698 acting on
the per-λ `θ_λ` vector), where the content grading and the isospin sign live in
different tensor factors rather than multiplying as scalars.

**Net narrowing (honest):**
- ✅ Binding extensive A-scaling ↔ **linear content / `L₀` grading** (derived
  constraint: linear, not quadratic Casimir).
- 🔴 `abs_content` is **not** a closure path on its own; content × phase does not
  jointly close. The measure is operator-valued, not a scalar product.

This keeps the discipline: the `abs_content` A-growth match is a structural
signal about the *extensive part*, not a binding closure. Δ_λ / A≥3-absolute
remains open; the refined target is an operator-valued `L₀`-graded, isospin-aware
measure on the `θ_λ` vector (#1698).
