**Proposition (chirality classification by writhe and topology).**
*Let $a_K(\beta) = \tau(\beta\beta^*)/\tau(1)$ be the Frobenius
self-pairing chirality factor
([def:frobenius-self-pairing-chirality](#def:frobenius-self-pairing-chirality))
of the atomic braid $\beta$. The chirality factor satisfies:*

1. *For a **chiral knot** $K$ with writhe $w(K) \neq 0$:*

$$
   a_K \;=\; 1 + w(K) \cdot h \;+\; O(h^2),
$$

*to leading order in the Hecke deformation $h = q - q^{-1}$.*

2. *For an **amphichiral knot** $K$ (i.e., $K = \overline{K}$ under
 mirror):*

$$
   a_K \;=\; 1 - c_K \cdot h^2 \;+\; O(h^4),
$$

*where $c_K$ is a topological invariant (writhe-squared
contribution). For the figure-eight $4_1$: $c_K = 1$, giving
$a_K = 1 - h^2$.*

3. *For a **Borromean-type link** (multiple amphichiral sublinks):*

$$
   a_K \;=\; \prod_i (1 - c_{K_i} h^2).
$$

*For $^4$He (two amphichiral pairs): $a_K = (1 - h^2)^2$.*

**Derivation sketch.**

*Under the Markov trace, $\tau(\sigma_i \sigma_i^{-1}) = \tau(1) = 1$
(Hecke eigenvalue pair $q, -q^{-1}$ gives $\sigma_i \sigma_i^{-1} = 1$
in $H_n(R, q)$). Thus the identity braid has $a_K = 1$.*

*For a **single positive crossing** $\beta = \sigma_i$:*

$$
  \beta^* = \sigma_i^{-1},
  \qquad
  \beta \beta^* = \sigma_i \sigma_i^{-1} = 1,
  \qquad
  \tau(\beta \beta^*) = 1,
$$

*which gives $a_K = 1$ — no deformation from the identity. The
**first-order** $h$-contribution therefore requires the braid to
have a **genuine chiral structure** that is not undone by the
self-pairing.*

*For $\beta = $ trefoil $(3_1) = \sigma_1^3$: $\beta^* = \sigma_1^{-3}$,
$\beta \beta^* = 1$, so $a_K = 1$ — trefoil is chiral but its
Frobenius self-pairing is trivial at the raw Hecke level. The
non-trivial $(1 + h)$ chirality factor arises from **higher Markov
moments** when the braid is viewed as a morphism $\varrho: \mathbf{1}
\to A$ (closure operation), not as an abstract algebra element.*

*Paper's derivation
(figure-eight BW coefficients
§Proof) uses the Fricke trace relation*

$$
  \mathrm{tr}([A, B])
  = \mathrm{tr}(A)^2 + \mathrm{tr}(B)^2 + \mathrm{tr}(AB)^2
  - \mathrm{tr}(A)\mathrm{tr}(B)\mathrm{tr}(AB) - 2
$$

*in $\mathrm{SL}_2$, evaluated at $A = T_1, B = T_2^{-1}$ in the
standard representation of $H_3(R, q)$. This gives the figure-eight
character $\chi_{4_1}((2,1)) = 2 - [3]_q = -1 - h^2$, from which
$a_{4_1} = 1 - h^2$. For satellite knots (e.g., $D$), the Fricke
relation does not apply at $H_3$ level — one must work in $H_6(R, q)$
or larger, where the character-trace identities are more involved.*
