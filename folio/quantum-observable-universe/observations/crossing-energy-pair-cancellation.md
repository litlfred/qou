**Proposition.**
*Let $\mathfrak{H}$ be a knot composite carrying $p$ positive and $m$ negative crossings, and let $\mathfrak{H}^{\sigma}$ be its mirror. Then*

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) +
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma})
  = 2E_{\mathrm{asym}}(\mathfrak{H})
  = 2(p + m)\sinh\lambda,
$$

*where $\lambda = \ln q$. The symmetric channel cancels identically and the surviving energy is purely antisymmetric.*

**Proof.**
By the [decomposition](#prop:crossing-energy-decomposition), $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = (p - m)\cosh\lambda + (p + m)\sinh\lambda$. The mirror exchanges $p$ and $m$, so $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma}) = (m - p)\cosh\lambda + (m + p)\sinh\lambda$. Adding, the $\cosh$ terms cancel and the $\sinh$ terms double. $\square$

**Structural content.**
The cancellation is a consequence of the multiplicity mismatch between the two channels. The $\cosh$ weight of a crossing carries the crossing sign and therefore enters the total with multiplicity $p - m$; the $\sinh$ weight is blind to the crossing sign and enters with multiplicity $p + m$. Only a sign-blind channel can survive mirror pairing, and the antisymmetric channel is the sign-blind one.

The residue is strictly positive for $q > 1$ and any composite with at least one crossing, so a composite and its mirror never annihilate to zero crossing energy. The [pair creation](#rem:pair-creation-energy) remark reads this residue as the Coulomb energy that separates a created particle-antiparticle pair.
