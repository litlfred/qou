---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-006-13-statement-of-results
section_title: "Statement of results"
section_number: 1.3
pages: 12-17
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
We are ﬁnally ready to state our main result, the Markov theorem without stabilization.
LetB be the collection of all braid isotopy classes of closed braid representatives
of oriented knot and link types in oriented 3–space. Among these, consider the
subcollectionB(X ) of representatives of a ﬁxed link typeX . Among these, letBmin(X )
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 425
exchange
move
exchange
move andisotopy
braid iso-topy
braid iso-topy
negative
ﬂype to a
7–braid
positive
ﬂype to a
6–braid
G–ﬂype
n = 7
n = 7 n = 7
n = 7 n = 7
n = 6 n = 6
W
X
Y
Z
W
X
Y
Z
W
X
Y
Z
W
X
Y
Z
W
X
Y
Z
W
X
Y
Z
W
X
Y
Z
Figure 9: Example of a G–ﬂype on a 6–braid
Geometry &Topology 10 (2006)
426 Joan S Birman and William W Menasco
G–exchange
A
B
C D
E
F
a
b
c
c
d
A
B
C D
E
F
a
b
c
c
d
d
A
B
C D
E
F
a
b
c
d
A
B
C D
E
F
a
b cd
a
b
c
d
A
B
C D
E
F
a
b
a
b
c
d
A
B
C D
E
F
a
b
c
d
a
b
c
d
Figure 10: Example of a G–exchange move on a 6–braid
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 427
be the subcollection of representatives whose braid index is equal to the braid index of
X .
Theorem 2 (Markov’s Theorem Without Stabilization (MTWS)) Choose any X+∈
B(X ) and any X−∈B min(X ). Then
• there is a complexity function with values in Z+× Z+× Z+ which is associated
to X+, X−, and
• for each braid index m there is a ﬁnite setT (m) of templates, each determining a
move which is non-increasing on braid index,
such that the following hold:
First, there are initial modiﬁcations in the choices of X+ and X−, which replace them
by X′
+ and X′
−:
X− = X1
−→···→ Xp
− = X′
−(1–2)
X+ = X1
+→···→ Xq
+ = X′
+(1–3)
In (1–2) and (1–3) each passage Xj
−→ Xj+1
− and Xj
+→ Xj+1
+ is strictly complexity-
reducing. In (1–2) each passage is realized by an exchange move, so that b(Xj+1
− ) =
b(Xj
−). In (1–3) each passage is realized by either an exchange move or a destabilization,
so that b(Xj
+)≥ b(Xj+1
+ ).
After these initial modiﬁcations, there is another sequence taking X′
+ to X′
−:
(1–4) X′
+ = Xq→···→ Xr = X′
−
In (1–4) each passage Xj→ Xj+1 is strictly complexity-reducing, and is realized by
either an exchange move, a destabilization, an admissible ﬂype or a move deﬁned by
one of the templatesT ∈T (m), where m = b(Xj). The inequality b(Xj)≥ b(Xj+1)
holds for each j = q,..., r− 1.
Remark 1.3.1 We explain why we refer to Theorem 2 asMarkov’s Theorem without
Stabilization. Setting Xj = Xj
+ when j = 1,..., q− 1, we have the combination of
sequences (1–3) and (1–4):
X+ = X1→···→ Xq→···→ Xr = X′
−
In this combined sequence b(Xj)≥ b(Xj+1) for each j = 1,..., q,... r. On the other
hand, b(X−) = b(X1
−) = b(X2
−) =··· = b(Xp
−) = b(X′
−), so that the braid index of the
second representative remains ﬁxed during all of our modiﬁcations. Thus Theorem 2 is,
indeed, a version of Theorem 1 which avoids stabilization. ♦
Geometry &Topology 10 (2006)
428 Joan S Birman and William W Menasco
Remark 1.3.2 The sequence (1–2) deals with the phenomenon which was exhibited in
Figure 6. It must be treated separately because if we only allowed modiﬁcations to X+
then the complexity would be forced to increase asX+ approached X−, if X− happened
to be wound up as on the left in Figure 6. Since (1–2) and (1–3) are inter-related, we
treat (1–3) (which uses a limited subset of the moves in (1–4)) and (1–4) separately.♦
Remark 1.3.3 When a passage Xj→ Xj+1 is realized by a template T , there are
braiding assignments to the blocks inT such that the initial and ﬁnal diagrams ofT
carry the pair (Xj, Xj+1). However, the templateT also carries inﬁnitely many other
knots and links, for other braiding assignments to the blocks. ♦
Remark 1.3.4 The templates in the setsT (m), m∈ Z+, are precisely the additional
moves which were not needed for the work in our earlier papers [8]–[10], but are needed
for our particular proof of the MTWS. We discuss them brieﬂy, starting with m = 2.
(1) The 2–string braid group is an inﬁnite cyclic group. Let σ1 denote its generator.
An arbitrary element is then σk
1, k∈ Z. It is easy to see that links which are
closed 2–braids are either (i) the 2–component unlink (k = 0), or (ii) the unknot
(k =±1) or (iii) the type (2, k) torus knots and links (|k|≥ 2). It is clear that the
2–component unlink and the type (2, k) torus knots and links have unique closed
2–braid representatives. The unknot has exactly 2 closed 2–braid representatives,
withσ1 (resp.σ−1
1 ) admitting a positive (resp. negative) destabilization. Since
the setT (m) does not include the two destabilization templates, it follows that
T (2) =∅. In our paper [ 6], which contains applications of Theorem 2 to
transverse knots, we will prove that, as a consequence of the main theorem in our
paper [11],T (3) =∅.
(2) It was proved by Fiedler [ 18] that closed 4–braids include inﬁnitely many
inequivalent 4–braid representatives of the unknot. His basic one is the example
discovered by Morton [ 27], with the others obtained from it by the winding
process which we illustrated in Figure 6. Fifteen other families of 4–braid unknot
examples were uncovered in the paper by Birman, Boldi, Rampichini and Vigna
[13], in the course of a computer implementation of the unknot recognition
algorithm of Birman and Hirsch [ 5]. All of them can be simpliﬁed to braids
which admit a destabilization with the help of exchange moves. We do not know
whether more general 4–braids are too complicated to be simpliﬁed with the
use of the 2 destabilization templates, the exchange move template, the cyclic
templates and the admissible ﬂype templates.
(3) Note that, given any templateT of braid index m, other templates for braid index
> m may be obtained from it by declaring the strands to be weighted, and also
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 429
by replacing some of the blocks by other templates. From this it follows that the
cardinality|T (m)| ofT (m) is an increasing function of m. However, we do not
have a precise description ofT (m) for any m> 3, although we do not expect
any fundamental difﬁculty in doing the actual enumeration for, say,m = 4, 5 and
perhaps 6. For the special case m = 6 two examples were given in the boxed
pairs of block-strand diagrams at the bottom of Figures 9 and 10. The general
picture seems to be quite complicated. ♦
