---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-022-73-reconciling-the-two-cactus-group-actions
section_title: "Reconciling the two cactus group actions"
section_number: 7.3
pages: 20-21
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.964
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
Let $\cC$ be a categorical representation of $U_q(\fg)$, and consider the $\fg$-crystal $\bB=\Irr(\cC)$.   There are two actions of the cactus group on $\bB$, the first arising combinatorially via  Sch\"utzenberger involutions (Theorem \ref{thm:cactact}) and the other categorically via Theorem \ref{thm:cactus}. 

\begin{Theorem}\label{thm:agree}
The two actions of the cactus group on $\bB$  agree.
\end{Theorem}

\begin{proof}
It suffices to show that $\varphi_I=\xi_I$.  
First, suppose $\cC$ is a simple categorification of type $\lambda \in X_+$.  In this case $\bB=\bB(\lambda)$, and $\xi=\xi_I$ is determined by:
\begin{align*}
\xi(v_\lambda)&=v_\lambda^{low}, \text{ and } \\
\xi(\tilde{e}_i(v))&=\tilde{f}_{\tau(i)}(\xi(v)) \text{ for all } v \in \bB,
\end{align*}
so we need to show that $\varphi_I$ satisfies these properties as well.  

The first is an immediate consequence of Corollary \ref{cor:mainthm}.  To show that $\varphi_I$ satisfies the second property, fix $\mu \in X$ and $ i \in I$.  We set $n=ht(\mu-w_0(\lambda)), j=\tau(i)$, and write $\Theta=\Theta_{w_0}$.  

Consider the following diagram:
\begin{equation}
\begin{tikzcd}
D^b(\cC_\mu) \arrow[rrr,"\Theta\bone_\mu\sh{-n}\langle \mu_i \rangle"] \arrow[d,"\sE_i\bone_\mu"] &&&  D^b(\cC_{w_0(\mu)}) \arrow[d,"\sF_j\bone_{w_0(\mu)}"] \\
D^b(\cC_{\mu+\alpha_i}) \arrow[rrr,"\Theta\bone_{\mu+\alpha_i}\sh{-n-1}"]  &&&  D^b(\cC_{w_0(\mu)-\alpha_j})
\end{tikzcd}
\end{equation}
By  Proposition \ref{prop:mainrel} this diagram commutes (note that we shifted both sides of the equation by $-n-1$).  By Theorem \ref{thm:mincat} both horizontal arrows are in fact t-exact equivalences so this restricts to a diagram of abelian categories:
\begin{equation}
\begin{tikzcd}
\cC_\mu \arrow[rrr,"\Theta\bone_\mu\sh{-n}\langle \mu_i \rangle"] \arrow[d,"\sE_i\bone_\mu"] &&&  \cC_{w_0(\mu)} \arrow[d,"\sF_j\bone_{w_0(\mu)}"] \\
\cC_{\mu+\alpha_i} \arrow[rrr,"\Theta\bone_{\mu+\alpha_i}\sh{-n-1}"]  &&&  \cC_{w_0(\mu)-\alpha_j}
\end{tikzcd}
\end{equation}

Let $L\in \cC_\mu$ be a simple object,  and let $L'=\Theta\bone_\mu(L)\sh{-n}\langle \mu_i \rangle$.  Note that $L'\in \cC_{w_0(\mu)}$ is simple and $\varphi_I(L)=L'$.  By the above diagram we have an isomorphism
\begin{align*}
\Theta\bone_{\mu+\alpha_i}(\sE_i(L))\sh{-n-1} \cong \sF_j(L').
\end{align*}
Now, $\widetilde{\sF}_j(L') \subset \sF_j(L')$ is the unique simple subobject.  On the other hand, since $\Theta\bone_{\mu+\alpha_i}\sh{-n-1}$ is an abelian equivalence, $\Theta\bone_{\mu+\alpha_i}(\widetilde{\sE}_i(L))\sh{-n-1}\subset \Theta\bone_{\mu+\alpha_i}(\sE_i(L))\sh{-n-1}$ is a simple subobject.  Therefore
\begin{align*}
\Theta\bone_{\mu+\alpha_i}(\widetilde{\sE}_i(L))\sh{-n-1} \cong \widetilde{\sF}_j(L').
\end{align*}
Since the equivalence class of the left hand side is $\varphi_I\circ \tilde{e}_i(L)$, this shows that $\varphi_I$ satisfies the second defining property, and hence the two cactus group actions agree in the case of a simple categorification. 

The general case when $\cC$ is not necessarily a simple categorification follows easily using the Jordan-H\"older filtration (Theorem \ref{thm:JH}) and Lemma \ref{lem:quot}.
\end{proof}
