**Corollary (knot factor for Markov-amphicheiral knots).**
*Let $\mathcal{K}$ be **Markov-amphicheiral**: its mirror braid
representative $\beta_\mathcal{K}^*$ is conjugate to
$\beta_\mathcal{K}$ in $H_n(R, q)$ — i.e. there exists
$w \in H_n(R, q)^{\times}$ with*

$$
  \beta_\mathcal{K}^* \;=\; w\,\beta_\mathcal{K}\, w^{-1}.
$$

*Then the knot factor is a sum of positive squares weighted by
Plancherel weights:*

$$
  a_\mathcal{K} \;=\;
  \sum_{\lambda \vdash n}\, w_\lambda\,
  \frac{\chi_\lambda(\beta_\mathcal{K})^2}{\chi_\lambda(\mathbf{1})^2}.
$$

*Proof.*
By trace cyclicity,
$\chi_\lambda(\beta_\mathcal{K}^*) = \chi_\lambda(w\,\beta_\mathcal{K}\, w^{-1}) = \chi_\lambda(\beta_\mathcal{K})$
for every $\lambda$.  Substituting in
([knot factor](#prop:knot-factor-spectral-form))
$a_\mathcal{K} = \sum_\lambda w_\lambda \cdot
\chi_\lambda(\beta_\mathcal{K})\,\chi_\lambda(\beta_\mathcal{K}^*) / \chi_\lambda(\mathbf{1})^2$
yields the displayed expression.
$\square$

**Worked example ($\mathcal{K} = 4_1$ in $B_3$).** Take the
figure-eight braid
$\beta_{4_1} = \sigma_1\,\sigma_2^{-1}\,\sigma_1\,\sigma_2^{-1}$.
Direct computation of the Hoefsmit characters on the three
partitions $\lambda \vdash 3$ at the substrate $q_0$ gives:

| $\lambda$ | $\chi_\lambda(\beta_{4_1})$ | $\chi_\lambda(\beta_{4_1}^*)$ | match? |
|-----------|---:|---:|---|
| $(3)$ | $+1$ | $+1$ | yes |
| $(2,1)$ | $-1$ | $-1$ | yes |
| $(1,1,1)$ | $+1$ | $+1$ | yes |

All three characters agree, so $\beta_{4_1}^*$ is conjugate to
$\beta_{4_1}$ in $H_3(q)$ — i.e. $4_1$ is Markov-amphicheiral.
The displayed formula therefore applies, with

$$
  a_{4_1} \;=\;
  w_{(3)}\cdot 1
  \;+\; w_{(2,1)}\cdot \tfrac{1}{4}
  \;+\; w_{(1,1,1)}\cdot 1.
$$

This is the alternating-block projection used in the
${}^3\mathrm{H}$ and ${}^3\mathrm{He}$ formulas — not a fitted
ansatz.

> **Errata banner (2026-05-19) — proof's sign-flip claim flagged.**
> The proof's assertion
> $\chi_\lambda(\beta_\mathcal{K}^*) = (-1)^{[\lambda=(1^n)]}
> \chi_\lambda(\beta_\mathcal{K})$
> is empirically inconsistent with the canonical Hoefsmit characters
> of the figure-eight $\beta = \sigma_1 \sigma_2^{-1} \sigma_1
> \sigma_2^{-1}$ at $q_0$: the BD probe
> [`knot-factor-amphicheiral-BD-probe.witness.json`](../../../folio-assistant/computations/knot-factor-amphicheiral-BD-probe.witness.json)
> reports
> $\chi_{(1^3)}(\beta) = \chi_{(1^3)}(\beta^*) = +1$
> (writhe-0, no sign flip), not the predicted $\chi_{(1^3)}(\beta^*)
> = -\chi_{(1^3)}(\beta) = -1$.  The standard categorical reading is
> that amphicheirality preserves the **Markov trace**
> $\mathrm{tr}_M(\rho(\beta_\mathcal{K}))$, not individual block
> characters $\chi_\lambda(\beta_\mathcal{K})$; only the Markov-trace
> ratio is a topological invariant after Markov stabilisation.  A
> revised derivation of $a_\mathcal{K}$ via Markov-invariance — or
> a Gram-pairing form $a_\mathcal{K} = \mathrm{tr}_M(\beta \cdot
> \beta^*) / \mathrm{tr}_M(\mathbf{1})$ — is the natural next step
> and is filed in
> [`docs/coordination/2026-05-19-i1-hecke-cluster-handover.md`](../../../docs/coordination/2026-05-19-i1-hecke-cluster-handover.md)
> as a deferred follow-up.  This banner stages the issue for the
> revision and does **not** assert the displayed $a = 1 - h^2$
> formula is correct or incorrect — empirical agreement with
> tritium / helium-3 mass data remains the dispositive check, and
> the BD probe records the relevant Hoefsmit values for both
> $\beta$ and $\beta^*$.
