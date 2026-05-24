**Proposition (Borromean Markov trace closed form).**
*The Markov trace of the Borromean braid
$\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$ on $H_3(q)$,
evaluated via the Jones polynomial of the Borromean rings
$\mathcal{B}_3$, admits the exact closed form*

$$
  \boxed{\;\;
  \mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)
  \;=\;
  \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4},
  \;\;}
$$

*where $h = q - q^{-1}$ and $h^2 + 4 = [2]_q^2$.*

**Proof.** The Jones polynomial of the Borromean rings is
\cite{murasugi1996}:

$$
  V(\mathcal{B}_3, t)
  = -t^{-3} + 3t^{-2} - 2t^{-1} + 4 - 2t + 3t^2 - t^3.
$$

Setting $t = q^2$ and introducing $u := q^2 + q^{-2}$, this becomes
a polynomial in $u$:

$$
  V = -u^3 + 3u^2 + u - 2.
$$

For a 3-component link, the Markov trace is $\mathrm{tr}_M =
V / [2]_q^2$ where $[2]_q^2 = (q + q^{-1})^2 = u + 2$. Polynomial
long division yields:

$$
  \frac{V}{u + 2}
  = -u^2 + 5u - 9 + \frac{16}{u + 2}.
$$

Substituting $u = h^2 + 2$ (where $h = q - q^{-1}$, so
$q^2 + q^{-2} = h^2 + 2$):

$$
  \mathrm{tr}_M
  = -(h^2 + 2)^2 + 5(h^2 + 2) - 9 + \frac{16}{h^2 + 4}
  = \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}.
$$

$\square$

## The $h$-expansion (purely even)

Taylor-expanding around $h = 0$:

$$
  \mathrm{tr}_M
  = 1
    + \underbrace{0}_{\text{no } h^2}
    \cdot h^2
    - \underbrace{\frac{3}{4}}_{h^4} \cdot h^4
    - \underbrace{\frac{1}{16}}_{h^6} \cdot h^6
    + \underbrace{\frac{1}{64}}_{h^8} \cdot h^8
    + \cdots
$$

The series is **purely even** in $h$ (the numerator and denominator
are both even polynomials in $h$). The higher-order coefficients
follow a geometric tail from the remainder term $16/(h^2 + 4)$.

## The $h^2$ coefficient is exactly zero

The vanishing of the $h^2$ term is a **non-trivial cancellation**:
the numerator HAS an $h^2$ coefficient ($+1$), but the denominator's
$h^2$ coefficient ($+1$) cancels it exactly:

$$
  \frac{4 + h^2 - 3h^4 - h^6}{4 + h^2}
  = \frac{(4 + h^2) + (-3h^4 - h^6)}{4 + h^2}
  = 1 + \frac{-3h^4 - h^6}{h^2 + 4}.
$$

The first non-trivial correction appears at $h^4$ with coefficient
$-3/4$: the **first topological invariant** of the Borromean linking
structure — the part of the Jones polynomial that distinguishes
$\mathcal{B}_3$ from the trivial 3-component unlink.

## Per-representation structure

The three irreps of $S_3$ / $H_3(q)$ contribute distinctly:

- **$\lambda = (3)$ [trivial, dim 1]:** $\sigma_i = q$ (scalar) →
  $(\sigma_1^{-1}\sigma_2)^3 = 1$ exactly for all $q$. Contributes
  only through the $q$-dependent Wenzl weight $y_{(3)}(q)$.

- **$\lambda = (1^3)$ [sign, dim 1]:** $\sigma_i = -q^{-1}$ (scalar) →
  $(\sigma_1^{-1}\sigma_2)^3 = 1$ exactly for all $q$. Same.

- **$\lambda = (2,1)$ [standard, dim 2]:** The **only non-abelian
  irrep**. ALL correction terms ($h^4, h^6, \ldots$) originate from
  this partition alone — the two 1-dimensional representations have
  commuting generators and contribute trivially.

## Structural significance for the linking weight

The exact closed form shows that the Borromean Markov trace has NO
$h^2$ curvature correction. The $h^2$ contribution to the linking
weight $\mathfrak{w}(\mathcal{B}_3)$ — whatever its categorical
derivation — must come from the **Geom functor's evaluation layer**
(the $\mathrm{Vol}/\hbar_q^2$ denominator parametrization), not from
the braid character itself. The Canonical Wedderburn $h^2$ coefficient
$+3/4$ (per `prop:lambda-scale-substrate-form`) is thus confirmed as a
**Geom-level contribution**, structurally independent of the Markov
trace.
