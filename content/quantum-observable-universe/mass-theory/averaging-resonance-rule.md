**Theorem (averaging-resonant rung selection rule).**
*Let $\sigma_{\mathrm{avg}} = \tfrac{1}{2}(\sigma + \sigma^{-1})$
be the bar-symmetric averaged-crossing operator on
$H_{n_{\mathrm{total}}}(R, q)$, and let $P_{\mathrm{avg}} = (1 +
\overline{\,\cdot\,})/2$ be the bar-invariant averaging projection.
For canonical typed-$\mathbf{B}_3$ braids of total strand count
$n_{\mathrm{total}}$ admitting the half-fill cyclic structure
(proton recipe: $n_{\mathrm{total}} = 9$, half-fill rung
$k = \lfloor 9/2 \rfloor = 4$ ⊕ 1 wrap-around contribution = 5),
the unique $\sigma_{\mathrm{avg}}$-resonant rung is*

$$
  k_{\mathrm{res}}
  \;=\;
  \left\lfloor \frac{n_{\mathrm{total}}}{2} \right\rfloor
  \;+\; \mathbb{1}_{\mathrm{wrap}}(n_{\mathrm{total}}),
$$

*where the wrap indicator $\mathbb{1}_{\mathrm{wrap}}$ adds one
when the half-fill cycle closes through the proton recipe's
inter-nucleon interface; otherwise zero.*

## Structural content

Two layers compose:

1. **Half-fill cyclicity** — the bar-invariant projection
   $P_{\mathrm{avg}}$ restricted to a typed-$\mathbf{B}_3$ braid
   admits the canonical Markov-trace expansion at the half-fill
   rung; rung positions above the floor see no $\sigma$-resonant
   contribution (their bar-averaged amplitudes cancel by the
   crossing-cyclicity dual). This supplies the **rung selection**:
   $k_{\mathrm{res}}$ is uniquely determined by $n_{\mathrm{total}}$.

2. **Bar-invariant magnitude** — at the selected rung, the
   $P_{\mathrm{avg}}$-fingerprint contributes magnitude $1/2$ to the
   resonant Markov-trace coefficient (the involution channel of
   $\sigma_{\mathrm{avg}}$ at $q_0$). This is the magnitude
   layer interpreted by
   [`prop:c5-involution-leibniz-decomposition`](../stochastic-mechanics/c5-involution-leibniz-decomposition.md),
   which observes $c_5 = -b^2 - 1/2$ at the proton recipe.

The two layers together yield $c_5 = -b^2 - 1/2$ at rung $k = 5$;
this proposition is the rung-selection layer (which $k$), while
$c5$-involution is the magnitude-and-sign layer (the
$\pm 1/2$ contribution at that $k$).

## Why $k = 5$ specifically (the proton recipe)

For the proton typed-$\mathbf{B}_3$ braid with
$n_{\mathrm{total}} = 9$ and a canonical
[`prop:pn-averaging-uniqueness`](pn-averaging-uniqueness.md) inter-nucleon
interface, the half-fill floor is $\lfloor 9/2 \rfloor = 4$ and
the wrap-around contribution is $+1$, giving $k_{\mathrm{res}} = 5$.
The wrap-around contribution is a structural consequence of the
inter-nucleon interface closing the typed-$\mathbf{B}_3$ cycle —
without it, the recipe would not be canonical.

## Lean closure (Phase 1 Tier A)

The structural content is captured by
[`averaging_resonance_rule_structural`](averaging-resonance-rule.lean)
as a sorry-free Lean theorem using only `Nat` arithmetic + `decide`:

- `kRes_def : ∀ n w, kRes n w = n / 2 + w` (rfl).
- `kRes_proton_recipe : kRes 9 1 = 5` (decide).
- `kRes_deuteron_recipe : kRes 6 0 = 3`, `kRes_tritium_recipe :
  kRes 9 0 = 4` (decide).

A backward-compat `class AveragingResonanceRule` with default
instance is retained, so downstream blocks that previously used it
as a §3b-cond hypothesis continue to compile. The wrap indicator
in the default instance is set to `1` at `n = 9` (proton recipe)
and `0` elsewhere — a minimal witness; downstream consumers
may override.

The substantive layer this closure does **not** address is the
**magnitude** of the resonant contribution (the $-1/2$ in
$c_5 = -b^2 - 1/2$) — that is handled by
[`prop:c5-involution-leibniz-decomposition`](../stochastic-mechanics/c5-involution-leibniz-decomposition.md).

## Scope

- The rule applies to typed-$\mathbf{B}_3$ braids admitting the
  half-fill cyclic structure. It is not claimed for arbitrary
  $H_n(R, q)$ elements.
- The wrap indicator depends on the inter-nucleon interface
  geometry (proton: $+1$; deuteron / tritium / $^3$He recipes
  documented separately).
- The conjecture is the **selection rule**, not the magnitude.
  Magnitude is the bar-involution channel; see
  [`prop:c5-involution-leibniz-decomposition`](../stochastic-mechanics/c5-involution-leibniz-decomposition.md).

While the underlying formal verification relies on standard floor arithmetic and bar-symmetry properties, defining this explicit averaging resonance rule as the predictive mechanism for the typed-$B_3$ proton recipe forms a mathematically novel structural claim within the Quantum Observable Universe.
