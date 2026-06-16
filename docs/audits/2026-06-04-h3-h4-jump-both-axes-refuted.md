# H₃→H₄ jump in `linking_weight_family_a`: both derivation axes refuted

**Date:** 2026-06-04
**Audit type:** consolidated negative result
**Owners:** PR chain #1762 (1ppQ roadmap, attack options A/B/C/D/E), #1816 (Option A data, MERGED), #1841 (Option B structural, MERGED), #1850 (Markov trace axis, MERGED), #1808 (Option E literature import).
**Status:** **closes 2 of the 5 #1762 attack options.** The H₃→H₄ jump in production's `linking_weight_family_a(q) = (3q²+4+3q⁻²)/4 ≈ 2.53` is not derived from algebra-tower induction nor from trace-level Markov stabilization. The remaining explanation is the **CODATA-implied near-match** already documented at `_li_2_q_util.py:298-313`.

---

## The question

`linking_weight_family_a(q)` ([`_li_2_q_util.py:172`](../../computations/_li_2_q_util.py)) appears in production as a global geometric multiplier:

> `vol_density_borromean(q) = Vol(𝓑₃) / ℏ_q² × linking_weight_family_a(q)`

and the linking_weight evaluates to `(3q²+4+3q⁻²)/4`. Symbolically it equals `(1/4) · Σ_{λ⊢4} dim_q(V_λ)` — a sum over partitions of **4**.

