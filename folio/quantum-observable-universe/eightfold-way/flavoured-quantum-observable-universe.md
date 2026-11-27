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
