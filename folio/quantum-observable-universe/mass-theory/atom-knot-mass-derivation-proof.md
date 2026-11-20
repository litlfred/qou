**Proof.** After the pre-Archimedean / post-Archimedean simplification
(Yekutieli at finite slices replaces any geometric-leg construction
with finite-categorical Markov trace), the proof is a single
pre-Archimedean categorical pipeline, terminated by the Archimedean
realization functor. We treat the algebraic content first and then
the functor.

### Categorical (pre-Archimedean) leg

By [prop:confinement-sdp](#prop:confinement-sdp), at substrate $q_0$
the joint mass-tower SDP admits a solution whose certificate
includes, per atom $\mathfrak{H}$ of strand count $n_0$, the canonical
Hecke element $T_w \in H_{n_0}(q_0)$ in Gröbner–Shirshov normal form.
The GB-NF carries a length filtration $\ell$ and a jet-order grading
($\ell$ from Coxeter length on $S_{n_0}$; jet-order from the temporal
sequence of reductions; both certificate components verified for
small cases by the canonical formalism).

**Yekutieli at finite slice** (multiplicative integration on surfaces,
restricted to finite slicing depth = filtration grade $\leq k$):
the categorical action's holonomy on the braid $\beta$ underlying
$T_w$ factors as the finite product
$\rho(\beta) = \prod_{j} \rho(\sigma_{i_j})$. The non-abelian Stokes
identity at adjacent slices reduces to braid + Hecke quadratic
relations, which are the only $E_2$-differentials of the GB
spectral sequence ([prop:gb-spectral-sequence](#prop:gb-spectral-sequence)).
The spectral sequence collapses at $E_2$ for semisimple $H_n(q)$ at
generic $q$ ([prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse))
because no relations beyond braid + Hecke exist; $E_\infty$
identifications recover Wedderburn
([prop:e-infinity-page-identifications](#prop:e-infinity-page-identifications)).

Wedderburn for the semisimple algebra $H_n(q)$ over the splitting
field $\mathbb{Q}(q^{1/2})$ gives
$H_n(q) \cong \bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q^{1/2}))$
where $\lambda$ ranges over partitions of $n$ and $d_\lambda$ is the
dimension of the $S_n$-irreducible $\lambda$
([prop:wedderburn-trace-identity](#prop:wedderburn-trace-identity)).
Under this decomposition the Markov trace on $H_n(q)$ takes the
finite-sum form
$\mathrm{tr}_M = \sum_\lambda y_\lambda(q) \chi_\lambda$
where $y_\lambda(q) = s_{\lambda, r}(Q) / Z$ is the Wenzl-bridge
coefficient ([thm:jones-markov-trace](#thm:jones-markov-trace),
[prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure))
and $\chi_\lambda$ is the $q$-Murnaghan–Nakayama character.

**The categorical mass invariant.** Setting
$M(\mathfrak{H}) := \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w) = \nu_{\mathrm{SDP}} \cdot \sum_\lambda y_\lambda(q) \chi_\lambda(T_w)$
gives an element of $\mathbb{Q}(q)$. Every quantity is finite-sum and
exact; the spectral-sequence collapse at $E_2$ guarantees no higher
analytic content (asymptotic at roots of unity, volume conjecture,
Reeb-density integral on the cover, etc.) is needed. $\nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$
is read off as the multiplicity of $T_w$'s SDP solution in the
Wedderburn decomposition (renamed from $\rho$ to
disambiguate from the categorical density $\rho_K$ of
[Atomic mass as Markov trace of the Gröbner–Shirshov normal form](../mass-endomorphism/atomic-mass-gb-nf.md) and the Hoefsmit
irrep $\rho_\lambda$).

### Archimedean realization

The Archimedean realization functor
([def:archimedean-realization-functor](#def:archimedean-realization-functor))
sends $\mathbb{Q}(q) \to \mathbb{R}$ by evaluating at $q_0$ and fixes
the dimensional bridge so that $m_e \cdot M(\mathfrak{H})|_{q = q_0}$
has units of MeV:

$$
B(\mathfrak{H}) \;:=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0} \;=\; m_e \cdot \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w) \big|_{q = q_0} \;\in\; \mathbb{R}.
$$

This is the binding-energy prediction.

### Post-Archimedean naming (borrowed, not part of derivation)

If $K = \widehat{T_w}$ is hyperbolic then by the volume conjecture
\cite{kashaev1997,murakami-murakami2001} the asymptotic
$2\pi \lim_{N \to \infty} (1/N) \log |J_K(\zeta_N)|$ at roots of unity
$\zeta_N = e^{2\pi i / N}$ equals $\mathrm{Vol}_{\mathrm{hyp}}(K)$,
where $J_K(q) = \mathrm{tr}_M(T_w)$ is the Jones polynomial. Combined
with Mostow rigidity \cite{mostow1968} and Gromov's norm theorem
\cite{gromov1982,thurston1978}, the post-Archimedean number admits
the conventional 3-manifold-theory name $\mathrm{Vol}_{\mathrm{hyp}}(K)$.

This is **borrowed, conventional, and used only as naming**. The QOU
mass identity above does not depend on the volume conjecture in any
way: it is a finite-sum categorical statement, terminated by the
Archimedean realisation.

### Concluding identity

Combining the categorical leg and the Archimedean realisation,

$$
B(\mathfrak{H}) \;=\; m_e \cdot \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w) \big|_{q = q_0}.
$$

For hyperbolic $K = \widehat{T_w}$ this number coincides with
$\nu_{\mathrm{SDP}} \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(K)$ via the volume
conjecture, which is the conventional way of writing the same
identity. $\square$

### Methodological preconditions

The proof above presumes the joint-tower SDP is constructively in
place (step 1 of the algorithm). Within the present implementation:

- For `principled-derivation` entries (electron, proton, neutron)
 the explicit $\sigma$-words are direct (electron $\sigma_1^3$ in
 $H_2$, proton/neutron $(\sigma_1 \sigma_2^{-1})^3$ in $B_3$); steps
 2–6 of the algorithm run end-to-end. $\nu_{\mathrm{SDP}} = 1$ by definition.
- For `manual-historical` entries (${}^2$H, ${}^{3}$H, ${}^{3}$He) step 1 is pending;
 the post-Archimedean naming (volume from SnapPy) is substituted
 for the categorical Markov trace, justified by the volume
 conjecture. Re-running step 1 with the joint-tower SDP would
 replace this substitution with a principled derivation.
- For `recursive-on-⁴He` (${}^{8}$Be–${}^{40}$Ca) the recursion factors through
 the ${}^{4}$He magic-A formula and inherits its methodology.
- A volume-match search that runs *backwards* from step 6 to a
 candidate knot, bypassing step 1 entirely, is excluded: it
 reverse-engineers the knot from the AME target rather than deriving
 it from the categorical pipeline. The principled atlas
 ([prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas))
 admits no such entry.

The collapsing-spectral-sequence framing
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence),
[prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse))
is what allows step 2 (Markov trace) to be a *finite* sum: $E_\infty$-page
identifications recover Wedderburn after one nontrivial differential,
so no infinite-page resolution is needed and no asymptotic content
enters the categorical leg.
