*Proof.*
The proton possesses quark content $\mathfrak{u}\mathfrak{u}\mathfrak{d}$;
the neutron possesses $\mathfrak{u}\mathfrak{d}\mathfrak{d}$. At the quark
level, the crossing types evaluate as:

- $\mathfrak{u}\mathfrak{u}$: same-type $\to \sigma$ (eigenvalue $q$).
- $\mathfrak{d}\mathfrak{d}$: same-type $\to \sigma^{-1}$ (eigenvalue $q^{-1}$).
- $\mathfrak{u}\mathfrak{d}$: mixed $\to \tfrac{1}{2}(\sigma + \sigma^{-1})$.

Replacing one $\mathfrak{u}\mathfrak{u}$ crossing with one
$\mathfrak{d}\mathfrak{d}$ crossing shifts the quantum dilogarithm by
$\Delta\Phi = \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d}) - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})$.

The ground-state configurations are $\mathfrak{u}\mathfrak{u}\mathfrak{d}$
(proton) and $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ (neutron). Each $\Phi$ is
the traced volume, with each strand paired with every later strand, evaluated at
the canonical Markov parameter $z_D = q^3/(q^2+1)$ at $q_0$:
$\Phi_{\mathfrak{p}} \approx -0.614886$ and $\Phi_{\mathfrak{n}} \approx -0.896395$.
This yields $|\Delta\Phi| \approx 0.281509$.

At the quark level, a more negative $\Phi$ implies greater confinement energy
(rather than reduced binding, as occurs at the nuclear level). The
$\mathfrak{d}\mathfrak{d}$ crossing ($\sigma^{-1}$) generates more
confinement than the $\mathfrak{u}\mathfrak{u}$ crossing ($\sigma$). This
excess makes the neutron heavier.

The scale $\alpha = m_e \times 8G$ governing nuclear binding also dictates
the quark-level confinement splitting:

$$
  \Delta m \approx 3.7445 \times 0.281509 \approx 1.0541 \;\mathrm{MeV}.
$$

$\square$

**Comparison with measurement.** The CODATA value is
$m_{\mathfrak{n}} - m_{\mathfrak{p}} \approx 1.2933$ MeV, so the model value is
about $18.5\%$ below it.

> **Earlier values (historical comparison only).** The previous version of
> this proof quoted $\Phi_{\mathfrak{p}} = -0.8785$, $\Phi_{\mathfrak{n}} = -1.2261$
> and $1.302$ MeV ($+0.63\%$). Those values use the retired convention-C
> parameter $z = 4993/10000$ with the all-pairs strand pairing, which reproduces
> both of them. Pairing adjacent strands only reproduces the proton value but not
> the neutron value; under convention D that reading gives $-2.87\%$. The
> all-pairs reading is the one used by the producer
> `computations/level1-qvalues.py`, and it is the one stated above.
