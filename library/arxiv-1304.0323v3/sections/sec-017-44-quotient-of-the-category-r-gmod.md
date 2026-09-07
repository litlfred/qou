---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS"
section_id: sec-017-44-quotient-of-the-category-r-gmod
section_title: "Quotient of the category R-gmod"
section_number: 4.4
pages: 46-61
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
ℓ≥0
Aℓ.
Similarly, we deﬁne Abig
ℓ andAbig byAbig
ℓ = Mod gr(R(ℓ)) andAbig = ⨁
ℓ∈Z≥0
Abig
ℓ . Then
we have a functor F = ⨁
ℓ≥0Fℓ :Abig→ Mod(U′
q(ˆslN )), whereFℓ is the functor from
Abig
ℓ to Mod(U′
q(ˆslN )) given in (
3.2.1).
LetS be the smallest Serre subcategory of A (see Appendix B) such that
(1)S containsL(a,a +N) for any a∈ Z,
(2) X◦Y, Y◦X∈S for all X∈A and Y∈S .(4.4.1)
Note thatS containsL(a,b ) if b≥a +N.
Let us denote byA/S the quotient category ofA relative toS and denote byQ :A→
A/S the canonical functor. Since F sendsS to 0, the functor F :A→ U′
q(ˆslN )-mod
factors throughQ by Theorem
B.1.1 (v):
A
Q /d47/d47
F /d38/d38▼▼▼▼▼▼▼▼▼▼▼ A/S
F ′
/d15/d15
U′
q(ˆslN )-mod
for a functor F′ :A/S→ U′
q(ˆslN )-mod.
Note thatA andA/S are tensor categories with the convolution as tensor product.
The module R(0)≃ k is a unit object. Note also that Q:=qR(0) is an invertible central
object ofA/S and X↦→Q◦X≃X◦Q coincides with the grading shift functor. The
functorsQ,F andF′ are tensor functors.
Similarly, we deﬁne S big as the smallest Serre subcategory of Abig such that
(1)S big containsL(a,a +N),
(2) X◦Y, Y◦X∈S big for all X∈A big, Y∈S big,
(3)S big is stable under (not necessarily ﬁnite) direct sums.
(4.4.2)
Then we can easily see that S big∩A =S and hence we have
The functorA/S→A big/S big is fully faithful.
Proposition 4.4.1.
(a) If an object X is simple inA/S, then there exists a simple object M inA satisfying
(i)Q(M)≃X,
(ii) bk−ak +1≤N for 1≤k≤r, where
(
(a1,b 1),..., (ar,br)
)
is the multisegment
associated with M.
(b) Let
(
(a1,b 1),..., (ar,br)
)
be the multisegment associated with a simple object M in
A. If bk−ak + 1≤N for 1≤k≤r, thenQ(M) is simple in A/S.
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 47
Proof. (a) If X is simple in A/S, then there exists an irreducible module M ∈ A
such that Q(M) ≃ X by Proposition B.1.2 (b). Let
(
(a1,b 1),..., (ar,br)
)
be the
multisegment associated with M. Then M≃ hd
(
L(a1,b 1)◦···◦ L(ar,br)
)
inR(ℓ)-mod,
by Proposition 4.2.5. If bk−ak + 1 > N for some 1 ≤k≤ r, then Q(M) = 0 by the
deﬁnition of S. Since X≃Q (M) is simple, it is a contradiction.
(b) Since M is irreducible, Q(M) is zero or simple in A/S. If M≃ hd
(
L(a1,b 1)◦
···◦ L(ar,br)
)
and bk−ak + 1≤ N for all 1 ≤ k≤ r, then F (M)⁄≃0 by Theorem
4.3.3. It follows that Q(M)⁄≃0. □
We obtain the following corollary as an immediate consequence.
Corollary 4.4.2. The functor F′ :A/S→ U′
q(ˆslN )-mod sends simple objects in A/S
to simple objects in U′
q(ˆslN )-mod.
4.5. The categoryT′
J . Since all the images of L(a,a +N−1) underF′ are isomorphic
to the trivial representation of U′
q(ˆslN ), we can localize A/S one step further by using
Appendix A.6.
Set
(4.5.1) La :=L(a,a +N− 1) and ua :=u(a,a +N− 1)∈La for a∈ Z.
ThenF (La) is isomorphic to the trivial representation of U′
q(ˆslN ).
The following proposition will play a central role in the rest of this sect ion.
Proposition 4.5.1. Leta,j∈ Z and set
p = ( ǫa−ǫa+N,αj)− 2δ(a≤j≤a +N− 1)
= −δj,a−δj,a−1−δj,a+N−1−δj,a+N− 2δ(a<j <a +N− 1).
(i) The image of the morphism RLa,L(j)z : La◦L(j)z→qpL(j)z◦La is contained in
qpzδ(a≤j<a+N−1)L(j)z◦La.
(ii) The image of the morphism RL(j)z,La : L(j)z◦La→qpLa◦L(j)z is contained in
qpzδ(a<j≤a+N−1)La◦L(j)z.
(iii) If j⁄=a− 1,a +N, then the morphisms
z−δ(a≤j<a+N−1)RLa,L(j)z : La◦L(j)z→qδj,a−δj,a+N−1L(j)z◦La
and
(−1)δ(a<j≤a+N−1)z−δ(a<j≤a+N−1)RL(j)z,La : qδj,a−δj,a+N−1L(j)z◦La→La◦L(j)z
are isomorphisms and the inverses to each other.
48 S.-J. KANG, M. KASHIW ARA, M. KIM
(iv) If j =a− 1, then we have a commutative diagram with an exact row:
0 /d47/d47La◦L(a− 1)z
RLa,L(a−1)z /d47/d47
/d23 /d119
/d42/d42❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯
q−1L(a− 1)z◦La /d47/d47
/d15/d15
z−1RL(a−1)z ,La
/d15/d15
q−1L(a− 1,a +N− 1) /d47/d47 0
La◦z−1L(a− 1)z.
(v) If j =a +N, we have a commutative diagram with an exact row:
0 /d47/d47qL(a +N)z◦La
qRL(a+N)z ,La /d47/d47
/d24 /d120
/d42/d42❱❱❱❱❱❱❱❱❱❱❱❱❱❱❱❱
La◦L(a +N)z /d47/d47
/d15/d15
−z−1RLa,L(a+N)z
/d15/d15
L(a,a +N) /d47/d47 0
qz−1L(a +N)z◦La.
Proof. (i) and (ii) immediately follow from Lemma 1.5.3.
(iii) For any j∈ Z, set hj(z) = ∏
a≤k≤a+N−1,k⁄=jQj,k(z, 0). Then we can easily see
that
hj(z) =





