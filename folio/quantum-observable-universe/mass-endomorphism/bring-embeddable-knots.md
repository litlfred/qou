**Remark (Bring-embeddable knot table).**

The QOU aether selects the knots whose Seifert genus is bounded by Bring's surface genus ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete), [knot exhaustiveness](#rem:knot-exhaustiveness)):

$$
  \mathrm{Knots}_{\mathrm{Bring}}
  \;:=\;
  \bigl\{ K \,:\, g(K) \;\leq\; 4 \bigr\}.
$$

By the [generation completeness theorem](#prop:knot-eigenbasis-complete), a finite list of torus-knot generators combined with skein crossing changes generates this class. The recursive atom-knot atlas lists the canonical low-genus representatives.

### Genus stratification and generators

The full enumeration of Bring-embeddable knots by genus appears in [Table: Bring-embeddable knot table](#tbl:bring-embeddable-knots-table-data). Every Bring-embeddable knot derives from seven torus-knot generators:

$$
  \{T(2, 3),\; T(2, 5),\; T(2, 7),\; T(2, 9),\; T(3, 4),\; T(3, 5),\; T(5, 2)\}
$$

via skein crossing changes. These generators satisfy $g(T(p, q)) = (p-1)(q-1)/2 \in [1, 4]$, and appropriate skein moves preserve the $g \leq 4$ bound.

### Falsifiability and depth-2 witnesses

For each Bring-embeddable knot $K$ with dominant cell $\lambda_K$ in $H_n(q)$ and shape parameter $z_K \in \overline{\mathbb{Q}}^\times$:

$$
  [\mathrm{Vol}(K)] \;=\; \tau_{\mathrm{arch}}\bigl( e_{\lambda_K}
  \cdot \mathrm{Li}_2^q(z_K) \bigr) \;\in\; \mathcal{P}_2 / \mathcal{P}_1.
$$

If [the Grothendieck–Brieskorn depth–period correspondence](#conj:gb-depth-period-correspondence) holds, every entry in the principled atlas must satisfy:

$$
  \mathrm{Vol}(K) \;\stackrel{!}{=}\; \tau_{\mathrm{arch}}\bigl(
  e_{\lambda_K} \cdot \mathrm{Li}_2^q(z_K) \bigr).
$$

A single counter-example falsifies the depth correspondence. The figure-$8$ row is verified ([Bring figure-eight depth-2 witness](#conj:bring-figure-eight-depth-2-witness)), while confirming nodes like $5_2$, $6_2$, and $6_3$ remains necessary. This verification entails identifying $\lambda_K$ and $z_K$, and computing the projection $e_{\lambda_K}$ as the explicit Goncharov-period witness ([explicit central idempotent](#prop:explicit-central-idempotent)).
