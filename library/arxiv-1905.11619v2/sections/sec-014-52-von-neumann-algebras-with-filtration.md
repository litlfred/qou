---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-014-52-von-neumann-algebras-with-filtration
section_title: "Von Neumann algebras with filtration"
section_number: 5.2
pages: 19-23
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.944
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
We fix again $(M, \tau)$ a finite von Neumann algebra with $(\Phi_t)_{t \geq 0} = (\exp(-t \Delta))_{t \geq 0}$ a quantum Markov semi-group. Let $$\partial: \mathcal{A}\rightarrow L_2(M)_\nabla: a \mapsto a \otimes \Omega_\tau$$ be the derivation of Corollary [\[Cor=Derivation\]](#Cor=Derivation){reference-type="ref" reference="Cor=Derivation"}. We shall assume that $\Delta$ satisfies certain properties that are close to being a length function.

::: dfn
We say that $\Delta$ is **filtered** if it has a compact resolvent and for every eigenvalue $\lambda$ of $\Delta$ there exists a (necessarily finite dimensional) subspace $\mathcal{A}(\lambda) \subseteq \mathcal{A}$ such that $\mathcal{A}(\lambda)\Omega_\tau$ equals the eigenspace of $\Delta$ at eigenvalue $\lambda \geq 0$. Moreover, let $\lambda_n, n \in \mathbb{N}$ be an increasing enumeration of the eigenvalues of $\Delta$, and we assume the spaces $\mathcal{A}(\lambda_n), n \in \mathbb{N}$, to be filtered in the sense that $$\label{Eqn=Filter}
        \bigoplus_{k=0}^{\infty} \mathcal{A}(\lambda_{k})=\mathcal{A}\quad \text{and} \quad \mathcal{A}(\lambda_n) \mathcal{A}(\lambda_m) \subseteq  \bigoplus_{k=0}^{m+n} \mathcal{A}(\lambda_{k}) \quad \text{for all }n,m\in \mathbb{N},$$ where $\bigoplus$ means the algebraic direct sum.
:::

Suppose now that $\Delta$ has a compact resolvent with a complete set of eigenvectors $(e_i)_i$ in $\mathcal A$ which is an orthonormal basis in $L^2(M)$ (for example if $\Delta$ is filtered this holds). Then since it is also a linear basis for $\mathcal{A}$, we can define the map $S$ by $(e_i)_i$ and $\partial$ as in [\[Eqn=S\]](#Eqn=S){reference-type="eqref" reference="Eqn=S"}. Observe that if $e_i \in \mathcal{A}(\lambda_{n})$, then $\|\partial(e_i)\|^2 = \langle \Delta(e_i),e_i\rangle = \lambda_{n}$. Using this, it is easy to see that $$\label{Eqn=S2}
    S(a) = {\lambda_n^{-\frac{1}{2}}}{\partial(a)}, \quad \text{for all }a\in \mathcal{A}(\lambda_n) \text{ and all eigenvalues }\lambda_n.$$ In particular, the map $S$ does not depend on the choice of $(e_i)_i$.

::: lem
[]{#Lem=AO label="Lem=AO"} Suppose that $\Delta$ has a compact resolvent with a complete set of eigenvectors in $\mathcal{A}$. Then the map $S$ in [\[Eqn=S2\]](#Eqn=S2){reference-type="eqref" reference="Eqn=S2"} is an isometry and hence satisfies Assumption 2.
:::

::: proof
*Proof.* By definition, $S$ is given by eigenvectors $(e_i)_i$. Then we have, $$\begin{split}
    \langle  S(e_i), S(e_j) \rangle  = &
    \Vert \partial(e_i) \Vert^{-1} \Vert \partial(e_j) \Vert^{-1}   \langle \partial(e_i), \partial(e_j) \rangle =
    \Vert \partial(e_i) \Vert^{-1} \Vert \partial(e_j) \Vert^{-1}   \langle \Delta^{\frac{1}{2}} e_i, \Delta^{\frac{1}{2}} e_j \rangle = \delta_{i,j}.
    \end{split}$$ So $S$ is an isometry. ◻
:::

::: lem
[]{#Lem=filtered label="Lem=filtered"} Suppose that $\Delta$ is filtered, then in fact we have $\mathcal{A}(\lambda_m)\mathcal{A}(\lambda_n) \subset \bigoplus_{k= \vert m - n \vert}^{m+n} \mathcal{A}(\lambda_k)$.
:::

::: proof
*Proof.* As $\Delta(x^\ast) = \Delta(x)^\ast$ for $x \in \mathcal{A}$, the spaces $\mathcal{A}(\lambda)$ are self-adjoint. Now take $x \in \mathcal{A}(\lambda_m)$, $y \in \mathcal{A}(\lambda_n)$ and $z \in \mathcal{A}(\lambda_k)$. Assume that $m > n$ and that $k <  m - n$. By assumption we find that $y^\ast z \in \bigoplus_{l=0}^{n+k} \mathcal{A}(\lambda_{l})$. As $n+k < m$ this shows that $0 = \langle y^\ast z \Omega_\tau, x \Omega_\tau \rangle = \langle z \Omega_\tau, y x \Omega_\tau \rangle$. So $yx$ is orthogonal to $\mathcal{A}(\lambda_k)$. The same holds for $xy$, which yields the lemma. ◻
:::

::: example
Let $\Lambda$ be a discrete finitely generated group and let $L: \Lambda \rightarrow \mathbb{N}$ be the length function given by the graph distance to the identity in the Cayley graph of $\Lambda$. Set $\Delta$ to be the closure of $\gamma \mapsto L(\gamma) \gamma$ as an unbounded operator on $\ell_2(\Lambda)$. Suppose that $L$ is conditionally positive definite so that $$Q(\xi) = \sum_{\gamma \in \Gamma}  L(\gamma)  \Vert \xi(\gamma ) \Vert^2 = \langle \Delta^{\frac{1}{2}} \xi, \Delta^{\frac{1}{2}} \xi\rangle$$ is a quantum Dirichlet form (see [@CiprianiSauvageot]), i.e. the generator of a quantum Markov semi-group. Then $\Delta$ is easily seen to be filtered.
:::

::: rmk
[]{#Rmk=FilteredExample label="Rmk=FilteredExample"} Let $\Gamma_q(H_{\mathbb{R}})$ be the $q$-Gaussian algebra for $-1 < q < 1$ with the Ornstein-Uhlenbeck semi-group $e^{-t \Delta}$, see Section [\[Sect=Orhnstein-Uhlenbeck\]](#Sect=Orhnstein-Uhlenbeck){reference-type="ref" reference="Sect=Orhnstein-Uhlenbeck"}. Then it follows from the Wick product formula of Lemma [\[Lem=WickProduct\]](#Lem=WickProduct){reference-type="ref" reference="Lem=WickProduct"} that $\Delta$ is filtered.
:::

::: dfn
We say that $\Delta$ has **subexponential growth** if it has a complete set of eigenvalues $\lambda_0 < \lambda_1 < \lambda_2 < \ldots$ for which $$\label{Eqn=Subexponential}
    \lim_{n\rightarrow \infty} \frac{\lambda_{n+1}}{\lambda_n} = 1.$$
:::

::: rmk
Subexponential growth of a generator of a quantum Markov semi-group should be compared to the amenability results obtained in [@CiprianiSauvageot] and [@CaspersGradient Appendix]. These results show that often one cannot expect a growth on the eigenvalues that is more than linear and so in particular [\[Eqn=Subexponential\]](#Eqn=Subexponential){reference-type="eqref" reference="Eqn=Subexponential"} holds.
:::

::: thm
[]{#Thm=Compact label="Thm=Compact"} Let $M$ be a finite von Neumann algebra and let $(\Phi_t)_{t \geq 0} = (\exp(-t \Delta))_{t \geq 0}$ be a quantum Markov semi-group such that $\Delta$ is filtered with subexponential growth. Let $S$ be as in [\[Eqn=S2\]](#Eqn=S2){reference-type="eqref" reference="Eqn=S2"}. Then for every $x,y \in \mathcal{A}$ the operator $T_{x,y}$ in [\[Eqn=Txy\]](#Eqn=Txy){reference-type="eqref" reference="Eqn=Txy"} is compact.
:::

::: proof
*Proof.* Fix $x,y \in \bigoplus_{k = 0}^K \mathcal{A}(\lambda_k)$ for some $K \in \mathbb{N}$. For each eigenvalue $\lambda$, let $P_{\lambda}$ be the orthogonal projection onto $\mathcal{A}(\lambda) \Omega_\tau$ and we also regard it as a map $\mathcal{A}\to \mathcal{A}(\lambda)$. Only in this proof, we will use the notation $\|a\|_\infty$ for the operator norm for $a\in \mathcal{A}$. Our first goal is to prove $\|T_{x,y}P_{\lambda_n}\| \to 0$ as $n \to \infty$. For this, we have only to prove that $\|T_{x,y} (a_n) \|  \to 0$ as $n\to \infty$, where $(a_n)_n$ is any sequence such that $a_n\in \mathcal{A}(\lambda_n)$ and $\|a_n\Omega_\tau\|=1$ for all $n\in \mathbb{N}$.

Take such a sequence $(a_n)_n$ and fix $n\in \mathbb{N}$. Then since $xa_n y\in \bigoplus_{k=-2K}^{2K} \mathcal{A}(\lambda_{n + k})$ by Lemma [\[Lem=filtered\]](#Lem=filtered){reference-type="ref" reference="Lem=filtered"} (where $\mathcal{A}(l)=0$ if $l<0$), one has $xa_ny = \sum_{k=-2K}^{2K}P_{\lambda_{n + k}}(xa_ny)$ (where $P_l=0$ if $l<0$), so that $$S(xa_ny) = \sum_{k=-2K}^{2K}{\lambda_{n + k}^{-\frac{1}{2}}}\partial(P_{\lambda_{n + k}}(xa_ny)) .$$ Using this, we can write $$T_{x,y}(a_n) =  x S(a_n) y - S(x a_n y) =  \lambda_{n}^{-\frac{1}{2}}{x \partial(a_n) y} -
 \sum_{k=-2K}^{2K}\lambda_{n + k}^{-\frac{1}{2}}\partial(P_{\lambda_{n + k}}(xa_ny) )$$ and further using $\partial(xa_ny) = \sum_{k=-2K}^{2K}\partial(P_{\lambda_{n + k}}(xa_ny))$, this translates into $$\label{Eqn=VStep}
 T_{x,y}(a_n)
 =  \lambda_{n}^{-\frac{1}{2}} \left(  x \partial(a_n) y  -
 \partial(xa_ny)  \right)  + \sum_{k=-2K}^{2K}(\lambda_{n}^{-\frac{1}{2}}- \lambda_{n + k}^{-\frac{1}{2}})\partial(P_{\lambda_{n + k}}(xa_ny)) .$$ We will show that the first and the second term on the right hand side converges to $0$ as $n \to \infty$.

We see the second term. Observe that for each $-2K \leqslant k\leqslant 2K$, $$\begin{aligned}
    \|\partial(P_{\lambda_{n + k}}(xa_ny))\|
    =  \|\Delta^{\frac{1}{2}}(P_{\lambda_{n + k}}(xa_ny))\|
    = \lambda_{n + k}^{\frac{1}{2}} \|P_{\lambda_{n + k}}(xa_ny)\|
    \leqslant \lambda_{n + k}^{\frac{1}{2}} \|x\|_\infty \|y\|_\infty.
\end{aligned}$$ The subexponential growth condition then shows that for any such $k$, $$\begin{aligned}
    \|(\lambda_{n}^{-\frac{1}{2}}- \lambda_{n + k}^{-\frac{1}{2}})\partial(P_{\lambda_{n + k}}(xa_ny))\|
    \leqslant   \lambda_{n +k}^{\frac{1}{2}}|\lambda_{n}^{-\frac{1}{2}}- \lambda_{n + k}^{-\frac{1}{2}}|\|x\|_\infty\|y\|_\infty \to 0
\end{aligned}$$ as $n\to \infty$. This finishes the case of the second term.

We next see the first term. By using the Leibniz rule, our term is $$\label{Eqn=RemainderTerm}
 \lambda_{n}^{-\frac{1}{2}}\left( x \partial(a_n) y - \partial(x a_n y) \right)
 =
 -\lambda_{n}^{-\frac{1}{2}}\left(   \partial(x)  a_n y + x a_n \partial(y) \right).$$ To estimate this term we firstly find $$\Vert \partial(x)  a_n y \Vert^2 = \Vert x  \otimes_\nabla a_n y \Omega_\tau \Vert^2  \leqslant \Vert \Gamma(x, x) \Vert_\infty \Vert  a_n \Omega_\tau \Vert^2 \Vert y \Vert^2_\infty = \Vert \Gamma(x, x)  \Vert_\infty  \Vert y \Vert^2_\infty,$$ hence, as $n\to \infty$, $$\label{Eqn=ConvergenceTwo}
 \lambda_{n}^{-\frac{1}{2}}  \Vert \partial(x)  a_n y \Vert \leqslant  \lambda_{n}^{-\frac{1}{2}} \Vert \Gamma(x, x)  \Vert^{\frac{1}{2}}_\infty  \Vert y \Vert_\infty \rightarrow 0.$$ This shows that the first summand on the right hand side of [\[Eqn=RemainderTerm\]](#Eqn=RemainderTerm){reference-type="eqref" reference="Eqn=RemainderTerm"} converges to 0. For the second summand, we first observe a couple of preliminary estimates. Using the equation $a_ny = \sum_{k=-K}^K P_{\lambda_{n+k}}(a_ny)$ by Lemma [\[Lem=filtered\]](#Lem=filtered){reference-type="ref" reference="Lem=filtered"} (where $P_l=0$ if $l<0$), we have $$\begin{aligned}
    \Vert ( \Delta(a_n ) y   - \Delta(a_n y)) \Omega_\tau \Vert^2
    &= \left\Vert \sum_{k = - K}^K \lambda_{n } P_{\lambda_{n + k}} (a_n y) - \sum_{k = - K}^K \lambda_{n + k} P_{\lambda_{n + k}} (a_n y)   \right\Vert^2 \\
    &=  \sum_{k = - K}^K |\lambda_{n}- \lambda_{n+k}|^2\left\Vert P_{\lambda_{n + k}} (a_n y)\right\Vert^2 \\
    &\leqslant \sum_{k = - K}^K |\lambda_{n}- \lambda_{n+k}|^2\left\Vert y\right\Vert^2_\infty,
\end{aligned}$$ so that by combining with the subexponential growth condition, as $n \rightarrow \infty$, $$\label{Eqn=Lim1}
    \lambda_{n}^{-1} \Vert ( \Delta(a_n ) y   - \Delta(a_n y)) \Omega_\tau \Vert \rightarrow 0.$$ Secondly, as $\Delta$ is self adjoint, $$\label{Eqn=Lim2}
\lambda_{n}^{-1} \tau(  \Delta(y^\ast a_n^\ast a_n)  y) = \lambda_{n}^{-1} \tau(  y^\ast a_n^\ast a_n  \Delta(y))=
\sum_{k=0}^K \frac{\lambda_k}{\lambda_{n}} \tau(       y^\ast a_n^\ast a_n  P_{\lambda_k}(y)) \to 0,$$ as $n\to \infty$, where we used the estimate for each summand as $$\begin{split}
 \frac{\lambda_k}{\lambda_{n}} |\tau(y^\ast a_n^\ast a_n P_{\lambda_k}(  y) )|
=\frac{\lambda_k}{\lambda_{n}} |\tau(     a_n P_{\lambda_k}(  y) y^\ast a_n^\ast ) |
\leqslant    \frac{\lambda_k}{\lambda_{n}} \Vert P_{\lambda_k}(  y) y^\ast \Vert_\infty,
\end{split}$$ which converges to 0 as $n \rightarrow \infty$. Similarly, $$\label{Eqn=Lim3}
\lambda_{n}^{-1} \tau(  y^\ast \Delta(a_n^\ast a_n ) y )=\lambda_{n}^{-1} \tau(   a_n^\ast a_n  \Delta(y y^\ast) )
\rightarrow 0,$$ as $n \rightarrow \infty$. Now we find that $$\begin{split}
& 2|\lambda_{n}^{-1} \tau( \Gamma(a_n, a_n y) y - y^\ast \Gamma(a_n, a_n) y  )| \\
\leqslant \  &
\lambda_{n}^{-1}  |\tau(  \Delta(  a_n y)^* a_n y   -  y^\ast \Delta(a_n)^* a_n y)| + \lambda_{n}^{-1}  |\tau(\Delta(y^\ast a_n^\ast a_n) y)| + \lambda_{n}^{-1} | \tau(y^\ast \Delta(a_n^\ast a_n) y )| \\
\leqslant \ &
\lambda_{n}^{-1}  \|(\Delta(a_ny )  -  \Delta(a_n)y )\Omega_\tau\| \|y\|_\infty + \lambda_{n}^{-1}  |\tau(\Delta(y^\ast a_n^\ast a_n) y)| + \lambda_{n}^{-1} | \tau(y^\ast \Delta(a_n^\ast a_n) y )|
\end{split}$$ which converges to 0 as $n \rightarrow \infty$ by [\[Eqn=Lim1\]](#Eqn=Lim1){reference-type="eqref" reference="Eqn=Lim1"}, [\[Eqn=Lim2\]](#Eqn=Lim2){reference-type="eqref" reference="Eqn=Lim2"} and [\[Eqn=Lim3\]](#Eqn=Lim3){reference-type="eqref" reference="Eqn=Lim3"}. Essentially the same estimates show that $$\begin{split}
& \lambda_{n}^{-1} \tau( \Gamma(a_n y, a_n y)  - y^\ast \Gamma(a_n y, a_n)   ) \rightarrow 0.
\end{split}$$ We therefore get that, as $n\to \infty$, $$\begin{split}
\lambda_{n}^{-1} \Vert  a_n \partial(y) \Vert^2 = &  \lambda_{n}^{-1}\tau\left( \Gamma (a_n y, a_n y )  + y^\ast \Gamma(a_n, a_n) y - y^\ast \Gamma(a_n y, a_n) - \Gamma(a_n, a_n y) y
\right) \rightarrow 0.
\end{split}$$ This shows that, as $n\to \infty$, $$\label{Eqn=ConvergenceThree}
\lambda_{n}^{-\frac{1}{2}}{\Vert x a_n \partial( y) \Vert}
\leqslant
\lambda_{n}^{-\frac{1}{2}}{ \Vert x \Vert_\infty \Vert  a_n \partial( y) \Vert} \rightarrow 0.$$ In all, the convergences [\[Eqn=ConvergenceThree\]](#Eqn=ConvergenceThree){reference-type="eqref" reference="Eqn=ConvergenceThree"} and [\[Eqn=ConvergenceTwo\]](#Eqn=ConvergenceTwo){reference-type="eqref" reference="Eqn=ConvergenceTwo"} show that [\[Eqn=RemainderTerm\]](#Eqn=RemainderTerm){reference-type="eqref" reference="Eqn=RemainderTerm"} and hence [\[Eqn=VStep\]](#Eqn=VStep){reference-type="eqref" reference="Eqn=VStep"} goes to 0. We conclude that $T_{x,y}(a_n) \to 0$ as $n\to \infty$ and therefore $\|T_{x,y} P_{\lambda_n}\| \to 0$ as $n\to \infty$.

By Lemma [\[Lem=filtered\]](#Lem=filtered){reference-type="ref" reference="Lem=filtered"}, for any $n,m$ with $|n-m|>2K$, $xa_n y$ and $xa_m y$ are orthogonal, so that $$\langle xa_n\otimes_\nabla y, xa_m\otimes_\nabla y \rangle = \langle xa_n\otimes_\nabla y, xa_m y \otimes_\nabla 1 \rangle = \langle x\otimes_\nabla a_n y, xa_my\otimes_\nabla 1 \rangle = 0.$$ This implies $\langle x \partial(a_n)y, x\partial(a_m)y\rangle = \langle x \partial(a_n)y, \partial(xa_my)\rangle=0$. We obtain $$\langle T_{x,y}(a_n), T_{x,y} (a_m) \rangle=0, \quad \text{for all }n,m \text{ with }|n-m|>2K.$$ It turns out that $T_{x,y}^* T_{x,y} P_{\lambda_n} = \sum_{k=-2K}^{2K} P_{\lambda_{n+k}} T_{x,y}^* T_{x,y} P_{\lambda_n}$ for all $n\in \mathbb{N}$ (where $P_l=0$ if $l<0$). By putting $T:=T_{x,y}^*T_{x,y}$, we see that $$\begin{aligned}
    T
    = \sum_{n\in \mathbb{N}} T P_{\lambda_n}
    = \sum_{n\in \mathbb{N}} \sum_{k=-2K}^{2K} P_{\lambda_{n+k}} T P_{\lambda_n}
    = \sum_{k=-2K}^{2K} \sum_{n\in \mathbb{N}}  P_{\lambda_{n+k}} T P_{\lambda_n},
\end{aligned}$$ where the sum is in the strong topology. For each fixed $-2K \leqslant k \leqslant 2K$ and $m\in \mathbb{N}$, since $P_{\lambda_{n+k}}$ is orthogonal for different $n$, it holds that $$\begin{aligned}
    \left\|\sum_{m\leqslant n\in \mathbb{N}} P_{\lambda_{n+k}} T P_{\lambda_n}\right\|
    = \sup_{m\leqslant n\in \mathbb{N}}\|P_{\lambda_{n+k}} T P_{\lambda_n}\|
    \leqslant \sup_{m\leqslant n\in \mathbb{N}}\|T_{x,y}P_{\lambda_{n+k}}\| \|T_{x,y} P_{\lambda_n}\|,
\end{aligned}$$ which converges to 0 as $m \to \infty$. Thus the sum $\sum_{n\in \mathbb{N}} P_{\lambda_{n+k}} T P_{\lambda_n}$ converges in the norm topology, hence it is a compact operator. We conclude that $T$ is compact, so $T_{x,y}$ is also compact. ◻
:::

We conclude as follows.

::: thm
[]{#Thm=AO label="Thm=AO"} Let $M$ be a finite von Neumann algebra and let $(\Phi_t)_{t \geq 0} = (\exp(-t \Delta))_{t \geq 0}$ be a quantum Markov semi-group that is gradient coarse and suppose that $\Delta$ is filtered with subexponential growth. Assume further that $A$ as defined above is locally reflexive. Then $M$ satisfies AO$^+$.
:::

::: proof
*Proof.* Lemma [\[Lem=AO\]](#Lem=AO){reference-type="ref" reference="Lem=AO"} and Theorem [\[Thm=Compact\]](#Thm=Compact){reference-type="ref" reference="Thm=Compact"} show that the assumptions of Proposition [\[Prop=Action\]](#Prop=Action){reference-type="ref" reference="Prop=Action"} are satisfied. Therefore this proposition together with local reflexivity of $A$ implies that $M$ satisfies AO$^+$. ◻
:::

The following corollary is then a consequence of [@IsonoTransactions] (see also [@PopaVaesCrelle]).

::: cor
Suppose $M$ has the W$^*$CMAP. Then under the assumptions of Theorem [\[Thm=AO\]](#Thm=AO){reference-type="ref" reference="Thm=AO"}, $M$ is strongly solid.
:::

The following examples are covered by Theorem [\[Thm=AO\]](#Thm=AO){reference-type="ref" reference="Thm=AO"}.

::: cor
For $\vert q \vert \leqslant \dim(H)^{-\frac{1}{2}}$ the $q$-Gaussian algebra $\Gamma_q(H_{\mathbb{R}})$ satisfies Condition AO$^+$.
:::

::: proof
*Proof.* In case $\vert q \vert < \dim(H)^{-\frac{1}{2}}$ we verify the conditions of Theorem [\[Thm=AO\]](#Thm=AO){reference-type="ref" reference="Thm=AO"} as follows. From Theorem [\[Thm=QGaussianSp\]](#Thm=QGaussianSp){reference-type="ref" reference="Thm=QGaussianSp"} and Remark [\[Rmk=FilteredExample\]](#Rmk=FilteredExample){reference-type="ref" reference="Rmk=FilteredExample"} we see that a $\Gamma_q(H_{\mathbb{R}})$ admits a filtered quantum Markov semi-group that is gradient-$\mathcal{S}_2$. From Corollary [\[Cor=GradientCoarseConsequence\]](#Cor=GradientCoarseConsequence){reference-type="ref" reference="Cor=GradientCoarseConsequence"} this semi-group is gradient coarse and the conditions of Theorem [\[Thm=AO\]](#Thm=AO){reference-type="ref" reference="Thm=AO"} are verified. In case $\vert q \vert \leqslant  \dim(H)^{-\frac{1}{2}}$ we have that Theorem [\[Thm=QGaussianSp\]](#Thm=QGaussianSp){reference-type="ref" reference="Thm=QGaussianSp"} and Remark [\[Rmk=FilteredExample\]](#Rmk=FilteredExample){reference-type="ref" reference="Rmk=FilteredExample"} show that $\Gamma_q(H_{\mathbb{R}})$ admits a filtered quantum Markov semi-group that is immediately gradient-$\mathcal{S}_2$. Then from [@CaspersGradient Proposition 4.3] and Proposition [\[Prop=NormalExtension\]](#Prop=NormalExtension){reference-type="ref" reference="Prop=NormalExtension"} we see that the semi-group is gradient coarse. We conclude again by Theorem [\[Thm=AO\]](#Thm=AO){reference-type="ref" reference="Thm=AO"}. ◻
:::

As mentioned before, Shlyakhtenko [@Shlyakhtenko] obtained the same result for $\vert q \vert < \sqrt{2} -1$ so that up to dimension 5 we find a new range. Other examples include the following.

::: example
Free group factors with the natural radial semi-group coming from the length function. Here conditon AO$^+$ is known, see [@NateTaka].
:::

::: example
Free orthogonal quantum groups $O_N^+$ (tracial case). In [@CaspersGradient] a gradient coarse quantum Markov semi-group was constructed which has the filter and subexponential growth property. Together with local reflexivity (which follows from the CMAP of [@FreslonJFA] or [@CFY]) one obtains AO$^+$. Here AO$^+$ was obtained already in [@VaesVergnioux] using boundary actions.
:::
