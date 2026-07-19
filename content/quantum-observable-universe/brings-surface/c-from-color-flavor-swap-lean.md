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
