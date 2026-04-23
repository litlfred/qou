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
  \mathrm{lead}(x) := y_0, \qquad
  \mathrm{lc}(x) := r_0.
$$

$\mathrm{lead}$ is a **group homomorphism** $(\mathbf{No}^\times,
\cdot) \to (\mathbf{No}, +)$:

$$
  \mathrm{lead}(x \cdot y) = \mathrm{lead}(x) + \mathrm{lead}(y).
$$

It is the non-archimedean valuation associated to the valuation
ring $\mathcal{O}$ of finite surreals
([valuation ring](#rem:valuation-ring-finite-surreals)):

| Regime | Condition on $\mathrm{lead}(x)$ | Meaning |
|---|---|---|
| $x$ infinitesimal | $\mathrm{lead}(x) < 0$ | $x \in \mathfrak{m}$ |
| $x$ finite non-inf. | $\mathrm{lead}(x) = 0$ | $\mathrm{st}(x) \neq 0$ |
| $x$ infinite | $\mathrm{lead}(x) > 0$ | $x \notin \mathcal{O}$ |

## Dictionary: Big-O / little-o $\leftrightarrow$ leading exponent

Classical asymptotic notation aligns cleanly — indeed, it *is* a
leading-exponent statement in disguise.

For $f, g$ evaluated at $q = 1 + \varepsilon$ (equivalently, for
$f, g$ in the Hahn field):

| Classical | Surreal | Proposed notation |
|---|---|---|
| $f = O(g)$ | $\mathrm{lead}(f) \leq \mathrm{lead}(g)$ | $f \preceq g$ |
| $f = o(g)$ | $\mathrm{lead}(f) < \mathrm{lead}(g)$ | $f \prec g$ |
| $f = \Theta(g)$ | $\mathrm{lead}(f) = \mathrm{lead}(g)$ | $f \asymp g$ |
| $f \sim g$ | $\mathrm{lead}(f) = \mathrm{lead}(g)$ and $\mathrm{lc}(f) = \mathrm{lc}(g)$ | $f \simeq g$ |
| $f = g + O(h)$ | $\mathrm{lead}(f - g) \leq \mathrm{lead}(h)$ | $f \equiv g \pmod{\preceq h}$ |

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

1. **Clean inequality** $\mathrm{lead}(f) \leq \mathrm{lead}(g)$ on
   elements of the ordered group $(\mathbf{No}, +)$.
2. **Algebraic laws**:
   $$
     \mathrm{lead}(f \cdot g) = \mathrm{lead}(f) + \mathrm{lead}(g),
     \qquad
     \mathrm{lead}(f + g) \leq \max(\mathrm{lead}(f), \mathrm{lead}(g))
   $$
   (ultrametric, with equality when leading exponents differ).
3. **Strict refinement by birthday**: when two quantities share a
   leading exponent, the birthday of that exponent —
   `$b(\mathrm{lead}(f))$` — gives an ordinal-valued depth gauge.
   So $\mathrm{lead}(e^{-1/\varepsilon})$ and $\mathrm{lead}(\varepsilon^\omega)$
   are both negative infinite, but at *different birthdays*,
   distinguishing functions that classical Big-O cannot.

## Example rewrites

```
classical:  f(x) = x² + 5x + O(1)  as x → ∞
surreal:    f(x) = x² + 5x + r     where r ≺ 1  (i.e., lead(r) < 0)

classical:  f(q) = g(q) + O((q-1)²)  as q → 1
surreal:    f ≡ g  (mod  ≺ ε²)      i.e., lead(f - g) ≤ -2

classical:  ∫₀¹ e^{-x/ε} dx ∼ ε  as ε → 0⁺
surreal:    ∫₀¹ e^{-x/ε} dx ≃ ε   (leading term and leading coeff agree)
```

## Why it matters for QOU

Three uses specific to the main paper:

1. **CODATA fits.** The $\sim 4\%$ MAE on $\mathcal{Q}$-values is
   a leading-coefficient-level fit. Writing predictions in the form
   $\mathfrak{m}_{\mathfrak{H}} = \hat{\mathfrak{m}}_{\mathfrak{H}}
   + r$ with $r \prec \mathfrak{m}$ makes the *order of the residual*
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

## Lean status

A full formalisation of Conway normal form requires Hahn series
with surreal-valued exponents — partially present in mathlib
(`Mathlib.RingTheory.HahnSeries`) but not yet integrated with
the `SurrealField` axiomatic class. The $\mathrm{lead}$ function
as a group homomorphism can be stated once that integration
lands; meanwhile the valuation-ring structure
([valuation ring](#rem:valuation-ring-finite-surreals)) gives
enough infrastructure to support the asymptotic dictionary at
the level of the standard-part map.