−z2 if a<j <a +N− 1,
(−1)δ(j=a+N−1,a+N )z if j =a− 1,a,a +N− 1,a +N,
1 otherwise
which can be rewritten as
hj(z) = (−1)δ(a<j≤a+N−1)zδ(a≤j<a+N−1)+δ(a<j≤a+N−1)
for j⁄=a− 1,a +N. Then Lemma
1.3.1 (vi) implies
RLa,L(j)z◦RL(j)z,La =hj(z) idL(j)z◦La,
RL(j)z,La◦RLa,L(j)z =hj(z) idLa◦L(j)z.
(4.5.2)
Hence we obtain (iii).
(iv) By Lemma
1.5.3, we have
RLa,L(a−1)z (ua⊗u(a− 1)z) = τN··· τ1
(
u(a− 1)z⊗ua
)
.
On the other hand, we have
(τ2··· τN )
(
τN··· τ1
(
u(a− 1)z⊗ua
) )
=τ1
(
u(a− 1)z⊗ua
)
,
which implies
Im(RLa,L(a−1)z ) = R(ǫa−1−ǫa+N )τ1
(
u(a− 1)z⊗ua
)
.
Note that we have τ 2
1
(
u(a− 1)z⊗ua
)
=x1
(
u(a− 1)z⊗ua
)
. Therefore we obtain
Ker
(
L(a− 1)z◦La→L(a− 1,a +N− 1)
)
=R(ǫa−1−ǫa+N )x1
(
u(a− 1)z⊗ua
)
+R(ǫa−1−ǫa+N )τ1
(
u(a− 1)z⊗ua
)
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 49
= Im(RLa,L(a−1)z ).
The other parts are derived from RL(a−1)z,La◦RLa,L(a−1)z = z id which is obtained by
(4.5.2).
(v) is proved similarly to (vi). □
Deﬁne an abelian group homomorphism
ca : QJ→ Z
as
ca(αj) := (ǫa +ǫa+N,αj) =













