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
