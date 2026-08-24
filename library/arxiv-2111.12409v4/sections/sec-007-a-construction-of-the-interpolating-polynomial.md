---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem Paolo Dolce Francesco Zucconi 0 Introduction 1 0.1 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
section_id: sec-007-a-construction-of-the-interpolating-polynomial
section_title: "A Construction of the interpolating polynomial"
section_number: null
pages: 19-20
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmi"
---
In this appendix we will sketch the construction of the inter polating polynomial δ of section 2. For
all the details the reader can check [ Cor97].
We employ the same notations of section 2. We are going to construct a complicated matrix
A(X) depending on the following parameters: s, t1, . . . , tn ∈ R, with 0 < s < 1 and 0 < t h < N
2 for
h = 1 , . . . , n. The columns of the matrix are indexed by a ∈ G N ; the rows are indexed by ih ∈ G th
(for any h = 1, . . . , n) and moreover we put in+1 ∈ G s. The order on multi-indices is the lexicographic
one.
19
A(X) :=


(a
ih
)
α a−ih
h
( a
in+1
)
X a−in+1


ih,a
(45)
Note that A(X) has #( Gs) +∑
h #(Gth ) rows and #( GN ) = ∏ n
h=1⌊dh + 1⌋ columns, and moreover
all the elements of the last #( Gs) rows are monomials. Clearly we can always choose the parame ters
s, t1, . . . , tn ∈ R in order to obtain a matrix A(X) with more rows than columns. Let’s see an explicit
condition that tells us when this can be achieved: the number of rows is greater than the number of
columns if
#(Gs) +
n∑
h=1
#(Gth) >
n∏
h=1
⌊dh + 1⌋ ,
therefore thanks to Lemma 2.2, for d1, . . . , dN very big, it is enough to have the following conditions
on volumes:
V (s) +
n∑
h=1
V (th) > 1. (46)
The volumes V (s), V (t1), . . . , V(tn) heavily determine the algebraic properties of the matrix A(X),
in fact we will now present a stronger condition on the quanti ty V (s) +∑ n
h=1 V (th) ensuring that
A(X) has maximal rank.
Proposition A.1. Let d1, . . . , dN be big enough and let d1 > d 2 > . . . > d N . Moreover assume that
α(j)
h ⁄= α(j)
k , ∀ j = 1, . . . N, ∀ h, k = 1, . . . , n, h ⁄= k .
If for s, t1, . . . , tn ∈ R, with 0 < s < 1 and 0 < t h < N
2 we have that
V (s) +
n∑
h=1
V (th) >
N−1∏
j=1
(
1 + (n − 1)
N∑
i=j+1
di
dj
)
(47)
then, for any β = (β(1), β(2), . . . , β(N)) ∈ KN such that
β(j) ⁄= α(j)
h , ∀ j = 1, . . . N, ∀ h = 1, . . . , n, ,
the rank of A(β ) is maximal and equal to the number of columns.
Proof. See [Cor97, Proposition 2.1] and notice that it uses a version of Dyson’ s lemma for polynomials
in many variables proved in [ EV84].
One can always assume that the parameters s, t1, . . . , tn are chosen in a way that we always get
(1 + η)N < V (s) +
n∑
h=1
V (th) < 1 + 2N η (48)
It is not diﬃcult to see (check [ Cor97, page 159]) that equation ( 48) implies ( 47). Therefore thanks
to Proposition A.1 we can extract from A(X) a square submatrix M (X) of dimension
r := #(GN ) =
n∏
h=1
⌊dh + 1⌋ ,
which is the number of columns of A(X), such that M (X) has maximal rank for any β componentwise
diﬀerent from any α h. Moreover one can choose M (X) in a way that contains the last #( Gs) rows
of A(X), since they are linearly independent for any choice of β ∈ KN . The polynomial δ(X) is
the determinant of the matrix M (X). At this point all the arguments used in [ Cor97] to prove the
bounds about δ can be applied verbatim in our setting with the only diﬀerenc e that in order to
estimate hX(δ) one has to take the integral over Ω instead of the summation o ver all places.
