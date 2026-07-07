**Proposition (canonical p-n averaging uniqueness).**
*Let $\sigma_{pn}$ and $\sigma_{pn}'$ be two p-n interface averaging functionals on $H_{3A}(R, q)$. Assume both satisfy: (a) bar-invariance $\sigma_{pn}(q) = \sigma_{pn}(q^{-1})$, (b) color-flavor compatibility, and (c) standard normalisation $\sigma_{pn} = z$. Then they are equal block-wise. The canonical p-n averaging is uniquely determined.*

## Setting

The QOU mass identity at $A \geq 2$ contracts a per-interface averaging functional $\sigma_{pn}$ across the p-n boundary slice. The two production candidates are the uniform bar-invariant form and the Bring color-tube weighted form. Both satisfy bar-invariance and standard normalisation. Once we fix color-flavor compatibility, the averaging is uniquely determined.

### Derivation chain for the closed-form weight

The substrate evaluation $w(t, t', q) = 1/(1 - h_q \cdot q^{10})$ derives from Bring's surface geometry:
- Bring's surface has genus $g = 4$.
- The genus-4 force-carrier pair is $\{T(2,9), T(3,5)\}$.
- We prove $\alpha_{\text{shift}}(T_{p,k}) = k \cdot (p-1)$. For $T(3,5)$, $\alpha_{\text{shift}}(T(3,5)) = 10$. This specifies the pole order of $\sigma$.
- The Bring color-tube weight inherits this derived pole order $q^{10}$.

## Lean structure

We stage the uniqueness via the conditional-class pattern:
- `BarInvariant R σ_pn`: the bar-involution axiom.
- `ColorFlavorCompatible R σ_pn`: the open class for color-sheet mapping.
- `StandardNorm R σ_pn z`: the pointwise normalisation.

Conditional on these classes, `theorem pn_averaging_unique` proves $\sigma_{pn} = \sigma_{pn}'$.
