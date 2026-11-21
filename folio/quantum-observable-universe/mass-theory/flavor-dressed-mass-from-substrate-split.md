**Proposition (conditional on [the substrate flavor split conjecture](#conj:flavor-split-substrate-mass)).** In Lean the conjecture is the class `FlavorSplitSubstrateMass`, which has no instance, and the proposition is derived from it.

*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor dressing functor. Let $m_{\mathfrak{p}}, m_{\mathfrak{n}}$ be the nucleon masses, $M_N = (m_{\mathfrak{p}} + m_{\mathfrak{n}})/2$, and $q > 1$ the substrate parameter. The down-up dressed mass splitting is exactly determined by the substrate flavor formula:*

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

**What is assumed and what is derived.** Two inputs are assumed. The first is [the substrate flavor split conjecture](#conj:flavor-split-substrate-mass), read at leading order as the equality $m_{\mathfrak{n}} - m_{\mathfrak{p}} = M_N (q-1)^2(1-q^{-4})/3$. The second is the nucleon form of the [pair Skein mass formula](#lem:pair-skein-mass-formula), $(m_{\mathfrak{n}} - m_{\mathfrak{p}})(q^{1/2} + q^{-1/2}) = (q + q^{-1})(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})$. The $O\!\left((\Delta m / M_N)^2\right)$ correction is absorbed in these inputs. From them the leading-order splitting follows by dividing by $q + q^{-1} > 0$ and substituting. The Lean theorem `dressed_mass_from_substrate_split` takes $(\mu, m_{\mathfrak{p}}, m_{\mathfrak{n}}, q)$, an instance of the conjecture's class and the Skein relation as a hypothesis, and derives this step. Neither input is proved. The leading-order equality is the strongest reading of the conjecture, and [the CODATA comparison](#rem:flavor-split-substrate-codata-comparison) records that it is not met exactly at physical values, so the proposition is a statement about the model under that reading.
