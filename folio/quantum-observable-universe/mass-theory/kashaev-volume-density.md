> **Superseded.** The scalar substrate density $\rho_q = 1/\hbar_q^2$ used below is the structurally-wrong leading-order ansatz; the operator-valued form supersedes it ([`mass-endomorphism-tower`](mass-endomorphism-tower.md)).

The topological mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ is exactly a volume $\times$ density product.

### Substrate density $\rho_q$

*Define the **substrate density** to be the inverse squared quantum Planck constant:*

$$
  \rho_q
  \;:=\;
  \frac{1}{\hbar_q^{2}}
  \;=\;
  \frac{q^{2}}{(q-1)^{2}}.
$$

Physically, $\rho_q$ measures the categorical drag cost of transporting a closed vortex through the Frobenius-Hopf structure. Mass is topological volume weighted by substrate drag.

### The Kashaev bridge

The [Kashaev volume conjecture](#conj:kashaev-volume-conjecture) bridges the archimedean continuous volume and the algebraic discrete Markov trace: it identifies the continuous hyperbolic volume $\mathrm{Vol}(K)$ with the Kashaev limit $2\pi \lim_{N \to \infty} \log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert / N$, an asymptotic limit of colored Markov traces evaluated within the Hecke algebra.

### Inverting the ontology

The QOU framework reverses the classical priority: the discrete trace is fundamental, while the continuous volume is emergent. The colored Jones polynomials are finite algebraic evaluations of Markov traces. The hyperbolic volume describes the asymptotic scaling of these exact categorical evaluations. The macroscopic continuum shadow emerges from the accumulated algebraic drag of discrete crossing resolutions.

### Consequences for the mass formula

Substituting the Kashaev identity yields a fully algebraic derived mass:

$$
  \mathfrak{m}(K)
  \;\approx\;
  \rho_{q}\;\cdot\;
  \Bigl[
    2\pi\,\lim_{N \to \infty}
    \frac{\log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert}{N}
  \Bigr].
$$

No continuous inputs remain. Every constituent is a discrete Hecke trace evaluated at roots of unity. The finite categorical evaluation operates precisely at the non-asymptotic substrate value $q_0 \approx 1.11$, avoiding the $N \to \infty$ continuum idealization entirely.
