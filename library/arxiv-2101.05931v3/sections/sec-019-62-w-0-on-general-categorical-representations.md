---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-019-62-w-0-on-general-categorical-representations
section_title: "_w_0 on general categorical representations"
section_number: 6.2
pages: 17-17
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.881
latex_coverage_ratio: 1.0
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
\label{sec:mainpf}

In this section we prove that $\Theta_{w_0}$ is a perverse equivalence on an arbitrary categorical representation.
Fix $\mu \in X$ such that $\cC_\mu$ is nonzero.  For ease of notation, set $\cA=\cC_\mu$ and $\cA'=\cC_{w_0(\mu)}$.    


Consider a filtration by Serre subcategories
\begin{align*}
0=\cC_0\subset \cC_1\subset \cdots \subset \cC_r=\cC,
\end{align*}
which can be either the Jordan-H\"older filtration (Theorem \ref{thm:JH}) or the isotypic filtration (Remark \ref{rem:isofilts}).  So for every $i$,  $\cC_i$ is a subrepresentation of $\cC$, and $\cC_i/\cC_{i-1}$ is either a simple categorification or an isotypic one.  Define $\lambda_i \in X_+$ by requiring that $[\cC_i/\cC_{i-1}]_{\CC(q)}$ is a representation of type $\lambda_i$.  




Construct filtrations of $\cA$ and $\cA'$ by $\cA_i=\cC_i\cap \cA, \cA_i'=\cC_i \cap \cA'$.  These are Serre subcategories of $\cA$ and $\cA'$ respectively.  Let $p:\{0,...,r\}\to \ZZ$ be given by 
$p(i)=ht(\mu-w_0(\lambda_i))$.  

\begin{Theorem}
\label{thm:perveq}
$\Theta_{w_0}\bone_\mu:D^b(\cA) \to D^b(\cA')$ is a perverse equivalence with respect to $(\cA_\bullet, \cA_\bullet',p)$ for either the Jordan-H\"older or the isotypic filtration. 
\end{Theorem}



\begin{proof}
Since $\cC_i \subset \cC$ is a categorical subrepresentation, the terms of the functor $\Theta_{w_0}\bone_\mu$ leave $\cC_i$ invariant, and in particular take objects in $\cA_i$ to $\cA_i'$.  By Lemma \ref{lem:trianginv} this implies that $\Theta_{w_0}\bone_\mu (D^b_{\cA_i}(\cA)) \subseteq D^b_{\cA_i'}(\cA')$.

Now, $\cC_i/\cC_{i-1}$ is a simple or isotypic categorification (of type $\lambda_i$).  By Corollary \ref{cor:mainthm}, $\Theta_{w_0}\bone_\mu[-p(i)]$ restricts to an abelian equivalence $\cA_i/\cA_{i-1} \to \cA_i'/\cA_{i-1}'$, i.e. the functor 
$$
\Theta_{w_0}\bone_\mu[-p(i)]:D^b_{\cA_i}(\cA)/D^b_{\cA_{i-1}}(\cA) \to D^b_{\cA'_i}(\cA')/D^b_{\cA'_{i-1}}(\cA')
$$
is a t-exact equivalence.  This shows that $\Theta_{w_0}\bone_\mu$ is a perverse equivalence with respect to $(\cA_\bullet, \cA'_\bullet, p)$.
\end{proof}

\begin{Remark}
The $\fsl_2$ case of Theorem \ref{thm:perveq} appears as \cite[Proposition 8.4]{CRperv}, by a different argument relying on a technical lemma \cite[Lemma 4.12]{CRperv}.  
\end{Remark}