0 if j⁄=a,a− 1,a +N− 1,a +N,
−1 if j =a− 1,
1 if j =a,
−1 if j =a +N− 1,
1 if j =a +N.
(4.5.3)
Then, by the preceding proposition, we obtain a homomorphism
z−δ(a≤j<a+N−1)−δj,a+NRLa,L(j)z : La◦L(j)z→qca(αj )z−1L(j)z◦La.(4.5.4)
Fora,j∈ Z, set
fa,j(z) = (−1)δj,a+Nz−δ(a≤j<a+N−1)−δj,a+N.(4.5.5)
Then we obtain the following corollary.
Corollary 4.5.2. For any a,j ∈J, the R(N + 1)-module homomorphism
fa,j(z)RLa,L(j)z : La◦L(j)z−−→qca(αj )z−1L(j)z◦La
induces an isomorphism
fa,j(z)RLa,L(j)z : La◦L(j)z−−→qca(αj )L(j)z◦La
inAbig/S big.
Remark 4.5.3. To make Corollary
4.5.2 hold, it is enough to take
fa,j(z) = cz−δ(a≤j<a+N−1)−δj,a+N
for an arbitrary c∈ k×. We take (−1)δj,a+N asc so that (ii) and (iii) in Theorem 4.5.8
below hold.
Forβ∈ Q+
J , we deﬁne commutative algebras
Pβ := ⨁
ν∈J β
k[x1,...,x ℓ]e(ν)⊂R(β),
K(β) := ⨁
ν∈J β
k[x±1
1 ,...,x ±1
ℓ ]e(ν), and
50 S.-J. KANG, M. KASHIW ARA, M. KIM
RK(β) :=K(β)⊗
Pβ
R(β)⊃R(β),
where ℓ =|β|. Set
fa,β =
∑
ν∈I β
ℓ∏
k=1
fa,νk(xk)e(ν)∈K(β)⊂RK(β).
It belongs to the center of RK(β). Hence we may consider fa,β as an R(β)-module
endomorphism of RK(β).
Since R(β)≃ ⨁
ν∈J β
(L(ν1))z1◦···◦ (L(νℓ))zℓ, we can apply the preceding proposition
to studyLa◦R(β) andR(β)◦La. Then Corollary 4.5.2 yields the following proposition.
Proposition 4.5.4. For any β∈ Q+
J , the R(ǫa−ǫa+N +β)-module homomorphism
fa,βRLa,RK (β) : La◦RK(β)→qca(β)RK(β)◦La induces an isomorphism
La◦R(β)∼−→qca(β)R(β)◦La
inAbig/S big.
Proof. By Corollary
4.5.2, the assertion holds for|β| = 1. The general case immediately
follows from this since Abig/S big is a tensor category with the convolution ◦ as tensor
product by Proposition B.1.4. □
Note that the morphism fa,βRLa,R(β) : La◦R(β)∼−→qca(β)R(β)◦La inAbig/S big com-
mutes with the right action of R(β).
Lemma 4.5.5. Let S be the automorphism of PJ = ⨁
a∈Z
Zǫa given by S(ǫa) = ǫa+N .
We deﬁne the bilinear form B on PJ by
B(x,y ) =−
∑
k>0
(Skx,y ) for x,y∈PJ .(4.5.6)
Then we have
ca(x) = B(x,ǫa−ǫa+N )−B(ǫa−ǫa+N,x )
for any x∈ QJ .
Proof. Set βa =ǫa−ǫa+N . Then we have
B(βa,x ) =−(ǫa+N,x ).
On the other hand, ∑
k∈Z(x,Skβa) = 0 implies that
B(x,βa) =−
∑
k>0
(Skx,βa) =−
∑
k>0
(x,S−kβa) =
∑
k≥0
(x,Skβa) = (x,ǫa).
□
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 51
For α∈ Q+
J , set Aα = R(α)-gmod and Sα =S∩A α. Then Sα is a Serre sub-
category of Aα and we have A/S = ⨁
α∈Q+
J
(A/S)α, where ( A/S)α =Aα/Sα. Then
Proposition
4.5.4 yields an isomorphism
qB(βa,α)La◦X ∼−→qB(α,βa)X◦La
inA/S functorial in X∈ (A/S)α.
Deﬁnition 4.5.6. We deﬁne the new tensor product ⋆ :Abig/S big×A big/S big →
Abig/S big by
X ⋆Y =qB(α,β)X◦Y≃Q⊗B(α,β)◦X◦Y,
whereX∈ (Abig/S big)α, Y∈ (Abig/S big)β and Q =q 1.
ThenAbig/S big as well as A/S is endowed with a new structure of tensor category
by⋆ as shown in Appendix A.9. With this tensor category structure, Proposition 4.5.4
can be rephrased as follows.
Lemma 4.5.7. For any a∈J and β∈ Q+
J , the
(
R(ǫa−ǫa+N−1 +β),R (β)
)
- bimodule
homomorphism
fa,βRLa,RK (β) : La⋆RK(β)−−→RK(β)⋆La
induces an isomorphism
fa,βRLa,R(β) : La⋆R (β)−−→R(β)⋆La
inAbig/S big which commutes with the right actions of R(β).
Theorem 4.5.8. The family{La}a∈J is a commuting family of central objects in A/S
(see §
A.6). Namely, the following statements hold.
(i) La is a central object in A/S (see § A.3); i.e.,
(a) fa,j(z)RLa,L(j)z induces an isomorphism in A/S
Ra(X) :La⋆X ∼−→X⋆L a
functorial in X∈A/S,
(b) the diagram
La⋆X ⋆Y
Ra(X)⋆Y /d47/d47
Ra(X⋆Y ) /d41/d41❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚ X⋆L a⋆Y
X⋆Ra(Y )
/d15/d15
X⋆Y ⋆L a
commutes inA/S for any X,Y ∈A/S.
(ii) The isomorphism Ra(La) :La⋆La ∼−→La⋆La coincides with idLa⋆La inA/S.
52 S.-J. KANG, M. KASHIW ARA, M. KIM
(iii) Fora,b∈ Z, the isomorphisms
Ra(Lb) :La⋆Lb ∼−→Lb⋆La and Rb(La) :Lb⋆La ∼−→La⋆Lb
inA/S are the inverses to each other.
Proof. (i) (a) follows from Lemma 4.5.7 and the fact that La⋆X≃
(
La⋆R (β)
)
⊗R(β)X
and X ⋆La≃
(
R(β)⋆La
)
⊗R(β)X.
(i) (b) For β,γ ∈ Q+
J (|β| =ℓ,|γ| =ℓ′), we have
(
R(β)⋆Ra(R(γ))
)
◦
(
Ra(R(β))⋆R (γ)
)(
ua⊗e(β)⊗e(γ)
)
=
(
R(β)⋆Ra(R(γ))
)
ϕℓ,Nfa,β
(
e(β)⊗ua⊗e(γ)
)
=ϕℓ,Nfa,β
(
e(β)⊗ϕℓ′,Nfa,γ(e(γ)⊗ua)
)
=ϕℓ+ℓ′,N (fa,β ⊠fa,γ)(e(β)⊗e(γ)⊗ua)
and
Ra(R(β)⋆R (γ))(ua⊗e(β)⊗e(γ)) = ϕℓ+ℓ′,Nfa,β+γ(e(β)⊗e(γ)⊗ua).
Since
fa,β+γe(β) ⊠e(γ) = (fa,β ⊠fa,γ)e(β) ⊠e(γ),
we obtain
Ra(R(β)⋆R (γ)) =
(
R(β)⋆Ra(R(γ))
)
·
(
Ra(R(β))⋆R (γ)
)
.
We obtain (i) (b) by applying ⊗R(β)X and⊗R(γ)Y for X∈A β and Y∈A γ.
If X∈ (A/S)β, we have Ra(Xz)|z=0 =Ra(X). If |β| =ℓ and x1,...,x ℓ act by 0 on
X, then we have
Ra(Xz)(ua⊗xz) =fa,β(z)RLa,Xz (ua⊗xz)
for x∈X, where fa,β(z) :=fa,β|x1=···=xℓ=z.
(ii) When X =La, we have fa,β(z) = z−(N−1) and hence
Ra(La) = Ra((La)z)|z=0 =rLa,La = idLa
by Proposition
4.2.3 (i).
(iii) By (ii), we may assume that a<b . It follows from Lemma 1.3.1 (vi) that
R(Lb)z′,(La)z◦R(La)z,(Lb)z′ =
∏
a≤i≤a+N−1,
b≤j≤b+N−1,i⁄=j
Qij(z,z′).
Set βa =ǫa−ǫa+N Then
fa,βb(z′−z) R(La)z,(Lb)z′ : (La)z⋆ (Lb)z′→ (Lb)z′⋆ (La)z
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 53
and
fb,βa(z−z′) R(Lb)z′,(La)z : (Lb)z′⋆ (La)z→ (La)z⋆ (Lb)z′
specialize to Ra(Lb) :La⋆L b ∼−→Lb ⋆L a and Rb(La) :Lb⋆L a ∼−→La⋆L b. Note that
fa,βb(z) = ∏ b+N−1
j=b fa,j(z). Hence, to prove our claim, it is enough to show that
fa,βb(z′−z)fb,βa(z−z′)
∏
a≤i≤a+N−1,
b≤j≤b+N−1,i⁄=j
Qij(z,z′) = 1.(4.5.7)
Set
A(a,b ) = {i|a≤i + 1≤a +N− 1, b≤i≤b +N− 1}
= {i|a− 1≤i≤a +N− 2, b≤i≤b +N− 1}.
Then we have ∏
a≤i≤a+N−1,
b≤j≤b+N−1,i⁄=j
Qij(z,z′) = (z′−z)♯A(a,b)(z−z′)♯A(b,a).
Similarly, set
B(a,b ) ={i|a≤i≤a +N, i⁄=a +N− 1, b≤i≤b +N− 1}.
Then we have
fa,βb(z′−z) = (−1)δ(b≤a+N≤b+N−1)(z′−z)−♯B(a,b).
Therefore, we obtain
♯A(a,b )−♯B(a,b ) = δ(b≤a− 1≤b +N− 1)−δ(b≤a +N≤b +N− 1)
= δ(1≤a−b≤N)−δ(1≤b−a≤N),
which proves ( 4.5.7). □
By the preceding theorem,{(La,Ra)}a∈J forms a commuting family of central objects
in (A/S,⋆ ) ( § A.6). Following Appendix A.6, we localize (A/S,⋆ ) by this commuting
family. Let us denote byT′
J the resulting category (A/S)[L⋆−1
a |a∈J] . Let Υ : A/S→
T′
J be the projection functor. We denote by TJ the tensor category (A/S)[La≃ 1|a∈
J] and by Ξ : T′
J→T J the canonical functor (see § A.7 and the remark below). Thus
we have a chain of functors
A
Q
−−→A/S
Υ
−−→(A/S)[L⋆−1
a |a∈J]
Ξ
−−→(A/S)[La≃ 1|a∈J].
Remark 4.5.9. Note thatA,A/S andT′
J are QJ -graded (namely,T′
J has a decomposi-
tionT′
J = ⨁
α∈QJ
(T′
J )α, etc.). The category TJ is QJ,N-graded with QJ,N :=QJ/ ∑
a∈Z Zβa,
where βa =εa−εa+N . Note that QJ,N≃
N−1⨁
k=1
Zαk.
54 S.-J. KANG, M. KASHIW ARA, M. KIM
4.6. Rigidity of the tensor categories T′
J andTJ . In this subsection, we will show
that the tensor category T′
J is rigid; i.e., every object in T′
J has a left dual and a right
dual. The rigidity of TJ follows from this fact.
Letℓ be a non-negative integer and a∈J. We set βa =ǫa−ǫa+N andγa =βa−αa =
ǫa+1−ǫa+N . Set
Kℓ(a) :=e(αa,γa +ℓβa)L◦(ℓ+1)
a ∈R(γa +ℓβa)-gmod.
By the shuﬄe lemma, we know
L◦(ℓ+1)
a =e(αa,γa +ℓβa)L◦(ℓ+1)
a .
Hence Kℓ(a) is isomorphic to L◦(ℓ+1)
a as a vector space. For example, we have
K0(a)≃L(a + 1,a +N− 1)∈R(γa)-gmod.
Let
Lℓ(a) :=L(a)z/zℓ+1L(a)z∈R(αa)-gmod.
We denote by uℓ(a)∈Lℓ(a) the image of u(a)z∈L(a)z.
Proposition 4.6.1. Forℓ≥ 0, let us denote by z theR(γa+ℓβa)-module endomorphism
of Kℓ(a) given by the action of x1 on L◦(ℓ+1)
a . Then we have
(i) zℓ+1 = 0,
(ii) Ker z = Imzℓ =R(αa,γa +ℓβa)u⊗(ℓ+1)
a ≃K0(a)◦L◦ℓ
a ,
(iii) Ker zℓ = Imz =R(αa,γa +ℓβa)R(ℓβa,βa)u⊗(ℓ+1)
a ≃Kℓ−1(a)◦La.
Proof. Set u =u⊗(ℓ+1)
a ∈L◦(ℓ+1)
a . Then
R(αa,γa +ℓβa)u≃K0(a)◦L◦ℓ
a,
which is an irreducible R(γa + ℓβa)-module by Corollary
4.2.8. It is obvious that
R(αa,γa +ℓβa)u⊂ Kerz.
In order to show the converse inclusion, let us prove
(4.6.1) zℓτ1··· τℓN u = (−1)ℓ(τ2··· τN ) (τN +2··· τ2N )··· (τ(ℓ−1)N +2··· τℓN ) u.
If ℓ = 0, it is trivial. Set a(u,v ) = uℓ−vℓ
u−v . Then we have
xℓ
1τ1τ2··· τℓN u =
(
τ1xℓ
2−a(x1,x 2)
)
τ2··· τℓN u
=τ1τ2··· τNxℓ
N +1τN +1··· τℓN u−τ2··· τNa(0,xN +1)τN +1··· τℓN u.
By induction on ℓ, we obtain
xℓ
N +1τN +1··· τℓN u =xN +1(−1)ℓ−1(τN +2··· τ2N )··· (τ(ℓ−1)N +2··· τℓN ) u = 0,
a(0,xN +1)τN +1··· τℓN u =xℓ−1
N +1τN +1··· τℓN u
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 55
= (−1)ℓ−1(τN +2··· τ2N )··· (τ(ℓ−1)N +2··· τℓN ) u,
from which we obtain ( 4.6.1).
Since the right-hand side of ( 4.6.1) is a non-zero element of the simple R(γa +ℓβa)-
module R(αa,γa +ℓβa)u, we conclude that
R(αa,γa +ℓβa)u⊂ Kerz∩ Imzℓ.
Consider the following sequence of homomorphisms
(
Kerzℓ+1/ Kerzℓ) z
֒→
(
Kerzℓ/ Kerzℓ−1) z
֒···
z
֒→
(
Kerz2/ Kerz
) z
֒→Kerz.
Since Kerzℓ+1/ Kerzℓ ∼−→zℓ Kerz∩ Imzℓ, we have
dim
(
Kerzk/ Kerzk−1)
≥ dim
(
Kerzℓ/ Kerzℓ−1)
≥ dimK0(a)◦L◦ℓ
a
for 1≤k≤ℓ + 1. Because
dimK0(a)◦L◦ℓ
a = ((ℓ + 1)N− 1)!
(N− 1)!(N!)ℓ , and dim Kℓ(a) = ((ℓ + 1)N)!
(N!)ℓ+1 ,
we have
dim Kerzℓ+1 =
ℓ+1∑
k=1
dim
(
Kerzk/ Kerzk−1)
≥ (ℓ + 1) dimK0(a)◦L◦ℓ
a = dimKℓ(a).
It follows that
Kℓ(a) = Ker zℓ+1,
Kerzk/ Kerzk−1 ∼−−→zk−1 Kerz for 1≤ k≤ℓ + 1,
Kerz = Imzℓ≃K0(a)◦L◦ℓ
a.
Hence we get the assertions (i) and (ii).
For (iii), observe that
dimKℓ−1(a)◦La =ℓ dimK0(a)◦L◦ℓ
a,
Kℓ−1(a)◦La≃R(αa,γa +ℓβa)R(ℓβa,βa)u.
On the other hand, z|Kℓ−1(a)◦La is induced by
(
z|Kℓ−1(a)
)
◦La. It follows that
R(αa,γa +ℓβa)R(ℓβa,βa)u⊂ Kerzℓ.
Comparing the dimensions, we have
R(αa,γa +ℓβa)R(ℓβa,βa)u = Kerzℓ
as desired. □
56 S.-J. KANG, M. KASHIW ARA, M. KIM
Corollary 4.6.2. There exist a surjective homomorphism
Lℓ(a)◦Kℓ(a) ։L◦(ℓ+1)
a ,(4.6.2)
and an injective homomorphism
L◦(ℓ+1)
a ֌q−ℓ−1Kℓ(a)◦Lℓ(a)(4.6.3)
in R
(
(ℓ + 1)βa
)
-gmod.
Proof. From Proposition
4.6.1 (i), we havexℓ+1
1 = 0 on L◦(ℓ+1)
a . Hence we obtain ( 4.6.2).
Taking duals, we have by ( 1.2.3)
(
L◦(ℓ+1)
a
) ∗
֌q(γa+ℓβa,αa)Kℓ(a)∗◦Lℓ(a)∗.
Since
(
L◦(ℓ+1)
a
) ∗
≃qℓ(ℓ+1)L◦(ℓ+1)
a , Kℓ(a)∗≃qℓ(ℓ+1)Kℓ(a), and Lℓ(a)∗≃q−2ℓLℓ(a),
we obtain ( 4.6.3). □
Note that B(αa,γa) = B(αa,βa) = B(βa,βa) = 1. Hence we have
L⋆(ℓ+1)
a ≃qℓ(ℓ+1)/2L◦(ℓ+1)
a ,
Lℓ(a)⋆Kℓ(a)≃qℓ+1Lℓ(a)◦Kℓ(a).
From (4.6.2), we have
Lℓ(a)⋆Kℓ(a) ։qℓ+1− ℓ(ℓ+1)
2 L⋆(ℓ+1)
a .
Set
~Kℓ(a) :=q
(ℓ+1)(ℓ−2)
2 Kℓ(a)⋆L⋆−(ℓ+1)
a ∈T ′
J.(4.6.4)
Then we obtain a morphism in T′
J
εℓ : Lℓ(a)⋆ ~Kℓ(a)−→ 1.
Similarly, from (
4.6.3), we obtain a morphism
ηℓ : 1−→ ~Kℓ(a)⋆Lℓ(a).
Theorem 4.6.3.
(i) The object ~Kℓ(a) is a right dual to Lℓ(a) in the category T′
J and (εℓ,ηℓ) is a
quasi-adjunction (see § A.2).
(ii) The categoryT′
J andTJ are rigid tensor categories; i.e., every object has a right
dual object and a left dual object.
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 57
Proof. (i) We shall prove it by the induction on ℓ. By interpreting ~K0(a) = L0(a) = 0,
the ℓ = 0 case is obvious. Assume that ℓ > 0. By the deﬁnition, we have an exact
sequence inA
1−→q2ℓL(a)−→Lℓ(a)−→Lℓ−1(a)−→ 0.
On the other hand, by Proposition 4.6.1 (ii) and (iii) we have an exact sequence
0−→Kℓ−1(a)◦La−→Kℓ(a)
zℓ
−→q−2ℓK0(a)◦L◦ℓ
a −→ 0.(4.6.5)
Since B(γa,βa) = 0, we have
Kℓ(a)⋆La≃qℓKℓ(a)◦La,
K0(a)⋆L⋆ℓ
a ≃K0(a)◦L⋆ℓ
a ≃q(ℓ−1)ℓ/2K0(a)◦L◦ℓ
a.
Hence (
4.6.5) can be understood as
0−−→q1−ℓKℓ−1(a)⋆La−−→Kℓ(a)
zℓ
−−→q−2ℓ−(ℓ−1)ℓ/2K0(a)⋆L⋆ℓ
a −−→0.
Applying the functor ⋆
(
q
(ℓ+1)(ℓ−2)
2 L⋆−(ℓ+1)
a
)
, we have an exact sequence in T′
J
0−→ ~Kℓ−1(a)−→ ~Kℓ(a)−→q−2ℓ ~K0(a)−→ 0.
We can easily see that the following diagrams are commutative:
Lℓ(a)⋆ ~Kℓ−1(a) /d47/d47
/d15/d15
Lℓ−1(a)⋆ ~Kℓ−1(a)
εℓ−1
/d15/d15
Lℓ(a)⋆ ~Kℓ(a)
εℓ /d47/d47 1
q2ℓL(a)⋆ ~Kℓ(a) /d47/d47
/d79/d79
q2ℓL(a)⋆q−2ℓ ~K0(a),
ε0
/d79/d79
~Kℓ−1(a)⋆Lℓ−1(a) /d47/d47 ~Kℓ(a)⋆Lℓ−1(a)
1
ηℓ /d47/d47
η0
/d15/d15
ηℓ−1
/d79/d79
~Kℓ(a)⋆Lℓ(a)
/d79/d79
/d15/d15
q−2ℓ ~K0(a)⋆q 2ℓL(a) /d47/d47q−2ℓ ~K0(a)⋆Lℓ(a).
Then the assertion follows by the induction on ℓ and Lemma A.2.3.
(ii) By (i), Lℓ(a) has a right dual for every a∈ Z and ℓ∈ Z≥0. Hence an object of
the form
qsLℓ1(a1)⋆··· ⋆Lℓr (ar)⋆S
has a right dual, where S is a tensor product of copies of L⋆−1
a (a∈ Z).
Because every object X inT′
J has a resolution
P′→P→X→ 0,
where P′ and P are direct sums of objects with the above form, we conclude that X
also has a right dual.
Similarly, every object has a left dual. Note that the left dual of L(a) in T′
J is
isomorphic to q−1L(a−N + 1,a− 1)⋆L⋆−1
a−N +1. □
58 S.-J. KANG, M. KASHIW ARA, M. KIM
Now we will show that the functor F′ :A/S→ U′
q(ˆslN )-mod factors throughTJ . We
need the following lemma.
Lemma 4.6.4. Forb∈J, set Vk =Vq2(b−k) (1≤k≤N), W =VN⊗VN−1⊗···⊗ V1,
and choose an epimorphism ϕ : W→ k in U′
q(ˆslN )-mod. Let
Rnorm
W,Vz : W⊗Vz→Vz⊗W
be the R-matrix obtained by the composition of normalized R- matrices
VN⊗···⊗ V1⊗Vz
Rnorm
V1 ,Vz
−−−−→VN⊗···⊗ V2⊗Vz⊗V1−−→···
Rnorm
VN ,Vz
−−−−→Vz⊗VN⊗···⊗ V1,
and let g(z) = qN−1(z−q2(b−N ))
z−q2(b−1) .
Then we have a commutative diagram
W⊗Vz
Rnorm
W,Vz /d47/d47ϕ⊗Vz
/d15/d15
Vz⊗W
Vz⊗ϕ
/d15/d15
k⊗Vz
g(z) /d47/d47Vz⊗ k.
(4.6.6)
Proof. Set W′ = V1⊗V2⊗···⊗ VN . Then there exists a U′
q(ˆslN )-module homomor-
phism r : W→W′ such that Im(r)≃ k. Thus we have a commutative diagram
W⊗Vz
Rnorm
W,Vz /d47/d47
r⊗Vz
/d15/d15
Vz⊗W
Vz⊗r
/d15/d15
W′⊗Vz
Rnorm
W ′,Vz /d47/d47
Vz⊗W′.
Since HomU ′q(g)(Vz,Vz) = k(z) and Im( r)≃ k, there exists g(z)∈ k(z) such that the
diagram ( 4.6.6) is commutative.
Set ck = q2(b−k) and choose ϕ such that ϕ((uN )cN⊗···⊗ (u1)c1) = 1. Denote by
Rnorm
k the normalized R-matrix
Rnorm
k : Vk⊗Vk−1⊗···⊗ V1⊗Vz→Vz⊗Vk⊗Vk−1⊗···⊗ V1
given inductively by Rnorm
Vk,Vz· (Vk⊗Rnorm
k−1 ).
It is enough to show that
(Vz⊗ϕ)◦Rnorm
N ((uN )cN⊗···⊗ (u1)c1⊗(u1)z) = g(z)(u1)z.(4.6.7)
We shall show
Rnorm
k
(
(uk)ck⊗···⊗ (u1)c1⊗(u1)z
)
∈ qk−1(z−ck)
z−c1
(u1)z⊗(uk)ck⊗···⊗ (u1)c1 + ∑
1<j≤N (uj)z⊗Vk−1⊗···⊗ V1
(4.6.8)
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 59
by induction on k. It is trivial if k = 1. Assume that k >1. Then by ( 4.1.1), we have
Rnorm(
(uk)ck⊗(u1)z
)
= q(z−ck)
z−q2ck
(u1)z⊗(uk)ck + z(1−q2)
z−q2ck
(uk)z⊗(u1)ck
= q(z−ck)
z−ck−1
(u1)z⊗(uk)ck + z(1−q2)
z−q2ck
(uk)z⊗(u1)ck
and
Rnorm(
(uk)ck⊗(uj)z
)
∈
∑
1<s≤N
(us)z⊗Vk for j >1.
Hence we obtain ( 4.6.8).
Applying Vz⊗ϕ, we obtain
(Vz⊗ϕ)◦Rnorm
N
(
(uN )cN⊗···⊗ (u1)c1⊗(u1)z
)
∈g(z)(u1)z +
∑
1<j≤N
k(uj)z,
which yields ( 4.6.7). □
Now we will choose {ci,j(u,v )}i,j∈J as promised in Remark 3.1.1. For r∈ Z, set
Ar(z) =
{
1 if r = 0,
q−r(z + 1−X(r)) otherwise,
where X(r) = q2r. Set
Br(u,v ) =
{
1 if r≤ 0,
q−r(1 +v)−qr(1 +u) if r≥ 1.
Then, for r≥ 1, we have
Br(0,z ) = Ar(z) and Br(z, 0) =−A−r(z).(4.6.9)
Theorem 4.6.5. Fork∈ Z≥0 and i,j∈ Z, set
ck,0(u,v ) =
∏
0≤s≤k,
s≡k modN
Bs(u,v )Bs−N (u,v )
Bs−1(u,v )Bs−N +1(u,v ),
ci,j(u,v ) =
{
ci−j,0(u,v ) for j≤i,
cj−i,0(v,u )−1 for j >i.
60 S.-J. KANG, M. KASHIW ARA, M. KIM
Then the diagram (A.7.1) is commutative for the functor F′ :A/S→ U′
q(ˆslN )-mod
and the commuting family of central objects {(La,Ra)}a∈J . That is, the diagram
F′(La⋆M )
F ′(Ra(M ))
/d15/d15
∼ /d47/d47F′(La)⊗F′(M)
ga⊗F ′(M )/d47/d47 k⊗F′(M)
/d40/d40◗◗◗◗◗◗◗◗◗◗◗◗
F′(M ⋆La)
∼ /d47/d47F′(M)⊗F′(La)
F ′(M )⊗ga/d47/d47F′(M)⊗ k /d47/d47F′(M)
(4.6.10)
is commutative for any isomorphism ga :F′(La)∼−→k.
Proof. First, one can easily check that {ci,j(u,v )} satisﬁes the condition (
3.1.1). It is
enough to show the commutativity of the diagram ( 4.6.10) for M =L(j)z. In this case,
we haveF′(M)≃Vaﬀ .
Set L = L(a)◦L(a + 1)◦···◦ L(a +N− 1) and W = F′(L). Then we have
Ra(L(j)z) = fa,j(z)RL,L(j)z . On the other hand, Proposition 3.2.2 implies
F′(RL,L(j)z ) =
∏
a≤k≤a+N−1
Pk,j(0,z )Rnorm
W,F ′(L(j)z ).
The above lemma implies that
F′(
Ra(L(j)z)
)
=fa,j(z)qN−1 Z−X(a)
Z−X(a +N− 1)
∏
a≤k≤a+N−1
Pk,j (0,z ) idVaﬀ,
where Z =zV and Z =X(j)(z + 1). Hence it is enough to show that
fa,j(z)qN−1 Z−X(a)
Z−X(a +N− 1)
∏
a≤k≤a+N−1
Pk,j(0,z ) = 1.(4.6.11)
Note that Pk,j (0,z ) = ck,j (0,z )(−z)δ(j=k+1). Because
fa,j(z) = (−1)δj,a+Nz−δ(a≤j<a+N−1)−δj,a+N,
it amounts to showing that
a+N−1∏
k=a
ck,j (0,z ) = ( −1)δ(a+1≤j≤a+N−1)q1−N
(
z + 1−X(a−j +N− 1)
) δ(j⁄=a+N−1)
(
z + 1−X(a−j)
) δ(j⁄=a)
= ( −1)δ(a<j≤a+N−1)Aa−j+N−1(z)
Aa−j(z)
for all a,j ∈ Z. Since ci+1,j+1(u,v ) = ci,j(u,v ) for all i,j ∈ Z, we have only to show
that
a+N−1∏
k=a
ck,0(0,z ) = (−1)δ(a<0≤a+N−1)Aa+N−1(z)
Aa(z)
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 61
for all a∈ Z.
It is straightforward to show that
a+N−1∏
k=a
ck,0(u,v ) =















Ba+N−1(u,v )
Ba(u,v ) if a≥ 0,
B−(a+N−1)(v,u )
B−a(v,u ) if a< 1−N,
Ba+N−1(u,v )
B−a(v,u ) if 1−N≤a< 0.
Then by ( 4.6.9), we obtain the desired result. □
Hence, Proposition A.7.3 implies that the functor F′ :A/S→ U′
q(ˆslN )-mod factors
throughTJ . Consequently, we obtain a functor ~F :TJ→ U′
q(ˆslN )-mod such that the
following diagram quasi-commutes:
(4.6.12) A
Q /d47/d47
F
/d43/d43❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲ A/S
Υ /d47/d47
F ′
/d40/d40◗◗◗◗◗◗◗◗◗◗◗◗◗◗ T′
J
/d15/d15
Ξ /d47/d47TJ
~F/d118/d118♠♠♠♠♠♠♠♠♠♠♠♠♠♠
U′
q(ˆslN )-mod.
Moreover, by Proposition A.7.2, we obtain
Proposition 4.6.6. The functor ~F is exact.
