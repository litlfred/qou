---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-015-61-background-on-association-schemes
section_title: "Background on association schemes"
section_number: 6.1
pages: 42-44
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
liminaries about association schemes, using notation from [MaSl]. Another
useful reference is [BaI], and what we call association sche mes some authors
call symmetric association schemes.
Deﬁnition . An association scheme with n classes consists of a ﬁnite set
X with n + 1 relations R0, · · ·,R n deﬁned on X which satisfy:
(1) Each Ri is symmetric: ( x,y ) ∈Ri ⇒ (y,x ) ∈Ri.
(2) For every x,y ∈X, one has that ( x,y ) ∈Ri for exactly one i.
(3) R0 = {(x,x ) : x ∈X} is the identity relation.
(4) If ( x,y ) ∈ Rk, the number of z ∈ X such that ( x,z ) ∈ Ri and
(y,z ) ∈ Rj is a constant cijk depending on i,j,k but not on the
particular choice of x and y.
The adjacency matrix Di corresponding to the relation Ri is the |X| × |X|
matrix with rows and columns labeled by the points of X deﬁned by
(Di)x,y =
{
1 if ( x,y ) ∈Ri
0 otherwise.
The Bose-Melner algebra is deﬁned to be the vector space cons isting of
all matrices ∑ n
i=0aiDi with ai real. Since the matrices in the Bose-Melner
algebra are symmetric and commute with each other (by parts 1 and 4 of the
deﬁnition of an association scheme), the Bose-Melner algeb ra is semisimple
and has a distinguished basis of primitive idempotents J0, · · ·,J n satisfying
(1) J 2
i =Ji i = 0, · · ·,n .
(2) JiJk = 0 i ⁄=k.
(3) ∑ n
i=0Ji =I.
43
Here I is the identity matrix.
The D’s are also a basis of the Bose-Melner algebra, so one can writ e
Ds =
n∑
i=0
φs(i)Ji, s = 0, · · ·,n
where the φs(i) are real numbers. Since DsJi = φs(i)Ji, the φs(i) are the
eigenvalues of Ds. For later use note that since D0 and∑ n
i=0Ji are both
the identity matrix, φ0(j) = 1 for all j.
Letµi be the rank of Ji. For all s, this is the multiplicity of the eigenvalue
φs(i) of Ds. We deﬁne the Plancherel measure of the association scheme t o
be the probability measure on {0, · · ·,n } which chooses i with probability
µ i
|X| .
Lemmas 6.1 and 6.2 are the orthogonality relations for eigen values of
association schemes. To state them it is helpful to deﬁne vi =cii0, so that
for any x, one has that vi is the number of pairs ( x,y ) ∈ Ri. Clearly∑ n
i=0vi = |X|.
Lemma 6.1. ([MaSl], page 655) For 0 ≤k,l ≤n,
n∑
r=0
φr(k)φr(l)
vr
= |X|
µk
δk,l.
Lemma 6.2. ([MaSl], page 655) For 0 ≤k,l ≤n,
n∑
i=0
µiφk(i)φl(i) = |X|vkδk,l.
Lemma 6.3 will be crucial.
Lemma 6.3. The coeﬃcient of Dl in Ds1 · · ·Dsm is equal to
1
vl
n∑
i=0
µi
|X|φs1(i) · · ·φsm(i)φl(i).
In particular, the coeﬃcient of Dl in (Ds)m is
1
vl
E[φs(i)mφl(i)],
wheres is random from Plancherel measure of the association scheme .
Proof. Since Ds =∑ n
i=0φs(i)Ji, one knows that
Ds1 · · ·Dsm =
n∑
i=0
φs1(i) · · ·φsm(i)Ji.
By pages 654 and 655 of [MaSl],
Ji = 1
|X|
n∑
l=0
µiφl(i)
vl
Dl.
The result follows. □
44
Let pm(r) denote vr
(vs)m multiplied by the coeﬃcient of Dr in (Ds)m. It
follows from the deﬁnitions that pm(r) admits the following probabilistic
interpretation. Start from some point x0 ∈ X, move to a random x1 ∈ X
such that ( x0,x 1) ∈ Rs, then to a random x2 ∈ X such that ( x1,x 2) ∈
Rs, and so on until one obtains xm. Then pm(r) is the probability that
(x0,x m) ∈Rr.
The following fact will be useful.
Lemma 6.4. (1) p4(0) =∑ n
r=0
p2(r)2
vr .
(2) p3(s) = vs
∑ n
r=0
p2(r)2
vr
.
Proof. The ﬁrst assertion is clear from the probabilistic interpre tation of
pm(r). For an analytic proof, note that by Lemma 6.3 (in the ﬁrst an d
fourth equalities) and Lemma 6.1 (in the second and third equ alities)
n∑
r=0
p2(r)2
vr
=
n∑
r=0
1
vr
(
1
(vs)2
n∑
i=0
µi
|X|φs(i)2φr(i)
) 2
= 1
(vs)4
n∑
r=0
1
vr
n∑
i=0
(µi)2
|X|2φs(i)4φr(i)2
= 1
(vs)4
n∑
i=0
µi
|X|φs(i)4
= p4(0).
The second assertion follows from the ﬁrst assertion since p3(s) = vsp4(0),
as can be seen either by the probabilistic interpretation of pm(r) or by
computing both sides of the equation using Lemma 6.3. □
