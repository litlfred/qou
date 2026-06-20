**Conjecture (conditional on `conj:s5-so3-fiber-action`).** The
canonical inter-nucleon Hecke channel assignment for the atomic
braid word — currently realised as the uniform-flavor map
$\mathrm{pp} \mapsto \sigma$, $\mathrm{nn} \mapsto \sigma^{-1}$,
$\mathrm{pn} \mapsto \sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2$ in
[`isotope_record_schema.py:65{-}70, 176{-}178`](../../computations/isotope_record_schema.py) — is the
**flavor-only projection** of a categorically-refined
*color-tube weighted* assignment derived from the Bring color-tube
structure on the quintic.

## Setup

Each nucleon carries 3 quark color sheets, with quark-flavor content
fixed by the nucleon type:

- **proton** (uud): color sheets $(\mu_u, \mu_u, \mu_d)$
- **neutron** (udd): color sheets $(\mu_u, \mu_d, \mu_d)$

The atomic braid word (per [`prop:atom-knot-exists`](#prop:atom-knot-exists))
places one inter-nucleon Hecke generator at every position $3k + 2$
for each adjacent nucleon pair $k, k+1$ with $k = 0, \ldots, A - 2$
(giving $A - 1$ inter-nucleon arcs total; matches
[`isotope_record_schema.build_knot_operator_catalogue`](../../computations/isotope_record_schema.py)
lines 248-262 and
[`def:canonical-braid-interface-composition`](canonical-braid-interface-composition.md)).
The current production assignment treats each such generator as a
*single* element of the Hecke algebra $H_{3A}(q)$ — one $\sigma$ for
pp, one $\sigma^{-1}$ for nn, one $\sigma_{\mathrm{avg}}$ for pn —
regardless of which flavor triple across the three color sheets is
paired across the inter-nucleon arc.

## The conjectural refinement

Per [`def:color-tube-coordinates`](../archimedean-universe/color-tube-coordinates.md) and
[`def:color-tube-fibers`](../archimedean-universe/color-tube-fibers.md),
Bring's surface carries a canonical
$(r, g, b)$ color-tube fiber structure. The
$S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action on Bring's quintic
(conjectural class supplied by `conj:s5-so3-fiber-action`)
maps each Bring fiber to a 3-dimensional color rotation. Composing
with the nucleon color-sheet assignment above gives a canonical
$3 \times 3 = 9$-element matrix of color-pair couplings per
inter-nucleon arc.

**Conjectured refined assignment.** For each inter-nucleon arc with
nucleon-pair flavor triples
$(F_1, F_2) \in \{u, d\}^3 \times \{u, d\}^3$ across the three
color sheets, the canonical Hecke generator is the
color-sheet-weighted sum

$$
  \sigma^{(F_1, F_2)}_{\text{int}}
  \;=\;
  \sum_{(c_1, c_2) \in \{r, g, b\}^2}
    W_{c_1 c_2}(F_1, F_2) \cdot \sigma^{\epsilon(c_1, c_2, F_1, F_2)}
$$

where:

- $W_{c_1 c_2}(F_1, F_2) \in \mathbb{Q}_{\geq 0}$ is the canonical
  color-sheet pair weight from the $S_{5}$/SO(3) fiber action, **normalised
  to** $\sum_{c_1, c_2} W_{c_1 c_2} = 1$ for each $(F_1, F_2)$ flavor
  pair (so the refined generator is a categorical average over the 9
  color-sheet pairs),
- $\epsilon(c_1, c_2, F_1, F_2) \in \{+1, -1, 0\}$ is the chirality
  sign for the color-sheet pair $(c_1, c_2)$ given the flavor triples
  $(F_1, F_2)$: $+1$ when the flavor at $c_1$ in $F_1$ equals the
  flavor at $c_2$ in $F_2$ (matter–matter), $-1$ when they are
  flavor-conjugate (matter–antimatter), $0$ for mixed-flavor pn
  pairs that average to $\sigma_{\mathrm{avg}}$.

**Uniform-flavor projection.** Setting $W_{c_1 c_2} = 1/9$ uniformly
(the 9-color-sheet-pair average that sums to 1) and collapsing
$\epsilon$ to its flavor-only majority sign reduces to the
current production assignment
($\mathrm{pp} \mapsto \sigma$ via majority same-flavor pairs;
$\mathrm{nn} \mapsto \sigma^{-1}$ via majority opposite-flavor pairs;
$\mathrm{pn} \mapsto \sigma_{\mathrm{avg}}$ via the bar-symmetric
mixed-flavor average).

## Why color-tube weighting is the load-bearing missing structure

The low-isotope sign-flip diagnostic
([`low-isotope-sign-flip-diagnostic.witness.json`](../../computations/low-isotope-sign-flip-diagnostic.witness.json),
PR [#1089](https://github.com/litlfred/qou/pull/1089))
shows that the per-isotope error correlates with inter-nucleon arc
**count** at $R^2 = 0.83$, not with the signed-h weight ($R^2 = 0.26$).
This linear-in-count pattern indicates the **uniform-flavor projection**
is missing a per-arc structural detail — exactly what the color-pair
weight $W_{c_1 c_2}$ would encode.

The empirical match between the (now-purged) $\lambda_{\mathrm{scale}}$
literal $2.4599527869$ and the color-tube Faddeev resummation
$1/(1 - h_q \cdot q_0^{10}) \approx 2.450$ (per
[`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)
§"How canonical includes Yekutieli + Bring together") is independent
evidence that 10-fold color-tube averaging (9 color pairs + 1 diagonal)
is the categorical structure behind the historical numerology.

The probe scripts
[`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py)
and [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py)
(referenced in the cheat-sheet, Phase 5q open finding) report that
Scheme 4 (per-sheet PL integration on Bring's surface with quark-content
weighting) reproduces $\Delta m_{n-p}$ to ${\sim}0.14\%$ — far better
than the uniform-flavor projection's ${\sim}305\,\mathrm{ppm}$ flavor
split ratio. This is third-line evidence that the categorical structure
exists and resolves residuals the uniform-flavor form does not.

## Conditional structure

This conjecture is conditional on
`conj:s5-so3-fiber-action` (PR
[#1081](https://github.com/litlfred/qou/pull/1081) Task 3) being
formalised as a Lean class. Once that class is available, the
weight matrix $W_{c_1 c_2}$ should be derivable as a tensor in the
SO(3)-fiber data over Bring, with no remaining degrees of freedom —
the conjecture would then promote to a `proposition` block under
the AGENTS.md §3b-cond conditional-class convention.

The block remains a `conjecture` until then.

## Lean axiomatisation (sketch)

```lean
-- Conditional on the S₅↔SO(3) fiber-action class:
class InterNucleonChannelColorTube
    (M : Type*) [BrCategory M] [ColorTube M] [S5SO3Fiber M] where
  /-- Per-arc canonical Hecke generator for (color-pair, nucleon-pair). -/
  hecke_of_color_pair :
    NucleonColorPair → HeckeAlgebra M
  /-- The flavor-only projection (current production rule) is the
      categorical average of `hecke_of_color_pair` over the 9 color
      pairs of the (nucleon₁, nucleon₂) flavor type. -/
  flavor_projection_compatibility :
    ∀ (C₁ C₂ : NucleonColorContent),
      avg_over_color_pairs (hecke_of_color_pair (C₁, C₂))
        = flavor_only_hecke (flavor_of C₁) (flavor_of C₂)
```

The class is *inhabited* by the $S_{5}$/SO(3) fiber data once
`conj:s5-so3-fiber-action` lands; until
then the instance carries an explicit `sorry` per AGENTS.md §3b
("class is inhabited") policy.

## Consumers

- [`isotope_record_schema.py`](../../computations/isotope_record_schema.py)
  — current uniform-flavor rule lives in
  `build_knot_operator_catalogue` lines 190-262
- [`mass_table_comprehensive.py`](../../computations/mass_table_comprehensive.py)
  — would replace per-channel canonical-form labels with color-tube-weighted forms
- [`closed_form_tau_M.py`](../../computations/closed_form_tau_M.py)
  — currently raises `NotImplementedError` when invoked with
  `pn_convention="bring_color_weighted"`; this conjecture supplies
  the categorical infrastructure that, once formalised, lets that
  code path return a definite value

## Open questions

1. **Closed form for $W_{c_1 c_2}$.** What are the exact rational weights
   from the SO(3)-fiber tensor over Bring? Numerical probes give
   $W \in \{1/3, 2/3, \ldots\}$ but the canonical formula needs the
   formalised class.
2. **Color-pair $\to$ chirality sign $\epsilon$ rule.** Why is
   same-color $\mapsto +1$, opposite-color $\mapsto -1$? Is this from
   CPT symmetry on the color sheets, or from a finer $S_{5}$ orbit
   decomposition? Partially constrained: $\epsilon$ must be a section of
   the $\mathbb{Z}_2$ kernel of the double cover $\mathrm{SU}(2) \to
   \mathrm{SO}(3)$ (see
   §"Representation-theoretic constraint on $\epsilon$"); the residual
   open content is the fiber-to-color assignment.
3. **${}^{4}\mathrm{He}$ magic-shell saturation.** Does the color-tube weighting
   saturate at $A = 4$ (filled-shell analogue), producing the
   $A \cdot 8G$ closure observed in
   [`isotope_record_schema.py:186`](../../computations/isotope_record_schema.py)?
   See [`docs/audits/-4he-magic-shell-color-tube-audit.md`](../../docs/audits/-4he-magic-shell-color-tube-audit.md).
4. **Cross-check $\rho_F$ density rule.** Does color-tube weighting
   give a categorical reading of the Kashaev density factor
   $\rho_F \in \{m_e, 2 m_e\}$? See
   [`docs/audits/-rule14-kashaev-density.md`](../../docs/audits/-rule14-kashaev-density.md).

## Representation-theoretic constraint on $\epsilon$

The chirality sign $\epsilon(c_1, c_2, F_1, F_2) \in \{+1, -1, 0\}$ in the
refined assignment is not free: it is constrained by the
$\mathrm{SO}(3) = \mathrm{SU}(2)/\mathbb{Z}_2$ level structure. The
$\mathbb{Z}_2$ kernel of the covering map $\mathrm{SU}(2) \to
\mathrm{SO}(3)$ is exactly the two-element group whose non-trivial
element acts as $-1$ on half-integer-spin (spinorial) irreps and $+1$
on integer-spin (tensor) irreps. The chirality dichotomy
$\{+1, -1\}$ the $S_5/\mathrm{SO}(3)$ fiber action must supply is
therefore the **grading by this $\mathbb{Z}_2$**, and the neutral value
$0$ (the bar-symmetric $\mathrm{pn}$ average) is the $\mathbb{Z}_2$-fixed
locus.

This grading has a closed formal handle. With $q = e^{\eta}$, the
$\mathrm{SU}(2)_q$ doublet character is $[2]_q = 2\cosh\eta$ and the
lowest $\mathrm{SO}(3)_q$ (integer-spin) character is the adjoint
$[3]_q$, satisfying the Chebyshev/Clebsch–Gordan square identity

$$
  [3]_q \;=\; [2]_q^{\,2} - 1,
$$

formalised (sorry-free) as `so3_adjoint_eq_chebyshev` in
[`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6. The
$\mathrm{SO}(3)$ characters are exactly the polynomials in $[2]_q$ that
are invariant under the $\mathbb{Z}_2$ that the square map quotients;
any admissible $\epsilon$ rule must be a section of this same
$\mathbb{Z}_2$-grading. This **narrows** the conjectural class — a valid
$\epsilon$ cannot assign $-1$ to a color-sheet pair whose combined
flavor content sits in the integer-spin (tensor) sector — but it does
**not** close it: the explicit map from color-sheet pairs $(c_1, c_2)$
to the $\mathbb{Z}_2$-grade still requires the $S_5 \leftrightarrow
\mathrm{SO}(3)$ fiber action of `conj:s5-so3-fiber-action`. The
representation-theoretic level structure is unconditional; the
*fiber-to-color* assignment remains the conjectural input.

## Cross-references

- Parent sign-flip audit:
  [`docs/audits/-sign-flip-interpretation.md`](../../docs/audits/-sign-flip-interpretation.md)
- ${}^{4}\mathrm{He}$ magic-shell color-tube reading:
  [`docs/audits/-4he-magic-shell-color-tube-audit.md`](../../docs/audits/-4he-magic-shell-color-tube-audit.md)
- Bring color-tube weighted averaging cheat-sheet entry:
  [`docs/canonical-derivation-cheat-sheet.md` §"Bring color-tube weighted averaging"](../../docs/canonical-derivation-cheat-sheet.md)
- Existing color-tube infrastructure:
  [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md),
  [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md),
  [`color-tube-cubic.md`](../archimedean-universe/color-tube-cubic.md)
- Supplier class (PR
  [#1081](https://github.com/litlfred/qou/pull/1081) Task 3):
  `conj:s5-so3-fiber-action`
- $\mathrm{SO}(3)_q = \mathrm{SU}(2)_q/\mathbb{Z}_2$ level structure
  (formal handle for the $\epsilon$ grading):
  [`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6
  (`so3_adjoint_eq_chebyshev`)
- Empirical probe scripts:
  [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py),
  [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py)
