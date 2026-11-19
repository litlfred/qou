This simulator computes nuclear beta-decay half-lives from the aether parameter $q$. It evaluates the transfer matrix Skein polynomial.

## Computed quantities

For a nucleus $\mathcal{N}(Z, N)$, the simulator determines:

1. **Skein polynomials.** It evaluates $P_{\mathrm{par}}(q)$ and $P_{\mathrm{dau}}(q)$.
2. **$Q$-value.** It calculates $Q = |\ln(P_{\mathrm{dau}}/P_{\mathrm{par}})| \times E_{\times} \times \mu_0$.
3. **Phase-space integral.** It evaluates $f(Z, Q)$ with the Skein-Coulomb Fermi function $F_q(Z, E)$.
4. **Half-life.** It computes $t_{1/2} = \ln 2 / \Gamma_\beta$.

## Operating modes

- **From $q$.** The simulator predicts the $Q$-value from the transfer matrix ratio.
- **From $Q_{\mathrm{exp}}$.** The simulator isolates the $q$-dependent prefactors and Coulomb enhancement using experimental $Q$-values.

## Physical regimes

The plot illustrates three regimes:

- **Classical** ($q \to 1$). $\Gamma_\beta \to 0$. No beta decay.
- **Descartes** ($q = q_0$). Recovers observed nuclear lifetimes.
- **Deep quantum** ($q \to \infty$). $\Gamma_\beta \to \infty$. Instantaneous decay.

## Benchmark nuclei

The verification nuclei and data are tabulated in [Table: Verification nuclei](#tbl:beta-decay-simulator-table-data).
