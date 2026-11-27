---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-014-41-bethe-ansatz-and-the-identification-of-scalin
section_title: "Bethe-ansatz and the identification of scaling states"
section_number: 4.1
pages: 17-18
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
When q not a root of unity, and the resonance criterion (11) is not satisﬁed, the XXZ Hamiltonian can be fully
diagonalized using a basis of orthonormal Bethe states (see [48,49] and references therein). The corresponding
Bethe equations are of the form
Nλj = 2πIj +φ−
∑
k⁄=j
ΘXXZ(λj,λk), (78)
for j = 1, 2,..., N
2 −Sz, and are obtained (after some rewriting) by taking the logarithm of (154) as given in
Appendix B; this deﬁnes the scattering kernel Θ XXZ(λj,λk). The Bethe integers Ij corresponding to a given
solution shall play an important role in the discussion below. (Note: they are sometimes half-integers, despite
their name.) The states have energies
E({Ij}) =− γ
π sinγ

2
∑
j
(cosγ + coskj)−Ne∞

, (79)
where kj is related to the Bethe root λj by tan(γ/2) tan(kj/2) = tanh(λj), and momenta
P({Ij}) =−2π
N
∑
j
Ij + φ
N
(N
2 −Sz
)
. (80)
For future convenience we also deﬁne the rescaled lattice momentum p as
p = N
2π P (81)
such that when φ = 0, p takes integer values 0, 1,...,N − 1.
The ground state—i.e., the state of lowest energy—depends on the value of φ. It will be convenient in
what follows to identify states by their corresponding set of Bethe integers, where the ground state is given by
the symmetric, maximally packed set of integers [47]. The boundaries of this set of integers are referred to as
“edges” (by analogy with the Fermi edge in solid state physics).
The third component Sz of the spin is conserved by the Hamiltonian (19), and we can split the problem of
diagonalizing H into subsectors of ﬁxed Sz. Within a given subsector, we identify states using the diﬀerence
between their set of Bethe integers and the one of the lowest-energy state within the same subsector. As N
increases, we focus only on scaling states, that is, states for which this diﬀerencemeasured from the edge remains
ﬁxed and ﬁnite. Representing the set of integers by ﬁlled circles, the edge simply refers to the boundary between
ﬁlled and empty circles in the ground state conﬁguration, as shown here marked by
999for N = 10:
[−2,−1, 0, 1, 2] ←→ ... ◦◦◦
999•••••
999◦◦◦ ...
For a scaling state there can only be ﬁnitely many empty circles between the edges and only ﬁnitely many ﬁlled
circles outside of the edges, and both must occur only at a ﬁnite distance from one of the edges. Examples
of scaling states are provided by the “electric excitations” discussed below, where the set of integers from the
ground state is shifted by a ﬁnite amount e.
Of course, the ground states of every ﬁnite-Sz sector are scaling states, since their integers coincide with those
of the ground state but for Sz of them.6 A non-scaling state would be, in contrast, a state whose magnetization
increases with N, for instance the “ferromagnetic ground state” will all spins up, Sz = N
2 . Another example of
a non-scaling state is obtained if we make a hole for some ﬁnite integer which remains ﬁxed as N→∞ . In this
case, the diﬀerence from the ground state conﬁguration, measured from the edge, increases linearly with N.
We now wish to give a brief motivation for the conjecture (66) given above. To this purpose we ﬁrst recall
the Coulomb gas (CG) picture, where we consider a free ﬁeld compactiﬁed on a circle (see section 3.2). Our
fundamental operators are vertex operators (exponentials of the ﬁeld) and their duals (discontinuities in the
ﬁeld), with conformal weights parametrized by integers e,m called the electric and magnetic charges. The con-
formal weights corresponding to these electromagnetic excitations are shown in (35), with −e,m corresponding
to r,s as in (66).
6Strictly speaking, changing the number of integers by an odd number means altering between Ij being integers or half-integers.
We expand our deﬁnition of scaling states to take this into account.
17
In the context of the spin chain we can make a purely magnetic excitation by taking the lowest-energy state
within a sector of non-zero total magnetization Sz. This means adding to or subtracting from the number of
Bethe integers, while still keeping them symmetrical and maximally packed. An electric excitation can then
be created within any sector of Sz by shifting all Bethe integers e steps from the symmetric conﬁguration.
Examples of such primary states are shown here. We mark the middle of each row of ﬁlled circles with a bar,
which will intersect the middle circle if their number is odd. This will be helpful for the discussion of descendant
states below.
... ◦◦◦•••|••◦◦◦ ... ↔ ground state
... ◦◦◦••|••◦◦◦ ... ↔ a magnetic excitation (m = 1)
... ◦◦◦◦•••|••◦◦ ... ↔ an electric excitation (e = 1)
... ◦◦•••|••◦◦◦◦ ... ↔ an electric excitation (e =−1)
... ◦◦◦◦••|••◦◦ ... ↔ an electromagnetic excitation (e = 1,m = 1)
... ◦◦••|••◦◦◦◦ ... ↔ an electromagnetic excitation (e =−1,m = 1)
Note that the magnetic excitation changes the number of ﬁlled circles; this corresponds to alternating
between having a set of integers or a set of half-integers.
From (80) we see that an electric excitation corresponds to a change in momentum. Here we also see that
if we introduce twisted boundary conditions, eφ =φ/2π enters on the same footing as e. This mirrors how in
the CG picture a twist can be implemented by inserting electric charges at inﬁnity. 7 With the identiﬁcation
e↔− (e−eφ) and m↔ Sz we claim that the scaling states corresponding to electromagnetic excitations in
the spin chain can be written in the CG picture as vertex operators Vα,¯α =:eiαϕ+i¯α ¯ϕ: of chargesα, ¯α as in (66).
Indeed, we see that with these charges we reproduce the weights (35) for CG electromagnetic excitations.
From any primary state obtained in this fashion, we must make further excitations to reach its descendants.
This is done by “creating holes” through shifting Bethe integers at the left edge (chiral excitations) or right
edge (anti-chiral excitations) of the set. Knowing that the lattice momentum must shift in accordance with the
change in conformal spin, we can easily read oﬀ which level we reach. If the level has more than one state, we
obtain an orthonormal basis for these states. To better see which excitations are chiral and which are anti-chiral
we compare to the bar inserted in the middle of the ﬁlled circles. We ﬁnd the chiral level by ﬁrst counting, for
each ﬁlled circle on the left side of the bar, the number of empty circles separating it from the bar, and then
adding up these numbers. We ﬁnd the anti-chiral level in the same manner by considering the right side of the
bar. Some examples of descendants:
... ◦◦•◦••|•••◦◦◦ ... ↔ chiral level 1
... ◦◦◦•••|••◦•◦◦ ... ↔ anti-chiral level 1
... ◦◦•◦••|••◦•◦◦ ... ↔ chiral and anti-chiral level 1
... ◦◦••◦•|•••◦◦◦ ...
... ◦•◦◦••|•••◦◦◦ ...
}
↔ chiral level 2
In practice, the Bethe integers may come in conﬁgurations where some integers coincide. We ﬁnd (via the
methods discussed in Appendix C.3) the sets of Bethe integers for all relevant scaling states based on the sets
listed in [50], in which the possibility of coinciding integers is also brieﬂy discussed. As a concrete example,
take N = 12,x = π,φ = 0 and consider the primary state that corresponds to the electromagnetic excitation
[−3,−2,−1, 0, 1]. In this case, the level-one chiral excitation does not correspond to [−4,−2,−1, 0, 1] but rather
to [−6,−1, 0, 0, 1], i.e., the integer 0 repeats. In such situations the simpliﬁed picture above fails to hold. The
way to identify the states more generally will be to look at their energy together with the sum of their Bethe
integers. A scaling state then corresponds to a state whose sum of Bethe integers is equal to the sum of a
“valid” conﬁguration, and which is also one of the low-energy states within that sector of lattice momentum.
The latter criterion can be quantiﬁed by demanding the state to be the kth excitation for somek<k 0. We only
takek0→∞ afterN→∞ , a procedure that is called the double limit in [1]. We can see from the picture above
the importance of taking N→∞ ﬁrst: to accommodate the shifts in momentum that we get from creating the
holes and shifts, we must keep N large enough.
