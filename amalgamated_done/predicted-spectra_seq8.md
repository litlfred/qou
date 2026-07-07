<!-- FILE_START: archimedean-hartree-crystal-mass-tower-deeper-intro.md -->
The substrate-flow construction rests on specific categorical structures. The Mathlib fillers identify these structures: the Clausen function, the Bloch-Wigner dilogarithm, and the Bloch-group quotient. The subsequent blocks lift the Faddeev-$\mathrm{Cl}_2$ pentagon identity. They assemble the mass-tower content required for the $\alpha_{\mathrm{EM}}$ derivation.
<!-- FILE_END: archimedean-hartree-crystal-mass-tower-deeper-intro.md -->

<!-- FILE_START: three-substantive-mathlib-fillers.md -->
**Remark (Three Mathlib gaps).**

The file [`three-substantive-mathlib-fillers.lean`](three-substantive-mathlib-fillers.lean) addresses three Mathlib gaps:

| # | Gap | Lean piece | Status |
|---|---|---|---|
| (1) | `BlochGroup F` quotient | `PreBlochElement F`, `PreBlochGroup F` (FreeAbelianGroup), `HasPentagonRelation F`, `HasBlochGroup F` | structural carrier + class hooks |
| (2) | Pentagon identity for $\mathrm{Cl}_2$ | `Cl_2_PentagonHolds`, `Cl_2_pentagon_at_zero` | class hook + boundary theorem |
| (3) | Faddeev-Kashaev quasi-classical limit | `FaddeevKashaevQuasiClassicalLimit x`, `faddeev_kashaev_at_zero` | class hook + boundary theorem |

A synthesis class `HasAllSubstantiveFillers F` collects all three into a single hypothesis. A consistency theorem `three_substantive_fillers_synthesis_consistent` shows this synthesis is structurally well-formed.

## (1) `BlochGroup F`

Downstream files require carrier types and class hooks for the Bloch group. The Lean file provides this structural carrier:

- `PreBlochElement F` is a structure carrying `val : F` with `val ≠ 0` and `val ≠ 1`. These elements generate the Bloch group.
- `PreBlochGroup F := FreeAbelianGroup (PreBlochElement F)` is the free abelian group over the pre-Bloch elements.
- `HasPentagonRelation F` axiomatizes the pentagon-relation subgroup.
- `HasBlochGroup F` axiomatizes the quotient as an abelian group and asserts the Bloch-Wigner regulator.

This construction defers the explicit enumeration of pentagon relations and the proof of the quotient group universal property.

## (2) Pentagon identity for $\mathrm{Cl}_2$

The five-term identity for $\mathrm{Cl}_2$ is the imaginary-part projection of the standard $\mathrm{Li}_2$ pentagon:

$$
  \mathrm{Cl}_2(\alpha) - \mathrm{Cl}_2(\beta) + \mathrm{Cl}_2(\gamma)
   - \mathrm{Cl}_2(\delta) + \mathrm{Cl}_2(\varepsilon) = 0
$$

for $(\alpha, \beta, \gamma, \delta, \varepsilon)$ satisfying the pentagon closure relation. The file provides:

- `Cl_2_PentagonHolds`, a typeclass with two boolean fields. One field asserts the general pentagon. The other asserts the specific instance at $\pi/3$.
- `Cl_2_pentagon_at_zero`, a theorem showing the pentagon holds at the boundary $\mathrm{Cl}_2(0) = 0$.

## (3) Faddeev-Kashaev quasi-classical limit

The relation [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit) specifies the convergence

$$
  (1 - q) \cdot \log \Phi_n(x; q) \;\to\; \mathrm{Li}_2(x)
$$

along $q \to 1$, $n \to \infty$, and $n(1-q) \to \infty$. The file adds:

- `FaddeevKashaevQuasiClassicalLimit x`, a typeclass for the upstream `ArchimedeanLimit` class. It formalizes the limit from Faddeev (1994) and Kashaev (1997).
- `faddeev_kashaev_at_zero`, a boundary theorem holding by definition at $x = 0$.

## Closed content

The three class hooks provide named carrier infrastructure. The synthesis class `HasAllSubstantiveFillers F` provides a single hypothesis for downstream blocks. The consistency theorem confirms the synthesis is well-formed.

## Remaining content

The open content comprises three tasks:

1. **An explicit `HasBlochGroup F` instance.** This requires the full `FreeAbelianGroup` quotient construction.
2. **An explicit `Cl_2_PentagonHolds` instance.** This requires a proof via Fourier-series rearrangements.
3. **An explicit `FaddeevKashaevQuasiClassicalLimit x` instance for $x \in (0, 1)$.** This requires a uniform Tauberian theorem proof.

The structural scaffolding for these tasks is complete.
<!-- FILE_END: three-substantive-mathlib-fillers.md -->

<!-- FILE_START: bloch-group-quotient-construction.md -->
**Proposition (Concrete `BlochGroup F` construction).** The Bloch group `BlochGroup F` for a field-like type `F` admits a concrete Lean construction as the quotient

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

