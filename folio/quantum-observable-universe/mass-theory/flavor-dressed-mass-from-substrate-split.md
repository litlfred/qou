*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor dressing functor. Let $M_N$ be the average nucleon mass, and $q = q_0$ the substrate parameter. The down-up dressed mass splitting is exactly determined by the substrate flavor formula:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;=\;
  M_N \cdot \frac{(q - 1)^2 (1 - q^{-4})}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left(\bigl(\Delta m / M_N\bigr)^2\right).
$$

*Dropping the $O$ correction yields the leading-order substrate-pure form:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;\approx\;
  \frac{M_N}{3} \cdot
  \hbar_q^2 \cdot h_q \cdot
  \frac{1}{z_{\mathrm{mkv}}}.
$$

The CODATA neutron-proton mass difference is no longer an input. The functor extracts the splitting purely from $q_0$ and the scale $M_N$. The individual masses $\mu_{\mathfrak{u}}$ and $\mu_{\mathfrak{d}}$ are then pinned by the baryon-content sum-rule.

Here $z_{\mathrm{mkv}} = \sqrt q/(q+1)$ is the excised convention-C Markov weight, inherited from the [pair-Skein formula](#lem:pair-skein-mass-formula). The statement is a convention-C result until that formula is re-derived under the canonical weight $z = q^3/(q^2+1)$.

**Conditional on two upstream results, neither yet formalised.** The formal
backing is a named accessor for a hypothesis carrying the substrate side
([Substrate-pure derivation of the $u$--$d$ flavor split](#prop:flavor-split-substrate)) together with
the Skein side ([Pair Skein mass and crossing-by-crossing recursion](#lem:pair-skein-mass-formula)),
which is also where the $O\!\left((\Delta m / M_N)^2\right)$ correction is
absorbed. The equality above is asserted for a triple $(\mu, M_N, q)$ carrying
that hypothesis, not for an arbitrary one.
