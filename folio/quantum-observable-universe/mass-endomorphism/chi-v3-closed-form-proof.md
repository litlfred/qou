**Formal proof of the $V_{(3)}$ per-irrep character difference closed form.**

$$
  \boxed{
    \chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)
    \;=\; -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q}
    \;=\; -\frac{q^5 + q^3 - q - q^{-1}}{4}
  }
$$

## Derivation

On $V_{(3)}$ (the symmetric 1-dimensional irrep of $H_3(q)$), each Hecke generator acts as the scalar $q$:

  - $\sigma_i \mapsto q$
  - $\sigma_i^{-1} = \sigma_i - (q - q^{-1}) \mapsto q^{-1}$
  - $\text{averaged} = \frac{1}{2}(\sigma + \sigma^{-1}) \mapsto (q + q^{-1})/2$

The canonical typed-$\mathbf{B}_3$ braids carry:

  - $\mathcal{B}_p$ (uud): $6\sigma + 3\sigma^{-1} + 2\text{ averaged}$
  - $\mathcal{B}_n$ (udd): $5\sigma + 4\sigma^{-1} + 2\text{ averaged}$

The characters multiply as:

  - $\chi_{(3)}(\mathcal{B}_p) = q^6 \cdot q^{-3} \cdot \left(\frac{q + q^{-1}}{2}\right)^2 = q^3 \cdot \frac{(q + q^{-1})^2}{4}$
  - $\chi_{(3)}(\mathcal{B}_n) = q^5 \cdot q^{-4} \cdot \left(\frac{q + q^{-1}}{2}\right)^2 = q \cdot \frac{(q + q^{-1})^2}{4}$

The difference factors as:

$$
  \chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)
  = (q - q^3) \cdot \frac{(q + q^{-1})^2}{4}
  = -q(q^2 - 1) \cdot \frac{(q^2 + 1)^2/q^2}{4}
  = -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q}.
$$

Expanding the rational form gives:

$$
  -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q}
  = -\frac{(q^4 + 2q^2 + 1)(q^2 - 1)}{4q}
  = -\frac{q^6 + q^4 - q^2 - 1}{4q}
  = -\frac{q^5 + q^3 - q - q^{-1}}{4}.
$$

## Pattern at $q = 1 + \varepsilon$

The closed form splits into polynomial and geometric components:

$$
  -\frac{q^5 + q^3 - q - q^{-1}}{4}
   \;=\; \underbrace{-\frac{q^5 + q^3 - q}{4}}_{\text{polynomial part (degree 5)}}
       \;+\; \underbrace{\frac{q^{-1}}{4}}_{\text{geometric series part}}.
$$

- The polynomial part has degree 5 in $q$. Its $\varepsilon^k$ coefficient at $q = 1 + \varepsilon$ vanishes for $k \geq 6$.
- The geometric part $\frac{q^{-1}}{4} = \frac{1}{4(1 + \varepsilon)} = \frac{1}{4} \sum_{k \geq 0} (-1)^k \varepsilon^k$ contributes $\frac{(-1)^k}{4}$ at every order $k$.

For $k \geq 6$, it follows that:

$$
  [\varepsilon^k]\;\bigl(\chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)\bigr)\big|_{q = 1 + \varepsilon}
   \;=\; \frac{(-1)^k}{4}.
$$

## Summary of established identities

See [Table 1](#tbl:chi-v3-closed-form-proof-table-data). All identities hold unconditionally by direct rational simplification after unfolding.
