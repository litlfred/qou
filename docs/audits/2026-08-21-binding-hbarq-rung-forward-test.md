# Binding vs mass ℏ_q-rung — forward test + critical-distance re-scope of the b_αα result

**Date:** 2026-08-21 · **Arc:** bk-crossing-coordination, item 3b follow-up · **PR:** #5346
**Probe:** [`computations/binding_hbarq_rung_forward_test.py`](../../computations/binding_hbarq_rung_forward_test.py)
**Witness:** [`computations/binding-hbarq-rung-forward-test.witness.json`](../../computations/binding-hbarq-rung-forward-test.witness.json) (allPassed)
**Re-scopes:** [`2026-08-19-b-alpha-alpha-voldensity-scaling.md`](2026-08-19-b-alpha-alpha-voldensity-scaling.md) (Lane 2, this PR — unmerged)
**Discipline:** scope-(a); critical-distance duty applied to my own Lane 2 claim; no fit; no wiring; q₀ proton-anchored.

Lane 2 floated "binding residuals are ℏ_q²-suppressed vs their VolDensity" as a forward-testable
rule off `ρ_αα ≈ ℏ_q²`. This runs the test — and the honest outcome is a **correction of that
phrasing**, plus one genuinely non-circular statement that survives.

## Test 1 — `ρ_implied/ℏ_q² = M_need` is definitional ⇒ "ρ ≈ ℏ_q²" ⟺ "M ≈ 1"

Writing binding in the VolDensity form `B = m_e·Vol·ρ/ℏ_q²` and solving gives
`ρ_implied := B·ℏ_q²/(m_e·Vol)`, so `ρ_implied/ℏ_q² = B/(m_e·Vol) = M_need` **identically**.

| iso | B_AME | Vol | `M_need = ρ/ℏ_q²` | z=A−1 |
|---|--:|--:|--:|--:|
| ³H | 8.482 | 8.286 | **2.003** | 2 |
| ³He | 7.718 | 7.328 | **2.061** | 2 |
| ⁴He | 28.296 | 7.328 | **7.557** | 3 |
| α–α (7²_1) | 2.416 | 4.750 | **0.995** | 1 |

So `ρ_αα ≈ ℏ_q²` is precisely `M_need(single α–α bond) ≈ 1` — **not** a universal law. Multi-bond
bindings have `M_need` = 2.0 (³H, ³He), 7.6 (⁴He).

> **CORRECTION to Lane 2.** "Binding residuals are ℏ_q²-suppressed" over-generalised. The accurate
> statement is `ρ_binding = M·ℏ_q²`; only the single α–α bond (M ≈ 1) gives ℏ_q².

## Test 2 — what survives is a genuine two-scale separation (non-circular)

The definitional identity is trivial; the comparison to the **mass** scale is not. At fixed
`(m_e·Vol)` normalisation:

- mass: `m_p/(m_e·Vol(𝓑₃)) = ρ_p/ℏ_q² ≈ 251`, with `ρ_p = linking_weight ≈ 2.53` = O(1);
- binding: `B/(m_e·Vol) = M_need ≈ 1 … 7.6` = O(1).

The mass multiplier is O(1/ℏ_q²), the binding multiplier O(1) — a **measured two-scale separation
~1/ℏ_q²**. This is a *scaling* statement, not a magnitude coincidence: `ρ_p = linking_weight_family_a`
is finite and O(1) as ℏ_q→0 (→ 2.5, the classical Wedderburn dimension average), whereas the binding
density `M·ℏ_q² → 0`. **Rest mass is classical (survives ℏ_q→0); nuclear binding is an O(ℏ_q²)
quantum correction (vanishes classically).** That is the defensible form of the "one rung below"
language.

## Test 3 — connection to Lane 1

In the linear-chain regime the multiplicity *is* Lane 1's coordination number: `M_need(³H)=2.003`,
`M_need(³He)=2.061 ≈ z = A−1 = 2` (`coordination_degree`). So there `ρ_binding = (A−1)·ℏ_q²` — the
binding density is the per-nucleon coordination number times ℏ_q², tying Lane 2's rung picture to
Lane 1's graph fact.

## What stands / what is open

- **Stands:** Lane 2 Result 1 (the full proton-VolDensity route overshoots `b_αα` by 259×) is
  unaffected.
- **Open (sharpened):** the two-scale separation is *measured*, not *derived*. Why the mass
  multiplier is `linking_weight/ℏ_q²` (O(1) density, one ℏ_q² enhancement) while the binding
  multiplier is the bare coordination count `M` (no linking_weight, no ℏ_q² enhancement) is the open
  question — now stated as a scaling law rather than a magnitude coincidence.
