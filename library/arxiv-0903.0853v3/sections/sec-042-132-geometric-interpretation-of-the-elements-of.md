---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-042-132-geometric-interpretation-of-the-elements-of
section_title: "Geometric interpretation of the elements of $H^1({\mathbf{E}_{q}};\Lambda_I)$"
section_number: 13.2
pages: 65-70
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.982
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:geometricinterpretation label="subsection:geometricinterpretation"}

We need some results on regularly separated subsets of the euclidean space ${\mathbf R}^2$. We first recall some definitions.

If $X \subset {\mathbf R}^n$ is a closed subset of the euclidean space ${\mathbf R}^n$, we denote by ${\mathscr{E}}(X)$ the algebra []{#not53 label="not53"} of $\mathcal{C}^{\infty}$ functions in Whitney sense on $X$ (*cf.* [@Ma1]).

We recall the *Whitney extension theorem*: if $Y \subset X$ are closed subset of ${\mathbf R}^n$, the restriction map ${\mathscr{E}}(X) \rightarrow {\mathscr{E}}(Y)$ is surjective.

Let $A,B$ be two closed sets of ${\mathbf R}^n$; we define the following maps: $$\alpha: f \in {\mathscr{E}}(A \cup B) \mapsto
(f_{\vert A},f_{\vert B}) \in {\mathscr{E}}(A) \oplus {\mathscr{E}}(B),$$ $$\beta:  (f,g)\in {\mathscr{E}}(A) \oplus {\mathscr{E}}(B) \mapsto
f_{\vert A\cap B} - g_{\vert A\cap B} \in {\mathscr{E}}(A \cap B),$$ and we consider the sequence:

$$0 \rightarrow {\mathscr{E}}(A\cup B) \overset{\alpha}{\rightarrow}
{\mathscr{E}}(A) \oplus {\mathscr{E}}(B) \overset{\beta}{\rightarrow}
{\mathscr{E}}(A \cap B)\rightarrow 0.$$

::: defi
Two subsets $A$ and $B$ of the euclidean space ${\mathbf R}^n$ are regularly separated if the above sequence is exact.
:::

The following result is due to Łojasiewicz (*cf.* [@Ma1]).

::: prop
[]{#prop:regsep label="prop:regsep"} Let $A$,$B$ be two closed subsets $A$ and $B$ of the euclidean space ${\mathbf R}^n$; the following conditions are equivalent:

-   $A$ and $B$ are regularly separated;

-   $A \cap B = \emptyset$ or for all $x_0\in A\cap B$, there exists a neighborhood $U$ of $x_0$ and constants $C > 0$, $\lambda > 0$ such that for all $x\in U$: $$d(x,A) + d(x,B) \geq C d(x,A \cap B)^{\lambda};$$

-   $A \cap B = \emptyset$ or for all $x_0\in A\cap B$, there exists a neighborhood $U$ of $x_0$ and a constant $C'>0$ such that for all $x\in A\cap U$: $$d(x,B) \geq C' d(x,A \cap B)^{\lambda}.$$
:::

If we can choose $\lambda = 1$ in the above condition(s), we will say that the closed subsets $A$ and $B$ are *transverse*. Transversality is in fact a *local* condition.

::: lemm
[]{#lemm:transverse label="lemm:transverse"} Let $K_1$, $K_2$ be two closed small parallelograms of ${\mathbf{E}_{q}}$. The sets $p^{-1}(K_1)$ and $p^{-1}(K_2)$ are transverse.
:::

::: proof
*Proof.* Using the map $p_0$ (introduced at the beginning of [\[subsection:glue\]](#subsection:glue){reference-type="ref" reference="subsection:glue"}), we set: $$\begin{aligned}
A := p^{-1}(K_1) \subset {\mathbf C}^*
& \text{~and~} 
A_0 := p_0^{-1}(A) = (p \circ p_0)^{-1}(K_1) \subset {\mathbf R}^2, \\
B := p^{-1}(K_2) \subset {\mathbf C}^*
& \text{~and~} 
B_0 := p_0^{-1}(B) = (p \circ p_0)^{-1}(K_2) \subset {\mathbf R}^2.
\end{aligned}$$ Since $K_1$ and $K_2$ are small parallelograms, both $A_0$ and $B_0$ are formed of a family of disjoint rectangles, that is to say: $$A_0 = \bigcup_{m,n\in{\mathbf Z}} A_{m,n} \text{~and~} B_0 =\bigcup_{m,n\in{\mathbf Z}} B_{m,n},$$ where the families $(A_{m,n})_{m,n\in{\mathbf Z}}$, $(B_{m,n})_{m,n\in{\mathbf Z}}$ are such that $d(A_{m,n}, A_{m',n'})\ge 3/4$ and $d(B_{m,n},B_{m',n'})\ge 3/4$ for any $(m',n') \not= (m,n)$. We only need to deal with the case when $A  \cap B \not= \emptyset$, that is, when there exists $(m,n)$, $(m',n')$ such that $A_{m,n} \cap B_{m',n'}\not=\emptyset$.

Consider the function $f$ defined over ${\mathbf C}^* \setminus A \cap B$ by $$f(x)=\frac{d(x,A)+d(x,B)}{d(x,A\cap B)}$$ and observe that $f$ is $q$-invariant; therefore, it is enough to prove the following statement: for any $x_0 \in  A \cap B$ such that $1 < \left |x_0 \right |\le  \left |q \right |$, there exists an open disk $D(x_0,r)$, $r>0$, and a constant $C>0$ such that $f(x)\ge C$ for all $x\in D(x_0,r) \setminus (A \cap B)$.

On the other hand, the mapping $p_0$ is a local diffeomorphism from ${\mathbf R}^2$ onto ${\mathbf C}^*$ inducing a local equivalence between the natural metrics. Therefore the proof of the lemma boils down to the transversality between $A_0$ and $B_0$, which is merely deduced from the transversality of each pair of rectangles $(A_{m,n},B_{m',n'})$ of the euclidean plane. ◻
:::

Let $\gamma \in H^1({\mathbf{E}_{q}};\Lambda_I)$, we can represent it by an element $g\in Z^1({\mathfrak{U}};\Lambda_I)$ where ${\mathfrak{U}}$ is a good open covering of ${\mathbf{E}_{q}}$. We can suppose that all the parallelograms of the covering are small. We will associate to $g$ a germ of fibered space $\bigl(M_g,\pi,({\mathbf C},0)\bigr)$. We will see that if we change the choice of $g$, then these germs of linear fibered space correspond by a canonical isomorphism. This construction mimicks a construction of [@MR] inspired by an idea of Malgrange (*cf.* [@Ma2]), it is a central point for the proof of one of our main results.\
Let $g \in Z^1({\mathfrak{U}};\Lambda_I)$. We interpret the $g_i$ as germs of holomorphic functions on the germ of $q^{-{\mathbf N}}$-invariant open set defined by $U_i$, that is the germ of $p^{-1}(U_i) \cap D$ ($D$ being an open disk centered at the origin). For sake of simplicity we will denote also by $U_i$ this germ. We consider the disjoint sum $\displaystyle \prod_{i\in I} U_i \times {\mathbf C}^n$ and (using representatives of germs) we identify the points $(x,Y) \in U_i \times {\mathbf C}^n$ and $(x,Z) \in U_j \times {\mathbf C}^n$ if $x \in U_{ij}$ and $Z =g_{ij}(x)(Y)$ (we verify that we have an equivalence relation using the cocycle condition), we denote the quotient by ${\mathbf M}_g$. If $x = 0$, $g_i(0)$ is the identity of ${\mathbf C}^n$ therefore the quotient ${\mathbf M}_g$ is a germ of topological space along $\{0\} \times {\mathbf C}^n$. []{#not54 label="not54"}

::: lemm
-   The projections $U_i \times {\mathbf C}^n \rightarrow U_i$ induce a germ of continuous fibration $\pi: {\mathbf M}_g\rightarrow ({\mathbf C},0)$, the fiber $\pi^{-1}(0)$ is identified with $({\mathbf C}^n,0)$.

-   The germ $\overset{\bullet}{\mathbf M}_g := {\mathbf M}_g \setminus \pi^{-1}(0)$ admits a natural structure of germ of complex manifold of dimension $n+1$, it is the unique structure such that the natural injections $(U_i \setminus \{0\}) \times {\mathbf C}^n \rightarrow \overset{\bullet}{\mathbf M}_g$ are holomorphic. The restriction of $\pi$ to $\overset{\bullet}{\mathbf M}_g$ is holomorphic.
:::

The proof of the lemma is easy.

::: lemm
There exists on ${\mathbf M}_g$ a unique structure of germ of differentiable manifold ($\mathcal{C}^{\infty}$) such that the natural injections $(U_i\setminus \{0\}) \times {\mathbf C}^n \rightarrow \overset{\bullet}{\mathbf M}_g$ are $\mathcal{C}^{\infty}$ (in Whitney sense). The induced structure on $\overset{\bullet}{\mathbf M}_g$ is the underlying structure of the holomorphic structure on $\overset{\bullet}{\mathbf M}_g$. The map $\pi$ is $\mathcal{C}^{\infty}$ of rank one, $\bigl({\mathbf M}_g,\pi,({\mathbf C},0)\bigr)$ is a germ of vector bundle.
:::

::: proof
*Proof.* This lemma is the central point. The proof uses the Whitney extension theorem and the notion of regularly separated closed sets (*cf.* above).

We replace the good open covering $(U_i)_{i\in I}$ by a good closed covering $(V_i)_{i\in I}$ with $V_i\subset U_i$. We interpret the $V_i$ as $q^{-{\mathbf N}}$-invariant germs of compact sets $p^{-1}(V_i) \cap \bar D \subset {\mathbf C}^*$ (we take $\bar D :=\bar D(r)$, $r>0$). The differentiable functions on $V_i \times {\mathbf C}^n$ are by definition the $\mathcal{C}^{\infty}$ functions in Whitney sense. We can built a germ of set as a quotient of $\displaystyle \prod_{i\in I} V_i \times {\mathbf C}^n$ using $g$ as above, the natural map from this quotient to ${\mathbf M}_g$ is an homeorphism and we can identify these two sets. If we consider a representative of the germ ${\mathbf M}_g$ and $x \in {\mathbf C}^*$ sufficiently small, there exists a structure of differentiable manifold along $\pi^{-1}(x)$ and it satisfies all the conditions. Let $Y_0\in{\mathbf C}^n$, we set $m_0=(0,Y_0)$ and we denote by ${\mathscr{E}}_{m_0}$ the ring of germs of real functions on ${\mathbf M}_g$ represented by germs at $m_0\in V_i \times {\mathbf C}^n$ of functions $f_i$ compatible with glueing applications, that is $f_j \circ g_{ji}=f_i$.

We will prove that each cordinate $y_h$ ($h =1,\ldots,n$) on ${\mathbf C}^n$ extends in an element $\eta_h$ of ${\mathscr{E}}_{m_0}$. It suffices to consider $y_1$.

We start with $i\in I$ We extend $y_1$ in a $\mathcal{C}^{\infty}$ function $f_i$ on $V_i \times {\mathbf C}^n$ (we can choose $f_i = y_1$).

Let $j \in I$, $j \neq i$. The glueing map $g_{ij}$ gives a $\mathcal{C}^{\infty}$ function $h_{j}$ on $V_{ij} \times {\mathbf C}^n \subset V_j \times {\mathbf C}^n$, using Whitney extension theorem, we can extend it in a $\mathcal{C}^{\infty}$ function $f_j$ on $V_j\times{\mathbf C}^n$.

Let $k \in I$, $k \neq i,j$. The glueing maps $g_{ik}$ and $g_{jk}$ give functions $h_{ik}$ and $h_{jk}$ respectively on $V_{ik} \times {\mathbf C}^n \subset V_k \times {\mathbf C}^n$ and $V_{jk} \times {\mathbf C}^n \subset V_k \times {\mathbf C}^n$; these functions coincide on $V_{ijk} \times {\mathbf C}^n \subset V_k \times {\mathbf C}^n$. The closed sets $V_{ik} \times {\mathbf C}^n$ and $V_{jk} \times {\mathbf C}^n$ are regularly separated ($V_{ik}$ and $V_{jk}$ are, as subsets of ${\mathbf{E}_{q}}$, closed parallelograms and we can apply lemma [\[lemm:transverse\]](#lemm:transverse){reference-type="ref" reference="lemm:transverse"}), therefore the $\mathcal{C}^{\infty}$ functions $h_{ik}$ and $h_{jk}$ define a $\mathcal{C}^{\infty}$ function $h_k$ on $(V_{ik} \cup V_{jk})\times {\mathbf C}^n \subset V_k \times {\mathbf C}^n$, using Whitney extension theorem, we can extend it in a $\mathcal{C}^{\infty}$ function $f_k$ on $V_k \times {\mathbf C}^n$.

Let $h \in I$, $h \neq i,j,k$, then $V_{ih} \cap  V_{jh} \cap  V_{kh} =V_{ijkh} =\emptyset$ and we can do as in the preceding step, using moreover the fact that to be $\mathcal{C}^{\infty}$ is a local property.

We can end the proof along the same lines. ◻
:::

The $n$ functions $\eta_1,\ldots,\eta_m\in {\mathscr{E}}_{m_0}$ and $\pi$, interpreted as an element of ${\mathscr{E}}_{m_0}$, define a system of local coordinates on ${\mathbf M}_g$ in a neighborhood of $m_0$; an element of ${\mathscr{E}}_{m_0}$ is a $\mathcal{C}^{\infty}$ function of these coordinates. Therefore ${\mathbf M}_g$ admits a structure of differentiable manifold, this structure is fixed on $\overset{\bullet}{\mathbf M}_g$, therefore unique.

::: prop
[]{#prop:manifold label="prop:manifold"}

-   The germ of differentiable manifold ${\mathbf M}_g$ admits a unique structure of germ of complex analytic manifold extending the complex analytic structure of $\overset{\bullet}{\mathbf M}_g$. For this structure the map $\pi$ is holomorphic and its rank is one, $\bigl({\mathbf M}_g,\pi,({\mathbf C},0)\bigr)$ is a germ of holomorphic vector bundle. []{#not55 label="not55"}

-   We consider the formal completion $\widehat{\mathbf M}_g$ of ${\mathbf M}_g$ along $\pi^{-1}(0)$ (for the holomorphic structure defined by (i)) and the formal completion $\hat{\mathbf F}$ of $({\mathbf C},0)\times{\mathbf C}^n$ along $\{0\}\times{\mathbf C}^n$. We denote by $\hat\pi: \widehat{\mathbf M}_g \rightarrow \bigl(({\mathbf C},0){\hat\vert}\{0\}\bigr)$ the completion of $\pi$ and by $\hat\pi_0: \hat{\mathbf F} \rightarrow  \bigl(({\mathbf C},0){\hat\vert}\{0\}\bigr)$ the natural projection. The formal vector bundle $\Bigl(\widehat{\mathbf M}_g,\hat\pi,\bigl(({\mathbf C},0){\hat\vert}\{0\}\bigr)\Bigr)$ is naturally isomorphic to the formal vector bundle $\bigl(\hat{\mathbf F},\hat\pi_0,(({\mathbf C},0){\hat\vert}\{0\})\bigr)$.
:::

::: proof
*Proof.* The proof of (i) is based on the Newlander-Niremberg integrability theorem, it is similar, mutatis mutandis to a proof in [@MR], page 77. The proof of (ii) is easy (the $\hat g_{ij}$ are equal to identity). ◻
:::

If $g,g'$ are two representatives of $\gamma$, the complex analytic manifolds ${\mathbf M}_g$ and ${\mathbf M}_{g'}$ are isomorphic (*cf.* [@MR], page 77)

## The formal trivialisation of the elements of $H^1({\mathbf{E}_{q}};\Lambda_I)$ and the fundamental isomorphism {#subsection:theformaltrivialisation}

Using the geometric interpretation of the cocycles of $Z^1({\mathfrak{U}};\Lambda_I)$ we will build a map: $$Z^1({\mathfrak{U}};\Lambda_I) \rightarrow  {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$$ defined up to composition on the right by an element of ${\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$. Hence we will get a map: $$H^1({\mathbf{E}_{q}};\Lambda_I) \rightarrow
{\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$$ and we will verify that it inverses the natural map: $${\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)
\rightarrow H^1({\mathbf{E}_{q}};\Lambda_I).$$

We consider the germ of trivial bundle $({\mathbf C},0) \times{\mathbf C}^n,\pi_0,({\mathbf C},0)$. We choose a holomorphic trivialisation $H$ of the germ of fiber bundle $\bigl({\mathbf M}_g,\pi,({\mathbf C},0)\bigr)$: $\pi_0\circ H = \pi$ ($H$ is defined up to composition on the right by an element of ${\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$). From the proposition [\[prop:manifold\]](#prop:manifold){reference-type="ref" reference="prop:manifold"} (ii) and $H$ we get an *automorphism* $\hat\varphi$ of the formal vector bundle $\bigl(\hat{\mathbf F},\hat\pi_0,({\mathbf C}{\hat\vert}\{0\}\bigr)$. We can interpet $\hat\varphi$ as an element of ${\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$, this element is well defined up to the choice of $H$, that is up to composition on the left by an element of ${\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$. Hence $\hat{\varphi}^{-1}$ is defined up to composition on the right by an element of ${\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$.\
The map: $$Z^1({\mathfrak{U}};\Lambda_I) \rightarrow
{\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$$ induced by $g\mapsto \hat\varphi^{-1}$ induces a map: $$H^1({\mathbf{E}_{q}};\Lambda_I) \rightarrow
{\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr).$$ We will verify that this map is the inverse of the natural map: $${\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)
\rightarrow H^1({\mathbf{E}_{q}};\Lambda_I).$$

From the natural injections $(U_i,0) \times {\mathbf C}^n \rightarrow M_g$ ($i\in I$) and the trivialisation $H$, we get automorphisms of the vector bundles $\bigl((U_i,0) \times {\mathbf C}^n \rightarrow (U_i,0)\bigr)$, that we can interpret as elements $\varphi_i \in \Gamma\bigl(U_i;{\text{GL}}_n({\mathscr{A}})\bigr)$ compatible with the glueing maps $g_{ij}$, *i.e.* $\varphi_i=\varphi_j\circ g_{ji}$. We have: $$g_{ij} = \varphi_i^{-1} \circ \varphi_j =
\varphi_i^{-1} \circ (\varphi_j^{-1})^{-1}\
\text{~and~} \partial(\varphi_i^{-1}) = (g_{ij}).$$ The element $\hat \varphi_i \in {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$ is independant of $i\in I$; we will denote it by $\hat\varphi$.\
We have $(\varphi_i^{-1}) \in {\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})\bigr)$ (remember that this space of cochains was defined in subsection [\[subsection:glue\]](#subsection:glue){reference-type="ref" reference="subsection:glue"}). The coboundary of $(\varphi_i^{-1})$ is $g$ and its natural image in ${\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$ is $\hat\varphi^{-1}$. This ends the proof of our contention.\
It is possible to do the same constructions replacing ${\text{GL}}_n({\mathbf C})$ by an algebraic subgroup (vector bundles are replaced by vector bundles admitting $G$ as structure group). We leave the details to the reader.

::: theo
[]{#theo:firstqMalgrangeSibuya label="theo:firstqMalgrangeSibuya"} Let $G$ be an algebraic subgroup of ${\text{GL}}_n({\mathbf C})$. The natural maps: $${\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)
\rightarrow H^1({\mathbf{E}_{q}};\Lambda_I),$$ $$G\bigl({{\mathbf C}[[z]]}\bigr)/ G\bigl({{\mathbf C}\{z\}}\bigr)\rightarrow H^1({\mathbf{E}_{q}};\Lambda_I^G)$$ are bijective.$\Box$
:::
