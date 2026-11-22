---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-012-41-orthogonal-coordinates-for-the-flag-manifold
section_title: "Orthogonal coordinates for the flag manifold"
section_number: 4.1
pages: 10-14
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.937
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:ortho label="sec:ortho"}

An immediate consequence of Proposition [\[prop:equivalent definition of flag manifold\]](#prop:equivalent definition of flag manifold){reference-type="ref" reference="prop:equivalent definition of flag manifold"} is that the flag manifold is connected. The characterization [\[eq:homo2\]](#eq:homo2){reference-type="eqref" reference="eq:homo2"} says that a point on $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ may be represented by the equivalence class of matrices $$\begin{aligned}
\label{eq:equivalence class}
\llbracket Q \rrbracket= \left\lbrace Q\begin{bsmallmatrix}
Q_1 & 0 & \dots & 0 \\
0 & Q_2 & \dots & 0\\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & Q_{d+1}
\end{bsmallmatrix}: Q_i \in \mathop{\mathrm{O}}(n_i-n_{i-1}),\; i=1,\dots,d+1, \;\prod_{i=1}^{d+1} \det Q_i = 1 \right\rbrace
\end{aligned}$$ for some $Q \in \mathop{\mathrm{SO}}(n)$. We will call such a representation *orthogonal coordinates* for the flag manifold.

The Lie algebra of $\mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n-n_d) \bigr)$ is simply $\mathfrak{so}(n_1) \times \mathfrak{so}(n_2-n_1)\times \dots \times \mathfrak{so}(n-n_d)$, which we will regard as a Lie subalgebra of block diagonal matrices, $$\begin{aligned}
\mathfrak{h} &= \left\lbrace
\begin{bsmallmatrix}
A_1 & 0 & \dots & 0\\
0 & A_2 & \dots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \dots & A_{d+1} 
\end{bsmallmatrix} \in \mathfrak{so}(n) :\begin{multlined} A_1 \in \mathfrak{so}(n_1), A_2 \in \mathfrak{so}(n_2-n_1), \dots \\ \dots,  A_{d+1} \in \mathfrak{so}(n-n_d) \end{multlined}  \right\rbrace. \label{eq:h}
\intertext{Let $\mathfrak{m}$ be the natural complement of $\mathfrak{h}$ in $\mathfrak{so}(n)$,}
\mathfrak{m} &= \left\lbrace
\begin{bsmallmatrix}
0 & B_{1,2}  &\dots & B_{1,d+1} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0   &\dots & B_{2,d+1} \\
\vdots & \vdots & \ddots & \vdots\\
-B_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d+1}^{\scriptscriptstyle\mathsf{T}}& \dots & 0
\end{bsmallmatrix} \in \mathfrak{so}(n) : \begin{multlined} B_{ij}\in \mathbb{R}^{(n_i-n_{i-1}) \times (n_j-n_{j-1})}, \\ 1\le i < j \le d+1 \end{multlined}\right\rbrace.\label{eq:m}
\end{aligned}$$ In particular, we have the direct sum decomposition $\mathfrak{so}(n) = \mathfrak{h}  \oplus \mathfrak{m}$ as vector spaces.

