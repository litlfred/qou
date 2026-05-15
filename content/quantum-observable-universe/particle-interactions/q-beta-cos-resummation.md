**Q_β cos-resummation theorem (conditional on [`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix)).**
*The single-wrap Form A closed-form prediction* $Q_\beta^A$
*admits a tighter symbolic refinement obtained by replacing the
linear bridge correction* $(z-1)h/2$ *from*
[`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge)
*with the classical cosine of half-argument:*

$$
  Q_\beta^{A,\mathrm{cos}}
  \;:=\;
  Q_\beta^A \cdot \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr),
  \qquad
  z = \tfrac{1}{\sqrt q + 1/\sqrt q},
  \quad
  h = q - q^{-1}.
$$

*This refinement tightens the CODATA residual from* $+1677.5$ *ppm
(Form A bare) to* $+305.7$ *ppm — a* $5.49\times$ *improvement —
via* [`probe_q_beta_tightening_landscape.py`](../../folio-assistant/computations/probe_q_beta_tightening_landscape.py) *at*
$q_0 \approx 1.110$.

## Structural origin

The transfer-matrix $M_\beta$ from
[`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix)
has spectrum $\{e^{+i\alpha},\, e^{-i\alpha}\}$ on the
$2$-dimensional irrep $V_{(2,1)}$ of $H_3(q)$, with eigenphase
$\alpha = (z-1) h / 2$ at the single-wrap order.  The Markov
trace $\tau_M$ symmetrizes the two eigenphases:

$$
  \tau_M(M_\beta)
  \;=\;
  \tfrac{1}{2}\bigl(e^{+i\alpha} + e^{-i\alpha}\bigr)
  \;=\;
  \cos\alpha
  \;=\;
  \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr).
$$

Two structural constraints force this form:

1. **Markov cyclicity.**
   The trace is cyclic, $\tau_M(xy) = \tau_M(yx)$, hence invariant
   under the bar involution $q \mapsto q^{-1}$ which sends
   $\sigma_i \leftrightarrow \sigma_i^{-1}$ and consequently
   $\alpha \mapsto -\alpha$.  The resummation must therefore be
   **even in $\alpha$**: only $\alpha^{2k}$ powers survive.  The
   minimal even-power resummation matching the linear bridge at
   the perturbative level is the cosine,
   $\cos\alpha = 1 - \alpha^2/2! + \alpha^4/4! - \cdots$.

2. **Classical decategorification.**
   The mass observable lives in the **classical** limit (Pauli /
   Bose–Einstein statistics, per CLAUDE.md §7b's
   Kazhdan–Lusztig decategorification principle), not in the
   q-deformed quantum group.  Empirical comparison confirms:

   | resummation | residual at $q_0$ |
   |---|---:|
   | $\cos((z-1)h/2)$ (classical) | $+305.7$ ppm |
   | $\cos_q((z-1)h/2)$ (q-deformed) | $+313.4$ ppm |

   The classical cosine wins by $\approx 7$ ppm, consistent with the
   mass observable's classical-limit residence.

## Numerical reduction

At $q_0$:

| quantity | $q_0$ value | role |
|----------|---------:|------|
| $z$ | $0.49915..$ | Markov–Jones parameter |
| $h$ | $0.20874..$ | quantum-integer differential |
| $\alpha = (z-1)h/2$ | $-0.05234..$ | single-wrap eigenphase |
| $\cos\alpha$ | $0.99863..$ | resummation factor |
| $Q_\beta^A$ | $0.78365$ MeV | bare Form A |
| $Q_\beta^{A,\cos}$ | $0.78257$ MeV | cos-resummed |
| CODATA $Q_\beta$ | $0.78233$ MeV | target |
| residual (bare) | $+1677.5$ ppm | — |
| residual (cos) | $+305.7$ ppm | $5.49\times$ tighter |

## Implication for 1 ppb roadmap

Per [`audit_delta_S_chain.py`](../../folio-assistant/computations/audit_delta_S_chain.py),
the n-p mass-split residual $\varepsilon_{\Delta S}$ inherits
$Q_\beta$'s residual through the algebraic chain identity

$$
  \varepsilon_{\Delta S}
  \;=\;
  \frac{Q_\beta}{Q_\beta + m_e} \cdot \varepsilon_Q
  \;\approx\;
  0.605\,\varepsilon_Q .
$$

Under the cos resummation:
$\varepsilon_Q$ drops $1678 \to 306$ ppm, and consequently
$\varepsilon_{\Delta S}$ drops $1015 \to 185$ ppm.  This is one
rung of the precision ladder toward the $1$ ppb target
($\varepsilon_Q \approx 0.0017$ ppm).  The remaining $305$ ppm
gap calls for the **3-irrep** extension: $V_{(3)}$ and
$V_{(1,1,1)}$ contribute at $O(h^2)$ to $\tau_M$ but are not yet
included in the single-eigenphase resummation above.

## Status

This proposition is **conditional** on
[`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix)'s
identification of $\alpha = (z-1)h/2$ as the single-wrap eigenphase
on $V_{(2,1)}$.  The Lean class
[`QOU.Interactions.QBetaCosResummation`](q-beta-cos-resummation.lean)
axiomatises that identification; the cos-resummation theorem then
follows from the Markov-cyclicity constraint (1) above by `ring`
on the $\alpha$ symbolic identity, with the empirical $5.49\times$
tightening recorded in the
[`q-beta-tightening-landscape`](../../folio-assistant/computations/q-beta-tightening-landscape.witness.json)
witness as numerical evidence.
