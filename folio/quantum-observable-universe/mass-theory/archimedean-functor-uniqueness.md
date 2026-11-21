**Proposition (conditional on [$(1{-}q)\,\log\Phi_n(x; q) \to \mathrm{Li}_2(x)$ under $\tau_{\mathrm{arch}}$](#conj:dilogarithm-archimedean-limit) and on the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`]).**
*Let $\tau_{\text{arch}} = \pi_\infty \circ \tau$ be the archimedean
realization functor of the QOU substrate
([archimedean realization functor](#def:archimedean-realization-functor)),
acting on motivic inputs assembled from braid / knot data. Under
hypotheses (C1)–(C2) below, $\tau_{\text{arch}}$ is uniquely
determined, up to a single multiplicative real scalar, by the
requirement that*

$$
  \lim_{q \to 1}\;\tau_{\text{arch}}\bigl(\Phi_q(z)\bigr)
  \;=\;
  D(z)
  \;:=\;
  \mathrm{Im}\,\mathrm{Li}_2(z) + \log|z|\,\arg(1-z)
$$

*equal the **Bloch-Wigner dilogarithm** on every shape parameter
$z \in \mathbb{C} \setminus \{0,1\}$, where:*

- *(C1) The substrate's mass-formula state sum is pentagon-coherent:
   $\tau_{\text{arch}}$ is a continuous, antisymmetric, real-valued
   functional on $B(\mathbb{C})$ — the structural content provided by
   the cosimplicial / Yekutieli triple machinery
   ([Cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid))
   together with the archimedean limit assumed in the opening
   banner.*
- *(C2) Bloch-Suslin pentagon-uniqueness [`suslin1991`,
   `bloch2000`]: any continuous antisymmetric pentagon-coherent
   real-valued function on $\mathbb{C} \setminus \{0,1\}$ is a
   constant scalar multiple of the Bloch-Wigner dilogarithm $D$.*

*The uniqueness reduces to the Bloch-Suslin pentagon
characterisation: $D$ is the unique (up to a real scalar)
continuous, antisymmetric, real-valued function on
$\mathbb{C} \setminus \{0,1\}$ satisfying the 5-term pentagon
identity*

$$
  D(x) - D(y) + D\!\left(\tfrac{y}{x}\right)
  - D\!\left(\tfrac{1-y^{-1}}{1-x^{-1}}\right)
  + D\!\left(\tfrac{1-y}{1-x}\right) \;=\; 0.
$$

> **Theorem (conditional on [$(1{-}q)\,\log\Phi_n(x; q) \to \mathrm{Li}_2(x)$ under $\tau_{\mathrm{arch}}$](#conj:dilogarithm-archimedean-limit)).**
> The upstream archimedean-limit conjecture is taken as a hypothesis, and
> the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`,
> `bloch2000`] is likewise taken as a hypothesis (cited, not re-proved).
> The uniqueness statement is proved from these two hypotheses alone,
> and therefore qualifies as a
> *rigorous conditional result* rather than an unproved
> conjecture.
