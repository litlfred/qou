---
doc_id: arxiv-math-0410111v2
doc_title: "Integer Polynomial Optimization in Fixed Dimension"
section_id: sec-002-3-fptas-for-optimizing-non-negative-polynomials
section_title: "FPTAS for Optimizing Non-Negative Polynomials over Integer Points of Polytopes"
section_number: 3
pages: 2-6
source_pdf: 0410111v2.pdf
source_sha256: 0ccaeeabd8de6b5f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.936
doc_brief: "Integer Polynomial Optimization in Fixed Dimension — 5 sections: Front matter; Introduction; Computational Complexity Bounds"
---
[]{#algo label="algo"}

Consider now a polynomial function $f \in
\mathbb Z[x_1,x_2, \dots ,x_d]$ of maximum total degree $D$ and a convex polytope $P=\{x | Ax \leq b\}$ where $A$ is an $m \times
d$ integral matrix and $b$ is an integral $m$-vector. The purpose of this section is to present an algorithm to generate lower and upper bounds $L_k,U_k$ to the integer global optimum value of $$\hbox{maximize} \ f(x_1,\dots,x_d) \  \hbox
{subject to} \  (x_1,\dots,x_d) \in P \cap \mathbb Z^d.$$ We should also remark that in our algorithm the polynomial objective function $f$ can be arbitrary (e.g. non-convex). As we have seen, the optimization problem is NP-hard already for two integer variables and polynomials of degree four. Nevertheless we will see that, in fixed dimension and when $f(x) \geq 0$ for all $x \in P$, the algorithm gives a fully polynomial time approximation scheme or FPTAS. This means that, in polynomial time on the input and $(1/\epsilon)$, one can compute a $(1-\epsilon)$-approximation to the maximum. The algorithm we present is based on A. Barvinok's theory for encoding all the lattice points of a polyhedron in terms of short rational functions. See [@bar; @BarviPom] for all details. Lattice points are thought of as exponent vectors of monomials. For example, $z_1^2z_2^{-11}$ encodes the lattice point $(2,-11)$. The set of lattice points is represented by a Laurent polynomial: $g_P(z)=\sum_{\alpha \in P\cap\mathbb Z^d}
z^\alpha.$ From Barvinok's theory this exponentially-large sum of monomials $g_P(z)$ can instead be written as a polynomial-size sum of rational functions (assuming the dimension $d$ is fixed) of the form: $$\label{eq:aa}
g_P(z) = \sum_{i\in I} {E_i \frac{z^{u_i}} {\prod\limits_{j=1}^d
(1-z^{v_{ij}})}},$$ where $I$ is a polynomial-size indexing set, and where $E_i\in\{1,-1\}$ and $u_i, v_{ij} \in\mathbb Z^d$ for all $i$ and $j$. For details see [@BarviPom; @latte1; @latte2].

We need a way to encode via rational functions the values of the polynomial $f$ over all the lattice points in a polytope. The key idea, first introduced in Lemma 9 of [@latte2] and generalized in [@hugginsthesis], is that differential operators associated to $f$ can be used to compute a rational function representation of $\sum_{a\in P \cap \mathbb Z^d} f(a) z^a.$ The following Lemma recently appeared in [@newbar]:

::: lemma
[]{#operators label="operators"} Let $g_P(z)$ be the Barvinok representation of the generating function of the lattice points of $P$. Let $f$ be a polynomial in $\mathbb Z[x_1,\dots,x_d]$ of maximum total degree $D$. We can compute, in time polynomial on $D$ and the size of the input data, a Barvinok rational function representation $g_{P,f}(z)$ for the generating function $\sum_{a\in P \cap \mathbb Z^d} f(a) z^a.$
:::

::: proof
*Proof.* We give here the author's original proof the lemma for $D$ fixed. The first proof without this assumption was recently given by A. Barvinok in [@newbar].

We begin assuming $f(z)=z_r$, the general case will follow from it: Consider the action of the differential operator $z_r\frac{\partial}{\partial z_r}$ in the generating function $g_P(z)$ and on its Barvinok representation. On one hand, for the generating function $$z_r\frac{\partial}{\partial z_r}\cdot g_P(z)=\sum\limits_{\alpha\in
  P \cap \mathbb Z^d} z_r \frac{\partial}{\partial z_r} z^\alpha=
\sum\limits_{\alpha\in P \cap \mathbb Z^d}\alpha_r z^\alpha.$$ On the other hand, by linearity of the operator, we have that in terms of rational functions $$z_r\frac{\partial}{\partial z_r}\cdot g_P(z)=\sum\limits_{i \in I} E_i
z_r\frac{\partial}{\partial z_r}\cdot \left( \frac{z^{u_i}} {\prod
\limits_{j=1}^d (1-z^{v_{ij}})}\right).$$ Thus it is enough to prove that the summands of the expression above can be written in terms of rational functions computable in polynomial time. The standard quotient rule for derivatives says that $$\frac{\partial}{\partial z_r} \left(\frac{z^{u_i}} {\prod
\limits_{j=1}^d (1-z^{v_{ij}})}\right)=\frac{(\frac{\partial z^{u_i} }{\partial
z_r}) \prod^d_{j=1}(1-z^{v_{ij}})
-z^{u_i}(\frac{\partial}{\partial z_r}
\prod_{j=1}^d(1-z^{v_{ij}}))} {\prod_{j=1}^d(1-z^{v_{ij}})^2}.$$ We can expand the numerator as a sum of no more than $2^d$ monomials. This is a constant number because $d$, the number of variables, is assumed to be a constant. This argument completes the proof of our lemma when $f(z)=z_r$.

For the case when $f(z)$ is a general monomial, i.e. $f(z)=c\cdot
z_1^{\beta_1}\cdot\ldots\cdot z_d^{\beta_d}$, then we can compute again a rational function representation of $g_{P,f}(z)$ by repeated application of basic differential operators: $$c\left(z_1\frac{\partial}{\partial z_1}\right)^{\beta_1}
\cdot\ldots\cdot \left(z_d \frac{\partial}{\partial
z_d}\right)^{\beta_d}\cdot g_P(z)=\sum\limits_{\alpha\in P \cap \mathbb Z^d} c\cdot
\alpha^{\beta} z^\alpha.$$ Thus we require no more than $O(D^d)$ repetitions of the single-variable case.

Finally, if we deal with a polynomial $f$ of many monomial terms, we compute and add up all such expressions that we get for each term of $f(x)$ and obtain our desired short rational function representation for the generating function for $\sum_{\alpha\in P \cap \mathbb Z^d} f(\alpha)
z^\alpha.$ Note that only polynomially many steps are needed because $d$ is fixed and the largest number of possible monomials in $f$ of degree $s$ is $\left(\begin{smallmatrix}d+s-1\\ d-1\\
  \end{smallmatrix}\right)$, thus for fixed $d$ we will do no more than $O(D^{d})$ repetitions of the monomial case. ◻
:::

Now we are ready to present our algorithm to obtain bounds $U_k,L_k$ that reach the optimum. Step 1 of preprocessing is necessary because we rely on the elementary fact that, for a collection $S=\{s_1,\dots,s_r\}$ of non-negative real numbers, $\hbox{\rm
  maximum} \{s_i | s_i \in S \}$ equals $\lim_{k \rightarrow \infty}
\sqrt[k]{\sum_{j=1}^r s_j^k}.$

[]{#Algorithm label="Algorithm"}

A rational convex polytope $P \subset \mathbb R^d$, a polynomial objective $f \in \mathbb Z[x_1,\dots,x_d]$ of maximum total degree $D$.

An increasing sequence of lower bounds $L_k$, and a decreasing sequence of upper bounds $U_k$ reaching the maximal function value $f^*$ of $f$ over all lattice points of $P$.

If $f$ is known to be non-negative in all points of $P$, then go directly to Step 2. Else, solving $2d$ linear programs over $P$, we find lower and upper integer bounds for each of the variables $x_1,\ldots,x_d$. Let $M$ be the maximum of the absolute values of these $2d$ numbers. Thus $|x_i|\leq M$ for all $i$. Let $C$ be the maximum of the absolute values of all coefficients, and $r$ be the number of monomials of $f(x)$. Then $$L:=-rCM^D\leq f(x)\leq rCM^D=:U,$$ as we can bound the absolute value of each monomial of $f(x)$ by $CM^D$. Replace $f$ by $\bar{f}(x)=f(x)-L\leq U-L$, a non-negative polynomial over $P$. Go to Steps 2, 3, etc. and return the optimal value of $\bar{f}.$ Trivially, if we find the optimal value of $\bar{f}$ over $P$ we can extract the optimal value for $f$.

Via Barvinok's algorithm (see [@bar; @BarviPom; @newbar]), compute a short rational function expression for the generating function $g_P(z)=\sum_{\alpha\in
  P\cap\mathbb Z^d} z^\alpha$. From $g_P(z)$ compute the number $|P \cap
\mathbb Z^d|=g_P(1)$ of lattice points in $P$ in polynomial time.

From the rational function representation $g_P(z)$ of the generating function $\sum\limits_{\alpha\in P \cap \mathbb Z^d}
z^\alpha$ compute the rational function representation of $g_{P,f^k}(z)$ of $\sum_{\alpha\in P \cap \mathbb Z^d} f^k(\alpha) z^\alpha$ in polynomial time by application of Lemma [\[operators\]](#operators){reference-type="ref" reference="operators"}. We define

$$L_k:=\sqrt[k]{g_{P,f^k}(1)/g_{P,f^0}(1)}\;\;\;\text{and}\;\;\;
U_k:=\sqrt[k]{g_{P,f^k}(1)}.$$

When $\lfloor U_{k}\rfloor-\lceil L_{k}\rceil<1$ stop and return $\lceil L_{k} \rceil=\lfloor U_{k} \rfloor$ as the optimal value.

.

::: lemma
The algorithm is correct.
:::

::: proof
*Proof.* Using the fact that the arithmetic mean of a finite set of nonnegative values is at most as big as the maximum value, which in turn is at most as big as the sum of all values, we obtain the sequences of lower and upper bounds, $L_{k}$ and $U_{k}$, for the maximum: $$L_{k}=
\sqrt[k]{\frac{\sum\limits_{\alpha\in P \cap \mathbb Z^d}
f(\alpha)^{k}}{|P\cap\mathbb Z^d|}} \leq
\max\{f(\alpha):\alpha\in P\cap\mathbb Z^d\}\leq
\sqrt[k]{\sum\limits_{\alpha\in P \cap \mathbb Z^d}
f(\alpha)^{k}}=U_{k}.$$ Note that as $s\rightarrow\infty$, $L_{k}$ and $U_{k}$ approach this maximum value monotonously (from below and above, respectively). Trivially, if the difference between (rounded) upper and lower bounds becomes strictly less than $1$, we have determined the value $\max\{f(x):x\in P\cap\mathbb Z^d\}=\lceil L_{k}\rceil$. Thus the algorithm terminates with the correct answer. ◻
:::

Theorem [\[main\]](#main){reference-type="ref" reference="main"} will follow from the next lemma:

::: lemma
[]{#lemma:bounds label="lemma:bounds"} Let $f$ be a polynomial with integer coefficients and maximum total degree $D$. When the dimension $d$ is fixed,

1.  the bounds $L_k$, $U_k$ can be computed in time polynomial in $k$, the input size of $P$ and $f$, and the total degree $D$. The bounds satisfy the following inequality: $$U_k-L_k \leq f^* \cdot \left(\sqrt[k]{|P \cap \mathbb Z^d|}-1 \right).$$

2.  In addition, when $f$ is non-negative over $P$ (i.e. $f(x)\geq 0$ for all $x \in P$), for $k=(1+1/\epsilon)\log({|P \cap \mathbb Z^d|})$, $L_k$ is a $(1-\epsilon)$-approximation to the optimal value $f^*$ and it can be computed in time polynomial in the input size, the total degree $D$, and $1/\epsilon$. Similarly, $U_k$ gives a $(1+\epsilon)$-approximation to $f^*$. Moreover, with the same complexity, one can also find a feasible lattice point that approximates an optimal solution with similar quality.
:::

::: proof
*Proof.* Part (i). From Lemma [\[operators\]](#operators){reference-type="ref" reference="operators"} on fixed dimension $d$, we can compute $g_{P,f}=\sum_{\alpha\in P \cap \mathbb Z^d} f(\alpha) z^\alpha$ as a rational function in time polynomial in $D$, the total degree of $f$, and the input size of $P$. Thus, because $f^k$ has total degree of $Dk$ and the encoding length for the coefficients of $f^k$ is bounded by $k \log (kC)$ (with $C$ the largest coefficient in $f$), we can also compute $g_{P,f^k} = \sum_{\alpha\in P \cap \mathbb Z^d}
f^k(\alpha) z^\alpha$ in time polynomial in $k$, the total degree $D$, and the input size of $P$. Note that using residue techniques [@newbar], we can evaluate $g_{P,f^k}(1)$ in polynomial time. Finally observe

$$\begin{aligned}
U_k-L_k&= \sqrt[k]{\sum_{\alpha \in P \cap \mathbb Z^d}
  f^k(\alpha)}-\sqrt[k]{\frac{\sum_{\alpha \in P \cap \mathbb Z^d}
  f^k(\alpha)}{|P \cap \mathbb Z^d|}} = \sqrt[k]{\frac{\sum_{\alpha \in P
  \cap \mathbb Z^d} f^k(\alpha)}{|P \cap \mathbb Z^d|}} \left( \sqrt[k]{|P \cap
  \mathbb Z^d|}-1 \right) \\
& =L_k \left( \sqrt[k]{|P \cap \mathbb Z^d|}-1 \right) \leq f^*
  \left(\sqrt[k]{|P \cap \mathbb Z^d|}-1 \right). 
\end{aligned}$$

Part (ii). Note that if $\left(\sqrt[k]{|P \cap \mathbb Z^d|}-1 \right) \leq
\epsilon$ then $L_k$ is indeed a $(1-\epsilon)$-approximation because $$f^* \leq U_k =L_k+(U_k-L_k) \leq L_k + f^*\left(\sqrt[k]{|P \cap
    \mathbb Z^d|}-1 \right) \leq L_k +f^* \epsilon.$$

Observe that $\phi(\epsilon) := (1+1/\epsilon)/(1/\log(1+\epsilon))$ is an increasing function for $\epsilon <1$ and $\lim_{\epsilon \rightarrow
  0}\phi(\epsilon)=1$, thus $\phi(\epsilon)\geq 1$ for $0<\epsilon\leq1$. Hence, for all $k \geq \log({|P \cap \mathbb Z^d|})+\log({|P \cap
  \mathbb Z^d|})/\epsilon \geq \log({|P \cap \mathbb Z^d|})/\log(1+\epsilon),$ we have indeed $\left(\sqrt[k]{|P \cap \mathbb Z^d|}-1 \right) \leq \epsilon.$ Finally, from Lemma [\[operators\]](#operators){reference-type="ref" reference="operators"}, the calculation of $L_k$ for $k=\log({|P \cap \mathbb Z^d|})+\log({|P \cap \mathbb Z^d|})/\epsilon$ would require a number of steps polynomial in the input size and $1/\epsilon$. A very similar argument can be written for $U_k$ but we omit it here.

To complete the proof of part (ii) it remains to show that not only we approximate the optimal value $f^*$ but we can also efficiently find a lattice point $\alpha$ with $f(\alpha)$ giving that quality approximation of $f^*$. Let $k = (1+1/\epsilon)\log({|P \cap
  \mathbb Z^d|})$, thus, by the above discussion, $L_k$ is an $(1-\epsilon)$-approximation to $f^*$. Let $Q_0 := [-M,M]^d$ denote the box computed in Step 1 of the algorithm such that $P\subseteq
Q_0$. By bisecting $Q_0$, we obtain two boxes $Q_1'$ and $Q_1''$. By applying the algorithm separately to the polyhedra $P\cap Q_1'$ and $P\cap Q_1''$, we compute lower bounds $L_k'$ and $L_k''$ for the optimization problems restricted to $Q_1'$ and $Q_1''$, respectively. Because $L_k^k$ is the arithmetic mean of $f^k(\alpha)$ for $\alpha\in
P\cap\mathbb Z^d$, clearly $$\min\{L_k', L_k''\} \leq L_k \leq \max\{L_k', L_k''\}.$$ Without loss of generality, let $L_k'\geq L_k''$. We now apply the bisection procedure iteratively on $Q_k'$. After $d\log M$ bisection steps, we obtain a box $Q_k'$ that contains a single lattice point $\alpha\in P\cap Q_k'\cap Z^d$, which has an objective value $f(\alpha) = L_k' \geq L_k \geq (1-\epsilon) f^*$. ◻
:::

We remark that if we need to apply the construction of Step 1 of the algorithm because $f$ takes negative values on $P$, then we can only obtain an $(1-\epsilon)$-approximation (and $(1+\epsilon)$-approximation, respectively) for the modified function $\bar f$ in polynomial time, but not the original function $f$. We also emphasize that, although our algorithm requires the computation of $\sum_{\alpha \in P} f^q(\alpha)$ for different powers of $f$, these numbers are obtained without explicitly listing all lattice points (a hard task), nor we assume any knowledge of the individual values $f(\alpha)$. We can access the power means $\sum_{\alpha \in P}
f^q(\alpha)$ indirectly via rational functions. Here are two small examples:

#### Example 1, monomial optimization over a quadrilateral:

The problem we consider is that of maximizing the value of the monomial $x^3y$ over the lattice points of the quadrilateral $$\{(x,y) | 3991 \leq 3996\,x-4\,y \leq 3993, \ 1/2\leq x \leq 5/2\}.$$ It contains only 2 lattice points. The sum of rational functions encoding the lattice points is $$\frac{{x}^{2}{y}^{1000}}{\left( 1-(xy^{999})^{-1} \right)
 \left( 1-{y}^{-1} \right)}+\frac{xy}{\left( 1-x{y}^{999} \right)
 \left( 1-{y}^{-1} \right)}+
{\frac {xy}{ \left( 1-x{y}^{999}
 \right)  \left( 1-y \right) }}+\frac{{x}^{2}{y}^{1000}}{\left( 1-(xy^{999})^{-1} \right)\left( 1-y \right)}.$$ In the first iteration $L_1=4000.50$ while $U_1=8001$. After thirty iterations, we see $L_{30}=7817.279750$ while $U_{30}=8000$, the true optimal value.

#### Example 2, nvs04 from MINLPLIB:

A somewhat more complicated example, from a well-known library of test examples (see <http://www.gamsworld.org/minlp/>), is the problem given by $$\begin{aligned}
    \min\quad & 100 \left(\frac12 + i_2 - \left(\frac35 + i_1\right)^2 \right)^2 + \left(\frac25 -
    i_1\right)^2\\
    \text{s.\,t.}\quad & i_1, i_2 \in [0,200] \cap \mathbb Z.
  \end{aligned}$$ Its optimal solution as given in MINLPLIB is $i_1=1$, $i_2=2$ with an objective value of $0.72$. Clearly, to apply our algorithm from page literally, the objective function needs to be multiplied by a factor of $100$ to obtain an integer valued polynomial.

Using the bounds on $i_1$ and $i_2$ we obtain an upper bound of $165
\cdot 10^9$ for the objective function, which allows us to convert the problem into an equivalent maximization problem, where all feasible points have a non-negative objective value. The new optimal objective value is $164999999999.28.$ Expanding the new objective function and translating it into a differential operator yields $$\begin{aligned}
    &\frac{4124999999947}{25} \mathrm{Id} - 28 z_2 \frac{\partial}{\partial
      z_2}+\frac{172}{5} z_1\frac{\partial}{\partial z_1}-117 \left(z_1
      \frac{\partial}{\partial z_1} \right) ^{(2)} - 100
    \left(z_2 \frac{\partial}{\partial z_2}\right)^{(2)} \\
    &+ 240 \left(z_2
      \frac{\partial}{\partial z_2}\right) \left(z_1 \frac{\partial}{\partial
        z_1}\right) 
    + 200  \left(z_2
      \frac{\partial}{\partial z_2}\right) \left(z_1 \frac{\partial}{\partial
        z_1}\right) ^{(2)} - 240 \left(z_1 \frac{\partial}{\partial
        z_1}\right)^{(3)}  
    - 100 \left(z_1 \frac{\partial}{\partial
        z_1}\right)^{(4)}.
  
\end{aligned}$$ The short generating function can be written as $g(z_1,z_2) = \left( \frac1{1-z_1} - \frac{z_1^{201}}{1-z_1} \right)
  \left( \frac1{1-z_2} - \frac{z_2^{201}}{1-z_2} \right).$

In this example, the number of lattice points is $|P\cap \mathbb Z^2|=40401.$ The first bounds are $L_1=139463892042.292155534$, $U_1=28032242300500.723262442$. After 30 iterations the bounds become $L_{30}=164999998845.993553019$ and $U_{30}=165000000475.892451381.$
