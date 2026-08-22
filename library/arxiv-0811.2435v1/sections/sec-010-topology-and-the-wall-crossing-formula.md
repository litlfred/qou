---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-010-topology-and-the-wall-crossing-formula
section_title: "Topology and the wall-crossing formula"
section_number: null
pages: 25-30
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
Here we are going to introduce a Hausdorﬀ topology on the set o f stability
data in such a way that the forgetting map
Stab(g)→ Hom(Γ, C)≃ Cn, (Z,a )↦→Z
will be a local homeomorphism. In particular Stab(g) carries a structure of
a complex manifold (in general with an uncountable number of components,
each of which is paracompact). In order to deﬁne the topology we deﬁne the
notion of a continuous family of points in Stab(g).
Let X be a topological space, x0∈X be a point, and ( Zx,ax)∈Stab(g)
be a family parametrized by X.
Deﬁnition 3 We say that the family is continuous at x0 if the following
conditions are satisﬁed:
a) The map X→ Hom(Γ, C),x↦→Zx is continuous at x =x0.
b) Let us choose a quadratic form Q0 such that (Zx0,ax0)∈ StabQ0(g).
Then there exists an open neighborhoodU0 ofx0 such that (Zx,ax)∈StabQ0(g)
for all x∈U0.
c) For any closed strict sector V such that Z(Suppax0)∩∂V =∅ the map
x↦→log AV,x,Q x∈ gV,Zx,Qx⊂
∏
γ∈Γ
gγ
25
is continuous at x = x0. Here we endow the vector space ∏
γ∈Γ gγ with the
product topology of discrete sets, and AV,x,Q x is the group element associ-
ated with (Zx,ax), sector V and a quadratic form Qx such that (Zx,ax)∈
StabQx(g).
Remark 10 Part c) of the Deﬁnition 3 means that for any γ∈ Γ \{ 0} the
component of log AV,x,Q x belonging to gγ is locally constant as a function of
x in a neighborhood of x0.
The element log( AV,x,Q x)∈ ∏
γ∈Γ gγ does not depend on Qx, e.g. we can
take Qx := Q0 for x close to x0. The continuity means informally that for
any closed triangle ∆ ⊂ R2 with one vertex at the origin, the projection of
log AV,Zx,Qx into the vector space ⊕γ∈∆ gγ does not depend on x∈X as long
as there is no element γ∈ Suppax such that Z(γ) crosses the boundary ∂∆.
It is easy to see that the above deﬁnition gives rise to a topol ogy on
Stab(g).
Proposition 1 This topology is Hausdorﬀ.
Proof. Let (Z,a ) and ( Z′,a′) be two limits of a sequence ( Zn,an) as n→
∞. We have to prove that ( Z,a ) = ( Z′,a′). It is clear that Z = Z′ since
Hom(Γ, C) is Hausdorﬀ. Let us now choose quadratic forms Q andQ′ which
are compatible with a and a′ respectively in the sense of Deﬁnition 3. Then
there exists a quadratic form Q0 such that Q0 is negative on Ker Z = KerZ′
and also Q≤ Q0,Q′≤ Q0. Then for all suﬃciently large n the form Q0 is
compatible with an.
For a generic sector V ⊂ R2 its boundary rays do not intersect Z(Γ).
By part c) of the Deﬁnition 3 we have: AV,Z,Q 0 =A′
V,Z ′,Q0 since the product∏
γ∈Γ gγ is Hausdorﬀ. Since any ray in R2 with the vertex at the origin can
be obtained as an intersection of generic sectors then we con clude thata =a′.
The Proposition is proved. ■
Let us ﬁx an element Z0∈ Hom(Γ, C) and a quadratic form Q0 compati-
ble with Z0 (i.e. negative on its kernel). We denote by UQ0,Z0 the connected
component containing Z0 in the domain {Z∈ Hom(Γ, C)| (Q0)| KerZ < 0}.
In what follows we will frequently use the following element ary observation.
Proposition 2 IfQ is a quadratic form on a ﬁnite-dimensional vector space
Γ R and Z : Γ R→ C is an R-linear map such that Q| KerZ < 0 then the
intersection{x∈ Γ R|Q(x) /greaterorequalslant0}∩ Z−1(l) is a convex cone (possibly empty)
for any ray l⊂ C with the vertex at the origin.
26
Let γ1,γ 2∈ Γ \{ 0} be two Q-linearly independent elements such that
Q0(γi) /greaterorequalslant0,Q 0(γ1 +γ2) /greaterorequalslant0,i = 1, 2. We introduce the set
WQ0
γ1,γ2 ={Z∈UQ0,Z0| R>0Z(γ1) = R>0Z(γ2)} .
In this way we obtain a countable collection of hypersurface sWQ0
γ1,γ2⊂UQ0,Z0
called the walls corresponding to Q0,γ 1,γ 2. We denote their union by W1 :=
WQ0
1 and sometimes call it the wall of ﬁrst kind (physicists call it the wall of
marginal stability).
Let us consider a continuous path Zt, 0≤t≤ 1 in UQ0,Z0 which intersects
each of these walls for ﬁnitely many values of t∈ [0, 1]. Suppose that we have
a continuous lifting path (Zt,at) of this path such that Q0 is compatible with
eachat for all 0 ≤t≤ 1. Then for any γ∈ Γ \{ 0} such that Q0(γ) /greaterorequalslant0 the
elementat(γ) does not change as long as t satisﬁes the condition
Zt(γ) /∈∪ γ1,γ2∈Γ\{0},γ 1+γ2=γWQ0
γ1,γ2 .
If this condition is not satisﬁed we say that t is a discontinuity point for γ.
For a given γ there are ﬁnitely many discontinuity points.
Notice that for each t∈ [0, 1] there exist limits
a±
t (γ) = lim
ε→0,ε> 0
at±ε(γ)
(fort = 0 or t = 1 only one of the limits is well-deﬁned). Then the continuit y
of the lifted path ( Zt,at) is equivalent to the following wall-crossing formula
which holds for any t∈ [0, 1] and arbitrary γ∈ Γ \{ 0}:
−→∏
µ∈Γ prim,Z t(µ)∈lγ,t
exp
(∑
n/greaterorequalslant1
a−
t (nµ)
)
=
= exp

 ∑
