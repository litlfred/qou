---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-074-101-dg-algebras
section_title: "Dg algebras"
section_number: 10.1
pages: 71-72
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.942
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:dg algebras label="sub:dg algebras"}

A vector space $V$ will be called dg (short for "differential graded\") if it comes endowed with a grading: $$V = \bigoplus_{n\in \mathbb{Z}} V^i$$ and a differential $d : V^\bullet \rightarrow V^{\bullet+1}$ such that $d^2=0$. A vector $v \in V$ is called homogeneous if $v\in V^i$ for some integer $i$. If this is the case, then we will write $\deg v = i$.

::: definition
[]{#def:dg algebra label="def:dg algebra"}

A **dg algebra** $A^\bullet$ is a dg vector space concentrated in non-positive degrees ($A^n=0$ for $n>0$), which is endowed with a multiplication that preserves the grading: $$A^i \cdot A^j \subset A^{i+j} \qquad \forall \ i,j \in \mathbb{N}_0$$ and the differential via the graded Leibniz rule: $$\label{eqn:leibniz}
d(a \cdot a') = (d a) \cdot a' + (-1)^{\deg a} a \cdot (da') \qquad \forall \ a,a'\in A$$ We impose the usual axioms on the dg algebra $A^\bullet$, such as associativity and unit $1 \in A^0$.
:::

All the dg algebras in this paper will be commutative, in the sense that: $$\label{eqn:dg commutative}
a \cdot a' = (-1)^{(\deg a)(\deg a')} a' \cdot a \qquad \forall \ a,a'\in A^\bullet$$ We will write $H^0(A)$ for the 0--th cohomology of $A^\bullet$, which is a usual commutative algebra. All the dg algebras studied in this paper will be finitely generated over $H^0(A)$.

::: definition
[]{#def:dg module label="def:dg module"}

A **dg module** $M^\bullet$ for a dg algebra $A^\bullet$ is a dg vector space $M^\bullet$ with a map: $$A^\bullet \otimes M^\bullet \longrightarrow M^\bullet$$ which is associative, preserves the grading, and satisfies the graded Leibniz rule (i.e. [\[eqn:leibniz\]](#eqn:leibniz){reference-type="eqref" reference="eqn:leibniz"} with $a'$ replaced by $m$). Note that all the cohomologies $H^i(M^\bullet)$ are modules for $H^0(A^\bullet)$.
:::

When the grading will not be particularly crucial, we may simplify notation by writing $A = A^\bullet$ and $M = M^\bullet$. We will only studied the derived category $A$--modules: $$A\text{--Mod} = \Big\{\text{dg modules }M \curvearrowleft A \Big\}/\text{quasi--isomorphism}$$ When the dg algebra $A$ is finitely generated over $H^0(A)$, we will call an object of $A\text{--Mod}$ **finitely presented** if all its cohomologies have this property over $H^0(A)$. Then we write: $$A\text{--mod} \subset A\text{--Mod}$$ for the full subcategory of finitely presented modules. The category of dg modules behaves much like that of usual modules, but with certain particular features. First of all is the existence of the grading shift: $$M^\bullet[1] = M^{\bullet+1}$$ Given two $A$--modules $M$ and $M'$, one can define the space of degree preserving homomorphisms between them as $\mathop{\mathrm{Hom}}_A(M,M')$. But it is more naturally to consider instead: $$\label{eqn:hom dg}
\mathop{\mathrm{Hom}}^\bullet_A(M,M') = \bigoplus_{n\in \mathbb{Z}} \mathop{\mathrm{Hom}}_A(M,M'[n])$$ which is actually a dg vector space with respect to: $$d(f) = d \circ f - (-1)^n f \circ d \qquad \forall \ f:M \rightarrow M'[n]$$ The spaces [\[eqn:hom dg\]](#eqn:hom dg){reference-type="eqref" reference="eqn:hom dg"} make $A$--Mod and $A$--mod into **dg categories**, which just means a category whose Hom spaces are dg vector spaces. We may inquire about the ordinary categories: $$\label{eqn:homotopy category}
H^0(A\text{--Mod}) \qquad \text{and} \qquad H^0(A\text{--mod})$$ whose Hom spaces are, by definition, the 0--th cohomologies of [\[eqn:hom dg\]](#eqn:hom dg){reference-type="eqref" reference="eqn:hom dg"}. Because the zero--cycles of [\[eqn:hom dg\]](#eqn:hom dg){reference-type="eqref" reference="eqn:hom dg"} are degree and differential preserving maps $f:M \rightarrow M'$, while the zero--boundaries are homotopies between such maps, we conclude that [\[eqn:homotopy category\]](#eqn:homotopy category){reference-type="eqref" reference="eqn:homotopy category"} is nothing but the homotopy category of $A$--modules. So the dg category $A$--mod supersedes the homotopy category.
