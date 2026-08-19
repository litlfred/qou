---
doc_id: arxiv-2002.07369v2
doc_title: "GR¨OBNER-SHIRSHOV BASES FOR THE COXETER GROUPS OF THE TYPESG 2,F 4,E 6,E 7 ANDE 8"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2002.07369v2.pdf
source_sha256: 6b8b1e509553b90c
doc_brief: "GRÖBNER-SHIRSHOV BASES FOR THE COXETER GROUPS OF THE TYPESG 2,F 4,E 6,E 7 ANDE 8 — It is known that the finite Coxeter groups are classified in terms of Coxeter-Dynkin diagrams."
---
LetM= (m ij) be a symmetricn×nmatrix over natural numbers, with∞
such thatm ii = 1,2≤m ij≤∞fori̸=j. The matrixMdetermines a group with
the following presentation
W= sgp⟨s 1,..,s n|(sisj)mij = 1,where 1≤i,j≤n,m ij̸=∞⟩,
which is called the Coxeter groupW=W(M).
The study of Coxeter groups can be said to go back to Greek antiquity, the
symmetries and classification of regular polytopes being part of the theory. In
1935, Coxeter classified the finitie Coxeter groups in terms of Coxeter-Dynkin dia-
grams [12]. When computing in a Coxeter group, whether by hand or by machine,
one faces the problem about how to efficiently represent its elements. For this
purpose, we focus on the noncommutative Gr¨ obner bases theory, which is called
2020Mathematics Subject Classification.20F55, 16S15.
Key words and phrases.Gr¨ obner-Shirshov basis; Shirshov algorithm; Coxeter group.
∗ Supported by Science Foundation of Hebei Normal University No. L2022B30, Natural Science
Fundation of Hebei Province (A2023205045), China Scholarship Council No.202308130193.
∗∗ Supported by Science and Technology Project of Hebei Education Department No.
QN2023030, Science Foundation of Hebei Normal University No. L2022B02, China Scholarship
Council No.202308130195, Natural Science Fundation of Hebei Province (A2023205045).
1
arXiv:2002.07369v2  [math.GR]  15 Mar 2026
2 XIAOWEI PANG AND JUN W ANG
the Gr¨ obner-Shirshov bases theory. The effecitve notion stems from Shirshov’s
composition Lemma and his algorithm [15,16] for Lie algebras, and independently
from Bchberger’s algorithm [10] of computing Gr¨ obner bases for commutative al-
gebras. The Gr¨ obner-Shirshov bases for some Lie algebras and superalgebras were
determined in [1–7]. In 2006, Bokut and Vesnin [9] applied Shirshov’s method to
some braid groups. Bokut considered the Coxeter groups of the typesA n,Bn,Dn
in 2001 [8] and formulated a general hypothesis about Gr¨ obner-Shirshov bases of
any Coxter group. In 2008, Lee Denis [13] got the Gr¨ obner-Shirshov bases for the
Coxeter groups of typesE 6 andE 7. In 2009, Yuqun Chen and Cihua Liu [11]
gave an counter-example for the general hypothesis by Bokut in [8]. For non-
crystallographic Coxeter groups, Jeong-Yup Lee and Dong-IL Lee [14] calculated
the Gr¨ obner-Shirshov bases in 2018. Thus the last piece of the Gr¨ obner-Shirshov
bases for finite Coxeter group is the type ofE 8, which is more complicated than
others.
In this paper, we rearrange the generators of Coxeter groups to reduce calcu-
lating amount, get a new presentation of Gr¨ obner-Shirshov bases of the Coxeter
groups of typesE 6,E 7 and the Gr¨ obner-Shirshov bases of the Coxeter groups of
typesE 8. Thus the calculations of Gr¨ obner-Shirshov basis of Coxeter groups are
beginning at 2001 by Bokut L.A. [8], up to now, Gr¨ obner-Shirshov bases of all
irreducible finite Coxeter group are solved.
The article is organized as follows. In Section 2, we introduce the Gr¨ obner-
Shirshov bases theory. The Gr¨ obner-Shirshov bases for Coxeter groups of type
G2,F 4,E 6,E 7,E 8 will be set out in Section 3 and Appendix A.
