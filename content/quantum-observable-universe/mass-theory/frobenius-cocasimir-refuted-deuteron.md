**Lemma (Frobenius co-Casimir Δ_λ ansatz refuted at the deuteron).**
*The Frobenius co-Casimir prescription $\Delta_\lambda = 1/\dim_q(\lambda)$ does
not close the per-isotope binding formula
$B(\mathcal{K}) = \mathfrak{m}_e \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$
at the deuteron anchor. Its signed binding-density sum*
$$
\Sigma_{\mathrm{coCas}} \;=\; +0.14496\ \mathfrak{m}_e
\qquad\text{misses the empirical target}\qquad
\Sigma_{\mathrm{target}} \;=\; -4.35337\ \mathfrak{m}_e ,
$$
*by $|\Sigma_{\mathrm{coCas}} - \Sigma_{\mathrm{target}}| = 4.49833\ \mathfrak{m}_e
> \text{tol} = 1$, and with the opposite sign
($\Sigma_{\mathrm{coCas}} > 0 > \Sigma_{\mathrm{target}}$).*

The co-Casimir ansatz is theorem-forced (no free parameters), so the miss
cannot be absorbed by a fit: it is a **magnitude** refutation (gap $\approx 4.5$
$\mathfrak{m}_e$ units against tolerance $1$) and a **sign** refutation
(positive prediction versus a negative target — the ansatz is vortex-blind).
This is the first of the six refuted $\Delta_\lambda$ closure ansätze
(Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal-graph, augmented Markov); the $\Delta_\lambda$ gate's "no seventh
fit-based ansatz" rule is the standing consequence.

## Lean structure

The refutation is a machine-checked rational (in)equality, sorry-free over
$\mathbb{Q}$ (decidable, `norm_num`-discharged): `coCasimir_refuted_deuteron`
($\text{tol} < |\Sigma_{\mathrm{coCas}} - \Sigma_{\mathrm{target}}|$) and
`coCasimir_wrong_sign` ($0 < \Sigma_{\mathrm{coCas}} \wedge
\Sigma_{\mathrm{target}} < 0$). The literals are 12-figure truncations of the
50-dps witness `rho-k-h3a-co-casimir.witness.json`; the gap exceeds tolerance by
a factor of $\approx 4.5$, so the inequality holds with large margin. Promoting
the standalone library refutation to this block places it under per-block QA so
the dead ansatz cannot be silently re-proposed past review.
