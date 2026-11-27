*A :defterm[flavoured quantum observable universe]{#flavoured-quantum-observable-universe} is a
[quantum observable universe](#def:quantum-observable-universe) together with a second object
$W$ of its category, the :defterm[flavour fundamental]{#flavour-fundamental}, and the following
data:*

1. *an antisymmetrisation $\pi_3 \colon W \otimes W \otimes W \twoheadrightarrow \Lambda^3 W$,
   an epimorphism;*
2. *a flavour volume constraint, an isomorphism $\varepsilon_3 \colon \Lambda^3 W \cong \mathbf{1}$;*
3. *non-self-duality: $\mathrm{Hom}(\mathbf{1}, W \otimes W) = 0$.*

*Condition (iii) of the definition of a quantum observable universe, $\Lambda^2 V \cong \mathbf{1}$,
is kept unchanged for the fundamental $V$.*

> **Scope.** This is an **axiom datum**, not a derivation. Nothing in the framework produces
> $W$; the block postulates it. Every flavour-$\mathrm{SU}(3)$ statement proved from it ---
> the meson octet, the baryon octet and decuplet, the split-bundle hypercharge relations ---
> is a consequence of the *extended* axioms, and is labelled that way.

**Why each clause is there.** At the level of a fibre of dimension $n$, the volume constraint
$\Lambda^3 W \cong \mathbf{1}$ forces $n = 3$, exactly as $\Lambda^2 V \cong \mathbf{1}$ forces
$\dim V = 2$; the two constraints cannot hold on one fibre, so $V$ and $W$ are different
objects. The constraint alone is not enough: inside the fibre's own category the spin-$1$
object $\mathrm{Sym}^2 V$ is, at $q = 1$, three-dimensional with $\Lambda^3 \cong \mathbf{1}$, but it is
self-dual and yields $\mathrm{SO}(3)$, not $\mathrm{SU}(3)$. Clause 3 excludes it, and since
every $\mathrm{SU}(2)$ irrep is self-dual it excludes every object of the single-fibre
category ([the Schur--Weyl proposition](#prop:schur-weyl-eightfold)). So the datum asks for
genuinely new structure, which is the content of the $N = 3$ problem.

**A model of clause 3.** The octonionic colour triple realises clause 3 at the level of linear
algebra: the stabilizer $\mathfrak{su}(3) \subset \mathrm{Der}(\mathbb{O})$ of a unit imaginary
leaves no nonzero bilinear pairing $\mathbf{3} \otimes \mathbf{3} \to \mathbf{1}$ invariant.
Whether the flavour triple and the colour triple coincide is a separate open problem.

The Lean structure is `QOU.FlavouredQuantumObservableUniverse` in
`QOU/Core/FlavouredQuantumObservableUniverse.lean`, with `flavour_fibre_rank_three`,
`fibre_and_flavour_ranks` and `octonionTriple_realises_not_selfDual`.

**Clause 3 from a central phase.** Clause 3 can be traded for a reason. Let $z$ be a
monoidal natural automorphism of the identity functor that acts on $W$ by a scalar $\omega$.
Naturality on $\pi_3$ followed by $\varepsilon_3$ forces $(\omega^3 - 1)\cdot \mathrm{id}_{\mathbf{1}} = 0$,
so the volume form fixes the phase to be a cube root of unity; it is not chosen. On a morphism
$\mathbf{1} \to W \otimes W$ the same naturality gives $f = \omega^2 f$, so if $1 - \omega^2$ acts
without torsion on $\mathrm{Hom}(\mathbf{1}, W \otimes W)$, clause 3 holds. For the fundamental $V$
the degree-2 volume form forces $\omega^2 = 1$, so a central phase never separates $V$ from its
dual; degree 3 is the first degree whose volume form admits a separating phase. This is a
reduction of the datum (the phase is the $N$-ality of $\mathrm{SU}(3)$), not a derivation of $W$:
the object and the phase are still supplied. The balancing twist does not provide the phase,
because it is natural but not monoidal. Lean: `QOU/Core/FlavourCentralPhase.lean`
(`phase_pow_of_volume`, `not_selfDual_of_phase`, `fundamental_phase_cannot_separate`,
`FlavouredQuantumObservableUniverse.ofCentralPhase`), over a generic commutative ring.

**The octonions supply the phase, but only after adjoining $\sqrt 3$.** The complex structure
$J$ on the colour triple (left multiplication by a unit imaginary octonion, $J^2 = -1$,
commuting with the $\mathfrak{su}(3)$ stabiliser) gives
$\Omega = \tfrac12(\sqrt 3\, J - 1)$, which satisfies $\Omega^2 + \Omega + 1 = 0$ and so $\Omega^3 = 1$,
over any commutative ring containing $\tfrac12$ and $\sqrt 3$; it commutes with everything that
commutes with $J$. Over $\mathbb{Q}$ no element $a + bJ$ is a nontrivial cube root of unity,
since $\mathbb{Q}(J) \cong \mathbb{Q}(i)$ does not contain $\omega$. This is a phase on the colour
triple; identifying it with flavour is still open. Lean: `QOU/StandardModel/OctonionCubeRootPhase.lean`
(`cubeRootPhase_cube`, `cubeRootPhase_commute`, `colourTriple_no_rational_cubeRoot_phase`).

**On the octonionic triple the phase is colour's, not flavour's.** Any rational
$6 \times 6$ operator that commutes with three explicit generators of the colour
$\mathfrak{su}(3) \subset \mathrm{Der}(\mathbb{O})$ has the form $a + bJ$. So the commutant of
colour on the octonionic triple is the commutative field $\mathbb{Q}(J)$. Two consequences follow.
First, the phase $\Omega$ above is a function of colour's own complex structure, i.e. it is the
centre of colour $\mathrm{SU}(3)$. Second, no non-abelian flavour algebra can act on the same
six-dimensional carrier while commuting with colour, and over $\mathbb{Q}$ the commutant contains
no nontrivial cube root of unity at all. A flavour $\mathrm{SU}(3)$ that commutes with colour
therefore needs a different carrier, such as a tensor factor or another fibre. What flavour and
colour share is the abstract $\mathbb{Z}/3$ grading forced by any degree-3 volume form, not an
operator. A flavour action that does not commute with colour is not excluded by this argument.
Lean: `QOU/StandardModel/ColourTripletCommutant.lean` (`commutant_end`,
`commutant_commutative`, `no_cubeRoot_phase_in_commutant`).

**A fibre label carries the phase, and shows how little the axioms ask.** Give each object
of $\mathbf{C}$ a label in $\mathbb{Z}/3$, with labels adding under $\otimes$ and no
morphisms between different labels. For $\omega$ with $\omega^3 = 1$ the assignment
$z_{(X,g)} = \omega^{g}\,\mathrm{id}_X$ is then a central phase, and $W = (V, 1)$ has no
morphism $\mathbb{1} \to W \otimes W$ because $W \otimes W$ carries label $2$. A volume form
on $V$ lifts to one on $W$ because $1 + 1 + 1 = 0$. This works for every $V$, including
$V = \mathbb{1}$: a one-dimensional $W$ satisfies both flavour conditions. So
$\Lambda^3 W \cong \mathbb{1}$ together with non-self-duality does not force $\dim W = 3$ or a
flavour $\mathrm{SU}(3)$; those need further axioms. The label here is put in by hand, and
deriving it from the aether is still open. Lean: `QOU/Core/FlavourLabelCarrier.lean`
(`labelPhase`, `flavour_hom_unit_tensor_empty`, `flavourVolume_epi`,
`unit_flavour_meets_axioms`).
