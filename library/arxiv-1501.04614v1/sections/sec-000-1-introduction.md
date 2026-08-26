---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL II"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL II — We continue our study of the degree of the colored Jones polyn omial under knot cabling started in [8]."
---
For a knot K ⊂ S3, let n(K) denote a tubular neighborhood of K and let MK :=
S3 \ n(K) denote the exterior of K. Let ⟨µ, λ ⟩ be the canonical meridian–longitude basis
of H1(∂n(K)). An element a/b ∈ Q ∪ {1/ 0} is called a boundary slope of K if there is
a properly embedded essential surface ( S, ∂S ) ⊂ (MK , ∂n (K)), such that ∂S represents
aµ +bλ ∈ H1(∂n(K)). Hatcher showed that every knot K ⊂ S3 has ﬁnitely many boundary
slopes [6]. We will use bsK to denote the set of boundary slopes of K.
For a Laurent polynomial f (v) ∈ C[v±1/ 4], let d+[f ] be the highest degree of f in
v. For a knot K ⊂ S3, Garoufalidis [3] proved that the highest degree of its colo red
Jones polynomial is a quadratic quasi-polynomial. This mea ns that there exist an integer
NK > 0 and periodic functions aK(n), b K (n), c K (n) such that
d+[JK (n)] = aK (n) n2 + bK (n)n + cK(n)
for n ≥ NK. The common period of aK (n), b K (n), c K (n) is called the period of K. Let
d−[JK (n)] denote the lowest degree of JK (n) in v. For a sequence {xn}, let {xn}′ denote
the set of its cluster points. Elements of the set
jsK :=
{
4n−2d+[JK (n)]
} ′
and js∗
K :=
{
4n−2d−[JK (n)]
} ′
are called Jones slopes of K. It is known that JK (n, v ) = JK ∗ (n, v −1), where K ∗ is the
mirror image of K. Thus statements about the lowest degree d−[JK (n)], which is equal
to −d+[JK ∗ (n)], can be equivalently made. With this in mind we will mostly discuss the
highest degree in this paper.
November 7, 2018.
E. K. was partially supported in part by NSF grants DMS–11058 43 and DMS–1404754 .
1
2
In [8] we studied the behavior of d+[JK (n)] under knot cabling for knots of period at
most two. In this paper we study knots with period greater tha n two.
To state our results, let K be a knot with framing 0, and p, q are co-prime integers. The
(p, q )-cable Kp,q of K is the 0-framed satellite of K with pattern ( p, q ) torus knot. It is
known that K−p, −q = rKp,q , where r Kp,q denotes Kp,q with the opposite orientation, and
that the colored Jones polynomial of a knot is independent of the orientation of the knot.
Hence in the statements of results below, and throughout the paper, we will assume that
our cables are non-trivial in the sense that q > 1.
Theorem 1.1. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = an2 + b(n)n + d(n)
where a is a constant, b(n) and d(n) are periodic functions with b(n) ≤ 0. Let
M1 = max {|b(i) − b(j)| : i ≡ j (mod 2) },
M2 = max {2b(i) + |b(i) − b(j)| + |d(i) − d(j)| : i ≡ j (mod 2) }.
Suppose p − (4a − M1)q < 0 or p − (4a + M1)q > max{0, M 2}. Then for n ≫ 0 we have
d+[JKp,q(n)] = An2 + B(n)n + D(n)
where A is a constant, and B(n), D (n) are periodic functions with B(n) ≤ 0. Moreover,
if jsK ⊂ bsK then jsKp,q ⊂ bsKp,q.
Theorem 1.1 has applications to two open conjectures about t he degree of JK (n). The
ﬁrst conjecture, formulated by the authors in [8], asserts t hat the linear part bK (n) is not
positive and it detects the existence of essential annuli in the knot complement.
Conjecture 1.2. [8] For every non-trivial knot K ⊂ S3, we have
bK(n) ≤ 0.
Moreover, if bK(n) = 0 then K is a composite knot or a cable knot or a torus knot.
Note that bU (n) = 1 / 2 for the trivial knot U . It is known that a knot K is composite or
cable or a torus knot if and only if its complement MK contains embedded essential annuli
[7, Lemma V.1.3.4]. Thus the last part of Conjecture 1.2 can a lternatively be stated as
follows: If bK(n) = 0, then MK contains an embedded essential annulus.
The second conjecture is the Slope Conjecture formulated by Garoufalidis in [4].
Conjecture 1.3 (Slope Conjecture) . [4] For every knot K ⊂ S3 we have
jsK := {4aK (n)} ⊂ bsK.
Conjecture 1.3 is known for the following classes of knots:
(1) alternating knots, non-alternating knots with up to nin e crossings, torus knots,
the family ( −2, 3, 2m + 3) of 3-string pretzel knots (by Garoufalidis [4]).
(2) adequate knots (by Futer, Kalfagianni and Purcell [2]).
(3) iterated cable knots of B-adequate knots, iterated torus knots, and iterated of all
non-alternating knots with up to nine crossings that have pe riod two (by Kalfa-
gianni and Tran [8]).
3
(4) a certain 2-parameter family of closed 3-braids, called 2-fusion knots (by Garoufa-
lidis and Dunﬁeld [1] and Garoufalidis and van der Veen [5]).
(5) some families of 3-string pretzel knots (by Lee and van de r Veen [9]).
In this paper we will verify Conjecture 1.2 for 2-fusion knot s and “most” of their cables.
For cases (1)-(3) the conjecture was veriﬁed in [8]. Theorem 1.1 implies the following.
Corollary 1.4. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = an2 + b(n)n + d(n)
where a is a constant, b(n) and d(n) are periodic functions. Let M1, M 2 be as in the
statement of Theorem 1.1. If K satisﬁes Conjectures 1.2 and 1.3, then Kp,q satisﬁes the
conjectures provided that p − (4a − M1)q < 0 or p − (4a + M1)q > max{0, M 2}.
As an application of Corollary 1.4 we will prove Conjectures 1.2 and 1.3 for cables of
2-fusion knots.
We would like to thank Stavros Garoufalidis for helpful corr espondence.
