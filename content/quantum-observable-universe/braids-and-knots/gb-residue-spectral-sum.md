Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q_0$ and Hecke algebra $H_n(R, q)$ filtered by the
confinement filtration $J^\bullet(q)$
([confinement level](#def:confinement-level)).  Let
$\Phi_q(z) = \prod_{k\geq 1}(1 - q^{-k} z)^{-1}$ be the non-perturbative
quantum dilogarithm and let $\zeta_\ell$ denote the root of unity at
which the $\ell$-th knot-operator energy degenerates,
$E_\ell(\zeta_\ell) = 0$.

This proposition is the **symbolic feeding lemma** that produces the
cyclotomic coefficients $a_m$ of the Habiro-completion proposition
([Habiro completion](#prop:full-pole-structure-mass-trace)) from
filtration-stratum residues. It is a formal identity in the
Grothendieck group of the filtered differential algebra
$(H_n(R,q), J^\bullet, d)$, **not** a complex-analytic identity on
or near $S^1$.

**Proposition (residue spectral sum, symbolic form).**
*For a knot $\mathcal{K}$ represented by the closed braid with Hecke
normal form $T_w \in A = H_n(R, q)$
([Hecke normal form](#def:hecke-normal-form)), the categorical mass
admits the symbolic decomposition*

$$
  \mathfrak{m}_{q_0, \mathcal{K}}
  \;=\;
  \underbrace{\bigl|\int_A T_w(q_0)\bigr|}_{\text{descended part } E^0}
  \;+\;
  \sum_{\ell = 1}^{\ell(\mathcal{K}, q_0)}
    r_\ell(T_w; q_0),
  \qquad
  r_\ell(T_w; q_0)
    \;=\;
    \frac{\operatorname*{Res}_{q = \zeta_\ell}\!
      \bigl[\Phi_q \cdot \mathrm{tr}_{M,\ell}(T_w)\bigr]}
    {q_0 - \zeta_\ell},
$$

*where $\mathrm{tr}_{M,\ell}$ is the induced Markov trace on the
graded piece $J^\ell(q)/J^{\ell+1}(q)$ and $\ell(\mathcal{K}, q_0)$ is the
confinement level of $\mathcal{K}$ at $q_0$. The numerators
$\operatorname{Res}_{q = \zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\ell}]$
are the **stratum residues** that feed the cyclotomic coefficients
$a_m$ of the Habiro expansion via*

$$
  \sum_{\ell \geq 1} r_\ell(T_w; q_0)
  \;\equiv\;
  \sum_{m \geq 1} a_m(T_w)\,(q_0; q_0)_m
  \pmod{\widehat{\mathbb{Z}[q]}\text{-equivalence}},
$$

*the equivalence being modulo the cyclotomic completion ideal of
([Habiro ring](#def:habiro-ring)).*

**Cohomological interpretation.**
*The filtration $J^\bullet(q)$ together with the rewriting
differential $d$ induced by the three Gröbner–Shirshov rules
(Hecke, far commutativity, Yang–Baxter) makes $H_n(R, q)$ a
filtered differential algebra. The associated spectral sequence
has*

$$
  E_1^{\ell,*} \;=\; H^*\bigl(J^\ell/J^{\ell+1},\,d\bigr),
  \qquad
  E_\infty^{\ell,*}
    \;\Longrightarrow\;
    \mathrm{gr}^\ell\,H_n(R, q).
$$

*The functional $\int_A$ is closed for $d$ (cyclicity) and so
descends to $E_\infty$. The residue $r_\ell(T_w; q_0)$ is the
pairing of $\int_A$ with the level-$\ell$ stratum: structurally,
the stratum residue is a Hochschild-cohomology class on
$J^\ell/J^{\ell+1}$ evaluated at the substrate parameter, and the
total mass is the sum of these classes — in agreement with the
[mass endomorphism conjecture](#conj:mass-endomorphism).*

**Caveat: this is a symbolic, not analytic, identity.**
*The Cauchy-kernel factor $1/(q_0 - \zeta_\ell)$ is a formal symbol
attached to each stratum, not a function on $\mathbb{C}$ analytic
at $q_0$. Because the primitive roots of unity are dense in $S^1$,
$\mathrm{tr}_M$ is **not** meromorphic on any neighbourhood of
$S^1$, and the sum $\sum_\ell r_\ell$ has no convergent
complex-analytic meaning across $S^1$. The convergent statement
is the Habiro expansion
([Habiro completion](#prop:full-pole-structure-mass-trace)); the
Cauchy-kernel form here is its $q$-adic shadow at fixed cyclotomic
truncation.*

**Reduction in the level-zero case.**
*When $T_w \in J^0(q_0) \setminus J^1(q_0)$, all higher stratum
residues vanish and the formula reduces to
$\mathfrak{m} = |\int_A T_w|$ — the pure descended case
([categorical mass as Markov trace](#prop:categorical-mass-markov)).*

**Convergent archimedean counterpart: PL thimble periods on $\mathcal{E}_q$.**
*Strict archimedean split: this proposition is intrinsically an
$R$-side statement — the residues live in the categorical base ring
$R$, and the Cauchy-kernel form $1/(q_0 - \zeta_\ell)$ is symbolic.
A **convergent** archimedean realisation does exist: under the
fibre functor $\tau \colon R \hookrightarrow \mathbb{C}$, the
filtration stratum $J^p/J^{p+1}$ maps to the geometric jet bundle
$J^p\mathcal{S}$ on $\mathcal{E}_q(\mathbb{C})$ via
([jet-GB-PL correspondence](#prop:jet-gb-pl-correspondence)),
and the residues at $\zeta_\ell \in S^1$ are replaced by
Picard–Lefschetz residues at the discriminant locus
$\{z \in \mathbb{C} : \Delta(z) = 0\}$ of the color-tube cubic
([Picard–Lefschetz thimble](#rem:picard-lefschetz-thimble)).
Because the discriminant points lie strictly off $S^1$, the
$\mathbb{C}$-side residues converge unconditionally and the sum
$\sum_p n_p \cdot \Pi^{(p)}$ is a bona fide complex-analytic
quantity — the **archimedean realisation** of the symbolic
$R$-side spectral sum.  The agreement
$\tau(\sum_\ell r_\ell) = \sum_p n_p \cdot \Pi^{(p)}$ is the
content of
([SW-period thimble equivalence](#prop:sw-period-thimble-equivalence));
the $R$-side and $\mathbb{C}$-side sums must not be conflated.*
