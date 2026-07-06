This interactive simulator computes nuclear beta-decay half-lives from the substrate parameter $q$. It evaluates the transfer matrix Skein polynomial ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)).

## Computed quantities

For a nucleus $\mathcal{N}(Z, N)$, the simulator determines four observables:

1. **Skein polynomials.** It evaluates $P_{\mathrm{par}}(q)$ and $P_{\mathrm{dau}}(q)$ for parent and daughter via $\binom{A}{2}$ transfer matrix multiplications ([transfer matrix operator](#def:transfer-matrix-operator)).
2. **$Q$-value.** It calculates $Q = |\ln(P_{\mathrm{dau}}/P_{\mathrm{par}})| \times E_{\times} \times \mu_0$. This calculation optionally includes the shell correction $\Delta_{\mathrm{shell}} + \Delta_{T_{3,5}}$ ([shell construction rules](#rem:shell-construction-rules)).
3. **Phase-space integral.** It evaluates $f(Z, Q)$ with the Skein-Coulomb Fermi function $F_q(Z, E)$ ([Skein-Coulomb enhancement](#prop:skein-coulomb-enhancement)) using $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$.
4. **Half-life.** It computes $t_{1/2} = \ln 2 / \Gamma_\beta$, where $\Gamma_\beta = G_F^2 m_e^5 / (2\pi^3 \hbar) \cdot [2]_q \cdot f(Z, Q)$ ([hadron half-life](#prop:hadron-half-life)).

## Operating modes

- **From $q$.** The simulator predicts the $Q$-value from the transfer matrix ratio. This yields $5$--$7\%$ error for light nuclei ($A \leq 14$). Heavy nuclei overshoot due to naive nucleon ordering ([verification](#ex:hadron-half-life-verification)).
- **From $Q_{\mathrm{exp}}$.** The simulator uses experimental $Q$-values (NNDC/ENSDF). This isolates the $q$-dependent prefactors and Coulomb enhancement. All six benchmarks agree to $< 3\%$.

## Physical regimes

The canvas plot shows $t_{1/2}$ versus $q$ for the selected nucleus. It illustrates three regimes ([half-life regimes](#rem:hadron-half-life-regimes)):

- **Classical** ($q \to 1$). Here $\Gamma_\beta \to 0$. The system exhibits no beta decay.
- **Descartes** ($q = q_0$). The framework recovers observed nuclear lifetimes.
- **Deep quantum** ($q \to \infty$). Here $\Gamma_\beta \to \infty$. Decay is instantaneous.

The plot displays the sensitivity $\partial \ln \Gamma / \partial \ln q \approx 48$ at $q_0$. A $1\%$ shift in $q$ alters decay rates by roughly $50\%$.

## Benchmark nuclei

The verification nuclei and their experimental data are tabulated in [Table: Verification nuclei](#tbl:beta-decay-simulator-table-data). Witness data from `computations/all-nuclei-transfer-matrix.py`.
