---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-020-141-reducible-character-in-components-of-irreduc
section_title: "Reducible character in components of irreducible type of the character variety"
section_number: 1.4.1
pages: 39-43
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
---
of the character variety
Deﬁnition 1.4.1. Let X be a one dimensional component of irreducible type of
the character variety X(M), v ∈ˆX a ﬁnite point in the smooth projective model
of X, and ρ : π1(M) →SL2(Ov) a convergent representative of the tautological re-
presentation. We will say the representation ρ is residually reducible (resp. residualy
abelian, irreducible, central) if the residual representation ¯ρ : π1(M) →SL2(k) is
reducible (resp. abelian, irreducible, central). Recall in addition that a character χ
is said central if χ(Yγ)2 = 4 for all Yγ ∈k[X].
Since X is of irreducible type, irreducible characters are dense in X hence for a
generic v ∈ˆX, the tautological representation ρ will be residually irreducible. Ne-
vertheless, there may exists a ﬁnite set of points where it is residually reducible,
they correspond to characters that are intersection points of X with a component
of reducible type of X(M).
Proposition 1.4.2. Let χ ∈X a reducible character, v ∈ˆX the associated va-
luation, and ρ : Γ →SL2(Ov) a choice of convergent tautological representation.
Then the character χ¯ρ is not central, and in particular the representation ρ is not
residually central. Moreover, one can choose the tautological representation ρ such
that it is not residually abelian.
Proof. In [Por97, Lemma 3.9], it is proved that a reducible character χ¯ρ in a com-
ponent of irreducible type X cannot be central, because there exists a non abelian
representation σ : Γ →SL2(k) with character χ¯ρ. It proves the ﬁrst claim. It remains
to show that such a non abelian representation is realized as ¯ρ, for some choice of
tautological representation ρ. We give a tree-theoretical argument.
38
Let Tv be the Bass-Serre tree associated to v, and consider the action of Γ on Tv.
— As the tautological representation is convergent, the subtree T ′
v of ﬁxed points
is non empty.
— The tree T ′
v is ﬁnite, because if not it would contain an half-line, hence from
Subsection 1.3.2 the tautological representation would ﬁx a line in ˆO2
v and it
would contradict the irreducibility of ρ.
— The tree T ′
v is a segment : assume it contains a vertex of valence at least 3
s
t
u
v
Then t, u and v represents three distincts points in kP1, ﬁxed by the residual
representation ¯ρ. Hence ¯ρ(Γ) ⊂{± Id} but it is a contradiction with the ﬁrst
part of the proposition.
— We just proved that T ′ is of the following form :
s0
s1
s2
...
sn−1
sn
Fix a basis such that si is the lattice Ov ⊕tiOv. Then for any γ ∈Γ, ρ(γ) =

a(γ) b(γ)
c(γ) d(γ)

∈SL2(Ov), with c(γ) ∈(tn). We conclude by noting that for some
γ ∈Γ, we have b(γ) ∈O∗
v ; because if not there should be an other ﬁxed point
at the left of s0. Finally, ρ is not residually abelian, and residually reducible
as soon as n > 0.
1.4.2
Alexander module
Here we recall the basic theory of Alexander module. We assume for simplicity that
M’s ﬁrst Betti number b1(M) is equal to 1, despite the theory can be extended to
higher cases. We refer to [Rol76, BZH14] for proofs and details on this theory.
We call abelianization an epimorphism ϕ : π1(M) →Z. As b1(M) = 1, there are
two possible choices for the homomorphism ϕ, but nothing we will state here will
depend on this choice. Moreover, we abuse of the term abelianization because we
omit the possibly non trivial torsion part of the abelianization of the fundamental
group.
We call the inﬁnite cyclic covering the regular covering ¯
M with deck transforma-
tion’s group Z. Let Z = ⟨t⟩, we denote by Λ the group ring Λ = Z[Z] = Z[t±1]. The
action of Z on ¯
M turns the homology groups H∗( ¯
M) into Λ-modules, and we call
39
the Λ-module H1( ¯
M) the Alexander module. Notice it is the ϕ-twisted homology of
M with coeﬃcient in Λ.
Proposition 1.4.3. The Λ-modules Hi( ¯
M) are trivial for i ≥2, H0( ¯
M) ≃Z[t±1]/(t−
1) and the Alexander module is a torsion Λ-module.
Proof. Since M has a non-empty boundary, it has the homotopy type of a two
dimensional cell complex, that can be obtained by collapsing all 3-cells adjacent to
the boundary in any cell decomposition of M, hence Hi( ¯
M) = 0 for i ≥3. Moreover,
it follows from [Jac80, Chapter V] that any presentation of π1(M) obtained from this
cell decomposition has deﬁciency one, that is π1(M) = ⟨x1, . . . , xn|r1, . . . , rn−1⟩and
one can assume that ϕ(x1) is a generator of Z. In fact this cell complex can be chosen
to be composed of an unique 0-cell e0, n loops e1
1, . . . , en
1 based in e0 corresponding
to the generators x1, . . . , xn and n −1 disks e1
2, . . . , en−1
2
such that the boundary of
the disk ei
2 follows the loops {ek
1, k = 1 . . . n} as indicated by the relator ri.
Now we consider the complex C2( ¯
M) →C1( ¯
M) →C0( ¯
M), which is nothing but
Λn−1 →Λn →Λ. The ﬁrst boundary map is given by the (n × n −1) matrix
A = (φ(∂xirj))i,j, where φ : Z[Γ] →Z[Z] is the natural ring extension of the abe-
lianization homomorphism, and the operators ∂xi are the Fox derivation operators
(see [BZH14] for details). Theorem 9.10 from the given reference states that this
matrix has maximal rank, hence H2( ˜
M) = 0. The second boundary map is the line
matrix

