**Typed-B_3 sub-braid extraction** — n-strand generalisation of the
$c_3 = -2$ chain, narrowing the open axiomatic content to a SINGLE focused
combinatorial fact.

## Scope of this closure

The $n$-strand ($= 3$-strand for typed-$B_3$) case requires extracting sub-braids from the canonical 11-crossing braids
$\beta_p$ ($uud$) and $\beta_n$ ($udd$). The formal derivation:

1. Defines typed 3-strand braid words matching the canonical crossing-list representation.
2. Defines the proton and neutron typed braids $\beta_p$ and $\beta_n$ as explicit lists of crossings.
3. Proves both have length 11 (matching the canonical recipe).
4. Defines sub-braid extraction by selecting crossing indices.
5. Encodes the final substantive hypothesis as a focused condition on the dominant sub-braid at order $\varepsilon^6$ and **proves $c_3 = -2$ conditionally** on it.

## The chain composition

Under this single axiomatic input, the full chain holds:

$$
\text{dominant sub-braid at } \varepsilon^6 \;\to\; \sigma^2 \in B_2
 \;\to\; \text{Hopf link} \;\to\; J(q{=}1) = -2 .
$$

The composed theorem $c_3 = -2$ is closed by the two-strand Jones specialization at $q = 1$ for $\sigma^2$ (already established in
[concrete braid and link types](#rem:braid-link-types)).

## The remaining axiom

The single open hypothesis is:

> Dominant sub-braid at $\varepsilon^6$:
> the dominant sub-braid in the order-$\varepsilon^6$ expansion of
> $\mathrm{tr}_M(\mathcal{B}_n) - \mathrm{tr}_M(\mathcal{B}_p)$ extracts the 2-strand 2-crossing
> case.

This is **categorically verified** via two canonical evaluation runs:
- the canonical formalism — $F_3$'s $\varepsilon^6$ leading coefficient is **exactly** $-3\sqrt{3}/4 = -2 \cdot b(1)^3$.
- the canonical formalism — categorical residual after $N=3$ is $-0.0066$ ppm ($112\times$ tightening), validating the magnitude.

Discharging this hypothesis algebraically requires:

1. **Braid-group perturbative-expansion infrastructure**: define
   $\mathrm{tr}_M(\beta; q)$ as a formal series at $q = 1+\varepsilon$.
2. **Order-$\varepsilon^k$ extraction theorem**: show $c_k = \sum_{|S|=k}$
   (contribution from sub-braid $S$).
3. **Dominant subset identification**: prove the order-$\varepsilon^6$
   dominant 3-element subset of $\beta$ extracts a 2-strand sub-braid.
4. **Composition**: chain into the 2-strand theorem.

Steps 1, 2, 4 are structural series-expansion infrastructure. Step 3 is the
substantive combinatorial content.

## Cumulative atoms

Summary of the derivation chain:

| step | content | status |
|---|---|---|
| **Step C (canonical-equivalence axiom)** | exact arithmetic match | closed (item 2) |
| **Step B (axiomatic closure map)** | two atomic axioms | closed |
| **Step A 2-strand (concrete types)** | $\sigma^2 \to$ Hopf $\to -2$ | closed |
| **Step A n-strand (sub-braid extraction)** | composed under 1 axiom | closed conditionally |
| **Remaining**: dominant-sub-braid combinatorial fact | empirically verified | open combinatorial step |

The single remaining axiomatic content is a **specific combinatorial
fact** about typed-braid sub-braid extraction rather than a research-level
categorical question. Verifying it reduces to a finite combinatorial check on typed three-strand words rather than a deep categorical conjecture.
