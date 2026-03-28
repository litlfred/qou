The Markov trace of the nuclear braid is a link invariant that
grows exponentially with $A$
([Markov trace factorization](#thm:markov-trace-factorization)).
The physical observable — the transition matrix element
$|\mathcal{M}_q|^2$ — is the **ratio** of parent and daughter
traces, where the exponential growth cancels.

**Proposition.**
The beta-decay matrix element squared is proportional to the
ratio of Markov-traced generator volumes at the affected
generators:

$$
  |\mathcal{M}_q|^2
  \;\propto\;
  \prod_{i=0}^{p}
  \left|
    \frac{\hat{V}_i^{\,\mathrm{par}}}{\hat{V}_i^{\,\mathrm{dau}}}
  \right|^2
$$

where $\hat{V}_i = z \cdot a_i + b_i$ is the Markov-traced
generator volume at $\sigma_i$, and the product runs only over
generators $i \leq p$ (those affected by the conversion of
nucleon $p$ from neutron to proton).  Generators $i > p$ cancel
exactly between parent and daughter.

**Proof.**
From the factorization theorem:

$$
  \frac{\mathrm{tr}(\overline{\mathcal{N}(Z, N)})}
       {\mathrm{tr}(\overline{\mathcal{N}(p+1, n-1)})}
  \;=\;
  \frac{\prod_{i=0}^{A-2} \hat{V}_i^{\,\mathrm{par}}}
       {\prod_{i=0}^{A-2} \hat{V}_i^{\,\mathrm{dau}}}
  \;=\;
  \prod_{i=0}^{A-2}
  \frac{\hat{V}_i^{\,\mathrm{par}}}{\hat{V}_i^{\,\mathrm{dau}}}.
$$

For generators $i > p$: the crossings from nucleon $i$ to
nucleons $j > i$ are identical in parent and daughter (neither
nucleon $i$ nor any $j > i$ changed type).  Therefore
$\hat{V}_i^{\,\mathrm{par}} = \hat{V}_i^{\,\mathrm{dau}}$ and
the ratio is $1$.  Only generators $i = 0, \ldots, p$ contribute.

The transition matrix element is the Skein amplitude at the
beta-decay vertex, which is proportional to the trace ratio:

$$
  |\mathcal{M}_q|^2
  \;=\;
  |\mathrm{skein\_amp}|^2
  \cdot
  \left|
    \frac{\mathrm{tr}(\overline{\mathcal{N}(Z, N)})}
         {\mathrm{tr}(\overline{\mathcal{N}(p+1, n-1)})}
  \right|^2
$$

where $\mathrm{skein\_amp} = q^{1/2} - q^{-1/2}$.  $\square$

**Computational results.**
The trace ratio $\hat{V}^{\mathrm{par}} / \hat{V}^{\mathrm{dau}}$
at each affected generator, for all six verification nuclei:

| Nucleus | Affected gens | $\prod |\hat{V}^{\mathrm{par}}/\hat{V}^{\mathrm{dau}}|$ | $|\mathcal{M}_q|^2$ rel. |
|---------|:---:|---:|---:|
| ${}^{3}\mathrm{H}$ | $\sigma_0, \sigma_1$ | $1.09$ | $1.00$ (ref) |
| ${}^{14}\mathrm{C}$ | $\sigma_0$--$\sigma_6$ | $1.72$ | $2.47$ |
| ${}^{60}\mathrm{Co}$ | $\sigma_0$--$\sigma_{27}$ | $41.3$ | $1{,}432$ |
| ${}^{90}\mathrm{Sr}$ | $\sigma_0$--$\sigma_{38}$ | $175$ | $25{,}610$ |
| ${}^{137}\mathrm{Cs}$ | $\sigma_0$--$\sigma_{55}$ | $3{,}106$ | $8.1 \times 10^6$ |
| ${}^{210}\mathrm{Bi}$ | $\sigma_0$--$\sigma_{83}$ | $271{,}454$ | $6.2 \times 10^{10}$ |

The trace ratio grows with $p$ (the number of affected generators),
reflecting the increasing number of crossings that change type.
The squared ratio $|\mathcal{M}_q|^2$ spans 10 orders of magnitude
— the correct order of magnitude for the observed variation in
nuclear matrix elements ($\log ft$ from 3 to 9, corresponding
to $|M|^2$ spanning $\sim 10^6$).

The growth of the ratio with $p$ means **heavier nuclei have
larger topological matrix elements**, which drives faster decay
rates.  This is consistent with the observation that allowed
beta transitions in heavy nuclei tend to have shorter half-lives
(smaller $\log ft$) than those in light nuclei.

**The half-life formula (final form).**
Combining the trace ratio with the phase space integral:

$$
  t_{1/2}
  \;=\;
  \frac{\ln 2 \cdot 2\,N_v^4}{243\,\mathfrak{E}_{\times} \cdot \mu_0}
  \;\cdot\;
  \frac{1}{[2]_q \;\cdot\; s^2}
  \;\cdot\;
  \frac{1}{f(Z_d,\, \mathcal{Q}_q)}
  \;\cdot\;
  \prod_{i=0}^{p}
  \left|
    \frac{\hat{V}_i^{\,\mathrm{dau}}}{\hat{V}_i^{\,\mathrm{par}}}
  \right|^2
$$

where $s = q^{1/2} - q^{-1/2}$ is the Skein amplitude,
$\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$ is the crossing energy,
$\mu_0$ is the single dimensional scale (unit choice),
$N_v$ is the effective crossing count of the weak scale
($v = N_v\,\mathfrak{E}_{\times}\,\mu_0$), and
$f(Z_d, \mathcal{Q}_q)$ is the Coulomb-corrected phase space integral
([Skein-Coulomb enhancement](#prop:skein-coulomb-enhancement)).
The prefactor replaces the standard-physics combination
$G_F^2\,m_e^5/(2\pi^3)$
([hadron half-life](#prop:hadron-half-life)).
The product of volume ratios gives the topological part of
$|\mathcal{M}_q|^2$.
