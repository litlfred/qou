**Proposition (general closed form for $\mathrm{Im}\,\mathrm{Li}_3$ at
every root of unity).**

The Kummer reflection formula
([`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
established the closed form at $\zeta_5$.  *This proposition
generalises to **all** $n \geq 1$:*

$$
  \boxed{\;
    \mathrm{Im}\,\mathrm{Li}_3(\zeta_n)
    \;=\;
    \frac{(n - 1)(n - 2)\,\pi^3}{3\,n^3}.
  \;}
$$

*In particular, $\mathrm{Im}\,\mathrm{Li}_3(\zeta_n)$ is **Tate-rational**
for every $n$ — lies in $\pi^3 \mathbb{Q}$ — and therefore projects
to zero under the Beilinson regulator quotient
$\mathcal{P}_3 \to \mathcal{P}_3 / \mathrm{Tate}$.*
### Significance

**Generalises round 10 of ** from "$\zeta_5$ only" to "every
root of unity". Concretely:

1. **Every cyclotomic depth-3 imaginary part is Tate-rational** —
   lives in $(2\pi i)^3 \mathbb{Q} = -\pi^3 \mathbb{Q}$ (up to a
   factor of $i$).
2. **Projects to zero under Beilinson regulator quotient** — the
   genuinely-new content at $\zeta_n$ over $\mathbb{Q}(\zeta_n)$ at
   depth 3 lives **entirely in the real part** $\mathrm{Cl}_3(2\pi/n)$
   and its Galois conjugates, not in $\mathrm{Im}\,\mathrm{Li}_3$.
3. **Reduces the depth-3 surface for every cyclotomic field** to the
   real-part Galois orbit, halving the dimension at the outset.

### Asymptotic behaviour

The formula reveals the asymptotic:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_n) \;=\; \frac{\pi^3}{3 n} + O(n^{-2})
$$

as $n \to \infty$.  Decays like $1/n$, with leading coefficient $\pi^3/3$.

### Cross-references

- Special case $n = 5$ (round 10 of ):
  [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- Related orbit-sum:
  [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
- canonical witness (verified at $n = 3, 4, 5, 6, 7, 10, 11, 12, 13$ at 50 dps):
  [`cyclotomic-trilog-imaginary.witness.json`](https://github.com/litlfred/qou/blob/main/computations/cyclotomic-trilog-imaginary.witness.json)
- Geometric realisation question:
  [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
