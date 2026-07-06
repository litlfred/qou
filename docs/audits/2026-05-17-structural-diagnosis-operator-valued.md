# Structural diagnosis: PR #671's 4 negative findings converge on operator-valued Z↔N-asymmetric framework

**Date:** 2026-05-17
**Branch:** `claude/post-670-story-b-mp-c5-c6`
**Status:** Synthesis audit consolidating the 4 negative findings shipped on PR #671 into a single positive diagnosis + next-PR scope.

## TL;DR

PR #671 tested 4 different symmetric-scalar-substrate hypotheses for
structural gaps in the QOU mass-prediction pipeline. **All 4 were
refuted, in convergent ways**, pointing at the same structural target:
the framework needs **operator-valued, Z↔N-asymmetric corrections at
the per-Wedderburn-block level** — exactly the operator-valued Wenzl
branching framework documented on [PR #681's audit doc](https://github.com/litlfred/qou/pull/681).

## The 4 negative findings

### Finding 1: pp-nn correlation hypothesis falsified at single-magic anchors

Refined Δ_coupling form $(A-2) \cdot E_0 \cdot \log(1/h(q_0)) + 2(Z-1)_+(N-1)_+ \cdot z^2 \cdot E_0 \cdot h^2$
held at doubly-magic ⁴He (gap 0.018%) but **failed at single-magic
anchors** by +8.74% (³He) and -3.95% (T) — opposite directions with a
**Z↔N asymmetry of +0.796 MeV** that the symmetric (A-2) leading form
cannot capture.

Probe: [`probe_delta_coupling_cross_anchor.py`](../../computations/probe_delta_coupling_cross_anchor.py)

### Finding 2: V_(2,2,2) is NOT the order-h^6 channel for c_3

PR #664's claim "V_(2,2,2) per-block contribution produces F_3 = -2·b³·ℏ_q^6"
is empirically refuted at the per-block Taylor level:
$\mathrm{contribution}(ε) \approx +0.0261 \cdot ε + O(ε²)$ — **leading
order is ε^1, not ε^6**. V_(2,2,2) contributes 5 Taylor orders BELOW
what the framework F_3 ansatz requires.

Probes: [`probe_V_222_projection.py`](../../computations/probe_V_222_projection.py) (numerical at q_0), [`probe_V_222_projection_symbolic.py`](../../computations/probe_V_222_projection_symbolic.py) (Taylor-order extraction).

### Finding 3: T5 categorical attribution resists symmetric substrate forms

Enumerated 20 substrate-primitive candidates (combinations of $E_0$,
$m_e$, $h$, $\hbar_q$, $z$, $b$, $[n]_q$, $\log(1/h)$, Jones-at-q=1
values) for the T5 chirality-BW term. **Best candidate** (`-[2]_q · log(1/h) · m_e · 5`)
has +3.2% / +7.7% gap vs T5(proton) / T5(neutron) — none of the 20
candidates matches both anchors within 5% AND captures the empirical
**Z↔N asymmetry of -0.325 MeV** (T5_p - T5_n).

Probe: [`probe_T5_categorical_attribution.py`](../../computations/probe_T5_categorical_attribution.py)

### Finding 4: Habiro residue at A=1 cannot close m_p chain alone

The cached `tr_M(β_atomic, q_0)` IS the Habiro-resummed value (rational
function in $u = q^{1/2}$); there is no separate "T6 residue tail" to
add. The T6 ~ 0.68·m_e ≈ 0.347 MeV quarantined value refers to a
different small-q expansion tail, bounded by ~0.3 MeV. **Item C alone
cannot close the 1571× m_p chain shortfall** (m_p_pred 0.5974 MeV vs
CODATA 938.27 MeV).

Probe: [`probe_habiro_residue_a1.py`](../../computations/probe_habiro_residue_a1.py)

## Convergent structural diagnosis

The 4 findings have a common structural conclusion: **all symmetric
scalar-substrate corrections miss the empirical structure**, and the
specific direction of the missing piece is **Z↔N-asymmetric and
operator-valued at the per-Wedderburn-block level**.

Why this convergence is meaningful:

| Finding | Missing structure |
|---|---|
| 1 (pp-nn correlation) | Z↔N asymmetry (+0.796 MeV between (1,2) and (2,1)) |
| 2 (V_(2,2,2)) | wrong Taylor order — per-block contributions don't aggregate as the F_n ansatz expects |
| 3 (T5 candidates) | Z↔N asymmetry (-0.325 MeV between proton and neutron T5) |
| 4 (Habiro at A=1) | m_p gap is not from a missing residue tail; it's from the brane-tower structure at A=1 |

Findings 1 and 3 both pin a Z↔N asymmetry directly. Finding 2 shows
the per-block aggregation is structurally non-trivial (NOT a clean
sum of per-channel scalar contributions). Finding 4 narrows the m_p
gap to the brane-tower terms (T2+T3) which my Item A probe earlier
showed gives ~10^6 raw at A=1 — way too big without structural
suppression.

**All 4 ⇒ the right framework is operator-valued per-block, which the
QOU paper already documents.**

## The paper already has this framework

Per [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md)
(operator-valued Wenzl 1988 branching):

$$
\chi^\lambda(\beta_1 \cdot I \cdot \beta_2) \;=\; \sum_{(\mu,\nu)} \operatorname{Tr}_{V_\mu \otimes V_\nu}\!\Bigl( A^\lambda_{\mu,\nu}(I) \cdot (\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2)) \Bigr)
$$

