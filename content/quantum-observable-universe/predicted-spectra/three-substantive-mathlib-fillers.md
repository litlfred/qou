**Remark (three substantive Mathlib gaps — partial fillings).**

Per the user request "1 2 3 please", three substantive Mathlib
gaps are addressed in
[`three-substantive-mathlib-fillers.lean`](three-substantive-mathlib-fillers.lean):

| # | Gap | Lean piece | Status |
|---|---|---|---|
| (1) | `BlochGroup F` quotient | `PreBlochElement F`, `PreBlochGroup F` (FreeAbelianGroup), `HasPentagonRelation F`, `HasBlochGroup F` | structural carrier + class hooks |
| (2) | Pentagon identity for $\mathrm{Cl}_2$ | `Cl_2_PentagonHolds`, `Cl_2_pentagon_at_zero` | class hook + sanity-check theorem at boundary |
| (3) | Faddeev-Kashaev quasi-classical limit | `FaddeevKashaevQuasiClassicalLimit x`, `faddeev_kashaev_at_zero` | class hook + boundary theorem |

Plus a synthesis class `HasAllSubstantiveFillers F` collecting all
three into a single §3b-cond hypothesis, and a consistency theorem
`three_substantive_fillers_synthesis_consistent` showing the
synthesis is structurally well-formed.

## (1) `BlochGroup F` — concrete carrier

The Lean file gives a **structural carrier** for the Bloch group:

- `PreBlochElement F` — a structure carrying `val : F` with
 `val ≠ 0` and `val ≠ 1`. These are the elements on which the
 Bloch group is built.
- `PreBlochGroup F := FreeAbelianGroup (PreBlochElement F)` —
 Mathlib's `FreeAbelianGroup` over the pre-Bloch elements.
- `HasPentagonRelation F` typeclass — axiomatises the existence
 of the pentagon-relation sub-additive-group.
- `HasBlochGroup F` typeclass — axiomatises the quotient as an
 abelian group plus the existence of the Bloch-Wigner regulator.

This is **not** the full ~150-line construction (which would
explicitly enumerate the pentagon relations, prove the quotient
group's universal property, and connect it to the Suslin map).
But it provides the carrier types and class hooks downstream
files can reference, leaving the substantive content as
`HasBlochGroup F` instance closure — a Mathlib-contribution-sized
task isolating exactly what's missing.

## (2) Pentagon identity for $\mathrm{Cl}_2$

The 5-term identity for $\mathrm{Cl}_2$ is the imaginary-part
projection of the standard $\mathrm{Li}_2$ pentagon. Stated as

$$
  \mathrm{Cl}_2(\alpha) - \mathrm{Cl}_2(\beta) + \mathrm{Cl}_2(\gamma)
   - \mathrm{Cl}_2(\delta) + \mathrm{Cl}_2(\varepsilon) = 0
$$

for $(\alpha, \beta, \gamma, \delta, \varepsilon)$ satisfying the
pentagon closure relation. The full Lean proof requires Mathlib's
sine-series rearrangement infrastructure. We provide:

- `Cl_2_PentagonHolds` typeclass with two boolean fields (general
 pentagon + the specific instance at $\pi/3$).
- `Cl_2_pentagon_at_zero` — sorry-free sanity-check theorem
 showing the pentagon is consistent with the boundary lemma
 $\mathrm{Cl}_2(0) = 0$ (by definition, $5 \cdot \mathrm{Cl}_2(0) = 0$).

## (3) Faddeev-Kashaev quasi-classical limit

The convergence

$$
  (1 - q) \cdot \log \Phi_n(x; q) \;\to\; \mathrm{Li}_2(x)
$$

along $q \to 1, n \to \infty, n(1-q) \to \infty$ is the substantive
content of [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit).
This file adds:

- `FaddeevKashaevQuasiClassicalLimit x` typeclass — surrogate for
 the upstream `ArchimedeanLimit` class with explicit named
 reference to Faddeev 1994 / Kashaev 1997.
- `faddeev_kashaev_at_zero` — sorry-free boundary theorem
 (holds by definition at $x = 0$ since both sides are identically zero
 there).

## Content fully closed by this file

The three §3b-cond class hooks are now formally available with
named carrier infrastructure for downstream usage. None of the
substantive content is closed unconditionally — that requires
either Mathlib upstream contributions or the ~150-line
construction that this file explicitly defers.

The synthesis class `HasAllSubstantiveFillers F` provides a
single §3b-cond hypothesis that downstream blocks can take in
their `[Instance]` lists; the consistency theorem confirms the
synthesis is structurally well-formed.

## Remaining content

After this file, the open content is exactly:

1. **An explicit `HasBlochGroup F` instance** — full FreeAbelianGroup
 quotient construction, ~150 lines.
2. **An explicit `Cl_2_PentagonHolds` instance** — proof via
 Mathlib Fourier-series rearrangements once those are available.
3. **An explicit `FaddeevKashaevQuasiClassicalLimit x` instance
 for $x \in (0, 1)$** — uniform Tauberian theorem proof.

Each is a separate, well-isolated mathematical task. The §3b-cond
scaffolding is structurally complete; the residual mathematical
work has known shape and known references.
