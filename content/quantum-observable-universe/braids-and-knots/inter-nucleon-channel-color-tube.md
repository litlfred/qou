**Conjecture (conditional on `conj:s5-so3-fiber-action`).** The
canonical inter-nucleon Hecke channel assignment for the atomic
braid word — currently realised as the uniform-flavor map
$\mathrm{pp} \mapsto \sigma$, $\mathrm{nn} \mapsto \sigma^{-1}$,
$\mathrm{pn} \mapsto \sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2$ in
[`isotope_record_schema.py:65{-}70, 176{-}178`](../../folio-assistant/computations/isotope_record_schema.py) — is the
**flavor-only projection** of a categorically-refined
*color-tube weighted* assignment derived from the Bring color-tube
structure on the quintic.

## Setup

Each nucleon carries 3 quark color sheets, with quark-flavor content
fixed by the nucleon type:

- **proton** (uud): color sheets $(\mu_u, \mu_u, \mu_d)$
- **neutron** (udd): color sheets $(\mu_u, \mu_d, \mu_d)$

The atomic braid word (per [`def:atom-knot-exists`](#def:atom-knot-exists))
places one inter-nucleon Hecke generator at every position $3k + 2$
($k = 0, \ldots, A - 1$). The current production assignment treats
each such generator as a *single* element of the Hecke algebra
$H_{3A}(q)$ — one $\sigma$ for pp, one $\sigma^{-1}$ for nn, one
$\sigma_{\mathrm{avg}}$ for pn — regardless of which quark-color sheets
are paired across the inter-nucleon arc.

## The conjectural refinement

Per [`def:color-tube-coordinates`](../archimedean-universe/color-tube-coordinates.md) and
[`def:color-tube-fibers`](../archimedean-universe/color-tube-fibers.md),
Bring's surface carries a canonical
$(r, g, b)$ color-tube fiber structure. The
$S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action on Bring's quintic
(conjectural class supplied by [`conj:s5-so3-fiber-action`](#conj:s5-so3-fiber-action))
maps each Bring fiber to a 3-dimensional color rotation. Composing
with the nucleon color-sheet assignment above gives a canonical
$3 \times 3 = 9$-element matrix of color-pair couplings per
inter-nucleon arc.

**Conjectured refined assignment.** For each inter-nucleon arc with
nucleon-pair colors $(C_1, C_2) \in \{u, d\}^3 \times \{u, d\}^3$,
the canonical Hecke generator is the color-pair-weighted sum

$$
  \sigma^{(C_1, C_2)}_{\text{int}}
  \;=\;
  \sum_{(c_1, c_2) \in C_1 \times C_2}
    W_{c_1 c_2} \cdot \sigma^{\epsilon(c_1, c_2)}
$$

where:

- $W_{c_1 c_2} \in \mathbb{Q}$ is the canonical color-pair weight from
  the S₅/SO(3) fiber action (sum to 9 over each $(C_1, C_2)$ pair),
- $\epsilon(c_1, c_2) \in \{+1, -1, 0\}$ is the chirality sign assigned
  to the $(c_1, c_2)$ color pair: $+1$ for same-color (matter–matter),
  $-1$ for opposite-color (matter–antimatter), $0$ for averaged
  (mixed-flavor pn pairs).

**Uniform-flavor projection.** Setting $W_{c_1 c_2} = 1/9$ uniformly
and collapsing $\epsilon$ to its flavor-only average reduces to the
current production assignment
($\mathrm{pp} \mapsto \sigma$ via 9 same-color pairs;
$\mathrm{nn} \mapsto \sigma^{-1}$ via 9 opposite-color;
$\mathrm{pn} \mapsto \sigma_{\mathrm{avg}}$ via 3 same + 6 different).

## Why color-tube weighting is the load-bearing missing structure

The low-isotope sign-flip diagnostic
([`low-isotope-sign-flip-diagnostic.witness.json`](../../folio-assistant/computations/low-isotope-sign-flip-diagnostic.witness.json),
PR [#1089](https://github.com/litlfred/qou/pull/1089))
shows that the per-isotope error correlates with inter-nucleon arc
**count** at $R^2 = 0.83$, not with the signed-h weight ($R^2 = 0.26$).
This linear-in-count pattern indicates the **uniform-flavor projection**
is missing a per-arc structural detail — exactly what the color-pair
weight $W_{c_1 c_2}$ would encode.

The empirical match between the (now-purged) $\lambda_{\mathrm{scale}}$
literal $2.4599527869$ and the color-tube Faddeev resummation
$1/(1 - h_q \cdot q_0^{10}) \approx 2.450$ (per
[`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../../docs/audits/2026-05-23-lambda-scale-canonical-unification.md)
§"How canonical includes Yekutieli + Bring together") is independent
evidence that 10-fold color-tube averaging (9 color pairs + 1 diagonal)
is the categorical structure behind the historical numerology.

The probe scripts
[`probe_pn_flavor_asymmetry.py`](../../folio-assistant/computations/probe_pn_flavor_asymmetry.py)
and [`probe_per_sheet_flavor_nonin.py`](../../folio-assistant/computations/probe_per_sheet_flavor_nonin.py)
(referenced in the cheat-sheet, Phase 5q open finding) report that
Scheme 4 (per-sheet PL integration on Bring's surface with quark-content
weighting) reproduces $\Delta m_{n-p}$ to ${\sim}0.14\%$ — far better
than the uniform-flavor projection's ${\sim}305\,\mathrm{ppm}$ flavor
split ratio. This is third-line evidence that the categorical structure
exists and resolves residuals the uniform-flavor form does not.

## Conditional structure

This conjecture is conditional on
[`conj:s5-so3-fiber-action`](#conj:s5-so3-fiber-action) (PR
[#1081](https://github.com/litlfred/qou/pull/1081) Task 3) being
formalised as a Lean class. Once that class is available, the
weight matrix $W_{c_1 c_2}$ should be derivable as a tensor in the
SO(3)-fiber data over Bring, with no remaining degrees of freedom —
the conjecture would then promote to a `proposition` block under
the CLAUDE.md §3b-cond conditional-class convention.

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

The class is *inhabited* by the S₅/SO(3) fiber data once
[`conj:s5-so3-fiber-action`](#conj:s5-so3-fiber-action) lands; until
then the instance carries an explicit `sorry` per CLAUDE.md §3b
("class is inhabited") policy.

## Consumers

- [`isotope_record_schema.py`](../../folio-assistant/computations/isotope_record_schema.py)
  — current uniform-flavor rule lives in
  `build_knot_operator_catalogue` lines 190-262
- [`mass_table_comprehensive.py`](../../folio-assistant/computations/mass_table_comprehensive.py)
  — would replace per-channel canonical-form labels with color-tube-weighted forms
- [`closed_form_tau_M.py`](../../folio-assistant/computations/closed_form_tau_M.py)
  — exposes `pn_convention="bring_color_weighted"` as a
  `NotImplementedError` placeholder; this conjecture is the
  categorical infrastructure that, once formalised, removes the
  placeholder

## Open questions

1. **Closed form for $W_{c_1 c_2}$.** What are the exact rational weights
   from the SO(3)-fiber tensor over Bring? Numerical probes give
   $W \in \{1/3, 2/3, \ldots\}$ but the canonical formula needs the
   formalised class.
2. **Color-pair $\to$ chirality sign $\epsilon$ rule.** Why is
   same-color $\mapsto +1$, opposite-color $\mapsto -1$? Is this from
   CPT symmetry on the color sheets, or from a finer S₅ orbit
   decomposition?
3. **⁴He magic-shell saturation.** Does the color-tube weighting
   saturate at $A = 4$ (filled-shell analogue), producing the
   $A \cdot 8G$ closure observed in
   [`isotope_record_schema.py:186`](../../folio-assistant/computations/isotope_record_schema.py)?
   See [`docs/audits/2026-05-24-4he-magic-shell-color-tube-audit.md`](../../docs/audits/2026-05-24-4he-magic-shell-color-tube-audit.md).
4. **Cross-check $\rho_F$ density rule.** Does color-tube weighting
   give a categorical reading of the Kashaev density factor
   $\rho_F \in \{m_e, 2 m_e\}$? See
   [`docs/audits/2026-05-24-rule14-kashaev-density.md`](../../docs/audits/2026-05-24-rule14-kashaev-density.md).

## Cross-references

- Parent sign-flip audit:
  [`docs/audits/2026-05-24-sign-flip-interpretation.md`](../../docs/audits/2026-05-24-sign-flip-interpretation.md)
- ⁴He magic-shell color-tube reading:
  [`docs/audits/2026-05-24-4he-magic-shell-color-tube-audit.md`](../../docs/audits/2026-05-24-4he-magic-shell-color-tube-audit.md)
- Bring color-tube weighted averaging cheat-sheet entry:
  [`docs/canonical-derivation-cheat-sheet.md` §"Bring color-tube weighted averaging"](../../docs/canonical-derivation-cheat-sheet.md)
- Existing color-tube infrastructure:
  [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md),
  [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md),
  [`color-tube-cubic.md`](../archimedean-universe/color-tube-cubic.md)
- Supplier class (PR
  [#1081](https://github.com/litlfred/qou/pull/1081) Task 3):
  `conj:s5-so3-fiber-action`
- Empirical probe scripts:
  [`probe_pn_flavor_asymmetry.py`](../../folio-assistant/computations/probe_pn_flavor_asymmetry.py),
  [`probe_per_sheet_flavor_nonin.py`](../../folio-assistant/computations/probe_per_sheet_flavor_nonin.py)
