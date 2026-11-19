Let $\mathfrak{H}$ be a knot composite with braid word $\beta$. Let $n_+(\beta)$ and $n_-(\beta)$ denote the number of positive and negative crossings in $\beta$. Define the **Coulomb charge** of $\mathfrak{H}$ as the halved writhe:

$$
  Q(\mathfrak{H}) =  \tfrac{1}{2}\bigl(n_+(\beta) - n_-(\beta)\bigr).
$$

By [the channel decomposition](#prop:crossing-energy-decomposition), the crossing energy of [the crossing-energy definition](#def:crossing-energy), $\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$, splits as

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  =
  \underbrace{\tfrac{1}{2}(n_+ - n_-)(q + q^{-1})}_{\text{symmetric (strong)}} +
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q - q^{-1})}_{\text{antisymmetric (Coulomb)}}.
$$

The multiplicities are not interchangeable. The symmetric $\cosh$ weight carries the crossing sign, so reversing a crossing negates it and the symmetric total is governed by the **writhe** $n_+ - n_-$. The antisymmetric $\sinh$ weight is blind to the crossing sign, contributing $+\sinh\lambda$ for a negative crossing exactly as for a positive one, so the antisymmetric total is governed by the **crossing count** $n_+ + n_-$.

**Consequences, and what $Q$ is not.** $Q$ is the coefficient of the *symmetric* channel. Under the channel identification of [the crossing-energy definition](#def:crossing-energy) — symmetric with strong binding, antisymmetric with the electromagnetic correction — the halved writhe therefore governs the strong term, and the electromagnetic coefficient is $\tfrac{1}{2}(n_+ + n_-)$, which is non-negative for every composite. Two things follow that constrain any use of $Q$ as an electric charge:

- No composite carries a negative antisymmetric coefficient, so this decomposition supplies no attractive Coulomb channel and no negative charge.
- The vanishing locus $n_+ = n_-$ annihilates the *symmetric* term, not the antisymmetric one; the antisymmetric-to-symmetric ratio diverges there rather than vanishing.

The identification of $Q$ with an electromagnetic charge is therefore not established by this decomposition. The name is retained for continuity with the blocks that cite this label; the identification itself is [an open problem](#conj:sm-hypercharge-invariant), and any candidate must supply the second gauge-invariant datum that the writhe alone does not.

**Ratio.** For a positive braid closure, $n_- = 0$ with $n_+ \geq 1$, the antisymmetric-to-symmetric ratio is $\tanh(\ln q) \approx 0.104$ at $q = q_0$, independent of $n_+$. For mixed crossing signs with $n_+ \neq n_-$ it acquires the multiplicity factor $\tfrac{n_+ + n_-}{n_+ - n_-}$ and is not a constant of the framework.
