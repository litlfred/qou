---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-004-3-sufficiency-of-conditions-21-and-22
section_title: "Sufficiency of conditions 2.1 and 2.2"
section_number: 3
pages: 7-9
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.995
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#suff label="suff"}

Somewhat surprisingly, the trivial conditions [\[dihpos\]](#dihpos){reference-type="ref" reference="dihpos"} and [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} guarantees that the linear program $L$ has a solution:

::: theorem
[]{#mainthm label="mainthm"} Let $T$ be a semi-simplicial triangulation of a surface $S$, possibly with boundary, let $\Delta:E(T)\rightarrow (0, \pi]$ be a function on the edges of $T$, $H_d$ a representation $\pi_1 (S \backslash V(T))
\rightarrow \mathbf{R}$. There exists a similarity structure with holonomy $H_d$ on $S$, with the Delaunay triangulation of $(S,
\mathcal{E})$ combinatorially equivalent to $T$, and with dihedral angles given by $\Delta$ if and only if conditions [\[dihpos\]](#dihpos){reference-type="ref" reference="dihpos"} and [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} are satisfied.
:::

We will use the Duality Theorem of linear programming to prove Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"}. Before stating the Duality Theorem we need to recall some notions: A *linear program* $L$ consists of a collection $\mathcal{C}(L)$ of *constraints*, which are linear equations or (nonstrict) inequalities, and the *objective function* $F(L)$, which is a linear function. The set of points in $\mathbf{R}^n$ satisfying the constraints $\mathcal{C}(L)$ is called the *feasible region* of $L$, which is, by definition, a polyhedral region, possibly unbounded, possibly not of full dimension, and possibly empty. The *solution* of the linear program is a point where the objective function attains an extremum (which may be a maximum or a minimum). The value of the objective function at the solution is the *objective* of $L$. If the feasible region of $L$ is empty, the program is said to be infeasible. Now we can state the Duality Theorem:

::: theorem
[]{#duality label="duality"} Let $P$ be a linear program of the form:

Minimize ${\bf c}^\perp {\bf x}$, subject to the constraints ${\bf A} {\bf x} = {\bf a}$, ${\bf x} \geq 0$.

Then the dual of $P$ is the program $P^*$:

Maximize ${\bf a}^\perp {\bf \lambda}$, subject to the constraints ${\bf \lambda}^\perp {\bf A} \leq {\bf c}$.

The feasible region of $P$ is nonempty if and only if the objective of $P^*$ is bounded. Conversely, the feasible region of $P^*$ is nonempty if and only if the objective of $P$ is bounded. If neither feasible region is empty, then the values of the objective functions of $P$ and $P^*$ are equal.
:::

*Remark.* While the *primal* program $P$ in the statement of Theorem [\[duality\]](#duality){reference-type="ref" reference="duality"} appears to be of a very special form, it is not hard to see that any linear program can be written in this form. Indeed, if our linear program asked us to maximize the objective, we can always convert it to a minimization problem by multiplying $\mathbf{c}$ by $-1$. If our program did not require the variables to be non-negative, we can always replace a variable $x$ by $x_+ - x_-$, where $x_+$ and $x_-$ are both required to be non-negative. If the program had some inequalities of the form $\mathbf{a_i}^\perp \mathbf{x} \geq a$, or of the form $\mathbf{a_i}^\perp \mathbf{x} \leq a$ we can first convert all the inequalities of the first type to those of the second type by negation, and then convert them to equations by introducing *slack variables* $x_i \geq 0$, and requiring $\mathbf{a_i}^\perp \mathbf{x} + x_i = a.$ Similarly, any program can be made to look like the dual program $P^*$ in the statement of Theorem [\[duality\]](#duality){reference-type="ref" reference="duality"}.

Program $L$ is almost in the primal form needed by the duality theorem, but for two differences: there is no objective function, and we want the primal variables (the angles of the triangles) to be strictly positive, rather than just non-negative.

For the moment, let us sweep these issues under the rug, by setting the objective function to be $0$, and allowing the angles to vanish -- it will be quickly apparent how to fix things up later. Let the modified program be $L_1$. The dual $L_1^*$ of $L_1$ is the following:

The dual program

:   Maximize $F({\bf u}, {\bf v}):\pi \sum_{t \in F(T)} u_t + \sum_{e\in E(T)} \Delta(e)v_e$, subject to the conditions $u_t+v_e\leq 0$ whenever $e$ is an edge of $t$.

::: theorem
[]{#maindual label="maindual"} Assume that the conditions described in conditions [\[dihpos\]](#dihpos){reference-type="ref" reference="dihpos"} and [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} are satisfied. Then the objective function of $L_1^*$ is nonpositive. It equals $0$ if and only if there is a $u$, such that $u_t=-v_e=u$, for all $t\in F(T)$, $e\in E(T)$.
:::

::: proof
*Proof.*

Observation 1

:   Note that if there is a $u$ as required in the statement of the Theorem, the objective function is, indeed, equal to $0$. This is nothing other than the equality case of Condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}.

Now, let $u = \min(u_1, \dots, u_{F(T)})$. Let $u_i^{(1)} = u_i - u$, and let $v_j^{(1)} = v_j + u$, for all values of the indices. The new variables are still feasible for $L_1^*$, and by the observation 1 above, this transformation does not change the value of the objective. Furthermore, if $u_i^{(1)} = 0$ for all $i$, then the objective is non-positive, and is equal to zero only if all of $v_j^{(1)}$ are equal to zero as well -- this is so, since all of the $v_j$ must be non-positive, and all of their coefficients are positive, by Observation [\[dihpos\]](#dihpos){reference-type="ref" reference="dihpos"}. Assume, then, that $u_t^{(1)}>0$ for $t \in \mathcal{F}^{(1)}$; $\mathcal{F}^{(1)}$ is a *proper* subset of $F(T)$ by construction.

Observation 2

:   Suppose now that $u_t^{(1)} = u$, for all $t \in \mathcal{F}_1$. Then $$F\leq \pi \sum_{t\in \mathcal{F}^{(1)}}u-
    \sum_{e\in E(\mathcal{F}^{(1)})} \Delta(e) u < 0,$$ by [\[sumdihineq\]](#sumdihineq){reference-type="ref" reference="sumdihineq"}.

Now, let $u^{(1)}  = \min_{t \in \mathcal{F}^{(1)}}(u_t^{(1)})$, and let $u_t^{2}=u_t^{(1)}=0$ if $t \notin \mathcal{F}^{(1)}$, and otherwise $u_t^{(2)} = u_t^{(1)}-u^{(1)}$. Likewise, $v_e^{(2)} = v_e^{(1)}$ if $e \notin E(\mathcal{F}^{(1)}$, and otherwise $v_e^{(2)}= v_e^{(1)} + u^{(1)}$.

This still leaves us in the feasible region of $L_1^*$ and strictly increases the value of the objective (by Observation 2). The new nonzero set $\mathcal{F}^{(2)}$ is a proper subset of $\mathcal{F}^{(1)}$, and we can repeat this process. In the end, we will wind up with a feasible point ${\bf u}^{(k)}, {\bf v}^{(k)}$, with ${\bf u}^{(k)} = {\bf 0}$, where the value of the objective is non-positive (by Observation 1), and strictly greater than the value of the objective at ${\bf u}, {\bf v}$ (by Observation 2), thus completing the proof. ◻
:::

The above theorem shows that the feasible region of $L_1$ is non-empty. In order to find a solution with strictly positive angles, we write our angles $\alpha_i$ as $\alpha_i = \beta_i+\epsilon$. We require all of the $\beta_i$ to be non-negative, and our new objective is simply $-\epsilon.$ Call the resulting program $L_2$. Its dual $L_2^*$ has the following form:

Second dual

:   Maximize $F({\bf u}, {\bf v}):\pi \sum_{t \in F(T)} u_t + \sum_{e\in E(T)} \Delta(e)v_e$, subject to the conditions $u_t+v_e\leq 0$ whenever $e$ is an edge of $t$, and also $3  \sum_{t \in F(t)} u_t + 
    2 \sum_{e\in E(T), e\notin \partial T} v_e + 
    \sum_{e\in E(T), e \in \partial T} v_e \leq -1$.

::: theorem
[]{#modified label="modified"} The optimal value of the objective of $L_2^*$ is strictly negative.
:::

::: proof
*Proof.* Suppose the contrary. Then $u_t = -v_e = u$, for some $u$, by Theorem [\[maindual\]](#maindual){reference-type="ref" reference="maindual"}. However, in that case the last inequality of $L_2^*$ is not satisfied, since the left hand side of the last constraint of $L_2^*$ vanishes. Indeed, it is equal to $$u \left(3  \sum_{t \in F(t)} 1 - 2 \sum_{e\in E(T), e\notin \partial
    T} 1 - \sum_{e\in E(T), e \in \partial T} 1 \right).$$ Observe, however, that $3 \sum_{t \in F(t)} 1$ counts each non-boundary edge with multiplicity $2$, and each boundary edge with multiplicity $1.$ ◻
:::
