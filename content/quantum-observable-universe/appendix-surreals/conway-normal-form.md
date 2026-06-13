Every surreal $x \in \mathbf{No}$ admits a unique **Conway normal
form** [@conway1976 §5; @gonshor1986 Ch. 5]:

$$
  x \;=\; \sum_{i < \lambda} \omega^{y_i} \, r_i
$$

where $y_0 > y_1 > \cdots$ is a strictly decreasing sequence of
surreals, $r_i \in \mathbb{R} \setminus \{0\}$, and $\omega$ is the
first infinite surreal. The sum has well-ordered support
(Hahn-series convention). This embeds $\mathbf{No}$ into the
Hahn field $\mathbb{R}((\omega^{\mathbf{No}}))$ [@ehrlich2012].

## Leading exponent, leading coefficient

For $x \neq 0$ define

$$
  \ordw(x) := y_0, \qquad
  \mathrm{lc}(x) := r_0.
$$

$\ordw$ is a **group homomorphism** $(\mathbf{No}^\times,
\cdot) \to (\mathbf{No}, +)$:

$$
  \ordw(x \cdot y) = \ordw(x) + \ordw(y).
$$

It is the non-archimedean valuation associated to the valuation
ring $\mathcal{O}$ of finite surreals
([valuation ring](#rem:valuation-ring-finite-surreals)):

| Regime | Condition on $\ordw(x)$ | Meaning |
|---|---|---|
| $x$ infinitesimal | $\ordw(x) < 0$ | $x \in \mathfrak{m}$ |
| $x$ finite non-inf. | $\ordw(x) = 0$ | $\mathrm{st}(x) \neq 0$ |
| $x$ infinite | $\ordw(x) > 0$ | $x \notin \mathcal{O}$ |

## Dictionary: Big-O / little-o $\leftrightarrow$ leading exponent

Classical asymptotic notation aligns — indeed, it *is* a
leading-exponent statement in disguise.

For $f, g$ evaluated at $q = 1 + \varepsilon$ (equivalently, for
$f, g$ in the Hahn field):

| Classical | Surreal | Proposed notation |
|---|---|---|
| $f = O(g)$ | $\ordw(f) \leq \ordw(g)$ | $f \preceq g$ |
| $f = o(g)$ | $\ordw(f) < \ordw(g)$ | $f \prec g$ |
| $f = \Theta(g)$ | $\ordw(f) = \ordw(g)$ | $f \asymp g$ |
| $f \sim g$ | $\ordw(f) = \ordw(g)$ and $\mathrm{lc}(f) = \mathrm{lc}(g)$ | $f \simeq g$ |
| $f = g + O(h)$ | $\ordw(f - g) \leq \ordw(h)$ | $f \equiv g \pmod{\preceq h}$ |

## Why this is better than classical Big-O

Classical Big-O has three well-known pathologies:

1. **$=$ abuse.** $f = O(g)$ is not an equality in any group-
 theoretic sense; $O(g)$ is silently a set and $f = O(g)$ means
 $f \in O(g)$.
2. **Asymmetric reading.** $O(f) + O(g) = O(f+g)$ is a rule of
 thumb, not a theorem in any algebraic structure.
3. **Cannot distinguish sub-polynomial behaviours.** $e^{-1/\varepsilon}$
 and $\varepsilon^\omega$ are both $o(\varepsilon^n)$ for every
 $n \in \mathbb{N}$, so Big-O cannot separate them.

The surreal valuation replaces these with:

1. **Clean inequality** $\ordw(f) \leq \ordw(g)$ on
 elements of the ordered group $(\mathbf{No}, +)$.
2. **Algebraic laws**:
 $$
     \ordw(f \cdot g) = \ordw(f) + \ordw(g),
     \qquad
     \ordw(f + g) \leq \max(\ordw(f), \ordw(g))
   $$
 (ultrametric, with equality when leading exponents differ).
3. **Strict refinement by birthday**: when two quantities share a
 leading exponent, the birthday of that exponent —
 $b(\ordw(f))$ — gives an ordinal-valued depth gauge.
 So $\ordw(e^{-1/\varepsilon})$ and $\ordw(\varepsilon^\omega)$
 are both negative infinite, but at *different birthdays*,
 distinguishing functions that classical Big-O cannot.

## Example rewrites

```
classical:  f(x) = x² + 5x + O(1)  as x → ∞
surreal:    f(x) = x² + 5x + r     where r ≺ 1  (i.e., ord_ω(r) < 0)

classical:  f(q) = g(q) + O((q-1)²)  as q → 1
surreal:    f ≡ g  (mod  ≺ ε²)      i.e., ord_ω(f - g) ≤ -2

classical:  ∫₀¹ e^{-x/ε} dx ∼ ε  as ε → 0⁺
surreal:    ∫₀¹ e^{-x/ε} dx ≃ ε   (leading exponent and leading coeff agree)
```

## Why it matters for QOU

Three uses specific to the main paper:

1. **Experimental fits.** The leading-coefficient-level fit on
 $\mathcal{Q}$-values gives a residual that is interpretable as
 a fit at that order. Writing predictions in the form
 $\mathfrak{m}_{\mathfrak{H}} = \hat{\mathfrak{m}}_{\mathfrak{H}}
   + r$ with $r \prec 1$ makes the *order of the residual*
 an explicit surreal exponent rather than a hidden Big-O.

2. **Spectral gaps and singularity formation as $q \to 1$.** The
 sequence of eigenvalues of a $q$-deformed operator has a normal
 form; the leading exponent tells you whether a gap closes
 algebraically (rational exponent) or transcendentally (involves
 $\omega$-order infinitesimals).

3. **Renormalisation counterterms.** Each counterterm $C(\Lambda)$
 in the [blow-up calculus](#def:surreal-blowup-calculus) has a
 specific leading exponent; matching counterterms to divergences
 becomes: match leading exponents.

## Suggested notational convention

For the appendix, use $\preceq, \prec, \asymp, \simeq$ uniformly.
The main paper can adopt this as a *macro-level* convention in a
future revision, reserving $O, o, \Theta, \sim$ for legacy citations.
