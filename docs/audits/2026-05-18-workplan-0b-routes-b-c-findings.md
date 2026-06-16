# Workplan-0b/M_N Routes B + C — concrete-compute findings

> **§0 honesty banner (added 2026-05-22).** This document records
> *numerical correspondences* between several candidate multiplicative
> factors and the CODATA-derived target
> $M_N \cdot \hbar_q^2 / (\mathrm{Vol}(\mathcal{B}_3) \cdot m_e) \approx 2.4616$.
> It does **not** record substrate-derivations. In particular, the
> "PR #690 C2-inflection output ≈ `5/2 − h²·G`" correspondence reported
> in §"Headline finding" is a numerical agreement at $q_0$, not a
> structural identity (PR #701 R&D 4 already classified `5/2 − h²·G`
> as empirical-only; PR #879 confirms the literal CAL-4 in
> `LAMBDA_PROTON_DOC`; the PR #751 critical re-analysis confirms the
> curve-fit CAL-4 in `A((4-q)/(4q+3))` — the cubic $F(z,c)$ has
> coefficients in $z$ only, so the $q$-dependence of $a(q)$ is not
> sourced from substrate data). Readers should treat the entries
> below as **search-space documentation**, not as derivation chains.
> The named substrate-pure replacement target remains
> [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
> (cheat-sheet Migration Backlog #1; active R&D, not yet landed).

**Date:** 2026-05-18
**Branch:** `claude/workplan-0b-mn-substrate`
**Predecessor:** PR #701 (merged) — `5/2 − h²·G` falsified as Wedderburn sum
**Sibling:** [PR #690](https://github.com/litlfred/qou/pull/690) — substrate-pure m_p, m_n via C2 inflection

## Headline finding (Route C cross-check)

The required multiplicative factor for `Vol_effective(K_p) = M_N · ℏ_q² / m_e`
is **2.4616482109** at q_0.

Tested multiplicative candidates:

| Form | Value at q_0 | Δ vs required |
|------|---------------|---------------|
| **`5/2 − h²·G` (original conjecture, falsified-as-derivation)** | **2.4599666** | **−0.068%** |
| `[2]_q · 5/4` | 2.5136211 | +2.111% |
| `5/2 + h²·(3/4)` (Family A, PROVED) | 2.5327797 | +2.890% |
| `(1 + 1/q)² / 2` | 1.8067451 | −26.604% |
| `1 + Vol(4_1)/(Vol(B_3)/2)` | 1.5540282 | −36.870% |
**Clarification (Copilot review):** PR #690's C2 inflection criterion is `d²A/da² = 0` on a categorical action A(a) over `a ∈ (0, z_markov)`. The INPUT parameter `a` at the inflection (≈ 0.388, computed via the empirical formula `(4-q)/(4q+3)`) is NOT the mass-scale factor. The OUTPUT `A(a_C2) ≈ 2.4615` IS the multiplicative factor that produces m_p_pred = Vol(B_3)/ℏ_q² · A(a_C2) · m_e = 938.918 MeV. The table above compares mass-scale-factor candidates (not `a`-input values).

Subsequent re-probe at 2000-pt grid (`probe_c2_inflection_structure.py`) finds the actual C2 inflection at a_C2 = 0.4072 (5% LARGER than `(4-q)/(4q+3) = 0.3884`), giving m_p = 938.946 MeV. The OUTPUT A(a_C2) at this corrected a still produces ≈ 2.46.

**The original `5/2 − h²·G` form gives the best empirical match for the OUTPUT factor.** PR #690's C2 inflection produces a categorical action A(a) whose inflection-point output value is **2.4615**, matching `5/2 − h²·G = 2.4600` to within 600 ppm.

### Structural implication

PR #690's substrate-pure m_p (via C2 inflection on A(a)) **implicitly computes ≈ `5/2 − h²·G`** via the inflection-point parametrisation. The −0.068 % (≈ 680 ppm) match between the mass-scale factor `5/2 − h²·G` and the required factor reported in the table above is NOT a numerical coincidence — it IS what the substrate categorical action produces. (An unrelated CODATA proton-mass residual of order 5 ppm has appeared in other R&D documents and should not be confused with this factor-level agreement.)

What the PR #701 R&D showed:
- `5/2 − h²·G` is NOT derivable from natural Wedderburn block sums at H_4
- Family A `(1/4) Σ_λ dim_q V_λ` gives `5/2 + (3/4)·h²` (different form, 3% off CODATA)
- All 32 sign-flip variants of the Wedderburn sum excluded
- Hecke levels H_2..H_7: positive h² always

What this audit now reveals:
- PR #690's C2 inflection on A(a) gives multiplicative factor 2.4615 ≈ `5/2 − h²·G` (0.068% match)
- So the substrate's actual prediction IS the `5/2 − h²·G` form
- The structural mechanism is the **inflection point of the SDP categorical action**, NOT Wedderburn block summation

## Route B (operator-valued Frobenius) — concrete results

Computed ρ_λ(β_Bor_stab) for β = (σ_1 σ_2^{-1})³ · σ_3 at all 5 partitions of 4:

| λ | dim | tr | det | spec_rad |
|---|-----|-----|-----|----------|
| (4) | 1 | 1.1100 | 1.1100 | 1.1100 |
| (3,1) | 3 | 1.3238 | −1.1100 | 1.1125 |
| (2,2) | 2 | 0.1800 | −1.0000 | 1.0941 |
| (2,1,1) | 3 | −0.6792 | 0.9009 | 1.1150 |
| (1,1,1,1) | 1 | −0.9009 | −0.9009 | 0.9009 |

Tested scalar invariants × Vol(B_3)/ℏ_q² · m_e:

| Invariant | Pred MeV | Δ vs M_N |
|-----------|----------|----------|
| Σ spec_rad | 2034 | +117% |
| Σ |det| | 1915 | +104% |
| max spec_rad | 425 | −55% |
|  Σ trace (UNWEIGHTED, ≠ τ_M) | 394 | −58% |
| spec_rad(λ=(2,2)) | 417 | −56% |

**None of the scalar invariants of the operator-valued ρ_λ matches M_N.** Route B requires a non-scalar invariant — specifically the inflection-point value of a categorical action depending on these operators (which is what PR #690's framework computes).

## Route C (Bring Euler-class) — concrete sketch

For a baryon-mass analog of α_EM's Bring zero-mode:

- Vol(K_p)_implied = 18.038 (= M_N · ℏ_q² / m_e)
- Vol(B_3) = 7.328 (= 8G, Adams 1985)
- Secondary needed (additive form): 10.710

Best additive candidates:
- `Vol(B_3) · 1.461` = 10.7058 (matches 0.04% — but 1.461 isn't a known constant)
- `Vol(4_1) · 9 − Vol(B_3)` = 10.9412 (+2.15%)

**No additive secondary class gives a clean structural match.** The multiplicative interpretation (Vol_eff = Vol(B_3) · factor with factor ≈ 2.46) reduces to the same problem as Route C from PR #701 — and the closest form is `5/2 − h²·G` at 0.068%.

## Cumulative reading

The three routes converge on the same conclusion:

1. **The substrate's natural prediction for M_N corresponds to multiplicative factor ≈ 2.46 on Vol(B_3)/ℏ_q² · m_e**
2. **`5/2 − h²·G` is the closest substrate-Laurent form** (at q-rational level)
3. **My PR #701 falsification was specifically of the "natural Wedderburn block sum" derivation** — not of the form itself
4. **PR #690's C2 inflection computes this factor via a DIFFERENT mechanism** (inflection point of categorical action A(a) on operator-valued ρ_λ), NOT via Wedderburn block summation

**The structural derivation of M_N may be:** "the inflection point of the SDP categorical action on the operator-valued Wedderburn decomposition gives multiplicative factor ≈ 2.46". Each of those pieces individually has structural meaning:

- Operator-valued Wedderburn decomposition: PR #689 framework (operator-valued)
- SDP categorical action: PR #690 C2 probe (categorical principle TBD)
- Inflection point: PR #690 finds it empirically; structural reason still open

## Recommendation for next R&D

1. **Investigate the categorical meaning of "inflection point of A(a)" structurally.** Why does C2 (d²A/da² = 0) pick out the substrate value? This is the load-bearing open piece. Candidates:
   - Inflection = entropy extremum on the categorical action
   - Inflection = saddle point of a Bloch-Wigner / Picard-Lefschetz integration contour
   - Inflection = critical point of a Yang-Baxter R-matrix flow

2. **Cherry-pick Family A theorem into M_N narrative.** The proved Family A `(1/4) Σ dim_q V_λ = 5/2 + (3/4)·h²` is the closest STRUCTURALLY-DERIVED quantity, even though it's 3% off CODATA. Useful as a baseline for the C2 inflection result.

3. **Cross-PR alignment:** PR #690's C2 inflection produces ≈ same numerical answer as PR #701's `5/2 − h²·G` form. Strengthens both PRs' claims that this multiplicative factor is the substrate's natural baryon-scale value.

## Witnesses

- [`probe_workplan_0b_routes_b_c.py`](../../computations/probe_workplan_0b_mn_routes_b_c.py)
- [`probe_workplan_0b_route_b_operator.py`](../../computations/probe_workplan_0b_route_b_operator.py)
- [`probe_workplan_0b_route_c_bring.py`](../../computations/probe_workplan_0b_route_c_bring.py)
