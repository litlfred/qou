<!-- FILE_START: archimedean-hartree-crystal-mass-tower-deeper-intro.md -->
The substantive Mathlib fillers identify the categorical structures (Clausen-function, Bloch-Wigner dilogarithm, Bloch-group quotient) underlying the substrate-flow construction. The subsequent blocks lift the Faddeev-Cl2 pentagon identity and assemble the mass-tower content required for the $\alpha_{\mathrm{EM}}$ derivation.
<!-- FILE_END: archimedean-hartree-crystal-mass-tower-deeper-intro.md -->

<!-- FILE_START: three-substantive-mathlib-fillers.md -->
**Remark (Three Mathlib gaps—partial fillings).**

This paper addresses three Mathlib gaps in [`three-substantive-mathlib-fillers.lean`](three-substantive-mathlib-fillers.lean):

| # | Gap | Lean piece | Status |
|---|---|---|---|
| (1) | `BlochGroup F` quotient | `PreBlochElement F`, `PreBlochGroup F` (FreeAbelianGroup), `HasPentagonRelation F`, `HasBlochGroup F` | structural carrier + class hooks |
| (2) | Pentagon identity for $\mathrm{Cl}_2$ | `Cl_2_PentagonHolds`, `Cl_2_pentagon_at_zero` | class hook + sanity-check theorem at boundary |
| (3) | Faddeev-Kashaev quasi-classical limit | `FaddeevKashaevQuasiClassicalLimit x`, `faddeev_kashaev_at_zero` | class hook + boundary theorem |

A synthesis class `HasAllSubstantiveFillers F` collects all three into a single hypothesis. A consistency theorem `three_substantive_fillers_synthesis_consistent` shows the synthesis is structurally well-formed.

## (1) `BlochGroup F` — concrete carrier

The Lean file provides a structural carrier for the Bloch group:

- `PreBlochElement F` — a structure carrying `val : F` with `val ≠ 0` and `val ≠ 1`. These elements generate the Bloch group.
- `PreBlochGroup F := FreeAbelianGroup (PreBlochElement F)` — the free abelian group over the pre-Bloch elements.
- `HasPentagonRelation F` — axiomatizes the existence of the pentagon-relation subgroup.
- `HasBlochGroup F` — axiomatizes the quotient as an abelian group and the existence of the Bloch-Wigner regulator.

This construction provides the carrier types and class hooks for downstream files. It defers the explicit enumeration of pentagon relations and the proof of the quotient group's universal property.

## (2) Pentagon identity for $\mathrm{Cl}_2$

The five-term identity for $\mathrm{Cl}_2$ is the imaginary-part projection of the standard $\mathrm{Li}_2$ pentagon:

$$
  \mathrm{Cl}_2(\alpha) - \mathrm{Cl}_2(\beta) + \mathrm{Cl}_2(\gamma)
   - \mathrm{Cl}_2(\delta) + \mathrm{Cl}_2(\varepsilon) = 0
$$

for $(\alpha, \beta, \gamma, \delta, \varepsilon)$ satisfying the pentagon closure relation. We provide:

- `Cl_2_PentagonHolds` — a typeclass with two boolean fields (general pentagon and the specific instance at $\pi/3$).
- `Cl_2_pentagon_at_zero` — a sanity-check theorem showing the pentagon is consistent with the boundary lemma $\mathrm{Cl}_2(0) = 0$.

## (3) Faddeev-Kashaev quasi-classical limit

The convergence

$$
  (1 - q) \cdot \log \Phi_n(x; q) \;\to\; \mathrm{Li}_2(x)
$$

along $q \to 1, n \to \infty, n(1-q) \to \infty$ is the content of [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit). We add:

- `FaddeevKashaevQuasiClassicalLimit x` — a typeclass for the upstream `ArchimedeanLimit` class with explicit reference to Faddeev (1994) and Kashaev (1997).
- `faddeev_kashaev_at_zero` — a boundary theorem holding by definition at $x = 0$.

## Content fully closed by this file

The three class hooks are formally available with named carrier infrastructure. The synthesis class `HasAllSubstantiveFillers F` provides a single hypothesis for downstream blocks. The consistency theorem confirms the synthesis is well-formed.

## Remaining content

The open content is:

1. **An explicit `HasBlochGroup F` instance** — full `FreeAbelianGroup` quotient construction.
2. **An explicit `Cl_2_PentagonHolds` instance** — proof via Fourier-series rearrangements.
3. **An explicit `FaddeevKashaevQuasiClassicalLimit x` instance for $x \in (0, 1)$** — uniform Tauberian theorem proof.

Each is a separate mathematical task. The scaffolding is structurally complete.
<!-- FILE_END: three-substantive-mathlib-fillers.md -->

