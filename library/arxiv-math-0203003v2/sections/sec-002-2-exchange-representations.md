---
doc_id: arxiv-math-0203003v2
doc_title: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002"
section_id: sec-002-2-exchange-representations
section_title: "Exchange Representations"
section_number: 2
pages: 4-8
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.965
doc_brief: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002 — 8 sections: Front matter; Introduction; Representations of Quantum Dynamic"
---
Let $\mathfrak{g}$ be a finite dimensional simple Lie algebra, and $\widehat{\mathfrak{g}}$ the corresponding affine Lie algebra. Let $q\in {\mathbb C}^*,|q|\ne 1$, and let $U_q(\widehat{\mathfrak{g}})$ be the associated quantum affine algebra (we will use the definition given in [@EFK98]). Let $\text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))$ be the category of finite dimensional (type 1) representations of $U_q(\widehat{\mathfrak{g}})$. For any $V \in \text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))$ and $z\in \text{$\mathbb{C}$}^*$ we can consider the shifted representation $V(z)$ where all the Chevalley generators act as before except for $e_0$ and $f_0$ which now act by $ze_0$ and $z^{-1}f_0$ respectively.

We will need the following theorem.

::: thm
[]{#mero label="mero"} (Kazhdan-Soibelman, [@KaSo95], Section 5) Let $V,W\in\text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))$, and $\mathbf R_{VW}(z)$ be the series obtained by evaluating the universal R-matrix in $V(z)\otimes W$. Then $\mathbf R_{VW}(z)$ is an analytic function near zero, that extends meromorphically to $\text{$\mathbb{C}$}$.
:::

We will give a new proof of this result (a bit simpler than the one in [@KaSo95]) in the appendix.

Now let $\mathfrak{h}$ denote a Cartan subalgebra of $\mathfrak{g}$, and $\widehat{\mathfrak{h}} = \mathfrak{h} \oplus \text{$\mathbb{C}$}$ the corresponding Cartan subalegbra in $\widehat{\mathfrak{g}}$. We denote the elements of $\widehat{\mathfrak{h}}^*$ by $\hat{\lambda} = (\lambda,k)$. Then we can define the fusion matrix $$J_{V,W}(u,\hat{\lambda}) : V(e^{-2\pi iu})\otimes W \to 
V(e^{-2\pi iu})\otimes W,$$ which is a formal power series in $e^{2\pi iu}$ with coefficients being ${\rm End}(V\otimes W)$-valued rational functions of $q^{(\hat\lambda,\alpha_i)}$, where $\alpha_i$ are the simple roots. (see [@EtSc98b] and also [@EFK98]). Namely, let $M_{\hat\lambda}$ be the Verma module over $U_q(\widehat{\mathfrak{g}})$ with highest weight $\hat\lambda$, and let $x_\lambda$ be its highest weight vector. Let $v\in V$ be a homogeneous vector, and $\Phi_{\hat\lambda}^v(u):
M_{\hat\lambda}\to M_{\hat\lambda-{\rm weight}(v)}\hat\otimes V(z)$ be the intertwining operator such that the matrix coefficient $(x^*_{\hat\lambda-{\rm
    weight}(v)},\Phi_{\hat\lambda}^v(z)x_\lambda)$ equals $v$ (here $x_{\hat\mu}^*$ is the lowest weight vector of $M_{\hat\mu}^*$). Then for any homogeneous vectors $v\in V$, $w\in W$, $$J_{V,W}(u,\hat\lambda):=(x^*_{\hat\lambda-{\rm
    weight}(v)-{\rm weight}(w)},(\Phi^v_{\hat\lambda-{\rm
    weight}(w)}(e^{-2\pi iu})\otimes
1)\Phi^w_{\hat\lambda}(1)x_\lambda).$$

Let ${\rm m}$ be the ratio of the squared lengths of long and short roots of $\mathfrak{g}$ (${\rm m}=1,2$ or $3$), and $h^\vee$ be the dual Coxeter number of $\mathfrak{g}$.

::: prop
[]{#p-adic label="p-adic"} The coefficients of the series $J_{V,W}(u,\hat\lambda)$ have an expansion into a power series in $p:=q^{-2{\rm m}(k+h^\vee)}$, and the sequence of these coefficients tends to $0$ in the p-adic norm.
:::

::: proof
*Proof.* This follows from the ABRR equation for the fusion matrix [@EtSc99] (which in our case is equivalent the qKZ equation of Frenkel and Reshetikhin [@FrRe92],[@EFK98]). ◻
:::

Proposition [\[p-adic\]](#p-adic){reference-type="ref" reference="p-adic"} implies that one may consider the fusion operator $J_{V,W}(\hat\lambda):=J_{V,W}(0,\hat\lambda)$, which is a power series in $p$.

::: prop
The series $J_{V,W}(\hat\lambda)$ is convergent when $|p|<<1$, and the sum of this series extends to a meromorphic function in the region $\lbrace{(\lambda,k):
|p|<1\rbrace}$.
:::

::: proof
*Proof.* This follows from the qKZ equation [@FrRe92],[@EFK98] and Theorem [\[mero\]](#mero){reference-type="ref" reference="mero"}. ◻
:::

Now define the exchange matrix with spectral parameter $$R_{V,W}(u,\hat{\lambda}) = J_{V,W}(u,\hat{\lambda})^{-1} 
\mathbf R_{W,V}^{21}(e^{2\pi i u}) J^{21}_{W,V}(-u,\hat{\lambda}).$$ It follows by the arguments sketched above that both $J_{V,W}(u,\hat\lambda)$ and $R_{V,W}(u,\hat\lambda)$ are meromorphic functions on ${\mathbb C}\times \mathfrak{U}$, where the open set $\mathfrak{U}\subset \widehat{\mathfrak{h}}^*$ is defined by the condition $|q^{-2{\rm m}(k+h^\vee)}|<1$. Moreover, these arguments actually show that the divisor of singularities of these functions is a union of hyperplanes of the form $u-bk=c$, $<x,\lambda>-bk=c$, where $b,c\in \text{$\mathbb{C}$}, x\in \mathfrak{h}$.

::: ex
[]{#ex:sln label="ex:sln"} Let $\mathfrak{g} = \mathfrak{sl}_n$. When $V = \text{$\mathbb{C}$}^n$, the formula for $R_{V,V}$ was obtained in [@Mou01].
:::

::: thm
[]{#thm:excisRm label="thm:excisRm"}

1.  [@EtSc99] The fusion matrix satisfies the dynamical twist equation $$\label{eq:dtwist}
    J_{V\otimes W,U}^{12,3}(\hat\lambda) J_{V,W}^{12}(\hat\lambda - h^{(3)}) = J_{V,W\otimes U}^{1,23}(\hat\lambda)J_{W,U}^{23}(\hat\lambda)$$

2.  [@EtSc98b] For any three finite dimensional representations $V_1,V_2,V_3$ of $U_q(\widehat{\mathfrak{g}})$ the exchange matrix satisfies the quantum dynamical Yang-Baxter equation $$\begin{aligned}
    \notag
    R_{V_1,V_2}^{12}(u_1-u_2,\hat\lambda- h^{(3)}) R_{V_1,V_3}^{13}(u_1-u_3,\hat\lambda) 
    R_{V_2,V_3}^{23}(u_2-u_3,\hat\lambda- h^{(1)})\\ \label{eq:qdybs1}
    = R_{V_2,V_3}^{23}(u_2-u_3,\hat\lambda) R_{V_1,V_3}^{13}(u_1-u_3,\hat\lambda- h^{(2)}) 
    R_{V_1,V_2}^{12}(u_1-u_2,\hat\lambda).
    \end{aligned}$$ In particular, for any $V\in \text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))$ the function $R_{V,V}(u,\hat\lambda)$ is a quantum dynamical R-matrix with spectral parameter and step 1.
:::

Strictly speaking, the last statement of the theorem contains an abuse of terminology, since $R_{V,V}$ is a meromorphic function not on $\text{$\mathbb{C}$}\times \widehat{\mathfrak{h}}^*$, but on its open subset $\text{$\mathbb{C}$}\times \mathfrak{U}$. In this paper, we will ignore this terminological problem.

Let $V$ be a finite dimensional representation of $U_q(\widehat{\mathfrak{g}})$ and define $R_V = R_{V,V}$. It follows from theorem [\[thm:excisRm\]](#thm:excisRm){reference-type="ref" reference="thm:excisRm"} that for any $W \in \text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))$, the pair $(W,R_{V,W}(u,\hat{\lambda}))$ is a representation of $R_{V}$. It is called the **exchange representation** of $R_V$ associated to $W$.

Now let us explain the main construction of this paper. Let $V \in \text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))$. Denote by $M$ the field of meromorphic functions on $\mathfrak{U}$ and let $M_V \subset M$ be the subfield of functions periodic under the weights of $V$. Set $\text{$\mathcal{C}$}(V) = \text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))\otimes_{\text{$\mathbb{C}$}} M_V$. It is easy to see then that the assignment $W\to (W,R_{V,W})$ provides an exact, faithful functor $\text{$\mathcal{F}$}_V : \text{$\mathcal{C}$}(V) \to \text{\bf Rep}_{\text{f}}(R_V)$.

One of our main results is the following theorem, which shows that for a nontrivial $V$, the category ${\mathcal C}(V)$ (which is obtained from $\text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{g}}))$ by extension of scalars) is a full subcategory in $\text{\bf Rep}_{\text{f}}(R_{V})$.

