---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-002-12-quantum-volume-conjecture
section_title: "Quantum volume conjecture"
section_number: 1.2
pages: 4-4
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.956
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
Classical solutions in Chern-Simons theory (*i.e.* flat connections on $M$) are labeled by the holonomy eigenvalue $x = e^u$ or, to be more precise, by a point on the algebraic curve $${\cal C }: \quad \left\{(x,y)\in\mathbb{C}^*\times \mathbb{C}^*\Big|
A(x,y) \; = \; 0 \right\}\,,
\label{Acurve}$$ defined by the zero locus of the $A$-polynomial, a certain classical invariant of a knot. In quantum theory, $A(x,y)$ becomes an operator $\widehat A (\widehat x, \widehat y; q)$ and the classical condition [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"} turns into a statement that the Chern-Simons partition function is annihilated by $\widehat A (\widehat x, \widehat y; q)$. This statement applies equally well to Chern-Simons theory with the compact gauge group $SU(2)$ that computes the colored Jones polynomial $J_n (K;q)$ as well as to its analytic continuation that localizes on $SL(2,{\mathbb C})$ flat connections. In the former case, one arrives at the "quantum version" of the volume conjecture [@Apol]: $$\widehat A \; J_* (K;q) \; \simeq \; 0 \,,
\label{VCquant}$$ which in the mathematical literature was independently proposed around the same time [@Garoufalidis] and is know as the AJ-conjecture. The action of the operators $\widehat x$ and $\widehat y$ follows from quantization of Chern-Simons theory. With the standard choice of polarization[^1] one finds that $\widehat x$ acts as a multiplication by $q^n$, whereas $\widehat y$ shifts the value of $n$: $$\begin{aligned}
& \widehat x J_n \; = \; q^n J_n \label{xyactionJ} \\
& \widehat y J_n \; = \; J_{n+1} \notag
\end{aligned}$$ In particular, one can easily verify that these operations obey the commutation relation $$\widehat y \widehat x \; = \; q \widehat x \widehat y
\label{xycomm}$$ that follows from the symplectic structure on the phase space of Chern-Simons theory. Therefore, upon quantization a classical polynomial relation of the form [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"} becomes a $q$-difference equation for the colored Jones polynomial or Chern-Simons partition function. Further details, generalizations, and references can be found in [@DGreview].\
One of the goals of the present paper is to propose a "refinement" or "categorification" of the generalized and quantum volume conjectures [\[VCparam\]](#VCparam){reference-type="eqref" reference="VCparam"} and [\[VCquant\]](#VCquant){reference-type="eqref" reference="VCquant"}.

[^1]: Although different choices of polarization will not play an important role in the present paper, the interested reader may consult *e.g.* [@GMtorsion; @Tudor] for further details.
