**Proposition (bar-parity energy decomposition).**
*Let $\sigma$ be the bar involution (the substrate $q \mapsto q^{-1}$, an
order-2 ring endomorphism) on a field $F$ of characteristic $\neq 2$. Every
energy $E \in F$ splits canonically as*

$$
E \;=\; \underbrace{\tfrac{1}{2}(E + \sigma E)}_{\text{retained } (\cosh)}
\;+\; \underbrace{\tfrac{1}{2}(E - \sigma E)}_{\text{emitted } (\sinh)},
$$

*with the retained part bar-even ($\sigma$-fixed) and the emitted part
bar-odd ($\sigma$-negated). The emitted (bar-odd, $\sinh$) channel is the
decay-width $\mathfrak{D}$ sector; it vanishes iff $E$ is purely retained.*

## The $\mathfrak{D}$ reinterpretation of $E_{\text{unit}}$

This is the energy-level form of the complex-volume split
$\mathfrak{V} = \mathrm{Vol} + i\,\mathrm{CS}$: the retained part is the
binding-proper (cosh) channel, the emitted part is the radiated
$\gamma\bar\gamma$ / decay-width (sinh) channel. Reading the deuteron law
$B(^2\mathrm{H}) = 5g \cdot E_{\text{unit}}$ through this split makes the
"$E_{\text{unit}} = \hbar/\mathfrak{D}$" reinterpretation precise: *if* the
unit is a decay-width energy (bar-odd), then it is its own emitted part with
zero retained part — a purely decay-channel energy
(`frakD_is_pure_emitted`). This keeps $E_{\text{unit}}$ inside the three
calibrations (the width $\mathfrak{D}$ is the CAL-2 datum), rather than a
fourth calibration.

The narrative caveat recorded in
[`docs/coordination/e-unit-deuteron-scale.md`](../../docs/coordination/e-unit-deuteron-scale.md)
stands: whether the deuteron binding actually carries this bar-odd character
is empirically open (the landed §2h data weakly favour a bar-even unit). The
proposition formalizes the *decomposition itself*, which holds regardless;
the parity assignment of the physical $E_{\text{unit}}$ is the open input.

## Already tabulated

The mass-binding dashboard's **Entanglement** table computes this split for
every light nucleus — its `retained E` column is $E_0 \cdot (\cosh$-channel$)$
and its `emitted E` column is $E_0 \cdot |\sinh$-channel$|$. The
`emitted/retained` ratio rises from $0.96$ at the deuteron — the least
saturated, most decay-like light binding, matching its $\beta$-threshold
character — toward $1.00$ by $^6\mathrm{Li}$. The Lean sibling
(`QOU.MassTheory.FrakD`) proves the projection is well-defined and
parity-correct over a generic field: `evenPart_barEven`, `oddPart_barOdd`,
`even_add_odd` (reconstruction), and `oddPart_eq_zero_iff_barEven` (a
nucleus carries no $\mathfrak{D}$ channel exactly when its binding is purely
retained).
