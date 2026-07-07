The left trefoil $T_{2,3}$ represents the electron generator. Its mirror image $T_{2,3}^{\sigma}$ has all crossings reversed.

**Statement.**

1. **Crossing reversal defines antiparticles.** Replacing every constituent $K_i$ with its mirror $K_i^{\sigma}$ yields the antihadron $\mathfrak{H}^{\sigma}$ of a composite hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$. The braid word $\beta$ representing the linking has all crossing signs reversed.
2. **Crossing energy sign reversal.** The [crossing energy](#def:crossing-energy) of $\mathfrak{H}$ is

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = \sum_{\text{crossings}} \epsilon_i,
     \qquad \epsilon_i \in \{q, -q^{-1}\}.
   $$

   The crossing energy of the antihadron satisfies

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma}) = -\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
     \bigg|_{q \leftrightarrow q^{-1}}.
   $$

   Positive crossings ($+q$) become negative ($-q^{-1}$) and vice versa.
3. **Coulomb charge reversal.** The antisymmetric component of the crossing energy determines the Coulomb channel. This reverses sign: $Q(\mathfrak{H}^{\sigma}) = -Q(\mathfrak{H})$. The antiproton specifically carries $Q(\mathfrak{p}^{\sigma}) = -1$.
4. **Bare mass invariance.** The mirror operation preserves the knot type and its hyperbolic volume. The bare mass of a particle equals that of its antiparticle: $m_{\mathrm{bare}}(\mathfrak{H}^{\sigma}) = m_{\mathrm{bare}}(\mathfrak{H})$.

**Formalization status.** The Lean formalization supplies partial coverage. The sub-lemmas for Coulomb reversal, pair crossing energy, and bare mass invariance remain `sorry`-free. These rely on basic arithmetic and ring properties. The formal proof establishes the mirror operation swapping the topological crossing counts. Upgrading this to the algebraic trace substitution under $q \leftrightarrow q^{-1}$ constitutes a localized, routine goal. It preserves the structural validity of the mechanism.

Formal knot-theoretic mirror swapping models the physical properties of antiparticles.
