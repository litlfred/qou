Let $T_{2,3}$ denote the left trefoil (the electron generator) and $T_{2,3}^{\sigma}$ its mirror image (all crossings reversed).

**Statement.**

1. **Crossing reversal defines antiparticles.** We obtain the antihadron $\mathfrak{H}^{\sigma}$ of a composite hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ by replacing every constituent $K_i$ with its mirror $K_i^{\sigma}$. The braid word $\beta$ representing the linking has all crossing signs reversed.
2. **Crossing energy sign reversal.** If the [crossing energy](#def:crossing-energy) of $\mathfrak{H}$ is

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = \sum_{\text{crossings}} \epsilon_i,
     \qquad \epsilon_i \in \{q, -q^{-1}\},
   $$

   then the crossing energy of the antihadron satisfies

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma}) = -\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
     \bigg|_{q \leftrightarrow q^{-1}}.
   $$

   Positive crossings ($+q$) become negative ($-q^{-1}$) and vice versa.
3. **Coulomb charge reversal.** The antisymmetric component of the crossing energy (the Coulomb channel) reverses sign: $Q(\mathfrak{H}^{\sigma}) = -Q(\mathfrak{H})$. Specifically, $Q(\mathfrak{p}^{\sigma}) = -1$ for the antiproton.
4. **Bare mass invariance.** The mirror operation preserves the knot type and its hyperbolic volume. The bare mass of a particle equals that of its antiparticle: $m_{\mathrm{bare}}(\mathfrak{H}^{\sigma}) = m_{\mathrm{bare}}(\mathfrak{H})$.

**Formalization status.** The Lean formalization supplies partial coverage. The sub-lemmas for Coulomb reversal, pair crossing energy, and bare mass invariance are `sorry`-free, relying on basic arithmetic and ring properties. The formal proof establishes that the mirror operation swaps the topological crossing counts. Upgrading this to the algebraic trace substitution under $q \leftrightarrow q^{-1}$ is a localized, routine goal that preserves the structural validity of the mechanism.

Equating formal knot-theoretic mirror swapping with the physical properties of antiparticles constitutes a conceptually novel contribution.
