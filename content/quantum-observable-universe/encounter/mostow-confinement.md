**Proposition (conditional on
[`MostowRigidity`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/content/quantum-observable-universe/lean/QOU/Encounter/MostowRigidity.lean)).**
*Let $K \subset U$ be the link formed at an encounter
([approach](#sec:approach-to-exceptional-divisor)), and assume
that the merged complement $U \setminus K$ admits a complete,
finite-volume hyperbolic structure satisfying Mostow rigidity
(class field `MostowRigidity` in
`QOU.Encounter.MostowRigidity`).  Then:*

1. *(**Volume rigidity.**) The hyperbolic volume
   $\mathrm{Vol}_{\mathrm{hyp}}(U \setminus K)$ is a topological
   invariant of $K$: it depends only on the link type, not on
   any continuous parameter of the encounter.*

2. *(**Mass rigidity.**) Under the
   [Archimedean realization functor](#def:archimedean-realization-functor)
   $\tau_{\mathrm{arch}}$, the categorical mass attached to $K$
   is*

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathfrak{m}^{\mathrm{trans}}(\varrho_K)\bigr)
  \;=\;
  \rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(U \setminus K),
$$

   *and is therefore **discrete**: distinct knot types yield
   distinct mass eigenvalues with no continuous interpolation.*

3. *(**Confinement.**) The energy required to deform $K$ into a
   non-isotopic link is bounded below by the Mostow gap to the
   nearest neighbour in the discrete volume spectrum.  Particles
   are confined because there is no nearby hyperbolic structure
   they can slip into.*

The proposition is **conditional on `MostowRigidity`** (§3b-cond
pattern).  The class is axiomatised in
[`QOU.Encounter.MostowRigidity`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/content/quantum-observable-universe/lean/QOU/Encounter/MostowRigidity.lean);
The current Lean module establishes the §3b *scaffold* only:
the class fields are placeholders (`True`) and the conditional
theorem `mass_rigidity_of_mostow` is `True := trivial`.  Parts
(1)--(3) above are stated at the narrative level; their Lean
counterparts will be filled in once the class fields carry
non-trivial predicates (e.g. an equality of hyperbolic-volume
invariants and a discreteness witness).  The shape mirrors
`SDPSlaterUniqueness`
([primal uniqueness in the SDP-rank module](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRealUniqueness.lean))
when that class was first introduced — both are
conditional-class axiomatisations of a multi-week Mathlib
formalisation; concrete instances and non-trivial fields land
incrementally.

## Why this is the geometric mirror of the SDP optimum

Mostow rigidity is the **geometric face of strong duality**.  We
unpack the parallel:

| Algebraic side                 | Geometric side                     |
|--------------------------------|------------------------------------|
| Primal SDP optimum $\Phi^\ast$ | Hyperbolic structure on $U\setminus K$ |
| Slater's condition (strict feasibility) | Existence of a complete finite-volume structure |
| Strong duality (gap $= 0$)     | Steepest-descent has converged     |
| `SDPSlaterUniqueness`          | Mostow rigidity                    |
| Discreteness of $\Phi^\ast$    | Discreteness of $\mathrm{Vol}_{\mathrm{hyp}}$ |
| Wedderburn-block content       | Knot type up to homeomorphism      |

The
[GB--PL thimble bijection](#conj:gb-reduction-pl-thimble-bijection)
realises this column-by-column: the algebraic SDP datum on the
left is the $\mathbb{Z}[q^{\pm 1/2}]$-shadow of the hyperbolic
datum on the right, with the
[Archimedean realisation functor](#def:archimedean-realization-functor)
as the explicit translator.  *Mass is quantised because volume is
rigid* — and volume is rigid because Mostow's theorem leaves no
room for it to drift.

## Cited literature

The hyperbolic-rigidity framing matches the
*rigid phase* of Witten's analytic continuation of Chern--Simons
theory: in three dimensions the Chern--Simons path integral
concentrates exactly on the hyperbolic structures satisfying
Mostow rigidity.  Neumann--Zagier give the first-order behaviour
of $\mathrm{Vol}_{\mathrm{hyp}}$ near the rigid point as the
critical behaviour of an algebraic potential — the
*Neumann--Zagier potential* — whose stationary points are the
"settled" configurations.  We collect these and other
literature precedents in the
[encounter literature bridge](#rem:encounter-literature-bridge).
