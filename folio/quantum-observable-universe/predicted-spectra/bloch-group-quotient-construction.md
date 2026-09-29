The Bloch group `BlochGroup F` for a field-like type `F` admits a concrete Lean construction as the quotient

$$
  B(F) \;:=\; \mathrm{FreeAbelianGroup}\bigl(\mathrm{PreBlochElement}\,F\bigr)
            \;\big/\; \mathrm{pentagonSubgroup},
$$

where `PreBlochElement F` carries the pre-Bloch elements (`val ≠ 0` and `val ≠ 1`) and `pentagonSubgroup` is the `AddSubgroup.closure` of the five-term pentagon-relation generators. The quotient inherits an `AddCommGroup` structure from the `QuotientAddGroup` instance in Mathlib. It carries a canonical projection `quot : PreBlochGroup F →+ BlochGroup F` and satisfies the standard universal property.

See [Table](#tbl:bloch-group-quotient-construction-table-data) for the Lean structure.

This construction yields a genuine `AddCommGroup` rather than a typeclass ansatz. The carrier types admit a real Lean construction. The `HasBlochGroup ℝ` instance is concretely inhabited.

The unconstrained `PentagonShape F` accepts arbitrary five-tuples of pre-Bloch elements. This makes `pentagonRelationGenerators` too permissive. Degenerate shapes with repeated entries trivialize the quotient. A `ValidPentagonShape F` predicate must constrain `PentagonShape F` to enforce the Rogers-form constraints:

$$
  e_3 \;\equiv\; e_2 / e_1, \quad
  e_4 \;\equiv\; (1 - e_2^{-1})/(1 - e_1^{-1}), \quad
  e_5 \;\equiv\; (1 - e_2)/(1 - e_1).
$$

These constraints derive from a valid Rogers pair
$(x, y) \in F^\times \times F^\times$ with $x \neq y$, $x \neq 0$,
$x \neq 1$, $y \neq 0$, and $y \neq 1$. This derivation requires
decidability of the pentagon-domain conditions on $F$, a pentagon-shape
map $F \times F \to \mathrm{PentagonShape}\,F$, and the restriction of
`pentagonRelationGenerators` to the `ValidPentagonShape F` subtype. The structural skeleton accommodates this restriction via the validity predicate and the constrained range.

The conditional-class chain anchored by `prop:archimedean-functor-uniqueness` brings `BlochSuslinUniqueness` closer to unconditional inhabitation. The remaining work includes the pentagon identity proof for $\mathrm{Cl}_2$ on the unit-circle subset, Bloch-Wigner regulator $D \otimes \mathbb{Q}$ injectivity, and the Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$.

**Archimedean specialisation.** The generic $\mathrm{BlochGroup}[\mathrm{Field}\ F]$ construction instantiates the pentagon and Bloch-group relation at $\mathbb{R}$.
