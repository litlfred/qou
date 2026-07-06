**Proposition.**
*The atomic mass $\mathcal{M}(Z, N)$ is recovered from the
[unified six-term decomposition](#thm:six-term-mass-formula-complete)
by **per-term physical weights** read off the individual derivations,
without proton-fitting:*

$$
  \mathcal{M}(Z, N)
  \;=\;
  Z\, m_{\mathfrak{p}} + N\, m_{\mathfrak{n}} + Z\, m_e
  \;-\;
  B(Z, N)
$$

*where the binding energy is the term-by-term differential
between bound (`include_inter=True`) and free (`include_inter=False`)
configurations:*

$$
  B(Z, N)
  \;=\;
  \underbrace{E_{0,\beta} \cdot \big(T_1^{\rm free} - T_1^{\rm atom}\big)}_{\text{T1 binding}}
  \;+\;
  \underbrace{\alpha \cdot \big((T_2 + T_3)^{\rm atom} - (T_2 + T_3)^{\rm free}\big)}_{\text{T2/T3 binding}}
  \;+\;
  \underbrace{m_e \cdot \big(T_4^{\rm atom} - T_4^{\rm free}\big)}_{\text{T4 binding}}
  \;+\;
  \underbrace{E_{0,\beta} \cdot (a_K - 1) \cdot T_1^{\rm atom}}_{\text{T5 binding}}
  \;+\;
  \underbrace{\big(T_6^{\rm atom} - T_6^{\rm free}\big)}_{\text{T6 binding (MeV)}}
$$

**Per-term weights and their derivations.**

See [Table 1](#tbl:six-term-per-derivation-weights-table1-data).

*Critically the ratio
$\alpha / E_{0,\beta} = 4.79$ is non-trivial: the brane-tower
contribution $T_2 + T_3$ is on the Borromean–Catalan scale
$m_e \cdot 8G$, while the descended Markov trace $T_1$ is on the
β-decay $Q$ scale.  Earlier proton-fitted assemblies collapsed
the two into a single calibration, balancing at $A = 1$ but
propagating mass error rapidly with $A$.*
