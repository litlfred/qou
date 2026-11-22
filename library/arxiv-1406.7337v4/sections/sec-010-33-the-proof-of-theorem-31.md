---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-010-33-the-proof-of-theorem-31
section_title: "The proof of Theorem 3.1"
section_number: 3.3
pages: 14-20
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
The proof of Theorem 3.1
We will now prove Theorem 3.1 using a series of lemmas, beginning by ﬁrst considering the simpler case that
β ∈B3 is a negative braid.
Lemma 3.1. Let D(K) = bβ, where β ∈B3 is a negative braid that satisﬁes the assumptions of Lemma 2.1.
Then β is generic and, furthermore, we are able to express the parameters k and s of the Schreier normal
form β′ in terms of the original 3-braid β as follows:
(1) k = −# {induced products σn2
2 σn1
1
of negative syllables of β, where n1, n2 ≤−3}.
(2) s = t−(D) = # {negative syllables in β}.
Proof. By Lemma 2.1, we have that K is hyperbolic. By Proposition 3.1, this implies that β is generic. Since
β is a negative braid, then (possibly using cyclic permutation) we may write β as β = σn1
1 σn2
2 · · · σn2m−1
1
σn2m
2
,
where ni ≤−3 and the fact that β is nice forces the condition that m ≥2. Applying the Schreier Normal
Form Algorithm, we get
β
=
σn1
1 σn2
2 · · · σn2m−1
1
σn2m
2
=
(xy)−n1(yx)−n2 · · · (xy)−n2m−1(yx)−n2m
=
(xy)−n1−1(xy2)(xy)−n2−1(x2)y · · · (x2)y(xy)−n2m−1−2(xy2)(xy)−n2m−1x
=
(xy)−n1−1(xy2)(xy)−n2−1(C−1)y · · · (C−1)y(xy)−n2m−1−2(xy2)(xy)−n2m−1x
∼=
(C−1)m−1(xy)−n1−1(xy2)(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−1x
∼=
(C−1)m−1x(xy)−n1−1(xy2)(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−1
=
(C−1)m−1(x2)y(xy)−n1−2(xy2)(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−1
=
(C−1)my(xy)−n1−2(xy2)(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−1
∼=
(C−1)m(xy)−n1−2(xy2)(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−1y
=
(C−1)m(xy)−n1−2(xy2)(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−2(xy2)
=
(C−1)mσn1+2
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+2
1
σ2
=
β′,
where ∼= denotes that cyclic permutation or the fact that C ∈Z(B3) has been used. Thus, we see that
k = −m = −#

induced products σni
2 σni+1
1
of negative syllables of β, where ni, ni+1 ≤−3
	
14
and
s = 2m = # {negative syllables in β} .
Recall that, when looking for the induced products σni
2 σni+1
1
of negative syllables of β to ﬁnd k, we must
look cyclically in the braid word.
We will now consider the more complicated case that β ∈B3 is not a negative braid. Since β is not a
negative braid, then (possibly using cyclic permutation) we may write β as β = P1N1 · · · PtNt, where Pi
denotes a positive syllable of β and where Ni denotes a maximal length negative induced subword of β. Note
that this decomposition arises as a result of Condition (2a), Condition (2b), and Condition (2c) of Lemma 2.1
(the conditions that positive syllables are cyclically neighbored on both sides by negative syllables).
Our strategy for the proof of this case is to apply the Schreier Normal Form Algorithm to the subwords
PiNi, showing along the way that cyclic permutation is never needed in applying the algorithm, to show
that Theorem 3.1 is locally satisﬁed for the PiNi, and to ﬁnally show that juxtaposing the subwords PiNi
to form β allows the local conclusions of Theorem 3.1 for the PiNi to combine to give the global conclusion
of Theorem 3.1 for β.
We now list the types of induced subwords PiNi below. For each subword, we consider the two possible
subtypes. Let p > 0 denote a positive exponent and let the ni ≤−3 denote negative exponents.
(1a) σp
2σn1
1
(1b) σp
1σn1
2
(2a) σp
2σn1
1 σn2
2 · · · σn2m−1
1
σn2m
2
, where m ≥1
(2b) σp
1σn1
2 σn2
1 · · · σn2m−1
2
σn2m
1
, where m ≥1
(3a) σp
2σn1
1 σn2
2 · · · σn2m−1
1
σn2m
2
σn2m+1
1
, where m ≥1
(3b) σp
1σn1
2 σn2
1 · · · σn2m−1
2
σn2m
1
σn2m+1
2
, where m ≥1
Lemma 3.2. Given the list of induced subwords PiNi above, applying the Schreier Normal Form Algorithm
produces the following corresponding list of braid words.
(1a) σp
2σn1
1
(1b) y2σp−1
2
σn1
1 x
(2a) (C−1)m−1σp
2σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+1
1
x, where m ≥1
(2b) (C−1)my2σp−1
2
σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+1
1
, where m ≥1
(3a) (C−1)mσp
2σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+2
1
σ2σn2m+1+1
1
, where m ≥1
(3b) (C−1)my2σp−1
2
σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+2
1
σ2σn2m+1+1
1
x, where m ≥1
Also, when applying the Schreier Normal Form Algorithm to the subwords PiNi, cyclic permutation is
avoided. Furthermore, letting ki denote the exponent of C in the application of the Schreier Normal Form
Algorithm to the subword PiNi, we have that a local version of Theorem 3.1 holds for the ki.
Proof. Let ∼= denote that the fact that C ∈Z(B3) has been used. Applying the Schreier Normal Form
Algorithm to type (1a), we get
PiNi = σp
2σn1
1
= (xy2)p(xy)−n1 = σp
2σn1
1 .
15
Applying the Schreier Normal Form Algorithm to type (1b), we get
PiNi = σp
1σn1
2
= (y2x)p(yx)−n1 = y2(xy2)p−1(xy)−n1x = y2σp−1
2
σn1
1 x
Applying the Schreier Normal Form Algorithm to type (2a), we get
PiNi
=
σp
2σn1
1 σn2
2 · · · σn2m−1
1
σn2m
2
=
(xy2)p(xy)−n1(yx)−n2 · · · (xy)−n2m−1(yx)−n2m
=
(xy2)p(xy)−n1−1(xy2)(xy)−n2−1(x2)y · · · (x2)y(xy)−n2m−1−2(xy2)(xy)−n2m−1x
=
(xy2)p(xy)−n1−1(xy2)(xy)−n2−1(C−1)y · · · (C−1)y(xy)−n2m−1−2(xy2)(xy)−n2m−1x
∼=
(C−1)m−1(xy2)p(xy)−n1−1(xy2)(xy)−n2−2(xy2) · · ·
· · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−1x
=
(C−1)m−1σp
2σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+1
1
x
Applying the Schreier Normal Form Algorithm to type (2b), we get
PiNi
=
σp
1σn1
2 σn2
1 · · · σn2m−1
2
σn2m
1
=
(y2x)p(yx)−n1(xy)−n2 · · · (yx)−n2m−1(xy)−n2m
=
y2(xy2)p−1(xy)−n1(x2)y(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−1(x2)y(xy)−n2m−1
=
y2(xy2)p−1(xy)−n1(C−1)y(xy)−n2−2(xy2) · · · (xy2)(xy)−n2m−1−1(C−1)y(xy)−n2m−1
∼=
(C−1)my2(xy2)p−1(xy)−n1−1(xy2)(xy)−n2−2(xy2) · · ·
· · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−1
=
(C−1)my2σp−1
2
σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+1
1
Applying the Schreier Normal Form Algorithm to type (3a), we get
PiNi
=
σp
2σn1
1 σn2
2 · · · σn2m−1
1
σn2m
2
σn2m+1
1
=
(xy2)p(xy)−n1(yx)−n2 · · · (xy)−n2m−1(yx)−n2m(xy)−n2m+1
=
(xy2)p(xy)−n1−1(xy2)(xy)−n2−1(x2)y · · ·
· · · (x2)y(xy)−n2m−1−2(xy2)(xy)−n2m−1(x2)y(xy)−n2m+1−1
=
(xy2)p(xy)−n1−1(xy2)(xy)−n2−1(C−1)y · · ·
· · · (C−1)y(xy)−n2m−1−2(xy2)(xy)−n2m−1(C−1)y(xy)−n2m+1−1
∼=
(C−1)m(xy2)p(xy)−n1−1(xy2)(xy)−n2−2(xy2) · · ·
· · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−2(xy2)(xy)−n2m+1−1
=
(C−1)mσp
2σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+2
1
σ2σn2m+1+1
1
Applying the Schreier Normal Form Algorithm to type (3b), we get
PiNi
=
σp
1σn1
2 σn2
1 · · · σn2m−1
2
σn2m
1
σn2m+1
2
=
(y2x)p(yx)−n1(xy)−n2 · · · (yx)−n2m−1(xy)−n2m(yx)−n2m+1
=
y2(xy2)p−1(xy)−n1(x2)y(xy)−n2−2(xy2) · · ·
· · · (xy2)(xy)−n2m−1−1(x2)y(xy)−n2m−2(xy2)(xy)−n2m+1−1x
=
y2(xy2)p−1(xy)−n1(C−1)y(xy)−n2−2(xy2) · · ·
· · · (xy2)(xy)−n2m−1−1(C−1)y(xy)−n2m−2(xy2)(xy)−n2m+1−1x
∼=
(C−1)my2(xy2)p−1(xy)−n1−1(xy2)(xy)−n2−2(xy2) · · ·
· · · (xy2)(xy)−n2m−1−2(xy2)(xy)−n2m−2(xy2)(xy)−n2m+1−1x
=
(C−1)my2σp−1
2
σn1+1
1
σ2σn2+2
1
σ2 · · · σ2σn2m−1+2
1
σ2σn2m+2
1
σ2σn2m+1+1
1
x
16
By inspecting the cases above, it can be seen that cyclic permutation is never used. Let ki denote the
exponent of C in the application of the Schreier Normal Form Algorithm to the subword PiNi. In each case
above, it can be see that
ki = −#

induced products σnj,i
2
σnj+1,i
1
of negative syllables of PiNi, where nj,i, nj+1,i ≤−3
	
,
which is a local version of conclusion (1) from Theorem 3.1.
The fact that cyclic permutation is never used in applying the Schreier Normal Form Algorithm to the
subwords PiNi is very important because the goal is to juxtapose the resulting braid words from Lemma 3.2
and claim that this gives, after some minor modiﬁcations, the normal form of the full braid word β. We are
now ready to combine the above results to prove Theorem 3.1 for the case that β ∈B3 is not a negative
braid. The following lemma establishes that β is generic and establishes the result for the parameter k from
the Schreier normal form (conclusion (1) from Theorem 3.1).
Lemma 3.3. Let D(K) = bβ, where β ∈B3 is a nonnegative braid that satisﬁes the assumptions of
Lemma 2.1. Then β is generic and the parameter k from the Schreier normal form β′ can be expressed
in terms of the original 3-braid β as
k = −# {induced products σn2
2 σn1
1
of negative syllables of β, where n1, n2 ≤−3} .
Proof. By Lemma 2.1, we have that K is hyperbolic. By Proposition 3.1, this implies that β is generic. Let
us now consider which types of induced subwords Pi+1Ni+1 can (cyclically) follow a given induced subword
PiNi. Since β is assumed to be cyclically reduced into syllables and since the the induced subwords PiNi
contain unbroken syllables of β, then (looking at the list of induced subwords PiNi preceding Lemma 3.2)
we get that
• the subwords PiNi of type (1) and type (3) with subtype either (a) or (b) can be followed by subwords
Pi+1Ni+1 of the same subtype (a) or (b), respectively.
• the subwords PiNi of type (2) with subtype either (a) or (b) can be followed by subwords Pi+1Ni+1 of
diﬀerent subtype (b) or (a), respectively.
It is important to note that the rules for juxtaposition given above also apply after the Schreier Normal
Form Algorithm is applied to the list of induced subwords PiNi preceding Lemma 3.2. Abusing terminology
slightly, call the braids words in the list given in Lemma 3.2 the normal forms of the PiNi.
Let ki denote the exponent of C in the normal form of PiNi. Recall that C ∈Z(B3) commutes with the
generators of B3. Thus, when juxtaposing the normal form of PiNi with the normal form of Pi+1Ni+1, we
may move the factor Cki+1 out of the way, moving it from the beginning of the normal form of Pi+1Ni+1 to
the beginning of the normal form of PiNi. This fact will be utilized below.
Looking at the list of braids words given in Lemma 3.2, notice that half of the braid words may potentially
contain the variable x at the end of the word and half of the braid words may contain the expression y2σp−1
2
at the beginning of the word (immediately after the Cki+1 term that will be moved out of the way). We can
now see that juxtaposing the normal form of PiNi with that of Pi+1Ni+1 either
(1) involves neither x at the end of the normal form of PiNi nor y2σp−1
2
at the beginning of the normal
form of Pi+1Ni+1, or
(2) involves (after moving Cki+1 out of the way) both an x at the end of the normal form of PiNi and
y2σp−1
2
at the beginning of the normal form of Pi+1Ni+1.
Consequently, upon juxtaposing the normal forms of all of the induced subwords together, we see that all
factors x and y2σp−1
2
in the list of normal forms combine to form
xy2σp−1
2
= σ2σp−1
2
= σp
2.
17
Note, in particular, that juxtaposing the normal form of PiNi with that of Pi+1Ni+1 does not create any new
nontrivial powers of C. Therefore, since C commutes with the generators of B3, then we may group all Cki
terms together at the beginning of the normal form braid word. Furthermore, by applying the conclusions
of Lemma 3.2, we have that
ki = −#

induced products σnj,i
2
σnj+1,i
1
of negative syllables of PiNi, where nj,i, nj+1,i ≤−3
	
.
We also have that juxtaposing PiNi with Pi+1Ni+1 does not create any new induced products σnj
2 σnj+1
1
of
negative syllables. This is because juxtaposing PiNi with Pi+1Ni+1 only joins a negative syllable with a
positive syllable. With this information, we are now able to conclude that
k
=
t
X
i=1
ki
=
t
X
i=1
−#

induced products σnj,i
2
σnj+1,i
1
of negative syllables of PiNi, where nj,i, nj+1,i ≤−3
	
=
−#

induced products σnj
2 σnj+1
1
of negative syllables of β, where nj, nj+1 ≤−3
	
.
The following lemma proves conclusion (2) from Theorem 3.1, the result concerning the parameter s from
the Schreier normal form, for the case that β ∈B3 is not a negative braid.
Lemma 3.4. Let D(K) = bβ, where β ∈B3 is a nonnegative braid that satisﬁes the assumptions of
Lemma 2.1.
Then the parameter s from the Schreier normal form β′ can be expressed in terms of the
original 3-braid β as
s = t−(D) = # {negative syllables in β} .
Proof. We need to relate the global parameter s from the Schreier normal form to local versions of the
parameter s. Let si denote the local version of the parameter s, which comes from the normal form of the
subword PiNi and will be more precisely deﬁned below.
As seen in the proof of Lemma 3.3 above, juxtaposing the normal forms of the subwords PiNi to create a
braid word groups together the x and y2 factors in the normal forms in such a way that they are absorbed
into σp−1
2
to form σp
2. Also recall that we can collect together all individual powers of C from each PiNi
normal form and use commutativity to form a single power of C at the beginning of the normal form braid
word. Thus, after juxtaposition of the normal forms of the PiNi, what results is a braid word that looks like
CkW1 · · · Wt, where k ∈Z and Wi is an alternating word that is positive in σ2, negative in σ1, begins with a
σ2 syllable, and ends with a σ1 syllable. To see this, recall the list of PiNi normal forms given in Lemma 3.2.
Given an alternating subword Wi = σp1,i
2
σn1,i
1
· · · σpq,i
2
σnq,i
1
as described above, we deﬁne si = q. To
provide an example, for the normal form C−1σp
2σn1+1
1
σ2σn2+2
1
σ2σn3+2
1
σ2σn4+1
1
x of Type (2a), we have that
si = 4. Consider the product
WiWi+1 = (σp1,i
2
[σn1,i
1
· · · σpq,i
2
σnq,i
1
) · (σp1,i+1
2
]σn1,i+1
1
· · · σpr,i+1
2
σnr,i+1
1
).
Note that the subword [σn1,i
1
· · · σpq,i
2
σnq,i
1
·σp1,i+1
2
] looks like the alternating part of a generic braid word, the
part of the normal form for which the parameter s measures the length. From this perspective of (cyclically)
borrowing the ﬁrst syllable of the next subword, the local parameter si makes sense as being the local version
of the global parameter s.
Recall that, since β is cyclically reduced into syllables, then the number of negative twist regions in
D(K) = bβ corresponds to the number of negative syllables in β. Also, note that the decomposition of β
into induced subwords PiNi (with unbroken syllables) gives that the number of negative syllables in β is the
sum of the numbers of negative syllables in the PiNi. Furthermore, returning to Lemma 3.2 and its proof,
it can be seen that the number of negative syllables in the subword PiNi is equal to the local parameter si
18
from the normal form of PiNi. Finally, since juxtaposing the normal forms of the PiNi gives a braid word
CkW1 · · · Wt that (by cyclic permutation and the commutativity of C) is equivalent to the generic normal
form of β, then the parameters si from the Wi sum to give the parameter s from the Schreier normal form
of β. With this information, we are now able to conclude that
t−(D)
=
# {negative syllables in β}
=
t
X
i=1
# {negative syllables in PiNi}
=
t
X
i=1
si
=
s.
References
[1] Ian Agol, Peter A. Storm, and William P. Thurston. Lower bounds on volumes of hyperbolic Haken
3-manifolds. J. Amer. Math. Soc., 20(4):1053–1077, 2007. With an appendix by Nathan Dunﬁeld.
[2] Oliver T. Dasbach and Xiao-Song Lin.
On the head and the tail of the colored Jones polynomial.
Compos. Math., 142(5):1332–1342, 2006.
[3] Oliver T. Dasbach and Xiao-Song Lin. A volumish theorem for the Jones polynomial of alternating
knots. Paciﬁc J. Math., 231(2):279–291, 2007.
[4] Oliver T. Dasbach and Anastasiia Tsvietkova. A reﬁned upper bound for the hyperbolic volume of
alternating links and the colored jones polynomial.
To appear in Mathematical Research Letters.
ArXiv:1310.0788v5.
[5] Kathleen Finlinson and Jessica S. Purcell. Volumes of montesinos links. ArXiv:1502.07991v1.
[6] David
Futer,
Efstratia
Kalfagianni,
and
Jessica
Purcell.
Hyperbolic
semi-adequate
links.
Arxiv:1311.3008v1.
[7] David Futer, Efstratia Kalfagianni, and Jessica Purcell. Jones polynomials, volume, and essential knot
surfaces: a survey. Proceedings of Knots in Poland III, Banach Center Publications, 100 (2014), 51-77.
ArXiv:1110.6388v2.
[8] David Futer, Efstratia Kalfagianni, and Jessica Purcell. Guts of surfaces and the colored Jones polyno-
mial, volume 2069 of Lecture Notes in Mathematics. Springer, Heidelberg, 2013.
[9] David Futer, Efstratia Kalfagianni, and Jessica S. Purcell. Dehn ﬁlling, volume, and the Jones polyno-
mial. J. Diﬀerential Geom., 78(3):429–464, 2008.
[10] David Futer, Efstratia Kalfagianni, and Jessica S. Purcell. Symmetric links and Conway sums: volume
and Jones polynomial. Math. Res. Lett., 16(2):233–253, 2009.
[11] David Futer, Efstratia Kalfagianni, and Jessica S. Purcell. Cusp areas of Farey manifolds and applica-
tions to knot theory. Int. Math. Res. Not. IMRN, 2010(23):4434–4497, 2010.
[12] Adam Giambrone.
Combinatorics of link diagrams and volume.
Journal of Knot Theory and Its
Ramiﬁcations, 24(01):1550001, 2015.
19
[13] Marc Lackenby. The volume of hyperbolic alternating link complements. Proc. London Math. Soc. (3),
88(1):204–224, 2004. With an appendix by Ian Agol and Dylan Thurston.
[14] Adam Lowrance. The khovanov width of twisted links and closed 3-braids. Math. Helv., 86(3):675–706,
2011.
[15] Otto Schreier. ¨Uber die gruppen AaBb = 1. Abh. Math. Sem. Univ. Hamburg, 3(1):167–169, 1924.
[16] Alexander Stoimenow. Coeﬃcients and non-triviality of the Jones polynomial. J. Reine Angew. Math.,
657:1–55, 2011.
20
