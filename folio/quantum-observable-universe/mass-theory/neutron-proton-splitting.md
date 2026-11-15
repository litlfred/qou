*The model neutron-proton mass splitting derives from the quantum dilogarithm volumes:*

$$
  \Delta m := \alpha \cdot \lvert \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d}) -
    \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d}) \rvert
  \approx 1.302 \; \mathrm{MeV}
$$

*where $\Phi$ evaluates the respective quark ordering and $\alpha = m_e \times 8G$ sets the binding scale.*

Replacing one positive $\mathfrak{u}\mathfrak{u}$ crossing with a negative $\mathfrak{d}\mathfrak{d}$ crossing causes the splitting. The $\mathfrak{d}\mathfrak{d}$ crossing carries more confinement energy. This makes the model neutron heavier. With the corpus values $\alpha \approx 3.7449$, $\Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d}) \approx -0.8785$ and $\Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d}) \approx -1.2261$, the model value is $3.7449 \times 0.3476 = 1.30172724$ MeV.

**Comparison with measurement.** The CODATA 2022 splitting is $m_{\mathfrak{n}} - m_{\mathfrak{p}} \approx 939.56542194 - 938.27208816 = 1.29333378$ MeV. The model value exceeds it by about $0.65\%$. This comparison is the empirical claim of the block; the Lean formalization states only the model value. The corpus values of $\Phi$ are computed with the Markov parameter $z = 4993/10000$, the rounded convention-C value $\sqrt{q}/(q+1)$, which is no longer the canonical convention. With the canonical convention-D parameter $z = q^3/(q^2+1)$ the same construction gives $|\Delta\Phi| \approx 0.2815$ and a model splitting of about $1.054$ MeV, $18.5\%$ below the measured value. The re-derivation under convention D is open.
