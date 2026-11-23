---
doc_id: arxiv-math-0408078v2
doc_title: "A basis for the full Homfly skein of the annulus"
section_id: sec-012-eigenvectors-of-the-meridian-maps
section_title: "Eigenvectors of the meridian maps"
section_number: null
pages: 16-19
source_pdf: 0408078v2.pdf
source_sha256: b632eb5e9b7a1753
toc_source: outline
doc_brief: "A basis for the full Homfly skein of the annulus — A basis, denoted {Qλ,µ}, for the full Homﬂy skein of the annulus C was introduced in [18], where λ and µ are partitions of integers n and p into k"
---
Eigenvectors of the meridian maps
We now come to the main result, giving potential eigenvectors Aw in C for
the meridian maps. We show later that suﬃciently many of these vectors
are non-zero, to provide our claimed basis Qλ,µ by suitable choices of index
vector w.
Theorem 3.1 Let w be any index vector. Then
Aw = det
 h∗
⊣
h
⊣

w
∈C
satisﬁes ¯ϕ(Aw) = cwAw, and hence also ϕ(Aw) = cwAw, for some cw ∈Λ.
16
Proof:
Write Mw =
 h∗
⊣
h
⊣

w
, with entries mi j and cofactors Mi j ∈C.
Write ci j for the entries in the distinguished jth column of
 
j
↓
l(h∗)
⊣
s2jr(h∗)
l(h∗)
⊣
l(h)
⊣
s2j−2r(h)
l(h)
⊣
!
w
.
The determinant of this matrix, expanded by the jth column is
k∗+k
X
i=1
ci jl(Mi j).
Consequently lemma 2.6 gives
s−2k∗
 k∗+k−1
X
j=1
s2j
!
det l(Mw) + det r(Mw) = s−2k∗
k∗+k
X
i,j=1
ci jl(Mi j).
(19)
Now apply the closure map ⋄to the elements of A on each side of equation
(19). Recall that
⋄(l(X))
=
δX,
⋄(r(X))
=
¯ϕ(X),
⋄(Y l(X))
=
⋄(Y )X, for any X ∈C, Y ∈A,
and that r and l are algebra homomorphisms, so that det l(Mw) = l(Aw)
and det r(Mw) = r(Aw). We then have
s−2k∗
 k∗+k−1
X
j=1
s2j
!
δAw + ¯ϕAw = s−2k∗
k∗+k
X
i,j=1
⋄(ci j)Mi j.
(20)
We now show that ⋄(ci j) is a multiple of mi j, and that the righthand
side of equation (20) can be written as a multiple of Aw, thus proving the
theorem.
We deduce this from the following lemma.
Lemma 3.2 There exist αi, βj ∈A, 1 ≤i, j ≤k∗+ k, such that
⋄(ci j) = (αi + βj)mi j.
17
Corollary 3.3
k∗+k
X
i,j=1
⋄(ci j)Mi j
=
k∗+k
X
i,j=1
(αi + βj)mi jMi j
=
k∗+k
X
i,j=1
αimi jMi j +
k∗+k
X
i,j=1
βjmi jMi j
=
k∗+k
X
i=1
αi
 k∗+k
X
j=1
mi jMi j
!
+
k∗+k
X
j=1
βj
 k∗+k
X
i=1
mi jMi j
!
=
k∗+k
X
i=1
αiAw +
k∗+k
X
j=1
βjAw,
using the expansion of Aw by the ith row in the ﬁrst sum and by the jth
column in the second.
Proof of lemma 3.2:
Since
ci j =
(
s2jr(mi j)
if i ≤k∗,
s2j−2r(mi j)
if i > k∗,
we have
⋄(ci j) =
(
s2j ¯ϕ(mi j)
if i ≤k∗,
s2j−2 ¯ϕ(mi j)
if i > k∗.
In every case mi j is either h∗
n or hn for some n depending on the index
vector w, and is hence an eigenvector of ¯ϕ.
For i ≤k∗we have mi j = h∗
n with n = wi−j+1 and ¯ϕ(mi j) = (v−1s2n−1+
δ −v−1s−1)mi j, while for i > k∗we have mi j = hn with n = wi + j −1 and
¯ϕ(mi j) = (v−1s−2n+1 +δ −vs)mi j. In each case ⋄(ci j) = (αi +βj)mi j, where
αi
=
(
v−1s2wi+1
if i ≤k∗,
vs1−2wi
if i > k∗
βj
=
s2j(δ −v−1s−1) = s2j−2(δ −vs)
=
v−1s2j−2 −vs2j
s −s−1
.
✷
The theorem is now established, with
cw
=
s−2k∗
 k∗+k
X
i=1
αi +
k∗+k
X
j=1
βj −δ
k∗+k−1
X
j=1
s2j
!
(21)
✷
18
3.1
