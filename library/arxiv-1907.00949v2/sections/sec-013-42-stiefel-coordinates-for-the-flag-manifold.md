---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-013-42-stiefel-coordinates-for-the-flag-manifold
section_title: "Stiefel coordinates for the flag manifold"
section_number: 4.2
pages: 14-16
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.963
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:stief label="sec:stief"}

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
