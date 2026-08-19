---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-164-55-analytic-classification-of-linear-q-differenc
section_title: "ANALYTIC CLASSIFICATION OF LINEAR q-DIFFERENCE EQUATIONS 97"
section_number: 5.5
pages: 103-104
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
Proof. — If A = A0, the formal solution boils down to the identity ma-
trix, which plainly coincides with F A
(Λ 1,...,Λ k−1) for any compatible partition
(Λ1,..., Λk−1).
On the other hand, if A⁄=A0, the polynomial Ui,j in (3.2) are not all 0. To
begin with, assume that Uj−1,j⁄= 0 for some index j. Since ˆFj−1,j diverges,
its sum along divisor Λ j will be distinct from its sum along any diﬀerent
divisor. More generally, when Ui,j⁄= 0, the solution F A
(Λ 1,...,Λ k−1) will depend
in a one-to-one way on divisor Λ j; details are left to the reader.
For anyλ∈ C∗, let [λ;q :A0] be the ordered partition of divisors generated
by the spiral [λ;q] in the following way:
[λ;q :A0] :=
(
(µ2−µ1)[λ;q], (µ3−µ2)[λ;q],..., (µk−µk−1)[λ;q]
)
,
where µj are as in (3.1), i.e. A0 = diag (zµ1A1,...,z µkAk).
If [λ;q : A0] is generic with respect to A0, we will write λ∈{A0} and say
that λ is generic for A0.
Theorem 5.5.7 (Stokes phenomenon) . — Fix some λ0 ∈{ A0} and for
any λ∈{A0} and A∈C A0, set:
Stλ0(λ;A) :=
(
F A
[λ0;q:A0]
) −1 F A
[λ;q:A0] .
The following conditions are equivalent.
1. There exists λ∈{A0} such that [λ;q]⁄= [λ0;q] but St λ0(λ;A) =Id.
2. For all λ∈{A0}, the equality St λ0(λ;A) =Id holds.
3. One has A =A0.
Proof. — It follows immediately from proposition 5.5.6
In the previous theorem, each St λ0(λ;A) represents an upper-triangular
unipotent matrix-valued function that is analytic in some d isk 0 <|z| < R
except at spirals [λ;q] and [λ0;q]; moreover, it is inﬁnitely close to the identity
matrix as z→ 0. If Y := St λ0(λ;A)−In, then Y is ﬂat at zero and satiﬁes
the relation:
(σqY ) A0 =A0 Y.
Theorem 5.5.7 implies that each matrix A chosen within the isoformal class
CA0 reduces to the normal form A0 whenever the Stokes matrix St λ0(λ;A)
becomes trivial for some couple of generic parameters λ0, λ such that
λ⁄=λ0 modqZ.
98 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
We shall now show that for any given pair of generic parameter s λ0, λ
that are not q-congruent, the data{Stλ0(λ;A),A 0} constitutes a complete set
of analytical invariants associated to theq-diﬀerence module determined byA.
Indeed, the notation Stλ0(λ;A) introduced for anyA∈C A0 can be naturally
generalized for any matrixB∈ G(C{z}) that belongs to the same formal class
as A0. To simplify, assume that ( A0)−1B∈ G(C{z}); this is for instance the
case if B is taken in Birkhoﬀ-Guenther normal form (deﬁnition 3.3.6). From
corollary 5.5.4 it follows that the corresponding conjugac y equation:
(σqY ) B =A0 Y
admits, in G, a unique solution in the space of multi-summable functions
associated to any given generic ordered partition of diviso rs [λ;q :A0]. Thus,
we are led to the notations F B
[λ;q:A0] and Stλ0(λ;B) as in the case of A∈C A0.
Corollary 5.5.8 . — Suppose that B1 and B2 are two matrices such that
(A0)−1Bi∈ G(C{z}). Then the following assertions are equivalent.
