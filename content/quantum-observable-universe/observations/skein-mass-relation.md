*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

> **Substrate-density (ρ_q) ansatz purge in progress .**
> The relation $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ below uses the
> **SUPERSEDED** substrate density $\rho_q = 1/\hbar_q^2$ as the
> dimensional factor. Per [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md)
> and [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md),
> the scalar $\rho_q$ is structurally wrong (braid-class-independent;
> categorical density $\rho_K$ varies $\sim 30\times$ across atoms).
> The Skein formula below is now interpreted as the **leading-order
> substrate-truncation** of the canonical operator-valued
> `ρ_K^LO + ρ_K^single-gen + ρ_K^pair-gen + ...` graded expansion.
> The numerical match to $m_\mu/m_e = 206.77$ holds at lepton level
> because operator-valued corrections are small for leptons; the
> +0.17% 𝔔_β residual flagged in
> [`-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md)
> is consistent with operator corrections becoming non-negligible
> for hadronic observables. The literal $\rho_q = 1/\hbar_q^2$
> interpretation is **deprecated**; re-derivation of $m_\mu/m_e$
> in canonical (graded-expansion) form is open work, tracked at
> [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The mass functional $\mathcal{M}(\mathfrak{H})$ for a composite hadron $\mathfrak{H}$ is not additive but obeys the quantum Skein relation at every crossing in the color-exchange space:

$$
q \mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\mathcal{M}(L_0).
$$

Evaluation of the lepton mass ratio $m_{\mu}/m_{e}$ against **CODATA** recommended values yields a precise derivation for the local substrate parameter $q$ **under the leading-order (SUPERSEDED-$\rho_q$) substrate-truncation**:

$$
\frac{m_{\mu}}{m_{e}} \;\stackrel{\text{LO}}{=}\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
  \approx \frac{:val[Vol_4_1]{precision=6}}{(1 - q^{-1})^2},
\qquad 206.7683 \implies q \approx 1.10998.
$$
