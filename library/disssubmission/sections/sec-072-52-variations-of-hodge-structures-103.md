---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-072-52-variations-of-hodge-structures-103
section_title: "Variations of Hodge structures 103"
section_number: 5.2
pages: 111-113
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
this we consider the commutative diagram
YU   i //
fU %%JJJJJJJJJJJJ U×X
pU

U
where pU denotes the projection onto the ﬁrst factor and where the closed
immersioni is deﬁned byi(x,y) = (x +y,y), recalling thatYU⊂ Θ×Θ by
construction. The adjunction morphismQU×X−→i∗(QYU) deﬁnes in each
degreen≥ 0 a morphism
Hn(X,Q)⊗Q QU = RnpU∗(QU×X)−→Rn fU∗(QYU)
of polarized variations of pure Hodge structures, and this morphism induces
on each ﬁbre the restriction morphism that occurs in the weak Lefschetz
theorem. Furthermore, the involution
σ : U×X−→U×X , (x,y)↦→ (x,x−y)
preservesYU and restricts on each ﬁbreYx to the involutionσx. This being
said, we can perform the constructions from section 5.1 ﬁbre by ﬁbre to
obtain the subvariationsV±⊂ Hg−2 with the desired property. □
As we mentioned in the introduction, one of the principal goals of this
chapter will be the proof of theorem 5.1. We now explain how this will
follow from the results to be discussed in the next sections. Let us for
convenience ﬁrst recall the statement of the theorem.
THEOREM 5.1. For a general complex ppav X of dimension g= 4 the
monodromy group G of the local systemV+ is either the Weyl group W(E6)
or its unique simple subgroup of index two which is the kernel of the sign
homomorphism sgn: W(E6)−→{±1}.
Plan of the proof. To begin with, in sections 5.3 and 5.4 we give a
detailed study of the integral cohomology and the N´eron-Severi lattices of
the smooth surfacesYx = Θ∩Θx andY+x =Yx/σx for x∈U(C). As a result
of the lattice computations it will in particular follow that if we viewV+ as
a polarized variation ofZ-Hodge structures, then its stalks can be identiﬁed
with theE6-lattice up to a rescaling of the bilinear form. Coming back to
the monodromy groupG of the underlying local system, we then deduce in
proposition 5.18 that
G≤ W(E6)
is a subgroup of the Weyl group. Once we have this upper bound, we can
proceed as follows. If equality holds, then we are done. If not, thenG must
be contained in some maximal proper subgroupM <W(E6). Now the table
104 Chapter 5 – A family of surfaces
of maximal subgroups in [23, p. 26] shows that any such subgroupM must
be conjugate to one of the following subgroups:
(a) the simple subgroupW+(E6) of index two which is the kernel of
the sign homomorphismsgn: W(E6)−→{±1},
(b) the stabilizer of a line through some minimal vector in the dual
latticeE∗
6 ={v∈ E6⊗Z Q|⟨ v,w⟩∈ Z∀w∈ E6},
(c) the stabilizer of a line through some root vector insideE6, with the
symmetric groupS6 as a subgroup of index two,
(d) three other subgroups, two of order 24·34 and one of order 27·39.
Furthermore, any proper subgroup of the simple group in(a) is by the table
of loc. cit. also contained in some of the maximal subgroups described in
cases(b), (c)or (d). So for the proof of theorem 5.1 it will sufﬁce to show
that for a general ppav the monodromy groupG cannot be contained in any
of the subgroups listed in(b), (c)and(d).
One tool for this will be the Tannakian formalism of convolution given
in chapters 2 and 3. Indeed, consider the perverse intersection cohomology
sheaf δΘ = CΘ[g−1]∈ Perv(X,C). Over the open dense subsetU⊂ X it
turns out that the local system underlyingV+ can be identiﬁed with a direct
summand of the convolution
δΘ∗δΘ∈ Db
c (X,C),
as we will show in section 5.6. Since for a general ppav of dimensiong = 4
we know the Tannaka groupG(δΘ) =Sp24(C) from theorem 4.2, it will then
follow via the representation theory of the symplectic group that the local
system underlyingV+ is irreducible — in other words, the monodromy
group G acts irreducibly on the stalksE6⊗Z C of this local system, see
proposition 5.23. HenceG cannot be contained in the stabilizer of a line as
described in the above cases(b) or (c).
The remaining cases cannot be excluded with the same argument, in fact
some of the subgroups in case(d) act irreducibly onE6⊗Z C. An example
is given in appendix C. However, a look at the group orders shows that the
maximal subgroups in case(d) do not contain the alternating groupA6 as a
subgroup, so the proof of theorem 5.1 will be ﬁnished if we can show that
for a general ppav there exists an embedding
A6 ↪→ G.
For this we use a degeneration argument to ﬁll in the dotted lines in the
following Hasse diagram, whereG(d2) is the Galois group of the difference
