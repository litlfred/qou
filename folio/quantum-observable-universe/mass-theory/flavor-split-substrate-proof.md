Step 5 proves the identity: dividing (4) by 3 gives it, and it holds for every nonzero $q$. Steps 1 to 4 and 6 relate its two sides to $(m_n - m_p)/M_N$ under the pair-Skein formula and the ansatz of Step 2, and Step 3 records that the ansatz does not reach them. Those steps are not needed for the identity.

*Step 1 (Pair-Skein difference, exact).*

Apply [Pair Skein mass and crossing-by-crossing recursion](pair-skein-mass-formula.md) to the Borromean baryon braids of the proton ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) and neutron ($\mathfrak{u}\mathfrak{d}\mathfrak{d}$). This gives the exact relation:

$$
  m_n - m_p
  \;=\;
  \kappa \cdot (\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}),
  \qquad
  \kappa = \mathrm{tr}_M(\sigma + \sigma^{-1}) = \frac{q^4 + 1}{q\,(q^2 + 1)},
$$

with the Markov trace at the canonical parameter $z = q^3/(q^2+1)$. Dividing by $\mu_{\text{avg}} = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2$:

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;=\;
  \kappa \cdot
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{\mu_{\text{avg}}}. \tag{1}
$$

*Step 2 (Aether ansatz for the per-quark split).*

The aether prescription for $(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})/\mu_{\text{avg}}$ is:

$$
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{\mu_{\text{avg}}}
  \;\approx\;
  h_q^2 \cdot \frac{\hbar_q}{\sqrt{q}},
  \qquad
  h_q = q - q^{-1},
  \quad
  \hbar_q = \frac{q - 1}{q}. \tag{2}
$$

This is the minimal aether-atom combination satisfying three conditions:
(a) Bar-involution antisymmetry under $q \mapsto q^{-1}$ (consistent with the antisymmetry of the splitting under flavor exchange $\mathfrak{u} \leftrightarrow \mathfrak{d}$).
(b) Leading order $(q-1)^3$ at the classical limit.
(c) Numerical agreement to $-0.13\%$ at the proton-anchored $q = q_0$.

**Scope of Step 2.** Equation (2) is a phenomenological ansatz rather than a derived identity: Condition (c) chooses the form because it agrees with experiment, which is selection against the target. Conditions (a) and (b) do not single it out:

- (b) holds: the right-hand side is $4(q-1)^3 + O((q-1)^4)$.
- (a) does not hold as stated. Writing $f(q) = h_q^2\,\hbar_q/\sqrt{q}$, one finds $f(q^{-1}) = -q^2 f(q)$, so $f$ is antisymmetric under $q \mapsto q^{-1}$ only up to the factor $q^2$ (checked symbolically).

Everything downstream of (2) therefore inherits a fitted input, and no derivation is on record. One class of derived objects is excluded. Suppose the nucleon masses are additive over strands, $m_{\mathfrak{p}} = 2\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}}$ and $m_{\mathfrak{n}} = \mu_{\mathfrak{u}} + 2\mu_{\mathfrak{d}}$, and that $m_{\mathfrak{p}}/m_{\mathfrak{n}}$ is a nonzero integer power of $q$, as for the pivot ratio $q^{\pm 2}$ that the restricted quantum trace gives on the $U_q(\mathfrak{sl}_2)$ commutant. Then, with $t = \sqrt{q}$, the per-quark split is $c\,(t^m - 1)/(t^m + 1)$ for a nonzero rational $c$ and an integer $m \ge 1$. This vanishes to first order at $q = 1$, while the right-hand side of (2) vanishes to third order, so the two never agree, and the ansatz also fails bar-parity symmetry. The exclusion says nothing about non-additive strand rules or about objects that break $U_q(\mathfrak{sl}_2)$ symmetry.

*Step 3 (The ansatz does not reach the closed form).*

Substituting (2) into (1) gives

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;=\;
  \kappa \cdot h_q^2 \cdot \frac{\hbar_q}{\sqrt{q}} .
$$

This is not the closed form $\hbar_q^2 \cdot h_q \cdot [2]_q$ of (3) below. At $q_0$ the ratio of the two is $1.0122$. The ansatz (2) was chosen under the retired pair-Skein denominator $q^{1/2} + q^{-1/2}$, for which $h_q/(q^{1/2} + q^{-1/2}) = \hbar_q\sqrt{q}$ made the product collapse to (3). With the derived pair-Skein formula that collapse does not happen, so this sketch no longer supports the conjecture. The conjecture rests on the identity of Step 5 and on [the CODATA comparison](#rem:flavor-split-aether-codata-comparison).

*Step 4 (The closed form, as conjectured).*

The conjectured per-quark form of the nucleon split is

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;=\;
  \hbar_q^2 \cdot h_q \cdot [2]_q. \tag{3}
$$

*Step 5 (Closed-form polynomial identity).*

Substituting $\hbar_q = (q-1)/q$, $h_q = (q^2-1)/q$, and $[2]_q = (q^2+1)/q$ into (3):

$$
  \hbar_q^2 \cdot h_q \cdot [2]_q
  \;=\;
  \frac{(q-1)^2}{q^2} \cdot \frac{q^2 - 1}{q} \cdot \frac{q^2 + 1}{q}
  \;=\;
  \frac{(q-1)^2 \, (q^2 - 1)(q^2 + 1)}{q^4}
  \;=\;
  \frac{(q-1)^2 \, (q^4 - 1)}{q^4}
  \;=\;
  (q-1)^2 \cdot (1 - q^{-4}). \tag{4}
$$

*Step 6 (Conversion to per-nucleon form).*

The per-quark mass averages to the per-nucleon mass via $M_N = 3 \mu_{\text{avg}}$ (one quark mass per strand of the baryon braid, summed over three strands). Therefore:

$$
  \frac{m_n - m_p}{M_N}
  \;=\;
  \frac{m_n - m_p}{3 \mu_{\text{avg}}}
  \;=\;
  \frac{\hbar_q^2 \cdot h_q \cdot [2]_q}{3}
  \;=\;
  \frac{(q-1)^2 \, (1 - q^{-4})}{3}. \tag{5}
$$
