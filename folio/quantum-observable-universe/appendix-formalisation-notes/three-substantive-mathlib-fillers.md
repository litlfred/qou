**Remark (Three Mathlib gaps).**

The file [`three-substantive-mathlib-fillers.lean`](three-substantive-mathlib-fillers.lean) addresses three Mathlib gaps:

| # | Gap | Lean piece | Status |
|---|---|---|---|
| (1) | `BlochGroup F` quotient | `PreBlochElement F`, `PreBlochGroup F` (FreeAbelianGroup), `HasPentagonRelation F`, `HasBlochGroup F` | structural carrier + class hooks |
| (2) | Pentagon identity for $\mathrm{Cl}_2$ | `Cl_2_PentagonHolds`, `Cl_2_pentagon_at_zero` | definition + class + instance (from Bloch–Wigner five-term) |
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

for $(\alpha, \beta, \gamma, \delta, \varepsilon)$ satisfying the pentagon closure relation: the five points $e^{i\alpha}, \dots, e^{i\varepsilon}$ are the five arguments $x,\ y,\ y/x,\ (1-x^{-1})/(1-y^{-1}),\ (1-x)/(1-y)$ of Suslin's five-term relation. The file provides:

- `cl2PentagonClosure`, that closure condition as a definition.
- `Cl_2_PentagonHolds`, a typeclass with one field asserting the pentagon on that condition. It is inhabited by `instCl_2_PentagonHolds` (`Cl2PentagonFromBlochWigner.lean`). That instance restricts the proved five-term relation of the Bloch–Wigner function $D$ to the unit circle, where $D(e^{i\theta}) = \mathrm{Cl}_2(\theta)$.
- `Cl_2_pentagon_at_zero`, a theorem showing the pentagon holds at the boundary $\mathrm{Cl}_2(0) = 0$.

## (3) Faddeev-Kashaev quasi-classical limit

The relation [$(1{-}q)\,\log\Phi_n(x; q) \to \mathrm{Li}_2(x)$ under $\tau_{\mathrm{arch}}$](#conj:dilogarithm-archimedean-limit) specifies the convergence

$$
  (1 - q) \cdot \log \Phi_n(x; q) \;\to\; \mathrm{Li}_2(x)
$$

along $q \to 1$, $n \to \infty$, and $n(1-q) \to \infty$. The file adds:

- `FaddeevKashaevQuasiClassicalLimit x`, a typeclass for the upstream `ArchimedeanLimit` class. It formalizes the limit from Faddeev (1994) and Kashaev (1997).
- `faddeev_kashaev_at_zero`, a boundary theorem holding by definition at $x = 0$.

## Closed content

The three class hooks provide named carrier infrastructure. The synthesis class `HasAllSubstantiveFillers F` provides a single hypothesis for downstream results. The consistency theorem confirms the synthesis is well-formed.

## Remaining content

The open content comprises two tasks:

1. **An explicit `HasBlochGroup F` instance.** This requires the full `FreeAbelianGroup` quotient construction.
2. **An explicit `FaddeevKashaevQuasiClassicalLimit x` instance for $x \in (0, 1)$.** This requires a uniform Tauberian theorem proof.

The structural scaffolding for these tasks is complete.
