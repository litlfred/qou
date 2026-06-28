**Proposition (joint Galois $\times$ braid action commutes on the figure-8
bi-filtration cell — verified directly).**

The joint motivic-Galois $\times$ braid-group action conjecture
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

### Cross-references

- Joint-action conjecture: [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Bi-filtration: [`def:hq-bi-filtration`](#def:hq-bi-filtration)
- Chirality structure: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)
- Figure-8 row theorem: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Bridge map verification: [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
