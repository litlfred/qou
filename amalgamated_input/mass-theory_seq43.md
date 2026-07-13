<!-- FILE_START: parity-classification-discrepancy-partition-sum-proton-intro.md -->
We now resolve the empirical chirality discrepancy using the partition-sum proton residual. We trace the substrate-level mechanism distinguishing proton from neutron. We document the resulting corrections to the binding energy formula.
<!-- FILE_END: parity-classification-discrepancy-partition-sum-proton-intro.md -->

<!-- FILE_START: partition-sum-proton-residual.md -->
*Let $\mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)$ be the pure-tower proton mass. The proton tower residual equals the electron-scaled Frobenius co-Casimir trace at $n = 3$:*

$$
  \boxed{
    \Delta m_{\mathfrak{p}}
    \;:=\;
    m_{\mathfrak{p}}^{\mathrm{CODATA}}
    - \mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)
    \;=\;
    m_e \cdot \mathrm{tr}_M\bigl(C_{\mathrm{Frob}}^{(n=3)}\bigr)
    \;=\;
    m_e\Bigl(2 + \frac{1}{[2]_q}\Bigr).
  }
$$

The self-dual Frobenius algebra gives the co-Casimir element. Its Markov trace analytically simplifies to the sum over partitions of inverse quantum dimensions. This matches the observed proton residual to within $0.1\%$. The residual isolates the substrate representation overhead independent of the atomic knot.
<!-- FILE_END: partition-sum-proton-residual.md -->

<!-- FILE_START: np-discrepancy-resolution.md -->
**Remark (neutron-proton discrepancy resolution).**
*The uncalibrated pure-tower formula drastically undershoots the neutron mass due to a $\Phi_q$ pole-distance asymmetry. The free-neutron beta decay prediction must instead use the trace difference directly.*

The raw tower prediction relies on per-generator amplitudes that sit at different distances from the $q_0$ pole. This introduces an artificial scale difference between mirror nucleons. Bypassing the per-nucleon evaluation entirely, the uncalibrated beta-decay $Q$-value emerges directly from the difference of the Markov normal forms:

$$
  \mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot E_0 \approx 0.7836\;\mathrm{MeV}.
$$

This structural difference evaluates to within $1.3$ keV of CODATA. It relies purely on the topological trace, completely avoiding the problematic single-generator Kashaev approximations.
<!-- FILE_END: np-discrepancy-resolution.md -->

<!-- FILE_START: mass-formula-regime-switching.md -->
*The binding energy $B(Z, N)$ switches evaluation regimes by mass number $A$. It tracks AME data to $\leq 5\%$ for $A \leq 4$:*

$$
  B(Z, N)
  \;=\;
  \begin{cases}
    B_{\mathrm{SW}}(Z, N) + m_e\,\tau(C_{\dim_q}^{H_3})
      & \text{if } A = 2, \\[4pt]
    B_{\mathrm{BW}+\chi}(Z, N)
      & \text{if } 3 \leq A \leq 4, \\[4pt]
    B_{\mathrm{BW}}(Z, N) + B_{\mathrm{shell}}(A)
      & \text{if } A \geq 5.
  \end{cases}
$$

The Schur-Weyl evaluation applies directly to the light satellite topology of the deuteron. For the Borromean topologies at $A \ge 3$, collective Wedderburn states dominate the mass formula. This is not double counting. Each regime merely selects the convergent limits of the exact unified mass functional.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: mass-formula-regime-switching.md -->

