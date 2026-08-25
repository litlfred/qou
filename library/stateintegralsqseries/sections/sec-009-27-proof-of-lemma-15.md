---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-009-27-proof-of-lemma-15
section_title: "Proof of Lemma 1.5"
section_number: 2.7
pages: 13-14
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
~FA,B.
Part (b) follows from an application of Zeilberger’s creative telescoping [Zei91]. To apply
the method, deﬁne
t(m,x ) = (−1)AmqAm(m+1)
2
(q)B
m
xm
Then, observe that t satisﬁes the recursions with respect to m and x:
(1−qm+1)Bt(m + 1,x ) = (−1)AqA(m+1)t(m,x ) t(m,qx ) =qmt(m,x ).
Now, we eliminateqm from the above equations as follows. The second equation implies that
t(m + 1,qjx) =qj(m+1)t(m + 1,x ). Expanding the ﬁrst equation, it follows that
B∑
j=0
(−1)j
(B
j
)
t(m + 1,qjx) = (−1)AqAxt(m,qAx)
Summing for m≥ 0 implies (b). □
Proof. (of Corollary 1.6) The admissibility ofF in the sense of Kontsevich-Soibelman, follows
from [KS11, Sec.6.1] and [KS11, Thm.9]. Given this, the Nahm Equation (12) for ω follows
easily from part (b) of Lemma 1.5. □
14 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
