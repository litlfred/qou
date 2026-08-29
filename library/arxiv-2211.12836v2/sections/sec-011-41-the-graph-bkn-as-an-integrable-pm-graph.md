---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-011-41-the-graph-bkn-as-an-integrable-pm-graph
section_title: "The graph Bk,n as an integrable PM-graph"
section_number: 4.1
pages: 22-25
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
I∈Bk,n CeI denotes the Hilbert space of functions on Bk,n with the scalar product⟨eI,eJ⟩ =δI,J ,
whereB0 = (eI)I∈Bk,n is the canonical basis on L2(Bk,n). Then, the graph structure on Bk,n is
encoded in the adjacency matrix A∈B (L2(Bk,n)) given by
AeI =
∑
I↗J
eJ.
In the sequel, we will use a specialization of the quantum cohomology of the Grassmannian
QH(Gk,n) to prove that Bk,n is an integrable PM-graph as deﬁned in Deﬁnition 3.1. The reader
should refer to Appendix A for any background on QH(Gk,n). We mainly need the fact that
QH(Gk,n) = Sym[x1,...,x k]⊗ C[q]/Sym[x1,...,x k]/⟨(x1,...,x k) = q1/k(
eit1,...e itk
)
,⃗t∈ Tk,n⟩,
see Appendix A, and we will consider the specialization
QH1(Gk,n) :=QH(Gk,n)/⟨q = 1⟩ =Sym[x1,...,x k]/⟨(x1,...,x k) =
(
eit1,...e itk
)
,⃗t∈Tk,n⟩.
The algebra QH1(Gk,n) is spanned by the basis{sλ,λ∈ Λk,n}, and we denote by 𝓁 :QH1(Gk,n)→
L2(Bk,n) the isomorphism deﬁned by
𝓁(sλ) =eIλ.
Then,Bk,n is a PM-graph in the sense of Deﬁnition 3.1 with an enveloping algebraA≃ QH1(Gk,n),
as the next proposition shows.
Proposition 4.2. There is a commutative algebra A ⊂ B(L2(Bk,n)) containing C[A] which is
isomorphic to QH1(Gk,n) through an isomorphism T : QH1(Gk,n)→A such that T (sλ)eI0 = eIλ
and T (s(1)) =A.
As a consequence Bk,n is a PM-graph rooted at I0.
Proof. Remark ﬁrst that since dim L2(Bk,n) =|Bk,n| =
(n
k
)
, for any commutative subalgebra A of
B(L2(Bk,n)) we have dimA≤
(n
k
)
. Recall that we deﬁned
QH1(Gk,n) =Sym[x1,...,x k]/⟨(x1,...,x k) =
(
eit1,...e itk
)
,⃗t∈Tk,n⟩.
SinceTk,n has cardinal
(n
k
)
and the map (t1,...,t k)↦→
(
eit1,...e itk
)
is injective onTk,n,QH1(Gk,n)
is isomorphic to the space of functions on
(n
k
)
elements and thus dim QH1(Gk,n) =
(n
k
)
. Since
QH1(Gk,n) is spanned by {sλ}λ∈Λk,n, by a dimension argument the latter set is actually a basis
of QH1(Gk,n). Recall that 𝓁 : QH1(Gk,n)→ L2(Bk,n) is the isomorphism sending sλ to eIλ, and
deﬁne T :QH1(Gk,n)→B (L2(Bk,n)) by
T (x)eI =𝓁(x𝓁−1(eI)), x∈QH1(Gk,n), I∈Bk,n.
Then,T is an injective morphism of algebra, since it can be written as the composition of the mul-
tiplication map m :QH1(Gk,n)→B (QH1(Gk,n)) with the conjugation map C𝓁 :B(QH1(Gk,n))→
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 23
B(L2(Bk,n)) given by M↦→ 𝓁◦M◦𝓁−1, both maps being injective morphisms of algebras. Since
QH1(Gk,n) is commutative, T (QH1(Gk,n)) is a commutative subalgebra of B(L2(Bk,n)).
Since 𝓁−1(eI) =sλI, we have
T (s(1))eI =𝓁(s(1)sλI).
The multiplication by s(1) in QH(Gk,n) is given by the quantum Pieri rule [6, Eq. (22)], which
gives for λ∈ Λk,n after specializing q = 1
s(1)sλ =
∑
λ↗µ
sµ +δλ1=n−k,λk>0qs˜λ =
∑
λ↗µ
sµ +δλ1=n−k,λk>0s˜λ,
where ˜λ = (λ2− 1,...,λ k− 1, 0). Hence, by Lemma 4.1, s(1)sλ = ∑
Iλ↗IsλI, which yields for
I∈Bk,n
T (s(1))eI =𝓁(s(1)sλI) =
∑
I↗J
𝓁(sλJ ) =
∑
I↗J
eJ,
and ﬁnally T (s(1)) =A, so that C[A]⊂T (QH1(Gk,n)).
For allI∈Bk,n,
T (sλI)eI0 =𝓁(sλIs∅) =𝓁(sλI) =eI,
which implies that the map T (QH1(Gk,n))→ L2(Bk,n) given by x↦→ x(eI0) is injective. Then,
since
[AT (sλI)]eI0 =AeI =
∑
I↗J
eJ =

