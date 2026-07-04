The $q$-Laplacian spectral tower
([$q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower)) is the
organizing observation behind several $q$-deformed structures in the
framework: rather than treat each one's spectral content separately, they
all read off the *same* tower $[k]_q^2$.

## One tower, four consumers

| Structure | How it uses $[k]_q^2$ |
|---|---|
| $q$-heat equation $\partial_t u = -\Delta_q u$ | mode $k$ decays as $e^{-[k]_q^2 t}$ |
| $q$-Navier–Stokes ($\Delta_q$ dissipation) | eigenvalues $[k]_q^2 \sim q^{2k}$ |
| Markov trace / Gram / Wenzl blocks | block quantum dimensions $[2j+1]_q$ |
| Yekutieli lifting obstruction tower | level capped at $\kappa-1$ by truncation |

Because the tower is established in the proposition, each consumer refers
**back** to it rather than re-introducing $[k]_q$ locally.

## Concrete truncation values

The surviving quantum dimensions are exact algebraic numbers: for example
$[3]_q$ at $\kappa = 5$ is the golden ratio $\varphi = \tfrac{1+\sqrt5}{2}$
(the Fibonacci-anyon dimension), and $[2]_q$ at $\kappa = 8$ is
$\sqrt{2+\sqrt2}$. The practical payoff is **exactness**: at a root of
unity the spectrum is *finite*, so any spectral computation built on it
(the $q$-heat kernel, a $q$-NS truncation, a Gram block) is a finite exact
sum with **no series-truncation error** — the compute-accuracy benefit of
the root-of-unity viewpoint.

## Fibre vs observable level

The tower and its truncation are **fibre-level** statements: $q$ is a
formal (or complex) variable with $\mathrm{Im}(q)$ unconstrained,
and the operative symmetry is the root of unity / bar involution
$q \mapsto q^{-1}$ — *not* a reality assumption. Only the *observable*
component, obtained by evaluating at the real archimedean substrate
value $q_0$, is real. The root-of-unity spectra and quantum dimensions
are exact identities in the relevant cyclotomic field, independent of
the eventual archimedean realisation (cf. the front-matter
fibre-versus-observable distinction).
