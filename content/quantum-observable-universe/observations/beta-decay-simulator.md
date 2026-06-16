An interactive simulator that computes nuclear beta-decay half-lives
from the substrate parameter $q$ using the transfer matrix Skein
polynomial ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)).

## What is computed

For a nucleus $\mathcal{N}(Z, N)$, the simulator evaluates:

1. **Skein polynomials** $P_{\mathrm{par}}(q)$ and
   $P_{\mathrm{dau}}(q)$ for parent and daughter via
   $\binom{A}{2}$ transfer matrix multiplications
   ([transfer matrix operator](#def:transfer-matrix-operator)).

2. **$Q$-value** from the ratio
   $Q = |\ln(P_{\mathrm{dau}}/P_{\mathrm{par}})| \times
   E_{\times} \times \mu_0$, optionally with the shell correction
   $\Delta_{\mathrm{shell}} + \Delta_{T_{3,5}}$
   ([shell construction rules](#rem:shell-construction-rules)).

3. **Phase-space integral** $f(Z, Q)$ with the
   Skein-Coulomb Fermi function $F_q(Z, E)$
   ([Skein-Coulomb enhancement](#prop:skein-coulomb-enhancement))
   using $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$.

4. **Half-life** $t_{1/2} = \ln 2 / \Gamma_\beta$ where
   $\Gamma_\beta = G_F^2 m_e^5 / (2\pi^3 \hbar) \cdot [2]_q
   \cdot f(Z, Q)$
   ([hadron half-life](#prop:hadron-half-life)).

## Two modes

- **From $q$**: the $Q$-value is predicted from the
  transfer matrix ratio.  Accurate for light nuclei ($A \leq 14$,
  $5$--$7\%$ error); heavy nuclei overshoot due to naive nucleon
  ordering ([verification](#ex:hadron-half-life-verification)).

- **From $Q_{\mathrm{exp}}$**: uses experimental $Q$-values
  (NNDC/ENSDF).  Isolates the $q$-dependent prefactors and Coulomb
  enhancement.  All six benchmarks agree to $< 3\%$.

## Three regimes

The canvas plot shows $t_{1/2}$ vs $q$ for the selected nucleus,
illustrating the three regimes
([half-life regimes](#rem:hadron-half-life-regimes)):

- **Classical** ($q \to 1$): $\Gamma_\beta \to 0$, no beta decay.
- **Descartes** ($q = q_0$): observed nuclear lifetimes.
- **Deep quantum** ($q \to \infty$): $\Gamma_\beta \to \infty$,
  instantaneous decay.

The sensitivity $\partial \ln \Gamma / \partial \ln q \approx 48$
at $q_0$ is displayed — a $1\%$ shift in $q$ changes decay rates
by $\sim 50\%$.

## Benchmark nuclei

The verification nuclei and their experimental data are tabulated in
[Table: Verification nuclei](#tbl:beta-decay-simulator-table-data).

Witness data from
`computations/all-nuclei-transfer-matrix.py`.
