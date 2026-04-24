This remark proposes an explicit notational convention unifying
Big-O / little-o / $\Theta$ / $\sim$ under the surreal $\omega$-adic
valuation $\Ow$
([Conway normal form](#rem:conway-normal-form)).

## Proposed convention for QOU

The ω-adic order $\Ow : \mathbf{No}^\times \to \mathbf{No}$ is the
leading exponent in the Conway normal form. Introduce four binary
relations on $\mathbf{No}^\times$ corresponding to asymptotic
classes:

| Relation | Meaning | Classical equivalent |
|---|---|---|
| $f \preceq g$ | $\Ow(f) \leq \Ow(g)$ | $f = O(g)$ |
| $f \prec g$ | $\Ow(f) < \Ow(g)$ | $f = o(g)$ |
| $f \asymp g$ | $\Ow(f) = \Ow(g)$ | $f = \Theta(g)$ |
| $f \simeq g$ | $\Ow(f) = \Ow(g)$ and $\mathrm{lc}(f) = \mathrm{lc}(g)$ | $f \sim g$ |
| $f \equiv g \pmod{\preceq h}$ | $\Ow(f - g) \leq \Ow(h)$ | $f = g + O(h)$ |

These symbols are all standard LaTeX: $\preceq$, $\prec$,
$\asymp$, $\simeq$. No new macros needed beyond $\Ow$ (added to
the paper manifest).

## Why adopt this

The equivalence between Big-O and valuation inequality is not new
— it is the content of the non-archimedean valuation interpretation
of asymptotics (Hardy, du Bois-Reymond, later Berarducci–Mantova).
What is new, and specific to a QOU revision, is that:

1. **The paper already uses $\omega$ as the first infinite
   surreal** (implicitly in limits, explicitly in
   [blow-up calculus](#def:surreal-blowup-calculus)), so
   $\Ow$ is already the natural invariant.

2. **The paper's existing $\mathrm{ord}_{\mathbb{F}_p^\times}$
   notation** (in $q$-logarithm and $q$-dilogarithm blocks)
   sets a precedent for subscripted-order functions. $\Ow$
   slots in cleanly.

3. **Big-O appears informally throughout** the main paper when
   discussing MAE residuals, quantum corrections,
   classical-limit approximations, and spectral gap behaviour.
   Making these leading-exponent-explicit sharpens each claim.

## Main-paper macro

Registered in the paper manifest
([quantum-observable-universe.ts](#sec:paper-manifest)):

```ts
macros: {
  // ω-adic Big-O / leading-exponent class (Conway normal form).
  Ow: { tex: "O_{\\omega}", unicode: "O_ω" },
  // (existing macros remain unchanged)
}
```

Usage in `.md`: `$\Ow(f) \leq \Ow(g)$`.

Effect on rendered LaTeX: `$O_\omega(f) \leq O_\omega(g)$`.

The symbol is Big-O flavored because, as the table above makes
explicit, $\Ow$ is the valuation that encodes the classical Big-O
relation: $f = O(g) \Leftrightarrow \Ow(f) \leq \Ow(g)$. Little-o
is the same valuation under strict inequality. The prose name —
"ω-adic order" — is retained; only the typeset symbol changes.

## Migration guide (for future paper revisions)

When adopting this convention in the main paper, the standard
rewriting rules are:

```
$f = O(g)$                        →  $f \preceq g$
$f = o(g)$                        →  $f \prec g$
$f = \Theta(g)$                   →  $f \asymp g$
$f \sim g$                        →  $f \simeq g$
$f = g + O(h)$                    →  $f \equiv g \pmod{\preceq h}$
$\lim_{n\to\infty} a_n / b_n = 1$ →  $a_\omega \simeq b_\omega$
$\lim_{n\to\infty} a_n / b_n = 0$ →  $a_\omega \prec b_\omega$
```

The LHS remains valid notation (standard) — it is not deprecated.
The RHS is an opt-in *sharpening* that makes the leading exponent
explicit.

## Birthday refinement

When two quantities share a leading exponent, further resolution
comes from the **birthday** of that exponent. Define:

$$
  f \asymp_\alpha g \quad :\Leftrightarrow \quad
  \Ow(f) = \Ow(g) \text{ and } b(\Ow(f)) \leq \alpha.
$$

For finite-birthday ($\alpha \leq \omega$) this is the archimedean
asymptotic class. For transfinite $\alpha$, this separates e.g.
$e^{-1/\varepsilon}$ from $\varepsilon^\omega$ — two functions that
are $\Theta$ of each other in the classical sense but have
distinct surreal birthdays.

## What this does NOT propose

- It does not replace any theorem in the main paper.
- It does not change any numerical prediction.
- It does not deprecate classical Big-O; that notation remains
  valid for citations and legacy cross-references.
- It does not require mathlib's Hahn series to be integrated with
  `SurrealField` — the dictionary is stated even at the level of
  the standard-part projection.

## Summary

$\preceq, \prec, \asymp, \simeq$ are the natural surreal
asymptotic relations; $\Ow$ is their underlying invariant; both
are algebraic cleanings of Big-O / little-o / $\Theta$ / $\sim$.
A one-line macro addition to the paper manifest suffices to make
$\Ow$ available paper-wide.
