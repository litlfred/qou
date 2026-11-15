---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-016-53-the-relation-between-w-0-and-chevalley-functo
section_title: "The relation between _w_0 and Chevalley functors"
section_number: 5.3
pages: 14-15
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.941
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
We now have the machinery in place to prove our main relation.  

\begin{Proposition}\label{prop:mainrel}
For any $i\in I, \lambda \in X$ we have the following relations:
\begin{align*}
\Theta_{w_0}\sE_i\bone_\lambda &\cong \sF_{\tau(i)}\Theta_{w_0}\bone_\lambda[1]\langle \lambda_i \rangle, 
\\
\Theta_{w_0}\sF_i\bone_\lambda &\cong \sE_{\tau(i)}\Theta_{w_0}\bone_\lambda[1]\langle -\lambda_i \rangle. 
\end{align*}
\end{Proposition}

\begin{proof}
We'll prove the first relation, the second being entirely analogous.  
For two functors $\sF,\sG$ we write $\sF \equiv \sG$ if there exist integers $\ell,k$ such that $\sF \cong \sG[\ell]\langle k \rangle$.  

We first show that $\Theta_{w_0}\sE_i \equiv \sF_{\tau(i)}\Theta_{w_0}$ by induction on the rank of $\fg$.   The base case, when $\fg=\fsl_2$,  follows from Lemma \ref{lem:Cau0}.  For the inductive step let $J \subset I$ be a strict subdiagram containing $i$.  Recall the bijection $\tau_J:I\to I$ induced by the longest element $w_0^J \in W_J$.  Let $u=w_0(w_0^J)^{-1}$ and let $u=s_{i_1}\cdots s_{i_n}$ be a reduced expression.  Define two marked words:
\begin{align*}
\ba&=(i_1,\hdots,i_n,\ul{\tau_J(i)}),\\
\bb&=(\ul{\tau(i)},i_1,\hdots,i_n).
\end{align*}
Note that $w(\ba)=w(\bb)$.  By the inductive hypothesis we have $\Theta_{w_0^J}\sE_i 
\equiv  \sF_{\tau_J(i)}\Theta_{w_0^J}$, and therefore
\begin{align*}
\Theta_{w_0}\sE_i \equiv \Theta_u\Theta_{w_0^J}\sE_i 
\equiv  \Theta_u\sF_{\tau_J(i)}\Theta_{w_0^J} \equiv \Phi(\ba)\Theta_{w_0^J}.
\end{align*}
Note that $\ba,\bb$ satisfy the hypothesis of Lemma \ref{lem:markwrds2}, so by Lemmas \ref{lem:markwrds1} and \ref{lem:markwrds2}
we have that $\Phi(\ba)\equiv\Phi(\bb)$, and hence
$\Theta_{w_0}\sE_i \equiv \Phi(\bb)\Theta_{w_0^J} \equiv \sF_{\tau(i)}\Theta_{w_0}.$

We now know there exist integers $k,\ell$ such that $\Theta_{w_0}\sE_i\bone_\lambda \cong \sF_{\tau(i)}\Theta_{w_0}\bone_\lambda[\ell]\langle k \rangle$, and it remains to show that $\ell=1, k=\lambda_i$.  Let $u=w_0s_i$ and let $u=s_{i_1}\cdots s_{i_n}$ be a reduced expression.  Define two marked words:
\begin{align*}
\ba&=(i_1,\hdots,i_n,\ul{i}),\\
\bb&=(\ul{\tau(i)},i_1,\hdots,i_n).
\end{align*}
Note that $\ba,\bb$ satisfy the hypothesis of Lemma \ref{lem:markwrds2}, so by Lemmas \ref{lem:markwrds1} and \ref{lem:markwrds2} there exists an integer $m$ such that $\Phi(\ba)\cong \Phi(\bb)[m]\langle -m \rangle$.  Hence we have that
\begin{align*}
\Theta_{w_0} \sE_i \bone_\lambda &\cong \Theta_u \Theta_i \sE_i\bone_\lambda \\
& \cong \Theta_u \sF_i \Theta_i\bone_\lambda [1]\langle \lambda_i \rangle \\
& \cong \sF_{\tau(i)}\Theta_u \Theta_i \bone_\lambda[m+1]\langle -m+\lambda_i \rangle \\
& \cong \sF_{\tau(i)}\Theta_{w_0} \bone_\lambda[m+1]\langle -m+\lambda_i \rangle
\end{align*}
showing that $\ell+k=1+\lambda_i$.  

On the other hand, we can deduce $k$ by inspecting the relation on the level of Grothendieck groups.  Namely, by \cite[Lemma 5.4]{KT}, we have that 
$$
\st_{w_0}E_i\sone_\lambda = -q^{-\lambda_i}F_{\tau(i)}\st_{w_0}\sone_\lambda,
$$
showing that $k=\lambda_i$.
\end{proof}
