Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q_0$ and Hecke algebra $H_n(R, q)$ filtered by the
confinement filtration $J^\bullet(q)$
([confinement level](#def:confinement-level)).  Let
$\Phi_q(z) = \prod_{k\geq 1}(1 - q^{-k} z)^{-1}$ be the non-perturbative
quantum dilogarithm and let $\zeta_\ell$ denote the root of unity at
which the $\ell$-th knot-operator energy $E_\ell(q)$ degenerates,
$E_\ell(\zeta_\ell) = 0$.

**Proposition.**
*For a knot $\mathcal{K}$ represented by the closed braid with Hecke
normal form $T_w \in A = H_n(R, q)$
([Hecke normal form](#def:hecke-normal-form)), the categorical mass
evaluated at $q_0$ admits the Mittag-Leffler decomposition*

$$
  \mathfrak{m}_{q_0, \mathcal{K}}
  \;=\;
  \underbrace{\bigl|\int_A T_w(q_0)\bigr|}_{E^0\ \text{(descended)}}
  \;+\;
  \sum_{\ell = 1}^{\ell(K, q_0)}
    \frac{\displaystyle
      \operatorname*{Res}_{q = \zeta_\ell}
        \!\Bigl[\Phi_q \cdot \mathrm{tr}_{M,\,\ell}(T_w)\Bigr]
    }{q_0 - \zeta_\ell},
$$

*where $\mathrm{tr}_{M,\,\ell}$ is the induced Markov trace on the
graded piece $J^\ell(q)/J^{\ell+1}(q)$, and $\ell(\mathcal{K}, q_0)$ is the
confinement level of $\mathcal{K}$ at $q_0$.*

**Why residues at roots of unity when $q_0 > 1$?**
*The substrate parameter $q_0 \approx 1.11$ lies outside the unit
circle, so the evaluation $\int_A T_w(q_0)$ is at a regular
point of $\Phi_q$ and $H_n(R, q)$.  The poles of $\int_A$ and
$\Phi_q$ lie at roots of unity $\zeta_\ell \in S^1$: these are the
values of $q$ at which the $\ell$-th generator's Hecke eigenvalues
$(q, -q^{-1})$ become equal in absolute value and $H_n(R, q)$ fails
to be semisimple.  A function $q \mapsto \int_A(T_w, q)$
meromorphic on $\mathbb{C} \setminus \{\zeta_\ell\}$ admits a
**Mittag-Leffler expansion**: its value at a regular point $q_0$
is the sum of an entire piece (the descended $\int_A$) and
simple-pole contributions weighted by the Cauchy kernel
$(q_0 - \zeta_\ell)^{-1}$.  The residue $\operatorname{Res}_{q=\zeta_\ell}$
captures the structural data of the $\ell$-th filtration stratum
(what collapses at $\zeta_\ell$); the kernel transports that data
out to $q_0$.  Distance to the nearest root of unity controls
the magnitude: $\zeta_1 = 1$ is closest ($|q_0 - 1| \approx 0.11$),
so the level-1 residue dominates; higher roots of unity
($\zeta_\ell = e^{2\pi i/n_\ell}$ with $n_\ell \geq 2$) are
further from $q_0$ and contribute less.*

**Habiro-cyclotomic form.**
*Equivalently, after expanding the Cauchy kernel against the
cyclotomic tower of $q$-Pochhammer symbols
$(q; q)_n = \prod_{k=1}^n (1 - q^k)$
([Habiro ring](#def:habiro-ring)), the residue sum becomes a
unified cyclotomic series*

$$
  \sum_{\ell \geq 1}
    \frac{\operatorname{Res}_{q=\zeta_\ell}[\cdots]}{q_0 - \zeta_\ell}
  \;=\;
  \sum_{n \geq 1} a_n(K)\,(q_0; q_0)_n,
$$

*with $a_n(\mathcal{K}) \in \mathbb{Z}[q, q^{-1}]$.  Each term
$(q_0; q_0)_n$ vanishes at all $\zeta_\ell$ of order $\leq n$, so
the expansion is structured by the tower of root-of-unity strata.
This is the categorical analogue of Habiro's unified quantum
invariant.*

**Relation to the brane tower.**
*The formula
$\mathfrak{m} = |\prod \hat V_i^{\mathrm{full}}| +
  \sum_i \Phi_{q_0}(|\hat V_i^{\mathrm{full}}|) +
  \sum_{i<j} z^2 \Phi_{q_0}(|\hat V_i \hat V_j|)$
([mass endomorphism tower](#prop:mass-endomorphism-tower))
is the **regular-value expansion** at $q = q_0$: the first term
is $E^0$, each single-generator $\Phi_{q_0}(|\hat V_i|)$ is the
level-$1$ contribution transported from $\zeta_1 = 1$, and each
pair term is a level-$2$ contribution transported from $\zeta_2$.
Regular-value evaluation is exact for the level-$\ell$ stratum
**only when** $q_0 \mapsto \mathrm{tr}_{M,\ell}$ is analytic at
$q_0$.  When $T_w$ has filtration components at deeper strata
than the regular-value expansion samples, those components
appear as residues at $\zeta_\ell$ for $\ell \geq 2$ and contribute
new terms missing from the regular-value tower.*

**Cohomological interpretation.**
*The filtration $J^\bullet(q)$ together with the rewriting differential
$d$ induced by the three Gröbner–Shirshov rules (Hecke, far
commutativity, Yang–Baxter) makes $H_n(R, q)$ a filtered differential
algebra.  The associated spectral sequence has*

$$
  E_1^{\ell,*} \;=\; H^*\!\bigl(J^\ell/J^{\ell+1},\; d\bigr),
  \qquad
  E_\infty^{\ell,*}
    \;\Longrightarrow\;
    \mathrm{gr}^\ell\,H_n(R, q),
$$

*and $\int_A$ is a closed linear functional with respect to $d$
(cyclicity), so it descends to $E_\infty$.  The Mittag-Leffler sum
is the pairing of $\int_A$ with $E_\infty$, transported from
the singular fibres $\{\zeta_\ell\}$ to the regular fibre $q_0$:
**the mass is the total Hochschild-type cohomology class of $T_w$
on the filtered Hecke algebra, evaluated by Cauchy kernel against
the root-of-unity support**.  This is the algebraic object that
the [mass endomorphism conjecture](#conj:mass-endomorphism)
predicts.*

**Consistency checks.**
*(i) When $T_w \in J^0(q_0) \setminus J^1(q_0)$ (the braid sits at
filtration level zero), all higher residues vanish and the formula
reduces to $\mathfrak{m} = |\int_A T_w|$ — the pure
descended case
([categorical mass as Markov trace](#prop:categorical-mass-markov)).
(ii) Finiteness of the sum follows from
$T_w \in J^{\ell(K, q_0)}(q_0) \setminus J^{\ell(K, q_0) + 1}(q_0)$
([confinement level, uniqueness](#prop:confinement-level-unique)).
(iii) Distance-to-$\zeta_\ell$ hierarchy: at $q_0 \approx 1.11$,
$|q_0 - \zeta_1| \approx 0.11$ (close) and
$|q_0 - \zeta_2| = |q_0 - (-1)| \approx 2.11$ (far), so the level-1
stratum dominates and higher strata contribute perturbatively —
consistent with the observed $\lesssim 1\%$ binding-energy
residuals on light atoms.*