But the proton braid `𝓑₃` lives in the Hecke algebra **H₃** (3-strand braid). The "4" comes out of nowhere structurally. This unexplained jump from H₃ to H₄ was the central derivation gap in [PR #1762 §2](https://github.com/litlfred/qou/pull/1762).

PR #1808's literature-import audit ([`2026-06-04-h3-h4-jump-literature-import.md`](./2026-06-04-h3-h4-jump-literature-import.md)) located two candidate mechanisms in the literature. This audit records the verdict of testing both, end-to-end.

## Axis 1 — algebra-tower induction (REFUTED by PR #1841)

**Hypothesis** ([scoping doc](./2026-06-04-option-b-h3-h4-bratteli-scoping.md)). The H₃ → H₄ jump is the Bratteli induction `Ind_{H₃}^{H₄}` — adding one box to each of the 3 partitions of 3 reaches the 5 partitions of 4 (7 box-additions, multiplicity-free). Family-A might emerge as a Markov-weighted box-adding sum.

**Three sub-hypotheses tested** (closed-form symbolic for B1/B3, numerical at q₀ for B2; see [Option B probe](../../computations/probes/option_b_h3_h4_bratteli_probe.py)):

| Sub-hypothesis | Verdict | Evidence |
|---|---|---|
| **B1** uniform — `Σ_{λ⊢3} Σ_{λ⁺⊃λ} dim_q(V_{λ⁺}) ?= c · λ_A(q)` for some constant `c` | **REFUTED** | residual at k(q=1)=32/5: `q²/5 − 2/5 + 1/(5q²)` (exact rational, non-zero, q-dependent) |
| **B2** y_λ-weighted at q₀ | **REFUTED** | weighted sum = 4.056 vs λ_A(q₀) = 2.533 — relative error 60.1 % |
| **B3** per-source λ — any single λ ⊢ 3 alone | **REFUTED** | per-λ k(q=1): (3): 8/5, (2,1): 16/5, (1,1,1): 8/5 — three distinct rationals; none reproduces λ_A's q-form |

**Conclusion for axis 1.** The box-adding Bratteli induction at the **algebra-tower** level does NOT derive the Family-A linking_weight. The H₃→H₄ jump is not the induction functor `Ind_{H₃}^{H₄}` acting on dim_q under any of the three natural weightings.

(Sanity assertion in the same probe: `Σ_{λ⊢4} dim_q = 3q²+4+3q⁻²` symbolic Δ=0 — the production identity is verified.)

## Axis 2 — Markov stabilization at the trace level (REFUTED by PR #1850)

**Hypothesis** ([scoping doc](./2026-06-04-markov-stab-trace-axis-scope.md)). The H₃ → H₄ promotion is a Markov move `β ↦ β·g_n^{±1}` (with `g_n` the Hecke image of `σ_n` under `B_n → H_n`), under which the Markov/Ocneanu trace scales by the **stabilization parameter**

  `z = 1 / (q^½ + q^{-½})`     ([`hecke_symbolic.py:46`](../../computations/hecke/hecke_symbolic.py))

**Formalize-first narrowing** (PR #1826 discipline). Before running any probe, the cheap structural fact:

  `z(q₀) ≈ 0.4993 < 1 < linking_weight ≈ 2.5328`

is a **direction obstruction**: a single stabilization scales the trace by z < 1, so it cannot produce a >1 multiplier. The naive "stabilization explains the jump" reading is structurally dead before any scan. What survives — the [probe](../../computations/probes/markov_stab_trace_axis_probe.py) tests these two exactly:

| Surviving candidate | Verdict | Evidence |
|---|---|---|
| **M1** identity trace — `linking_weight ?= tr_M(1_{H₄}) = Σ_{λ⊢4} y_λ·f^λ` | **REFUTED** | `tr_M(1_{H₄}) = 1.0000000000` *exactly* (the normalized Markov trace), not 2.53 |
| **M2** z-renormalised — `(1/4)Σ_{λ⊢4} dim_q ?= z^{±k} · clean-H₃ quantity`, k∈{1,2} | **REFUTED** | no exact `z^{±k}·linking_weight = clean-H₃` coincidence; `z⁻¹ ≈ 2.003` is `q^½+q^{-½}` (irrational at q₀), not exactly 2 |

**Conclusion for axis 2.** The trace-level Markov stabilization (single move OR identity trace OR z-renormalised H₃ identity) does NOT derive the Family-A linking_weight. The H₄ count is not the result of evaluating tr_M on a Markov-stabilized braid.

## Synthesis — what the two refutations say together

Neither of the two structurally-natural candidates derives `linking_weight_family_a(q) = (3q²+4+3q⁻²)/4`:

- **Not algebra-tower induction.** The H₃→H₄ jump is not `Ind_{H₃}^{H₄}` acting on any natural weighting of dim_q over partitions of 3.
- **Not trace-stabilization.** The H₃→H₄ jump is not a Markov move scaling the trace by z, and the H₄ identity-trace is 1, not 2.53.

The remaining explanation is the one the production code itself documents:

> *"the 2.53 is a CODATA-implied-λ near-match that lands near `λ = m_p / (m_e · Vol/ℏ²) ≈ 2.46` (the value that round-trips m_p)"* — [`_li_2_q_util.py:298-313`](../../computations/_li_2_q_util.py)

So `(1/4)·Σ_{λ⊢4} dim_q` is the closed-form expression nearest to the CODATA-implied scaling λ — a numerical match dressed in categorical clothing, not a structural derivation. The H₄ count is a *post-hoc fit form*, not a *forward consequence of the H₃ proton braid*.

## What this closes in the #1762 roadmap

Two of the five attack options listed in [PR #1762 §5](https://github.com/litlfred/qou/pull/1762) are now closed:

| Option | Status after this audit |
|---|---|
| **A** — Vol(β_K) for the light series (diagnostic) | shipped (#1816); confirmed the gap; not a derivation |
| **B** — H₃ brane-tower / Bratteli induction | **REFUTED** (#1841) |
| **E** — literature analogy import (Markov stabilization) | **REFUTED** (#1850) at the trace level — the lead the literature pointed to |
| C — Hilbert-space resolution-of-identity in extended H₄ | not pursued; orthogonal to the two structural axes above |
| D — GAP-A-3 / Δ_λ closure via Kashiwara crystal | open (research-grade) |

## What this leaves open

- **The Family-A formula is still the production multiplier** that round-trips m_p. The uniform VolDensity pipeline stays unchanged; Option A confirmed flipping it would break m_p by ≈ 2.38× and the gap grows with A. This audit is structural, not actionable on production.
- **Option D (Kashiwara crystal / Δ_λ closure)** remains the productive direction for the per-isotope binding-energy gap (separate from the H₃→H₄ Family-A question).
- **Honest framing for `linking_weight_family_a`.** The production docstring's "CODATA-implied near-match" label is now the recommended canonical framing. The function should not be referred to as a "derived" or "categorical" multiplier in new content — it is a **post-hoc fit form** that closely matches an empirical scaling. The `(1/4)·Σ_{λ⊢4} dim_q` decomposition is exact but the choice of H₄ (not H₃, not H₆) is not structurally derived.

## Files

- [`docs/audits/2026-06-04-option-b-h3-h4-bratteli-scoping.md`](./2026-06-04-option-b-h3-h4-bratteli-scoping.md) — Option B scope
- [`docs/audits/2026-06-04-markov-stab-trace-axis-scope.md`](./2026-06-04-markov-stab-trace-axis-scope.md) — Markov-stab scope
- [`docs/audits/2026-06-04-h3-h4-jump-literature-import.md`](./2026-06-04-h3-h4-jump-literature-import.md) — Option E lit import
- [`computations/probes/option_b_h3_h4_bratteli_probe.py`](../../computations/probes/option_b_h3_h4_bratteli_probe.py) + `.witness.json`
- [`computations/probes/markov_stab_trace_axis_probe.py`](../../computations/probes/markov_stab_trace_axis_probe.py) + `.witness.json`
- [`computations/probes/option_a_vol_per_knot_light_series.py`](../../computations/probes/option_a_vol_per_knot_light_series.py) + `.witness.json` (Option A diagnostic)
