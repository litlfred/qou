---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-017-6-on-t-exactness-and-perversity-of-w-0
section_title: "On t-exactness and perversity of _w_0"
section_number: 6
pages: 15-17
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.932
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
In this section we will state and prove the central results of the paper.  We fix throughout a categorical representation $\cC$ of  $U_q(\fg)$, and let $w_0=s_{i_1}s_{i_2} \cdots s_{i_n}$ be a reduced expression.





\subsection{$\Theta_{w_0}$ on isotypic categorifications}	In this section we prove that $\Theta_{w_0}$ is t-exact on any isotypic categorification.  Fix $\lambda \in X_+$.  We write $\Theta=\Theta_{w_0}, L=L(\lambda)$ and $\cL=\cL(\lambda)$.

\begin{Lemma}\label{lem:techbit}
Let $k\in\{2,\hdots,n\}$ and set $\mu=s_{i_k}\cdots s_{i_n}(w_0(\lambda))$.  The weight space $L(\lambda)_{\mu-\alpha_{i_{k-1}}}$ is zero.
\end{Lemma}

\begin{proof}
By \cite[Proposition 21.3]{Humph}, it suffices to find $u\in W$ such that $u(\mu-\alpha_{i_{k-1}}) \nsucc w_0(\lambda)$.  Take $u=s_{i_{k-1}}$ and, noting that $(\mu,\alpha_{i_{k-1}})<0$, the result follows.
\end{proof}

Recall that $v_\lambda$ and $v_\lambda^{low}$ are the highest and lowest weight elements of the canonical basis $\bB(\lambda)$.

\begin{Lemma}\cite[Comment 5.10]{KT}\label{lemma:KT}
We have $\st_{w_0}(v_\lambda^{low})=v_\lambda$.
\end{Lemma}

\begin{Proposition}\label{prop:lowestwt}
The equivalence $\Theta\bone_{w_0(\lambda)}:D^b(\cL_{w_0(\lambda)})\to D^b(\cL_{\lambda})$ satisfies $\kk_{low}\mapsto\kk_{high}$, where both are considered as complexes concentrated in degree zero.  In particular, under the equivalences $\cL_\lambda \cong \cL_{w_0(\lambda)}\cong \kk\mmod_\ZZ$,  $\Theta\bone_{w_0(\lambda)}$ is isomorphic to the identity autofunctor of $D^b(\kk\mmod_\ZZ)$.
\end{Proposition}

\begin{proof}
Consider first the case $\fg=\fsl_2$.  On the minimal categorification of highest weight $m$, we have that $\Theta\bone_{-m}(\kk_{low})=\kk_{high}\langle \ell \rangle$ for some $\ell$ by \cite[Theorem 6.6]{CR}.  Since $[\Theta\bone_{-m}]=\st_{1}\sone_{-m}$, by Lemma \ref{lemma:KT} we conclude that $\ell=0$, and hence $\Theta\bone_{-m}(\kk_{low})=\kk_{high}$.

For general $\fg$, suppose $X \in \cL_\nu$ is simple and  $\sF_iX=0$ for some $i \in I$.  Consider $\cL$ as a categorical representation of $\fsl_2$ by restriction to the $i$-th root subalgebra. 
Then for some $m$ we have a morphism of categorical $\fsl_2$ representations
$
R_X:\cL(m) \to \cL,
$
such that $R_X(\kk_{low})=X$ \cite[Theorem 5.24]{CR}.  

The functor $R_X$ is equivariant for the categorical $\fsl_2$ action on $\cC$ determined by $\sE_i,\sF_i$ (in fact it is strongly equivariant in the sense of \cite[Definition 3.1]{LoWe}), and hence commutes with $\Theta_i\bone_\nu$.  Therefore we have that 
\begin{align*}
\Theta_i\bone_{\nu}(X) &\cong  \Theta_i\bone_{\nu}(R_X(\kk_{low})) \\
&\cong R_X(\Theta_i\bone_{\nu}(\kk_{low})) \\
&\cong R_X(\kk_{high}) \in \cL,
\end{align*}
and so $\Theta_i\bone_{\nu}(X)$ is in homological degree zero.  
It follows that in the case when $X$ is not necessarily simple (but still assume that $\sF_iX=0$), $\Theta_i\bone_{\nu}(X)$ is still in homological degree zero.  Indeed, by induction on the length of a Jordan-H\"older filtration of $X$ one deduces this since $\cL \subset D^b(\cL)$ is extension closed. 





