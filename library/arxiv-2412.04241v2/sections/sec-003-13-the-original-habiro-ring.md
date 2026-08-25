---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-003-13-the-original-habiro-ring
section_title: "The original Habiro ring"
section_number: 1.3
pages: 4-5
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
tion [27]
H := lim←−n
Z[q]/(q;q)nZ[q] (3)
(where (q;q)n = (1−q)... (1−qn) is the q-Pochhammer symbol), originated in Quantum
Topology as a natural home for quantum invariants of knots and 3-manifolds such as the
Kashaev invariant of a knot [32] or the Witten-Reshetikhin-Turaev invariant of an integer
homology 3-sphere [28]. A detailed discussion of this ring is given in the recent work [21].
Let us recall some basic properties of H whose proofs can be found in Habiro [27]. From
its very definition, it follows that it consists of elements of the form
f(q) =
∞X
n=0
Pn+1(q)(q;q)n, P n(q) ∈ Z[q]. (4)
(The shift of index by 1 will be very convenient in Section 5 and reflect multiplicative
properties of n.) This makes it easy to construct elements of H. In fact, those quantum
invariants of knots and three-manifolds often arise as expressions of this form. An example
coming from the Kashaev invariant of the trefoil (3 1) knot is given by [33, Eqn.(4.7)]
f31(q) =
∞X
n=0
(q;q)n ∈ H. (5)
This particular element ofH was studied years later by Kontsevich and Zagier (cf. [49]), with-
out knowing its topological provenance, from the point of view of its modularity properties
(with respect to τ, where q =e2πiτ ).
A different property of the Habiro ring will play the central role in this paper. Observe
that if q = ζm is a primitive m-th root of unity, then ( q;q)n = 0 for all m > n; thus an
element f(q)∈H can be evaluated at q = ζm and the result is an element of Z[ζm]. More
generally, whenq =ζm +x, we have (q;q)n∈x⌊n/m⌋Z[ζm][x]. This implies that if f(q) is an
element of the Habiro ring, then f(ζm +x)∈ Z[ζm][ [x] ], giving rise to a ring homomorphism
ιm :H→ Z[ζm][ [x] ]. Putting these homomorphisms together, we obtain a map
ι :H→
Y
m≥1
Z[ζm][ [x] ], such that ι(f) = ( fm(x))m≥1, f m(x) := f(ζm +x), (6)
where ζm for each m is a fixed primitive m-th root of unity. We will always suppose that
the collection (ζm) is a compatible collection of roots of unity of order m, that is a collection
satisfying
ζmm′ = ζmζm′, (m,m′) = 1 , (ζpr)p = ζpr−1 (7)
for all positive integers m and m′, primes p and positive integers r. For example, one can
think of ζm = exp(2πiP
p primep−vp(m)), with vp(m) being the p-adic valuation of m. We
note that our choice of compatible collection differs from the traditional choice ωm =e2πi/m,
which does not satisfy (7), but instead satisfies ωm
mm′ = ωm′. However, our choice satisfies
