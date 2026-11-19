Let $\mathcal{N}(Z,N)$ be the normal form of a nucleus with $Z$ protons and $N$ neutrons, and let $\mathfrak{S}_q(\mathcal{N})$ be its categorical action ([categorical action](#def:categorical-action)). For a $\beta^-$ transition $\mathcal{N}(Z,N) \to \mathcal{N}(Z{+}1,N{-}1) + e^- + \bar{\nu}_e$, the :defterm[$\mathcal{Q}_q$-value]{#q-value} is the **categorical action difference** between the parent and the products:

$$
  \mathcal{Q}_q
  = 
  \mathfrak{S}_q\bigl(\mathcal{N}(Z,N)\bigr) -
  \mathfrak{S}_q\bigl(\mathcal{N}(Z{+}1,N{-}1)\bigr) -
  \mathfrak{S}_q(e) -
  \mathfrak{S}_q(\bar{\nu}_e),
$$

with $\mathfrak{S}_q(\bar{\nu}_e) = 0$ since the antineutrino is the unknot. This is the primary definition. It does not assume classical energy conservation, which is the $q = 1$ limit; the relation between $\mathcal{Q}_q$ and the kinetic energies of the products is the $q$-anomaly $\delta_q$ treated in [the $Q$-value transition properties](#rem:Q-value-transition-properties). When $q$ is fixed, $Q$ denotes $\mathcal{Q}_q$.

**Mass-difference form.** In the archimedean realisation the action of a nucleus is its mass, and the same transition is evaluated as the difference of neutral atomic masses,

$$
  Q = M(Z, N) - M(Z{+}1, N{-}1),
  \qquad
  M(Z, N) = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e - B(Z, N),
$$

where $B(Z,N)$ is the binding energy at Hecke level $k$ under the Bethe–Weizsäcker emergence conjecture ([Bethe–Weizsäcker emergence conjecture](#conj:q-integer-mass-formula)). Expanding the atomic masses gives $Q = m_{\mathfrak{n}} - m_{\mathfrak{p}} - m_e - \bigl(B(Z,N) - B(Z{+}1,N{-}1)\bigr)$. This is the form in which $Q$ is compared with measured values; it is a realisation of the action difference, not a second definition, and its numerical content is conditional on the conjecture that supplies $B$.
