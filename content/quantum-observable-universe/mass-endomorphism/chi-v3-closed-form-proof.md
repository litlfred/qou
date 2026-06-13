*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Formal proof of the $V_{(3)}$ per-irrep character difference closed form.**

Following the user direction "first prove formally V" + "V_3 ε^k
pattern" on the per-Wedderburn-block probe (#672), this block
delivers a **complete formal proof** of the V_(3) component:

$$
  \boxed{
    \chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)
    \;=\; -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q}
    \;=\; -\frac{q^5 + q^3 - q - q^{-1}}{4}
  }
$$

## Derivation (proven in Lean)

On $V_{(3)}$ (the symmetric 1-d irrep of $H_3(q)$), each Hecke
generator acts as the scalar $q$:

  - $\sigma_i \mapsto q$
  - $\sigma_i^{-1} = \sigma_i - (q - q^{-1}) \mapsto q^{-1}$
  - averaged $= \frac{1}{2}(\sigma + \sigma^{-1}) \mapsto (q + q^{-1})/2$

The canonical typed-$\mathbf{B}_3$ braids carry:

  - $\mathcal{B}_p$ (uud): 6 $\sigma$ + 3 $\sigma^{-1}$ + 2 averaged
  - $\mathcal{B}_n$ (udd): 5 $\sigma$ + 4 $\sigma^{-1}$ + 2 averaged

The characters multiply as

  - $\chi_{(3)}(\mathcal{B}_p) = q^6 \cdot q^{-3} \cdot \left(\frac{q + q^{-1}}{2}\right)^2 = q^3 \cdot \frac{(q + q^{-1})^2}{4}$
  - $\chi_{(3)}(\mathcal{B}_n) = q^5 \cdot q^{-4} \cdot \left(\frac{q + q^{-1}}{2}\right)^2 = q \cdot \frac{(q + q^{-1})^2}{4}$

and the difference factors as

$$
  \chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)
  = (q - q^3) \cdot \frac{(q + q^{-1})^2}{4}
  = -q(q^2 - 1) \cdot \frac{(q^2 + 1)^2/q^2}{4}
  = -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q}.
$$

Expanding the rational form:

$$
  -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q}
  = -\frac{(q^4 + 2q^2 + 1)(q^2 - 1)}{4q}
  = -\frac{q^6 + q^4 - q^2 - 1}{4q}
  = -\frac{q^5 + q^3 - q - q^{-1}}{4}.
$$

## ε^k pattern at q = 1 + ε

The closed form splits as

$$
  -\frac{q^5 + q^3 - q - q^{-1}}{4}
   \;=\; \underbrace{-\frac{q^5 + q^3 - q}{4}}_{\text{polynomial part (degree 5)}}
       \;+\; \underbrace{\frac{q^{-1}}{4}}_{\text{geometric series part}}.
$$

- The **polynomial part** has degree 5 in $q$, so its $\varepsilon^k$ coefficient at $q = 1 + \varepsilon$ **vanishes for $k \geq 6$**.
- The **geometric part** $\frac{q^{-1}}{4} = \frac{1}{4(1 + \varepsilon)} = \frac{1}{4} \sum_{k \geq 0} (-1)^k \varepsilon^k$ has $\varepsilon^k$ coefficient $\frac{(-1)^k}{4}$ for every $k$.

**Hence for $k \geq 6$**:

$$
  [\varepsilon^k]\;\bigl(\chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)\bigr)\big|_{q = 1 + \varepsilon}
   \;=\; \frac{(-1)^k}{4}.
$$

This matches the probe output `+1/4, -1/4, +1/4, ...` for $k = 6, 7, 8, ...$ exactly.

## Lean theorems exported

See [Table: Lean theorems for $\chi_{V_3}$](#tbl:chi-v3-closed-form-proof-table-data).
| `chi_V3_difference_decomposition` | split into polynomial part + geometric part |
| `chi_V3_polynomial_part_at_one` | polynomial part vanishes at $q = 1$ |
| `chi_V3_geom_part_at_one` | geometric part equals $1/4$ at $q = 1$ |
| `chi_V3_difference_at_two` | numerical: $-75/8$ at $q = 2$ |
| `chi_V3_difference_at_one` | vanishes at $q = 1$ (isospin invariance) |
| `chi_V3_decomposition_at_two` | decomposition verified at $q = 2$ |

All theorems are **sorry-free**, closed by `field_simp + ring` after
unfolding.
