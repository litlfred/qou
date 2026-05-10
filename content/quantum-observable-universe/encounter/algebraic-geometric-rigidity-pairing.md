**Reading.** The QOU manuscript carries two **independently
axiomatised rigidity classes**, one on each side of the
Archimedean wall.  This remark pairs them so the reader has a
single picture of why the encounter has a unique outcome.

* **Algebraic side** (§3b-cond, $\mathbb{Z}[q^{\pm 1/2}]$):
  [`SDPSlaterUniqueness`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRealUniqueness.lean)
  asserts that under Slater's condition the primal SDP optimum
  $\Phi^\ast$ is unique among feasible matrices with matching
  objective value.  Concrete instances close the interior and
  active-empty cases; the general case is a conditional class.

* **Geometric side** (§3b-cond, post-$\tau$):
  [`MostowRigidity`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/content/quantum-observable-universe/lean/QOU/Encounter/MostowRigidity.lean)
  asserts that the hyperbolic structure on a finite-volume
  complete 3-manifold is uniquely determined by its fundamental
  group.  Its volume invariant is therefore a topological
  invariant of the knot type; the volume spectrum is discrete.

These two classes are not independent statements about
unrelated objects.  They are two **realisations of the same
categorical rigidity**, joined by the
[Archimedean realisation functor](#def:archimedean-realization-functor):

$$
  \underbrace{\text{SDPSlaterUniqueness}(\Phi^\ast)}_{\text{algebraic, in } \mathbb{Z}[q^{\pm 1/2}]}
  \;\xrightarrow{\;\tau_{\mathrm{arch}}\;}\;
  \underbrace{\text{MostowRigidity}(U \setminus K)}_{\text{geometric, in } \mathbb{R}}.
$$

The
[GB--PL thimble bijection](#conj:gb-reduction-pl-thimble-bijection)
makes this arrow explicit: the active Wedderburn channels
$\mathcal{S}^\ast = \{\lambda : u_\lambda > 0\}$ on the left
correspond to the steepest-descent thimbles whose Newton flow
realises the unique hyperbolic structure on the right.

**Operationally** this means a derivation can choose either
side as its primary tool:

* When working in $\mathbb{Z}[q^{\pm 1/2}]$ — Hecke spectra,
  Markov traces, LP/SDP feasibility — invoke
  `SDPSlaterUniqueness`.
* When working post-$\tau$ — hyperbolic volumes, mass
  eigenvalues, observed spectra — invoke `MostowRigidity`.
* The two are connected by `\tau_{\mathrm{arch}}` and must
  **never** be mixed within a single derivation step (cf.
  [pre-$\tau$ vs post-$\tau$](#rem:pre-tau-vs-post-tau)).

This is the QOU analogue of the classical observation that
strong duality on the algebraic side is "the same theorem" as
existence of a complete hyperbolic structure on the geometric
side — both are statements that no continuous obstruction
remains to selecting a unique optimum.
