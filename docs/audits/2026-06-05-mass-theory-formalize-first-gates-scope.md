# Mass-theory formalize-first invariants — applying the Q_β §4 gate template

**Date:** 2026-06-05
**Branch:** `claude/gap-a3-a4-mass-formalize-first-2026-06-05`
**Status:** scope + probe (one extended invariant check; results in §3)
**Builds on:** Q_β §4 formalize-first chain (PRs #1875, #1889, #1890, #1893 — all merged today) + existing `bar_symmetry_three_candidates.py` (linking_weight bar-symmetry test)

## §1. Why a mass-theory analog

Today's Q_β formalize-first chain shipped four sorry-free Lean gate classes (PR #1875 bar-even, PR #1889 radius-of-convergence, PR #1890 q=1 shadow + direction sanity, PR #1893 unified `BarEvenKernel` typeclass) plus a 7-step Δ_λ pre-flight checklist. The structural discipline is now established for the decay-side.

The mass-side has an **established checklist tradition only for bar-evenness** (the existing [`bar_symmetry_three_candidates.py`](../../computations/bar_symmetry_three_candidates.py) tests three `linking_weight` candidates against the Φ_q vs Li_2^q context-sorting rule). The other three §4 invariants — anchor-stability, q=1 classical-limit shadow, direction sanity — have **no mass-side analog yet**.

This audit closes that gap. It extends the bar-symmetry test to a unified **mass-theory formalize-first invariants probe** that runs all four §4 invariant checks on the three published `linking_weight` candidates.

## §2. The four §4 invariants on mass-theory quantities

| # | invariant | Q_β source | mass-theory analog |
|---|---|---|---|
| (a) | **Anchor-stable** | proton + muon cross-anchor swing < 1 ppm at u_substrate (PR #1889) | proton + muon swing of `linking_weight(q_0)` < 1% (registry §8 mass-side gate) |
| (b) | **Bar-even** | `q ↦ q⁻¹` Taylor-even-in-t for the c_k ladder (PR #1875) | `linking_weight(q) = linking_weight(q⁻¹)` as a q-rational (existing test, [`bar_symmetry_three_candidates.py`](../../computations/bar_symmetry_three_candidates.py)) |
| (c) | **q = 1 classical-limit shadow** | `c_2 → −1`, `c_3 → J_Hopf(1) = −2` (PR #1890 Track A) | `linking_weight(q → 1)` reproduces a known categorical integer or rational (e.g. `5/2` for Family A, from `(3·1² + 4 + 3·1⁻²)/4 = 10/4`) |
| (d) | **Direction sanity** | `|F(q_0)|` within 10× of Q_β target ~0.998 (PR #1890 Track B) | `linking_weight(q_0)` in same order of magnitude as the empirical multiplier needed to close `m_p/m_e` (registry-level: ~2.46 from CODATA-implied near-match per PR #1850 audit) |

The four invariants are independent: a candidate `linking_weight` can pass (b) (manifestly q-symmetric) while failing (c) (wrong q=1 limit) or (d) (wrong order of magnitude).

## §3. Probe — three `linking_weight` candidates × four invariants

The three published `linking_weight` candidates (from the existing bar-symmetry test):

1. **Family A** `(3q² + 4 + 3q⁻²)/4` — PROVED Wedderburn, bar-symmetric, ≈ 2.5328 at q_0
2. **via-Jones** `5/2 + 4·(tr_M(β_Borromean) − 1)` — Markov trace, bar-symmetric, ≈ 2.5328 at q_0
3. **Bring color-tube** `1/(1 − h·q¹⁰)` (Φ_q-side) — Bar-asymmetric, ≈ 2.4619 at q_0

The probe ([`mass_theory_formalize_first_invariants_probe.py`](../../computations/mass_theory_formalize_first_invariants_probe.py)) tests each candidate against all four §4 invariants and reports a per-cell verdict.

### Anticipated results (pre-formalize-first prediction)

| invariant | Family A | via-Jones | Bring color-tube |
|---|---|---|---|
| (a) anchor-stable | ✓ PASS (Wedderburn-derived; sub-ppm) | ✓ PASS (trace-stable) | ? unknown — q¹⁰ may amplify cross-anchor shift |
| (b) bar-even | ✓ PASS (q² + q⁻² symmetric) | ✓ PASS (Markov trace bar-invariant) | ✗ FAIL (q¹⁰ asymmetry, established in existing probe) |
| (c) q=1 shadow | ? unknown — Family A → 10/4 = 2.5 ≠ 2.5328; need categorical interpretation | ? unknown | ? unknown |
| (d) direction sanity | ✓ PASS (≈ 2.5328, target ≈ 2.46) | ✓ PASS (same value) | ✓ PASS (≈ 2.4619) |

The interesting cell is **(c) q=1 shadow**: Family A's q → 1 limit is `(3 + 4 + 3)/4 = 10/4 = 2.5`, which is close to but **not equal to** the numerical value at q_0 (2.5328) or the CODATA-implied near-match (2.46). What integer or simple rational SHOULD `linking_weight(q=1)` reproduce? This is the formalize-first question (c) opens for mass-theory.

If no candidate has a clean (c) shadow, the registry-level "linking_weight is CODATA-implied near-match" framing (PR #1850 audit) is reinforced — at the formalize-first level, mass-theory's `linking_weight` is structurally weaker than Q_β's c_k anchors. If some candidate DOES have a clean shadow, that's the next derivable structural anchor.

## §4. What this PR ships

1. **This audit** consolidating the 4-invariant template for mass-theory.
2. **The sympy probe** running the 4×3 invariant matrix on the published candidates.
3. **No Lean class** (deferred to a follow-up PR once the probe results identify which mass-theory quantities are anchor-derivable).

The probe is **diagnostic only** — it does NOT propose a new `linking_weight` candidate; it tests the existing three against the four §4 invariants and reports the verdict matrix.

## §5. Cross-references

- **Q_β §4 invariant chain (this session):** PRs #1875, #1889, #1890, #1893
- **Existing bar-symmetry test:** [`bar_symmetry_three_candidates.py`](../../computations/bar_symmetry_three_candidates.py)
- **linking_weight CODATA-implied near-match audit:** PR #1850 + the `_li_2_q_util.vol_density_borromean` docstring ([`_li_2_q_util.py`](../../computations/_li_2_q_util.py))
- **Registry §3 (Q_β c_k canonicity gates):** [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
- **Mass = Vol × Density formalization:** PR #1834 (merged) + PR #1871 (open, SU(2)/SO(3) density)
- **§4(b) bar-even Lean lemma:** [`prop:q-beta-bar-even-kernel-invariant`](../../content/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-invariant.md) (PR #1875)
- **§4(a) radius-of-convergence:** [`prop:q-beta-radius-of-convergence-gate`](../../content/quantum-observable-universe/mass-theory/q-beta-radius-of-convergence-gate.md) (PR #1889)
- **§4(c) q=1 shadow:** [`prop:q-beta-q-eq-one-shadow-gate`](../../content/quantum-observable-universe/mass-theory/q-beta-q-eq-one-shadow-gate.md) (PR #1890)
- **§4(d) direction sanity:** [`prop:q-beta-direction-sanity-gate`](../../content/quantum-observable-universe/mass-theory/q-beta-direction-sanity-gate.md) (PR #1890)
- **Unified `BarEvenKernel` typeclass:** [`prop:q-beta-bar-even-kernel-typeclass`](../../content/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-typeclass.md) (PR #1893)
