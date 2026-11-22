---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-004-iia-diagram-algebras
section_title: "IIA. Diagram Algebras"
section_number: null
pages: 24-29
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
doc_brief: "REPRESENTATIONS OF HECKE — 16 sections: Front matter; INTRODUCTION; ILL Links and Braids"
---
II.4.1.
Temperley-Lieb ATe Diagrams
Definition II.4.10 A (d, d')-arc diagram D is a topological embedding of the disjoint union of
(d+d')/2 intervals in the strip JRx [0,1] such that the boundary of the embedded I-manifold consists
of the points {(I, 0), ... , (d', On u{ (1, 1), ... , (d, 1n. A (d, d)-diagram is called a Temperley-Lieb
diagram on d strands. Let [D] denote the isotopy class of an arc diagram D, keeping its endpoints
fixed.
See Figure 11.4.1 for an illustration of Temperley-Lieb diagrams on three stands.
'--..)
'--..)
(\
(\
Figure II.4: The five Temperley-Lieb diagrams on 3 strands.
There is a natural concatenation operation given by placing one arc diagram above another,
identifying boundary points, and scaling down the result to fit in the strip. However, this process
may produce extra disjoint components, each homeomorphic to a circle. For diagrams D 1 and D 2 ,
let D 1 0 D 2 denote the arc diagram obtained by placing D 1 on top of D 2 followed by removal of
the resulting circles, and let c(D1 , D 2 ) E Z~o denote the number of such circles. We now make an
algebra out of the linear span of isotopy classes of Temperley-Lieb diagrams.
17
Definition 11.4.2. Let T L~ (0) consist of the q v)-vector space on the set of isotopy classes of
Temperley-Lieb diagrams [D] on d strands, endowed with a multiplication defined by
(II.23)
The quantity 0 is called the loop value, which we assume is non-zero.
Lemma 11.4.3.
Up to isotopy, there are Cd distinct arc diagrams on d strands. Hence,
dimTL~(r5) = Cd
(II.24)
PTOOf. There is a bijection between isotopy classes of Temperley-Lieb diagrams on d strands and
isotopy classes of (0,2d)-arc diagrams, as illustrated in (Figure II.5). It is well known that the
latter set has size Cd
Cc.:J
n~
.n ....~
o
Figure 11.5: The correspondence between (d, d)-diagrams and (0,2d)-diagrams.
Let Id denote the TL diagram in which each strand is a vertical segment. It's clear that
[Id] is the unit for T L~(r5).
For each i =
1, ... , d - 1, let UI be the TL diagram with a single
cap-cup pair occurring at positions (i, i + 1) and vertical line segments elsewhere (see Figure II.6).
I I I I
I I
I I
Figure II.6: The generating diagrams 14 and Uf, U&, U~ in TL~(r5).
Lemma 11.4.4. Every TL diagram D on d strands is isotopic to the composition UI! o· .. 0 UI, for
some sequence (i l , ... , ie) of integers with 0< ij < d. Therefore, [D] = lUI!]··' fUr,] E TL~(o).
Proof. The proof is by induction on d and sub-induction on the location of the leftmost cap on
the bottom of the diagram D (see [25, Theorem 5.34]).
o
Theorem 11.4.5.
The map e
TLd(o)
---->
TL~(o) defined on generators by e(Ui )
isomorphism of C(v) -algebras.
18
[Un is an
Proof. Showing that eis well-defined amounts to finding planar isotopies between the two diagrams
corresponding to the relations (11.15)-(11.17). The most interesting relation is illustrated below.
Note that these pictures are meant to represent TL diagrams on d strands, where the remaining
vertical strands are supressed.
(II.25)
By Lemma 11.4.4, every diagram D is isotopic to [UII ] ••• [UI,] = e(Uil ... UiJ for some sequence
(i l , ... , if) of indices. Therefore, eis surjective. Since dim T Ld(O) :s: Cd = dim T L~(o), we conclude
that eis an isomorphism.
Corollary 11.4.6. The set of words in Lemma II. 3.2 forms a basis for TLd(O). Hence,
From now on, we use the isomorphism eto identify T Ld and T L~.
[J
(II.26)
II.4.2.
Eval'Uation of Jones via Temperley-Lieb
Here we set 0 =
[2]
=
'U + V-I.
Let [D] denote the clos'Ure of an element of TL~ by
connecting the ith vertex at the top of the diagram D to the ith vertex at the bottom of D by a
simple curve for each i = 1, ... ,d. The result is a disjoint union of circles, each of which can be
replaced by [2] = v + V-I E C(v), as in the definition of multiplication in TL~. See Figure II.7.
o
Figure 11.7: An example of the closure operation on arc diagrams.
19
Let T : 3 d
----> C(v) denote the composition
(11.27)
Theorem 11.4.7. The function J d : 3 d
----> C(v) defined by
(11.28)
Before proving the theorem, we introduce the following diagrammatic way to calculate ]d.
Resolve each crossing of a braid diagram in a manner representing the map a I-t v- 2e (a) 'ljJ 0 ip(a).
This is suggested by the pictures below, where the remaining vertical strands are suppressed.
x
x
-2
-v
(11.29)
(11.30)
Now, close the corresponding arc diagrams to form a collection of circles, each of which evaluates
to the scalar v + V-I. As an immediate consequence, the trivial braid on d strands representing
1 E 3 d, closes to form d unlinked, unknotted circles, and takes the value ]d(l) = (v + v- 1)d.
Froof of Theorem. \Ve check invariance under the second Markov move. Let a E 3d and let D be
an arc diagram representing a term in the expansion 'ljJ 0 ip(a) E TL~. Calculate the resolution of
the last crossing in the braid acrd E 3 d+1.
t,
, 'I"'"
L. J
- v- 2
D
(11.31)
T"
........
(""'\
Upon closing the strands for both of the diagrams on the right, the first diagram has an extra
disjoint circle. Therefore, we obtain:
(11.32)
20
The calcuation that J d+ l (ewd
l ) = Jd(a) is completely analogous, replacing v by V-I. It remains to
check that J d = (v+V-I)Jd(a). Working in !C(v)Bd, where we may take !C(v)-linear combinations
of braids,
2X
V
""
-2 X
-v
/
(II.33)
Upon closing the resulting arc diagrams, we recover the skein relation for the Jones polynomial
(11.34)
This shows that Jd is a scalar multiple of let, and so we compare the value of each function on the
unknot to complete the proof: Jd(l) = v + V-I = (v + v-I )Jd(l).
D
Perhaps the most important consequence of Theorem II.4.7 is that the Jones polynomial
can be calculated as a state-sum.
This observation, as well as the diagrammatic expansion of
crossings (as in formulas II.29 and 11.30) are due to Kauffman ([26]). By opening parentheses, a
braid diagram with 'IT! crossings yields 2m terms in T Ld. Starting from these states, Khovanov was
able to construct a link homology theory, categorifying the Jones polynomial ([30]).
Fix a braid 0, and an explicit diagram for it with exponent sum e. A state is a diagram
of unlinked circles that results from smoothing each crossing in the closure of the braid. For each
state s, let c = c(s) be the number of circles in the state, and let r = r(s) be the number of
crossings that are smoothed horizontally to form a cap-cup pair in the diagram s. Then,
Theorem 11.4.8 (Kauffman).
(II.35)
21
CHAPTER III
