---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-002-23-adding-a-superpotential
section_title: "Adding a superpotential"
section_number: 2.3
pages: 11-12
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
In the framework of [19], another important operation on a 3d N = 2 SCFT T was the
addition of a superpotential. The index is aﬀected by superpotential terms in a simple
fashion; one just has to drop, in an appropriate way, any ﬂavor symmetry broken by the
superpotential.
This has three basic consequences. To illustrate them, suppose that we add a superpo-
tentialW charged only under the ﬁrst U(1) of the ﬂavor symmetry group U(1)N; in other
words,W has electric chargecW = (1, 0,..., 0). Suppose thatW also has R-chargeRW. Then:
1. In order for W not to break R-symmetry, its R-charge must equal 2. This requires an
electric R-charge shift by αe = (RW− 2, 0,..., 0), so that RW−αe·cW = 2, thereby
multiplying the index by q(1−RW/2)e1, where e = (e1,...,e N).
2. The theory cannot be coupled to ﬂux for a broken ﬂavor symmetry. Therefore, we must
restrict m = (0,m′), where m′ = (m2,...,m N).
3. The Hilbert space cannot be graded by the broken ﬂavor charge, and states whose
diﬀerence in charge is a multiple of cW will now live in the same charge sector. This
means that we must sum over e1.
Altogether, we ﬁnd that the addition of W amounts to
IT (γ;q) +W−→ IT′(γ′;q) =
∑
e1∈Z
q
(
1−RW
2
)
e1IT (γ;q)
⏐⏐
m1=0, (2.21)
7It is interesting to remark that in the context of four-dimensional N = 2 gauge theory, wall-crossing
considerations lead to the conjecture that (−1)R+2j3 should always be equal to a quadratic reﬁnement of the
charge lattice when acting on BPS states [20].
– 10 –
with a new reduced charge vector γ′ = (m′,e′) = (m2,...,m N,e 2,...,e N).
In general, a superpotential might contain a sum of several operators Oi, with general
electric chargesci and R-chargesRi. We can add these operators one at a time, in any order.
Each of them transforms the index as
IT (γ;q)
+Oi
−→ IT′(γ′;q) =
∑
n∈Z
q
(
1−Ri
2
)
nIT (e +nci,m ;q)
⏐⏐
m·ci=0. (2.22)
This can be thought of as a discrete version of a “symplectic quotient,” with respect to a
moment map⟨ci,m⟩. After adding all the operators Oi, we will be left with a charge vector
γ′ = (m′,e′) that obeys m′·ci = 0 and e′≡e′ +nici (ni∈ Z), for all i.
