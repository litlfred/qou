---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-026-relations-for-correlators
section_title: "Relations for correlators"
section_number: null
pages: 87-89
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
toc_source: outline
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
Relations for correlators
Recall from §1.1.1 that the Hodge correlators satisfy a ﬁrst shuﬄe relation, and that in Chapter 2 we describe
a family of second shuﬄe relations for correlators on P1, the terms of which were formed by permuting
quotients of successive arguments. One of the main results of this chapter is that the Hodge correlators on an
elliptic curve satisfy second shuﬄe relations in depth 2.
0
푎
푎+ 푏
푆푛1,푛′
1
푆푛2,푛′
2
푆푛0,푛′
0
+
0
푏
푎+ 푏
푆푛2,푛′
2
푆푛1,푛′
1
푆푛0,푛′
0
Figure 3.2. The highest-depth terms of the second shuﬄe relation on an elliptic curve.
For Hodge correlators of depth 2 on an elliptic curve with arbitrary base point, this new relation has the
form:
CorH(푆푛0,푛′
0, 0, 푆푛1,푛′
1, 푎, 푆푛2,푛′
2, 푎+푏)+CorH(푆푛0,푛′
0, 0, 푆푛2,푛′
2, 푏, 푆푛1,푛′
1, 푎+푏)+lower-depth terms = 0, (3.5)
where an argument 푆푛,푛′ indicates that we sum over all possible ways to insert in some order the arguments
휔, . . . , 휔
|    {z    }
푛
, 휔, . . . , 휔
|    {z    }
푛′
.
The highest-depth terms in these relations arise from shuﬄes of the diﬀerences between successive arguments,
푥푖−푥푖−1, together with the 1-forms between those arguments. For example, in (3.5) we have shuﬄed 푎(with
푛1 copies of 휔and 푛′
1 of 휔) with 푏(with 푛2 휔’s and 푛′
2 휔’s). See Figure 3.2) for an illustration.
We describe the lower-depth correction terms in §3.2.2. In the simplest case – weight 4 – the full relation
is:
CorH(0, 푎, 푎+ 푏) + CorH(0, 푏, 푎+ 푏) −(CorH(0, 휔, 휔, 푎+ 푏) + CorH(0, 휔, 휔, 푎+ 푏))
−1
2

CorH(0, 푎, 휔, 휔) −CorH(0, 푎, 휔, 휔)
+ CorH(0, 푏, 휔, 휔) −CorH(0, 푏, 휔, 휔)
+ CorH(휔, 휔, 푎, 푎+ 푏) −CorH(휔, 휔, 푎, 푎+ 푏)
+ CorH(휔, 휔, 푏, 푎+ 푏) −CorH(휔, 휔, 푏, 푎+ 푏)

= 0.
The relation (3.5) can be formulated simply as a functional equation on biperiodic functions of three complex
variables. It states that a sum of several integrals over an elliptic curve is equal to 0, modulo correlators of
depth 1 (which are expressed by Kronecker-Eisenstein series). However, this functional equation is diﬃcult
to prove. To understand it, we will need to upgrade it to the Hodge-theoretic or motivic setting.
The second shuﬄe relations have a prehistory. The ﬁrst objects known to satisfy a system of ﬁrst and
second shuﬄe relations of this form were the multiple polylogarithms (see §1.2.3 and [G3]): these relations
follow from two alternative expressions for multiple polylogarithms: as power series and as iterated integrals.
In Chapter 2, for 푋= P1, we found second shuﬄe relations for Hodge correlators, in every depth, and
described the lower-depth terms. In depth 2, these relations depend on integers 푛0, 푛1, 푛2 ≥0 and points
푎, 푏∈G푚\ {1}. They state:
CorH(0, . . . , 0
|   {z   }
푛0
, 1, 0, . . . , 0
|   {z   }
푛1
, 푎, 0, . . . , 0
|   {z   }
푛2
, 푎푏) + CorH(0, . . . , 0
|   {z   }
푛0
, 1, 0, . . . , 0
|   {z   }
푛2
, 푏, 0, . . . , 0
|   {z   }
푛1
, 푎푏)
+ lower-depth terms = 0.
(3.6)
The highest-depth terms in these relations arise from shuﬄes of the quotients between successive arguments,
푥푖
푥푖−1 , together with the 0s between those arguments. For example, in (3.6) we have shuﬄed 푎(with 푛1 0s) with
푏(with 푛2 0s).
Conjecturally, the ﬁrst and second shuﬄe relations give all linear relations among the Hodge correlators on
P1. While the ﬁrst shuﬄe relations emerge from the trivalent tree construction – they hold on the level of the
integrands in (1.4) – the proof of the second shuﬄe relations is diﬃcult, requiring motivic or Hodge-theoretic
arguments even in depth 2.
Note the similarity between (3.6) and (3.5). In fact, as an elliptic curve degenerates to a nodal projective
line, a variant of the second shuﬄe relation (3.5) specializes to (3.6).
In §3.2.3 (Theorem 3.8) we will prove these relations, as well as their upgrades to the Hodge correlator
coalgebra. Assuming the motivic formalism, all results of this chapter should hold in the ℓ-adic realization as
well.
