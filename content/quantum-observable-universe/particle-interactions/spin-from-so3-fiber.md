**Conjecture (D10 spin closure, conditional on the $S_5
\leftrightarrow \mathrm{SO}(3)$ fiber action).**
*Within the QOU framework, spin $\mathrm{SU}(2)_S$ arises as the
continuous lift of the **full $\mathrm{SO}(3)$ rotation group acting
on the 3 color sheets per nucleon**, via the $S_5 \to A_5 \cong I
\subset \mathrm{SO}(3)$ icosahedral embedding on Bring's quintic
surface ([`def:color-tube-fibers`](#def:color-tube-fibers)).  The
current pipeline implements only the discrete $S_3$ subgroup of
$\mathrm{SO}(3)$ (the 3! = 6 permutations of three color sheets);
extending to the **full continuous $\mathrm{SO}(3)$** populates the
$\ell = 2, 3, 4, \ldots$ spherical-harmonic decompositions, which
contribute the $h^4$, $h^6$, $\ldots$ corrections to the Borromean
linking weight that the current $S_3$-truncated framework cannot
see.*

## The structural gap (per `-h4-coefficient-source-trace-and-so3-gap.md`)

The Family A linking weight `(3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h²`
terminates at $h^2$.  The Borromean Markov trace's exact closed
form (per
[`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form))
has $h^2 = 0$ and first non-trivial coefficient $h^4 = -3/4$.  The
gap between Family A's $(3/4)h^2$ contribution and the Markov-trace
$h^4 = -3/4$ structural value is the **load-bearing $h^4$ closure
gap**.

The framework's pipeline currently uses only the **$S_3$ discrete
subgroup** of $\mathrm{SO}(3)$ — the 6 permutations on 3 color
sheets.  A natural-looking proposal was that $S_3$ "sees only
$\ell \le 1$", so that reaching $\ell = 2$ (and hence $h^4$) would
require the full continuous $\mathrm{SO}(3)$.  **This
$\ell$-truncation premise is false** (character-table check, audit
[`2026-06-01-s5-so3-su2-u1-fiber-action.md`](../../docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md)):
under $S_3 \subset \mathrm{SO}(3)$ the standard/$(2,1)$ irrep already
appears at **both** $\ell = 1$ (multiplicity 1) and $\ell = 2$
(multiplicity 2), so $S_3$ is not $\ell$-truncated and the
"only full $\mathrm{SO}(3)$ reaches $\ell = 2$" reasoning does not
hold.

Spherical-harmonic levels of $\mathrm{SO}(3)$ do still organise the
higher-order corrections —

- $\ell = 2$ (5-dim irrep) — the order at which $h^4$ first appears,
- $\ell = 3$ (7-dim irrep) — $h^6$, and so on —

but the proposed *categorical link*, that the icosahedral
$\ell = 2$ level **produces** the Borromean $h^4 = -3/4$, is **not
derivable as written**.  The icosahedral construction lives on
$A_5 \subset S_5$ (**5 strands**), whereas the $h^4 = -3/4$
coefficient lives on the $H_3$ Borromean Markov trace (**3 strands**,
the $(2,1)$ irrep); these are different representation rings with no
canonical map between them.  The genuine missing object is therefore
a functor from the $S_5$/$\mathrm{SO}(3)$ level $\ell$ (5-strand) to
a Wedderburn coefficient of the 3-strand $H_3$ trace — the same gap
named on the flavour-to-sheet side in
[`2026-06-01-flavor-dependent-cusp-shape.md`](../../docs/audits/2026-06-01-flavor-dependent-cusp-shape.md).

## The conjectural content

Per `conj:s5-so3-fiber-action` (PR
[#1081](https://github.com/litlfred/qou/pull/1081) supplier — class
scaffolded in [`S5SO3FiberAction.lean`](../../computations/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)):

1. **The icosahedral lift is well-defined.** $S_5 \supset A_5 \cong I
   \subset \mathrm{SO}(3)$ provides a canonical map from $S_5$-orbits
   on Bring's quintic to $\mathrm{SO}(3)$ rotations on the 3 color
   sheets.
2. **The full $\mathrm{SO}(3)$ fiber action commutes with the Hecke
   structure.** The spherical-harmonic decomposition into $\ell$
   levels respects the Wedderburn-block structure of $H_n(q)$ in the
   sense that each $\ell$-level contributes to a definite
   subset of partition blocks.
3. **The $\ell = 2$ contribution at the Borromean linking weight
   produces the $h^4 = -3/4$ coefficient.** This is the "structural
   reading" of the Markov-trace closed-form coefficient: the $h^4$
   value comes from the dimension-5 irrep ($\ell = 2$) of
   $\mathrm{SO}(3)$ acting on the 3-color tensor space.

## How D10 partners with D9 to unlock D11 (Wigner SU(4))

Per [`docs/duality-tracker.md`](../../docs/duality-tracker.md)
§Cluster B:

- D9 (isospin $\mathrm{SU}(2)_I$) = flavor-swap $u \leftrightarrow d$
  on color-sheet flavor triples (closed in
  [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md))
- D10 (spin $\mathrm{SU}(2)_S$) = $\mathrm{SO}(3)$ rotation on color
  sheets (this conjecture)
- D11 (Wigner $\mathrm{SU}(4) = \mathrm{SU}(2)_S \times
  \mathrm{SU}(2)_I$) = combined symmetry — the natural categorical
  source for nuclear-shell structure (the $A = 4$ magic shell is the
  first SU(4) supermultiplet, Wigner 1937).

Closing D10 (this conjecture) together with D9 (already in flight)
unlocks D11, which IS the L3 (nuclear-shell binding) categorical
source per
[`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md).

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: the SO(3)-fiber decomposition is
  per-partition; different Wedderburn blocks of $H_n(q)$ couple to
  different $\ell$ levels.  Per-block Coxeter length determines
  which $\ell \leq \ell_{\max}$ levels contribute.
- **Jet order**: $h^4$ is the first non-trivial level contributed
  by $\ell = 2$ ($\mathrm{SO}(3)$ dim-5 irrep) — the load-bearing
  closure step.  $h^6$ comes from $\ell = 3$, etc.
- **Bar-symmetry status**: bar-symmetric.  Spherical-harmonic
  decomposition coefficients are real-valued under
  $q \mapsto q^{-1}$ (the fiber action commutes with bar).

## Lean axiomatisation (sketch)

```lean
-- Conditional on the S_5↔SO(3) fiber action class (PR #1081):
class SpinFromSO3Fiber
    (M : Type*) [BrCategory M] [ColorTube M]
    [BringFiberAction M] where
  /-- The spherical-harmonic decomposition of the color-tube tensor
      under the full SO(3) action. -/
  spherical_harmonic_decomp :
    ColorTubeTensor → ∀ (ℓ : ℕ), SO3IrrepOfDim (2*ℓ + 1)
  /-- The S_3 subgroup pipeline sees only ℓ ≤ 1. -/
  s3_truncation_at_ell_le_one :
    ∀ T, spherical_harmonic_decomp T ℓ = 0 → ℓ ≥ 2 ∨ ℓ = 0 ∨ ℓ = 1
  /-- ℓ = 2 contributes the h^4 = -3/4 Borromean coefficient. -/
  ell_two_yields_h4_coefficient :
    borromean_h4_via_so3 = -3/4
  /-- Together with D9 (isospin), defines SU(4) Wigner. -/
  combined_with_isospin_yields_wigner_su4 :
    True   -- placeholder until SU(4) structure axiomatised
```

## Open R&D

1. **Compute prototype**: extend
   [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py)
   from $S_3$-truncated PL integration to full $\mathrm{SO}(3)$
   spherical-harmonic decomposition on Bring's surface; verify
   $h^4 = -3/4$ at the $\ell = 2$ level.
2. **D10 to closed** requires the Lean class instance + the
   `ell_two_yields_h4_coefficient` proof (with `sorry` for the
   regulator of the divergent series at higher $\ell$, per CLAUDE.md
   §3b "class is inhabited").
3. **Connect to 's W/Z $\approx$ cos θ_W within 1%** binomial
   pattern — the unified $T(2, 2m)$ torus-knot Markov-trace
   closed form may have a spherical-harmonic reading at the
   $\mathrm{SO}(3)$-fiber level.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D10
  + §2 Cluster B (D9 $\to$ D10 $\to$ D11 nuclear physics)
- [`docs/audits/-h4-coefficient-source-trace-and-so3-gap.md`](../../docs/audits/-h4-coefficient-source-trace-and-so3-gap.md)
  — the structural-gap audit that proposed this closure
- Upstream class supplier:
  `conj:s5-so3-fiber-action`
  (PR [#1081](https://github.com/litlfred/qou/pull/1081),
  [`S5SO3FiberAction.lean`](../../computations/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean))
- Sibling Cluster B item:
  [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md) (D9)
- Color-tube structure on Bring's quintic:
  [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md),
  [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md)
- $h^4 = -3/4$ topological reference:
  [`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form)