These constraints derive from a valid Rogers pair `(x, y) \in F^\times \times F^\times` with `x \neq y`, `x \neq 0`, `x \neq 1`, `y \neq 0`, and `y \neq 1`. This derivation requires decidability of the pentagon-domain conditions on `F`, a pentagon-shape map `F \times F \to \text{PentagonShape F}`, and the restriction of `pentagonRelationGenerators` to the `ValidPentagonShape F` subtype. The structural skeleton accommodates this restriction via the validity predicate and the constrained range.

The §3b-cond chain anchored by `prop:archimedean-functor-uniqueness` brings `BlochSuslinUniqueness` closer to unconditional inhabitation. The remaining work includes the pentagon identity proof for $\mathrm{Cl}_2$ on the unit-circle subset, Bloch-Wigner regulator $D \otimes \mathbb{Q}$ injectivity, and the Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$.

**Archimedean specialisation (§7c).** The generic $\mathrm{BlochGroup}[\mathrm{Field}\ F]$ construction instantiates the pentagon and Bloch-group relation at $\mathbb{R}$.
<!-- FILE_END: bloch-group-quotient-construction.md -->

<!-- FILE_START: cl2-pentagon-and-faddeev-partial.md -->
**Proposition (Boundary closures).**
*The boundary cases of the $\mathrm{Cl}_2$ pentagon identity and the Faddeev-Kashaev quasi-classical limit are unconditional Lean theorems:*

- *(2-boundary)* `Cl_2(0) - Cl_2(0) + Cl_2(0) - Cl_2(0) + Cl_2(0) = 0` establishes the all-zero-input pentagon.
- *(3-boundary)* For every $(q, n)$, $(1 - q) \cdot \log \Phi_n(0; q) - \mathrm{Li}_2(0) = 0$ establishes the boundary case of the Faddeev-Kashaev limit at $x = 0$.

## Lean theorems

See [Table 1](#tbl:cl2-pentagon-and-faddeev-partial-table1-data).

Proofs proceed by direct rewriting, `simp`, `ring`, and `linarith` on the unconditional building blocks `Cl_2_zero` and `faddeev_limit_at_zero`.

## Closed content

The boundary-case identities are proven Lean theorems. Any future proof of the full pentagon or Tauberian limit must agree with these boundaries. This discharges the consistency requirements for the classes `Cl_2_PentagonHolds` and `FaddeevKashaevQuasiClassicalLimit`.

## Remaining content

The general non-boundary cases contain the primary mathematical content:

See [Table 2](#tbl:cl2-pentagon-and-faddeev-partial-table2-data).

Both remain isolated tasks. The §3b-cond scaffolding is structurally complete. The boundary-case identities are closed in Lean. The open content isolates the upstream Mathlib gap.

## Status

Combined with [`prop:bloch-group-quotient-construction`](#prop:bloch-group-quotient-construction), the three Mathlib gaps have the following status:

See [Table 3](#tbl:cl2-pentagon-and-faddeev-partial-table3-data).

This represents the maximum formalization achievable without upstream Lean analysis infrastructure.
<!-- FILE_END: cl2-pentagon-and-faddeev-partial.md -->

<!-- FILE_START: cl2-pentagon-and-faddeev-partial-novelty.md -->
**Remark.** Extending these relations over non-standard algebraic domains requires consistency boundaries. Resolving the boundary scaffolding for the Faddeev-Kashaev relation anchors the pentagon formulation formally. This establishes the required consistency boundaries.
<!-- FILE_END: cl2-pentagon-and-faddeev-partial-novelty.md -->

<!-- FILE_START: upstream-mathlib-additions.md -->
**Proposition (Upstream Mathlib Additions).**

The file [`upstream-mathlib-additions.lean`](upstream-mathlib-additions.lean) provides three unconditional additions for Mathlib:

See [Table 1](#tbl:upstream-mathlib-additions-table1-data).

## Advances

**(A) `Real.dilog` and `Complex.dilog`.**
The `complexLiTwo` definition implements a concrete `tsum`-based dilogarithm. The $1/k^2$ factor guarantees summability on the closed unit disk. Mathlib provides `Summable` for geometric series. Appending absolute-convergence proofs makes this a candidate Mathlib PR.

**(B) `BlochWigner`.**
The `blochWigner` definition utilizes `Complex.log` and `Complex.arg` from Mathlib. Proving the standard five-term pentagon identity for `blochWigner` closes gap (2). This proof reduces to the absolute convergence of `complexLiTwo` and the Spence-style functional equations for the real and imaginary parts of $\mathrm{Li}_2$.

**(C) $\mathrm{Cl}_2$ functional equations.**
The reflection identity `Cl_2(-θ) = -Cl_2(θ)` is an unconditional Lean theorem. The proof applies `Real.sin_neg` and `tsum_neg`. This establishes the simplest $\mathrm{Cl}_2$ functional equation. Analogous `tsum` rearrangements extend this technique to periodicity identities such as `Cl_2(θ + 2π) = Cl_2(θ)`.

## Target translation

The §3b-cond chain provides unconditional functional identities (`Cl_2_neg`, `complexLiTwo_zero`, `blochWigner_zero`) alongside concrete Lean definitions for `complexLiTwo` and `blochWigner`. This translates a prior axiomatic gap into specific, named Lean targets ready for upstreaming.
<!-- FILE_END: upstream-mathlib-additions.md -->
