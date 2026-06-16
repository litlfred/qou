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

**α_EM is the same Hopf channel.** The fine-structure constant is itself a
2-strand Hopf-operation coupling: by [`thm:em-spectral-completeness`](#thm:em-spectral-completeness)
the 2-strand braiding has exactly the two idempotents $e_+, e_-$, and
[`cor:gauge-coupling-uniqueness`](#cor:gauge-coupling-uniqueness) /
[`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
make $\alpha_{EM}$ the unique multiple of the **antisymmetric $e_-$** coupling,
$\alpha_{EM} = h^2/(q\,\delta_q(T_{2,9})\delta_q(T_{3,5}))$ with
$\delta_q(T_{2,k}) = q^k - q^{-k} = h\,[k]_q$ — the $\sinh$/$e_-$ trace. So
$\alpha_{EM}$ (the $e_-$ coupling) and van der Waals (the bar-odd
$\sinh(2\lambda)(e_+-e_-)$ residual) are the **same antisymmetric / sinh / EM
channel** of the Hopf $H_2(q)$ operation — the fine-structure constant and the
dispersion force are two faces of one Hopf knot operation. The α_EM Habiro
element [`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution),
$H = [2]_q(1-h^2\alpha) = 2\cosh\lambda\,(1-h^2\alpha)$, is the **bar-even** next-order
correction (a $\cosh$ carrier $\times$ $\sinh^2$ correction), opposite the bar-odd vdW.

At $q_0$: $\cosh(2\lambda) \approx :val[vdw_cosh_2lambda]{precision=5, witness=computations/vdw-pskew-sinh-probe.witness.json}$,
and the bar-odd residual $\sinh(2\lambda)(e_+-e_-) \approx :val[vdw_bar_odd_residual]{precision=5, witness=computations/vdw-pskew-sinh-probe.witness.json}$ (exact, no fit).

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
