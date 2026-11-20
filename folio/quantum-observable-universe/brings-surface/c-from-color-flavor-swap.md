**Conjecture (charge conjugation as the color-sheet flavor swap; conditional on [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube)).**
*Within the QOU framework, charge conjugation $C$ acts as the **flavor swap on color sheets** that exchanges each quark flavor with its antimatter-conjugate:*

$$
  C \;:\;
  \begin{cases}
    u \;\longleftrightarrow\; \bar u, \\
    d \;\longleftrightarrow\; \bar d,
  \end{cases}
$$

*applied independently to each of the three color sheets of every nucleon-coloured braid strand. The proton flavor triple $(u, u, d)$ maps to $(\bar u, \bar u, \bar d)$ (the antiproton); the neutron flavor triple $(u, d, d)$ maps to $(\bar u, \bar d, \bar d)$ (the antineutron). $C$ is an involution ($C^2 = \mathrm{id}$) and commutes with the color-tube weighted averaging of [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube).*

## Separating $C$ from the CPT composite

[CPT-saturation as Type-B fold-orbit closure: deriving $\rho_F \in \{m_e, 2m_e\}$ from crystal structure](#conj:cpt-orbit-closure-density) formalises the **composite** CPT action. The framework historically collapses C, P, T into the single bar-involution [Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections](#def:bar-involution) on Hecke generators ($q \mapsto q^{-1}$ together with $\sigma_i \mapsto \sigma_i^{-1}$). That conflation suppresses the **distinct categorical sources** of the three discrete symmetries:

| Symmetry | Categorical source | Acts on |
|----------|--------------------|---------|
| **C** (this conjecture) | flavor swap on color sheets | quark-flavor content of nucleon braid strands |
| **P** | mirror reflection of braid diagram | writhe / signed-crossing classification ([`bar-involution-table3-data`](../stochastic-mechanics/bar-involution-table3-data.md)) |
| **T** | Markov-trace word reversal | trace-cyclicity dual |

The bar-involution $q \mapsto q^{-1}$, $\sigma_i \mapsto \sigma_i^{-1}$ acts as the **composite CPT** in this categorisation, not as C alone. This conjecture locates the C-component on the color sheets, orthogonal to P (braid-diagram mirror) and T (trace reversal).

## The conjectural content

The proposition relies on the color-sheet flavor structure established in [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube). Specifically:

1. **C is well-defined.** The flavor-content map $(F_1, F_2) \mapsto (\bar F_1, \bar F_2)$ commutes with the color-tube weight tensor $W_{c_1 c_2}(F_1, F_2)$—i.e. $W_{c_1 c_2}(\bar F_1, \bar F_2) = W_{c_1 c_2}(F_1, F_2)$ (the weights are flavor-conjugation invariant).
2. **C is an involution.** Each color sheet flips back to its original flavor under two applications.
3. **C commutes with bar-involution on the algebraic side.** This forces $\mathrm{CP} \cdot \mathrm{T}$ and $\mathrm{C} \cdot \mathrm{PT}$ to reduce to the bar-involution identity classified in [`bar-involution.md`](../braids-and-knots/bar-involution.md) §Bar-symmetric.

When all three hold, $C$ constitutes the well-defined Z/2 categorical symmetry on the color-sheet flavor data. The CPT composite of [CPT-saturation as Type-B fold-orbit closure: deriving $\rho_F \in \{m_e, 2m_e\}$ from crystal structure](#conj:cpt-orbit-closure-density) factors as $\mathrm{CPT} = C \cdot P \cdot T$ in the natural order, as three commuting Z/2 actions on the color-tube structure.

## Structural position

- **GB filtration level.** None: the claim addresses a Z/2 categorical symmetry on color-sheet metadata, not Hecke elements at a particular Coxeter length.
- **Jet order.** $h^0$: the $C$-action is independent of $q$, and the flavor-conjugation map forms a structural Z/2 lifting through the color-tube tensor.
- **Bar-symmetry.** $C$ is bar-symmetric. It preserves $q$ and commutes with $\sigma_i \leftrightarrow \sigma_i^{-1}$, since it acts on color-sheet labels and not on Hecke generators. It is $C$ composed with $PT$ that yields the bar-involution; $C$ itself is bar-trivial in [`bar-involution-table4-data`](../stochastic-mechanics/bar-involution-table4-data.md).

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

The class becomes inhabited by the color-tube data once [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube) is instantiated.

## Consumers / downstream

- [CPT-saturation as Type-B fold-orbit closure: deriving $\rho_F \in \{m_e, 2m_e\}$ from crystal structure](#conj:cpt-orbit-closure-density) becomes a corollary of $\mathrm{CPT} = C \cdot P \cdot T$ once the charge-conjugation, parity and time-reversal components close jointly—the content of [CPT closure: charge conjugation, parity and time reversal jointly preserve the Markov trace](#conj:cpt-d6-d7-d8-closure).
- The matter/antimatter sheet structure on Bring's quintic surface ([Color tube fibers](color-tube-fibers.md)) acquires a natural C-action that descends to the SO(3) fiber.
- Type-B folding for chirality and CPT (`conj:type-b-folding-cpt`) is the symmetric-crystal analogue of this conjecture. Folding the $\mathfrak{sl}_n$ Cartan datum to Type B realises C as a symmetric-crystal structure.

## Numerical cross-check and open content

At the 50-digit substrate $q_0$, the flavor-conjugation involution leaves the color-tube weighted inter-nucleon Hecke generator invariant for all sixteen nucleon pairs drawn from $\{p, n, \bar p, \bar n\}$, in two two-dimensional Hecke representations (the diagonal eigenvalue model and a non-diagonal conjugate of it), with the $\epsilon$ and $W$ tables invariant cell by cell ([`verify_c_color_swap.py`](../../../computations/verify_c_color_swap.py), [`verify-c-color-swap.witness.json`](../../../computations/verify-c-color-swap.witness.json)). The check runs the uniform projection $W = 1/9$—the only realisation of $W$ available while its closed form remains open—so it corroborates the derivation rather than testing the conjectural Bring-derived $W$. No parameter is fitted.

The statement is conjectural only for as long as [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube) and the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber-action class `conj:s5-so3-fiber-action` remain uninhabited; supplying both makes it unconditional.

## Cross-references

- Upstream class: [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube)
- [CPT-saturation as Type-B fold-orbit closure: deriving $\rho_F \in \{m_e, 2m_e\}$ from crystal structure](#conj:cpt-orbit-closure-density)—the CPT composite, already formalised
- [`bar-involution.md`](../braids-and-knots/bar-involution.md)—the bar-involution = CPT composite identification at the algebraic level
