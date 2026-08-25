---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-004-2-two-dimensions
section_title: "Two Dimensions"
section_number: 2
pages: 14-21
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 19 sections: A Hamiltonian; Instantons; Dirac Monopoles"
---
Indistinguishable Particles: Braid Group On the other hand, in two dimensions
the fundamental group of the conﬁguration space of a system ofn identical particles is given
by the more general braid group:
π1(Cn(R2))≃Bn(R2) =⟨σi, 1≤i≤n− 1|σiσi+1σi =σi+1σiσi+1,
σiσj =σjσi∀|i−j|≥ 2⟩.
Theσi are deﬁned physically by interchanging theith and (i+1)st particles counterclockwise.
In contrast to the symmetric group, not all braid group generators satisfy σ2
i = Id. The
monodromy operator/R2 matrix is deﬁned as the square of the braiding operator/R matrix.
Intuitively, two dimensional space allows for more possibilities because particles are topo-
logically pointlike. Adding a particle to a 2D surface is like poking a hole in the surface, so
loops around the hole can no longer be continuously deformed to a single point. (Note that
our motivational Aharonov-Bohm eﬀect example simulates 2D as the solenoid is inﬁnite in
length, so only 2 of the dimensions really matter. This corresponds to the fact that the
loops around a line are characterized by the fundamental group (ﬁrst homotopy group),
π1(R2\line) =π1(S1× R) = Z.)
14
Truncated Braid Group The braid group as deﬁned is inﬁnite and torsion-free (all
elements of the group have inﬁnite order). For theories with a ﬁnite symmetry group, it is
actually the truncated braid group B(m,n ), that governs the interaction of particles. These
are the braid groups on n elements with the additional condition that σm = 1 for some
ﬁnite m (m is taken to be minimal. m = 2 corresponds to the case of Sn, so the truncated
braid group is indeed a generalization of the symmetric groups.) When σ acts on physical
particles, the Hamiltonian transforms as a representation of σ (the braid operator), which
we call the R matrix. (More on this topic will be discussed in the next section.)
Distinguishable Particles: Colored (Pure) Braid Group If the particles are
distinguishable, the conﬁguration space is given by C((R2)n−D). The colored (pure) braid
groupP (m,n ), forn even, describes the fundamental group of the conﬁguration space of the
underlying manifold. (Intuitively, only monodromy operators make sense since after each
exchange the two particles have to be back in their original positions.) Formally, the pure
braid group P (m,n ) is the kernel of the homomorphism φ : Bn→ Sn mapping each braid
to the associated corresponding permutation.
Partially Colored Braid Group If the system consists of a combination of distinguish-
able particles and indistinguishable particles, then the fundamental group is the partially
colored braid group.
V. SPIN-STATISTICS CONNECTION
A. The Abelian Case
The topological approach to proving the spin-statistics connection ( [8])that depends
only on the existence of antiparticles and Lorentz invariance is useful when considering the
spins of particles in 2 dimensions. (This proof was originally proposed by Finkelstein and
Rubinstein in the case of three spatial dimensions, then adapted to the two dimensional case
by Propitius de Wild. [8]) Consider the process in which two particle/antiparticle pairs are
created from the vacuum, the particles are interchanged, then the new pairs annihilate. The
associated spacetime ribbon can be deformed via Lorentz transformations into the ribbon
for rotation of a single one of the particles by an angle of 2π about its center, as can be seen
from diagram [2]. Thus from the topological perspective, these two processes are seen to be
15
FIG. 2: Note that the eﬀect of interchanging two particles in two separate particle/antiparticle
pairs can be continuously deformed into the process under which one of the particles is rotated by
an angle of 2π about its center. Thus the two eﬀects should be topologically the same.
physically equivalent.
Thus the statistical phase factor eiθ picked up by exchanging the two particles must in
fact be equal to the spin factor e2πis obtained by rotating a particle of spin s. Note that the
procedure in the above proof is independent of whether the particles or the antiparticles are
interchanged (the same orientation results either way). Thus as an additional consequence
we obtain that the spin of the antiparticle is equal to that of the corresponding particle.
B. The Non-Abelian Case: Generalized Spin-Statistics Connection
When the group is non-abelian, the canonical spin statistics connection must be general-
ized as the topological equivalence in Fig.[3] shows. Speciﬁcally, when a composite particle
C (the result of fusion of A and B) is rotated, not only is the phase of the composite picked
up, but each of the constituents A and B are also rotated. Thus both A and B must both
be rotated back in the opposite direction, each picking up a phase.
16
FIG. 3: The Generalized Spin-Statistics Connection applies to two particle fusion in non-abelian
theories. On the left, fusion is performed after a monodromy operation. This can be continuously
deformed via Lorentz transformations to the diagram on the right, in which the particles are each
twisted by a−2π rotation before being fused, then the fusion product is twisted by 2 π.
KABC
αβγ R2 =e2πi(s(C,γ)−s(A,α)−s(B,β ))KABC
αβγ
When the two particles are the same, a square root version of the generalized Spin-
Statistics Connection is satisﬁed:
KAAC
ααγ R =ϵeπi(s(C,γ)−2s(A,α))KAAC
ααγ
VI. DETERMINING THE PARTICLES FROM THE HAMILTONIAN
A. Abelian
Consider the following action for a minimally coupled scalar ﬁeld with an Abelian sym-
metry group:
17
S =SYMH +Smatter =
∫
d3x(−1
4FµνFµν + (DµΦ)∗DµΦ−V (|Φ|)−jµAµ)
where the covariant derivative is given by DρΦ = (∂ρ +iNeAρ)Φ (i.e. the Higgs ﬁeld has
charge Ne with respect to the compact U(1) symmetry). The last term represents the
contribution from the matter ﬁelds while the others are the Yang-Mills-Higgs contribution.
Terms in the Lagrangian density that can be written as a total derivative are not included
as usually the terms cancel at the boundaries. (This is not always the case. In particular,
Chern-Simons theories contain an additional term which is a total derivative but the bound-
ary conditions still contribute precisely because there is a non-trivial topological winding
at the boundary as in the case, for instance, of axions. There is also a description of the
Fractional Quantum Hall eﬀect in terms of Chern-Simons theories. However, in this paper,
the emphasis is on topological eﬀects due solely to the ordinary Lagrangian terms.)
B. Non-Abelian Cases
In the case of the nonabelian Higgs ﬁeld, the ﬁeld tensor must be given an extra index a.
SYMH =
∫
d3x(−1
4FaµνFa
µν + (DµΦ)†·DµΦ−V (Φ))
where the covariant derivative is given, for instance, in the adjoint representation of
the nonabelian group by ( DµΦ)a = ∂µφa + gfabcAb
µΦc. Explicitly, the ﬁeld strength is
Fa
µν =∂µAa
ν−∂νAa
µ−gfabcAb
µAc
ν.
C. Determining the Particles
Note that there is spin-charge separation in the system as the ﬂux and the charge can
be measured independently (and there are both charged particles with no magnetic ﬂux
and magnetic ﬂuxes with no electric charge). A speciﬁc particle type is determined by a
conjugacy class A of the symmetry group H and a representation α of the centralizer of a
representative of that conjugacy class. (The centralizers of each element of the conjugacy
class are isomorphic, so the representation thus deﬁned is independent of the particular
representative chosen.) In particular, label the elements of each conjugacy class AC =
18
{Ah1,Ah2,...,Ahk}. Let AN denote the subgroup of H that is the centralizer for Ah1. Choose
a set of representatives of H/AN ={αv1,...,αvk}. The states
{|Ahi,αvj⟩}
then constitute a basis for the internal Hilbert space VA
α .
A bit more formally, given the ﬂux values take values in a group H, then quantum
mechanically we should consider complex combinations C[H]. The electric charge takes
values in the dual F(H). The particles thus correspond to representations of Drinfeld’s
quantum double construction applied to the Abelian algebra F(H) of functions on a ﬁnite
group H. Generators are given by combinations {Phg}h,g∈H, where Ph is the operator
projecting the ﬂux h∈ H and g∈ H corresponds to the global symmetry transformation.
The operators Ph are projections as PhPh′ = δh,h′Ph. We demonstrated earlier that the
action of the global symmetry transformations does not commute with the ﬂux projection
operators, and in fact: gPh = Pghg−1g due to ﬂux metamorphosis. Combining these two
relations we obtain the multiplication rule for two elements of the quantum double: Phg·
Ph′g′ =δh,gh′g−1Phgg. The particles permitted by a discrete gauge theory are given by unitary
irreducible representations of the quantum double. Note that since the quantum double is an
algebra, not a group, representations Π here are deﬁned not only to respect the multiplicative
structure, but are also required to be linear, i.e. addition and scalar multiplication are
preserved. Each unitary irreducible representation of D(H) is labeled uniquely by ﬁxing a
conjugacy class of the underlying group H and specifying the representation of the centralizer
of a representative element in that conjugacy class. The algebra is semisimple, i.e. it can
be decomposed into a direct sum. Thus the sum of squares of internal Hilbert spaces = the
dimension of the quantum double. (This will be used as a consistency check to conﬁrm the
explicit dimensions obtained in future sections.)
D. Changing Basis: The S-Matrix
The S-matrix implements the change of basis between the given basis of the fusion algebra
and the diagonal basis. (Such a matrix S must exist since the algebra is commutative and
associative.) Explicitly, the S matrix can be written as:
19
SAB
αβ := 1
|H|tr R−2AB
αβ
= 1
|H|
∑
Ahi∈AC,Bhj∈BC:[Ahi,Bhj ]=e
tr(α(Ax−1
i
BhA
jxi))∗tr(β(Bx−1
j
AhB
i xj))∗
In the appendices, a MAGMA program that computes the S matrix values is included.
E. Spin and the T-Matrix
The diagonal T-matrix records the information about the spins. Explicitly, the T matrix
is given by:
TAB
αβ :=δα,βδA,Be2πis(A,α)
Within each internal Hilbert space, all particles carry the same spin. Furthermore, the
only particles which have nontrivial spin are dyons with both nontrivial ﬂux and nontrivial
charge. Note that in the construction for the quantum double, by deﬁnition the conjugacy
class A representative element Ah1 commutes with all elements in the centralizer AN, so
Schur’s lemma yields:
α(Ah1) =e2πis(A,α)1α
for every irreducible representation α. This formula is implemented in the MAGMA
program to yield the values of the spin for the various anyonic particles. While this does
not distinguish between spin s = 0 and s = 1, it does the best that is possible in any
superselection sector as it is always possible to add orbital angular momentum. In the
speciﬁc groups discussed in the next section, a number of exotic spins are discovered.
F. Magnetic-Electric Charge Duality
The symmetry transformations of the second factor ( C(H)) in the quantum double con-
struction relate D(H) to the electric charge. Similarly, the ﬁrst part F (H) of D(H) yields
the magnetic ﬂuxes. Note that these are in fact dual to each other, as F (H)≃ CH∗. The
magnetic-electric charge duality is implemented by the SL(2, Z) action generated by the S
20
and T matrices. The action of theS matrix has an interpretation as a Fourier transform. [15]