Now we study $\Theta\bone_{w_0(\lambda)}$ applied to $\kk_{low}$.  For $k=2,\hdots,n$, by Lemma \ref{lem:techbit}, $$\sF_{i_{k-1}}(\Theta_{i_k}\cdots\Theta_{i_n}\bone_{w_0(\lambda)}(\kk_{low}))=0.$$ By the previous paragraph, it follows that $\Theta_{i_{k-1}}\cdots\Theta_{i_n}\bone_{w_0(\lambda)}(\kk_{low})$ is in homological degree zero, and in particular, $\Theta\bone_{w_0(\lambda)}(\kk_{low})$ is supported in homological degree zero.  Since in addition $$[\Theta\bone_{w_0(\lambda)}]=\st_{w_0}\sone_{w_0(\lambda)},$$ by Lemma \ref{lemma:KT} we conclude that $\Theta\bone_{w_0(\lambda)}(\kk_{low})\cong\kk_{high}$.
\end{proof}

\begin{Theorem}\label{thm:mincat}
Let $\lambda \in X_+$ and set $\cL=\cL(\lambda)$.  For any $\mu \in X$, $$\Theta\bone_\mu[-n]:D^b(\cL_\mu) \to D^b(\cL_{w_0(\mu)})$$ is t-exact, where $n=ht(\mu-w_0(\lambda))$.
\end{Theorem}

\begin{proof}
Consider  $P=\sE_{i_1}\cdots \sE_{i_\ell}(\kk_{low}) \in \cL_\mu$.  We will first prove by induction on $n$ that there exists an integer $k$ such that 
\begin{align}\label{eq:ind}
\Theta(P)[-n] \cong \sF_{j_1}\cdots \sF_{j_\ell}(\kk_{high})\langle k \rangle \in \cL_{w_0(\mu)},
\end{align}
where $j_r=\tau(i_{r})$.

The base case when $n=0$ follows by Proposition \ref{prop:lowestwt}.  For the inductive step write $P=\sE_{i_1}(Q)$. Note that $Q\in \cL_{\mu-\alpha_{i_1}}$.  By Proposition \ref{prop:mainrel} we have that 
\begin{align*}
\Theta\bone_\mu(P)[-n] &= \Theta \sE_{i_1}\bone_{\mu-\alpha_{i_1}}(Q)[-n] \\
&\cong \sF_{\tau(i_1)}\Theta\bone_{\mu-\alpha_{i_1}}(Q)[-n+1]\langle (\mu-\alpha_{i_1},\alpha_{i_1}) \rangle.
\end{align*}
By hypothesis $$\Theta\bone_{\mu-\alpha_{i_1}}(Q)[-n+1] \cong \sF_{j_2}\cdots \sF_{j_\ell}(\kk_{high})\langle k \rangle \in \cL_{w_0(\mu-\alpha_{i_1})}$$ for some $k$, and hence Equation (\ref{eq:ind}) follows.

Since up to grading shift, any projective indecomposable object in $\cL_\mu$, respectively $\cL_{w_0(\mu)}$, is a summand of an object of the form $\sE_{i_1}\cdots \sE_{i_\ell}(\kk_{low})$ (respectively $\sF_{j_1}\cdots \sF_{j_\ell}(\kk_{high})$), it follows that $\Theta\bone_\mu[-n]$ takes projective objects in $\cL_\mu$ to projective objects in $\cL_{w_0(\mu)}$.  Since $\Theta\bone_\mu[-n]$ is a derived equivalence it follows that it is t-exact.








\end{proof}


\begin{Remark}
Theorem \ref{thm:mincat} is a generalisation of  \cite[Theorem 6.6]{CR}, which covers the $\fsl_2$ case.  Note that \cite[Theorem 6.6]{CR} is crucial in the work of Chuang and Rouquier, since it's one of the main technical results needed to prove that Rickard complexes are invertible.  Our proof in the general case follows a completely different approach, but   it does not give a new proof in the case of $\fsl_2$. Indeed we use \cite[Theorem 6.6]{CR} explicitly in the proof of Proposition \ref{prop:lowestwt}, and more generally we use the fact the $\Theta_i$ is invertible throughout.  
\end{Remark}

\begin{Corollary}\label{cor:mainthm}
Suppose $\cC$ is an isotypic categorification of type $\lambda$, for some $\lambda \in X_+$, and let $\mu \in X$.  Then $\Theta\bone_\mu[-n]:D^b(\cC_\mu) \to D^b(\cC_{w_0(\mu)})$ is a t-exact equivalence, where $n=ht(\mu-w_0(\lambda))$.  
\end{Corollary}

\begin{proof}
By Lemma \ref{lem:isocat}, there exists an abelian $\kk$-linear category $\cA$ such that $\cC \cong \cL(\lambda)\otimes_\kk \cA$ as categorical representations.  We have that 
$$
\Theta\bone_\mu[-n](\cL(\lambda)_\mu\otimes_\kk \cA) \cong \Theta\bone_\mu[-n](\cL(\lambda)_\mu) \otimes_\kk \cA \cong \cL(\lambda)_{w_0(\mu)}\otimes_\kk \cA,
$$
proving that $\Theta\bone_\mu[-n]:D^b(\cC_\mu) \to D^b(\cC_{w_0(\mu)})$ is a t-exact equivalence.

\end{proof}
