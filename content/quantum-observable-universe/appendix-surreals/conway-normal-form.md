Every surreal $x \in \mathbf{No}$ admits a unique **Conway normal form**
[@conway1976 §5; @gonshor1986 Ch. 5]:

$$
  x \;=\; \sum_{i < \lambda} \omega^{y_i} \, r_i
$$

where:

- $\lambda$ is an ordinal (possibly finite);
- $y_0 > y_1 > y_2 > \cdots$ is a strictly decreasing sequence of
  surreals (not necessarily ordinals) — the **exponents**;
- $r_i \in \mathbb{R} \setminus \{0\}$ — the **coefficients**;
- $\omega$ is the first infinite surreal.

The sum is formal; convergence is in the Hahn-series sense (well-
ordered support). This embeds $\mathbf{No}$ into the Hahn series
ring $\mathbb{R}((\omega^{\mathbf{No}}))$ [@ehrlich2012], making
$\mathbf{No}$ a field of *generalised power series* in $\omega$
with surreal exponents.

## Why this is not just an analogy

The normal form **literally is** the algebra of growth rates:

- The **leading exponent** $y_0$ gives the exact asymptotic class
  of $x$.
- Big-O notation $f = O(g)$ is a coarse, analytic shadow of the
  algebraic relation $b(y_0^{f}) \leq b(y_0^{g})$ on leading
  surreal exponents.
- Multiplication of normal forms corresponds to ordinary growth-
  rate arithmetic: $\omega^{y_i} r_i \cdot \omega^{y_j} r_j =
  \omega^{y_i + y_j} r_i r_j$.
- Infinitesimal $\varepsilon = 1/\omega = \omega^{-1}$; its normal
  form is $\omega^{-1} \cdot 1$, exponent $-1$.
- The substrate deviation $q - 1 = \varepsilon$ has normal form
  exponent $-1$; $(q-1)^2 = \varepsilon^2$ has exponent $-2$.

## Examples in the QOU setting

| Quantity | Normal form at $q = 1 + \varepsilon$ | Leading exp |
|---|---|---|
| $c_q = 1/(q-1)$ | $\omega \cdot 1$ | $1$ |
| $\hbar_q = (q-1)/q$ | $\omega^{-1} \cdot 1 + \omega^{-2} \cdot (-1) + \cdots$ | $-1$ |
| $q - 1 = \varepsilon$ | $\omega^{-1} \cdot 1$ | $-1$ |
| $d_H(q) - 1$ | $\omega^{-1} \cdot 2 + \cdots$ | $-1$ |
| $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ at $q = 1$ | $\omega^0 \cdot n + O(\omega^{-1})$ | $0$ |
| $\mathrm{Vol}$-like quantum dilogarithm | surreal-log expansion | transfinite |

## The leading-exponent functor

Write $\mathrm{lead}(x) = y_0$ for the leading exponent of
$x \in \mathbf{No}^\times$. This is a group homomorphism from
$(\mathbf{No}^\times, \cdot)$ to $(\mathbf{No}, +)$:

$$
  \mathrm{lead}(x \cdot y) = \mathrm{lead}(x) + \mathrm{lead}(y).
$$

It is the **non-archimedean valuation** associated to the valuation
ring $\mathcal{O}$
([valuation ring of finite surreals](#def:valuation-ring-finite-surreals)):

- $\mathrm{lead}(x) < 0$ iff $x \in \mathfrak{m}$ (infinitesimal).
- $\mathrm{lead}(x) = 0$ iff $x$ is a finite non-infinitesimal
  (has a non-zero real standard-part).
- $\mathrm{lead}(x) > 0$ iff $|x|$ is infinite.

## Applications in the appendix

1. **Growth-rate of spectral operators**
   ([spectral normal form](#conj:spectral-normal-form)): read the
   leading exponent of each eigenvalue under $q = 1 + \varepsilon$
   deformation.

2. **Asymptotic classes of substrate expansions**: the
   Hahn-series substrate $q = 1 + \varepsilon + \alpha_2\varepsilon^2
   + \cdots$ has normal form
   $\omega^0 \cdot 1 + \omega^{-1} \cdot 1 + \omega^{-2} \cdot \alpha_2 +
   \cdots$, and each $\alpha_k$ can be tested by projection to the
   coefficient at exponent $-k$.

3. **Diophantine approximation structure**: algebraic numbers have
   *rigid* normal forms (short, finite support in $\omega^{\mathbb{Q}}$);
   transcendental numbers have *infinite-support* normal forms with
   transfinite exponents. This gives a clean algebraic shadow of
   Liouville/Roth approximation theorems.

## Non-archimedean valuation theorem

Because $\mathbf{No}$ with normal-form comparison is a Hahn field
over $(\mathbf{No}, +)$, it is a **maximally-complete valued field**
[@ehrlich2012 Theorem 14.3]. Every universal construction in the
theory of valued fields (Newton polygon, ramification, completions)
can be ported.
