The computation `tau-lepton-nf.py` evaluates the continuant
recurrence ([lepton continuant](#prop:lepton-continuant-recurrence))
at $q_0 \approx 1.1100$ for $n = 0, 1, \ldots, 9$.  The witness
file `tau-lepton-nf.witness.json` records every coefficient to
machine precision; the recurrence residuals are all
$< 10^{-12}$.

## Full NF table

| $n$ | $a_n$ | $b_n$ | $\mathrm{net}$ | Particle |
|:---:|:-----:|:-----:|:--------:|:--------:|
| $0$ | $1.000$ | $0.000$ | $1.000$ | $\nu$ (identity) |
| $1$ | $0.000$ | $1.000$ | $1.000$ | $H^0$ (unknot) |
| $2$ | $1.000$ | $0.209$ | $1.209$ | — |
| $3$ | $0.209$ | $1.044$ | $\mathbf{1.253}$ | $e^-$ (trefoil) |
| $4$ | $1.044$ | $0.427$ | $1.471$ | — |
| $5$ | $0.427$ | $1.133$ | $\mathbf{1.560}$ | $\mu^-$ (cinquefoil) |
| $6$ | $1.133$ | $0.664$ | $1.797$ | — |
| $7$ | $0.664$ | $1.272$ | $\mathbf{1.936}$ | $\tau^-$ (septafoil) |
| $8$ | $1.272$ | $0.930$ | $2.202$ | — |
| $9$ | $0.930$ | $1.466$ | $2.396$ | — |

Odd-$n$ torus knots $T_{2,n}$ with $n \leq 7$ exhaust the
embeddable fermion spectrum on the Bring surface
([torus knot generators](#prop:torus-knot-generators)).
The even-$n$ entries are not torus knots but they demonstrate
the monotone growth of the net coefficient.

## Lepton decay differences

$$
  \Delta\mathrm{net}(\tau \to e)
  = \mathrm{net}(T_{2,7}) - \mathrm{net}(T_{2,3})
  = 1.936 - 1.253
  = +0.683
$$

$$
  \Delta\mathrm{net}(\tau \to \mu)
  = \mathrm{net}(T_{2,7}) - \mathrm{net}(T_{2,5})
  = 1.936 - 1.560
  = +0.376
$$

The NF difference ratio
$\Delta(\tau \to e) / \Delta(\tau \to \mu) \approx 1.816$
reflects the **crossing count difference** ($4$ crossings
released in $\tau \to e$ vs $2$ in $\tau \to \mu$), but does
**not** directly give the branching ratio because the
matrix element factorises through the weak vertex trace
([lepton universality](#prop:tau-leptonic-universality)).

## Mass-ratio indicators

$$
  \frac{\mathrm{net}(\mu)}{\mathrm{net}(e)}
  = \frac{1.560}{1.253} = 1.245
  \qquad
  \frac{\mathrm{net}(\tau)}{\mathrm{net}(e)}
  = \frac{1.936}{1.253} = 1.545
$$

These are **not** the physical mass ratios
$m_\mu / m_e \approx 206.8$ and $m_\tau / m_e \approx 3477$;
the net coefficients parameterise the topological complexity
of the torus knot, while physical mass requires the full
Seiberg–Witten integral
([lepton mass integrals](#rem:lepton-mass-integrals)) over
the jet bundle prolongation.
