---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-009-23-traces-in-ribbon-categories
section_title: "Traces in Ribbon Categories"
section_number: 2.3
pages: 5-6
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.953
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
\label{SS:traces} For any objects $V,W$ of $\cat$ and $f \in \End_{\cat}( V \otimes W)$, set
\begin{equation}\label{E:trL}
\tr_{L}(f)=(\ev_{V}\otimes \Id_{W})(\Id_{V^{*}}\otimes
f)(\coev'_{V}\otimes \Id_{W}) \in \End_{\cat}(W),
\end{equation} and
\begin{equation}\label{E:trR}
\tr_{R}(f)=(\Id_{V}\otimes \ev'_{W})  (f \otimes \Id_{W^{*}})
(\Id_{V}\otimes \coev _{W}) \in \End_{\cat}(V).
\end{equation}


\begin{definition}\label{D:trace}  If $\ideal$ is an ideal in $\cat$, then a \emph{trace on $\ideal$} is a family of linear functions
$$\mt = \{\mt_V:\End_\cat(V)\rightarrow K\}$$
where $V$ runs over all objects of $\ideal$ and such that following two conditions hold:
\begin{enumerate}
\item  If $U\in \ideal$ and $W\in \ob$ then for any $f\in \End_\cat(U\otimes W)$ we have
\begin{equation}\label{E:VW}
\mt_{U\otimes W}\left(f \right)=\mt_U \left( \tr_R(f)\right).
\end{equation}
\item  If $U,V\in \ideal$ then for any morphisms $f:V\rightarrow U $ and $g:U\rightarrow V$  in $\cat$ we have 
\begin{equation}\label{E:fggf}
\mt_V(g f)=\mt_U(f  g).
\end{equation} 
\end{enumerate}
\end{definition}
Using the trace on $\ideal$ introduced above, we define a modified
dimension function on objects in $\ideal$.  Namely, we define the \emph{modified dimension function} 
\[
\md_{\mt}: \operatorname{Ob}(\ideal ) \to  K
\] by the formula 
\[
\md_{\mt} (V) = \mt_{V}\left(\Id_{V} \right).
\]



\begin{example}\label{X:categoricaltrace}
If $\cat$ is a ribbon category, then $\cat$ itself is an ideal and the well known \emph{categorical trace} function
\[
\tr_{\cat}: \End_{\cat}(V) \to  K
\] given by 
\[
\tr_{\cat}(f) = \ev'_{V}  (f \otimes 1)  \coev_{V}
\] defines a trace on $\cat$.  The modified dimension function then coincides with the familiar \emph{categorical dimension} function.
\end{example}

The following theorem from \cite{GKP} gives a convenient way of creating ideals with traces.  Assume that $J$ in $\cat$ admits a linear map 
\[
\mt_{J}: \End_{\cat}(J) \to K
\] which satisfies 
\begin{equation*}
\mt_{J}\left( \tr_{L}(h) \right) = \mt_{J} \left( \tr_{R}(h)\right),
\end{equation*} for all $h \in \End_{\cat}(J\otimes J)$. 
Such a linear map is called an \emph{ambidextrous trace on $J$}. 

For an object $J$, let $\ideal_{J}$ denote the ideal whose objects are all objects which are retracts of $J \otimes X$ for some $X$ in $\cat$.
\begin{theorem}\label{T:ambitrace} If $J$ is an object of $\cat$ which admits an
  ambidextrous trace, then there is a unique trace on $\ideal_{J}$ determined
  by that ambidextrous trace.
\end{theorem}
