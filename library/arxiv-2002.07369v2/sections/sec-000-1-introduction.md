---
doc_id: arxiv-2002.07369v2
doc_title: "GRÖBNER-SHIRSHOV BASES FOR THE COXETER GROUPS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2002.07369v2.pdf
source_sha256: 6b8b1e509553b90c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.818
doc_brief: "GRÖBNER-SHIRSHOV BASES FOR THE COXETER GROUPS — It is known that the finite Coxeter groups are classified in terms of Coxeter-Dynkin diagrams."
---
Let $M=(m_{ij})$ be a symmetric $n\times n$ matrix over natural numbers, with $\infty$ such that $m_{ii}=1,2\leq m_{ij}\leq \infty$ for $i\ne j$. The matrix $M$ determines a group with the following presentation $$W=\mbox{sgp}\langle s_1,..,s_n|(s_is_j)^{m_{ij}}=1, \mbox{ where } 1\leq i,j\leq n, m_{ij}\ne \infty\rangle,$$ which is called the Coxeter group $W=W(M)$.

The study of Coxeter groups can be said to go back to Greek antiquity, the symmetries and classification of regular polytopes being part of the theory. In 1935, Coxeter classified the finitie Coxeter groups in terms of Coxeter-Dynkin diagrams [@coxeter]. When computing in a Coxeter group, whether by hand or by machine, one faces the problem about how to efficiently represent its elements. For this purpose, we focus on the noncommutative Gröbner bases theory, which is called the Gröbner-Shirshov bases theory. The effecitve notion stems from Shirshov's composition Lemma and his algorithm [@MR2547481; @MR0183753] for Lie algebras, and independently from Bchberger's algorithm [@MR2202562] of computing Gröbner bases for commutative algebras. The Gröbner-Shirshov bases for some Lie algebras and superalgebras were determined in [@MR3899218; @MR1800688; @MR2028080; @MR1700511; @MR1414346; @MR1733166; @MR1432728]. In 2006, Bokut and Vesnin [@MR2202556] applied Shirshov's method to some braid groups. Bokut considered the Coxeter groups of the types $A_n,B_n,D_n$ in 2001 [@MR1857281] and formulated a general hypothesis about Gröbner-Shirshov bases of any Coxter group. In 2008, Lee Denis [@MR2440119] got the Gröbner-Shirshov bases for the Coxeter groups of types $E_6$ and $E_7$. In 2009, Yuqun Chen and Cihua Liu [@chen2009grbnershirshov] gave an counter-example for the general hypothesis by Bokut in [@MR1857281]. For non-crystallographic Coxeter groups, Jeong-Yup Lee and Dong-IL Lee [@MR3947551] calculated the Gröbner-Shirshov bases in 2018. Thus the last piece of the Gröbner-Shirshov bases for finite Coxeter group is the type of $E_8$, which is more complicated than others.

In this paper, we rearrange the generators of Coxeter groups to reduce calculating amount, get a new presentation of Gröbner-Shirshov bases of the Coxeter groups of types $E_6,E_7$ and the Gröbner-Shirshov bases of the Coxeter groups of types $E_8$. Thus the calculations of Gröbner-Shirshov basis of Coxeter groups are beginning at 2001 by Bokut L.A. [@MR1857281], up to now, Gröbner-Shirshov bases of all irreducible finite Coxeter group are solved.

The article is organized as follows. In Section [\[pre\]](#pre){reference-type="ref" reference="pre"}, we introduce the Gröbner-Shirshov bases theory. The Gröbner-Shirshov bases for Coxeter groups of type $G_2,F_4,E_6,E_7,E_8$ will be set out in Section [\[e\]](#e){reference-type="ref" reference="e"} and Appendix [\[GF\]](#GF){reference-type="ref" reference="GF"}.
