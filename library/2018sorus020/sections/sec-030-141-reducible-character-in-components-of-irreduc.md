---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-030-141-reducible-character-in-components-of-irreduc
section_title: "Reducible character in components of irreducible type"
section_number: 1.4.1
pages: 39-43
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
of the character variety
Deﬁnition 1.4.1.Let X be a one dimensional component of irreducible type of
the character varietyX(M), v∈ ˆX a ﬁnite point in the smooth projective model
of X, andρ :π1(M)→ SL2(Ov) a convergent representative of the tautological re-
presentation. We will say the representationρ is residually reducible(resp. residualy
abelian, irreducible, central) if the residual representation ¯ρ : π1(M)→ SL2(k) is
reducible (resp. abelian, irreducible, central). Recall in addition that a characterχ
is said central ifχ(Yγ)2 = 4 for allYγ∈k[X].
Since X is of irreducible type, irreducible characters are dense inX hence for a
generic v∈ ˆX, the tautological representationρ will be residually irreducible. Ne-
vertheless, there may exists a ﬁnite set of points where it is residually reducible,
they correspond to characters that are intersection points ofX with a component
of reducible type ofX(M).
Proposition 1.4.2. Let χ∈ X a reducible character,v∈ ˆX the associated va-
luation, and ρ : Γ → SL2(Ov) a choice of convergent tautological representation.
Then the characterχ¯ρ is not central, and in particular the representationρ is not
residually central. Moreover, one can choose the tautological representationρ such
that it is not residually abelian.
Proof. In [Por97, Lemma 3.9], it is proved that a reducible characterχ¯ρ in a com-
ponent of irreducible typeX cannot be central, because there exists a non abelian
representationσ : Γ→ SL2(k) with characterχ¯ρ. It proves the ﬁrst claim. It remains
to show that such a non abelian representation is realized as¯ρ, for some choice of
tautological representationρ. We give a tree-theoretical argument.
38
Let Tv be the Bass-Serre tree associated tov, and consider the action ofΓ on Tv.
— As the tautological representation is convergent, the subtreeT′
v of ﬁxed points
is non empty.
— The treeT′
v is ﬁnite, because if not it would contain an half-line, hence from
Subsection 1.3.2 the tautological representation would ﬁx a line inˆO2
v and it
would contradict the irreducibility ofρ.
— The treeT′
v is a segment : assume it contains a vertex of valence at least 3
s t
u
v
Thent,u andv represents three distincts points inkP1, ﬁxed by the residual
representation ¯ρ. Hence ¯ρ(Γ)⊂{± Id} but it is a contradiction with the ﬁrst
part of the proposition.
— We just proved thatT′ is of the following form :
s0 s1 s2 ... sn−1 sn
Fix a basis such thatsi is the latticeOv⊕tiOv. Then for anyγ∈ Γ, ρ(γ) =(
a(γ) b(γ)
c(γ) d(γ)
)
∈ SL2(Ov), withc(γ)∈ (tn). We conclude by noting that for some
γ∈ Γ, we haveb(γ)∈O∗
v; because if not there should be an other ﬁxed point
at the left ofs0. Finally,ρ is not residually abelian, and residually reducible
as soon asn> 0.
1.4.2 Alexander module
Here we recall the basic theory of Alexander module. We assume for simplicity that
M’s ﬁrst Betti numberb1(M) is equal to1, despite the theory can be extended to
higher cases. We refer to [Rol76, BZH14] for proofs and details on this theory.
We callabelianization an epimorphismϕ : π1(M)→ Z. Asb1(M) = 1 , there are
two possible choices for the homomorphismϕ, but nothing we will state here will
depend on this choice. Moreover, we abuse of the term abelianization because we
omit the possibly non trivial torsion part of the abelianization of the fundamental
group.
We call theinﬁnite cyclic coveringthe regular covering ¯M with deck transforma-
tion’s groupZ. Let Z =⟨t⟩, we denote byΛ the group ringΛ = Z[Z] = Z[t±1]. The
action of Z on ¯M turns the homology groupsH∗( ¯M) into Λ-modules, and we call
39
the Λ-module H1( ¯M) the Alexander module. Notice it is theϕ-twisted homology of
M with coeﬃcient inΛ.
Proposition1.4.3. The Λ-modulesHi( ¯M) are trivial fori≥ 2,H0( ¯M)≃ Z[t±1]/(t−
1) and the Alexander module is a torsionΛ-module.
Proof. Since M has a non-empty boundary, it has the homotopy type of a two
dimensional cell complex, that can be obtained by collapsing all3-cells adjacent to
the boundary in any cell decomposition ofM, henceHi( ¯M) = 0 fori≥ 3. Moreover,
it follows from [Jac80, Chapter V] that any presentation ofπ1(M) obtained from this
cell decomposition has deﬁciency one, that isπ1(M) =⟨x1,...,x n|r1,...,r n−1⟩ and
one can assume thatϕ(x1) is a generator ofZ. In fact this cell complex can be chosen
to be composed of an unique0-cell e0, n loops e1
1,...,e n
1 based ine0 corresponding
to the generatorsx1,...,x n and n− 1 disks e1
2,...,e n−1
2 such that the boundary of
the diskei
2 follows the loops{ek
1,k = 1...n } as indicated by the relatorri.
Now we consider the complexC2( ¯M)→ C1( ¯M)→ C0( ¯M), which is nothing but
Λn−1 → Λn → Λ. The ﬁrst boundary map is given by the(n× n− 1) matrix
A = (φ(∂xirj))i,j, whereφ : Z[Γ]→ Z[Z] is the natural ring extension of the abe-
lianization homomorphism, and the operators∂xi are the Fox derivation operators
(see [BZH14] for details). Theorem 9.10 from the given reference states that this
matrix has maximal rank, henceH2( ˜M) = 0. The second boundary map is the line
matrix
(
φ(x1)− 1 ... ϕ (xn)− 1
)
, and the rest of the proposition follows from the
obvious fact thatφ(xi) =t.
Deﬁnition 1.4.4.Let ∆M = gcd({(n− 1) minors ofA})∈ Z[t±1], whereA is the
matrix of the proof above (we callA a presentation matrix for H1( ¯M). We call
this polynomial the(ﬁrst) Alexander polynomialof M. Similarly, we call∆k(M) =
gcd({(n−k) minors ofA})∈ Z[t±1] the k-th Alexander polynomialof M.
Remark 1.4.5. It follows from the fact thatA has maximal rank that none of
those polynomials are zero. A proof that they only depend onM and are in fact
topological invariants can be found in [BZH14]. Note that they are deﬁned up to a
power oft.
Proposition 1.4.6. [BZH14] The Alexander polynomial has the following proper-
ties : ∆M(t) = ∆M(t−1) and ∆M(1) = 1
The following theorem is due to Burde and DeRham [Bur67, deR67], see [HPSP01]
for a more recent treatment and improvement of the result. We give a proof of this
40
well-known fact because we did not ﬁnd it in those terms in the literature, and we
will use some similar techniques along this manuscript.
Theorem 1.4.7. Let χ∈ X be a reducible character. Then there isλ∈ k∗ such
that ∆(λ2) = 0 and for allγ∈π1(M), χ(Yγ) =λϕ(γ) +λ−ϕ(γ).
Proof. As usual we ﬁxv∈ ˆX a point in the smooth projective model such that
ν(v) = χ, and ρ : π1(M) → SL2(Ov) a convergent tautological representation,
by hypothesis it is residually reducible, and we can choose it to be not residually
abelian,byProposition1.4.2.Thentheresidualrepresentationcanbewritten ¯ρ(γ) =(
λϕ(γ) λ−ϕ(γ)u(γ)
0 λ−ϕ(γ)
)
for someλ∈k∗. We want to show thatλ2 is a root of the Alexander
polynomial ∆M.
— The ﬁrst observation is that we knowλ to be diﬀerent from±1 from Propo-
sition 1.4.2.
— The group relation¯ρ(γδ) = ¯ρ(γ)¯ρ(δ) implies that the mapu : Γ→k satisﬁes
the relationu(γδ) =u(γ) +λ2ϕ(γ)u(δ), henceu∈Z1(Γ,λ 2) is a cocycle in the
λ2-twisted cohomology of the group with coeﬃcients in the ﬁeldk.
— Now we prove that the class[u]∈H1(Γ,λ 2) is trivial iﬀ the representation¯ρ
is abelian. Sinceλ⁄=±1, ¯ρ being residually abelian is equivalent to¯ρ being
conjugatedtoadiagonalrepresentation,thatistotheexistenceof a,b,c,d ∈k
such that for allγ∈ Γ,
(
a b
c d
)(
λϕ(γ) λ−ϕ(γ)u(γ)
0 λ−ϕ(γ)
)
=
(
λϕ(γ) 0
0 λ−ϕ(γ)
)(
a b
c d
)
It is equivalent to



aλ−ϕ(γ)u(γ) +bλ−ϕ(γ) =λϕ(γ)b
cλ(γ) =cλ−1(γ)
cλ−ϕ(γ)u(γ) +dλ−ϕ(γ) =dλ−ϕ(γ)
or



c = 0
u(γ) = b
a(λ2ϕ(γ)− 1)
, that isu is a coboundary.
— Since ¯ρ is not abelian, we have proved thatH1(Γ,λ 2)⁄={0}, consequently
H1(Γ,λ 2)⁄= 0. But the Universal Coeﬃcients Theorem provides the isomor-
phism H1( ¯M)⊗Z[t,t−1]
k[t,t−1]
(t−λ2) ≃ H1(M,λ 2). TakeA(t)∈M n×(n−1)(Z[t±1]) a
presentation matrix for the Alexander moduleH1( ¯M), then the matrixA(λ2)
41
becomes a presentation matrix forH1(M,λ 2). Since the latter is non trivial,
we deduce that∆M(λ2), which is the greatest common divisor of the(n− 1)
minors of the matrixA(λ2), is zero, and the theorem is proved.
Example 1.4.8. 1. For the trefoil knot, we recall that the tautological repre-
sentation is ρ : a↦→
( t 1
−(t2+1)−t
)
,b ↦→
(
−j 0
0 −j2
)
. It is residually reducible
when t2 =−1. The curveab−1∈ Γ is a meridian (that is its abelianization
is 1), and at the reducible charactersρ(ab−1) has eigenvalueλ =±ij2, thus
λ2 =−j, which is a root of the Alexander polynomial∆M(t) =t2−t + 1.
