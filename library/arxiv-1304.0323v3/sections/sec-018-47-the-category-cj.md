---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-018-47-the-category-cj
section_title: "The Category CJ"
section_number: 4.7
pages: 61-65
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
Recall that Cg denotes the category of ﬁnite-dimensional integrable U′
q(ˆslN )-modules.
LetCJ be the full subcategory of Cg consisting of U′
q(ˆslN )-modules M such that every
composition factor of M appears as a composition factor of a tensor product of modules
of the form V (̟1)q2s (s∈ J). By the deﬁnition, CJ is abelian and is stable under
taking submodules, quotients, extensions and tensor products. Moreover,CJ contains
V (̟i)(−q)i+2s−1 for 1≤i≤N− 1 and s∈ Z. Hence ~F can be considered as an exact
functor
~F :TJ→C J.
Note that the category CJ coincides with the category CZ in [ 11].
Lemma 4.7.1. Let s =
(
(a1,b 1),..., (ar,br)
)
be an ordered multisegment such that
bk−ak + 1 ≤ N for any 1≤ k≤ r. Let t be an integer such that 1≤ t≤ r and
bt−at + 1 = N. Let us set s′ =
(
(ak,bk)
)
k⁄=t, and let M(s) and M(s′) be the simple
gradedR-modules associated with s and s′, respectively.
Then M(s′)◦L(at,bt) is isomorphic to M(s) inA/S up to a grading shift.
62 S.-J. KANG, M. KASHIW ARA, M. KIM
Proof. In this proof, we omit the grading shift. Set
L =L(a1,b 1)◦···◦ L(at−1,bt−1),
L′ =L(at−1,bt−1)◦···◦ L(a1,b 1),
K =L(at+1,bt+1)◦···◦ L(ar,br),
K′ =L(ar,br)◦···◦ L(at+1,bt+1).
Then M(s′) is isomorphic to the image of L◦K
f ′
→K′◦L′ and M(s) is isomorphic to
the image of L◦L(at,bt)◦K
f
→K′◦L(at,bt)◦L′. The homomorphism f is decomposed
into
L◦L(at,bt)◦K
φ
− −−−−− →L◦K◦L(at,bt)
f ′◦L(at,bt)
− −−−−−−− →K′◦L′◦L(at,bt)
ψ
−−−−→ K′◦L(at,bt)◦L′.
Since L(at,bt)◦K→K◦L(at,bt) and L′◦L(at,bt)→L(at,bt)◦L′ are isomorphisms
inA/S by Proposition 4.2.3, φ and ψ are also isomorphisms in A/S. Hence M(s′)◦
L(at,bt) is isomorphic to M(s) inA/S. □
Corollary 4.7.2. If X be a simple object in A/S, then X◦La is a simple object in
A/S for any a∈ Z.
Proposition 4.7.3.
(i) The canonical functor Ω = Ξ ◦ Υ : A/S → TJ sends simple objects to simple
objects.
(ii) dim k HomTJ (X,Y )<∞ for any X,Y ∈T J .
(iii) Let us denote by Irr(TJ ) the set of the isomorphism classes of simple objects in
TJ . Deﬁne an equivalence relation ∼ onIrr(TJ ) byX∼Y if and only if X≃qcY
inTJ for some integer c. Let Irr(TJ )q=1 be a set of representatives of elements
inIrr(TJ )/∼.
Then the set Irr(TJ )q=1 is isomorphic to the set of ordered multisegments
s =
(
(a1,b 1),... (ar,br)
)
satisfying
(4.7.1) bk−ak + 1<N for any 1≤k≤r.
(iv) The functor ~F :TJ→C J induces a bijection betweenIrr(TJ )q=1 andIrr(CJ ), the
set of isomorphism classes of irreducible objects in CJ .
Proof. (i) follows from Corollary 4.7.2 and Proposition A.7.2.
(ii) follows from Lemma A.6.3.
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 63
(iii) By (i), every element in Irr(TJ )q=1 is of the form [Ω( M(s))], for some ordered
multisegment s =
(
(a1,b 1),... (ar,br)
)
. By Lemma 4.7.1, we can assume that s satisﬁes
(4.7.1). Hence the assignment s↦→[Ω(M(s))]∈I rr(TJ )q=1 is surjective.
For two multisegments s1 and s2 satisfying ( 4.7.1), if Ω( M(s1))≃ Ω(M(s2)) in TJ
up to grading shift, then F (M(s1))≃F (M(s2)) in U′
q(ˆslN )-mod implies s1 = s2 by
Theorem 2.2.1 (iii). Thus we obtain (iii).
(iv) By (iii), for any simple object X inTJ , we have X≃ (Ω·Q )(qcM(s)) for some
ordered multisegment s satisfying ( 4.7.1) and some integer c. Then ~F (X) =F (M(s))
is irreducible by Theorem 4.3.3.
It is known that every irreducible module in CJ can be obtained as the head of a
tensor product of the form
V (̟i1)(−q)c1⊗···⊗ V (̟ir)(−q)cr
for some {ck∈ Z}1≤k≤r such that ck≡ ik− 1 mod 2 and that ( −q)ck−cj is not the
zero of dV (̟j),V (̟k) for 1≤j < k≤r. Moreover, such a sequence
(
(i1,c 1),... (ir,cr)
)
is unique up to a permutation (Theorem 2.2.1 (iii)).
Set ak = ck−ik + 1
2 and bk = ck +ik− 1
2 . By applying a permutation, we may
assume that the multisegment
(
(a1,b 1),... (ar,br)
)
is ordered. Note that ( aj,bj)≥
(ak,bk) implies that (−q)ck−cj is not the zero of dV (̟j ),V (̟k). Then we have
F (L(a1,b 1)◦···◦ L(ar,br))≃V (̟i1)(−q)c1⊗···⊗ V (̟ir )(−q)cr
andF (M(s)) is isomorphic to the head of V (̟i1)(−q)c1⊗···⊗ V (̟ir )(−q)cr . Hence the
assignmentIrr(TJ )q=1∋X↦→[ ~F (X)]∈I rr(CJ ) is bijective. □
Finally, we have established one of the main theorems of this paper.
Theorem 4.7.4. The exact functor ~F :TJ→C J induces a ring isomorphism
φ ~F : K(TJ )/(q− 1)K(TJ )∼−→K(CJ ).
ThereforeTJ may be regarded as a Z-graded lifting of the rigid tensor category CJ .
Recall that the ring K(CJ ) admits interesting t-deformations ([ 36, 32, 10]). In [ 12],
Hernandez and Leclerc gave a presentation of Kt, one of those t-deformations. For
each simple object W ofCJ , there is a distinguished element χq,t(W ) in Kt, and the
χq,t(W )’s form a basis of Kt as a C(t1/2)-vector space. Set yi,0 :=χq,t(V (̟1)q2i) and
set yi,m+1 :=χq,t(∗W ), if yi,m =χq,t(W ) (m∈ Z). Then Kt coincides with the C(t1/2)-
algebra generated by {yi,m|i = 1,...,N − 1, m∈ Z} with the deﬁning relations
for every m∈ Z,(4.7.2)
64 S.-J. KANG, M. KASHIW ARA, M. KIM
{
yi,myj,m =yj,myi,m if j⁄=i + 1,i− 1,
y2
i,myj,m− (t +t−1)yi,myj,myi,m +y2
j,myi,m = 0 if j =i + 1 or i− 1,
for every m∈ Z, and every i,j∈{ 1, 2,...,N − 1},(4.7.3)
yi,myj,m+1 =t−2δi,j +δ(i=j+1)+δ(i=j−1)yj,m+1yi,m +δ(i =j)(1−t−2),
for every p>m + 1, and every i,j∈{ 1, 2,...,N − 1},(4.7.4)
yi,myj,p =t(−1)p−m(2δi,j−δ(i=j+1)−δ(i=j−1))yj,pyi,m.
Note that our generator yi,m is the element x
← −Q
i,m−1 given in [ 12, §7.1], associated with
the quiver← −Q : 1 ← 2←···← N− 1.
Set KC(q1/2)(TJ ) = C(q1/2)⊗Z[q±1]K(TJ ).
Theorem 4.7.5. There is a C-algebra isomorphism ψ :Kt→KC(q1/2)(TJ ) sending
t1/2↦→q−1/2, y i,2k↦→[L(i +kN )], y i,2k+1↦→[q−1L(i +kN + 1,i + (k + 1)N− 1)].
Proof. In the proof, we denote by Zi,2k andZi,2k+1 the objects L(i +kN ) and q−1L(i +
kN + 1,i + (k + 1)N− 1)), respectively. Note that Zi,m+1 is the right dual of Zi,m.
We denote by zi,m ∈ K(TJ ) the element [ Zi,m]. It is straightforward to check that
{zi,m|i = 1...,N − 1, m∈ Z} satisfy the relations ( 4.7.2)–(4.7.4). For example, we
have
zi,2k⋆zi,2k+1 =qB(εi−εi+1,εi+1−εi+N )zi,2k◦zi,2k+1 =q(zi,2k◦zi,2k+1)
=−q2Li+kN +q2zi,2k+1◦zi,2k +Li+kN
=(1−q2)1 +q2−B(εi+1−εi+N,εi−εi+1)zi,2k+1⋆zi,2k = (1−q2)1 +q2zi,2k+1⋆zi,2k,
which yields the relation ( 4.7.3) when i = j and m = 2k. Here, the third equality
follows from Proposition 4.2.3 (vi). The other relations can be checked similarly.
Note that we have
χq,t(V (̟i)(−q)p) = t−1/2
1−t−2
(
χq,t(V (̟i−1)(−q)p−1)χq,t(V (̟1)(−q)p+i−1)(4.7.5)
−t−1χq,t(V (̟1)(−q)p+i−1)χq,t(V (̟i−1)(−q)p−1)
)
,
for all ( i,p )∈{ 2,...,N − 1}× Z such that i≡ p + 1 mod 2. Indeed, if i = 2, then
it is nothing but a consequence of [ 12, Proposition 5.6]. The other cases can be also
shown by similar arguments. On the other hand, Proposition 4.2.3 (vi) implies that
[L(a,b )] = 1
1−q2
(
[L(a,b− 1)]⋆ [L(b)]−q[L(b)]⋆ [L(a,b− 1)]
)
,(4.7.6)
for every a,b∈ Z with 0 <b−a + 1<N . For such a pair a,b∈ Z, assume that there
exists k∈ Z such that 1 + kN ≤ a≤ b≤ N− 1 +kN . Then by comparing ( 4.7.5)
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 65
with ( 4.7.6) and arguing by induction on b−a + 1, we deduce that
ψ
(
χq,t(V (̟b−a+1)(−q)a+b
)
=q
b−a
2 [L(a,b )](4.7.7)
if 1 +kN≤a≤b≤N− 1 +kN for some k∈ Z. If there is no such a k, then we have
there exists s∈ Z such that a≤sN≤b.(4.7.8)
Recall that there is a C-algebra anti-automorphism d′ onKt deﬁned by d′(t1/2) = t−1/2,
d′
(
χq,t(V (̟i)(−q)p)
)
= χq,t(V (̟N−i)(−q)p+N ) ([ 12, §5.7, §7.1]). On the other hand,
from the duality, we obtain a ring anti-automorphism d onK(TJ ) given by d(q) = q−1,
d([X]) = [ ∗X] (X∈T J ). Then we have d◦ψ = ψ◦d′, by the deﬁnition of ψ. For
a,b∈ Z with 0 <b−a + 1<N and ( 4.7.8), we have
ψ
(
χq,t
(
V (̟b−a+1)(−q)a+b
) )
=ψ
(
d′(
χq,t
(
V (̟N−b+a−1)(−q)a+b−N
)) )
= d
(
ψ
(
χq,t
(
V (̟N−b+a−1)(−q)a+b−N
)) )
=d
(
q
N−b+a−2
2 L(b + 1−N,a− 1)
)
= q
−N+b−a+2
2 q−1L(a,b ) = q
−N+b−a
2 L(a,b ),
where the third equality comes from ( 4.7.7). Hence we have
ψ(χq,t(V (̟b−a+1)(−q)a+b))≡ [L(a,b )]
for everya,b∈ Z with 0 <b−a+1 <N , wherex≡y meansx =qm/2y for somem∈ Z.
LetKC[t±1/2] denote the C[t±1/2]-subalgebra of Kt generated by the χq,t(W )’s, where
W ranges over the set of the isomorphism classes of simple objects of CJ . Because the
[L(a,b )]’s generate the Z[q±1]-algebra K(TJ ), the restriction ˜ψ of ψ toKC[t±1/2] gives
the surjective map
˜ψ :KC[t±1/2] ։ C[q±1/2] ⊗
Z[q±1]
K(TJ ).
Since ˜ψ gives an isomorphism
KC[t±1/2]/(t1/2− 1)KC[t±1/2]≃ C⊗ZK(CJ )∼−→C⊗Z
(
K(TJ )/(q− 1)K(TJ ))
)
after specializing at t1/2 = 1, the homomorphism ˜ψ, as well as ψ, is an isomorphism. □