The groups $\mathop{\mathrm{O}}(n)$ and $\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1)\times \cdots \times \mathop{\mathrm{O}}(n - n_d)$ have the same Lie algebras as $\mathop{\mathrm{SO}}(n)$ and $\mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1)\times  \cdots \times  \mathop{\mathrm{O}}(n - n_d)\bigr)$, namely, $\mathfrak{so}(n)$ and $\mathfrak{so}(n_1) \times \mathfrak{so}(n_2-n_1)\times \dots \times \mathfrak{so}(n-n_d)$ respectively. The tangent space of a homogeneous space $G/H$ at any point is a translation of the tangent space at the identity element $\llbracket H \rrbracket\in G/H$, which depends only on the Lie algebras $\mathfrak{g}$ and $\mathfrak{h}$ of $G$ and $H$ respectively: $$T_{\llbracket H \rrbracket} G/H  \simeq \mathfrak{g}/\mathfrak{h},$$ a fact that we will use in the proof of Proposition [\[prop:tangent1\]](#prop:tangent1){reference-type="ref" reference="prop:tangent1"}. As such we do not need to distinguish the two homogeneous space structures [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"} and [\[eq:homo2\]](#eq:homo2){reference-type="eqref" reference="eq:homo2"} when we discuss geometric quantities associated with tangent spaces, e.g., geodesic, gradient, Hessian, parallel transport. In the sequel we will make free use of this flexibility in switching between [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"} and [\[eq:homo2\]](#eq:homo2){reference-type="eqref" reference="eq:homo2"}.

::: proposition
[]{#prop:reductive complement label="prop:reductive complement"} Let $\mathfrak{h}$ and $\mathfrak{m}$ be as in [\[eq:h\]](#eq:h){reference-type="eqref" reference="eq:h"} and [\[eq:m\]](#eq:m){reference-type="eqref" reference="eq:m"} and $H =\mathop{\mathrm{O}}(n_1)\times \mathop{\mathrm{O}}(n_2-n_1)\times \dots \times \mathop{\mathrm{O}}(n-n_d)$. Then the subspace $\mathfrak{m}$ is $\mathop{\mathrm{Ad}}_H$-invariant, i.e., $\mathop{\mathrm{Ad}}(a)(X) \in \mathfrak{m}$ for every $a \in H$ and $X\in \mathfrak{m}$.
:::

::: proof
*Proof.* We need to show that $\mathop{\mathrm{Ad}}(a)(X) \in \mathfrak{m}$ whenever $a\in H$ and $X\in \mathfrak{m}$. For notational simplicity, we assume $d = 2$. Let $$a = \begin{bsmallmatrix}
A_1 & 0 & 0 \\[0.75ex]
0 & A_2 & 0 \\[0.75ex]
0 & 0 & A_3
\end{bsmallmatrix}\qquad\text{and}\qquad
X = \begin{bsmallmatrix}
0 & B_{1,2} & B_{1,3} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0 & B_{2,3} \\
-B_{1,3}^{\scriptscriptstyle\mathsf{T}}& -B_{2,3}^{\scriptscriptstyle\mathsf{T}}& 0
\end{bsmallmatrix},$$ where $A_i \in \mathop{\mathrm{O}}(n_i-n_{i-1})$, $i =1,2,3$, and $B_{ij} \in \mathbb{R}^{(n_i-n_{i-1}) \times (n_j-n_{j-1})}$, $1\le i < j \le 3$. Then $\mathop{\mathrm{Ad}}(a)(X) =a X a^{-1} = a X a^{\scriptscriptstyle\mathsf{T}}$ since $a$ is an orthogonal matrix; and we have $$a X a^{\scriptscriptstyle\mathsf{T}}= \begin{bsmallmatrix}
A_1 & 0 & 0 \\[0.75ex]
0 & A_2 & 0 \\[0.75ex]
0 & 0 & A_3
\end{bsmallmatrix}  \begin{bsmallmatrix}
0 & B_{1,2} & B_{1,3} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0 & B_{2,3} \\
-B_{1,3}^{\scriptscriptstyle\mathsf{T}}& -B_{2,3}^{\scriptscriptstyle\mathsf{T}}& 0
\end{bsmallmatrix} \begin{bsmallmatrix}
A_1^{\scriptscriptstyle\mathsf{T}}& 0 & 0 \\
0 & A_2^{\scriptscriptstyle\mathsf{T}}& 0 \\
0 & 0 & A_3^{\scriptscriptstyle\mathsf{T}}
\end{bsmallmatrix} 
 = \begin{bsmallmatrix}
0 & A_1 B_{1,2} A_2^{\scriptscriptstyle\mathsf{T}}& A_1B_{1,3}A_3^{\scriptscriptstyle\mathsf{T}}\\
-A_2 B_{1,2}^{\scriptscriptstyle\mathsf{T}}A_1^{\scriptscriptstyle\mathsf{T}}& 0 & A_2B_{2,3}A_3^{\scriptscriptstyle\mathsf{T}}\\
-A_3B_{1,3}^{\scriptscriptstyle\mathsf{T}}A_1^{\scriptscriptstyle\mathsf{T}}& -A_3B_{2,3}^{\scriptscriptstyle\mathsf{T}}A_2^{\scriptscriptstyle\mathsf{T}}& 0
\end{bsmallmatrix} \in \mathfrak{m}$$ as required. ◻
:::

We now have all the ingredients necessary for deriving closed-form analytic expressions for the tangent space, metric, geodesic, geodesic distance, and parallel transport on a flag manifold in orthogonal coordinates. We begin with the representation of a tangent space as a vector space of matrices.

::: proposition
[]{#prop:tangent1 label="prop:tangent1"} Let $\llbracket Q \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = \mathop{\mathrm{O}}(n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr)$ be represented by $Q\in \mathop{\mathrm{O}}(n)$. Its tangent space at $\llbracket Q \rrbracket$ is given by $$\begin{gathered}
T_{\llbracket Q \rrbracket}  \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)  = \lbrace QB \in \mathbb{R}^{n \times n} : B \in \mathfrak{m}\rbrace \\
=\left\lbrace Q\begin{bsmallmatrix}
0 & B_{1,2}  &\dots & B_{1,d+1} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0   &\dots & B_{2,d+1} \\
\vdots & \vdots & \ddots & \vdots\\
-B_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d+1}^{\scriptscriptstyle\mathsf{T}}& \dots & 0
\end{bsmallmatrix} \in \mathbb{R}^{n \times n} :\begin{multlined} B_{i,j}\in \mathbb{R}^{(n_i-n_{i-1}) \times (n_j-n_{j-1})}, \\ 1\le i < j \le d + 1 \end{multlined} \right\rbrace.
\end{gathered}$$ In particular, the dimension of a flag manifold is given by $$\dim \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = \sum_{1 \le i < j \le d+1} (n_i-n_{i-1}) (n_j - n_{j-1}).$$
:::

::: proof
*Proof.* Let $M = \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$. For $Q = I$, the identity matrix, this follow from $T_{\llbracket I \rrbracket} M \simeq \mathfrak{g}/\mathfrak{h} \simeq \mathfrak{m}$. For $Q$ arbitrary, the left translation $L_Q: M \to M$ is a diffeomorphism, which means that $(d {L_Q})_{\llbracket I \rrbracket} : T_{\llbracket I \rrbracket} M \to T_{\llbracket Q \rrbracket} M$ is an isomorphism. The result then follows from $(d {L_Q})_{\llbracket I \rrbracket} (X) = QX$ for all $X \in T_{\llbracket I \rrbracket} M$. ◻
:::

There are several ways to equip $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ with a Riemannian metric but there is a distinguished choice that is given by a negative multiple of the *Killing form* of $\mathfrak{so}(n)$, although we will not need to introduce this concept.

::: proposition
[]{#prop:metric label="prop:metric"} The metric $g$ on $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ defined by $$\label{eq:metric1}
g_{\llbracket Q \rrbracket} (X,Y) = \frac{1}{2} \mathop{\mathrm{tr}}(X^{\scriptscriptstyle\mathsf{T}}Y)$$ for all $X,Y\in T_{\llbracket Q \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ is an $\mathop{\mathrm{SO}}(n)$-invariant metric. If we write $$X = Q\begin{bsmallmatrix}
0 & B_{1,2}  &\dots & B_{1,d+1} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0   &\dots & B_{2,d+1} \\
\vdots & \vdots & \ddots & \vdots\\
-B_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d+1}^{\scriptscriptstyle\mathsf{T}}& \dots & 0
\end{bsmallmatrix}, \quad 
Y = Q\begin{bsmallmatrix}
0 & C_{1,2}  &\dots & C_{1,d+1} \\
-C_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0   &\dots & C_{2,d+1} \\
\vdots & \vdots & \ddots & \vdots\\
-C_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -C_{2,d+1}^{\scriptscriptstyle\mathsf{T}}& \dots & 0
\end{bsmallmatrix}  \in \mathbb{R}^{n \times n},$$ where $B_{ij}, C_{ij}\in \mathbb{R}^{(n_i-n_{i-1}) \times (n_j-n_{j-1})}$, $1\le i < j \le d$, then $g$ may be expressed as $$\label{eq:metric2}
g_{\llbracket Q \rrbracket}  (X, Y) = \sum_{1\le i < j \le d+1} \mathop{\mathrm{tr}}(B_{ij}^{\scriptscriptstyle\mathsf{T}}C_{ij}).$$
:::

::: proof
*Proof.* We will first need to establish an $\mathop{\mathrm{Ad}}_{\mathop{\mathrm{SO}}(n)}$-invariant inner product on $\mathfrak{so}(n)$. It is a standard fact [@{O'Neil1983}] that bi-invariant metrics on a Lie group $G$ are in one-to-one correspondence with $\mathop{\mathrm{Ad}}_G$-invariant inner products on its Lie algebra $\mathfrak{g}$. In our case, $G = \mathop{\mathrm{SO}}(n)$, $\mathfrak{g} =\mathfrak{so}(n)$, and $\mathop{\mathrm{Ad}}_{\mathop{\mathrm{SO}}(n)} : \mathop{\mathrm{SO}}(n) \to \mathop{\mathrm{GL}}(\mathfrak{so}(n))$. Since $\mathop{\mathrm{SO}}(n)$ is compact, by Proposition [\[prop:nhs\]](#prop:nhs){reference-type="ref" reference="prop:nhs"} it has a bi-invariant metric, which corresponds to an $\mathop{\mathrm{Ad}}_{\mathop{\mathrm{SO}}(n)}$-invariant inner product on $\mathfrak{so}(n)$.

When $n \ne 2,4$, $\mathfrak{so}(n)$ is a simple Lie algebra and so the $\mathop{\mathrm{Ad}}_{\mathop{\mathrm{SO}}(n)}$-invariant inner product is unique up to a scalar multiple. When $n  = 2$, $\mathop{\mathrm{SO}}(2)$ is one-dimensional and thus abelian, so the bi-invariant metric on $\mathop{\mathrm{SO}}(2)$ is unique up to a scalar. When $n  = 4$, $\mathop{\mathrm{SO}}(4) \simeq \mathop{\mathrm{SO}}(3) \times \mathop{\mathrm{SO}}(3)$ as Lie groups, so it has a two-dimensional family of bi-invariant metrics. For all values of $n$, we may take our $\mathop{\mathrm{Ad}}_{\mathop{\mathrm{SO}}(n)}$-invariant inner product (the choice is unique for all $n \ne 4$) as $$\label{eq:ip1}
\langle X,Y\rangle \coloneqq \frac{1}{2} \mathop{\mathrm{tr}}(X^{\scriptscriptstyle\mathsf{T}}Y)$$ for all $X,Y\in \mathfrak{so}(n)$.

Let $G =\mathop{\mathrm{SO}}(n)$ and $H = \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n-n_d) \bigr)$. We will use the characterization of a flag manifold in [\[eq:homo2\]](#eq:homo2){reference-type="eqref" reference="eq:homo2"}, i.e., $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = G/ H$. Since $\mathfrak{m}$ is a subspace of $\mathfrak{so}(n)$, the restriction of $\langle\cdot,\cdot\rangle$ in [\[eq:ip1\]](#eq:ip1){reference-type="eqref" reference="eq:ip1"} to $\mathfrak{m}$, denoted by $\langle \cdot,\cdot\rangle_{\mathfrak{m}}$, is an inner product on $\mathfrak{m}$. It is easy to verify that $\langle \cdot,\cdot\rangle_{\mathfrak{m}}$ is $\mathop{\mathrm{Ad}}_H$-invariant. Taken together with Propositions [\[prop:metric inner product correspondence\]](#prop:metric inner product correspondence){reference-type="ref" reference="prop:metric inner product correspondence"}, [\[prop:nhs\]](#prop:nhs){reference-type="ref" reference="prop:nhs"}, and [\[prop:reductive complement\]](#prop:reductive complement){reference-type="ref" reference="prop:reductive complement"}, we have that $\langle\cdot,\cdot\rangle_{\mathfrak{m}}$ uniquely determines a $G$-invariant metric $g$ on $G/H$, as required. ◻
:::

Unsurprisingly the metric $g$ in Proposition [\[prop:metric\]](#prop:metric){reference-type="ref" reference="prop:metric"} coincides with the canonical metric on Grassmannian ($d= 1$) introduced in [@EAS]. It also follows from Theorem [\[thm:GO\]](#thm:GO){reference-type="ref" reference="thm:GO"} that, with this metric $g$, $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ is not merely a Riemannian manifold but also a geodesic orbit space. In fact, $g$ is the only choice of a metric that makes $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ into a geodesic orbit space [@AA2007]. We will next derive explicit analytic expressions for geodesic (Propositions [\[prop:geodesics1\]](#prop:geodesics1){reference-type="ref" reference="prop:geodesics1"} and [\[prop:geodesics2\]](#prop:geodesics2){reference-type="ref" reference="prop:geodesics2"}), arclength (Corollary [\[cor:arc-length\]](#cor:arc-length){reference-type="ref" reference="cor:arc-length"}), geodesic distance (Proposition [\[prop:geodist\]](#prop:geodist){reference-type="ref" reference="prop:geodist"}), and parallel transport (Proposition [\[prop:pt\]](#prop:pt){reference-type="ref" reference="prop:pt"}).

::: proposition
[]{#prop:geodesics1 label="prop:geodesics1"} Let $\llbracket Q \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = \mathop{\mathrm{O}}(n)/\bigl(\mathop{\mathrm{O}}(n_1)\times \dots \times \mathop{\mathrm{O}}(n-n_d)\bigr)$ and $g$ be the metric in [\[eq:metric2\]](#eq:metric2){reference-type="eqref" reference="eq:metric2"}. Every geodesic on $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ passing through $\llbracket Q \rrbracket$ takes the form $$\llbracket Q(t) \rrbracket= \left\lbrace Q\exp (tB) \begin{bsmallmatrix}
Q_1 & 0 & \dots & 0\\
0 & Q_2 & \dots & 0\\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & Q_{d+1}
\end{bsmallmatrix}  \in \mathop{\mathrm{O}}(n): Q_i \in \mathop{\mathrm{O}}(n_i- n_{i-1}),\; i=1,\dots, d+1
\right\rbrace,$$

for some direction $$\label{eq:exp map direction}
B = \begin{bsmallmatrix}
0 & B_{1,2}  &\dots & B_{1,d+1} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0   &\dots & B_{2,d+1} \\
\vdots & \vdots & \ddots & \vdots\\
-B_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d+1}^{\scriptscriptstyle\mathsf{T}}& \dots & 0
\end{bsmallmatrix} \in \mathbb{R}^{n \times n}, \quad \begin{multlined} B_{ij}\in \mathbb{R}^{(n_i-n_{i-1}) \times (n_j-n_{j-1})}, \\ 1\le i < j \le d+1\end{multlined}.$$
:::

::: proof
*Proof.* Since $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ with the metric $g$ in Proposition [\[prop:metric\]](#prop:metric){reference-type="ref" reference="prop:metric"} is a geodesic orbit space, the result follows immediately from Theorem [\[thm:1-parameter subgp\]](#thm:1-parameter subgp){reference-type="ref" reference="thm:1-parameter subgp"}. ◻
:::

::: corollary
[]{#cor:arc-length label="cor:arc-length"} The arclength of a geodesic $\gamma(t) = \llbracket Q(t) \rrbracket$ passing through $Q$ in the direction $B$ is given by $$\lVert\gamma(t)  \rVert  = t \Bigl[  \sum\nolimits_{1\le i<j \le d+1} \mathop{\mathrm{tr}}(B_{ij}^{\scriptscriptstyle\mathsf{T}}B_{ij}) \Bigr]^{1/2} 
 = t \sqrt{\frac{\mathop{\mathrm{tr}}(B^{\scriptscriptstyle\mathsf{T}}B)}{2}},$$ where $B$ is as in [\[eq:exp map direction\]](#eq:exp map direction){reference-type="eqref" reference="eq:exp map direction"}.
:::

::: proof
*Proof.* This follows from the definition of arclength $$\lVert\gamma(t)  \rVert \coloneqq  \int_{0}^t \sqrt{g_{\llbracket Q \rrbracket} (\gamma'(x), \gamma'(x)) } \; dx$$ and the expressions for $g$ in [\[eq:metric1\]](#eq:metric1){reference-type="eqref" reference="eq:metric1"} and [\[eq:metric2\]](#eq:metric2){reference-type="eqref" reference="eq:metric2"}. ◻
:::

::: proposition
[]{#prop:geodesics2 label="prop:geodesics2"} Let $\gamma$ be a geodesic in $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = \mathop{\mathrm{O}}(n)/\bigl(\mathop{\mathrm{O}}(n_1)\times \dots \times \mathop{\mathrm{O}}(n-n_d)\bigr)$ with $\gamma(0) = \llbracket Q \rrbracket$ for some $Q\in \mathop{\mathrm{O}}(n)$ and $\gamma'(0) = H \in T_{\llbracket Q \rrbracket}  \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$. Let $Q^{\scriptscriptstyle\mathsf{T}}H =  V D V^{\scriptscriptstyle\mathsf{T}}$ with $V\in \mathop{\mathrm{O}}(n)$ and $$\begin{aligned}
\label{eq:geodesic variable D}
D = \operatorname{diag} \biggl( \begin{bmatrix}
0 & -\lambda_1 \\
\lambda_1 & 0 
\end{bmatrix}, \dots, \begin{bmatrix}
0 & -\lambda_r \\
\lambda_r & 0 
\end{bmatrix}, 0_{n-2r}
\biggr)\in \mathfrak{so}(n),
\end{aligned}$$ where $2r = \mathop{\mathrm{rank}}(Q^{\scriptscriptstyle\mathsf{T}}H )$ and $\lambda_1,\dots,\lambda_r$ are positive real numbers. Then $\gamma(t)  = \llbracket U \Sigma(t) V^{\scriptscriptstyle\mathsf{T}}\rrbracket$ where $U = QV\in \mathop{\mathrm{O}}(n)$ and $$\begin{aligned}
 \label{eq:geodesic variable sigma}
\Sigma(t) = \operatorname{diag} \biggl(
\begin{bmatrix}
\cos t\lambda_1 & -\sin t\lambda_1 \\
\sin t\lambda_1 & \cos t\lambda_1 
\end{bmatrix}, 
\dots, 
\begin{bmatrix}
\cos t\lambda_r & -\sin t\lambda_r \\
\sin t\lambda_r & \cos t\lambda_r 
\end{bmatrix}, 
I_{n - 2r}
\biggr) \in \mathop{\mathrm{O}}(n).
\end{aligned}$$
:::

::: proof
*Proof.* By Proposition [\[prop:geodesics1\]](#prop:geodesics1){reference-type="ref" reference="prop:geodesics1"}, the geodesic $\gamma$ takes the form $\gamma(t) = \llbracket Q \exp(tB) \rrbracket$ for some $B\in \mathfrak{so}(n)$ and $Q \in \mathop{\mathrm{O}}(n)$ representing $\gamma(0)$. Hence we have $H = \gamma'(0) = QB$ and $Q^{\scriptscriptstyle\mathsf{T}}H = B$. Since $B$ is a skew-symmetric and thus a normal matrix, by the spectral theorem [@Sheldon1997 Theorem 7.25], $B = V D V^{\scriptscriptstyle\mathsf{T}}$ for some $V\in \mathop{\mathrm{O}}(n)$ and $D$ of the form in [\[eq:geodesic variable D\]](#eq:geodesic variable D){reference-type="eqref" reference="eq:geodesic variable D"}, with $2r = \mathop{\mathrm{rank}}(B) =  \mathop{\mathrm{rank}}(Q^{\scriptscriptstyle\mathsf{T}}H)$ and $\lambda_1,\dots,\lambda_r$ are positive reals as they are singular values of $B$. Therefore, $$Q \exp(tB) = U \Sigma(t) V^{\scriptscriptstyle\mathsf{T}},$$ where $U = QV$ and $\Sigma(t)$ is as in [\[eq:geodesic variable sigma\]](#eq:geodesic variable sigma){reference-type="eqref" reference="eq:geodesic variable sigma"}. ◻
:::

::: proposition
[]{#prop:geodist label="prop:geodist"} The geodesic distance with respect to the metric $g$ between $\llbracket P \rrbracket, \llbracket Q \rrbracket\in  \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = \mathop{\mathrm{O}}(n)/\bigl(\mathop{\mathrm{O}}(n_1)\times \dots \times \mathop{\mathrm{O}}(n-n_d)\bigr)$ is $$\label{eq:geodist}
d(\llbracket P \rrbracket,\llbracket Q \rrbracket) = \sqrt{\sum\nolimits_{i=1}^r \lambda_i^2},$$ where $\lambda_1,\dots, \lambda_r$ are positive real numbers such that $P^{\scriptscriptstyle\mathsf{T}}Q = V \Sigma V^{\scriptscriptstyle\mathsf{T}}$ with $V \in \mathop{\mathrm{O}}(n)$ and $$\Sigma = \operatorname{diag} \biggl(
\begin{bmatrix}
\cos \lambda_1 & -\sin \lambda_1 \\
\sin \lambda_1 & \cos \lambda_1 
\end{bmatrix}, 
\dots, 
\begin{bmatrix}
\cos \lambda_r & -\sin \lambda_r \\
\sin \lambda_r & \cos \lambda_r 
\end{bmatrix}, 
0_{n-2r}
\biggr).$$
:::

::: proof
*Proof.* By Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"}[\[it:cls1\]](#it:cls1){reference-type="eqref" reference="it:cls1"}, we may regard $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ as a closed, and therefore compact, submanifold of $\mathop{\mathrm{Gr}}(n_1,n)\times \dots \times \mathop{\mathrm{Gr}}(n_d,n)$. By Theorem [\[thm:Hopf\--Rinow\]](#thm:Hopf--Rinow){reference-type="ref" reference="thm:Hopf--Rinow"}, there is a distance minimizing geodesic $\llbracket P\exp(tB) \rrbracket$ connecting $\llbracket P \rrbracket$ and $\llbracket Q \rrbracket$. By Corollary [\[cor:arc-length\]](#cor:arc-length){reference-type="ref" reference="cor:arc-length"}, we get [\[eq:geodist\]](#eq:geodist){reference-type="eqref" reference="eq:geodist"} with $\lambda_1,\lambda_1,\dots,\lambda_r,\lambda_r$ the nonzero singular values of $B$. Lastly, by Proposition [\[prop:geodesics2\]](#prop:geodesics2){reference-type="ref" reference="prop:geodesics2"}, we get the decomposition $P^{\scriptscriptstyle\mathsf{T}}Q = V \Sigma V^{\scriptscriptstyle\mathsf{T}}$ for some $V\in \mathop{\mathrm{O}}(n)$. ◻
:::

Let $\mathfrak{m}$ be as in [\[eq:m\]](#eq:m){reference-type="eqref" reference="eq:m"}. For $B \in \mathfrak{m}$, we define a map $$\label{eq:phi}
\varphi_{B}: \mathfrak{m} \to \mathfrak{m}, \quad X \mapsto \frac{1}{2}[B,X]_{\mathfrak{m}} \coloneqq  \frac{1}{2} \operatorname{proj}_{\mathfrak{m}} ([B,X]),$$ where $\operatorname{proj}_{\mathfrak{m}}:\mathfrak{so}(n) \to \mathfrak{m}$ is the projection from $\mathfrak{so}(n) = \mathfrak{h} \oplus \mathfrak{m}$ to $\mathfrak{m}$. For example, if $d = 2$ and $$B = \begin{bmatrix}
0 & B_{12} & B_{13} \\
-B_{12}^{\scriptscriptstyle\mathsf{T}}& 0 & B_{23} \\
-B_{13}^{\scriptscriptstyle\mathsf{T}}& -B_{23}^{\scriptscriptstyle\mathsf{T}}& 0
\end{bmatrix}\in\mathfrak{m},
\quad X = \begin{bmatrix}
0 & X_{12} & X_{13} \\
-X_{12}^{\scriptscriptstyle\mathsf{T}}& 0 & X_{23} \\
-X_{13}^{\scriptscriptstyle\mathsf{T}}& -X_{23}^{\scriptscriptstyle\mathsf{T}}& 0
\end{bmatrix}\in \mathfrak{m},$$ where $B_{ij},X_{ij}\in \mathbb{R}^{(n_i-n_{i-1}) \times (n_j-n_{j-1})}, 1\le i < j \le 3$, then $$\varphi_B(X) =  \begin{bmatrix}
0 & -B_{12} X_{23}^{\scriptscriptstyle\mathsf{T}}+  X_{12} B_{23}^{\scriptscriptstyle\mathsf{T}}& B_{11}X_{23} - X_{11}B_{23} \\
X_{23}B_{12}^{\scriptscriptstyle\mathsf{T}}-  B_{23} X_{12}^{\scriptscriptstyle\mathsf{T}}& 0 & -B_{11}X_{12}^{\scriptscriptstyle\mathsf{T}}+ X_{11}B_{12}^{\scriptscriptstyle\mathsf{T}}\\
-X_{23}^{\scriptscriptstyle\mathsf{T}}B_{11}^{\scriptscriptstyle\mathsf{T}}+ B_{23}^{\scriptscriptstyle\mathsf{T}}
X_{11}^{\scriptscriptstyle\mathsf{T}}& X_{12} B_{11}^{\scriptscriptstyle\mathsf{T}}- B_{12} X_{11}^{\scriptscriptstyle\mathsf{T}}& 0
\end{bmatrix}\in \mathfrak{m}.$$

::: proposition
[]{#prop:pt label="prop:pt"} Let $B,X \in T_{\llbracket I \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots, n_d; n) \cong  \mathfrak{m}$ and $\llbracket Q \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots, n_d; n)$. The parallel transport of $QX\in T_{\llbracket Q \rrbracket}  \mathop{\mathrm{Flag}}(n_1,\dots, n_d; n)$ along the geodesic $\llbracket Q\exp(tB) \rrbracket$ is $$\label{eq:pt}
X(t) = Q \exp(tB)  e^{-\varphi_{tB}} ( X ),$$ where $e^{-\varphi_B}  : \mathfrak{m} \to \mathfrak{m}$, for $\varphi_B$ as in [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"}, is defined by $$\label{eq:expphi}
e^{-\varphi_B} = \sum_{k=0}^\infty \frac{(-1)^k}{k!} \varphi_B^k.$$
:::

::: proof
*Proof.* This follows from applying [@Tojo1996 Lemma 3.1] to $\mathop{\mathrm{Flag}}(n_1,\dots, n_d; n)$. ◻
:::

For the $d= 1$ case, i.e., $\mathop{\mathrm{Flag}}(k;n) = \mathop{\mathrm{Gr}}(k,n)$, it is straightforward to verify that $[B,X]_\mathfrak{m} = 0$ for all $B,X\in \mathfrak{m}$. So the expression for parallel transport in [\[eq:pt\]](#eq:pt){reference-type="eqref" reference="eq:pt"} reduces to $X(t) = Q \exp(tB) X$, which is the well-known expression for parallel transport on the Grassmannian [@EAS].
