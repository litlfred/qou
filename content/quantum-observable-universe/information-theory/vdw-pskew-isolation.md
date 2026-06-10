*Lean sibling: any commutative ring with $q, q_i$ formal (fibre-level, no reality imposed — the `alpha-em-habiro-bar-involution` convention; CLAUDE.md §7c).*

**Proposition (van der Waals $=$ the bar-odd $P_{\mathrm{skew}}$ channel).**
*Under the bar involution $q \mapsto q^{-1}$, the Hopf weighting of
[`prop:hopf-link-symmetric-decomposition`](#prop:hopf-link-symmetric-decomposition)
splits into a bar-even and a bar-odd part. With rapidity $\lambda = \ln q$,*

$$
  2\,\sigma_1^2 \;=\;
  \underbrace{2\cosh(2\lambda)\,\mathbf 1}_{\text{bar-even (retained)}}
  \;+\;
  \underbrace{2\sinh(2\lambda)\,(e_+ - e_-)}_{\text{bar-odd } (P_{\mathrm{skew}})},
$$

*using $q^2+q^{-2}=2\cosh 2\lambda$, $q^2-q^{-2}=2\sinh 2\lambda$ and
$e_+ + e_- = \mathbf 1$.*

**Van der Waals is the bar-odd residual** $\sinh(2\lambda)\,(e_+-e_-)$. Per
[`crossing-energy-decomposition`](#prop:crossing-energy-decomposition) the
$\sinh$ channel is the antisymmetric / Coulomb–EM channel, and the canonical
$P_{\mathrm{avg}}$ projection ([`def:bar-involution`](#def:bar-involution))
**discards** it. That is exactly why van der Waals is (a) **small** — a discarded
residual; (b) $\sinh$ / $h$-power suppressed rather than a covalent-scale energy;
and (c) **absent from the main mass/binding formula**. The retained bar-even part
is the trivial $\cosh(2\lambda)\,\mathbf 1$ carrier — the "hidden cosh," but *not*
the van der Waals energy itself.

**Im(q) caveat.** Per [`rem-im-q-vs-p-skew`](#rem:im-q-vs-p-skew), the
$P_{\mathrm{skew}}$ (sinh) content is **real** at real $q$ — kept then discarded,
*not* imaginary. $\mathrm{Im}(q)$ is a separate lever (zero by convention). So the
van der Waals residual is a real observable living in the discarded sector;
$\mathrm{Im}(q)\neq 0$ would be a distinct, later refinement, not this channel.

**α_EM sibling.** The α_EM Habiro element
[`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution),
$H = [2]_q(1-h^2\alpha) = 2\cosh\lambda\,(1-h^2\alpha)$, is **bar-even** (a $\cosh$
carrier times a $\sinh^2$ correction); van der Waals is **bar-odd**
($\sinh\cdot\cosh$). Same hyperbolic machinery, opposite bar sector — α_EM is the
retained coupling correction, van der Waals the discarded residual.

At $q_0$: $\cosh(2\lambda) \approx :val[vdw_cosh_2lambda]{precision=5, witness=folio-assistant/computations/vdw-pskew-sinh-probe.witness.json}$,
and the bar-odd residual $\sinh(2\lambda)(e_+-e_-) \approx :val[vdw_bar_odd_residual]{precision=5, witness=folio-assistant/computations/vdw-pskew-sinh-probe.witness.json}$ (exact, no fit).

## Narrowed probe

This prunes the search formally: the molecular van der Waals energy is the
archimedean projection of the **exact** bar-odd expression
$\sinh(2\lambda)\,(e_+-e_-)$ — *not* an $h^k$ fit, and *not* a $\cosh$ factor on
the covalent ladder (the earlier $0.81$ was the wrong $\sinh^4$/covalent framing).
The one remaining open piece is the archimedean inter-molecular separation
($1/r^6$; $e_+$ is the touching limit) that scales the fibre residual to the
$\sim\!\mathrm{kJ/mol}$ molecular energy — open, not fitted.

## Lean structure

`QOU.VdwPskew` (sibling `vdw-pskew-isolation.lean`):
`hopf_bar_even_odd_decomposition` (the bar split, pure-`ring`) and
`vdw_is_bar_odd_residual` (the bar-odd part isolated on the idempotents). Both
sorry-free, verified Lean 4.24.0 + Mathlib.
