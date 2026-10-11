---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-010-4-flag-manifolds-as-matrix-homogeneous-spaces
section_title: "Flag manifolds as matrix homogeneous spaces"
section_number: 4
pages: 9-16
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.98
---
[]{#sec:homo label="sec:homo"}

We will discuss three representations of the flag manifold as *matrix homogeneous spaces*, i.e., where a flag is represented as an equivalence class of matrices: $$\begin{aligned}
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\cong \mathop{\mathrm{O}}(n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr), \label{eq:homo1}\\
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\cong \mathop{\mathrm{SO}}(n) / \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr),\label{eq:homo2}\\
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\cong  \mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr).\label{eq:homo3}
\end{aligned}$$ The characterization [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"} is standard [@Monk1959; @Borel1991] and generalizes the well-known characterization of the Grassmannian as $\mathop{\mathrm{Gr}}(k,n) \cong \mathop{\mathrm{O}}(n)/\bigl(\mathop{\mathrm{O}}(k) \times \mathop{\mathrm{O}}(n-k)\bigr)$ whereas the characterization [\[eq:homo3\]](#eq:homo3){reference-type="eqref" reference="eq:homo3"} generalizes another well-known characterization of the Grassmannian as $\mathop{\mathrm{Gr}}(k,n) \cong \mathop{\mathrm{V}}(k,n)/\mathop{\mathrm{O}}(k)$.

Nevertheless, we will soon see that it is desirable to describe $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ as a homogeneous space $G/H$ where $G$ is a connected Lie group --- note that $\mathop{\mathrm{O}}(n)$ is not connected whereas $\mathop{\mathrm{V}}(n_d,n)$ is not a group, so [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"} and [\[eq:homo3\]](#eq:homo3){reference-type="eqref" reference="eq:homo3"} do not meet this criterion. With this in mind, we state and prove [\[eq:homo2\]](#eq:homo2){reference-type="eqref" reference="eq:homo2"} formally.

::: proposition
[]{#prop:equivalent definition of flag manifold label="prop:equivalent definition of flag manifold"} Let $0 < n_1< \dots < n_d < n$ be $d$ positive integers. The flag manifold $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ is diffeomorphic to the homogeneous space $$\mathop{\mathrm{SO}}(n) / \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr)$$ where $\mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr)$ is the subgroup of unit-determinant block diagonal matrices with orthogonal blocks, i.e., $$\begin{bsmallmatrix}
Q_1 & 0 & \dots & 0 \\
0 & Q_2 & \dots & 0\\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & Q_{d+1}
\end{bsmallmatrix} \in \mathop{\mathrm{O}}(n), \quad Q_i\in \mathop{\mathrm{O}}(n_i-n_{i-1}), \quad i=1,\dots, d+1, \quad \prod_{i=1}^{d+1} \det (Q_i) = 1.$$
:::

::: proof
*Proof.* We start with the characterization [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"}, i.e., in this proof we assume '$=$' in place of '$\cong$' in [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"}. We claim that the required diffeomorphism $\tau$ is given as in the commutative diagram below: $$\begin{tikzcd}
\mathop{\mathrm{SO}}(n) \arrow{r}{j} \arrow[swap]{d}{\pi'} & \mathop{\mathrm{O}}(n) \arrow{d}{\pi} \\
\mathop{\mathrm{SO}}(n) / \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n-n_d) \bigr) \arrow{r}{\tau} & \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) 
\end{tikzcd}$$ Here $j$ is the inclusion of $\mathop{\mathrm{SO}}(n)$ in $\mathop{\mathrm{O}}(n)$, $\pi$ and $\pi'$ the respective quotient maps, and $\tau$ the induced map. Since $$\mathop{\mathrm{SO}}(n)  \cap  \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots  \times \mathop{\mathrm{O}}(n-n_d) \bigr)=  \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n - n_{d}) \bigr),$$ $\tau$ is injective. To show that it is surjective, let $\{\mathbb{V}_i\}_{i=1}^d \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ be a flag represented by some $A\in \mathop{\mathrm{O}}(n)$, i.e., $\pi(A) = \{\mathbb{V}_i\}_{i=1}^d$. If $\det(A) = 1$, then we already have $\tau (\pi_1(A)) = \{\mathbb{V}_i\}_{i=1}^d$ by commutativity of the diagram. If $\det(A) = -1$, take any $A_1\in \mathop{\mathrm{O}}(n_1)$ with $\det(A_1)=-1$, set $$B = A \begin{bsmallmatrix}
A_1 & 0 &\cdots & 0 \\
0 & I_{n_2 - n_1} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & I_{n - n_d}
\end{bsmallmatrix} \in \mathop{\mathrm{SO}}(n),$$ and observe that $\tau (\pi_1(B)) = \pi (B) = \pi (A)$. ◻
:::

## Orthogonal coordinates for the flag manifold {#sec:ortho}

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

## Stiefel coordinates for the flag manifold {#sec:stief}

We next discuss the characterization of a flag manifold as a quotient of the Stiefel manifold [\[eq:homo3\]](#eq:homo3){reference-type="eqref" reference="eq:homo3"} and discuss its consequences. This characterization will give our coordinates of choice for use in our optimization algorithms (see Section [\[sec:gH\]](#sec:gH){reference-type="ref" reference="sec:gH"}).

::: proposition
[]{#prop:Stiefel label="prop:Stiefel"} Let $0 < n_1< \dots < n_d < n$ be $d$ positive integers. The flag manifold $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ is diffeomorphic to the homogeneous space $$\label{prop:Stiefel:eqn1}
\mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr)$$ where $\mathop{\mathrm{V}}(n_d,n)$ is the Stiefel manifold of orthonormal $n_d$-frames in $n$.
:::

::: proof
*Proof.* This follows from the standard characterization of $\mathop{\mathrm{V}}(n_d,n)$ is a homogeneous space of $O(n)$, $\mathop{\mathrm{V}}(n_d,n) \cong  \mathop{\mathrm{O}}(n)/\mathop{\mathrm{O}}(n-n_d)$, together with [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"}. ◻
:::

For the rest of this article, we will regard the Stiefel manifold $\mathop{\mathrm{V}}(k,n)$ as the set of all $n\times k$ matrices whose column vectors are orthonormal. With this identification, Proposition [\[prop:Stiefel\]](#prop:Stiefel){reference-type="ref" reference="prop:Stiefel"} allows us to represent a flag $\{ \mathbb{V}_i\}_{i=1}^d \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ by a matrix $Y =[y_1,\dots,y_{n_d}] \in \mathbb{R}^{n\times n_d}$ with orthonormal $y_1,\dots,y_{n_d} \in \mathbb{R}^n$ and where the first $n_i$ of them span the subspace $\mathbb{V}_i$, $i=1,\dots, d$. This representation is not unique but if $Y'\in \mathbb{R}^{n\times n_d}$ is another such matrix, then $$\label{eq:rep}
Y' = Y \begin{bsmallmatrix}
Q_1 & 0 & \dots & 0\\
0 & Q_2 &\dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &\dots & Q_{d}
\end{bsmallmatrix},
\quad Q_i \in \mathop{\mathrm{O}}(n_i - n_{i-1}), \quad i =1,\dots, d.$$ Hence $\{ \mathbb{V}_i\}_{i=1}^d \in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ may be represented by the equivalence class of matrices $$\label{eq:equiv2}
\llbracket Y \rrbracket= \left\lbrace
Y \begin{bsmallmatrix}
Q_1 & 0 & \dots & 0\\
0 & Q_2 &\dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &\dots & Q_d
\end{bsmallmatrix} \in \mathbb{R}^{n \times n_d}:
\begin{multlined}
Y\in \mathop{\mathrm{V}}(n_d,n), \;
\mathop{\mathrm{span}}\{y_1,\dots,y_{n_i}\} =  \mathbb{V}_i, \\
Q_i \in \mathop{\mathrm{O}}(n_i - n_{i-1}), \; i =1,\dots, d
\end{multlined}
\right\rbrace.$$ We will call such a representation *Stiefel coordinates* for the flag manifold.

In the following, for any $k < n$, we write $$I_{n,k} \coloneqq \begin{bmatrix}
I_{k} \\
0 
\end{bmatrix} \in \mathbb{R}^{n\times k},$$ i.e., the $n \times k$ matrix comprising the first $k$ columns of the $n \times n$ identity matrix $I_n$. Thus for any $A =[a_1,\dots, a_n] \in \mathbb{R}^{n \times n}$, $AI_{n,k} = [a_1,\dots,a_k] \in  \mathbb{R}^{n \times k}$ gives us the first $k$ columns of $A$.

For a flag $\{ \mathbb{V}_i\}_{i=1}^d$, it is easy to convert between its orthogonal coordinates, i.e., $\llbracket Q \rrbracket$ in [\[eq:equivalence class\]](#eq:equivalence class){reference-type="eqref" reference="eq:equivalence class"} with $Q\in \mathop{\mathrm{O}}(n)$, and its Stiefel coordinates, i.e., $\llbracket Y \rrbracket$ in [\[eq:equiv2\]](#eq:equiv2){reference-type="eqref" reference="eq:equiv2"} with $Y \in \mathop{\mathrm{V}}(n_d,n)$. Given $Q \in \mathop{\mathrm{O}}(n)$, one just takes its first $n_d$ columns to get $Y = QI_{n,n_d}$; note that $QI_{n,n_i}$ is automatically an orthonormal basis for the subspace $\mathbb{V}_i$, $i=1,\dots, d$. Given $Y \in \mathop{\mathrm{V}}(n_d,n)$, take any orthonormal basis $Y^\perp \in \mathop{\mathrm{V}}(n-n_d, n)$ of the orthogonal complement of $\mathop{\mathrm{im}}(Y)$ to get $Q = [Y, Y^\perp]\in \mathop{\mathrm{O}}(n)$.

We now derive expressions for tangent space, metric, arclength, geodesic, and parallel transport in Stiefel coordinates.

::: proposition
[]{#prop:tangent2a label="prop:tangent2a"} Let $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = \mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr)$ be represented by $Y\in \mathop{\mathrm{V}}(n_d, n)$. Its tangent space at $\llbracket Y \rrbracket$ is given by $$T_{\llbracket Y \rrbracket}\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) = \lbrace  [Y,Y^{\perp}] B I_{n,n_d} \in \mathbb{R}^{n \times n_d}: B\in \mathfrak{m}\rbrace,$$ where $Y^{\perp} \in \mathop{\mathrm{V}}(n-n_d,n)$ is such that $[Y,Y^{\perp}] \in \mathop{\mathrm{O}}(n)$ and $\mathfrak{m}$ is as in [\[eq:m\]](#eq:m){reference-type="eqref" reference="eq:m"}.
:::

::: proof
*Proof.* The calculation is straightforward and details can be found in [@NSP2006]. Essentially it follows from differentiating a curve $\tau(t)$ in $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ with $\tau(0) = \llbracket Y \rrbracket$ and noting that the tangent vector $\tau'(0)$ is perpendicular to $\mathfrak{h}$ in [\[eq:h\]](#eq:h){reference-type="eqref" reference="eq:h"}, whose orthogonal complement is precisely $\mathfrak{m}$. ◻
:::

The description of $T_{\llbracket Y \rrbracket}\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ in Proposition [\[prop:tangent2a\]](#prop:tangent2a){reference-type="ref" reference="prop:tangent2a"} is a parametric one (like the description of the unit circle as $\{(\cos \theta, \sin \theta) : \theta \in [0,2\pi)\}$). We may also derive an implicit description of $T_{\llbracket Y \rrbracket}\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ (like the description of the unit circle as $\{(x,y) : x^2 + y^2 = 1\}$).

::: corollary
[]{#prop:tangent2b label="prop:tangent2b"} Let $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) = \mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr)$ be represented by $Y\in \mathop{\mathrm{V}}(n_d, n)$. Let $Y$ be partition as $$Y = [Y_1,\dots, Y_d], \quad Y_i \in \mathop{\mathrm{V}}(n_i - n_{i-1},n), \quad i=1,\dots, d.$$ Then its tangent space at $\llbracket Y \rrbracket$ is given by $$\begin{gathered}
\label{eq:tangent space}
T_{\llbracket Y \rrbracket}\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) = \lbrace  [X_1,\dots,X_d]\in \mathbb{R}^{n\times n_d} : X_i\in \mathbb{R}^{n \times (n_i - n_{i-1})}, \\
Y_i^{\scriptscriptstyle\mathsf{T}}X_j + X_i^{\scriptscriptstyle\mathsf{T}}Y_j = 0,\; Y_i^{\scriptscriptstyle\mathsf{T}}X_i = 0,\; 1\le i, j \le d  \rbrace.
\end{gathered}$$ Equivalently, the matrix $[X_1,\dots, X_d]$ can be expressed as $$[X_1,\dots, X_d] = [Y_1,\dots,Y_d,Y^\perp] \begin{bsmallmatrix}
0 & B_{1,2} & \dots & B_{1,d} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0 & \dots & B_{2,d} \\
\vdots & \dots & \ddots & \vdots \\
-B_{1,d}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d}^{\scriptscriptstyle\mathsf{T}}& \dots & 0  \\
-B_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d+1}^{\scriptscriptstyle\mathsf{T}}& \dots & -B_{d,d+1}^{\scriptscriptstyle\mathsf{T}}
\end{bsmallmatrix},$$ where $Y^{\perp} \in \mathop{\mathrm{V}}(n-n_d,n)$ is such that $[Y,Y^{\perp}] \in \mathop{\mathrm{O}}(n)$ and $B_{ij}\in \mathbb{R}^{(n_i-n_{i-1})\times (n_j-n_{j-1})}$, $1\le i<j\le d+1$.
:::

::: proof
*Proof.* Since $[Y_1,\dots, Y_d] \in \mathop{\mathrm{V}}(n_d,n)$ and $Y_i \in \mathop{\mathrm{V}}(n_i - n_{i-1},n)$, the $Y_i$'s are characterized by $$\label{eq:tangent space2}
Y_i^{\scriptscriptstyle\mathsf{T}}Y_i = I_{n_i - n_{i-1}},\quad Y_i^{\scriptscriptstyle\mathsf{T}}Y_j = 0,\quad i\ne  j =1,\dots, d.$$ Differentiating [\[eq:tangent space2\]](#eq:tangent space2){reference-type="eqref" reference="eq:tangent space2"} gives us the first relation in [\[eq:tangent space\]](#eq:tangent space){reference-type="eqref" reference="eq:tangent space"}. On the other hand, by Proposition [\[prop:tangent2a\]](#prop:tangent2a){reference-type="ref" reference="prop:tangent2a"} we notice that a tangent vector in $T_{\llbracket Y \rrbracket}\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ is written as $[Y,Y^\perp] B I_{n,n_d}$ for some $B\in \mathfrak{m}$, from which we may easily verify the second relation in [\[eq:tangent space\]](#eq:tangent space){reference-type="eqref" reference="eq:tangent space"}. ◻
:::

Comparing Propositions [\[prop:tangent1\]](#prop:tangent1){reference-type="ref" reference="prop:tangent1"} and [\[prop:tangent2a\]](#prop:tangent2a){reference-type="ref" reference="prop:tangent2a"}, for a tangent vector $QB \in T_{\llbracket Q \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ in orthogonal coordinates $Q \in \mathop{\mathrm{O}}(n)$, its corresponding tangent vector in Stiefel coordinates $Y = Q I_{n,n_d} \in \mathop{\mathrm{V}}(n_d,n)$ is simply given by $QB I_{n,n_d} \in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$. Conversely, $[Y,Y^{\perp}] B I_{n,n_d} \in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ in Stiefel coordinates corresponds to $QB \in T_{\llbracket Q \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ in orthogonal coordinates where $Q = [Y,Y^{\perp}]$. Note that from the matrix $B I_{n,n_d}$, i.e., just the first $n_d$ columns of $B \in \mathfrak{m}$, the full matrix $B$ can be easily and uniquely recovered by its skew symmetry.

The straightforward translation between orthogonal and Stiefel coordinate representations of points and tangent vectors on a flag manifold allows us to immediately deduce analogues of Propositions [\[prop:metric\]](#prop:metric){reference-type="ref" reference="prop:metric"}, [\[prop:geodesics1\]](#prop:geodesics1){reference-type="ref" reference="prop:geodesics1"}, [\[prop:pt\]](#prop:pt){reference-type="ref" reference="prop:pt"}, and Corollary [\[cor:arc-length\]](#cor:arc-length){reference-type="ref" reference="cor:arc-length"}.

::: proposition
[]{#prop:metric2 label="prop:metric2"} The metric $g$ at a point $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) = \mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr)$ is given by $$\label{eq:g2}
g_{\llbracket Y \rrbracket}(W,Z) = \sum_{1\le i < j \le d+1} \mathop{\mathrm{tr}}(B_{ij}^{\scriptscriptstyle\mathsf{T}}C_{ij}),$$ where $W,Z\in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ are $$W = [Y,Y^\perp] \begin{bsmallmatrix}
0 & B_{1,2}  &\dots  &B_{1,d} \\
-B_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0   &\dots& B_{2,d} \\
\vdots & \vdots & \ddots  &\vdots\\
-B_{1,d}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d}^{\scriptscriptstyle\mathsf{T}}& \cdots  & 0\\
-B_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -B_{2,d+1}^{\scriptscriptstyle\mathsf{T}}&  \dots & -B_{d,d+1}^{\scriptscriptstyle\mathsf{T}}
\end{bsmallmatrix},\quad  Z = [Y,Y^\perp]\begin{bsmallmatrix}
0 & C_{1,2}  &\dots  &C_{1,d} \\
-C_{1,2}^{\scriptscriptstyle\mathsf{T}}& 0   &\dots& C_{2,d} \\
\vdots & \vdots & \ddots  &\vdots\\
-C_{1,d}^{\scriptscriptstyle\mathsf{T}}& -C_{2,d}^{\scriptscriptstyle\mathsf{T}}& \cdots  & 0\\
-C_{1,d+1}^{\scriptscriptstyle\mathsf{T}}& -C_{2,d+1}^{\scriptscriptstyle\mathsf{T}}&  \dots & -C_{d,d+1}^{\scriptscriptstyle\mathsf{T}}
\end{bsmallmatrix} \in \mathbb{R}^{n \times n_d}.$$
:::

::: proposition
[]{#prop:geodesic3a label="prop:geodesic3a"} Let $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)  = \mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr)$ and $g$ be the metric in [\[eq:g2\]](#eq:g2){reference-type="eqref" reference="eq:g2"}. Every geodesic $\gamma$ on $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ passing through $\llbracket Y \rrbracket$ takes the form $$\gamma(t) = \llbracket Y(t) \rrbracket= \left\lbrace
[Y,Y^\perp] \exp (tB) \begin{bsmallmatrix}
Q_1 & 0 & \dots & 0\\
0 & Q_2 &\dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &\dots & Q_d\\
0 & 0 & \dots & 0
\end{bsmallmatrix} \in  \mathop{\mathrm{V}}(n_d,n) : \begin{multlined} Q_i\in \mathop{\mathrm{O}}(n_i - n_{i-1}),\\ i=1,\dots, d \end{multlined}
\right\rbrace,$$ where $[Y,Y^\perp]\in \mathop{\mathrm{O}}(n)$ and $B\in \mathfrak{m}$. In particular, the arclength of $\gamma(t)$ is $$\lVert \gamma(t) \rVert =  t \Bigl[  \sum\nolimits_{1\le i<j \le d+1} \mathop{\mathrm{tr}}(B_{ij}^{\scriptscriptstyle\mathsf{T}}B_{ij}) \Bigr]^{1/2}.$$
:::

::: proposition
[]{#prop:pt2 label="prop:pt2"} Let $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ and $$[Y,Y^{\perp}] B I_{n,n_d}, \; [Y,Y^{\perp}] X I_{n,n_d} \in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n).$$ The parallel transport of $[Y,Y^{\perp}] X I_{n,n_d}$ along the geodesic $\llbracket[Y,Y^\perp] \exp (tB)I_{n,n_d}  \rrbracket$ is given by $$\label{eq:pt2}
X(t) = [Y,Y^\perp]  \exp(tB)  e^{-\varphi_{tB}} ( X ) I_{n,n_d},$$ with $e^{-\varphi_{tB}}$ defined as in [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} and [\[eq:expphi\]](#eq:expphi){reference-type="eqref" reference="eq:expphi"}.
:::

While is also straightforward to obtain analogues of Proposition [\[prop:geodesics2\]](#prop:geodesics2){reference-type="ref" reference="prop:geodesics2"} and [\[prop:geodist\]](#prop:geodist){reference-type="ref" reference="prop:geodist"} in Stiefel coordinates, we omit them as the expressions are more involved and we will not need them in the sequel.
