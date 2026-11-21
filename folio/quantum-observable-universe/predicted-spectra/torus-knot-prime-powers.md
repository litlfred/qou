The torus knots $T_{3,n}$ with $n = p^k$ (prime power, $p \neq 3$) form subfamilies with exponentially growing genus. The Bring surface genus bound permits few of these.

**Genus formula.**
For $T_{3,p^k}$ with $\gcd(3, p^k) = 1$:

$$
  g(T_{3,p^k}) = \frac{(3-1)(p^k - 1)}{2} = p^k - 1.
$$

Embeddability requires $p^k - 1 \leq 4$, which implies $p^k \leq 5$.

**The $p = 2$ tower: $T_{3, 2^k}$.**

| $k$ | Knot | Genus $= 2^k - 1$ | Crossings | Embeddable? | Assignment |
|-----|------|--------------------|-----------|-------------|------------|
| $1$ | $T_{3,2} = T_{2,3}$ (trefoil $3_1$) | $1$ | $3$ | Yes | Electron $e^-$ (lepton partner of $\mathfrak{u}$) |
| $2$ | $T_{3,4}$ ($8_{19}$) | $3$ | $8$ | Yes | Hopf${}^2$ color binding |
| $3$ | $T_{3,8}$ | $7$ | $21$ | **No** | Excluded |
| $4$ | $T_{3,16}$ | $15$ | $45$ | **No** | Excluded |

The genus sequence $1, 3, 7, 15, \ldots$ follows the Mersenne numbers $g = 2^k - 1$. Bring's surface admits exactly two levels of this tower: the trefoil ($k = 1$) and $T_{3,4}$ ($k = 2$, force carrier). A third generation of $p = 2$ knots is impossible.

**The trefoil as self-intersection.**

The identity $T_{3,2} = T_{2,3}$ places the trefoil in both winding families simultaneously:

$$
  T_{2,3} \in \{T_{2,n}\}_{n \text{ odd}} \qquad\text{and}\qquad T_{3,2} \in \{T_{3,p^k}\}_{p \neq 3}.
$$

The trefoil is the unique generator at the intersection of the $m = 2$ (leptonic) and $m = 3$ (quark) families. It places the trefoil in both families. It does not make the trefoil the up quark's knot type: by the [knot–particle dictionary](#rem:knot-particle-dictionary) the up quark is an unknot strand of $\mathcal{B}_3$ whose lepton partner is the trefoil.

| Family | Generators from trefoil seed |
|--------|----------------------------|
| $m = 2$: $T_{2,3} \to T_{2,5} \to T_{2,7} \to T_{2,9}$ | $e^-, \mu, \tau,$ **strong force** |
| $m = 3$: $T_{3,2}, T_{3,4}, T_{3,5}$ | $u,$ **color binding,** **weak force** |

The trefoil is the root node of both generation chains.

**The $p = 5$ tower: $T_{3,5^k}$.**

| $k$ | Knot | Genus $= 5^k - 1$ | Embeddable? |
|-----|------|--------------------|-------------|
| $1$ | $T_{3,5}$ ($10_{124}$) | $4$ | Yes (saturating) |
| $2$ | $T_{3,25}$ | $24$ | No |

Only $k = 1$ embeds. The knot $T_{3,4} = T_{3,2^2}$ squares the trefoil's winding number. By contrast, $T_{3,5}$ is an isolated prime. It does not extend to a tower within Bring's surface.

**The $p = 7$ tower and beyond.**

For $p \geq 7$, $g(T_{3,p}) = p - 1 \geq 6 > 4$. No knot $T_{3,p^k}$ with $p \geq 7$ embeds.

**Classification of embeddable $T_{3,p^k}$.**

$$
  \{T_{3,p^k} : \gcd(3,p^k) = 1, p^k - 1 \leq 4\} = \{T_{3,2}, T_{3,4}, T_{3,5}\}.
$$

The $p = 2$ tower contributes the trefoil (matter) and $T_{3,4}$ (Hopf${}^2$ color binding, $H^{0,1}$ force carrier). The $p = 5$ singleton sits at the genus boundary.

**Matter vs. force dichotomy.**

The power tower $T_{3,2^k}$ establishes a physical pattern:

- $k = 1$: $T_{3,2}$ = trefoil. Lightest matter (the electron, lepton partner of the up quark).
- $k = 2$: $T_{3,4}$. Hopf${}^2$ color binding ($H^{0,1}$ force carrier).
- $k = 3$: Excluded. Bring's surface forbids a third level.

The mass ratio $m_t / m_u \approx 7.5 \times 10^4$ spans four orders of magnitude across the single step $k = 1 \to k = 2$. Exponential genus growth ($2^k - 1$) separates the levels. The Hodge decomposition places $T_{3,4}$ in the $H^{0,1}$ force carrier sector rather than the $H^{1,0}$ matter sector.

The knot $T_{3,5}$ is structurally distinguished from both matter generations. Its prime winding ($n = 5$, not a power of 2) and saturating genus (4) separate it from any power tower. This supports its force carrier interpretation.

**Remark on $T_{2,9}$.**
The three-fold cover $T_{2,9}$ has $n = 9 = 3^2$, a prime power in the $m = 2$ family. Its genus is $(9 - 1)/2 = 4$ (saturating). 

| Family | Power tower (matter) | Isolated prime (force?) |
|--------|---------------------|------------------------|
| $m = 2$ | $T_{2,3}, T_{2,5}, T_{2,7}$ | $T_{2,9}$ ($n = 3^2$) |
| $m = 3$ | $T_{3,2}, T_{3,4}$ ($n = 2^k$) | $T_{3,5}$ ($n = 5$) |

Matter generators have lower genus. The saturating genus-4 generator stands apart. The genus-4 boundary separates matter from force across both winding families.
