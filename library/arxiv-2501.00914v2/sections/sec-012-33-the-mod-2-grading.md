---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-012-33-the-mod-2-grading
section_title: "The mod 2 grading"
section_number: 3.3
pages: 17-19
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
to whichdHF(Y) has Euler characteristic|H 1(Y;Z)|if this order is finite, and 0 otherwise. We will
write the graded pieces as dHF even(Y) and dHF odd(Y).
Lemma 3.4.For alln≥0, we havedeg(F X◦n) = 1anddeg(F Wn+1) = 0with respect to the absolute
Z/2Zgradings on dHF(S 3
n(K))and dHF(S 3
n+1(K)). Therefore, each of the elementsz n,i from(3.2)
has odd grading.
Proof.A Spin c cobordism (Z,t) : (Y 0,t|Y0)→(Y 1,t|Y1) between connected, nonempty 3-manifolds
induces a cobordism map on dHFthat shifts the absoluteZ/2Zgrading by
deg(FZ,t)≡ 1
2(χ(Z) +σ(Z) +b 1(Y1)−b 1(Y0)) (mod 2).
This is discussed in detail for monopole Floer homology in [KM07]: see [KM07,§22.4] for the
reduction of the canonical plane field grading on }HM(Y) to a canonicalZ/2Zgrading, and [KM07,
18 JOHN A. BALDWIN AND STEVEN SIVEK
§25.4] for the computation of the mod 2 degrees of cobordism maps. In [KM07,§42.3] this is applied
to the surgery exact triangle (3.4), and the authors show that forn≥0 the mapF X◦n has odd
degree whileF Wn+1 and the connecting homomorphism both have even degree.
In Heegaard Floer homology, Huang–Ramos [HR17] lifted the relativeZ/d(c 1(s))Zgrading on
HF◦(Y,s) (itself a lift of the absoluteZ/2Zgrading) to an analogous plane field grading, and showed
that this lift is compatible with the degree formula for cobordism maps, so the same formula used
for deg(FZ,t) (mod 2) in }HMalso applies to dHF. In particular, since dHF(S 3)∼= Fis supported in
even grading, it follows that the elementsz n,i =F X◦n,tn,i(1) have odd grading.□
Lemma 3.4 tells us that the subspaces of eachdHF(S 3
n(K)) spanned by the relative invariantsz n,i
are also entirely in odd grading, i.e.,
Sn⊂dHF odd(S3
n(K))
for alln≥0. We can also use it to deduce the following:
Proposition 3.5.Suppose thatKhas genusg≥1, and fix nonnegative integersn≤mwith
m≥2g−1. ThenS n = span{zn,i|i∈Z}fits into a short exact sequence
0→S n→dHF odd(S3
n(K))
FVn,m
−−−−→dHF odd(S3
m(K))→0,
whereV n,m is the cobordismS 3
n(K)→S 3
m(K)of(3.7).
Proof.For anyk≥0, the exact triangle (3.4) has the form
···→ dHF(S 3)
FX◦
k
− −− →dHF(S 3
k(K))
FWk+1
−−−−→dHF(S 3
k+1(K)) δ− →...,
and we recall from [KM07,§42.3] (as noted in the proof of Lemma 3.4) thatδhas even degree.
Since its codomain dHF(S 3)∼= Fis supported in even grading, it follows that
δ

dHF odd(S3
k+1(K))

= 0
and hence by exactness that dHF odd(S3
k+1(K)) lies in the image ofF Wk+1. But thenF Wk+1 also has
even degree, soF Wk+1 must restrict to a surjection
FWk+1 :dHF odd(S3
k(K))→ dHF odd(S3
k+1(K))
for allk≥0.
To conclude, we observe thatF Vn,m is equal to the composition
FWm◦FWm−1◦···◦F Wn+1
of maps which are all surjective on dHF odd, and henceF Vn,m is surjective on dHF odd as well. Since
m≥2g−1, we use Proposition 3.3 to say that the kernel ofF Vn,m is equal toS n.□
The main result of this section is now an immediate corollary:
Theorem 3.6.Fix a nontrivial knotK⊂S 3 and an integern≥0. Then for all integersm≫0,
the dimension of dHF odd(S3
m(K))is equal to
dimdHF odd(∂Xn(K))−dim span{F X◦n,t(1)|t∈Spin c(X◦
n)}.
In particular,Kis an L-space knot if and only if the elements{F X◦n,t(1)}span all of dHF odd(S3
n(K)).
L-SPACES AND KNOT TRACES 19
Proof.The short exact sequence of Proposition 3.5 tells us that for allm≥max(2g−1,n), the
dimension of dHF odd(S3
m(K)) is equal to
dimdHF odd(S3
n(K))−dim span{z n,i|i∈Z}.
But this is exactly the quantity we wanted to prove equal to dim dHF odd(S3
m(K)).□
Remark 3.7.The proof of Theorem 3.6 applies equally well to show thatX n(K) determines the
odd portion of theZ/2Z-graded framed instanton homologyI #(S3
m(K)) form≫0; in particular,
the case whereI #
odd(S3
m(K)) = 0 says that for any fixedn≥0, then-traceX n(K) determines
whether or notKis an instanton L-space knot. Indeed, the key Lemma 3.1 that we used to start
the proof can be replaced by the original [BS23, Proposition 7.1], and then after some mild care
with coefficients the rest of the argument follows in the same way.
Remark 3.8.The casen= 0 of Theorem 3.6 was used in [BS22] to prove that L-space knots are
fibered and strongly quasipositive, as follows: we know (at least forg≥2) that dHF(S 3
0(K),sg−1)
is nonzero [OS04], and its Euler characteristic is zero, so the portions in even and odd gradings are
both nonzero. Theorem 3.6 says that ifKis an L-space knot then dHF odd(S3
0(K),sg−1)̸= 0 must
be spanned byz 0,g−1 =F X◦
0,t0,g−1(1); but then dHF odd(S3
0(K),sg−1)∼= F, and fiberedness follows.
ThenF X◦
0,t0,g−1(1)̸= 0 ultimately implies (via the Heegaard Floer contact invariant) that the open
book forS 3 with bindingKsupports the tight contact structure onS 3, and soKmust be strongly
quasipositive.
