Let $H_n(R, q)$ carry the confinement filtration $J^\bullet(q)$
([confinement level](#def:confinement-level)), with associated
graded algebra $\mathrm{gr}\,H_n(R, q) = \bigoplus_\ell
J^\ell(q)/J^{\ell+1}(q)$, and let $\mathrm{tr}_M$ be the Markov
trace on $H_n(R, q)$
([Jones–Markov trace](#thm:jones-markov-trace)).

**Proposition (graded-trace residue split).**
*The Markov trace admits a canonical decomposition*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \underbrace{\mathrm{tr}_{\mathrm{gr}}(T_w, q_0)}_{\text{smooth / graded}}
  \;+\;
  \underbrace{\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)}_{\text{oscillating / residue}},
$$

*where:*

1. *$\mathrm{tr}_{\mathrm{gr}}(T_w, q_0)$ is the Markov trace of the
 **image of $T_w$ in $\mathrm{gr}\,H_n(q_0)$** — i.e., the trace
 computed on the associated graded algebra, obtained by
 replacing each generator product with its leading-order term
 in the Gröbner–Shirshov filtration (no rewriting defects).*
2. *$\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)$ is the sum of
 rewriting-defect residues from
 ([GB residue spectral sum](#prop:gb-residue-spectral-sum)).
 In symbolic feeding-lemma form this is
 $\sum_{\ell \geq 1} (q_0 - \zeta_\ell)^{-1} \cdot
   \mathrm{Res}_{q=\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\ell}(T_w)]$
 — formal cyclotomic shadow, not a $\mathbb{C}$-analytic
 identity. The convergent statement is the Habiro expansion
 ([Habiro completion](#prop:full-pole-structure-mass-trace))
 of $\mathrm{tr}_M(T_w)$ minus its level-$0$ piece.*

*Both pieces are computable from $T_w$ alone; neither involves
empirical calibration.*

**Canonicity of the split.**
*The filtration $J^\bullet(q)$ makes $H_n(R, q)$ a filtered algebra
with compatible trace
([Hecke mass trace](#prop:hecke-mass-trace)). Any such filtered
trace admits the canonical splitting*

$$
  \mathrm{tr}(x)
  =
  \mathrm{tr}_{\mathrm{gr}}(\sigma(x))
  +
  \bigl[\mathrm{tr}(x) - \mathrm{tr}_{\mathrm{gr}}(\sigma(x))\bigr],
$$

*where $\sigma: J^\ell \to J^\ell/J^{\ell+1}$ is the symbol map
and the second summand — the defect of the symbol map to preserve
the trace — is precisely the residue sum above. The
decomposition is functorial in the filtered algebra and does not
depend on the choice of Gröbner–Shirshov normal form.*

**Reduction to the mass endomorphism conjecture.**
*Combining with the quantum-dilogarithm rewriting at each
stratum
([quantum dilogarithm](#cor:quantum-dilogarithm))
gives the mass of a braid as*

$$
  \mathfrak{m}(K, q_0)
  =
  |\mathrm{tr}_{\mathrm{gr}}(T_w, q_0)|
  +
  |\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)|,
$$

*which is the content predicted by the
[mass endomorphism conjecture](#conj:mass-endomorphism). The
graded piece reproduces the regular-value brane-tower formula
([mass endomorphism tower](#prop:mass-endomorphism-tower)) when
$T_w$ lies in filtration level $0$ and all cross-pair terms
commute through the symbol map; deviations between
$\mathrm{tr}_{\mathrm{gr}}$ and the regular-value expansion are
absorbed into $\mathrm{Res}_{\mathrm{GB}}$.*

**Physical interpretation of each piece.**
*The split mirrors Strutinsky's macroscopic-plus-shell
decomposition $E = \tilde E + \delta E_{\mathrm{shell}}$: the
graded trace is the categorical analogue of the liquid-drop
(macroscopic) energy, and the residue sum is the shell
correction. This is not only a formal analogy: the Strutinsky
smoothing procedure (Gaussian convolution of the single-particle
spectrum) is the physics shadow of the symbol map $\sigma$ on
$\mathrm{gr}\,H_n(R, q)$, and the oscillating $\delta E_{\mathrm{shell}}$
is the residue contribution from filtration strata that the
smoothing collapses. The precise identification is made in
([Strutinsky from graded trace](#rem:strutinsky-from-graded-trace)).*

**Cohomological form.**
*In the spectral-sequence formulation of
([GB residue spectral sum](#prop:gb-residue-spectral-sum)),
$\mathrm{tr}_{\mathrm{gr}}$ is the pairing with the $E^\infty$
page restricted to filtration level $0$; $\mathrm{Res}_{\mathrm{GB}}$
is the pairing with the higher strata. The full Markov trace is
the pairing with all of $E^\infty$, i.e., the total
Hochschild-type cohomology class of $T_w$.*

**Consistency checks.**
*(i) If $T_w \in J^0 \setminus J^1$ then $\mathrm{Res}_{\mathrm{GB}}
= 0$ and $\mathrm{tr}_M = \mathrm{tr}_{\mathrm{gr}}$; recovers the
pure-descended case
([categorical mass as Markov trace](#prop:categorical-mass-markov)).
(ii) The split is additive under braid concatenation: for
commuting braids $T_{w_1}, T_{w_2}$ in the same stratum, the two
pieces add separately.
(iii) The split is multiplicatively stable under tensor products
of atoms only on the graded part; the residue part picks up
cross-terms, which is consistent with the observed
non-multiplicativity of shell corrections across nucleon
boundaries.*
