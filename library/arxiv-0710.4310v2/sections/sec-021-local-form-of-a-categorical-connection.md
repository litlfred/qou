---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-021-local-form-of-a-categorical-connection
section_title: "Local form of a categorical connection"
section_number: null
pages: 20-22
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#lform label="lform"}

Let ${\Gc=(\d\colon E \to G,\tr)}$ be some Lie crossed module, and let ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$ be the associated differential crossed module. Fix a smooth manifold $M$ and a smooth principal $G$-bundle $P \to M$, with a categorical $\Gc$-connection $(\w,m)$, where, as usual, $\w \in \A^1(P,\lg)$ and $m \in \A^2(P,\le)$.

The local form of the categorical $\Gc$-connection $(\w,m)$ is similar to the local form of a connection. Let $\{U_\a\}$ be an open covering of the manifold $M$. We can suppose that each $U_\a$ is contractible and that, for each $\a$ and $\b$, the intersection $U_\a \cap U_\b$ is contractible; see [@BT]. Therefore, for each $\a$, the restriction $P_\a$ of $P$ to $U_\a$ is trivial, and, in particular, it admits a section $f_\a\colon U_\a \to P_\a$. The local form of a categorical $\Gc$-connection is therefore given by the family of forms $\w_a=f_\a^*(\w)$ and $m_\a=f_\a^*(m)$.

For each $\a$, by the structure equation, the local curvature form $\W_\a=f_\a^*(\W)$ takes the form $$\W_\a=d \w_\a+\frac{1}{2} \w_\a\wedge^{\ad}\w_\a.$$ Locally, the Bianchi identity reads: $$d \W_\a+\w_\a\wedge^\ad \W_\a=0.$$ Analogously, from the 2-structure equation, locally in each $U_\a$, the 2-curvature 3-form $\M_\a=f_\a^*(\M)$ takes the form: $$\M_\a=d m_\a+\w_\a\wedge^{\tr}  m_\a,$$ and the 2-Bianchi identity reads: $$d \M_\a+\w_\a \wedge^{\tr} \M_\a=0.$$ These local expressions correspond to the formulae in [@B] when the fake curvature vanishes.

Let $\f_{\a,\b} \colon U_a \cap U_\b \to G$ be defined as $f_\a(x)\f_{\a,\b}(x)=f_\b(x)$, for each $x \in  U_\a \cap U_\b$. We have: $$\begin{aligned}
\label{x} \w_\b(X)&=\f_{\a,\b}^{-1} \w(X) \f_{\a,\b}+\f_{\a,\b} ^{-1} d \f_{\a,\b},\\
\label{y} \W_\b(X,Y)&=\f_{\a,\b}^{-1}  \W (X,Y)\f_{\a,\b}, 
\end{aligned}$$ for each $X,Y \in \X(M)$. Since both $m$ and $\M$ are $G$-equivariant and horizontal, it follows that for each $\a,\b$: $$\begin{aligned}
\label{z}
 m_\b(X,Y)&=\f_{\a,\b}^{-1} \tr  m_\a(X,Y),\\
 \M_\b(X,Y,Z)&=\f_{\a,\b}^{-1} \tr  \M_\a(X,Y,Z),
\end{aligned}$$ for each $X,Y,Z \in \X(M)$.

::: Lemma
Let $M$ be a smooth manifold. Let also ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module, and let ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$ be the associated differential crossed module. Suppose $\pi\colon P \to M$ is the trivial bundle $M \times G$. Given $m_0 \in \A^2(M,\le)$ and $\w_0 \in \A^1(M,\lg)$, such that $\d(m_0)=\W_0=d \w_0+\frac{1}{2} \w_0 \wedge^{\ad} \w_0$, there exists a categorical $\Gc$-connection $(\w,m)$ on $P$ such that its local form is $(\w_0,m_0)$.
:::

