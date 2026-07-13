# Per-depth diagnosis of the 1.82× variance — PR #801

**Date**: 2026-05-19
**Context**: PR #801 (claude/log-delta-categorical-derivation), `binding_depth_stratified_rust.py`
**Question**: Why is the variance 1.82× (not 1.0×) when the depth-stratified α_k · Φ_k formula has the right categorical structure?

## Per-atom, per-depth contribution to B_pred

| atom | k=1 | k=2 | k=3 | **k=4** | k=5+ | Total | B_AME | AME/Pred |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D | 0.21 | 0.20 | 0.19 | 0.004 | 0 | 0.61 | 2.225 | **3.67×** |
| T | 0.03 | 0.19 | **1.41** | 0.76 | 0 | 2.81 | 8.482 | **3.02×** |
| ³He | 0.02 | 0.18 | **1.26** | 0.81 | 0 | 2.65 | 7.718 | **2.91×** |
| ⁴He | 0.001 | 0.09 | 2.28 | **9.50** | 0.60 | 14.06 | 28.30 | **2.01×** |

## Structural pattern

The under-prediction factor **monotonically decreases** with A: 3.67 → 3.02 → 2.91 → 2.01.

Each atom lives in a different *categorical stratum*:

- **D (A=2)**: low-k structural (k=1, 2, 3 each ~0.2, k≥4 ≈ 0). Dominated by curvature-rank 1–3 contributions which lack a *distinguished hyperbolic-knot ideal*.

- **T, ³He (A=3)**: **k=3 chirality channel** dominates (T: 1.41 / 2.81 = 50%; ³He: 1.26 / 2.65 = 48%). This is the `6_1` Frobenius integral restriction per `prop:plancherel-term-7-formulation` §"Why universal at k≥4".

- **⁴He (A=4)**: **k=4 universal stratum** dominates (9.50 / 14.06 = 68%). The α_{k≥4} = m_e · 8G universal residue is the structural majority contribution.

## Diagnosis: per-knot ideal restriction missing at low k

Per [`prop:plancherel-term-7-formulation`](../../content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.md), the *Frobenius integral* at low depth k ≤ 3 should factor through a *distinguished hyperbolic-knot ideal*:

> "At low strata k ≤ 3 the restricted Frobenius integral
> $\int_{A_\lambda} \rho(\beta_K) \cdot T$ factors through specific
> hyperbolic-knot ideals (e.g. $6_1$ at k=3, the chirality channel).
> At k ≥ 4 no specific knot ideal remains in the centre — what
> survives is the dualizing-complex residue."

**My current compute uses the uniform Wedderburn weight $\tilde w_\lambda = \dim_q^2/[n]_q!$ at all depths**, treating low and high k identically. This is incorrect per the proposition:

- **High k (≥4)**: uniform $\tilde w_\lambda$ correct (universal residue, no distinguished knot)
- **Low k (≤3)**: should *restrict to the distinguished hyperbolic-knot ideal* — e.g.
  - k=1: ? (per-atom ideal, possibly $4_1$ figure-eight)
  - k=2: ? (possibly $5_2$)
  - k=3: $6_1$ chirality channel (named explicitly in the proposition)

The per-knot restriction would **enhance low-k contributions** by the ratio of (full $A_\lambda$ algebra) / (knot-ideal restricted subalgebra) — typically a factor of order $\dim(A_\lambda) / \dim(\text{ideal})$.

This is the categorical content missing from my compute.

## What this means for variance closure

If the low-k contributions are enhanced by a per-knot factor, the under-prediction at small A (D, T, ³He) closes. At large A (⁴He+), the dominant k≥4 stratum already uses uniform weights correctly — small change.

Predicted variance closure (qualitative):
- D's deficit 3.67× → close (low-k enhancement of ~3×)
- T/³He deficit 3.0× → close (k=3 already chirality-channel-dominated)
- ⁴He deficit 2.0× → partial close (k=4 already correct; some low-k enhancement)

**Implementation gap**: identify the distinguished knot ideal for k=1 and k=2 in the unified curvature-rank framework. The k=3 case ($6_1$) is named in the prop; k=1 and k=2 are NOT named. This is an open structural question for the next PR.

## Categorical derivations unique to this PR (#801)

1. **Hecke-convolution binding** β_K = T_constit *_q Δ_I^K in same H_{3A}(q)
2. **Depth-stratified α_k · Φ_k** mass formula with structural prefactors
3. **Sign-correct via convolution** (tensor-product baseline gives wrong sign on T/³He)
4. **Block-multiplicativity conjecture** (V̂ A-independent at H_{3A}; classical-limit proven)
5. **LR-decomposition equivalence** (free-config χ factorises via iterated LR from H_3)
6. **Symmetric Li_2^q** mass tower (NOT compact q-dilog Φ_q — avoids −737 MeV mirror-nucleus pathology)

None of these are in the existing Kashaev mass-table-ppb pipeline. The two compute pathways are **complementary**:
- **Kashaev**: empirical/topological — Vol_hyp(K_closure) at ppb precision via volume-match
- **This PR**: structural categorical — α_k · Φ_k at H_{3A} via Wedderburn-character + interface-knot convolution

Closing the variance to ≤ 1.05× requires the per-knot ideal restriction at low k — an open structural item not in either pipeline today.
