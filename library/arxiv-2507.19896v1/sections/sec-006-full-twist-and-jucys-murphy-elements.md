---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-006-full-twist-and-jucys-murphy-elements
section_title: "``Full twist'' and Jucys-Murphy elements."
section_number: null
pages: 4-4
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 1.0
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
\label{sec:full-twist-jucys} Assume that $(W, S)$ is of finite type. Let $w_0$ stand for the longest element in $W$ with respect to the Bruhat length. Let $\Se(W,S) = t_{w_0}^{-2} \in \He(W,S)$. In classical types, we will write $\Se(X_n) \in \He(X_n)$, when $X$ is $A, B$ or $D$, or simply $\Se$ when the type is clear from the context.  

The following proposition is also standard:
\begin{proposition}
  \label{sec:iwah-hecke-algebr}
  The element $\Se(W,S)$ is central in $\He(W,S)$. 
\end{proposition}

We will need the following ``Serre property'' of the operator of multiplication by $\Se(W,S)$.
\begin{proposition}
  \label{sec:full-twist-jucys-1}
  For any $h_1, h_2 \in \He(W,S)$ we have the identity
  \[
   \langle h_1, \Se(W,S)h_2 \rangle = \overline{\langle h_2, h_1 \rangle}.
  \]
\end{proposition}
\begin{proof}
  It is enough to prove the proposition for $h_1 = t_{w_1}^{-1}, h_2 = t_{w_2}$ for arbitrary $w_1, w_2 \in W$. We have, by Proposition \ref{sec:trace-funct-pair}~\ref{item:3},
  \begin{multline*}
    \langle t_{w_1}^{-1}, \Se(W,S)t_{w_2} \rangle = \langle t_{w_0}t_{w_1}^{-1}, t_{w_0}^{-1}t_{w_2}\rangle = \langle t_{w_0w_1^{-1}}, t_{w_2^{-1}w_0}^{-1} \rangle =\\
    = \delta_{w_0w_1^{-1},w_0w_2} = \delta_{w_1,w_2^{-1}} = \overline{\langle t_{w_2}, t_{w_1}^{-1}\rangle}.
\end{multline*}
This completes the proof.
\end{proof}

We have the natural embedding $\iota_n:\He(X_n) \to \He(X_{n+1})$, where $X$ is $A, B$ or $D$, induced by the embedding of the sets of labels of the Coxeter diagram. Using these embeddings, an element of $\He(X_n)$ can be considered as an element of $\He(X_m)$ for $m > n$. 

\begin{definition}
  For $n \geq 2$, let $J_n^X = \Se(X_{n})^{-1}\cdot \Se(X_{n-1})$ when $X$ is $A_{-1}, B$ or $D$. We let $J_1^A = 1, J_1^B = t_0^2$, $J_1^D = 1$. We call these elements \emph{Jucys-Murphy elements} of finite Hecke algebras in classical types.

  
\end{definition}

We have the following corollary of Proposition \ref{sec:iwah-hecke-algebr}.
\begin{corollary}
  \label{sec:iwah-hecke-algebr-1}
   For $X$ equal to $A_{-1}, B$ or $D$, elements $J_k^X$ commute with each other when considered lying in the same Iwahori-Hecke algebra via the embedding described above. The element $J_n^X$ lies in the centralizer of $\He(X_{n-1})$ in $\He(X_{n})$.
\end{corollary}
\begin{remark}
  The elements $J_k^A$ are sometimes called multiplicative Jucys-Murphy elements in the Iwahori-Hecke algebra of type $A$. There seem to be no agreement in the literature on which elements to call the Jucys-Murphy elements in other types. We chose our convention because under it the definition of the Jucys-Murphy element is uniform in all types, but elements $j_k^X$ for $X = B, D$ defined below arguably also deserve the name.  
\end{remark}
