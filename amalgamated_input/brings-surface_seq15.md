<!-- FILE_START: brings-surface-orphan-reconnect-intro.md -->
These blocks were reconnected during the Phase 7 orphan audit. They address supplementary Bring's-surface results awaiting thematic placement.
<!-- FILE_END: brings-surface-orphan-reconnect-intro.md -->

<!-- FILE_START: bring-fibre-q0-figure.md -->
**Figure (Bring chiral fibre near a branch point of the discriminant).**

*Two-panel illustration of the chiral elliptic fibre structure of Bring's surface in the $q \to 0$ regime. At this categorical big-bang scale, sheet-merging monodromy dominates.*

The cubic $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$ is the canonical chiral cubic from Bring's invariant ring over the spacetime affine chart $z = x_0/x_1 \in \mathbb{CP}^1$. Its discriminant $\Delta(z) = 18bcd - 4b^3 d + b^2 c^2 - 4 c^3 - 27 d^2$ (with $b = z+1$, $c = z^2+z+1$, $d = z^3+z^2+z+1$) vanishes at exactly six points in $\mathbb{C}$. Newton-Raphson on a $200 \times 200$ grid over $|z| \le 3$ locates them: $z \approx (0.119, \pm 1.054)$, $(0.106, \pm 0.937)$, $(-0.975, \pm 0.223)$.

The chosen branch point for the right panel is the one of smallest $|z|$. Among the six discriminant zeros, the pair $z \approx (0.106, \pm 0.937i)$ has $|z| \approx 0.943$. This is smaller than $|-0.975 + 0.223i| \approx 1.000$. We select the negative-imaginary representative $z_c \approx 0.106 - 0.937i$ (see the `branch_point_chosen` field in the witness). As $z$ circles $z_c$ at radius $0.15$, exactly two of the three sheets merge. This is the $B_3$-monodromy fingerprint. The third sheet remains well-separated. We draw the merging sheets in matched line styles (solid and dashed) and the isolated sheet in dotted.

We generate this figure programmatically via [`bring_chiral_fibre_figure.py`](../../../computations/bring_chiral_fibre_figure.py). We record parameters and verified sample values in [`bring-chiral-fibre-figure.witness.json`](../../../computations/bring-chiral-fibre-figure.witness.json).
<!-- FILE_END: bring-fibre-q0-figure.md -->

<!-- FILE_START: bring-fibre-qhalf-figure.md -->
**Figure (Bring chiral fibre along a real segment, intermediate regime).**

