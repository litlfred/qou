---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-055-2b2-the-iteration-of-the-harmonic-frobenius
section_title: "2B2. The iteration of the harmonic Frobenius"
section_number: null
pages: 64-65
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
at(1, 0), in Section 2A2, to discussing the harmonic Frobenius. We ﬁrst describe how the map iter
∫1,0
a,λ
depends on its parametersλ and a.
Deﬁnition 2B.4. For any d∈ N∗, let τ∗,⩽d: K⟨⟨e0∪µN⟩⟩→ K⟨⟨e0∪µN⟩⟩ be the map which sends f=∑
w word f[w]w to∑
w word, depth(w)⩽d f[w]w.
Proposition 2B.5. Let3,˜3, a be three formal variables. There exists a map
iter∫1,0(3,˜3, a): Ad˜51,0(K)(e1)→ K⟨⟨e0∪µN⟩⟩[˜3, a](3), (2-2)
such that, for any f∈ Ad˜51,0(K)(e1), wordw, a∈ N∗ such that a> depth(w) andλ∈ K\{ 0} which is
not a root of unity, we have
iter
∫1,0
a,λ( f)[w]= iter∫1,0(λ,λ a, a)( f)[w].
Proof. With the assumptions of the statement, let d= depth(w); knowing that g[∅]= 1, dualizing the
multiplication of the a factors in (1-17) gives
iter
∫1,0
a,λ(g)[w]=
∑
0⩽d′⩽d
∑
0⩽i1<···<id′⩽a−1
∑
wi1⁄=∅,...,wid′⁄=∅
wi1···wid′=w
g(λi1−1e0,(λ i1−1 Adg(ξ) i1−1(eξ))ξ)[wi1]×···
× g(λid′−1e0,(λ i1−1 Adg(ξ) id′−1(eξ))ξ)[wid′]. (2-3)
We have assumed that a> d; let us thus separate the indices i j⩽ d and i j> d:
∑
0⩽d′⩽d
∑
0⩽i1<···<id′⩽a−1
=
∑
0⩽d′′⩽d′⩽d
∑
0⩽i1<···<id′′⩽d
∑
d<id′′+1<···<id′⩽a−1
.
This yields an expression of (2-3), as a K -linear combination indexed by{(d′′, d′)| 0⩽ d′′⩽ d′⩽ d}×
{deconcatenations ofw in d′ nonempty subwords} which is independent of a but depends polynomially
ofλ, and with coefﬁcients as well independent of a and polynomial functions ofλ, of the numbers
∑
d<id′′<···<id′⩽a−1
g(λi1−1e0,(λ id′′−1 Adg(ξ) id′′−1(eξ))ξ)[wid′′]×···× g(λid′−1e0,(λ id′′−1 Adg(ξ) id′′−1(eξ))ξ)[wid′].
(2-4)
Letϵ(ξ)= g(ξ)− 1 and˜ϵ(ξ)= g(ξ)−1− 1. For 0⩽ i j⩽ a− 1, we have (where τ∗,⩽d is deﬁned in
Deﬁnition 2B.4)
τ∗,⩽d(Adg(ξ) i j−1(eξ))=
∑
m j,m′
j∈N
m j⩽i j,m′
j⩽i j,m j+m′
j+1⩽d
( i j
m j
)( i j
m′
j
)
˜ϵ
m′
j
ξ eξϵ
m j
ξ .
When i j> d, the collection of conditions{m j, m′
j∈ N, m j⩽ i j, m′
j⩽ i j, m j+ m′
j+ 1⩽ d} is equivalent
to{m j, m′
j∈ N, m j+ m′
j+ 1⩽ d}; thus, dualizing in (2-4) each factor g(λi j−1e0,(λ i j−1 Adg(ξ) i j−1(eξ))ξ)
tells us that (2-4) is a linear combination, independent of a andλ, of sums
∑
d<id′′<···<id′⩽a−1
d′
∏
j=d′′
( i j
m j
)( i j
m′
j
)
λi j weight j,
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1731
where weight j∈ N∗ arises as the weight of a certain quotient sequence ofwi j , and
( i j
m j
)( i j
m′
j
)
are polynomials
of i j.
Finally, any function ofa of the form∑
L⩽I1<···<Iδ⩽a−1
∏δ
j=1 Pj(I j)λI j C j with L,δ∈ N∗, C1,..., Cδ∈
N∗ and P1,..., Pδ∈ K[T] polynomials, depends on a as a polynomial function of (a,λ a): one can
reduce this statement to L= 0 by splitting an iterated sum over 0⩽ I1<··· < Iδ⩽ a− 1 at L and by
induction onδ, then use, again by induction on δ that, for all deg j∈ N∗, we have
deg j∑
I j=0
Iδ′
j λC j I j=
(
λC j d
d(3C j)
)l(λC j deg j− 1
3C j− 1
)
. □
Let us now deﬁne the map of iteration of the harmonic Frobenius of integrals at (1, 0), by using the
above iteration map and the summation map S of Deﬁnition 2A.2.
Deﬁnition 2B.6. Let iter
∫1,0
har(a,λ)= S◦ iter∫1,0(λ,λ a, a): Ad˜51,0(K)(e1)→ K⟨⟨e0∪µN⟩⟩
∫1,0
har .
We can now deduce from Section 2B1, and the previous proposition a second description of the iterated
harmonic Frobenius as a function of its number of iterations; this is (0-4).
By Proposition 2B.1, we have8q,˜α= iter
∫1,0
˜α/˜α0,q;˜α0
(8q,˜α0), thus by Proposition 2B.5, we have 8q,˜α=
iter∫1,0(q˜α0, q˜α,˜α/˜α0)(8q,˜α0), whence S8q,˜α= S iter∫1,0(q˜α0, q˜α,˜α/˜α0)(8q,˜α0). By Deﬁnition 2B.6, this
amounts to S8q,˜α= iter
∫1,0
har(˜α/˜α0, q˜α)(8q,˜α0). Finally, by (1-19), we have S8q,˜α= harq,˜α. Whence (0-4).