∑
I↗J
T (sλJ )

eI0,
we deduce that
AT (sλI) =
∑
I↗J
T (sλJ ) =
∑
J∈Bk,n
AJIT (sλJ ).
Finally, by (62), for all λ,µ∈ Λk,n we have
T (sλ)T (sµ) =T (sλsµ) =
∑
d≥0,ν∈Λk,n
⟨λ,µ,ν c⟩dT (sν)
with each term⟨λ,µ,ν c⟩d≥ 0.
By the previous results, Bk,n is a PM-graph whose enveloping algebra isA =T (QH1(Gk,n)) and
the corresponding basis is {T (sλI),I ∈Bk,n}. □
As a consequence of the latter result and the presentation of QH1(Gk,n), we will prove thatBk,n
is an integrable PM-graph. Let us simply write AI =T (sλI). In the case of Bk,n, there is a natural
indexation of left and right common eigenvectors of {AI}I∈Bk,n by the set Bk,n itself. We do not
known if such natural indexation holds for any integrable PM-graph. As we will see in the next
proposition, we are in the particular case where the adjacency matrix A is normal, so that left and
right eigenvectorsu(I) andw(I),I∈Bk,n of all operators AI coincide up to a constant, see (9). For
I∈Bk,n, set
(10) w(I) =
∑
J∈Bk,n
SJ(ξn(I))eJ,
where SJ(⃗ u) = sλJ
(
eiu1,...,e iuk
)
for ⃗ u∈ Rk, and let V (u1,...,u k) = ∏
j<j′
(
eiuj′−eiuj
)
be the
Vandermonde determinant of
(
eiuj
)
1≤j≤k.
Lemma 4.3. The set{w(I)}I∈Bk,n is an orthogonal basis of L2(Bk,n), and for all J∈Bk,n,
AJ(w(I)) =SJ(ξn(I))w(I) and A∗
J(w(I)) =SJ(ξn(I))w(I).
24 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Proof. The orthogonality relation is given by the following Cauchy type formula from [47, Propo-
sition 4.3]: for I,I′∈Bk,n,
(11)
∑
J∈Bk,n
SJ(ξn(I))SJ(ξn(I′)) =δI,I′
nk
|V (ξn(J))|2,
which directly yields
⟨w(I),w (I′)⟩ =δI,I′
nk
|V (ξn(J))|2(12)
for I,I′∈Bk,n.
To prove the eigenvector property, it is easier to work on QH1(Bk,n). Indeed, by Proposition
4.2, it suﬃces to prove that sλJ·𝓁−1(w(I)) = SJ(ξn(I))𝓁−1(w(I)), where· denotes the product in
QH1(Gk,n). From the proof of Proposition 4.2, QH1(Bk,n) is the space of functions on Zk,n =
{exp(i⃗ u),⃗ u∈ Tk,n}, where exp(i⃗ u) =
(
eiu1,...,e iuk
)
for ⃗ u∈ Rk. Hence, we need to show that
the values of sλJ·𝓁−1(w(I)) and SJ(ξn(I))𝓁−1(w(I)) agree on Zk,n. First, we have by the usual
evaluation of multiplication of functions
[
sλJ·𝓁−1
(
w(I)
)]
(exp(iξn(I))) =sλJ (exp(iξn(I)))
[
𝓁−1
(
w(I)
)]
(exp(iξn(I)))
=
[
SJ(ξn(I))𝓁−1(w(I))
]
(exp(iξn(I))).
Then, for I′⁄=I,
[
sλJ·𝓁−1(w(I))
]
(exp(iξn(I′)))−
[
SJ(ξn(I))𝓁−1(w(I))
]
(exp(iξn(I′)))
=
(
SJ(ξn(I′))−SJ(ξn(I))
)

 ∑
J′∈Bk,n
SJ′(ξn(I))sλJ′

 (exp(iξn(I′)))
=
(
SJ(ξn(I′))−SJ(ξn(I))
) ∑
J′∈Bk,n
SJ′(ξn(I))SJ′(ξn(I′)) = 0
by (12). Hence, we deduce that sλJ·𝓁−1(w(I)) =SJ(ξn(I))𝓁−1(w(I)), and the result is deduced by
applying𝓁. Since AJ is diagonalized on an orthogonal basis, it is actually normal and we thus have
A∗
J
(
w(I)
)
=SJ(ξn(I))w(I).
□
Note that as a corollary of (12), we have
‖w(I)‖2 = nk/2
|V (ξn(I))|.
Hence, following the notation of Section 3, we set
(13) u(I) =|V (ξn(I))|2
nk w(I),
so that⟨w(I),u (J)⟩ =δIJ .
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 25