*Companion to [fig:bring-fibre-q0](#fig:bring-fibre-q0). Two-panel illustration of the chiral fibre structure away from any branch point in the intermediate $q = \tfrac{1}{2}$ regime, where all three sheets remain well-separated.*

The cubic and base match [fig:bring-fibre-q0](#fig:bring-fibre-q0). We evaluate along the real segment $z \in [-0.5, 1.5]$. This segment lies outside any neighbourhood of the six branch points $z \approx (0.119, \pm 1.054)$, $(0.106, \pm 0.937)$, $(-0.975, \pm 0.223)$. The cubic has one real root $X_{\text{real}}$ and a complex-conjugate pair $X_{\text{conj},1}$, $X_{\text{conj},2} = \overline{X_{\text{conj},1}}$.

The right-hand stacked sub-plots show Re$(X)$ (top) and Im$(X)$ (bottom) versus $z$ along the segment. The real sheet (solid) appears in Re-only with Im $\equiv 0$. The conjugate pair (dashed and dotted) have opposite imaginary parts and matching real parts.

We generate this via [`bring_chiral_fibre_figure.py`](../../../computations/bring_chiral_fibre_figure.py), witnessed by [`bring-chiral-fibre-figure.witness.json`](../../../computations/bring-chiral-fibre-figure.witness.json).
<!-- FILE_END: bring-fibre-qhalf-figure.md -->

<!-- FILE_START: inter-nucleon-channel-color-tube.md -->
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

## Color-tube weighting as the load-bearing missing structure

The low-isotope sign-flip diagnostic ([`low-isotope-sign-flip-diagnostic.witness.json`](../../computations/low-isotope-sign-flip-diagnostic.witness.json), PR [#1089](https://github.com/litlfred/qou/pull/1089)) shows that the per-isotope error correlates with inter-nucleon arc **count** at $R^2 = 0.83$, not with the signed-h weight ($R^2 = 0.26$). This indicates the **uniform-flavor projection** is missing a per-arc structural detail. The color-pair weight $W_{c_1 c_2}$ encodes exactly this detail.

The empirical match between the (now-purged) $\lambda_{\mathrm{scale}}$ literal $2.4599527869$ and the color-tube Faddeev resummation $1/(1 - h_q \cdot q_0^{10}) \approx 2.450$ (per [`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)) provides independent evidence that 10-fold color-tube averaging is the categorical structure behind the historical numerology.

Probe scripts [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py) and [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py) report that Scheme 4 (per-sheet PL integration on Bring's surface with quark-content weighting) reproduces $\Delta m_{n-p}$ to ${\sim}0.14\%$. This dramatically improves on the uniform-flavor projection's ${\sim}305\,\mathrm{ppm}$ flavor split ratio.

The **gg-production collapse** isolates the cost of the projection directly. Decomposing the production binding $B_{\mathrm{sym}} = \alpha\,\ln(\mathrm{tr}_{\mathrm{free}}/\mathrm{tr}_{\mathrm{atom}})$ into its per-bond log-suppressions $L_{\mathrm{pp}}, L_{\mathrm{pn}}, L_{\mathrm{nn}}$ at $q_0$ gives $L_{\mathrm{nn}}/L_{\mathrm{pp}} - 1 \approx 78\%$ ([`charge-symmetry-bond-probe.witness.json`](../../computations/probes/charge-symmetry-bond-probe.witness.json)). This represents roughly $570\times$ the substrate-derived $p/n$ flavor split $\delta_{\mathrm{lead}} \approx 0.14\%$ and $78\times$ the experimental charge-symmetry-breaking bound. This over-break derives entirely from the $\sigma$-vs-$\sigma^{-1}$ inter-crossing sign of the flavor-only projection. Gluons couple color, not flavor. The leading gg interface is the single flavor-blind color-average $\sigma_{\mathrm{avg}} = \sigma - (h/2)\cdot 1$ for every bond type. Forcing all inter-nucleon crossings to $\sigma_{\mathrm{avg}}$ collapses the $78\%$ asymmetry to $0$ ([`gg-production-bond-probe.witness.json`](../../computations/probes/gg-production-bond-probe.witness.json)). The sub-leading flavor weighting $W_{c_1 c_2}$ reintroduces the correct $\delta_{\mathrm{lead}}$-scale split. The uniform-flavor projection manufactures an $O(1)$ charge asymmetry that the color-tube average removes.

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

## Open questions

1. **Closed form for $W_{c_1 c_2}$.** What are the exact rational weights from the SO(3)-fiber tensor over Bring?
2. **Color-pair $\to$ chirality sign $\epsilon$ rule.** Why is same-color $\mapsto +1$, opposite-color $\mapsto -1$?
3. **${}^{4}\mathrm{He}$ magic-shell saturation.** Does the color-tube weighting saturate at $A = 4$ (filled-shell analogue), producing the $A \cdot 8G$ closure observed in [`isotope_record_schema.py:186`](../../computations/isotope_record_schema.py)?
4. **Cross-check $\rho_F$ density rule.** Does color-tube weighting yield a categorical reading of the Kashaev density factor $\rho_F \in \{m_e, 2 m_e\}$?

## Representation-theoretic constraint on $\epsilon$

The chirality sign $\epsilon(c_1, c_2, F_1, F_2) \in \{+1, -1, 0\}$ is constrained by the $\mathrm{SO}(3) = \mathrm{SU}(2)/\mathbb{Z}_2$ level structure. The $\mathbb{Z}_2$ kernel of the covering map $\mathrm{SU}(2) \to \mathrm{SO}(3)$ acts as $-1$ on half-integer-spin (spinorial) irreps and $+1$ on integer-spin (tensor) irreps. The chirality dichotomy $\{+1, -1\}$ from the $S_5/\mathrm{SO}(3)$ fiber action supplies this **grading by this $\mathbb{Z}_2$**. The neutral value $0$ (the bar-symmetric $\mathrm{pn}$ average) identifies the $\mathbb{Z}_2$-fixed locus.

With $q = e^{\eta}$, the $\mathrm{SU}(2)_q$ doublet character is $[2]_q = 2\cosh\eta$ and the lowest $\mathrm{SO}(3)_q$ (integer-spin) character is the adjoint $[3]_q$. They satisfy the Chebyshev/Clebsch–Gordan square identity

$$
  [3]_q \;=\; [2]_q^{\,2} - 1,
$$

formalised as `so3_adjoint_eq_chebyshev` in [`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6. The $\mathrm{SO}(3)$ characters are exactly the polynomials in $[2]_q$ invariant under the $\mathbb{Z}_2$ quotient. Any admissible $\epsilon$ rule must be a section of this same $\mathbb{Z}_2$-grading. A valid $\epsilon$ cannot assign $-1$ to a color-sheet pair whose combined flavor content sits in the integer-spin (tensor) sector. The explicit map from color-sheet pairs $(c_1, c_2)$ to the $\mathbb{Z}_2$-grade still requires the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action of `conj:s5-so3-fiber-action`.

## Cross-references

- Parent sign-flip audit: [`docs/audits/-sign-flip-interpretation.md`](../../docs/audits/-sign-flip-interpretation.md)
- ${}^{4}\mathrm{He}$ magic-shell color-tube reading: [`docs/audits/-4he-magic-shell-color-tube-audit.md`](../../docs/audits/-4he-magic-shell-color-tube-audit.md)
- Bring color-tube weighted averaging cheat-sheet entry: [`docs/canonical-derivation-cheat-sheet.md` §"Bring color-tube weighted averaging"](../../docs/canonical-derivation-cheat-sheet.md)
- Existing color-tube infrastructure: [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md), [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md), [`color-tube-cubic.md`](../archimedean-universe/color-tube-cubic.md)
- Supplier class (PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3): `conj:s5-so3-fiber-action`
- $\mathrm{SO}(3)_q = \mathrm{SU}(2)_q/\mathbb{Z}_2$ level structure: [`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6 (`so3_adjoint_eq_chebyshev`)
- Empirical probe scripts: [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py), [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py)
<!-- FILE_END: inter-nucleon-channel-color-tube.md -->

<!-- FILE_START: c-from-color-flavor-swap.md -->
**Conjecture (D6 charge-conjugation closure, conditional on [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube)).**
*Within the QOU framework, charge conjugation $C$ acts as the **flavor swap on color sheets** that exchanges each quark flavor with its antimatter-conjugate:*

$$
  C \;:\;
  \begin{cases}
    u \;\longleftrightarrow\; \bar u, \\
    d \;\longleftrightarrow\; \bar d,
  \end{cases}
$$

*applied independently to each of the three color sheets of every nucleon-coloured braid strand. The proton flavor triple $(u, u, d)$ maps to $(\bar u, \bar u, \bar d)$ (the antiproton); the neutron flavor triple $(u, d, d)$ maps to $(\bar u, \bar d, \bar d)$ (the antineutron). $C$ is an involution ($C^2 = \mathrm{id}$) and commutes with the color-tube weighted averaging of [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube).*

## Disentanglement of D6 from CPT

[`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) formalises the **composite** CPT action. The framework historically collapses C, P, T into the single bar-involution [`def:bar-involution`](#def:bar-involution) on Hecke generators ($q \mapsto q^{-1}$ together with $\sigma_i \mapsto \sigma_i^{-1}$). That conflation suppresses the **distinct categorical sources** of the three discrete symmetries:

| Symmetry | Categorical source | Acts on |
|----------|--------------------|---------|
| **C** (this conjecture) | flavor swap on color sheets | quark-flavor content of nucleon braid strands |
| **P** | mirror reflection of braid diagram | writhe / signed-crossing classification ([`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)) |
| **T** | Markov-trace word reversal | trace-cyclicity dual |

The bar-involution $q \mapsto q^{-1}$, $\sigma_i \mapsto \sigma_i^{-1}$ acts as the **composite CPT** in this categorisation, not as C alone. This conjecture locates the C-component on the color sheets—orthogonal to P (braid-diagram mirror) and T (trace reversal).

## The conjectural content

The proposition relies on the color-sheet flavor structure established in [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube). Specifically:

1. **C is well-defined.** The flavor-content map $(F_1, F_2) \mapsto (\bar F_1, \bar F_2)$ commutes with the color-tube weight tensor $W_{c_1 c_2}(F_1, F_2)$—i.e. $W_{c_1 c_2}(\bar F_1, \bar F_2) = W_{c_1 c_2}(F_1, F_2)$ (the weights are flavor-conjugation invariant).
2. **C is an involution.** Each color sheet flips back to its original flavor under two applications.
3. **C commutes with bar-involution on the algebraic side.** This forces $\mathrm{CP} \cdot \mathrm{T}$ and $\mathrm{C} \cdot \mathrm{PT}$ to reduce to the bar-involution identity classified in [`bar-involution.md`](bar-involution.md) §Bar-symmetric.

When all three hold, $C$ constitutes the well-defined Z/2 categorical symmetry on the color-sheet flavor data. The CPT composite of [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) factors as $\mathrm{CPT} = C \cdot P \cdot T$ in the natural order—three commuting Z/2 actions on the color-tube structure.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: N/A—claim addresses a Z/2 categorical symmetry on color-sheet metadata, not Hecke elements at a particular Coxeter length.
- **Jet order**: $h^0$ (the C-action is independent of $q$; the flavor-conjugation map forms a structural Z/2 lifting through the color-tube tensor).
- **Bar-symmetry status**: $C$ is bar-symmetric. It preserves $q$ and commutes with $\sigma_i \leftrightarrow \sigma_i$ (it acts on color-sheet labels, not on Hecke generators). C composed with PT yields the bar-involution. C itself is bar-trivial in [`bar-involution-table4-data`](bar-involution.md#tbl:bar-involution-table4-data).

## Lean axiomatisation (sketch)

```lean
-- Conditional on the color-tube channel-assignment class:
class CFromColorFlavorSwap
    (M : Type*) [BrCategory M] [ColorTube M]
    [InterNucleonChannelColorTube M] where
  /-- The Z/2 flavor-conjugation involution on color-sheet flavors. -/
  c_action : ColorSheetFlavor → ColorSheetFlavor
  /-- C^2 = id. -/
  c_involution : ∀ f, c_action (c_action f) = f
  /-- C commutes with the color-tube weight tensor (flavors are
      conjugation invariant). -/
  c_commutes_W :
    ∀ (F₁ F₂ : NucleonFlavorContent) (c₁ c₂ : ColorSheet),
      color_tube_weight (c_action F₁) (c_action F₂) c₁ c₂
        = color_tube_weight F₁ F₂ c₁ c₂
  /-- CPT factorisation: C · P · T = bar-involution. -/
  cpt_factorisation :
    bar_involution = c_action ∘ p_braid_mirror ∘ t_trace_reverse
```

The class becomes inhabited by the color-tube data once [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube) is instantiated.

## Consumers / downstream

- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) becomes a corollary of $\mathrm{CPT} = C \cdot P \cdot T$ once D6, D7, D8 close.
- The matter/antimatter sheet structure on Bring's quintic surface ([`def:color-tube-fibers`](color-tube-fibers.md)) acquires a natural C-action that descends to the SO(3) fiber.
- Type-B folding for chirality / CPT (AGENTS.md §7b, **D22** in the duality tracker) emerges as the symmetric-crystal analogue of this conjecture. Folding the $\mathfrak{sl}_n$ Cartan datum to Type B realises C as a symmetric-crystal structure.

## Open R&D

1. **Compute prototype**: `verify_c_color_swap.py`—verify numerically at $q_0$ that the flavor-conjugation involution on the proton/neutron color-tube tensor leaves the canonical Hecke generator invariant.
2. **Close D7 and D8**—author `conj:p-from-braid-mirror` and `conj:t-from-trace-cyclicity` to complete the CPT decomposition.
3. **Promote to proposition** once [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube) and the $S_{5}$$\leftrightarrow$SO(3) fiber-action class (PR [#1081](https://github.com/litlfred/qou/pull/1081) supplier) resolve.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D6 (this conjecture) + §2 Cluster A (CPT decomposition D5 $\to$ D6 + D7 + D8)
- Upstream class: [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube) (PR [#1111](https://github.com/litlfred/qou/pull/1111) merged)
- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) (CPT composite already formalised)
- [`bar-involution.md`](bar-involution.md)—the bar-involution = CPT composite identification at the algebraic level
- AGENTS.md §7b—Type-B folding for chirality / CPT (symmetric-crystal authoring shortcut, D22)
<!-- FILE_END: c-from-color-flavor-swap.md -->

<!-- FILE_START: outro-brings-surface.md -->
This closes the Bring's-surface chapter. The archimedean base—the genus-4 surface $\mathcal{E}_q$ with Euler characteristic $\chi = -6$—functions as the QOU spacetime. We fixed the Descartes / archimedean condition via the genus-ideal characterisation. We assembled the colour-tube coordinates and spectral gauge. The reconnected orphan blocks wire the surface-level constructions to the substrate-arithmetic of the preceding chapters.

The climax chapter on volume-mass duality pairs the hyperbolic-volume content of Bring's surface with the categorical mass content extracted from the eigenbasis. The subsequent chapters specialise the resulting duality to atomic isotopes and the $\beta$-decay $Q$-value predictions.
<!-- FILE_END: outro-brings-surface.md -->