φ(x1) −1
. . .
ϕ(xn) −1

, and the rest of the proposition follows from the
obvious fact that φ(xi) = t.
Deﬁnition 1.4.4. Let ∆M = gcd({(n −1) minors of A}) ∈Z[t±1], where A is the
matrix of the proof above (we call A a presentation matrix for H1( ¯
M). We call
this polynomial the (ﬁrst) Alexander polynomial of M. Similarly, we call ∆k(M) =
gcd({(n −k) minors of A}) ∈Z[t±1] the k-th Alexander polynomial of M.
Remark 1.4.5. It follows from the fact that A has maximal rank that none of
those polynomials are zero. A proof that they only depend on M and are in fact
topological invariants can be found in [BZH14]. Note that they are deﬁned up to a
power of t.
Proposition 1.4.6. [BZH14] The Alexander polynomial has the following proper-
ties : ∆M(t) = ∆M(t−1) and ∆M(1) = 1
The following theorem is due to Burde and DeRham [Bur67, deR67], see [HPSP01]
for a more recent treatment and improvement of the result. We give a proof of this
40
well-known fact because we did not ﬁnd it in those terms in the literature, and we
will use some similar techniques along this manuscript.
Theorem 1.4.7. Let χ ∈X be a reducible character. Then there is λ ∈k∗such
that ∆(λ2) = 0 and for all γ ∈π1(M), χ(Yγ) = λϕ(γ) + λ−ϕ(γ).
Proof. As usual we ﬁx v ∈ˆX a point in the smooth projective model such that
ν(v) = χ, and ρ : π1(M) →SL2(Ov) a convergent tautological representation,
by hypothesis it is residually reducible, and we can choose it to be not residually
abelian, by Proposition 1.4.2. Then the residual representation can be written ¯ρ(γ) =

λϕ(γ) λ−ϕ(γ)u(γ)
0
λ−ϕ(γ)

for some λ ∈k∗. We want to show that λ2 is a root of the Alexander
polynomial ∆M.
— The ﬁrst observation is that we know λ to be diﬀerent from ±1 from Propo-
sition 1.4.2.
— The group relation ¯ρ(γδ) = ¯ρ(γ)¯ρ(δ) implies that the map u : Γ →k satisﬁes
the relation u(γδ) = u(γ)+λ2ϕ(γ)u(δ), hence u ∈Z1(Γ, λ2) is a cocycle in the
λ2-twisted cohomology of the group with coeﬃcients in the ﬁeld k.
— Now we prove that the class [u] ∈H1(Γ, λ2) is trivial iﬀthe representation ¯ρ
is abelian. Since λ̸ = ±1, ¯ρ being residually abelian is equivalent to ¯ρ being
conjugated to a diagonal representation, that is to the existence of a, b, c, d ∈k
such that for all γ ∈Γ,
 
a
b
c
d
! 
λϕ(γ)
λ−ϕ(γ)u(γ)
0
λ−ϕ(γ)
!
=
 
λϕ(γ)
0
0
λ−ϕ(γ)
! 
a
b
c
d
!
It is equivalent to









aλ−ϕ(γ)u(γ) + bλ−ϕ(γ) = λϕ(γ)b
cλ(γ) = cλ−1(γ)
cλ−ϕ(γ)u(γ) + dλ−ϕ(γ) = dλ−ϕ(γ)
or



c = 0
u(γ) = b
a(λ2ϕ(γ) −1)
, that is u is a coboundary.
— Since ¯ρ is not abelian, we have proved that H1(Γ, λ2)̸ = {0}, consequently
H1(Γ, λ2)̸ = 0. But the Universal Coeﬃcients Theorem provides the isomor-
phism H1( ¯
M) ⊗Z[t,t−1]
k[t,t−1]
(t−λ2) ≃H1(M, λ2). Take A(t) ∈Mn×(n−1)(Z[t±1]) a
presentation matrix for the Alexander module H1( ¯
M), then the matrix A(λ2)
41
becomes a presentation matrix for H1(M, λ2). Since the latter is non trivial,
we deduce that ∆M(λ2), which is the greatest common divisor of the (n −1)
minors of the matrix A(λ2), is zero, and the theorem is proved.
Example 1.4.8.
1. For the trefoil knot, we recall that the tautological repre-
sentation is ρ : a 7→
 t
1
−(t2+1) −t

, b 7→

−j
0
0 −j2

. It is residually reducible
when t2 = −1. The curve ab−1 ∈Γ is a meridian (that is its abelianization
is 1), and at the reducible characters ρ(ab−1) has eigenvalue λ = ±ij2, thus
λ2 = −j, which is a root of the Alexander polynomial ∆M(t) = t2 −t + 1.
2. For the ﬁgure-eight knot, the component of irreducible type and the com-
ponent of reducible type intersect when the trace of the meridian is ±
√
5.
Thus the square of the eigenvalues are 3±
√
5
2
, the roots of the Alexander po-
lynomial ∆M(t) = t2 −3t + 1.
1.5
