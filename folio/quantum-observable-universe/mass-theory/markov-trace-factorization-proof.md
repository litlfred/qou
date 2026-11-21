## Proof of factorization

By hypothesis the nuclear braid word is $X_0 X_1 \cdots X_{A-2}$,
where $X_i$ collects the crossing factors at the single generator
$\sigma_i$.  Using $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$,
each $X_i$ reduces to $a_i \sigma_i + b_i$.  This step needs the
grouping: Hecke reduction does not regroup an interleaved word, since
adjacent generators do not commute.

The full reduced element is the product
$\prod_{i=0}^{A-2} (a_i \sigma_i + b_i)$ where the factors are
ordered by generator index (right to left: $\sigma_{A-2}$ first,
$\sigma_0$ last).

The Markov trace processes this product by peeling generators from
the right.  At each step, $\sigma_i$ is the rightmost (largest)
generator in the remaining word, and the Markov property gives:

$$
  \mathrm{tr}(\cdots (a_i \sigma_i + b_i))
  = 
  (z \cdot a_i + b_i) \cdot \mathrm{tr}(\cdots).
$$

This works because:

1. The chain at $\sigma_i$ reduces to $a_i \sigma_i + b_i$
   (a linear combination of $\sigma_i$ and the identity).

2. The Markov property $\mathrm{tr}(x \sigma_n) = z\mathrm{tr}(x)$
   applies to the $\sigma_i$ term, and $\mathrm{tr}(x \cdot 1) = \mathrm{tr}(x)$ for the identity term.

3. Generator $\sigma_i$ is the **rightmost** active generator
   when processing from right to left, so the Markov property
   applies directly.

4. The remaining word after peeling $\sigma_i$ involves only
   generators $\sigma_0, \ldots, \sigma_{i-1}$, which are
   independent of $\sigma_i$.

Applying this recursively from $i = A-2$ down to $i = 0$ gives
the product formula.  $\square$

**The ratio = 1.000000 in the computational verification is
exact by construction** — the product formula and the direct
trace compute the same algebraic object.  The canonical
verification confirms code correctness, not an approximation.
The values below were computed under the excised convention-C weight
$z = \sqrt q/(q+1)$; they
are not the canonical traces (for ${}^{2}\mathrm{H}$ the convention-D value is
$z = q^3/(q^2+1) \approx 0.61269$). The ratio column does not depend on the
convention, because the factorization is an algebraic identity in $z$.

| Nucleus | $A$ | $\binom{A}{2}$ | $\prod_i \hat{V}_i$ | Direct trace | Ratio |
|---------|-----|:-:|------|------|:-----:|
| ${}^{2}\mathrm{H}$ | 2 | 1 | $0.49932008$ | $0.49932008$ | $1$ |
| ${}^{3}\mathrm{H}$ | 3 | 3 | $0.65630083$ | $0.65630083$ | $1$ |
| ${}^{3}\mathrm{He}$ | 3 | 3 | $0.60100173$ | $0.60100173$ | $1$ |
| ${}^{4}\mathrm{He}$ | 4 | 6 | $0.50430647$ | $0.50430647$ | $1$ |
| ${}^{6}\mathrm{Li}$ | 6 | 15 | $1.07955763$ | $1.07955763$ | $1$ |

For heavy nuclei ($A > 6$), only the product formula is
tractable — the direct computation exceeds $10^5$ terms.
