---
doc_id: arxiv-math-0410111v2
doc_title: "Integer Polynomial Optimization in Fixed Dimension"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0410111v2.pdf
source_sha256: 0ccaeeabd8de6b5f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.974
doc_brief: "Integer Polynomial Optimization in Fixed Dimension — 5 sections: Front matter; Introduction; Computational Complexity Bounds"
---
Mixed integer non-linear programs combine the hardness of combinatorial explosion with the non-convexity of non-linear functions. For example, the well-known optimality conditions developed for differentiable objective functions have no meaning when the variables are discrete. Thus, it is perhaps not surprising that already linear integer programming with general quadratic constraints is undecidable [@jeroslow]. Nevertheless, when the number of variables is fixed discrete optimization problems often become tractable and efficient polynomial algorithms exist (e.g. [@bar; @khachiyanporkolab; @lenstra]). It is thus natural to ask *what is the complexity of integer non-linear optimization assuming that the number of variables is fixed?* We study the problem $$\label{model} \hbox{maximize} \  f(x_1,\dots,x_d) \
  \hbox{subject to} \ g_i(x_1,\dots,x_d) \geq 0, \ x \in  \mathbb Z^d.$$ Here $f,g_i$ are polynomials with integral coefficients. Note that all throughout the paper we assume that the number of variables is fixed. Here are our two contributions to the theory:

*(1)* We give a classification of the computational complexity of Problem ([\[model\]](#model){reference-type="ref" reference="model"}) according to special cases. Section [\[bounds\]](#bounds){reference-type="ref" reference="bounds"} of this article presents the details, but the reader can see the classification in Table [1](#gogo){reference-type="ref" reference="gogo"}. New results are marked with letters, known results are marked with asterisks, arrows indicate implications:

::: center
::: {#gogo}
                                                         Type of objective function                                                    
  ----------------------------------------------------- ---------------------------- --------------- ----------------- --------------- -----------------
                           2-6                                                                            convex                           arbitrary
                   Type of constraints                             linear                               polynomial                        polynomial
          Linear constraints, integer variables                polytime ($*$)         $\Leftarrow$    polytime ($**$)                     NP-hard (a)
                                                                 $\Uparrow$                             $\Uparrow$                       $\Downarrow$
   Convex semialgebraic constraints, integer variables        polytime ($**$)         $\Leftarrow$    polytime ($**$)                     NP-hard (c)
                                                                                                                                       
   Arbitrary polynomial constraints, integer variables        undecidable (b)         $\Rightarrow$   undecidable (d)   $\Rightarrow$   undecidable (e)

  : Computational complexity of problem ([\[model\]](#model){reference-type="ref" reference="model"}) in fixed dimension.
:::
:::

For problem $(a)$, that of optimizing an arbitrary integral polynomial over the lattice points of a convex rational polytope with fixed number of variables, we present an algorithm to compute a sequence of upper and lower bounds for its optimal value. Our bounds can be used, for instance, in a branch-and-bound search for the optimum. We use Barvinok's algebraic encoding of the lattice points of polytopes via rational functions [@BarviPom]. In Section [\[algo\]](#algo){reference-type="ref" reference="algo"} we prove:

::: theorem
[]{#main label="main"} Let the number of variables $d$ be fixed. Let $f(x_1,\dots,x_d)$ be a polynomial of maximum total degree $D$ with integer coefficients, and let $P$ be a convex rational polytope defined by linear inequalities in $d$ variables. We obtain an increasing sequence of lower bounds $\{L_k\}$ and a decreasing sequence of upper bounds $\{U_k\}$ to the optimal value $$f^*=\hbox{maximize} \  f(x_1,x_2,\dots,x_d) \ \hbox{subject to} \ x
    \in P \cap \mathbb Z^d.\label{eq:maximize}$$ The bounds $L_k$, $U_k$ can be computed in time polynomial in $k$, the input size of $P$ and $f$, and the maximum total degree $D$ and they satisfy the inequality $U_k-L_k \leq f^* \cdot (\sqrt[k]{|P
    \cap \mathbb Z^d|}-1).$

More strongly, if $f$ is non-negative over the polytope (i.e. $f(x)\geq 0$ for all $x \in P$), there exists a fully polynomial-time approximation scheme (FPTAS) for the optimization problem [\[eq:maximize\]](#eq:maximize){reference-type="eqref" reference="eq:maximize"}.
:::

We conclude with examples and a brief look at the mixed integer problem.
