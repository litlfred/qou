---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-008-52-locality-axiom-and-the-equivalence-of-topolog
section_title: "Locality axiom and the equivalence of topological chiral homology with higher Hochschild functor for CDGAs"
section_number: 5.2
pages: 43-47
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
with higher Hochschild functor for CDGAs. In view of Proposition 11 and
Theorem 1, Morse theory (or any triangulation) suggests the follo wing result, which
is the main result of this section.
Theorem 5. Let M be a manifold of dimension m endowed with a framing of
M×Dk and A be a diﬀerential graded commutative algebra viewed as an Em+k-
algebra. Then, the topological chiral homology of M with coeﬃcients in A, denoted
by
∫
MA is equivalent to CH •
M (A) viewed as an Ek-algebra (in other words to
j∗
k(CH •
M (A))).
In particular, topological chiral homology
∫
MA with coeﬃcient in a CDGA A is
always equivalent to a CDGA and is deﬁned for any manifold M .
This theorem is similar to [25, Theorem 5.3.3.8] (with the diﬀerence that we
assume M to be smooth and keep track of the Ek-algebra structure). In this
section, we wish to prove it by using a straightforward geometrical approach based
on the gluing property. Indeed, the key idea to prove Theorem 5 is t o use handle
decomposition which is very appropriate to deal with manifolds and th e deﬁnition
of topological chiral homology. However, note that, with respect to Hochschild
chains, a representation of M as a CW complex is already nice enough.
Before proving Theorem 5, we recall a few facts on the handle deco mpositions.
Let M be a smooth manifold of dimension m. A handle decomposition of M is
a sequence ∅⊂ M0⊂···⊂ Mm = M , where each Mj is obtained by attaching
j-handles to Mj−1, see [28]. That is gluing a copy of Hj =Dj×Dm−j using the
attaching map Sj−1×Dm−j→∂Mj−1 which is assumed to be an embedding. In
particular all handles of same dimension are attached using diﬀeomor phisms.
We can achieve such a handle decomposition for M using Morse theory as follows.
Let f :M→ R be a Morse function with critical points p1,··· ,pk numbered in a
way thatf (p1)<··· <f (pk). Choose a0,··· ,ak such thata0 <f (p1)<a 1<··· <
ak−1<f (pk)<a k. Now it is suﬃcient to note that f −1([ai−1,ai]) is diﬀeomorphic
to attaching a j-handle to f (ai−1)× [0, 1], where j is the index of the critical point
pi, i.e. the number of the negative eigenvalues of the Hessian of f at that critical
point. For example a torus with the height function is ﬁrst given by at taching a
D0×D2 to the empty set, then attaching a D1×D1 (think of it as a thin ribbon) to
the boundary of the previous D2. Then attaching another ribbon to the boundary
44 G. GINOT, T. TRADLER, AND M. ZEINALIAN
of the previous ribbon, and the ﬁnally attaching a D2×D0 to what has been
obtained along the boundary.
Lemma 7. Let M be an n-framed manifold and N be an n-framed manifold ob-
tained from M by attaching a countable sequence of handles (Hi)i∈N. For any
n∈ N, we write Xk for the result of attaching the ﬁrst k-handles to M . For any
En-algebraA, there is a natural equivalence
lim−→
k∈N
∫
Xk
A
≃
−→
∫
N
A.
Proof. We may assume dim(M ) = n. The maps Xk→Xk+1 yield a diagram
(19) N (Disj(M ))→N (Disj(X1))→···→ N (Disj(Xk))→···→ N (Disj(N ))
of faithfull maps, hence canonical maps lim−→
k∈N
N (Disj(Xk))→N (Disj(N )) and
(20) lim −→
k∈N
∫
Xk
A∼= lim−→
k∈N
(
lim−→ψXk
)
→ lim−→ψN∼=
∫
N
A
(using the notation introduced in Deﬁnition 4). Note that lim −→
k∈N
(
lim−→ψXk
)
can be
identiﬁed with the colimit lim−→
˜ψN given informally by the diagram
˜ψN (Vk
1 ∪···∪ Vk
j ) =
∫
V k
1
A⊗···⊗
∫
V k
j
A
where the Vk
i are disjoint open subsets of Xk homeorphic to a ball (here k is not
ﬁxed).
Since A is a ﬁxed En-algebra, it is in particular an E(X)-algebra (in the sense
of [25, Section 5.2.4]) for any n-framed manifold X. In particular, by [25, Theorem
5.2.4.9] (also see Proposition [25, Proposition 5.3.2.13]), if U ⊂ V are two open
subsets ofX which are homeomorphic to a ball, then the induced map ∫
UA→ ∫
V A
is an equivalence.
Now, let V be an open subset of N which is homeomorphic to a ball. Since
N = lim−→
k∈N
Xk, there exists a k such that V∩Xk is a non-empty open subset of Xk,
and thus contains an open ball Vk in Xk which is lying in V too. In particular
the natural map
∫
V kA→
∫
V A is an equivalence. It follows that, given a ﬁnite
set V1,...,V n of open homeomorphic to a ball in N , we can ﬁnd an integer k big
enough and open sets Vk
1 ⊂V1, ...., Vk
n ⊂Vn in Xk which are homeomorphic to a
ball, yielding a natural equivalence
˜ψN (Vk
1,...,V k
n ) =
∫
V k
1
A⊗···⊗
∫
V kn
A∼=
∫
V1
A⊗···⊗
∫
Vn
A =ψN (V1,...,V n).
This proves the coﬁnality of the functor N ( ~Disj(N ))֒→N (Disj(N )) induced by
the natural inclusion. Here we have denoted ~Disj(N ) the partially ordered set
of open subsets of N which are homeomorphic to F×Rn for a ﬁnite set F and
included in some Xk (where k is not ﬁxed). Passing to colimits, we get that the
map lim−→
k∈N
(
lim−→ψXk
) ∼= lim−→
˜ψN→ lim−→ψN is an equivalence and thus the canonical
map (20) is an equivalence as well. □
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 45
Proof of Theorem 5. Let us sketch the key idea of the proof ﬁrst: by the value
on a point axiom, both topological chiral homology and higher Hochsc hild chains
agree on a point and further on any disk Dk (up to neglect of structure). Using
handle decompositions, one can chop manifolds on disks which are glue d along
their boundaries. Since both topological chiral homology and higher Hochschild
chains satisfy a similar gluing axiom (and also behave the same way unde r disjoint
unions), one then can lift the natural equivalence for disks to any m anifold using
handle decompositions. We now make the above scheme precise.
Assume M is compact. Let us choose a generic Morse function on M and
the associated handle decomposition ∅ ⊂M0 ⊂ ··· ⊂Mm = M of M . Then
∅⊂ M0×Dk⊂···⊂ Mm×Dk =M×Dk is a handle decomposition of M×Dk.
That is (M×Dk)j =Mj×Dk where we replace each j-handle Hj =Dj×Dm−j
attached to Mj−1 by the j-handleDj×Dm+k−j∼=Dj×
(
Dm−j×Dk)
attached to
Mj−1×Dk = (M×Dk)j−1. The (m +k)-framing of M induces an (m +k)-framing
of each Mj×Dk = (M×Dk)j.
By homotopy invariance of Hochschild chains, one has an equivalence of CDGAs
CHM×Dd (A)∼=CHM (A) (for any integerd). Further, from diagram (18) we deduce
that, for any CDGA B, one has j∗
k (B)∼=ι∗
d(j∗
k+d(B)) where ιd :Ek֒→Ek+d is the
natural map. Since, for any Em+k-algebra B, one has
∫
DmB∼= B viewed as an
Ek-algebra, the result of Theorem 5 holds for all disks.
We now prove by induction that it holds for all (( m +d)-framed) spheres Sm and
Em+d-algebra A. For S0 = pt ∐ pt, it follows from Theorem 1 and [25, Theorem
5.3.3.1] that
∫
S0A∼=A⊗A∼=CHS0 (A) (as Ed-algebras). Now, assume the result
for Sm−1 and m≥ 1. We have a decomposition of the m-sphere Sm as Sm ∼=
Dm∪Sm−1Dm as in the assumption of Proposition 11. Since this decomposition is
also an homotopy pushout, it follows from the induction hypothesis, Proposition 11
and Theorem 1.(3) that there are natural equivalences∫
Sm
A ∼= A
L
⊗∫
Sn−1A
A ∼= CH •
Dm(A)
L
⊗
CH •
Sm−1 (A)
CH •
Dm (A) ∼= CH •
Sm (A)
of Ed-algebras which ﬁnishes the induction step.
Clearly, M0 is a disjoint union M0 = ∐
I0Dm of ﬁnitely many m-dimensional
balls (here I0 is the set indexing the various disks in M0). Using again that, for any
Em+k-algebra B, one has
∫
DmB∼= B viewed as an Ek-algebra, we get a natural
equivalence of Ek-algebras
∫
M0
A ∼= ⨂
I0j∗
k(A) ∼= j∗
k(⨂
I0A) since
∫
M ∐ NA ∼=∫
MA⊗
∫
NA by [25, Theorem 5.3.3.1], the set I0 is ﬁnite and jk is monoidal (that is
commutes with the diagonals of the Ek-operads). Further CH •
Dm (A)∼=CH •
pt(A)∼=
A and, by Theorem 1.(1) and (2), there is a natural equivalence CH •
M0 (A)∼=
⨂
I0A
of CDGAs. Hence the theorem is proved for M0.
By assumption M1 is obtained by attaching ﬁnitely many 1-handles H 1
1,...,H 1
i1
(the sequence may be empty) to M0. Choosing appropriate tubular neighborhoods
for the image of ∂D 1×Dm−1 in M0 and gluing it with
(
∂D 1×Dm−1)
× [0,ε ]∼=(
∂D 1× [0,ε ]×Dm−1)
⊂H 1
1 , we can assume that the result M0∪∂D 1×Dm−1H 1
1 of
attachingH 1
1 to M0 satisﬁes the assumption of Proposition 11. Then, by Proposi-
tion 11 we have a natural equivalence of Ek-algebras:
(21)
∫
M0
A
L
⊗∫
∂D1 ×Dm−1A
∫
H1
1
A∼=
∫
M0∪∂D1 ×Dm−1H1
1
A.
46 G. GINOT, T. TRADLER, AND M. ZEINALIAN
By Theorem 1.(3), we also have a natural equivalence of CDGAs (and thus of the
underlying Ek-algebras)
(22) CH •
M0 (A)
L
⊗
CH •
∂D1 ×Dm−1 (A)
CH •
H1
1
(A)∼=CH •
M0∪∂D1×Dm−1H1
1
(A).
We have already seen that we have natural equivalences CH •
M0 (A)∼=
∫
M0
(A) of
Ek-algebras and similarly for ∂D 1×Dm−1 and D1×Dm−1 in place of M0 (since
those manifolds are disks). Combining these equivalences with those given by the
identities (21) and (22), we get a natural equivalence
∫
M0∪∂D1×Dm−1H1
1
A∼=CH •
M0∪∂D1 ×Dm−1H1
1
(A).
Attaching more 1-handles, we inductively get a natural equivalence
∫
M1
A∼=CH •
M1 (A)
of Ek-algebras.
We proceed the same for attaching j ≥ 2-handles (by induction on j). The
proof is identical to the 1-handles case once we notice that there a re also a natural
equivalence
∫
∂D j ×Dm−jA∼= CH •
∂D j ×Dm−j (A). The later follows from the natural
equivalences relating topological chiral homology and higher Hochsc hild chains of
spheres (with value in A) proved above. Indeed, ∂Dj×Dm−j∼=Sj−1×Dm−j and
there is a natural equivalence
∫
Sj−1×Dm−jA∼=i∗
m−j
( ∫
Sj−1A
)
whereim−j :Ek+1֒→
Em+k−j+1 is the canonical map (neglecting part of the structure). Similarly, t here
are natural equivalences CH •
Sj−1 (A)∼= CH •
Sj−1×Dm−j (A) of CDGAs. It follows,
since j∗
k+m−j+1
(
CH •
Sj−1 (A)
) ∼=
∫
Sj−1A, that we get a natural equivalence
j∗
k+1(CH •
Sj−1×Dm−j
(
(A)
) ∼=i∗
m−jj∗
k+m−j+1
(
CH •
Sj−1×Dm−j (A)
) ∼=
∫
Sj−1×Dm−j
A
which ﬁnishes the proof in the compact case.
If M is non-compact, we still have a handle decomposition, but we may hav e
to attach countable many handles to go from Mi to Mi+1. In particular, we can
ﬁnd an increasing sequence of relatively compact open subsets Mi = X0⊂ X1⊂
··· Xn⊂···⊂ ⋃
n≥0Xn = Mi+1 (for instance by choosing Xn to be the result of
attaching the ﬁrst n i-handles to Mi). We wish to prove the result by induction
on i. Note ﬁrst that, by deﬁnition of the Hochschild chain functor and L emma 6,
there is an equivalence (for the underlying Ek-algebras structures)
CH •
M0 (A)∼= lim−→
F0 ⊂ I0
F0 ﬁnite

 ⨂
f ∈F0
CH •
Dm (A)

∼= lim−→
F0 ⊂ I0
F0 ﬁnite

 ⨂
f ∈F0
∫
Dm
(A)

∼=
∫
M0
A
which proves the result for M0. Now, assume we have an natural equivalence
CH •
Mi (A)∼=
∫
Mi
A. Writing Mi = X0⊂ X1⊂··· Xn⊂···⊂ ⋃
n≥0Xn = Mi+1,
by the above argument for the ﬁnite handles case, we have natura l equivalences
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 47
CH •
Xn (A)∼=
∫
Xn
A for all n and thus a commutative diagram
(23) lim −→
n∈N
CH •
Xn (A) ≃ /d47/d47
/d15/d15
lim−→
n∈N
∫
Xn
A
/d15/d15
CH •
Mi+1 (A) /d47/d47 ∫
Mi+1
A
.
By Lemmas 7 and Lemma 1, the vertical arrows are equivalences,hen ce the lower
map is too, which ﬁnishes the induction. □
Remark 14. A geometric intuition behind Theorem 5 can be seen as follows. Let
M be a dimension m manifold. Since a CDGA A is an En-algebra for any n, the
topological chiral homology
∫
MA is deﬁned for any n-framing of M , and is an
En−m-algebra. Further, if M isn-framed (hence we have chosen a trivialization of
M×Dn−m), then M is also naturally (n +k)-framed for any integer k. Since A is a
CDGA, it is an En+k-algebra as well and thus we could have used the trivialization
ofM×Dn−m×Dk∼=M×Dn+k−m as well to deﬁne
∫
MA as an En−m+k-algebra.
It is well known that the transversality theorem implies that two emb eddings
φ1 :M→Sn andφ2 :M→Sn ofM are isotopic if n is large enough. In particular,
for large n the framing that comes from the embedding into Sn is unique. This
unique invariant of M is called the stable normal bundle. Note that this implies
that any two abstract framings of M×Dk andM×Dl are stably equivalent since,
for example, for M×Dk we can make M sit inside Rn and then the normal bundle
of M in Rn is the complement of the framing of the tangent bundle of M×Dk in
Rn×Dk.
Building upon the last remark, we see that the topological chiral hom ology of
an (m +k)-framed manifold M with value in a CDGA should be equivalent (up
to neglect of structure) to the topological chiral homology of M equipped with the
stable normal framing so that we get
Corollary 12. Topological chiral homology with values in CDGAs is indepen dent
of the framing. In other words, if M1 andM2 are diﬀeomorphic manifolds equipped
respectively with an (n +k1)-framing and (n +k2)-framing, then there is a canonical
equivalence ∫
M1
A∼=
∫
M2
A of Emin(k1,k2)-algebras.
In particular,
∫
MA is naturally deﬁned for every manifold M whenA is a CDGA.
Proof. By Theorem 5, there are natural equivalences
∫
M1
A∼= CH •
M1 (A) of Ek1 -
algebras and
∫
M2
A∼=CH •
M2 (A) of Ek2 -algebras. Since M1 and M2 are diﬀeomor-
phic, we have an equivalence CH •
M1 (A)∼=CH •
M2 (A) as CDGAs. □
