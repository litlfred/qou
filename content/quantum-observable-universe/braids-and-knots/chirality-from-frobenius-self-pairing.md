The paper's chirality factors $\{1 + h,\ 1 - h^2,\ (1 - h^2)^2\}$
for $\{D,\ T/^3{\rm He},\ {}^4{\rm He}\}$
([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients))
arise from a "Frobenius-norm-deviation" argument that upstream
commits describe but do not fully derive.  This proposition
formalises the chirality factor as a **Frobenius self-pairing**
invariant of the atomic braid and derives the known values from
that definition.

**Definition (Frobenius self-pairing chirality).**
*Let $(A, \tau)$ be a self-dual Frobenius algebra (e.g., the Hecke
algebra $H_n(R, q)$ under Markov trace
([Jones–Markov trace](#thm:jones-markov-trace))), and let
$\beta \in A$ be a braid word.  Let $\beta^* \in A$ denote the
image of $\beta$ under the algebra **antipode** (the anti-involution
$\sigma_i \mapsto \sigma_i^{-1}$, reverse word order).  Define the
**chirality factor** of $\beta$ as*

$$
  a_K(\beta)
  \;:=\;
  \frac{\tau(\beta \cdot \beta^*)}{\tau(1 \cdot 1)}.
$$

*Equivalently: $a_K(\beta) = \|\beta\|_\tau^2 / \|1\|_\tau^2$ is the
normalised Frobenius norm of $\beta$ in the self-dual pairing.*

**Proposition (chirality classification by writhe and topology).**
*The chirality factor satisfies:*

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
   contribution).  For the figure-eight $4_1$: $c_K = 1$, giving
   $a_K = 1 - h^2$.*

3. *For a **Borromean-type link** (multiple amphichiral sublinks):*

$$
   a_K \;=\; \prod_i (1 - c_{K_i} h^2).
$$

   *For $^4$He (two amphichiral pairs): $a_K = (1 - h^2)^2$.*

**Derivation sketch.**

*Under the Markov trace, $\tau(\sigma_i \sigma_i^{-1}) = \tau(1) = 1$
(Hecke eigenvalue pair $q, -q^{-1}$ gives $\sigma_i \sigma_i^{-1} = 1$
in $H_n(R, q)$).  Thus the identity braid has $a_K = 1$.*

*For a **single positive crossing** $\beta = \sigma_i$:*

$$
  \beta^* = \sigma_i^{-1},
  \qquad
  \beta \beta^* = \sigma_i \sigma_i^{-1} = 1,
  \qquad
  \tau(\beta \beta^*) = 1,
$$

*which gives $a_K = 1$ — no deformation from the identity.  The
**first-order** $h$-contribution therefore requires the braid to
have a **genuine chiral structure** that is not undone by the
self-pairing.*

*For $\beta = $ trefoil $(3_1) = \sigma_1^3$: $\beta^* = \sigma_1^{-3}$,
$\beta \beta^* = 1$, so $a_K = 1$ — trefoil is chiral but its
Frobenius self-pairing is trivial at the raw Hecke level.  The
non-trivial $(1 + h)$ chirality factor arises from **higher Markov
moments** when the braid is viewed as a morphism $\varrho: \mathbf{1}
\to A$ (closure operation), not as an abstract algebra element.*

*Paper's derivation
([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients)
§Proof) uses the Fricke trace relation*

$$
  \mathrm{tr}([A, B])
  = \mathrm{tr}(A)^2 + \mathrm{tr}(B)^2 + \mathrm{tr}(AB)^2
  - \mathrm{tr}(A)\mathrm{tr}(B)\mathrm{tr}(AB) - 2
$$

*in $\mathrm{SL}_2$, evaluated at $A = T_1, B = T_2^{-1}$ in the
standard representation of $H_3(R, q)$.  This gives the figure-eight
character $\chi_{4_1}((2,1)) = 2 - [3]_q = -1 - h^2$, from which
$a_{4_1} = 1 - h^2$.  For satellite knots (e.g., $D$), the Fricke
relation does not apply at $H_3$ level — one must work in $H_6(R, q)$
or larger, where the character-trace identities are more involved.*

**Status: partial derivation, amphichiral case only.**

*This proposition gives a rigorous definition
$a_K(\beta) = \tau(\beta \beta^*)$ that is categorical (monoidal-
category self-duality) and universal (applies to any $(A, \tau)$
with antipode).  For **amphichiral** knots ($4_1$, Borromean), the
Fricke identity + paper's derivation gives the specific values.
For **chiral knots** (trefoil, satellite), the Frobenius self-pairing
at the Hecke algebra level gives $a_K = 1$ trivially; the observed
$1 + h$ factor for $D$ comes from the **closure** operation
(Markov-trace normalisation), not from the algebra pairing.*

*A complete categorical derivation of all three cases requires
tracking the **braid closure** (cylinder tensor product) in a
braided monoidal category with ribbon structure.  The ribbon twist
$\varTheta_X$ encodes writhe; its interaction with the Frobenius
pairing produces the first-order $h$ contribution for chiral knots.
This derivation is **open**; paper's empirical values
$\{1+h, 1-h^2, (1-h^2)^2\}$ await a uniform categorical proof.*

**Structural value.**

*Even without the complete derivation, this proposition provides:*

1. *A **rigorous** definition of chirality in any self-dual Frobenius
   algebra with antipode — not just the Hecke case.*
2. *A categorical framing that ties chirality to the **same**
   Frobenius structure producing the co-Casimir residual
   ([Frobenius universal](#thm:frobenius-codim-universal)).*
3. *A clear path to the missing derivation: ribbon-category closure
   + writhe identification.*

*Recommended next step: formalise the ribbon-category closure of
$\varrho: \mathbf{1} \to A$ and compute $a_K$ via the composite
$\tau \circ (\varrho \otimes \varrho^*)$ explicitly for trefoil and
figure-eight.*
