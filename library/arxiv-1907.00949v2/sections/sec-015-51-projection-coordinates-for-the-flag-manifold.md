---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-015-51-projection-coordinates-for-the-flag-manifold
section_title: "Projection coordinates for the flag manifold"
section_number: 5.1
pages: 17-18
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.942
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:proj label="sec:proj"}

We will construct our first analogue of [\[eq:epsGr\]](#eq:epsGr){reference-type="eqref" reference="eq:epsGr"} for the flag manifold. Let $$\label{eq:eps}
\varepsilon : \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) \to \mathbb{R}^{nd\times nd}, \quad
\{\mathbb{V}_i\}_{i=1}^d \mapsto \mathop{\mathrm{diag}}(V_1V_1^{\scriptscriptstyle\mathsf{T}}, \dots, V_d V_d^{\scriptscriptstyle\mathsf{T}}),$$ where $V_i \in \mathbb{R}^{n\times n_i}$ is an orthonormal basis of $\mathbb{V}_i$, $i=1,\dots, d$, and the image is a block-diagonal matrix in $\mathbb{R}^{nd \times nd}$ with $d$ blocks $V_1V_1^{\scriptscriptstyle\mathsf{T}}, \dots, V_d V_d^{\scriptscriptstyle\mathsf{T}}\in \mathbb{R}^{n \times n}$. In fact, the map in [\[eq:eps\]](#eq:eps){reference-type="eqref" reference="eq:eps"} is essentially the map in [\[eq:j\]](#eq:j){reference-type="eqref" reference="eq:j"} that we used to establish Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"}[\[it:cls1\]](#it:cls1){reference-type="eqref" reference="it:cls1"} except that we identify the Grassmannians with sets of projection matrices as in [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"}.

::: proposition
[]{#prop:representation of flags label="prop:representation of flags"} The flag manifold $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ is diffeomorphic to $$\label{eq:Pflag}
\{P = \mathop{\mathrm{diag}}(P_1,\dots,P_d)\in \mathbb{R}^{nd\times nd}: P_i^2 = P_i = P_i^{\scriptscriptstyle\mathsf{T}},\; \mathop{\mathrm{tr}}(P_i) = n_i, \; P_j P_i = P_i, \; i<j \}.$$
:::

::: proof
*Proof.* One may check that $\varepsilon$ in [\[eq:eps\]](#eq:eps){reference-type="eqref" reference="eq:eps"} has its image in contained in the set [\[eq:Pflag\]](#eq:Pflag){reference-type="eqref" reference="eq:Pflag"}; and the map that takes $P= \mathop{\mathrm{diag}}(P_1,\dots,P_d)$ to the flag $\{\mathop{\mathrm{im}}(P_i)\}_{i=1}^d \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ is its inverse. ◻
:::

We will call the representation in Proposition [\[prop:representation of flags\]](#prop:representation of flags){reference-type="ref" reference="prop:representation of flags"} *projection coordinates* for the flag manifold. Unlike the orthogonal and Stiefel coordinates introduced earlier, which are not unique, projection coordinates are unique. Let $\{\mathbb{V}_i\}_{i=1}^d \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ with

1.  []{#it:o label="it:o"} orthogonal coordinates $\llbracket Q \rrbracket$ for some $Q  \in \mathop{\mathrm{O}}(n)$;

2.  []{#it:s label="it:s"} Stiefel coordiantes $\llbracket Y \rrbracket$ for some $Y \in \mathop{\mathrm{V}}(n_d, n)$;

3.  []{#it:p label="it:p"} projection coordinates $P$ as in [\[eq:Pflag\]](#eq:Pflag){reference-type="eqref" reference="eq:Pflag"}.

We have seen how we may easily convert between orthogonal and Stiefel coordinates after [\[eq:equiv2\]](#eq:equiv2){reference-type="eqref" reference="eq:equiv2"}, we now see how they may be interchanged with projection coordinates just as easily:

-   Given $Q=[q_1,\dots,q_n] \in \mathop{\mathrm{O}}(n)$, let $Q_i = [q_1,\dots, q_{n_i}] \in \mathop{\mathrm{V}}(n_i, n)$; then $P_i = Q_i Q_i^{\scriptscriptstyle\mathsf{T}}$, $i = 1,\dots,d$.

-   Given $Y = [y_1,\dots,y_{n_d}] \in \mathop{\mathrm{V}}(n_d, n)$, let $Y_i = [y_1,\dots, y_{n_i}] \in \mathop{\mathrm{V}}(n_i, n)$; then $P_i = Y_i Y_i^{\scriptscriptstyle\mathsf{T}}$, $i = 1,\dots,d$.

-   Given $P =\mathop{\mathrm{diag}}(P_1,\dots,P_d)$, let $y_1,\dots, y_{n_{i}}$ be an orthonormal basis of $\mathop{\mathrm{im}}(P_i)$; then $Y_i= [y_1,\dots, y_{n_i}] \in \mathop{\mathrm{V}}(n_i, n)$, $i=1,\dots, d$.

-   As above but appending an orthonormal basis $y_{n_d+1},\dots, y_{n}$ of $\mathop{\mathrm{im}}(P_d)^\perp$ gives us $Q = [y_1,\dots, y_{n_d}, y_{n_d+1},\dots, y_{n}] \in \mathop{\mathrm{O}}(n)$.

As is the case for the Grassmannian, the flag manifold has several extrinsic coordinates systems with which differential geometric objects and operations have closed-form analytic expressions and where one coordinate representation can be transformed to another with relative ease. This flexibility to switch between coordinate systems can be exploited in computations but as we will see next, it can also be exploited in deriving the requisite analytic expressions.

::: proposition
[]{#prop:tangent2 label="prop:tangent2"} Let $P = \mathop{\mathrm{diag}}(P_1,\dots,P_d) \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ as represented in [\[eq:Pflag\]](#eq:Pflag){reference-type="eqref" reference="eq:Pflag"}. Then the tangent space is given by $$\begin{gathered}
\label{eq:tangent2}
T_P\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) = \lbrace Z = \mathop{\mathrm{diag}}(Z_1,\dots,Z_d) \in \mathbb{R}^{nd\times nd} :
Z_i P_i + P_i Z_i= Z_i = Z_i^{\scriptscriptstyle\mathsf{T}},\\  \mathop{\mathrm{tr}}(Z_i) = 0, \; Z_j P_i + P_j Z_i = Z_i,\; i<j, \; i,j=1,\dots, d. \rbrace
\end{gathered}$$
:::

::: proof
*Proof.* Let $\gamma(t)$ be a curve in $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ as characterized by [\[eq:Pflag\]](#eq:Pflag){reference-type="eqref" reference="eq:Pflag"}, i.e., $\gamma : (-1, 1) \to \mathbb{R}^{nd\times nd}$, $t \mapsto  \mathop{\mathrm{diag}}\bigl(P_1(t),\dots, P_d(t)\bigr)$ where $$\label{eq: curve in flag1}
P_i(t)^2 = P_i(t), \; P_i(t)^{\scriptscriptstyle\mathsf{T}}= P_i(t),\; \mathop{\mathrm{tr}}(P_i(t)) = n_i,\; P_j(t)P_i(t) = P_i(t),\; i<j, \; i,j=1,\dots,d,$$ for all $t\in (-1,1)$. Taking derivatives of these relations at $t = 0$ gives the required description. ◻
:::

Again the ease of translation from orthogonal and Stiefel coordinates to projection coordinates yields counterparts of Proposition [\[prop:metric\]](#prop:metric){reference-type="ref" reference="prop:metric"}--[\[prop:pt\]](#prop:pt){reference-type="ref" reference="prop:pt"} readily. We will just provide expressions for geodesic and parallel transport as examples.

::: proposition
[]{#prop:geodesics3 label="prop:geodesics3"} Let $P = \mathop{\mathrm{diag}}(P_1,\dots,P_d) \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ be as represented in [\[eq:Pflag\]](#eq:Pflag){reference-type="eqref" reference="eq:Pflag"} and $Z = \mathop{\mathrm{diag}}(Z_1,\dots,Z_d)\in T_P\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ be as represented in [\[eq:tangent2\]](#eq:tangent2){reference-type="eqref" reference="eq:tangent2"}. Then there exist $Y \in \mathop{\mathrm{V}}(n_d, n)$ and skew-symmetric $B \in \mathbb{R}^{n \times n}$ such that for $Y_i = YI_{n,n_i}$, $B_i =BI_{n,n_i} \in \mathbb{R}^{n \times n_i}$, $$\label{eq:pyb}
P_i = Y_i Y_i^{\scriptscriptstyle\mathsf{T}}, \quad Z_i = Y_i B_i^{\scriptscriptstyle\mathsf{T}}+ B_iY_i^{\scriptscriptstyle\mathsf{T}}, \quad i=1,\dots,d;$$ and a geodesic $P(t)$ passing through $P$ in the direction $Z$ takes the form $$\label{eq:geo3}
\{\mathop{\mathrm{diag}}\bigl(P_1(t),\dots, P_d(t)\bigr) \in \mathbb{R}^{nd \times nd} : P_i(t) = Y_i(t) Y_i(t)^{\scriptscriptstyle\mathsf{T}}, \; Y_i(t) = [Y,Y^\perp] \exp(tB)I_{n,n_i}\}.$$
:::

::: proof
*Proof.* The matrix $Y$ is just $P$ in Stiefel coordinates and may be obtained from [\[it:p\]](#it:p){reference-type="eqref" reference="it:p"}$\to$[\[it:s\]](#it:s){reference-type="eqref" reference="it:s"} above. By Proposition [\[prop:geodesic3a\]](#prop:geodesic3a){reference-type="ref" reference="prop:geodesic3a"}, in Stiefel coordinates, the geodesic through $\llbracket Y \rrbracket$ in direction $[Y,Y^{\perp}] B I_{n,n_d}$ is $$\llbracket[Y,Y^{\perp}]  \exp(tB) I_{n,n_d} \rrbracket.$$ By [\[it:s\]](#it:s){reference-type="eqref" reference="it:s"}$\to$[\[it:p\]](#it:p){reference-type="eqref" reference="it:p"}, $Y$ and $P$ are related by $P_i = Y_iY_i^{\scriptscriptstyle\mathsf{T}}$, $i=1,\dots,d$, which upon differentiation gives $Z_i = Y_i B_i^{\scriptscriptstyle\mathsf{T}}+ B_i Y_i^{\scriptscriptstyle\mathsf{T}}$. The required expression [\[eq:geo3\]](#eq:geo3){reference-type="eqref" reference="eq:geo3"} then follows. ◻
:::

The observant reader might have noticed that $B_{d+1}$ does not appear in [\[eq:pyb\]](#eq:pyb){reference-type="eqref" reference="eq:pyb"} --- the reason is that since $B$ is skew-symmetric, $B_{d+1}$ is uniquely determined by $B_1,\dots, B_d$.

::: proposition
[]{#prop:pt1 label="prop:pt1"} Let $P$, $Z$, $Y$, $B$, and $P(t)$ be as in Proposition [\[prop:geodesics3\]](#prop:geodesics3){reference-type="ref" reference="prop:geodesics3"}. Let $Y^\perp \in \mathop{\mathrm{V}}(n-n_d, n)$ be such that $[Y, Y^\perp] \in \mathop{\mathrm{O}}(n)$ and set $$\label{eq:geo4}
Y_i(t)=[Y, Y^\perp] \exp(tB)I_{n,n_i}, \quad X_i(t) = [Y, Y^\perp] \exp(tB)  e^{-\varphi_{tB}} ( X ) I_{n,n_i},  \quad i=1,\dots, d.$$ Then the parallel transport of the tangent vector $Z$ along the geodesic $P(t)$ is given by $$\label{eq:pt3}
Z(t) = \mathop{\mathrm{diag}}\bigl(Z_1(t),\dots, Z_d(t)\bigr),\quad Z_i(t) = Y_i(t) X_i(t)^{\scriptscriptstyle\mathsf{T}}+ X_i(t) Y_i(t)^{\scriptscriptstyle\mathsf{T}},\quad i=1,\dots, d.$$
:::

::: proof
*Proof.* As in the proof of Proposition [\[prop:geodesics3\]](#prop:geodesics3){reference-type="ref" reference="prop:geodesics3"}, we obtain the corresponding projection coordinates $P = \mathop{\mathrm{diag}}(P_1,\dots, P_d)$, $P_i = Y_i Y_i^{\scriptscriptstyle\mathsf{T}}$, $Y_i = YI_{n,n_i}$, $i=1,\dots, d$. Differentiating these relations give a tangent vector $Z = \mathop{\mathrm{diag}}(Z_1,\dots, Z_d)\in T_P \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ in projection coordinates as $$Z_i = Y_i X_i^{\scriptscriptstyle\mathsf{T}}+ X_iY_i^{\scriptscriptstyle\mathsf{T}},\quad i=1,\dots, d,$$ where $X\in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ is the expression of the same tangent vector in Stiefel coordinates as in Proposition [\[prop:tangent2a\]](#prop:tangent2a){reference-type="ref" reference="prop:tangent2a"} and $X_i = XI_{n,n_i}$, $i=1,\dots, d$. The required expressions [\[eq:geo4\]](#eq:geo4){reference-type="eqref" reference="eq:geo4"} and [\[eq:pt3\]](#eq:pt3){reference-type="eqref" reference="eq:pt3"} then follow from the expression [\[eq:pt2\]](#eq:pt2){reference-type="eqref" reference="eq:pt2"} for parallel transport in terms of Stiefel coordinates $Y$. ◻
:::
