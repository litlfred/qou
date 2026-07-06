### Proof of joint commutativity

**Step 1 (braid action fixes $e_{(2,2)}$).** The idempotent $e_{(2,2)} \in Z(H_4(q))$ is central. For any $\beta \in B_4$, we have

$$
  \beta \cdot e_{(2,2)} \cdot \beta^{-1} \;=\; e_{(2,2)}.
$$

The braid action on $e_{(2,2)}$ is trivial.

**Step 2 (bar action on $e_{(2,2)}$).** The partition $(2, 2)$ is self-conjugate, $(2, 2)' = (2, 2)$. The bar involution transposes partitions, so it fixes $e_{(2,2)}$:

$$
  *(e_{(2,2)}) \;=\; e_{(2,2)' } \;=\; e_{(2,2)}.
$$

**Step 3 (bar action on $\mathrm{Li}_2^q(\zeta_6)$).**
The bar involution maps $\zeta_6 \mapsto \zeta_6^{-1} = \zeta_6^5 = \overline{\zeta_6}$.
The depth-2 grouplike element transforms as

$$
  *\bigl( \mathrm{Li}_2^q(\zeta_6) \bigr)
  \;=\;
  \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}).
$$

Under archimedean realisation, this yields

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1})\bigr)
  \;=\;
  \mathrm{Li}_2(\overline{\zeta_6})
  \;=\;
  \overline{\mathrm{Li}_2(\zeta_6)}.
$$

The Bloch–Wigner companion satisfies $D(\overline{z}) = -D(z)$ for $z$ on the unit circle. The bar involution therefore maps $D(\zeta_6) \mapsto -D(\zeta_6)$.

**Step 4 (braid action on $\mathrm{Li}_2^q(\zeta_6)$).** The shape parameter $\zeta_6 \in F^\times$ is the algebraic argument of the polylogarithm, not an element of the Hecke algebra. The braid group $B_4$ does not act on it. We find

$$
  \beta \cdot \mathrm{Li}_2^q(\zeta_6) \;=\; \mathrm{Li}_2^q(\zeta_6)
  \quad\text{for } \beta \in B_4.
$$

**Step 5 (composite actions).** We evaluate both operator compositions on the cell. Applying the results of Steps 1 through 4, we compute

$$
  \begin{aligned}
    \beta \circ * \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr)
    & \;=\; \beta \cdot \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}) \bigr) \\
    & \;=\; e_{(2,2)} \cdot \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}) \\[4pt]
    * \circ \beta \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr)
    & \;=\; * \cdot \bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr) \\
    & \;=\; e_{(2,2)} \cdot \mathrm{Li}_2^{q^{-1}}(\zeta_6^{-1}).
  \end{aligned}
$$

Both compositions yield the same element. Joint commutativity holds. $\square$
