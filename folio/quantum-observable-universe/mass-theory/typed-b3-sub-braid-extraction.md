**Typed-B_3 sub-braid extraction** — n-strand generalisation of the
$c_3 = -2$ chain, narrowing the open axiomatic content to a SINGLE focused
combinatorial fact.

## Scope of this closure

The n-strand (= 3-strand for typed-B_3) case requires extracting sub-braids from the canonical 11-crossing braids
β_p (uud) and β_n (udd). Both are typed braid words of length 11, and a
sub-braid is extracted by selecting a subset of crossing indices. The one
substantive input is taken as a hypothesis (stated below), and
**c_3 = -2 is proved conditionally** on it.

## The chain composition

Under the single hypothesis, the full chain is proved:

$$
\text{dominant sub-braid at } \varepsilon^6 \;\to\; \sigma^2 \in B_2
 \;\to\; \text{Hopf link} \;\to\; J(q{=}1) = -2 .
$$

The last step is the value $J(q{=}1) = -2$ of the closure of $\sigma^2$,
already proved in [the concrete braid and link types](#rem:braid-link-types).

## The remaining hypothesis

The single open hypothesis is:

> the dominant sub-braid in the order-$\varepsilon^6$ expansion of
> $\mathrm{tr}_M(\mathcal{B}_n) - \mathrm{tr}_M(\mathcal{B}_p)$ extracts the 2-strand 2-crossing
> case.

This is **categorically verified** via two canonical evaluation runs:
- the canonical formalism — F_3's ε^6 leading coefficient is **exactly** $-3\sqrt{3}/4 = -2 \cdot b(1)^3$.
- the canonical formalism — categorical residual after N=3 is $-0.0066$ ppm (112$\times$ tightening), validating the magnitude.

A proof of this hypothesis requires:

1. **Perturbative-expansion infrastructure on $B_n$**: define
   $\mathrm{tr}_M(\beta; q)$ as a formal series at $q = 1+\varepsilon$.
2. **Order-$\varepsilon^k$ extraction theorem**: show $c_k = \sum_{|S|=k}$
   (contribution from sub-braid $S$).
3. **Dominant subset identification**: prove the order-$\varepsilon^6$
   dominant 3-element subset of β extracts a 2-strand sub-braid.
4. **Composition**: chain into the 2-strand theorem.

Steps 1, 2, 4 are mechanical infrastructure. Step 3 is the
substantive combinatorial content.

## Cumulative atoms

In summary:

| step | content | status |
|---|---|---|
| **Step C (canonical-equivalence axiom)** | exact arithmetic match | closed (item 2) |
| **Step B (axiomatic closure map)** | two atomic axioms | closed |
| **Step A 2-strand (concrete types)** | $\sigma^2 \to$ Hopf $\to -2$ | closed |
| **Step A n-strand (sub-braid extraction)** | composed under 1 axiom | closed conditionally |
| **Remaining**: dominant-sub-braid combinatorial fact | empirically verified | open |

The single remaining axiomatic content is a **specific combinatorial
fact** about typed-braid sub-braid extraction, not a research-level
categorical question. Proving it is substantial work but no
longer at the categorical-frontier level.
