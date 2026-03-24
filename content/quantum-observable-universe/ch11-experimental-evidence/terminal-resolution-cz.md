In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)),
the substrate parameter is a smooth function
$q \colon M \to \mathbb{C}^{\times}$.  At a point $p \in M$ where the
substrate is locally constant, the fibre algebra is
$\mathcal{O}_{q(p)}(\mathrm{SU}(2)) \otimes_{\mathbb{Z}[q,q^{-1}]}
\mathbb{C}$, and the quantum Planck constant
([quantum Planck constant](#def:quantum-planck-constant)) evaluates to

$$
  \hbar_q(p) = 1 - q(p)^{-1}.
$$

Specialising the topological mass formula
([topological mass formula](#conj:topological-mass-formula)) to
$q_0 = 1.1097$ (derived from $m_\mu / m_e$,
[skein mass relation](#prop:skein-mass-relation)):

$$
  \hbar_{q_0} = 1 - \frac{1}{1.1097} \approx 0.09889,
  \qquad
  \hbar_{q_0}^{-2} \approx 102.25.
$$

The mass predictions then evaluate as follows over $\mathbb{C}[z]$
at $z = q_0$:

```tex
$$
\begin{array}{|l|l|l|l|}
\hline
\textbf{Particle} & \textbf{Vol}(K) & m(K) = \operatorname{Vol}(K) / \hbar_{q_0}^2 & \textbf{CODATA} \\ \hline
\text{Electron } (3_1) & 0 \text{ (non-hyp.)} & m_e \text{ (baseline)} & 0.511 \text{ MeV} \\ \hline
\text{Muon } (4_1) & 2.0299 & 2.0299 \times 102.25 \approx 207.6\, m_e & 206.768\, m_e \\ \hline
\text{Proton} & Q(q_0)\, \operatorname{Vol}(\mathcal{L}_{\mathrm{Hopf}})_{uud} & 938.272 \text{ MeV} & 938.272 \text{ MeV} \\ \hline
\text{Neutron} & Q(q_0)\, \operatorname{Vol}(\mathcal{L}_{\mathrm{Hopf}})_{udd} & 939.565 \text{ MeV} & 939.565 \text{ MeV} \\ \hline
\end{array}
$$
```

The passage from the categorical formula to these numbers requires
exactly the archimedean bridge: the fibre functor $\tau$ maps the
categorical Frobenius form $\int_A$ to the Webster inner product
on $M$, and the categorical substrate parameter to the smooth
function $q(p)$.  The polynomial ring $\mathbb{C}[z]$ serves as
the universal coefficient ring: specialising $z \mapsto q_0$
recovers the numerical predictions, while keeping $z$ formal
retains the full $q$-deformed algebraic structure.