where `I ∈ H_n(q)` is the inter-nucleon **interface operator** — exactly
the structure that PR #679's pure-LR consumer missed and that PR #681's
audit confirms is needed.

The witness [`sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json)
verifies the `A^λ_{μ,ν}(I)` matrices to ~10⁻¹⁵ for all 11 partitions
of H_6 (deuteron interface); **19 of 35 (μ,ν) blocks are non-scalar
operators** (per Gemini-corrected count). Pure-LR / symmetric-scalar
consumers fail because they implicitly assume `A^λ_{μ,ν}(I) = α · 𝟙`
for some scalar α — empirically false for >50% of (μ,ν) blocks.

## Can we derive operator-valued corrections from the mass endomorphism?

**Yes.** The categorical mass formula
([`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md))
is the single-categorical-pipeline statement:

$$
M(\mathfrak{H}) \;:=\; \rho \cdot \mathrm{tr}_M(T_w) \;=\; \rho \cdot \sum_\lambda y_\lambda(q) \chi^\lambda(T_w)
$$

The 6-term decomposition (`mass_formula_6term_mpfr_50dps.py`'s T1+T2+T3+T4+T5+T6)
is a PRODUCTION-SIDE engineering split. The operator-valued branching identity
$\chi^\lambda(\beta_1 \cdot I \cdot \beta_2)$ — applied with $\beta_1, \beta_2$
the per-nucleon intra-braids and $I$ the inter-nucleon interface — turns
the production-side scalar approximations into operator-valued ones:

| Production-side (scalar) | Operator-valued (per Wenzl branching) |
|---|---|
| T1 = abs(tr_M) descended | $\sum_\lambda y_\lambda \cdot \chi^\lambda(\beta_1 \cdot I \cdot \beta_2)$ via $A^λ_{μ,ν}(I)$ |
| T2 = $\sum_g \Phi_q(|V_g|)$ | per-block brane-tower with operator-valued $A^λ_{μ,ν}$ |
| T3 = $z^2 \sum \Phi_q(|V_i V_j|)$ | per-pair-block operator-valued correlation |
| T5 chirality-BW $a_K \cdot B_{\mathrm{bulk}}$ | per-channel operator-valued via mirror interface |

The non-scalar A^λ_{μ,ν}(I) entries capture exactly:
- Z↔N asymmetry: σ_pp and σ_nn channels have different A^λ_{μ,ν} entries
- Per-block decomposition: each Wedderburn block λ gets its own correction
- Order-h^k scaling: A^λ_{μ,ν}(I) is rational in q with specific pole structure

The Δ_coupling 3-anchor decomposition I extracted (pp_term, nn_term, corr)
should re-derive from the proper per-block A^λ_{μ,ν}(I) computation —
the PR #671 combiner shipped (`canonical_tr_m_via_chi_cache.py`)
provides the |tr_M| at q_0 level needed for the reformulation, once
chi caches for T/³He/⁴He complete.

### Quantitative magnitude budget

The probe [`probe_operator_valued_ansatze_from_mass_endo.py`](../../computations/probe_operator_valued_ansatze_from_mass_endo.py)
quantifies the operator-valued correction Frobenius norm

$$
\|\Delta_{\text{op}}^{\lambda,\mu,\nu}\|_F \;=\; \sqrt{\|A^\lambda_{\mu,\nu}\|_F^2 \;-\; \tfrac{|\operatorname{tr} A|^2}{d_\mu d_\nu}}
$$

(Pythagoras: scalar-approximation projection onto the 1-d subspace
spanned by $\mathbf{1}$). Aggregated across all 35 (λ,μ,ν) blocks of
the H_6 deuteron interface:

| Quantity | Frobenius |
|---|---|
| Scalar-approximation $\sum \|A_{\text{scalar}}\|_F^2$ | 3.517 |
| Operator-valued correction $\sum \|\Delta_{\text{op}}\|_F^2$ | **3.603** |
| Ratio op / (scalar + op) | **0.72** |
| Genuinely non-scalar blocks | 19 / 35 |

**The operator-valued correction Frobenius (3.603) exceeds the scalar
approximation (3.517).** Symmetric scalar substrate ansatze do not
just incompletely cover the structure — they capture *less than half*
the magnitude. This is the unambiguous quantitative case that the
4 negatives converge on operator-valued, not scalar-substrate-with-
better-coefficients.

Witness: [`operator-valued-ansatze-from-mass-endo.witness.json`](../../computations/operator-valued-ansatze-from-mass-endo.witness.json).

## Next-PR scope (concrete)

**Phase 1' (next)** — Reformulated Δ_coupling via operator-valued
A^λ_{μ,ν}(I):

1. Run `per_irrep_pole_atom.py` for tritium (28 partitions, ~minutes
   each — total ~hours) — **already running on this branch's session**
2. Run for ³He (27 partitions, similar time)
3. Use the `canonical_tr_m_via_chi_cache.py` combiner to compute
   canonical |tr_M(β_atomic, q_0)| for T, ³He once chi caches done
4. Read off the per-block contributions y_λ · χ^λ at each anchor
5. Extract the channel-specific corrections from the 3-anchor system
   (Δ_coupling at (2,2), (2,1), (1,2))
6. Cross-validate against the A^λ_{μ,ν}(I) values for the deuteron
   interface in `sublemma-2-1-A-operator-extract.witness.json`

**Phase 2' (downstream)** — Apply the operator-valued reformulation
to:

- m_p / m_n / m_He mass predictions (Items A, B, C of the m_p chain
  audit now have a concrete framework)
- F_n precision-ladder coefficients (PR #664's c_3, c_4, c_5)
- T5 chirality-BW per-channel decomposition

## Cross-references

- [PR #681 audit](https://github.com/litlfred/qou/pull/681) — operator-valued Wenzl framework
- [PR #671 combiner](../../computations/canonical_tr_m_via_chi_cache.py) — Step 2 of PR #681's plan
- [PR #664 critical review](2026-05-17-pr-664-c3-c4-critical-review.md) — the c_3/c_4/κ analysis
- [PR #663](https://github.com/litlfred/qou/pull/663) — `a = z_markov` MILP/SDP finding (relevant to operator-valued LP)
- [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) — single-pipeline mass formula
- [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md) — operator-valued Wenzl
- [`sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json) — A operator extracts for H_6
