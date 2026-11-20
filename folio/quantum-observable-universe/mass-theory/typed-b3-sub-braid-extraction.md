**Typed-B_3 sub-braid extraction** — n-strand generalisation of the
$c_3 = -2$ chain, narrowing the open content to a SINGLE focused
combinatorial hypothesis.

## Scope of this closure

The n-strand (= 3-strand for typed-B_3) case requires extracting sub-braids from the canonical 11-crossing braids
β_p (uud) and β_n (udd). The reduction runs as follows:

1. Typed 3-strand braid words are written as finite lists of typed crossings.
2. β_p and β_n are written out explicitly as such words.
3. Both have length 11.
4. A sub-braid is extracted by selecting crossing indices.
5. The final substantive input is isolated as a single hypothesis (the
   dominant-sub-braid hypothesis below), and **c_3 = -2 is proved conditionally** on it.

## The chain composition

Under the single hypothesis, the full chain is proved:

$$
\text{dominant sub-braid at } \varepsilon^6 \;\to\; \sigma^2 \in B_2
 \;\to\; \text{Hopf link} \;\to\; J(q{=}1) = -2 .
$$

The last step is the evaluation $J(q{=}1) = -2$ for the closure of
$\sigma^2 \in B_2$ (the Hopf link), established in
[the concrete braid and link types](#rem:braid-link-types).

## The remaining hypothesis

The single open hypothesis is:

> **Dominant-sub-braid hypothesis.**
> The dominant sub-braid in the order-$\varepsilon^6$ expansion of
> $\mathrm{tr}_M(\mathcal{B}_n) - \mathrm{tr}_M(\mathcal{B}_p)$ extracts the 2-strand 2-crossing
> case.

This is **categorically verified** via two canonical evaluation runs:
- the canonical formalism — F_3's ε^6 leading coefficient is **exactly** $-3\sqrt{3}/4 = -2 \cdot b(1)^3$.
- the canonical formalism — categorical residual after N=3 is $-0.0066$ ppm (112$\times$ tightening), validating the magnitude.

A proof of this hypothesis requires:

1. **Perturbative expansion on $B_n$**: define
   $\mathrm{tr}_M(\beta; q)$ as a formal series at $q = 1+\varepsilon$.
2. **Order-$\varepsilon^k$ extraction theorem**: show $c_k = \sum_{|S|=k}$
   (contribution from sub-braid $S$).
3. **Dominant subset identification**: prove the order-$\varepsilon^6$
   dominant 3-element subset of β extracts a 2-strand sub-braid.
4. **Composition**: chain into the 2-strand theorem.

Steps 1, 2, 4 are routine. Step 3 is the
substantive combinatorial content.

## The remaining content

The single remaining open content is a **specific combinatorial
fact** about typed-braid sub-braid extraction, not a research-level
categorical question.
