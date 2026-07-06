**Proposition (Concrete `BlochGroup F` construction).** The Bloch group `BlochGroup F` for a field-like type `F` admits a concrete Lean construction as the quotient

$$
  B(F) \;:=\; \mathrm{FreeAbelianGroup}\bigl(\mathrm{PreBlochElement}\,F\bigr)
            \;\big/\; \mathrm{pentagonSubgroup},
$$

where `PreBlochElement F` carries the pre-Bloch elements (`val ≠ 0 ∧ val ≠ 1`) and `pentagonSubgroup` is the `AddSubgroup.closure` of the 5-term pentagon-relation generators. The quotient inherits an `AddCommGroup` structure from Mathlib's `QuotientAddGroup` instance, with a canonical projection `quot : PreBlochGroup F →+ BlochGroup F` and the standard universal property.

See [Table](#tbl:bloch-group-quotient-construction-table-data) for the Lean structure.

This construction closes a substantive Mathlib gap. The carrier types are backed by a real Lean construction, making `BlochGroup F` a genuine `AddCommGroup` rather than a typeclass ansatz. The `HasBlochGroup ℝ` instance is concretely inhabited.

The current `PentagonShape F` accepts arbitrary 5-tuples of pre-Bloch elements, making `pentagonRelationGenerators` too permissive. Degenerate shapes with repeated entries trivialise the quotient. We must constrain `PentagonShape F` via a `ValidPentagonShape F` predicate enforcing the Rogers-form constraints:

$$
  e_3 \;\equiv\; e_2 / e_1, \quad
  e_4 \;\equiv\; (1 - e_2^{-1})/(1 - e_1^{-1}), \quad
  e_5 \;\equiv\; (1 - e_2)/(1 - e_1).
$$

These derive from a valid Rogers pair `(x, y) \in F^\times \times F^\times` with `x \neq y, x \neq 0, x \neq 1, y \neq 0, y \neq 1`. This requires decidability of the pentagon-domain conditions on `F`, a pentagon-shape map `F \times F \to \text{PentagonShape F}`, and restricting `pentagonRelationGenerators` over the `ValidPentagonShape F` subtype. The structural skeleton accommodates this via the validity predicate and constrained range.

The §3b-cond chain anchored by `prop:archimedean-functor-uniqueness` brings `BlochSuslinUniqueness` closer to unconditional inhabitation. The remaining work includes the pentagon identity proof for $\mathrm{Cl}_2$ on the unit-circle subset, Bloch-Wigner regulator $D \otimes \mathbb{Q}$ injectivity, and the Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$.

**Archimedean specialisation (§7c).** The generic $\mathrm{BlochGroup}[\mathrm{Field}\ F]$ construction instantiates the pentagon and Bloch-group relation at $\mathbb{R}$.
