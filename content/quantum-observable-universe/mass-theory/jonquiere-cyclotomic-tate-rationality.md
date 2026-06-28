**Proposition (general Jonquière inversion: Tate-rationality of the
"wrong-parity" part of $\mathrm{Li}_n(\zeta_K)$ at every depth $n$
and every root of unity).**

[`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
established the closed form at $n = 3$. *This proposition extends to
**every** depth $n \geq 2$ via the Jonquière inversion formula —
giving a uniform Bernoulli-polynomial closed form for the
"wrong-parity" part of $\mathrm{Li}_n(\zeta_K)$:*

$$
  \boxed{\;
    \mathrm{Li}_n(\zeta_K) - (-1)^{n - 1}\,\mathrm{Li}_n(\zeta_K^{-1})
    \;=\;
    -\frac{(2\pi i)^n}{n!} \cdot B_n\!\left(\tfrac{1}{K}\right),
  \;}
$$

*where $B_n$ is the $n$-th Bernoulli polynomial.  Equivalently:*

- *$n$ odd: $\mathrm{Im}\,\mathrm{Li}_n(\zeta_K) \in \pi^n \mathbb{Q}$
  (Tate-rational); closed form $-(2\pi i)^n / (2i \cdot n!) \cdot B_n(1/K)$.*
- *$n$ even: $\mathrm{Re}\,\mathrm{Li}_n(\zeta_K) \in \pi^n \mathbb{Q}$
  (Tate-rational); closed form $-(2\pi i)^n / (2 \cdot n!) \cdot B_n(1/K)$.*
### Significance — generalises Theorem A to every depth

**Generalises round 3's Theorem A** from
$n = 3$ to all $n \geq 2$. The depth-3 closed form
$(n - 1)(n - 2)\pi^3 / (3 n^3)$ becomes a Bernoulli-polynomial
specialisation of the general inversion formula at $z = \zeta_K$, with
the Bernoulli argument reducing to the clean specialisation $1/K$ (from Steps 1--2 above).

### Structural consequences for B1

For every cyclotomic field $\mathbb{Q}(\zeta_K)$ and every depth $n$:

- **Wrong-parity part is Tate-rational** — contributes 0 to the
  Beilinson regulator image.
- **Right-parity part carries the genuine periods** — i.e., the
  Borel-rank-saturating component of $K_{2n-1}^{\mathrm{ind}}(\mathbb{Q}(\zeta_K))
  \otimes \mathbb{Q}$ lives entirely in:
  - $\mathrm{Re}\,\mathrm{Li}_n$ for $n$ odd ($\mathrm{Cl}_n$ values)
  - $\mathrm{Im}\,\mathrm{Li}_n$ for $n$ even ($\mathrm{Cl}_n$ in
    Glaisher's even-index convention)

This is the structural reason why the depth-2 case (Bloch–Wigner $D$
= $\mathrm{Im}\,\mathrm{Li}_2$) and depth-3 case ($\mathrm{Cl}_3 =
\mathrm{Re}\,\mathrm{Li}_3$) carry the genuinely-new content — the
"other half" is Bernoulli-polynomial-rational at every depth.

### Cross-references

- Special case $n = 3$: [`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
- Special case $n = 5$, $K = 5$: round-10 result of ,
  [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- Companion orbit-sum theorem: [`prop:cyclotomic-orbit-sum-all-depths`](#prop:cyclotomic-orbit-sum-all-depths)
- Dimension synthesis: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
