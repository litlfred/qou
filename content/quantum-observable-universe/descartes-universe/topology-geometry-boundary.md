The categorical action $\mathcal{S}_q = \mathrm{tr}(\mathcal{L}_q)$
([canonical action](#prop:qou-canonical-action)) evaluated on a nuclear
link $\mathcal{N}(Z, N)$ produces observables at two levels.

**What $q$ alone determines.**

These are computed from the Iwahori--Hecke algebra $H_A(q)$ at the single
parameter the substrate $q$, the Descartes condition $\chi(A) = -6$,
and the categorical definitions:

| Observable | Formula | Status |
|-----------|---------|:---:|
| Which nuclei are stable | $p^*(A)$ from the beta-stability line at $q$ | From $q$ |
| Sensitivity to $q$ | $\partial \ln \Gamma / \partial \ln q \approx 48$ | Exact |
| Ground-state ordering | Minimum $\Phi_q$ over braid representatives | Computed (A $\le$ 14 exhaustive) |
| Markov trace | $\mathrm{tr}(\mathcal{N}) = \prod_i \hat{V}_i$ | **Theorem** |
| Trace sign structure | $\mathrm{sign}(\mathrm{tr})$ per nucleus | Exact (Singular) |
| Hecke step count | $\Delta(\text{R2 steps}) = -1$ universally | Computed |
| Writhe change | $\Delta w = A - 1$ | Computed |
| Emission topology | $L_0^{-} = T_{2,3} \sqcup T_{1,0}^{\sigma}$ ($\beta^-$: $e^- + \nu_e^{\sigma}$) | Derived |
| Shell blocking | $e_i p_n = 0$ in TL (Jones--Wenzl kills smoothing) | Algebraic |
| Nucleon masses | $m_\mathfrak{p} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} \approx 938.272$ MeV | From $q$ (terminal resolution) |
| Mass splitting | $m_n - m_p = \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}} \approx 1.290$ MeV | From $q$ |
| Deuteron binding | $B_d \approx 1.29$ MeV from Vol($\mathcal{B}_3 \bowtie_\text{Hopf} \mathcal{B}_3$) / $\hbar_q^2$ | From $q$ (SnapPy) |
| Relative decay rates | $\propto \prod_{i \leq p} \lvert\hat{V}_i^{\mathrm{par}}/\hat{V}_i^{\mathrm{dau}}\rvert^2$ | Computed |
| Environmental $q$-shift | $q(p) = 1 + \lvert\langle L_\varTheta, F_A^+\rangle\rvert$ | Predicted |

**What is not yet computed from $q$ alone.**

The **$Q$-value** for nuclei beyond the deuteron.  The $Q$-value
is the mass difference $M(\text{parent}) - M(\text{daughter}) - m_e$.
Each nuclear mass requires the terminal resolution of the full
composite link $L_{3A}$ — the pair Skein mass formula applied to
all crossings with Hecke compounding.  This computation is set up
(braid registry, SnapPy, Singular/Hecke engine) but not yet
evaluated for $A > 2$.

The mass formula for individual hadrons:
$\mathfrak{m} = \mathrm{Vol}(K) / \hbar_q^2$ (hyperbolic volume normalised
by $\hbar_q^2 = (1 - q^{-1})^2$) gives sub-keV masses for the
electron, muon, proton, and neutron.  For multi-nucleon links
(satellite links with $\mathrm{Vol} = A \times \mathrm{Vol}(\mathcal{B}_3)$
exactly), the nuclear binding comes from the pair Skein mass
$\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$
evaluated at the inter-nucleon crossings.

The $Q$-value is a $\sim 0.001\%$ mass difference ($\sim 0.1$--$1$ MeV
on $\sim 10{,}000$--$200{,}000$ MeV total mass).  Computing it
requires the composite pair Skein weights to high precision — the
terminal resolution applied to the full $3A$-strand link.

The framework gives the correct **structure** of the $Q$-value
(which nuclei decay, in which direction, with which shell
blocking and sensitivity) from $q$ alone.
