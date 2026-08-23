---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-014-relation-with-the-works-of-joyce-and-of-bridgela
section_title: "Relation with the works of Joyce, and of Bridgeland and Toledano-Laredo"
section_number: null
pages: 38-43
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
land and Toledano-Laredo
Let g, Γ be as in Section 2.1. We assume that the ground ﬁeld is C. Suppose
thatC⊂ Γ R is a strict convex cone. We are interested in such stability d ata
38
(Z,a ) that Suppa⊂C∪(−C). We deﬁne D as an open subset of Hom(Γ , C)
which consists of additive maps such that C∩ Γ is mapped into the upper-
half planeH+ ={z∈ C| Im(z)> 0}. We interpret D as an open subset of
Stab(g). Every α∈ C∩ Γ gives rise to an invertible function (coordinate)
zα∈O (D)× such that zα(Z,a ) = Z(α).
Recall the pro-nilpotent Lie algebra gC =∏
γ∈C∩Γ gγ and the correspond-
ing pro-nilpotent group GC.
In the paper [32] by D. Joyce the following system of diﬀerent ial equations
for a collection of holomorphic functions ( fα)α∈C∩Γ,fα ∈ O(D)⊗ gα was
considered:
∀α∈C∩ Γ dfα =−1
2
∑
β+γ=α
[fβ,fγ] d logzβ
zγ
.
It follows that if ( fα) satisﬁes the above system of equations then the
diﬀerential 1-form
ω =
∑
α
fαd log zα∈ Ω 1(D)ˆ⊗gC :=
∏
α∈C∩Γ
(Ω 1(g)⊗ gα)
gives rise to the ﬂat connection, since
dω + 1
2 [ω,ω ] = 0 .
Moreover, setting F =∑
αfα we observe that
dF + [ω,F ] = 0 ,
i.e. F is a ﬂat section of this connection in the adjoint representa tion.
One can check by induction that there exists a unique solutio n to the
above system of diﬀerential equations (modulo constants fo r each function
fα). This means that the set of solutions is isomorphic to gC (non-canonically).
For anyn /greaterorequalslant0 and pairwise diﬀerent numbers xi∈ C\{ 0, 1}, i= 1,...,n
we introduce the following function (multilogarithm) whic h is holomorphic
when all xi lie outside of the interval [0 , 1]:
Ln(x1,...,x n) := v.p.
∫
0<t1<t2<···<tn<1
∏
1≤i≤n
dti
ti−xi
,
39
where v.p. means “principal value”. Then L0 = 1,L 1(x) = log(1 − 1/x)
where we deﬁne the branch of the logarithm by taking the cut al ong the ray
(−∞, 0).
For a given collection (fα) as above, Joyce deﬁned a collection of functions
Eα on D with values in the completed universal enveloping algebra U(gC):
Eα =
∑
n/greaterorequalslant1
∑
α1+···+αn=α
fα1...f αnIn(zα1,zα2,...,z αn) ,
where for z1,...,z n∈ C such that 0 < Imz1< Imz2<··· < Imzn we set 9
In(z1,z 2,...,z n) :=
= 2πi(−1)n−1Ln−1
(
z1
z1+···+zn
, z1+z2
z1+···+zn
,..., z1+z2+···+zn−1
z1+···+zn
)
.
One can show that in fact Eα∈ gC, and it is a locally constant along
strata of the stratiﬁcation deﬁned by the walls zβ/zγ∈ R where α =β +γ
with β,γ ∈C∩ Γ and β is not parallel to γ.
For a solution (fα) of the above system of diﬀerential equations we deﬁne
a diﬀerential 1-form on D× C∗ such that
ˆω :=
∑
α
fαevzα d log(vzα) ,
where v is the standard coordinate on C∗.
Then one checks that
dˆω + 1
2 [ˆω,ˆω] = 0 .
Let M(fα ) ∈ GC be the monodromy of the corresponding ﬂat connection
computed along a closed loop in the complex v-plane, which starts at + i∞
and goes in the anti-clockwise direction around v = 0. The ﬂatness implies
that the monodromy does not depend on the point of D.
On the other hand let us consider the element N(fα )∈GC deﬁned as
−→∏
l⊂H+
exp
( ∑
α∈C∩Γ,zα∈l
Eα
)
,
where the product is taken over all rays l⊂H + with the vertex at the origin.
9This formula was proposed in [10] as the inversion of the Joyc e formula which expressed
fα ’s in terms of Eα ’s.
40
Conjecture 2 We have M(fα ) =N(fα ).
The conjecture implies that the elementsaα :=Eα satisfy the wall-crossing
formula. The element M(fα ) is equal (in our notation) to the element AV ,
where V is a strict sector in H+ containing Z(C). We will discuss below a
sequence of identities which imply the conjecture. But we ne ed to introduce
certain functions ﬁrst.
Let ϕ : (0, 1)→ C\{ 0} be the inﬁnite contour which starts and ends at
+i∞, goes in the anti-clockwise direction and surrounds the poi nt 0 ∈ C.
With the contour ϕ we associate the following function on ( H+)n, n/greaterorequalslant1:
Kn(z1,...,z n) :=
∫
0<t1<···<tn<1
exp
(∑
1≤i≤n
ϕ(ti)zi
) ∏
1≤i≤n
ϕ′(ti)/ϕ(ti)dti .
Notice that this function can be written as a Chen iterated in tegral
Kn(z1,...,z n) =
∫
ϕ
ω1◦ω2◦···◦ ωn ,
where ωi =evzidv/v, 1≤i≤n, v∈ C\{ 0}.
Let us ﬁx n /greaterorequalslant1 and a collection of complex numbers zi∈H +, 1≤i≤n.
We call a sequence 0 = i0 <i 1<··· <i k−1<i k admissible if
Arg(z1 +··· +zi1) /greaterorequalslantArg(zi1+1 +··· +zi2) /greaterorequalslant··· /greaterorequalslantArg(zik−1+1 +··· +zik) .
For a ﬁxed admissible sequence we have a partition k =l1 +··· +lm where
l1,l 2,...,l m are the numbers of consecutive equalities in the above seque nce
of inequalities for the arguments. Let Ω k,l1,...,lm(z1,...,z n) be the set of all
admissible sequences 0 = i0 < i1 <··· < ik−1 < ik with the given partition
k = l1 +··· +lm. Under these assumptions and notation one can see that
the previous Conjecture 2 is equivalent to
Conjecture 3 We have
Kn(z1,...,z n) =
∑
Ω k,l 1,...,l m (z1,...,zn)
∏
1≤j≤m
1
lj!Ii1(z1,...,z i1)·Ii2−i1(zi1+1,...,z i2)·...
·Iik−ik−1(zik−1+1,...,z n) .
41
Indeed, for zi =zαi, i= 1,...,n the l.h.s. of the formula is the contribution
of the term fα1...f αn in the expansion of M(fα ). Similarly, the r.h.s. is the
contribution of the same term in N(fα ).
Here we give a proof of the above conjecture in the special cas e:
Proposition 5 If 0< Arg z1 <··· < Arg zn <π then
Kn(z1,...,z n) = In(z1,z 2,...,z n) .
Proof. Forn = 1 both sides are equal to 2 πi. For n /greaterorequalslant2 we proceed by
induction. First one checks directly that
dKn(z1,...,z n) =−
n−1∑
i=1
d log
(zi+1
zi
)
Kn−1(z1,...,z i +zi+1,...,z n) .
The same formula holds if we replace Kn,Kn−1 byIn,In−1 respectively. Thus
we see by induction thatKn−In =constn. We want to prove that constn = 0.
In order to do that we take zj =zj(ε), 1≤j≤n, such as follows:
z1(ε) = i + 1
ε, zn(ε) = i− 1
ε, zk(ε) = i−k, 2≤k≤n− 1 .
Here i =√−1. Then
0< Arg z1(ε)< Arg z2(ε)<··· < Arg zn(ε)<π
and|∑
1≤j≤kzj(ε)| → ∞as ε → 0 for k = 1 ,...,n − 1, and moreover
|∑
1≤j≤nzj(ε)| is a constant function of ǫ. Therefore,
In(z1(ε),...,z n(ε))→ 0
asε→ 0, since all the arguments of the function Ln−1 in the deﬁnition of In
approach inﬁnity.
Hence in order to ﬁnish the proof it suﬃces to show that
Kn(z1(ε),...,z n(ε))→ 0
as ε→ 0. Here is the sketch of the proof. 10 Notice that
∫ v2
+i∞
ev1z1(ε)dv1/v1 = 1
z1(ε)ev1z1(ε)/v2 +r1(ε) ,
10We thank Andrei Okounkov for the idea of the proof.
42
where r1(ε)→ 0 as ε→ 0. Repeating we obtain that
Kn(z1(ε),...,z n(ε)) = 1
z1(ε)
1
z1(ε) +z2(ε)... 1
z1(ε) +z2(ε) +··· +zn−1(ε)×
×
∫
ϕ
evn(z1(ε)+···+zn(ε))dvn/vn +rn(ε) ,
where the integral is taken over the contourϕ described before, and rn(ε)→ 0
as ε → 0. It follows from our choice of numbers zj(ε), 1≤ j ≤ n that
Kn(z1(ε),...,z n(ε))→ 0 as ε→ 0. ■
One can hope that the technique developed in [32] helps in pro ving the
general case.
A relationship between Joyce formulas and iterated integra ls is discussed
in [10] in a slightly diﬀerent form. In that paper the element s N(fα ) are in-
terpreted as Stokes multipliers for a diﬀerent system of diﬀ erential equations
on C (with coordinate t) with values in the Lie algebra which is an exten-
sion of gC by the abelian Lie algebra Hom(Γ , C) (an analog of the Cartan
subalgebra). It has irregular singularity at the origin giv en by Z
t2 , where Z
is the central charge of the stability structure. In fact the connection from
[10] reduces to our connection after the change of variables v = 1/t and the
conjugation by exp(−vZ ).
