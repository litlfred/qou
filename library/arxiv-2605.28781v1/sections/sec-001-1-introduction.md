---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
Given any finite setAin some ring we define the sum set and product set ofAas
A+A={a+b:a,b∈A}andAA={ab:a,b∈A}.
The sum-product conjecture in a given ring is that at least one of these must grow
near-maximally; more precisely
(1.1) max(|A+A|,|AA|)≥|A| 2−o(1)
(where theo(1) term tends 0 as|A|→∞). This is often attributed to Erd˝ os and
Szemer´ edi, who proved the first results in this direction [13], but it first appeared
in the literature in a paper of Erd˝ os in 1976 [10] (in which he says he first made the
conjecture 18 months earlier). This question makes sense over any ring (although
there are obvious complications in finite rings or rings with zero divisors). Erd˝ os
[10] asked this specifically forZ,R, andC, although his main interest was for
A⊂Z.
Most proofs in the sum-product literature are geometric and combinatorial, using
no number theory, and thus apply to any finiteA⊂R; the best result achieved in
this direction so far is
max(|A+A|,|AA|)≥|A|
4
3 +c−o(1) forA⊂R
for some small constantc >0. This was proved withc= 0 by Solymosi [38] and
for somec>0 by Konyagin and Shkredov [25]. The value ofchas been improved
a number of times since, with the current record ofc= 10
4407 due to Cushman [8].
In this paper we prove that the sum-product conjecture (1.1) is false over the
reals, by constructing arbitrarily large counterexamples in totally real algebraic
1
arXiv:2605.28781v1  [math.NT]  27 May 2026
2 THOMAS F. BLOOM, WILL SA WIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
number fields of large degree. The degree of these fields tends to infinity as the sets
grow (like≍lognfor a counterexample of sizen), and so (1.1) may still be true in
number fields of bounded degree (and, in particular, the original setting ofZ).
Theorem 1.1.There exists an absolute constantc >0such that there are arbi-
trarily large finiteA⊂Rwith
max(|A+A|,|AA|)≤|A| 2−c.
Our arguments deliver an explicit value ofc, but this is a tedious calculation,
and the value obtained is very small. Since the main interest of this result is the
existence of an absolute constantc >0, we have chosen to present a non-explicit
version of the proof, to better demonstrate the main ideas. In Section 5 we sketch
how a version of the proof with explicit constants can deliverc≥0.00000087
(although this should not be taken too seriously, and can certainly be improved
with a little more effort).
Theorem 1.1 is easily deduced from the following more general result.
Theorem 1.2.There exists an absolute constantC >0such that the following
holds. There are infinitely manyd, with accompanying totally real number fieldsK
of degreedoverQ, such that, for anyX≥1, there existsA⊂O K with
Xd≤|A|≤(CX) d,
|A+A|≤C d|A|, and|AA|≤2 −d|A|2.
By choosing an arbitrary embedding ofKintoR, andX=C 1/ϵ, we deduce
the following, which provides examples in which the sum set is very small, and yet
there is still a power saving on the size of the product set.
Corollary 1.3.There exists an absolute constantc >0such that the following
holds. For anyϵ∈(0,1)there are arbitrarily largeA⊂Rwith
|A+A|≤|A| 1+ϵ and|AA|≤|A| 2−cϵ.
Theorem 1.1 is an immediate consequence. This result should also be compared
to the lower bound of Solymosi [38], who proved that for anyA⊂R
(1.2)|A+A| 2|AA|≥|A| 4−o(1).
Using similar ideas we also obtain new lower bounds in a number of other related
problems of a sum-product flavour, which we summarise below.
1.1.Many sums and products.Erd˝ os [11] also made the stronger conjecture
that, for anyk≥2 andϵ>0,
max(|kA|,|A (k)|)≫ k,ϵ|A|k−ϵ,
wherekAandA (k) denote thek-fold sum set andk-fold product set, respectively.
(Once again this was forA⊂Zoriginally, but Erd˝ os and Szemer´ edi [13] asked it
also forA⊂R). Our methods provide a strong counterexample to this conjecture
for largek.
Theorem 1.4.There exists an absolute constantC >0such that for any fixed
k≥3there exist arbitrarily largeA⊂Rwith
max(|kA|,|A (k)|)≤|A| C logk
log logk .
THE SUM-PRODUCT CONJECTURE IS F ALSE FOR REAL NUMBERS 3
Furthermore, for any fixedϵ∈(0,1), there exist arbitrarily largeA⊂Rsuch that
max(|kA|,|A (k)|)≤|A| C1/ϵ+ϵlogk for allk≥3.
This is likely the best possible dependence onkin the exponent (at least fork
fixed and|A|→∞). It follows from work of Mudgal [31] and the recent resolution
of the weak polynomial Freiman–Ruzsa conjecture by Gowers, Green, Manners, and
Tao [18] that, for anyA⊂R, for allk≥3,
max(|kA|,|A (k)|)≥|A| (logk)c
for some absolute constantc>0. With sufficiently improved bounds on the number
of solutions to linear equations in multiplicative groups (as discussed in Section 6)
this exponent can likely be improved to logk
log logk . This exact quantitative dependence
was achieved forA⊂Zby P´ alv¨ olgyi and Zhelezov [44]. In a similar vein, Konyagin
[26] proved that ifA⊂Cis a finite set such that|AA|≤|A| 1+O(1/k) then|kA|≥
|A|clogk for some constantc>0.
