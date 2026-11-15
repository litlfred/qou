---
doc_id: arxiv-math-0410111v2
doc_title: "Integer Polynomial Optimization in Fixed Dimension"
section_id: sec-001-2-computational-complexity-bounds
section_title: "Computational Complexity Bounds"
section_number: 2
pages: 2-2
source_pdf: 0410111v2.pdf
source_sha256: 0ccaeeabd8de6b5f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "Integer Polynomial Optimization in Fixed Dimension — 5 sections: Front matter; Introduction; Computational Complexity Bounds"
---
[]{#bounds label="bounds"}

All the results we present refer to the complexity model where the number of operations is given in terms of the input size measured in the standard binary encoding. The results of H. W. Lenstra Jr. [@lenstra] imply the entry of Table [\[gogo\]](#gogo){reference-type="ref" reference="gogo"} marked with $(*)$, i.e. solving linear integer programming problems with a fixed number of variables can be done in time polynomial in the size of the input. More recently, Khachiyan and Porkolab [@khachiyanporkolab] have proved that in fixed dimension, the problem of minimizing a convex polynomial objective function over the integers, subject to polynomial constraints that define a convex body, can be solved in polynomial time in the encoding length of the input. Thus, they settled all entries marked by $(**)$. By the natural containment exhibited by these complexity classes, to show the validity of the remaining entries of Table [\[gogo\]](#gogo){reference-type="ref" reference="gogo"} is enough to prove the following lemma:

::: lemma
1.  The problem of minimizing a degree four polynomial over the lattice points of a convex polygon is NP-hard (entry $(a)$ in Table [\[gogo\]](#gogo){reference-type="ref" reference="gogo"}).

2.  The problem of minimizing a linear form over polynomial constraints in at most 10 integer variables is not computable by a recursive function (entry $(b)$ in Table [\[gogo\]](#gogo){reference-type="ref" reference="gogo"}).
:::

::: proof
*Proof.* (1) We use the NP-complete problem AN1 on page 249 of [@GarJohn79]. This problem states it is NP-complete to decide whether, given three positive integers $a,b,c$, there exists a positive integer $x<c$ such that $x^2$ is congruent with $a$ modulo $b$. This problem is clearly equivalent to asking whether the minimum of the quartic polynomial function $(x^2-a-by)^2$ over the lattice points of the rectangle $\{(x,y) | \ 1 \leq x  \leq c-1,\ \frac{1-a}{b} \leq y
\leq \frac{(c-1)^2-a}{b} \}$ is zero or not. This settles part (1).

\(2\) In 1973 Jeroslow [@jeroslow] proved a similar result without fixing the number of variables. We follow his idea, but resorting to a stronger lemma. More precisely our proof relies on a 1982 result [@jones] which states that there is no recursive function that, given an integer polynomial $f$ with *nine* variables, can determine whether $f$ has a non-negative integer zero, in the sense that it finds an explicit zero or returns null otherwise. Jones paper is a strengthening of the original solution of Hilbert's tenth problem [@mati]. Now to each polynomial $f$ in $\mathbb Z[x_1,x_2\dots,x_9]$ associate the ten-dimensional minimization problem $$\hbox{minimize} \ y  \quad  \hbox
{subject to} \quad (1-y)f(x_1,x_2,\dots,x_9)=0, \ (y,x_1,\dots,x_9)
\in \mathbb Z_{\geq 0}^{10}.$$ The minimum attained by $y$ is either zero or one depending on whether $f$ has an integer non-negative solution or not. Thus part (2) is settled. ◻
:::
