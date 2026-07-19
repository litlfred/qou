**Conjecture (conditional on `conj:s5-so3-fiber-action`).** The canonical inter-nucleon Hecke channel assignment for the atomic braid word—currently realised as the uniform-flavor map $\mathrm{pp} \mapsto \sigma$, $\mathrm{nn} \mapsto \sigma^{-1}$, $\mathrm{pn} \mapsto \sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2$ in [`isotope_record_schema.py:65{-}70, 176{-}178`](../../computations/isotope_record_schema.py)—is the **flavor-only projection** of a categorically-refined *color-tube weighted* assignment derived from the Bring color-tube structure on the quintic.

## Setup

Each nucleon carries 3 quark color sheets. The nucleon type fixes the quark-flavor content:

- **proton** (uud): color sheets $(\mu_u, \mu_u, \mu_d)$
- **neutron** (udd): color sheets $(\mu_u, \mu_d, \mu_d)$

The atomic braid word ([`prop:atom-knot-exists`](#prop:atom-knot-exists)) places one inter-nucleon Hecke generator at every position $3k + 2$ for each adjacent nucleon pair $k, k+1$ with $k = 0, \ldots, A - 2$. This gives $A - 1$ inter-nucleon arcs total (matching [`isotope_record_schema.build_knot_operator_catalogue`](../../computations/isotope_record_schema.py) lines 248-262 and [`def:canonical-braid-interface-composition`](canonical-braid-interface-composition.md)). The current production assignment treats each such generator as a single element of the Hecke algebra $H_{3A}(q)$—one $\sigma$ for pp, one $\sigma^{-1}$ for nn, one $\sigma_{\mathrm{avg}}$ for pn—regardless of which flavor triple across the three color sheets pairs across the inter-nucleon arc.

## The conjectural refinement

Per [`def:color-tube-coordinates`](../archimedean-universe/color-tube-coordinates.md) and [`def:color-tube-fibers`](../archimedean-universe/color-tube-fibers.md), Bring's surface carries a canonical $(r, g, b)$ color-tube fiber structure. The $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action on Bring's quintic (conjectural class supplied by `conj:s5-so3-fiber-action`) maps each Bring fiber to a 3-dimensional color rotation. Composing with the nucleon color-sheet assignment gives a canonical $3 \times 3 = 9$-element matrix of color-pair couplings per inter-nucleon arc.

**Conjectured refined assignment.** For each inter-nucleon arc with nucleon-pair flavor triples $(F_1, F_2) \in \{u, d\}^3 \times \{u, d\}^3$ across the three color sheets, the canonical Hecke generator is the color-sheet-weighted sum

$$
  \sigma^{(F_1, F_2)}_{\text{int}}
  \;=\;
  \sum_{(c_1, c_2) \in \{r, g, b\}^2}
    W_{c_1 c_2}(F_1, F_2) \cdot \sigma^{\epsilon(c_1, c_2, F_1, F_2)}
$$

where:

- $W_{c_1 c_2}(F_1, F_2) \in \mathbb{Q}_{\geq 0}$ is the canonical color-sheet pair weight from the $S_{5}$/SO(3) fiber action, **normalised to** $\sum_{c_1, c_2} W_{c_1 c_2} = 1$ for each $(F_1, F_2)$ flavor pair (so the refined generator is a categorical average over the 9 color-sheet pairs).
- $\epsilon(c_1, c_2, F_1, F_2) \in \{+1, -1, 0\}$ is the chirality sign for the color-sheet pair $(c_1, c_2)$ given the flavor triples $(F_1, F_2)$. It is $+1$ when the flavor at $c_1$ in $F_1$ equals the flavor at $c_2$ in $F_2$ (matter–matter). It is $-1$ when they are flavor-conjugate (matter–antimatter). It is $0$ for mixed-flavor pn pairs that average to $\sigma_{\mathrm{avg}}$.

**Uniform-flavor projection.** Setting $W_{c_1 c_2} = 1/9$ uniformly and collapsing $\epsilon$ to its flavor-only majority sign recovers the current production assignment.

## Conditional structure

This conjecture remains conditional on `conj:s5-so3-fiber-action` (PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3) being formalised as a Lean class. Once available, the weight matrix $W_{c_1 c_2}$ derives as a tensor in the SO(3)-fiber data over Bring, with no remaining degrees of freedom. The conjecture will then promote to a `proposition` block under the AGENTS.md §3b-cond conditional-class convention.

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

The class becomes inhabited by the $S_{5}$/SO(3) fiber data once `conj:s5-so3-fiber-action` lands.

## Consumers

- [`probes/charge_symmetry_bond_probe.py`](../../computations/probes/charge_symmetry_bond_probe.py)
- [`probes/gg_production_bond_probe.py`](../../computations/probes/gg_production_bond_probe.py)
- [`isotope_record_schema.py`](../../computations/isotope_record_schema.py)
- [`mass_table_comprehensive.py`](../../computations/mass_table_comprehensive.py)
- [`closed_form_tau_M.py`](../../computations/closed_form_tau_M.py)

## Cross-references

- Existing color-tube infrastructure: [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md), [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md), [`color-tube-cubic.md`](../archimedean-universe/color-tube-cubic.md)
- Supplier class (PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3): `conj:s5-so3-fiber-action`