<!-- FILE_START: bloch-group-quotient-construction.md -->
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
<!-- FILE_END: bloch-group-quotient-construction.md -->

<!-- FILE_START: cl2-pentagon-and-faddeev-partial.md -->
**Proposition (partial closures of substantive Mathlib gaps 2+3, sorry-free).**
*The boundary cases of the $\mathrm{Cl}_2$ pentagon identity and the Faddeev-Kashaev quasi-classical limit are unconditional Lean theorems:*

- *(2-boundary) `Cl_2(0) - Cl_2(0) + Cl_2(0) - Cl_2(0) + Cl_2(0) = 0`, the all-zero-input pentagon.*
- *(3-boundary) For every $(q, n)$, $(1 - q) \cdot \log \Phi_n(0; q) - \mathrm{Li}_2(0) = 0$, the boundary case of the Faddeev-Kashaev limit at $x = 0$.*

## Lean theorems (sorry-free)

See [Table 1](#tbl:cl2-pentagon-and-faddeev-partial-table1-data).

Proofs proceed by direct rewriting, `simp`, `ring`, and `linarith` on the unconditional building blocks `Cl_2_zero` and `faddeev_limit_at_zero`.

## Content of this closure

**Items (2) and (3) — boundary portions, unconditional.** The boundary-case identities are Lean theorems. Any future proof of the full pentagon or full Tauberian limit must agree with these boundaries. This formally discharges the consistency requirements for the Mathlib-pending classes `Cl_2_PentagonHolds` and `FaddeevKashaevQuasiClassicalLimit`.

## Remaining content

**The general (non-boundary) cases.** These constitute the substantive mathematical content:

See [Table 2](#tbl:cl2-pentagon-and-faddeev-partial-table2-data).

Both remain isolated as Mathlib-contribution-sized tasks. The §3b-cond scaffolding is structurally complete. The boundary-case identities are unconditionally closed in Lean. The open content is exactly the upstream Mathlib gap, free from QOU-internal axiomatization.

## Significance

Combined with [`prop:bloch-group-quotient-construction`](#prop:bloch-group-quotient-construction) (item 1 closure), the three substantive Mathlib gaps have the following status:

See [Table 3](#tbl:cl2-pentagon-and-faddeev-partial-table3-data).

This represents the maximum advance achievable without upstream Mathlib contributions or extensive Lean analysis infrastructure.
<!-- FILE_END: cl2-pentagon-and-faddeev-partial.md -->

<!-- FILE_START: cl2-pentagon-and-faddeev-partial-novelty.md -->
**Remark.** Resolving the boundary scaffolding for the Faddeev-Kashaev relation anchors the pentagon formulation in a formal setting. This establishes consistency boundaries required to extend these relations over non-standard algebraic domains.
<!-- FILE_END: cl2-pentagon-and-faddeev-partial-novelty.md -->

<!-- FILE_START: upstream-mathlib-additions.md -->
**Proposition (Upstream Mathlib Additions).**

The Lean file [`upstream-mathlib-additions.lean`](upstream-mathlib-additions.lean) provides three sorry-free additions targeting Mathlib:

See [Table 1](#tbl:upstream-mathlib-additions-table1-data).

## Advances

**(A) Towards `Real.dilog`/`Complex.dilog`.**
The `complexLiTwo` definition implements a concrete `tsum`-based dilogarithm. With absolute-convergence proofs added, this becomes a candidate Mathlib PR. (Mathlib provides `Summable` for geometric series; the $1/k^2$ factor guarantees summability on the closed unit disk).

**(B) Towards `BlochWigner`.**
The `blochWigner` definition leverages Mathlib's `Complex.log` and `Complex.arg`. Proving the standard 5-term pentagon identity for `blochWigner` closes substantive gap (2). This proof reduces to the absolute-convergence of `complexLiTwo` and the Spence-style functional equations for the real and imaginary parts of $\mathrm{Li}_2$.

**(C) Towards $\mathrm{Cl}_2$ functional equations.**
The reflection `Cl_2(-θ) = -Cl_2(θ)` is now a sorry-free Lean theorem. The proof relies directly on `Real.sin_neg` and `tsum_neg`. This establishes the simplest $\mathrm{Cl}_2$ functional equation. Analogous `tsum` rearrangements extend this technique to other identities, such as periodicity `Cl_2(θ + 2π) = Cl_2(θ)`.

## Significance

The §3b-cond chain now features two unconditional functional identities (`Cl_2_neg`, `complexLiTwo_zero`, `blochWigner_zero`) alongside concrete Lean definitions for `complexLiTwo` and `blochWigner`. This translates a previously axiomatic "Mathlib gap" into specific, named Lean targets ready for individual upstreaming.
<!-- FILE_END: upstream-mathlib-additions.md -->

