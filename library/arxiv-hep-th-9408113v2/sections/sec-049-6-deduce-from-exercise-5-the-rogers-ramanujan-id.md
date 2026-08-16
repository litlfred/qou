---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Steklov Mathematical Institute"
section_id: sec-049-6-deduce-from-exercise-5-the-rogers-ramanujan-id
section_title: "Deduce from Exercise 5 the Rogers-Ramanujan identities ( a = 0 or 1)"
section_number: 6
pages: 43-44
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "DILOGARITHM IDENTITIES ANATOL N. KIRILLOV — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
∑
j≥0
qj2+aj
(q)j
=
∏
j≥0
1
(1−q5j+1+a)(1−q5j+4−a). (2)
• Prove, RHS(2)= lim
N→∞
∑
σi∈{ 0, 1}, σiσi+1 = 0
σ1 =a, σN+1 = 0
q
∑ N −1
j=1 jσj+1
= 1
(q)∞
∑
k∈Z
(
qk(10k+1+2a)−q(2k+1)(5k+2−a)
)
. (3)
7. (Fusion rules and Rogers-Ramanujan’s type identities).
A. Let r≥ 3 be an odd integer and l := r− 3
2 . Let us introduce
i) matrix M :=M (x)∈ Matl+1×l+1(Z[x]), where (1 ≤i,k≤l + 1)
Mik :=
{
0, if i +k <l + 2;
xl−k+1, if i +k≥l + 2;
ii) the highest weight vector |j >=el−j+1 +... +el+1, where 0 ≤j≤l andei is the basis
vector in ( Rl)∗, namely, et
i = (δik), 1≤k≤l + 1;
iii) vector aj,N :=aj,N (x;q) = (a(1)
j,N,...,a (l+1)
j,N ) by the following rule
M (qN−1x)M (qN−2x)··· M (qx)M (x)|j >=at
j,N.
• Prove, a(p)
j,N (x,q ) =
∑
m=(m1,...,ml)∈Zl
+
xN1+...+NlqN 2
1 +N 2
2 +...+N 2
l −N1−...−Nj
l∏
k=1
[
Pk(m;j,p ) +mk
mk
]
q
,
where Ni :=mi +mi+1 +... +ml, 1≤p≤l + 1, and
Pk(m;j,p ) := kN + min(k,l−j)− max(k + 1−p, 0)− 2
l∑
i=1
min(i,k )mi.
It is well-known (see e.g. [FrSz1]) that
lim
N→∞
a(p)
j,N (q,q ) = χ(2,r)
1,1+j(q).
Using the Feigin–Fuchs–Rocha-Caridi character formula fo rχ(2,r)
1,1+j(q) (see e.g. [FF] or for-
mula (5)), and the exact expression for a(p)
j,N (x,q ), we obtain the group-theoretic proof/ex-
planation of the Gordon-Andrews identity. Even more, one ca n consider the polynomial
(x;q)N·a(l+1)
j,N (x,q ) as a ”natural ﬁnitization” of the Watson-Andrews identity (9). How-
ever, the exact computation of polynomials ( x;q)N·a(l+1)
j,N (x,q ) seems to be very diﬃcult
(even for x = 1). In this direction one can obtain the following partial r esult.
44 Anatol N. Kirillov
Theorem 8 (A.N. Kirillov). We have (x;q)Na(l+1)
j,N (x,q )≡
∑
m≥0
(−1)mx(l+1)mq
1
