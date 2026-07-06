The archimedean realization ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) assigns mass values to knot configurations. The substrate parameter is a smooth function $q \colon M \to \mathbb{C}^{\times}$. At a point $p \in M$ where the substrate is locally constant, the fibre algebra is $\mathcal{O}_{q(p)}(\mathrm{SU}(2)) \otimes_{\mathbb{Z}[q,q^{-1}]} \mathbb{C}$. The quantum Planck constant ([quantum Planck constant](#def:quantum-planck-constant)) evaluates to

$$
  \hbar_q(p) = 1 - q(p)^{-1}.
$$

We specialize the topological mass formula ([topological mass formula](#prop:topological-mass-formula)) to $q_0$ (derived from $m_\mu / m_e$, [skein mass relation](#rem:skein-mass-relation)):

$$
  \hbar_{q_0} = 1 - q_0^{-1} \approx 0.09889,
  \qquad
  \hbar_{q_0}^{-2} \approx 102.25.
$$

Evaluating over $\mathbb{C}[z]$ at $z = q_0$ yields the mass predictions:

| **Particle** | $\mathrm{Vol}(K)$ | $\mathfrak{m}(K) = \mathrm{Vol}(K) / \hbar_{q_0}^2$ | **CODATA** |
|---|---|---|---|
| Electron ($3_1$) | 0 (non-hyp.) | $m_e$ (baseline) | 0.511 MeV |
| Muon ($T_{2,5}$, via Higgs $4_1$) | 2.0299 | $2.0299 \times 102.25 \approx 207.6 m_e$ | $206.768 m_e$ |
| Proton | $Q(q_0) \mathrm{Vol}(\mathcal{L}_{\mathrm{Hopf}})_{uud}$ | 938.272 MeV | 938.272 MeV |
| Neutron | $Q(q_0) \mathrm{Vol}(\mathcal{L}_{\mathrm{Hopf}})_{udd}$ | 939.565 MeV | 939.565 MeV |

Passing from the categorical formula to numerical values requires the archimedean bridge. The fibre functor $\tau$ maps the categorical Frobenius form $\int_A$ to the Webster inner product on $M$. It maps the categorical substrate parameter to the smooth function $q(p)$. The polynomial ring $\mathbb{C}[z]$ serves as the universal coefficient ring. Specializing $z \mapsto q_0$ recovers the numerical predictions. Keeping $z$ formal retains the $q$-deformed algebraic structure.