::: thm
[]{#main label="main"} The functor $\text{$\mathcal{F}$}_{V} : \text{$\mathcal{C}$}(V) \to \text{\bf Rep}_{\text{f}}(R_{V})$ is a tensor functor. Furthermore, if $V$ is nontrivial, then this functor is fully faithful.
:::

::: proof
*Proof.* We start with the following lemma.

::: lem
[]{#lem:tensoriso label="lem:tensoriso"} $$R_{V,W}^{12}(u,\hat\lambda - h^{(3)}) R_{V,U}^{13}(u,\hat\lambda) = J_{W,U}^{23}(\hat\lambda)^{-1}R_{V,W\otimes U}^{1,23}(u,\hat\lambda) J_{W,U}^{23}(\hat\lambda - h^{(1)})$$
:::

::: proof
*Proof.* To shorten the notation we will write $V[u]$ instead of $V(e^{-2\pi iu})$. Let $\mathbf R_{W,V}^{21}[u] = \text{$\mathcal{R}$}^{21}|_{W\otimes V[u]}$ (analogously for other pairs of indices). Then $$\begin{aligned}
\text{l.h.s.} = & J_{V,W}^{12}(u,\hat\lambda - h^{(3)})^{-1}\mathbf R^{21}_{W,V}[u] J_{W,V}^{21}(-u,\hat\lambda-h^{(3)}) J_{V,U}^{13}(u,\hat\lambda)^{-1}\mathbf R^{31}_{U,V}[u] J^{31}_{U,V}(-u,\hat\lambda)  = \\
& J_{V[u],W}^{12}(\hat\lambda - h^{(3)})^{-1}\mathbf R^{21}_{W,V}[u] \Big(J_{W,V[u]}^{21}(\hat\lambda-h^{(3)}) J_{V[u],U}^{13}(\hat\lambda)^{-1}\Big)\mathbf R^{31}_{U,V}[u] J^{31}_{U,V[u]}(\hat\lambda)  \stackrel{\eqref{eq:dtwist}}{=} \\ 
& J_{V[u],W}^{12}(\hat\lambda - h^{(3)})^{-1}\mathbf R^{21}_{W,V}[u] \Big(J_{W\otimes V[u],U}^{21,3}(\hat\lambda)^{-1} J_{W,V[u]\otimes U}^{2,13}(\hat\lambda)\Big)\mathbf R^{31}_{U,V}[u] J^{31}_{U,V[u]}(\hat\lambda) =\\  
& \Big(J_{V[u],W}^{12}(\hat\lambda - h^{(3)})^{-1} J_{V[u]\otimes W,U}^{12,3}(\hat\lambda)^{-1}\Big)\mathbf R^{21}_{W,V}[u]\mathbf R^{31}_{U,V}[u]\Big( J_{W,U\otimes V[u]}^{2,31}(\hat\lambda)  J^{31}_{U,V[u]}(\hat\lambda)\Big) \stackrel{\eqref{eq:dtwist}}{=} \\
& \Big(J_{W,U}^{23}(\hat\lambda)^{-1} J_{V[u],W\otimes U}^{1,23}(\hat\lambda)^{-1}\Big) \mathbf R^{21}_{W,V}[u]\mathbf R^{31}_{U,V}[u]\Big( J_{W\otimes U,V[u]}^{23,1}(\hat\lambda)  J^{23}_{W,U}(\hat\lambda-h^{(1)})\Big) = \text{r.h.s.} 
\end{aligned}$$ The fourth equality is clear while the last follows from the hexagon axiom for the R-matrix. ◻
:::

A more general version of this lemma in the non-affine situation is used in [@EtVa00].

Now let us prove that $\text{$\mathcal{F}$}$ is a tensor functor. To do this, define the tensor structure $\text{$\mathcal{F}$}_V(W)\odot \text{$\mathcal{F}$}_V(U) \to \text{$\mathcal{F}$}_V(W\otimes U)$ to be given by $$J_{W,U}(\hat{\lambda}) : (W,R_{V,W})\odot (U,R_{V,U}) \to (W\otimes U,R_{V,W\otimes U})$$ It follows from Lemma [\[lem:tensoriso\]](#lem:tensoriso){reference-type="ref" reference="lem:tensoriso"} that $J_{W,U}$ is a morphism (in fact an isomorphism) and from [\[eq:dtwist\]](#eq:dtwist){reference-type="eqref" reference="eq:dtwist"} that it satisfies the properties of a tensor structure on a functor, as required.

The rest of the section is dedicated to the proof of the full faithfulness of $\text{$\mathcal{F}$}$ in the case when $V$ is nontrivial.

Following the conventions of [@EFK98], set $L_W^+(z):=\mathbf
R_{W,V}^{21}(z)$.

::: lem
[]{#lem:M(W,U) label="lem:M(W,U)"} One has ${\rm Hom}_{U_q(\widehat{\mathfrak{g}})}(W,U) = \{ A\in \text{Hom}_{U_q(\widehat{\mathfrak{h}})}(W,U)$; $L^{+}_U(z)^{-1}(1\otimes A)L^{+}_W (z)$ is of zero weight in both components$\}$.
:::

::: proof
*Proof.* It is clear that the first space is a subspace in the second one. For the converse it is enough to prove that, if $A:W \to U$ is such that $L^{+}_U(z)^{-1}(1\otimes A)L^{+}_W (z)$ is of zero weight in both components, then $A \in \text{Hom}_{U_q(\widehat{\mathfrak{g}})}(W,U)$. To do this, recall that the universal R-matrix on modules with central charge $0$ can be written as $$\text{$\mathcal{R}$} = q^{\sum x_i\otimes x_i}\big(1 + \sum_{i\geq 0} (q_i - q_i^{-1}) e_i\otimes f_i +\dots \big)$$ where $x_i$ form an orthonormal basis for $\mathfrak{h}$ and the remaining terms are in $U_q(\widehat{\mathfrak{n}}_+)\otimes U_q(\widehat{\mathfrak{n}}_-)$ and correspond to other weights. This means that for nontrivial $V$, the condition that the expression $L^{+}_U(z)^{-1}(1\otimes
A)L^{+}_W (z)$ is of zero weight in both components implies that $A$ is of zero weight, and $f_i|_V\otimes[e_i,A] = 0 \,\forall\,i\ge 0$ (one just needs to look at the terms corresponding to simple roots in the expression of the universal R-matrix). It follows that $[e_i,A]=0$. Hence $A$ is an interwiner over $U_q(\widehat{\mathfrak{b}}_+)$. But it is proved in Proposition 4.1.3 of [@KaSo95] that the images of $U_q(\widehat{\mathfrak{b}}_+)$ and $U_q(\widehat{\mathfrak{g}})$ in the endomorphism algebra of any finite dimensional $U_q(\widehat{\mathfrak{g}})$-module are the same. Hence, $A$ is an intertwiner over the whole $U_q(\widehat{\mathfrak{g}})$, as desired. ◻
:::

Let $\text{$\mathcal{M}$}(W,U):={\rm Hom}_{U_q(\widehat{\mathfrak{g}})}(W,U)\otimes_{\text{$\mathbb{C}$}} M_V$ be the space of morphisms between $W$ and $U$ in the category $\text{$\mathcal{C}$}(V)$, and let $\widetilde{\text{$\mathcal{M}$}}(W,U):={\text{$\mathcal{M}$}}(W,U)\otimes_{M_V}M$. Lemma [\[lem:M(W,U)\]](#lem:M(W,U)){reference-type="ref" reference="lem:M(W,U)"} implies that $\widetilde{\text{$\mathcal{M}$}}(W,U)$ is the space of solutions over $M$ of the system of linear algebraic equations in finitely many variables (entries of $A$), expressing the condition that $L^{+}_U(z)^{-1}(1\otimes A)L^{+}_W (z)$ is of zero weight in both components.

Now let ${\text{$\mathcal{N}$}}(W,U)={\rm Hom}_{\text{\bf Rep}_{\text{f}}(R_V)}({\text{$\mathcal{F}$}}(W),{\text{$\mathcal{F}$}}(U))$. Below we will show that the space $\widetilde{\text{$\mathcal{N}$}}(W,U):={\text{$\mathcal{N}$}}(W,U)\otimes_{M_V}M$ is contained in the space of solutions over $M$ of a **deformation** of this system of linear algebraic equations. This will imply that ${\rm dim}{\text{$\mathcal{N}$}}(W,U)\le {\rm dim}{\text{$\mathcal{M}$}}(W,U)$, which immediately implies that the injective map ${\text{$\mathcal{M}$}}(W,U)\to {\text{$\mathcal{N}$}}(W,U)$ defined by ${\text{$\mathcal{F}$}}$ is actually an isomorphism, i.e., ${\text{$\mathcal{F}$}}$ is fully faithful.

To do this, we need the following lemma.

::: lem
[]{#lem:M'(W,U) label="lem:M'(W,U)"} Let $L_W, L_U$ be the exchange operators $R_{V,W}, R_{V,U}$ and $\widetilde{\text{$\mathcal{M}$}}\,'(W,U) = \{ A(\hat\lambda) \in \text{Hom}_{U_q(\widehat{\mathfrak{h}})}(W,U)\otimes_{\text{$\mathbb{C}$}}M; L_U(u,\hat\lambda)^{-1}(1\otimes A(\hat\lambda))L_W (u,\hat\lambda)$ is of zero weight in both components$\}$. Then the natural map $\xi:{\text{$\mathcal{N}$}}(W,U)\otimes_{M_V}M \to \widetilde{\text{$\mathcal{M}$}}\,'(W,U)$ is injective.
:::

::: proof
*Proof.* We need to show that any $M_V$-linearly independent set $\{a_1, \dots, a_m\} \subset {\text{$\mathcal{N}$}}(W,U)$ is also linearly independent over $M$. Assume it is false and take a counterexample with the smallest length. We can assume that $a_m = g_1 a_1 + \dots + g_{m-1} a_{m-1}$ with $g_i \in M$ but not all of them in $M_V$. Then $$\begin{aligned}
a_m(\hat\lambda - h^{(1)}) & = L_U(u,\hat\lambda)^{-1}(1\otimes a_m(\hat\lambda))L_W (u,\hat\lambda)\\ & = \sum g_i(\hat\lambda) L_U(u,\hat\lambda)^{-1}(1\otimes a_i(\hat\lambda))L_W (u,\hat\lambda) = \sum g_i(\hat\lambda) a_i(\hat\lambda -h^{(1)})
\end{aligned}$$ Let $v \in V$ be homogeneous of weight $\mu$. Then, applying the last equality to $v\otimes {\rm Id}$, we have $$a_m(\hat\lambda-\mu) = \sum g_i(\hat\lambda)a_i(\hat\lambda -\mu) \quad\Leftrightarrow\quad a_m(\hat\lambda) = \sum g_i(\hat\lambda+\mu)a_i(\hat\lambda)$$ Hence, for some $\mu$, $\sum \big(g_i(\hat\lambda)-g_i(\hat\lambda+\mu)\big)a_i(\hat\lambda)$ is a non-trivial (since not all $g_i$ are in $M_V$) vanishing linear combination of an even smaller length. Contradiction. ◻
:::

Now it remains to prove that $L_W(u,\hat\lambda)$ is a deformation of $L_W^{+}(z)$, where $z=e^{2\pi iu}$.

Let $\kappa = k+h^\vee{}$ and $p=q^{-2{\rm m}\kappa}$. We will write $k \to \infty$ to mean $p \to 0$ keeping $q$ fixed.

::: lem
[]{#lem:klimit label="lem:klimit"} Let $J_{V,W}(\lambda)$ be the fusion matrix corresponding to the the "finite dimensional" quantum group $U_q(\mathfrak{g})$. Then $\lim_{k\to \infty} J_{V,W}(u,\hat\lambda) = 
J_{V,W}(\lambda)$.
:::

::: proof
*Proof.* Let $v$ and $w$ be homogeneous vectors in $V$ and $W$ respectively and consider the correlation function [@EFK98] $\psi(z,\hat\lambda) = z^{\Delta}J_{V,W}(u,\hat\lambda)(v\otimes
w)$ where $\Delta$ depends on the weights of $v$ and $w$ and on $\hat\lambda$. It is easy to see that $$\psi(z,\hat\lambda) = z^{\Delta}\sum_{m\geq 0} \psi_m(\hat\lambda)z^m$$ and that $\psi_0(\hat\lambda) = J_{V,W}(\lambda)(v\otimes w)$. Furthermore, $\psi$ satisfies the q-Knizhnik-Zamolodchikov equations, from which we get $$\psi(pz,\hat\lambda) = \mathbf R_{W,V}^{21}(pz) q_{(2)}^{\Lambda} \psi(z,\hat\lambda)$$ where $\Lambda$ depends only on $\lambda$ and the weights of $v,w$ (not on $k$). Writing $\mathbf R_{W,V}^{21}(z) = \sum_{j\geq 0} \mathbf R^{21}_j z^j$ we find $$p^{\Delta} \sum_{m\geq 0}\psi_m(\hat\lambda) p^m z^m = \Big(\sum_{j\geq 0} \mathbf R^{21}_j p^j z^j\Big) q^{\Lambda}_{(2)}\Big(\sum_{i\geq 0} \psi_i(\hat\lambda)z^i\Big)$$ Actually $p^{\Delta}$ is some constant $c$ depending only on $q,\lambda$ and the weights of $v,w$. We collect the term in $z^l$ in both sides to get $$(cp^l - \mathbf R_0^{21}q^{\Lambda}_{(2)}) \psi_l = \sum_{m=1}^l \mathbf R^{21}_m p^m q^{\Lambda}_{(2)} \psi_{l-m}$$ from where we conclude by induction that $\psi_l \to 0$ as $k \to \infty$ for all $l>1$, as stated. ◻
:::

Now assume that $|q|<1$ and let $\lambda \to -\infty$ mean ${\rm
  Re}(\lambda,\alpha_i) \to -\infty$, where $\alpha_i$ are the simple roots. Then, by [@EtVa00], $J_{V,W}(\lambda) \to 1$ as $\lambda \to
-\infty$, and we conclude that $L_W(u,\hat\lambda) \to
\mathbf R_{W,V}^{21}(z)$ and, therefore, $L_W(u,\hat\lambda)$ is a deformation of $L_W^{+}(z)$. One can proceed analogously for $|q|>1$. Theorem [\[main\]](#main){reference-type="ref" reference="main"} is proved. ◻
:::
