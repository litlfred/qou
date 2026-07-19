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

[`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) establishes the **composite** CPT action. The framework historically collapses C, P, T into the single bar-involution [`def:bar-involution`](#def:bar-involution) on Hecke generators ($q \mapsto q^{-1}$ together with $\sigma_i \mapsto \sigma_i^{-1}$). That conflation suppresses the **distinct categorical sources** of the three discrete symmetries:

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

## Axiomatisation

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

The color-tube data populates this structure conditionally upon [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube).

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
- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) (CPT composite)
- [`bar-involution.md`](bar-involution.md)—the bar-involution = CPT composite identification at the algebraic level
- AGENTS.md §7b—Type-B folding for chirality / CPT (symmetric-crystal authoring shortcut, D22)
