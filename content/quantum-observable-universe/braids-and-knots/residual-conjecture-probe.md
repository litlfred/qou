**Remark (probe).**
The residual conjecture
([conj:genus-2-ansatz](#conj:genus-2-ansatz)) reduces to two
structural hypotheses on the commutative-limit base manifold $X$:

- (i) hyperellipticity,
- (ii) faithful $\mathbb{Z}_5$ Bring-residual automorphism.

We examine each in turn, asking whether it is conjectural
irreducibly or further reducible to a smaller assumption.

## Probe of (i): hyperellipticity

**Structural hint.**  The fibre-adjoint involution
$\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$
of [prop:fiber-adjoint-involution](#prop:fiber-adjoint-involution)
gives a canonical $\mathbb{Z}_2$ involution on the projective-line
fibre $\mathbb{P}^1(\mathbb{C}) \cong \mathcal{S}_p$.  A hyperelliptic
curve is by definition a smooth projective curve admitting a degree-$2$
cover of $\mathbb{P}^1$ with associated involution; thus (i) asks
that a $\mathbb{Z}_2$ structure visible on each fibre lift to a
global $\mathbb{Z}_2$ action on $X$.

**What is provable.**  Given a smooth family of fibres each carrying
$\sigma$ and a compatibility condition across fibres, one can
construct a global $\mathbb{Z}_2$-action $\iota$ on $X$ with
$\pi \colon X \to X/\iota$ a degree-$2$ cover.  If $X/\iota$ is rational
(genus $0$), $X$ is hyperelliptic.  The compatibility-across-fibres
requirement is the non-trivial input --- it amounts to a
choice of $\mathbb{Z}_2$-equivariant lift of the fibre involutions,
which a reader of
[def:commutative-qou](#def:commutative-qou) may or may not accept as
automatic.

**What is genuinely conjectural.**  That the base manifold
$X$ that emerges from the commutative limit carries this global
$\mathbb{Z}_2$-lift, as opposed to, say, a $\mathbb{Z}_4$-lift (giving
a more specialised cyclic cover) or no lift at all (giving no
hyperelliptic structure).  The hyperellipticity hypothesis (i)
restricts the possible substrate topology to curves admitting this
particular lift.  It is plausible but not forced by the axioms.

## Probe of (ii): the $\mathbb{Z}_5$-residual from Bring

**Structural hint.**  Bring's surface has automorphism group $S_5$.
The commutative-limit specialisation restricts to an *abelian*
subgroup of $S_5$, since commutativity of $A$ is dual to an abelian
gauge structure.  The abelian subgroups of $S_5$ are, up to
conjugacy:

| Subgroup | Order | Cycle type generator |
|----------|-------|----------------------|
| $\{e\}$ | $1$ | --- |
| $\mathbb{Z}_2$ | $2$ | $(12)$ or $(12)(34)$ |
| $\mathbb{Z}_3$ | $3$ | $(123)$ |
| $V_4 = \mathbb{Z}_2 \times \mathbb{Z}_2$ | $4$ | $(12)(34), (13)(24)$ |
| $\mathbb{Z}_4$ | $4$ | $(1234)$ |
| $\mathbb{Z}_5$ | $5$ | $(12345)$ |
| $\mathbb{Z}_6$ | $6$ | $(12)(345)$ |

Of these, only $\mathbb{Z}_5 = \langle (12345) \rangle$ acts
*transitively* on the five coordinate axes of Bring's
$\mathbb{P}^4$-embedding.  Transitivity on the coordinates is the
abelian analogue of the $S_5$-symmetric treatment of all five
coordinates on equal footing --- no coordinate privileged.

**What is reducible.**  (ii) as stated is equivalent under
transitivity to the simpler hypothesis:

> (ii$'$) The commutative-limit automorphism group acts *transitively*
> on the five coordinates of Bring's $\mathbb{P}^4$-embedding.

Because only $\mathbb{Z}_5 \subset S_5$ is both abelian and transitive
on $5$ coordinates, (ii$'$) implies (ii).  Conversely (ii) trivially
implies transitivity.  The reduction is therefore exact.

**What is genuinely conjectural.**  That the commutative-limit
theory inherits transitive action on the five Lagrange-coordinate
axes from the full non-commutative Bring framework.  This is
defensible on parsimony grounds (it says "no coordinate is
privileged in the abelian limit") but is not a theorem of
`def:commutative-qou`.  A theory in which commutativity were
compatible with a privileged coordinate (breaking transitivity)
would instead select a different abelian subgroup such as
$\mathbb{Z}_4$ or $V_4$, giving a different and non-minimal
base surface.

## Summary of the irreducible core

After the probe, the residual conjecture reduces to two unrelated
structural hypotheses:

| Hypothesis | Content | Status |
|------------|---------|--------|
| (i) | Fibre $\mathbb{Z}_2$ lifts to global $\iota$ on $X$ | Plausible; not forced |
| (ii$'$) | Commutative limit retains transitivity on Bring's 5 coordinates | Plausible; not forced |

Neither follows from the present axioms for a commutative QOU.
Each is a testable structural assumption: a failure of the
downstream Solomon-seal saturation
([conj:torus-knot-seifert-bound](#conj:torus-knot-seifert-bound))
or of the single $\mathrm{U}(1)$-tube prediction
([rem:u1-phase-tube](#rem:u1-phase-tube)) would implicate one or
the other.

**Remaining paths to full derivation.**  Proving (i) would likely
require an extension of `def:commutative-qou` with an explicit
fibre-to-base descent axiom for the $\mathbb{Z}_2$ involution.
Proving (ii$'$) would require a symmetry-preservation axiom
linking the abelian limit to the transitive coordinate action of
the parent $S_5$.  Both are plausible additions that future work
may make rigorous; neither is in the paper as currently stated.
