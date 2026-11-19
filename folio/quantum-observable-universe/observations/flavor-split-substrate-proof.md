**Proof.**

*Step 1 (Pair-Skein difference, exact).*

Applying the [pair-Skein mass formula](pair-skein-mass-formula.md) to the Borromean baryon braids of the proton ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) and neutron ($\mathfrak{u}\mathfrak{d}\mathfrak{d}$) gives the exact relation:

$$
  m_n - m_p
  \;=\;
  \frac{q + q^{-1}}{q^{1/2} + q^{-1/2}} (\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})
  \;=\;
  [2]_q \cdot z_{\text{mkv}} \cdot (\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}),
$$

where $z_{\text{mkv}} = (q^{1/2} + q^{-1/2})^{-1} = \sqrt q/(q+1)$ is the excised convention-C Markov weight, inherited from the pair-Skein formula. Steps 1 and 3 therefore hold in the convention-C frame only. At the canonical weight $z = q^3/(q^2+1)$ the product $[2]_q z$ would be exactly $q^2$, but that substitution is not valid until the pair-Skein formula is re-derived under the canonical weight. Dividing by $\mu_{\text{avg}} = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2$:

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;=\;
  [2]_q \cdot z_{\text{mkv}} \cdot
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{\mu_{\text{avg}}}. \tag{1}
$$

*Step 2 (Substrate ansatz for the per-quark split).*

The substrate prescription for $(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})/\mu_{\text{avg}}$ is:

$$
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{\mu_{\text{avg}}}
  \;\approx\;
  h_q^2 \cdot \frac{\hbar_q}{\sqrt{q}},
  \qquad
  h_q = q - q^{-1},
  \quad
  \hbar_q = \frac{q - 1}{q}. \tag{2}
$$

This is the minimal substrate-atom combination satisfying three conditions:
(a) Bar-involution antisymmetry under $q \mapsto q^{-1}$ (consistent with the antisymmetry of the splitting under flavor exchange $\mathfrak{u} \leftrightarrow \mathfrak{d}$).
(b) Leading order $(q-1)^3$ at the classical limit.
(c) Numerical agreement to $-0.67\%$ at $q = q_0$.

**Scope of Step 2.** Equation (2) is a phenomenological ansatz rather than a derived identity: Condition (c) chooses the form because it agrees with experiment, which is selection against the target. Conditions (a) and (b) do not single it out:

- (b) holds: the right-hand side is $4(q-1)^3 + O((q-1)^4)$.
- (a) does not hold as stated. Writing $f(q) = h_q^2\,\hbar_q/\sqrt{q}$, one finds $f(q^{-1}) = -q^2 f(q)$, so $f$ is antisymmetric under $q \mapsto q^{-1}$ only up to the factor $q^2$ (checked symbolically).

Everything downstream of (2) therefore inherits a fitted input. The derivation that would replace it is open.

*Step 3 (Algebraic identity tying the equivalent forms).*

$$
  h_q \cdot z_{\text{mkv}}
  \;=\;
  \frac{q - q^{-1}}{q^{1/2} + q^{-1/2}}
  \;=\;
  \frac{(q^{1/2} - q^{-1/2})(q^{1/2} + q^{-1/2})}{q^{1/2} + q^{-1/2}}
  \;=\;
  q^{1/2} - q^{-1/2}
  \;=\;
  z_0,
$$

and $\hbar_q \cdot \sqrt{q} = (q - 1)/\sqrt{q} = q^{1/2} - q^{-1/2} = z_0$. So $h_q \cdot z_{\text{mkv}} = z_0 = \hbar_q \cdot \sqrt{q}$. The first equality holds for the convention-C weight only: at the canonical weight $h_q z \approx 0.1281$ at $q_0$, against $q_0^{1/2} - q_0^{-1/2} \approx 0.1044$. This gives the chain of equivalent forms:

$$
  h_q^2 \cdot \frac{\hbar_q}{\sqrt{q}}
  \;=\;
  h_q^2 \cdot \frac{z_0}{q}
  \;=\;
  h_q^3 \cdot \frac{z_{\text{mkv}}}{q}
  \;=\;
  \frac{h_q^2 \cdot (q-1)}{q^{3/2}}.
$$

*Step 4 (Factored Hecke-atom form for the nucleon split).*

Substituting (2) into (1):

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;=\;
  [2]_q \cdot z_{\text{mkv}} \cdot h_q^2 \cdot \frac{\hbar_q}{\sqrt{q}}.
$$

Using $z_{\text{mkv}} = z_0 / h_q = (\hbar_q \cdot \sqrt{q})/h_q$ (from Step 3), this collapses to:

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;=\;
  [2]_q \cdot h_q^2 \cdot \hbar_q \cdot \frac{\hbar_q \sqrt{q}}{h_q \sqrt{q}}
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

*Step 7 (Empirical evaluation).*

At $q = q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps):

$$
  (q_0 - 1)^2 \cdot (1 - q_0^{-4}) / 3
  \;\approx\;
  (0.10998)^2 \cdot (1 - 0.6585) / 3
  \;\approx\;
  0.01210 \cdot 0.3415 / 3
  \;\approx\;
  1.376 \times 10^{-3},
$$

This matches the CODATA value $1.293 / 938.92 \approx 1.377 \times 10^{-3}$ to $-0.10\%$. $\square$
