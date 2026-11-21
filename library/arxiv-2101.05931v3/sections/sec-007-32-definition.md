---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-007-32-definition
section_title: "Definition"
section_number: 3.2
pages: 6-7
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.971
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
In this section we introduce our main objects of study: representations of the 2-quantum group on abelian categories, which we refer to as “categorical representations” of $U_q(\fg)$.  This definition of the categorified quantum groups and their categorical actions is originally due to Rouquier and Khovanov-Lauda \cite{Rou2KM, KLI,KLII}.  

In the literature, there are a number of slightly different-looking examples of 2-representations, depending not just on whether or not one is working with the Khovanov-Lauda or Rouquier 2-categories, but also depending on whether or not one is interested in categorifications of representations of $U_q(\fg)$ or of $U(\fg)$.  At the categorical level, the difference between $U_q(\fg)$ or of $U(\fg)$ arises from grading considerations; in categorifications of representations of  $U_q(\fg)$, one works with categories enriched in graded vector spaces, whereas in categorifications of representations of  $U(\fg)$ no such grading is needed.  

Fortunately, the different notions of categorical representations - and in particular relationships between the Rouquier and Khovanov-Lauda frameworks in both graded and ungraded settings, have been brought in line by work of Cautis-Lauda, who proved that in the graded setting, integrable 2-representations of the Rouquier 2-category induce 2-representations of the Khovanov-Lauda 2-category \cite{CaLa}, and by work of Brundan \cite{Brundandef}, who proved that the underlying ungraded 2-categories of Rouquier and Khovanov-Lauda are equivalent.  

The important point for us is that all our theorems, including our main results (Theorem \ref{thm:mincat} and Theorem \ref{thm:perveq}), remain true in any 2-representation of the Khovanov-Lauda-Rouqier 2-category, in either the graded or ungraded setting.
Since the compatibility of the internal grading with the braid group is of some independent combinatorial interest, we elect to keep track of the gradings in the rest of the paper, and leave it to the reader to verify that the arguments go through while ignoring the gradings and working in the setup of, e.g. Brundan \cite{Brundandef}.  To that end, we have chosen to follow the notation and conventions of Cautis-Lauda below.

A \textbf{categorical representation} of $U_q(\fg)$ consists of the following data:
\begin{itemize}
\item A family of graded abelian $\kk$-linear categories $\cC_\mu$ indexed by $\mu \in X$.  We refer to each $\cC_\mu$ as a \textbf{weight category}. 
\item Exact graded functors $\sE_i\bone_\mu:\cC_\mu\to \cC_{\mu+\alpha_i}$ and $\sF_i\bone_\mu:\cC_\mu\to \cC_{\mu-\alpha_i}$, for $i\in I$ and $\mu\in X$. We refer to $\sE_i,\sF_i$ as \textbf{Chevalley functors}. 
\item A collection of natural transformations between these functors.  We won't be using directly these natural transformations in this work, so refer the reader to \cite[Definition 1.1]{CaLa} for their definition.




\end{itemize}
This data is subject to the conditions spelled out in items (1)-(5) of \cite[Definition 1.1]{CaLa}.  We only record those that are relevant for us:
\begin{enumerate}
\item The functors $\sE_i\bone_\mu$ and $\sF_i\bone_\mu$ are biadjoint up to a specified degree shift (see \eqref{eqs:biadjs} below).  
\item The powers of  $\sE_i$ carry an action of the KLR algebra associated to $Q$, where $Q$ denotes a choice of units $(t_{ij})_{i \neq j \in I}$ in $\mathbbm{k}^\times$.  These units satisfy some restrictions which are not relevant for us.  

\item We have the following isomorphisms:
\begin{align*}
\sF_i\sE_i\bone_\mu &\cong \sE_i\sF_i\bone_\mu\oplus_{[-\langle h_i,\mu \rangle]}\bone_\mu, \text{ if  }\langle h_i,\mu \rangle \leq 0, \\
\sE_i\sF_i\bone_\mu &\cong \sF_i\sE_i\bone_\mu\oplus_{[\langle h_i,\mu \rangle]}\bone_\mu, \text{ if  }\langle h_i,\mu \rangle \geq 0,\\
\sE_i\sF_j\bone_\mu &\cong \sF_j\sE_i\bone_\mu.
\end{align*}
This notation is explained as follows: for a Laurent polynomial $f=\sum f_a q^a$, $\oplus_f A$ is a direct sum over $a\in \ZZ$ of $f_a$ copies of $A\langle a \rangle$, and $[n]:=q^{n-1}+q^{n-3}+\cdots+q^{1-n}$.
\end{enumerate}

Usually we just say that $\cC=\bigoplus_\mu \cC_\mu$ is a categorical representation of $U_q(\fg)$ (the remaining data is implicit).   Given an integrable $U_q(\fg)$-module $V$, we say that $\cC$ is a categorification of $V$ if $\cC$ is a categorical representation of $U_q(\fg)$ such that $[\cC]_{\CC(q)} \cong V$ as $U_q(\fg)$-modules.

An \textbf{additive categorification} is a categorical representation on a graded additive $\kk$-linear category $\cV$ satisfying the same conditions as above, except the Chevalley functors are of course only required to be additive.  We let $\cV^i$ be the idempotent completion of $\cV$.

Given an abelian category $\cC$, we consider the additive category $\cC\proj$ defined as the full subcategory of projective objects in $\cC$.  Note that if $\cC$ is a categorical representation of $U_q(\fg)$, then $\cC\proj$ naturally inherits the structure of an additive categorification.  



As a consequence of this definition, and in particular condition (2), there exist divided power functors $\sE_i^{(r)}\bone_\lambda \subset \sE_i^r\bone_\lambda, \sF_i^{(r)}\bone_\lambda \subset \sF_i^r\bone_\lambda$ which categorify the usual divided powers on the level of the quantum group.  Again, we refer the reader to \cite{CaLa} and references therein for further details.  We note that their adjoints are related as follows:
\begin{align}\label{eqs:biadjs}
(\sE_i^{(r)}\bone_\lambda)_R &\cong \sF_i^{(r)}\bone_{\lambda+r\alpha_i}\langle r(\lambda_i+r) \rangle,\\
(\sE_i^{(r)}\bone_\lambda)_L &\cong \sF_i^{(r)}\bone_{\lambda+r\alpha_i}\langle -r(\lambda_i+r) \rangle.
\end{align}