µ∈Γ prim,Z t(µ)∈lγ,t ,n /greaterorequalslant1
at(nµ)

 =
−→∏
µ∈Γ prim,Z t(µ)∈lγ,t
exp
(∑
n/greaterorequalslant1
a+
t (nµ)
)
,
where lγ,t = R>0Zt(γ), and Γ prim⊂ Γ is the set of primitive vectors. The
ﬁrst and the last products are taken in the clockwise order of Arg(Zt−ε) and
Arg(Zt+ε) respectively, where ε >0 is suﬃciently small. Moreover, for each
γ we havea−
t (γ) = a+
t (γ) = at(γ) unless there exist non-zero γ1,γ 2 such that
γ =γ1 +γ2 and Zt∈W Q0
γ1,γ2.
27
Remark 11 Informally speaking, the wall-crossing formula says that f or a
very small sector V containing the ray lγ,t the corresponding element AV ,
considered as a function of time, is locally constant in a nei ghborhood of t.
For eachγ∈ Γ\{ 0} the wall-crossing formula allows us to calculate a1(γ)
is terms of a0(γ′) for a ﬁnite collection of elements γ′∈ Γ\{ 0}. Morally it is
an inductive procedure on the ordered set of discontinuity p ointsti∈ [0, 1].
The only thing we need to check is that for each γ∈ Γ\{ 0} the computation
involves ﬁnitely many elements of Γ. For that we need some pre paration.
First we introduce a partial order on the set SQ0 = (Γ ∩Q−1
0 (R/greaterorequalslant0))× [0, 1]
generated by the following relations:
a) (γ,t ) /greaterorequalslant(γ,t′) if t /greaterorequalslantt′;
b) if γ =∑
1≤i≤mγi,Q 0(γi) /greaterorequalslant0,Zt(γi)∈ R>0Zt(γ), 1≤ i≤ m,m /greaterorequalslant2,
where not all γi belong to Q·γ, then (γ,t ) /greaterorequalslant(γi,t ) for all 1 ≤i≤m.
Lemma 1 For any (γ,t )∈SQ0 the set (γ′,t′)∈SQ0 such that (γ′,t′)≤ (γ,t )
is a ﬁnite union of sets of the form {γα}× [0,tα].
The Lemma immediately implies the desired result.
Corollary 1 The element at(γ) is a ﬁnite Lie expression of the elements
a0(γα).
Proof of the Lemma . Let us assume the contrary. Then we have an
inﬁnite sequence t1>t 2>t 3 >... such that
(γ1,t 1) /greaterorequalslanta) (γ2,t 2) /greaterorequalslantb) (γ3,t 3) /greaterorequalslanta) (γ4,t 4) /greaterorequalslantb) ... ,
where the subscript a) or b) denotes the two diﬀerent possibilities for the
partial order deﬁned above. Let t∞ = limn→∞tn. It is easy to see that there
exists a Euclidean norm ‖•‖on Γ R such that for any v1,v 2∈ Γ R satisfying
the properties Q0(vi) /greaterorequalslant0,Zt∞(v1)∈ R>0Zt∞(v2) we have the inequalities
‖vi‖<‖v1 +v2‖for i = 1, 2.
Moreover the same property holds if we replace the map Zt∞ by an addi-
tive map Z which is close to it. Then we conclude that
‖γ2n‖>‖γ2n+1‖=‖γ2n+2‖
for all suﬃciently large n. This contradicts to the fact the lattice Γ is discrete
in Γ R. The Lemma is proved. ■
28
The previous discussion allows us to lift a generic path Zt, 0≤ t≤ 1 as
above to a unique continuous path ( Zt,at)∈Stab(g), 0≤t≤ 1 which starts
at a given point ( Z0,a 0)∈ Stab(g). In other words, we have the notion of
a parallel transport along a generic path. This observation is a part of the
following more general statement.
Theorem 3 For given quadratic form Q0 and (Z0,a 0)∈ StabQ0(g) there
exists a unique continuous map φ :UZ0,Q0→Stab(g) such that it is a section
of the natural projection Stab(g)→UZ0,Q0, and φ(Z0) = (Z0,a 0).
Proof. We have already proved the existence of a lifted path ( Zt,at) for
a generic path Zt provided the beginning point Z0 is ﬁxed. What is left to
prove that the endpoint ( a1,Z 1) does not depend on a choice of the generic
path Zt. We are going to sketch the proof leaving the details for the r eader.
Let us consider an inﬁnitesimally small loop around the inte rsection point
Z of two or more walls. We would like to prove that the monodromy of the
parallel transport along the loop is trivial. There are two p ossibilities:
a) there are two diﬀerent sublattices Γ 1, Γ 2⊂ Γ of ranks /greaterorequalslant2 such that
Z(Γ i),i = 1, 2 belong to two diﬀerent lines in the plane R2;
b) there exists a sublattice Γ 3⊂ Γ such that rk Γ 3 /greaterorequalslant3 and Z(Γ 3) belongs
to a line in R2.
In the case a) the corresponding Lie subalgebras of the compl etion of
gΓ are graded by non-intersecting subsets of Γ. Hence the corre sponding
wall-crossing transformations commute.
In the case b) let us choose a decomposition R2\{ (0, 0)} =⊔1≤i≤4Vi,
whereVi, 1≤i≤ 4 are strict sectors such that R·Z(Γ 3)⊂V1⊔V3⊔{ (0, 0)}.
When we move around the inﬁnitesimally small loop the elemen t a(γ) can
change only for γ∈ Γ 3. Hence we can replace Γ by Γ 3 in all computations.
The wall-crossing formula implies that the elements AVi, 1≤ i≤ 4 do not
change along the loop (moreover, by our assumption we have AV2 =AV4 = 1).
By Remark 7 from Section 2.2 we conclude that the stability da ta with the
central charge Z′ which is close to Z are uniquely determined by Z′ and the
collection of elements AVi, 1≤i≤ 4. Hence the monodromy around the loop
is trivial.
Finally one has to check the the global monodromy around a loop in UZ0,Q0
is trivial. It follows from the fact that the fundamental gro up π1(UZ0,Q0) is
generated by the loop Z↦→Ze 2πit,t∈ [0, 1]. But the monodromy around this
loop is trivial for generic Z, because the loop does not intersect the walls. ■ .
29
We can write the wall-crossing formula in the way similar to t he one from
the Introduction. In the case of generic path we have at a disc ontinuity point
t0∈ [0, 1] a two-dimensional lattice Γ 0≃ Z2 which is projected by Zt0 into
a real line in R2. We choose an isomorphism Γ 0≃ Z2 in such a way that
Q−1
0 (R/greaterorequalslant0)∩ (Γ 0\{ 0}) is contained in Z2
>0∪ Z2
<0. Also we assume that the
orientation of Γ 0⊗ R deﬁned by Zt agrees with the one on Z2
>0 fort =t0−ε
and is opposite to it for t =t0 +ε, where ε> 0 is suﬃciently small.
Then if γ = (m,n )∈ Z2
>0, and a±
t0(γ) := a±(m,n ), we can write the the
wall-crossing formula in the following way:
−→∏
(m,n)=1
exp
(∑
k/greaterorequalslant1
a−(km,kn )
)
=
←−∏
(m,n)=1
exp
(∑
k/greaterorequalslant1
a+(km,kn )
)
,
where in the LHS we take the product over all coprime m,n in the increasing
order ofm/n∈ Q, while in the RHS we take the product over all coprime m,n
in the decreasing order. Both products are equal to exp( ∑
m,n>0at0(m,n )).