::: Proof
Let $\theta$ be the canonical $\lg$-valued left-invariant 1-form on $G$; see [\[wkl\]](#wkl){reference-type="ref" reference="wkl"}. Then $\w=g^{-1}\pi^*(\w_0)g+\theta$ is a connection 1-form on $M \times G$, and its local form, considering the section $f\colon M \to P$ such that, for each $x \in M$, $f(x)=(x,1_G)$, is $\w_0$. The 2-form $\pi^*(m_0)\in \A^2(P,\le)$ is horizontal. However, it is not $G$-equivariant. Therefore we define $m\in \A^2(M \times G,\le)$ as being such that, given $X,Y \in T_{(x,g)}P$, we have: $$m(X,Y)=g^{-1}\tr \pi^*(m_0)(X,Y),$$ where $g \in G$, $x \in M$ and $X,Y \in T_{(x,g)} M\times G$. This 2-form is obviously smooth and horizontal. Moreover, given $X,Y \in T_{(x,g)}P$ it follows that: $$\begin{aligned}
(R_h^*m)(X,Y)&=m(Xh,Yh)\\
             &=(gh)^{-1}\tr \pi^*(m_0)(Xh,Yh)\\
             &=h^{-1}g^{-1}\tr \pi^*(m_0)(X,Y)   \\
             &=h^{-1}\tr m(X,Y).
\end{aligned}$$ Therefore $m$ is $G$-equivariant. Let $\W$ be the curvature of $\w$. Then $\W(X,Y)=g^{-1} \pi^*(\W_0)(X,Y)g$, where as before $X,Y \in T_{(x,g)}P$. In particular it follows that $\W=\d(m)$.
:::

The following follows from the previous discussion.

::: Corollary
Let $M$ be a smooth manifold. Let also ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module, and let ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$ be the associated differential crossed module. Let $\{U_\a\}$ be an open cover of $M$, such that the restriction $P_\a$ of $P$ to $U_\a$ is the trivial bundle. Let also $f_\a \colon U_\a \to P_\a$ be local sections of $P$. Define $\f_{\a,\b} \colon U_\a \cap U_\b \to G$ as $f_\a(x)\f_{\a,\b}(x)=f_\b(x)$. Suppose that for each $\a$ we are given forms $\w_\a \in \A^1(U_\a,\lg)$ and $m_\a \in \A^2(U_\a,\le)$, satisfying $\d(m_\a)=\W_\a={{d\w_\a}+\frac{1}{2}\w_\a \wedge^{\ad} \w_\a}$. Moreover, suppose that for each $\a,\b$ with $U_\a \cap U_\b \neq \emptyset$ equations ([\[x\]](#x){reference-type="ref" reference="x"}) and ([\[z\]](#z){reference-type="ref" reference="z"}) are satisfied. There exists a unique categorical connection $(\w,m)$ on $P$ such that the forms $\w_\a$ and $m_\a$ are its local form.
:::

The trivial bundle $M \times G\to M$ always admits the trivial categorical connection, whose local form is given by the forms $\w_0=0$ and $m_0=0$. However, there exist several other examples for the trivial bundle. Let $A=\d(E)$, and let $\la$ be its Lie algebra. There exists a linear map $r\colon \la \to \le$ such that $\d \circ r=\id_\la$. Let $\w_0$ be any $\la$-valued 1-form on $M$. Let $\W_0$ be the curvature of $\w_0$ and define $m_0=r(\W_0)$. Then $(\w_0,m_0)$ is the local form of a categorical $\Gc$-connection on $M\times G$. In fact, let $B=\ker\d\subset E$. Therefore $B$ is closed under the action of $G$ on $E$, by the first condition of the definition of crossed modules; see definition [\[LCM\]](#LCM){reference-type="ref" reference="LCM"}. Let $\lb$ be the Lie algebra of $B$. Given any $\lb$-valued 2-form $\rho_0$ on $M$ then $\rho_0+m_0$ is the local form of a categorical $\Gc$-connection on $M\times G$.

It is not a trivial problem whether there always exists a categorical $\Gc$-connection on any principal $G$-bundle. This issue is very likely to depend on the topology of the manifold. The strategy of combining locally defined connection 1-forms $\w$ using a partition of unity cannot be carried through for the 2-forms $m$, since $\partial (m) = \W$, which is not ${\rm C}^\infty$-linear in $\w$.
