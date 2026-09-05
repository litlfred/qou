*Define the curvature-rank-$k$ residue functional using the q-deformed Wedderburn weight $w_\lambda(q) = \dim_q^2 V_\lambda / [n]_q!$:*

$$
  \Phi_k(\mathcal{K}, \mathcal{T})
  \;:=\; \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
  w_\lambda(q) \cdot \log\Bigl|\!\int_{A_\lambda}\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$

*The universal residue extracts the high-tower contribution as:*

$$
  \mathfrak{m}^{\geq 4}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \alpha \cdot \!\!\sum_{k \geq 4}\!\Phi_k(\mathcal{K}, \mathcal{T}),
  \qquad \alpha \;=\; m_e \cdot 8G.
$$

At low strata ($k \leq 3$), the restricted Frobenius integral routes through distinct hyperbolic-knot ideals. At deep strata ($k \geq 4$), specific knot identities evaporate. The surviving residue isolates the universal Frobenius co-Casimir tail, dependent solely on the block weight topology.

**Note on the weight's normalisation (added 2026-09-05).** $w_\lambda(q) = \dim_q^2 V_\lambda/[n]_q!$ as written above is **not** a probability measure: $c_n = \sum_\lambda \dim_q^2/[n]_q!$ is $0.9874 / 0.9911 / 1.1109 / 1.5171$ at $n = 3/6/9/12$ at the substrate $q_0$, and the defect is structural rather than a $q$-integer-convention artifact — the $q$-deformation breaks Burnside's $\sum_\lambda (f^\lambda)^2 = n!$, and no convention restores it.

**This does not invalidate the definition above, but the cancellation is narrower than it first appears.** $\Phi_k$ is *linear* in $w_\lambda$ and enters observables only through differences $\Phi_k^{\text{free}} - \Phi_k^{\text{atom}}$, so rescaling $w$ by a $\lambda$-independent constant rescales the whole functional. The precise condition is:

> $c_n$ cancels **iff the reported quantity is a ratio of two $w$-weighted sums at the same $n$.**

**Two ways that fails, and both occur in production** (corrected 2026-09-05 — an earlier version of this note said "cancels from any comparison made at fixed $n$", which is *too permissive* and would wave through both):

1. **Across $n$.** $c_n$ depends on $n$, so any quantity comparing different $n$ — equivalently different mass number $A$, since $n = 3A$ — is distorted by its spread.
2. **At fixed $n$, against a non-$w$-weighted quantity.** A $w$-weighted number compared to an experimental magnitude, a closed-form scalar, or a $y_\lambda$-weighted object does **not** cancel, because only one side carries $c_n$. Measured instances: [`probes/deuteron_fpn_wlambda_wiring.py`](../../../computations/probes/deuteron_fpn_wlambda_wiring.py) ($n=3$, against the AME-required $f_{pn}$) and [`yekutieli_volume_join.py`](../../../computations/yekutieli_volume_join.py) ($k=3$, against a closed-form linking weight).

**And $c_n$ is producer-specific — do not carry the numbers above between producers.** A producer that binds $\dim_q$ to the *classical* $f^\lambda$ (as the two log-delta producers do) has normalizer $n!/[n]_q!$, measured $0.980 / 0.858 / 0.612 / 0.326$ at $n = 3/6/9/12$: a $3.0\times$ spread **decreasing** in $n$, where the $\dim_q^2$ form gives $0.987/0.991/1.111/1.517$, increasing. Neither the magnitude nor the direction transfers. Measure per producer. Consumers of this definition that compare atoms must therefore use the self-normalised form $\dim_q^2/\sum_\mu \dim_q^2 = d_q^2/D^2$, the Reshetikhin–Turaev/Verlinde measure, which differs from the form above by exactly that $\lambda$-independent factor (Lean: `QOU.BraidKnot.WLambdaNormalizationInvariance.wPlanch_eq_global_factor`, sorry-free). [`fr_pullback_k3_test.py`](../../../computations/fr_pullback_k3_test.py) and [`fr_pullback_borromean_h3a_test.py`](../../../computations/fr_pullback_borromean_h3a_test.py) now do; the divergence between their weight and the one written here is deliberate and is recorded rather than silent. Measurements: [`2026-09-04-plancherel-convention-gap.md`](../../../docs/audits/2026-09-04-plancherel-convention-gap.md); registry [§B-norm](../../../docs/coordination/trace-convention-registry.md).

Whether $\dim_q^2$ is the right *numerator* at all — as against the Molien weight $f^\lambda \dim_q(\lambda)$, which sums to $[n]_q!$ exactly for all $n$ and all $q>1$ (`QOU.MathlibExt.NormalizedSumUnconditional.molienSum_eq_qFactorial`, sorry-free), or the Markov weights $y_\lambda$ of the canonical Frobenius pairing — is a separate and **open** question, bean `qou-oots`.
