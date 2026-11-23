---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-004-31-symmetric-functions-and-the-skein-of-the-annu
section_title: "Symmetric functions and the skein of the annulus."
section_number: 3.1
pages: 10-13
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
Symmetric functions and the skein of the annulus.
In this section I recall some explicit results about elements in the Hecke
algebras and their closure in C, and their interpretation in the context of
symmetric functions, following the methods of Macdonald. This leads to a
simple description in terms of generating functions of some interrelations in
C, and also of the elements to be used later to represent the power sums of
the Murphy operators.
The starting point is the description of the two simplest idempotents in
Hn, corresponding to the single row and column Young diagrams. These
are given algebraically in [6]; here I use the skein version as described in
[12] in terms of the positive permutation braids ωπ, π ∈Sn. Deﬁne two
quasi-idempotents by
an =
X
π∈Sn
sl(π)ωπ,
bn =
X
π∈Sn
(−s)−l(π)ωπ,
where l(π) = wr(ωπ) is the writhe of the braid ωπ.
The following result is straightforward.
Lemma 3.2 We can write
an = an−1γn,
where γn = 1 + sσn−1 + s2σn−1σn−2 + · · · + sn−1σn−1 · · · σ1.
We have γn+1 = 1 + sσnγn, and also an immediate skein relation
γ n+1
=
γ n
+ sn
,
in Rn+1
n+1.
The next lemma is proved in [13].
10
Lemma 3.3 For any braid β ∈Bn we have anβ = ϕs(β)an = βan, where
ϕs(β) = swr(β).
Similar results, with s replaced by −s−1, hold for bn.
The element an then satisﬁes
a2
n = ϕs(an)an = ϕs(an−1)ϕs(γn)an.
Since ϕs(γn) = 1 + s2 + · · · + s2n−2 = sn−1[n], we have an immediate
corollary.
Corollary 3.4 We can write
sn−1[n]hn = hn−1γn,
where hn = an/ϕs(an) is the true idempotent.
The element hn ∈Hn is the idempotent which corresponds to the single
row with n cells. The single column idempotent is given from hn by using
−s−1 in place of s.
With a slight abuse of notation write hn ∈C in place of ˆhn for the
closure of this element in C, and en ∈C for the closure of the single column
idempotent.
Remark. Aiston uses the notation Qcn and Qdn in [1], in place of en and hn
which are used here to suggest the terminology and techniques of symmetric
functions from [11].
Write
H(t) = 1 +
∞
X
n=1
hntn
for the generating function of the elements {hn}, regarded as a formal power
series with coeﬃcients in C, and similarly set E(t) = 1 +
P∞
n=1 entn. In [1]
Aiston showed that
Theorem 3.5
E(−t)H(t) = 1,
as power series in C.
11
If we regard the elements hn formally as the nth complete symmetric
functions in a large number N of variables x1, . . . , xN, setting
H(t) =
N
Y
i=1
1
1 −xit ,
then E(t) =
Q(1 + xit) and en is the nth elementary symmetric function in
the variables.
Following Macdonald, the Schur function sλ(x1, . . . , xn) for each partition
λ can be expressed as a polynomial in the elements hn which does not depend
on N for large enough N, and is therefore determined formally by the series
H(t) and λ as an element sλ of C. This is the element sλ used by Kawagoe,
which is identiﬁed with the idempotent closures Qλ by Lukac in [10].
The π(n) elements {sλ} with |λ| = n form a linear basis for Cn, and can
be expressed in terms of the monomials of weight n in {hr} by the classical
Jacobi-Trudy formulae [11].
Indeed the skein C+, deﬁned as ∪Cn, is spanned by all monomials in {hr},
and can be interpreted as the ring of symmetric polynomials in an unlimited
number of variables {xi}.
Monomials in the geometrically simpler closed braid elements {Am} also
span Cn, and it is thus interesting to relate these directly to {hr}. An at-
tractive formula connecting these two generating sets can be derived from
corollary 3.4.
Theorem 3.6 Write A(t) = 1 + z P∞
m=1 Amtm, with z = s −s−1.
Then
A(t) =
H(st)
H(s−1t) = H(st)E(−s−1t).
The proof will be given in section 4.
Lemma 3.7 The elements {hn} are invariant under the mirror map switch-
ing crossings and inverting s and v.
Proof :
In Hn we have σian = ϕs(σi)an = san. Then σian = σ−1
i an = s−1an
giving σian = san. It follows that βan = ϕs(β)an for any β and so anan =
ϕs(an)an.
On the other hand anan = anϕs(an) by lemma 3.3, so that
hn =
an
ϕs(an) =
an
ϕs(an) = hn.
12
✷
Corollary 3.8 The inverse series to A(t) = 1 + z P Amtm is A(t) = 1 −
z
P Amtm, where Am is the negative closed braid corresponding to Am.
Proof :
Apply the mirror map in theorem 3.6 to get
A(t) = H(st) / H(s−1t) = H(s−1t) / H(st) = A(t)−1.
✷
In our later description of the power sums of Murphy operators we use
the element Pm ∈C which can be interpreted formally as the mth power
sum, Pm =
P xm
i , of the variables. This is determined unambiguously as a
polynomial in {hr}, and hence an element of C, by Newton’s power series
equation
∞
X
m=1
Pm
m tm = ln H(t).
Aiston showed in [2] that [m]Pm is the sum of m closed m-string braids given
by switching the ﬁrst i crossings of the closed braid Am from positive to
negative, for i = 0, . . . , m −1. Her proof depends on some quantum group
translations to identify sλ and Qλ, and to write Am in terms of sλ. In another
article I give a direct skein theory proof of her result, using theorem 3.6.
