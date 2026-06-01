**Proposition (the $q$-Laplacian spectral tower).** *The $q$-Laplacian
$\Delta_q = d_q\delta_q + \delta_qd_q$
([particle / $q$-harmonic form](#def:q-harmonic-form)) has eigenvalues
given by the **$q$-integer tower***
$$
  [k]_q^2, \qquad [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}}
  \quad (k = 1, 2, 3, \ldots).
$$
*At a primitive root of unity $q = e^{i\pi/\kappa}$ the $q$-integer
$[\kappa]_q$ **vanishes**, and the spectrum truncates to the finite set*
$$
  \{\,[1]_q^2, [2]_q^2, \ldots, [\kappa-1]_q^2\,\},
$$
*the **Verlinde / ADE quantum-dimension** data of the truncated
representation category.*

This is the organizing observation behind several $q$-deformed
structures in the framework: rather than treat each one's spectral
content separately, they all read off the *same* tower $[k]_q^2$.

## One tower, four consumers

| Structure | How it uses $[k]_q^2$ |
|---|---|
| $q$-heat equation $\partial_t u = -\Delta_q u$ | mode $k$ decays as $e^{-[k]_q^2 t}$ |
| $q$-Navier–Stokes ($\Delta_q$ dissipation) | eigenvalues $[k]_q^2 \sim q^{2k}$ |
| Markov trace / Gram / Wenzl blocks | block quantum dimensions $[2j+1]_q$ |
| Yekutieli lifting obstruction tower | level capped at $\kappa-1$ by truncation |

Because the tower is established here, each consumer refers **back** to
this proposition rather than re-introducing $[k]_q$ locally.

## The root-of-unity truncation

The vanishing $[\kappa]_q = 0$ at $q = e^{i\pi/\kappa}$ is elementary:
the numerator $q^\kappa - q^{-\kappa}$ vanishes because
$q^\kappa = e^{i\pi} = -1$, hence $q^{-\kappa} = -1$ as well and the
difference is $0$. By the **Verlinde formula**
[[verlinde1988]](#) the fusion coefficients are diagonalised by the
modular $S$-matrix and the surviving simple objects are
$j = 0, \tfrac12, \ldots, \tfrac{\kappa-2}{2}$ — the **Reshetikhin–
Turaev** truncation [[reshetikhin1991]](#). The surviving quantum
dimensions are exact algebraic numbers in the cyclotomic field
$\mathbb{Q}(\zeta_\kappa)$; for example $[3]_q$ at $\kappa = 5$ is the
golden ratio $\varphi = \tfrac{1+\sqrt5}{2}$ (the Fibonacci-anyon
dimension), and $[2]_q$ at $\kappa = 8$ is $\sqrt{2+\sqrt2}$.

The practical payoff is **exactness**: at a root of unity the spectrum
is *finite*, so any spectral computation built on it (the $q$-heat
kernel, a $q$-NS truncation, a Gram block) is a finite exact sum with
**no series-truncation error** — the compute-accuracy benefit of the
root-of-unity viewpoint.

## Fibre vs observable level

The tower and its truncation are **fibre-level** statements: $q$ is a
formal (or complex) variable with $\operatorname{Im}(q)$ unconstrained,
and the operative symmetry is the root of unity / bar involution
$q \mapsto q^{-1}$ — *not* a reality assumption. Only the *observable*
component, obtained by evaluating at the real archimedean substrate
value $q_0$, is real. The root-of-unity spectra and quantum dimensions
are exact identities in the relevant cyclotomic field, independent of
the eventual archimedean realisation (cf. the front-matter
fibre-versus-observable distinction).

## Lean structure

`truncRoot κ := exp(iπ/κ)` over $\mathbb{C}$;
`truncRoot_pow` proves $\zeta_\kappa^{\,\kappa} = -1$ (hence
$\zeta_\kappa^{\,2\kappa} = 1$), and
`qIntegerNumerator_vanishes_at_truncRoot` proves the numerator
$q^\kappa - q^{-\kappa} = 0$ at $q = \zeta_\kappa$ — the level-$\kappa$
truncation. The statement lives over $\mathbb{C}$ because the
truncation root is genuinely complex; no reality is assumed.
