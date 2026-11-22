---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-014-5-some-commutation-relations
section_title: "Some commutation relations"
section_number: 5
pages: 12-13
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.91
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
\label{sec:commrels}
We fix throughout a categorical representation $\cC$ of  $U_q(\fg)$.
Recall that $w_0\in W$ is the longest word, and let $w_0=s_{i_1}s_{i_2} \cdots s_{i_r}$ be a reduced expression.
We consider the composition of Rickard complexes which categorifies the positive lift in $B$ of $w_0$:
$$
\Theta_{w_0}\bone_\lambda=\Theta_{i_1} \cdots \Theta_{i_r}\bone_\mu:D^b(\cC_\lambda) \to D^b(\cC_{w_0(\lambda)}).
$$
In preparation for the proofs our main results in the next section, we prove some commutation relations between $\Theta_{w_0}$ and the Chevalley functors.  



\subsection{Cautis' relations}
To begin, we recall some relations of Cautis (building on work with Kamnitzer \cite{CK3}).  Although they are stated only for type A,  their proofs apply to any simply-laced Lie algebra.

\begin{Lemma}[Lemma 4.6, \cite{Cauclasp}]\label{lem:Cau0}
For any $i\in I, \lambda \in X$ we have the following relations:
\begin{align*}
\Theta_i\sE_i\bone_\lambda &\cong \sF_i\Theta_i\bone_\lambda[1]\langle \lambda_i \rangle, 

\\
\Theta_i\sF_i\bone_\lambda &\cong \sE_i\Theta_i\bone_\lambda[1]\langle -\lambda_i \rangle. 

\end{align*}
\end{Lemma}

\begin{Remark}
The careful reader will notice that actually Cautis proves Lemma \ref{lem:Cau0} under certain conditions on $\lambda$.  For instance, the first relation is only proven in the case when $\lambda_i \leq 0$.  To deduce the general case from this, one can rewrite the relation
as $\sE_i \Theta_i^{-1}\cong \Theta_i^{-1}\sF_i[1]\langle \lambda_i \rangle$.  Now recall that there is an anti-automorphism $\tilde{\sigma}$ on the $\fsl_2$ 2-category which on objects maps $n \mapsto -n$ \cite[Section 5.6]{Laucq}.  This anti-automorphism maps $\Theta_i^{-1}$ to $\Theta_i$, and hence applying it to the relation above we deduce the desired relation in the case when $\lambda_i \geq 0$.

Alternatively, in a recent preprint Vera proves a version of the relation between the Rickard complex and Chevalley functors in the (bounded homotopy category of the) $\fsl_2$ 2-category, which of course implies it also in any 2-representation \cite{Vera}.
\end{Remark}













Next we recall the categorical analogues of commutators $[E_i,E_j]$ acting on representations of $U_q(\fg)$.  Given nodes $i,j\in I$ such that $(i,j)=-1$ and  $\lambda \in X$, define complexes of functors 
\begin{align*}
\sE_{ij}\bone_\lambda:D^b(\cC_\lambda) \to D^b(\cC_{\lambda+\alpha_i+\alpha_j}), \quad \sE_{ij}\bone_\lambda &=\sE_i\sE_j\bone_\lambda\langle-1\rangle \to \sE_j\sE_i\bone_\lambda, \\
\sF_{ij}\bone_\lambda: D^b(\cC_\lambda) \to D^b(\cC_{\lambda-\alpha_i-\alpha_j}), \quad \sF_{ij}\bone_\lambda &=\sF_i\sF_j\bone_\lambda \to \sF_j\sF_i\bone_\lambda\langle 1 \rangle.
\end{align*}
In both instances the differential  is given by the element $T_{ij}$ arising from the KLR algebra, and the left term of the complex is in homological degree zero \cite{Cauclasp}.



\begin{Lemma}[Lemma 5.2, \cite{Cauclasp}]\label{lem:Cau} Let $i,j\in I,  \lambda \in X$ and suppose $(i,j)=-1$.  We have the following isomorphisms:
\begin{align*}

\sE_{ij} \Theta_i \bone_\lambda &\cong \begin{cases} \Theta_i\sE_j &\text{ if } \lambda_i>0, \\
\Theta_i\sE_j[1]\langle -1 \rangle &\text{ if } \lambda_i\leq 0 \end{cases} \\
\sF_{ij} \Theta_i \bone_\lambda &\cong \begin{cases} \Theta_i\sF_j &\text{ if } \lambda_i\geq0, \\
\Theta_i\sF_j[-1]\langle 1 \rangle &\text{ if } \lambda_i< 0 \end{cases} \\
\bone_\lambda\Theta_j\sE_{ij} &\cong \begin{cases} \sE_i\Theta_j &\text{ if } \lambda_j<0, \\
\sE_i\Theta_j[1]\langle -1 \rangle &\text{ if } \lambda_j\geq 0 \end{cases} \\
\bone_\lambda\Theta_j\sF_{ij} &\cong \begin{cases} \sF_i\Theta_j &\text{ if } \lambda_j\leq0, \\
\sF_i\Theta_j[-1]\langle 1 \rangle &\text{ if } \lambda_j> 0 \end{cases} 
\end{align*}

\end{Lemma}
