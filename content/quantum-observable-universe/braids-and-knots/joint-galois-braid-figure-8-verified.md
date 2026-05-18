**Proposition (joint Galois × braid action commutes on the figure-8
bi-filtration cell — verified directly).**

The joint motivic-Galois × braid-group action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
predicts commutativity on each $\mathcal{H}_q^{(n, K)}$ stratum.
*This proposition verifies the prediction on the figure-8 row
$\mathcal{H}_q^{(2, 4_1)}$ by direct computation.*

### Setup

The figure-8 bi-filtration cell is

$$
  \mathcal{H}_q^{(2, 4_1)}
  \;\subseteq\;
  G^{(2)}(\mathcal{H}_q),
$$

with dominant cell $\lambda_K = (2, 2)$ in $H_4(q)$ — *self-conjugate*
([`rem:chirality-period-pairing`](#rem:chirality-period-pairing))
— and shape parameter $z_K = \zeta_6 = e^{i\pi/3}$.

The two group actions:

| Group | Generator | Action on $\mathcal{H}_q^{(2, 4_1)}$ |
|---|---|---|
| $G_{\mathrm{mot}} \supseteq \langle * \rangle$ (bar) | $*: q \mapsto q^{-1}$, $\zeta_6 \mapsto \zeta_6^{-1}$ | $\mathrm{Li}_2^q(\zeta_6) \mapsto \mathrm{Li}_2^q(\zeta_6^{-1})$ |
| $B_4 \to H_4(q)$ | $\sigma_1, \sigma_2, \sigma_3$ | conjugation in $H_4(q)$, fixes central idempotents |

### Proof of joint commutativity

**Step 1 (braid action fixes $e_{(2,2)}$).** $e_{(2,2)} \in Z(H_4(q))$
is central by definition, so for any $\beta \in B_4$:

$$
  \beta \cdot e_{(2,2)} \cdot \beta^{-1} \;=\; e_{(2,2)}.
$$

The braid action on $e_{(2,2)}$ is **trivial** as an automorphism
of $H_4(q)$.

**Step 2 (bar action on $e_{(2,2)}$).** Self-conjugate partition
$\Rightarrow$ bar fixes $e_{(2,2)}$:

$$
  *(e_{(2,2)}) \;=\; e_{(2,2)' } \;=\; e_{(2,2)}
$$

(since $(2, 2)' = (2, 2)$ — transpose of $(2, 2)$ is itself).
**Trivial action on $e_{(2,2)}$.**

**Step 3 (bar action on $\mathrm{Li}_2^q(\zeta_6)$).**
$* \colon \zeta_6 \mapsto \zeta_6^{-1} = \zeta_6^5 = \overline{\zeta_6}$.
The depth-2 grouplike maps:

$$
  *\bigl( \mathrm{Li}_2^q(\zeta_6) \bigr)
  \;=\;
  \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}).
$$

Under archimedean realisation:

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1})\bigr)
  \;=\;
  \mathrm{Li}_2(\overline{\zeta_6})
  \;=\;
  \overline{\mathrm{Li}_2(\zeta_6)}.
$$

The Bloch–Wigner companion: $D(\overline{z}) = -D(z)$ for $z$ on the unit
circle. So bar takes $D(\zeta_6) \mapsto -D(\zeta_6)$.

**Step 4 (braid action on $\mathrm{Li}_2^q(\zeta_6)$).** $B_4$ does
not act on the input $\zeta_6 \in F^\times$ — the shape parameter is
not in the Hecke algebra, it's the algebraic argument of the polylog.
So:

$$
  \beta \cdot \mathrm{Li}_2^q(\zeta_6) \;=\; \mathrm{Li}_2^q(\zeta_6)
  \quad\text{for } \beta \in B_4
$$

(the braid acts on the cell, not on the polylog argument).
**Trivial action.**

**Step 5 (composite actions).** Compute both compositions:

$$
  \begin{aligned}
    \beta \circ * \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr)
    & \;=\; \beta \cdot \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}) \bigr) \\
    & \;=\; e_{(2,2)} \cdot \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}) \quad\text{(Step 1, 4)} \\[4pt]
    * \circ \beta \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr)
    & \;=\; * \cdot \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr) \quad\text{(Step 1, 4)} \\
    & \;=\; e_{(2,2)} \cdot \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}). \quad\text{(Step 2, 3)}
  \end{aligned}
$$

Both compositions yield the same element. **Joint commutativity
holds.** $\square$

### Why this case is structurally trivial

The verification works because **the bar and braid actions touch
disjoint structure**:

- Braid acts on the *cell* $e_{(2,2)} \in Z(H_4(q))$ — but trivially,
  since central idempotents are fixed by inner automorphisms.
- Bar acts on the *coefficient ring* $q$ and the *shape parameter*
  $\zeta_6 \in F^\times$ — but not on the cell.

**Trivial commutativity from disjoint action.** This verifies the
*easiest* case of the joint-action conjecture; the structurally
non-trivial case is **chiral pairs**, where bar swaps cells while
braid acts non-trivially on the swapped pair.

### What this verifies and what remains

**Verified**: $(\lambda, K) = ((2, 2), 4_1)$ — a self-conjugate cell.
By extension, any self-conjugate cell with a polylog argument in
$F^\times$ has trivially commuting bar × braid action.

**Remaining (open)**: chiral-pair cases, e.g.

- $(\lambda, K) = ((3) + (1, 1, 1), 3_1)$ — trefoil cell pair.
- $(\lambda, K) = ((3, 1) + (2, 1, 1), 4_1$-related$)$ — chiral-pair
  partition of 4.
- $(\lambda, K) = (\text{chiral hyperbolic}, 5_2)$ — non-trivial
  cell pair + hyperbolic geometry.

For the trefoil case ($n = 3$): bar takes $e_{(3)}$ to $e_{(1,1,1)}$;
braid $\sigma_1, \sigma_2$ act on the $(2, 1)$ standard rep
non-trivially but commute with central idempotent assignment.
**Verification possible by direct computation** but technical.

### Significance

**The joint-action conjecture
[`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
is verified at the figure-8 row** — the canonical depth-2 row of
B1. The verification is structural (disjoint actions trivially
commute), not numerical. Combined with the figure-8 row's
theorem-level B1 status
([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)):

> **The figure-8 row of the bi-filtration carries the full
> graded-Mikusiński structure as a theorem**: depth-2 inclusion,
> strong sharpness over $\mathbb{Q}(\zeta_6)$, joint Galois × braid
> commutativity, VC asymptotic match, depth correspondence
> verified.

Reduces remaining open questions about the joint action to *non-
self-conjugate / chiral-pair* cases.

### Cross-references

- Joint-action conjecture: [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Bi-filtration: [`def:hq-bi-filtration`](#def:hq-bi-filtration)
- Chirality structure: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)
- Figure-8 row theorem: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Bridge map verification: [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
