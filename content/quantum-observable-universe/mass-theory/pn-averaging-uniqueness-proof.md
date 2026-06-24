The uniqueness is staged with the §3b-cond conditional-class pattern: the
three structural hypotheses are named as Lean classes on a p-n averaging
form $\sigma_{pn} : R \to R$, and the conclusion is derived from them.

Let $\sigma_{pn}, \sigma_{pn}'$ both satisfy

- **bar-invariance** $\mathrm{BarInvariant}$: $\sigma_{pn}(q) = \sigma_{pn}(q^{-1})$,
- **color-flavor compatibility** $\mathrm{ColorFlavorCompatible}$ (Bring
  color-tube symmetry over quark composition),
- **standard normalisation** $\mathrm{StandardNorm}(z)$: $\sigma_{pn}(q) = z(q)$
  pointwise, with the *same* normalising form $z$.

The equality is immediate from the normalisation hypothesis alone: for
every $q$,
$$
\sigma_{pn}(q) = z(q) = \sigma_{pn}'(q),
$$
so $\sigma_{pn} = \sigma_{pn}'$ by function extensionality
(`pn_averaging_unique`; the subsingleton packaging
`pn_averaging_subsingleton` records that the set of forms normalised by a
fixed $z$ has at most one element). No fitting and no empirical input
enter: once the three structural conditions are named, the averaging
functional is pinned.

The work the other two hypotheses do is *upstream* of this step — they
constrain which normalising form $z$ is admissible. Bar-invariance forces
$z(q) = z(q^{-1})$, and color-flavor compatibility refines $z$ to the
canonical Bring color-weighted form; the variant
`pn_averaging_unique_via_weight` runs the same uniqueness argument through
the color-pair weight. The genuine open content is the
$\mathrm{ColorFlavorCompatible}$ class instance — the per-quark color
weighting derivation (Phase 5q) — on which this proposition is therefore
conditional per AGENTS.md §3b-cond. Everything downstream of the named
classes is verified by Lean, sorry-free. $\qquad\blacksquare$
