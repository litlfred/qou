---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-010-general-markov-traces-in-types-b-d
section_title: "General Markov traces in types B, D."
section_number: null
pages: 7-9
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.993
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
\label{sec:gener-mark-trac-3}
In type $A$, the classical result of Jones and Ocneanu \cite{jonesHeckeAlgebraRepresentations1987} says that a Markov trace with given constants $\rho, \mu$ is defined uniquely up to an overall scaling. Thus, Theorem~\ref{sec:markov-traces-via} gives a general description of a Markov trace in type $A$.

In types $B, D$, the general description of Markov traces was obtained by Geck and Lambropoulou \cite{geckMarkovTracesKnot2004}, \cite{geckTraceFunctionsIwahoriHecke1998}. We recall their results.

For $n \geq 1$, define the elements
\[T_n = t_{n-1}\dots t_1 t_0 t_1^{-1}\dots t_{n-1}^{-1}\in \He(B_n), n \geq 2, T_1 = t_0,\]
and
\[U_n = t_{n-1}\dots t'_1 t_1^{-1}\dots t_{n-1}^{-1}\in \He(D_n), n \geq 2, U_1 = 1.\]

\begin{theorem}[\cite{geckMarkovTracesKnot2004}, \cite{geckTraceFunctionsIwahoriHecke1998}]
  \label{sec:gener-mark-trac-1}
 Let $\mathcal{R} = \mathcal{A}(a,y_1,\dots,y_n,\dots)$, with infinite number of variable $y_k$. There is a unique Markov trace $(\tr^X_{n,(y_{\bullet})})$, where $X$ is $B$ or $D$, with values in $\mathcal{R}$, with constants $\rho = 1 + a, \mu = v-v^{-1}$, normalization $\tr^{X}_{n,(y_\bullet)}(1) = (1+a)^n$ and additional properties:
  \begin{enumerate}
  \myitem[.]{(B)}\label{item:2} $\tr^{B}_{n,(y_{\bullet})}(T_1T_2 \dots T_n) = y_n$, $n \geq 1$, in type $B$.
  \myitem[.]{(D)}\label{item:7} $\tr^{D}_{2n,(y_{\bullet})}(U_1U_2 \dots U_{2n}) = y_{2n}$, $n \geq 1$, in type $D$.
  \end{enumerate}
Any Markov trace with the chosen $\rho, \mu$ and normalization is of this form.  Moreover, every such Markov trace in type $D$ is obtained by restriction from the Markov trace on $\He_{v,1}(B_n)$ (see Section \ref{sec:some-centr-elem}).
\end{theorem}

We will be interested in a particular case of these traces when $y_n$ is of the form $y_n = y^n.$ Let from now on $\mathcal{R} = \mathcal{A}(y)$ and denote by $\tr^{X}_{n,y}$ the Markov trace from Theorem \ref{sec:gener-mark-trac-1} with $y_n = y^n$ for all $n \geq 1$. Extend the bar involution to $\mathcal{R}$, formally writing $\overline{y}$ --- we assume that such an extension exists under any specialization of $y$ we will use. To simplify the formulas, we adopt the notation $\alpha = v - v^{-1}, \alpha_0 = v_0 - v_0^{-1}$.
Define the elements
\[
  \beta_n(y) = \prod_{i = 1}^n(1 + (\overline{y}+\alpha_0)j^B_i + a^{-1}J^B_i) \in \He_{v,v_0}(B_n) \otimes_\mathcal{A}\mathcal{R}.
\]
By Corollary \ref{sec:jucys-murphy-central}, the element $\beta_n(y)$ is central in $\He_{v,v_0}(B_n)\otimes_\mathcal{A}\mathcal{R}$. 
We have the following
\begin{theorem}
  \label{sec:gener-mark-trac-2}
  The equality $\tr_{n,y}^B = \tr_{\beta_n(y)}$ holds.
\end{theorem}
The property in Theorem \ref{sec:gener-mark-trac-1}~\ref{item:2} follows from the more general property (compare \cite[Proposition 4.5]{geckMarkovTracesKnot2004}).
\begin{proposition}
  \label{sec:gener-mark-trac-5}
 For any $h \in \He(B_{n-1})$, we have $\tr_{\beta_n(y)}(\iota(h)T_n) = y\tr_{\beta_{n-1}(y)}(h).$ 
\end{proposition}
\begin{proof}
   We will use the following lemma, verified by a direct computation.
  \begin{lemma}
    \label{sec:gener-mark-trac}
    \begin{enumerate}[label=(\alph*).,ref=(\alph*)]
    \item \label{item:8} We have $T_n^{-1} = T_n - \alpha_0.$
    \item \label{item:9} The elements $T_n, T_n^{-1}$ satisfy \[T_n \in \mathrm{span}_{\mathcal A}\langle t_w, w \in W(B_n)\backslash W(B_{n-1})\rangle\] and \[T_n^{-1} \in \mathrm{span}_{\mathcal A}\langle t_w^{-1}, w \in W(B_n)\backslash W(B_{n-1})\rangle.\]
    \item \label{item:10} The element $(j^B_n)^{-1}T_n$ satisfies \[(j^B_n)^{-1}T_n - 1\in \mathrm{span}_{\mathcal A}\langle t_w^{-1}, w \in W(B_n)\backslash W(B_{n-1})\rangle.\]
    \end{enumerate}
  \end{lemma}

  To simplify the formulas, introduce the notation $y' = y-\alpha_0, \overline{y'} = \overline{y}+\alpha_0$. We have
  \begin{equation*}
    \langle\beta_n(y), \iota(h)T_n\rangle = \langle\beta_{n-1}(y), \iota(h)T_n\rangle + {y'}\langle\beta_{n-1}(y)j^B_n,\iota(h)T_n\rangle +a\langle\beta_{n-1}(y)J_n^B, \iota(h)T_n\rangle.
  \end{equation*}
  Let us examine the summands on the right-hand side of this equation one by one. We will rutinely use the Corollary \ref{sec:trace-funct-pair-1}. For the first summand, we have, by Lemma \ref{sec:gener-mark-trac}~\ref{item:8}, \ref{item:9}, 
  \[
   \langle\beta_{n-1}(y), \iota(h)T_n\rangle = \langle\beta_{n-1}(y), \iota(h)T_{n}^{-1}\rangle + \alpha_0\langle\beta_{n-1}(y), \iota(h)\rangle = \alpha_0\langle\beta_{n-1}(y), \iota(h)\rangle.
  \]
  For the second summand, first note that $j^B_n$ is in the centralizer of $\He(X_{n-1})$ in $\He(X_n)$. It follows that
  \[
  {y'}\langle\beta_{n-1}(y)j^B_n,\iota(h)T_n\rangle = {y'}\langle\beta_{n-1}(y),\iota(h)(j_n^B)^{-1} T_n\rangle.
  \]
  Thus we have, by Lemma \ref{sec:gener-mark-trac}~\ref{item:10}, 
  \[
 {y'}\langle\beta_{n-1}(y),\iota(h)(j^{B}_n)^{-1}T_n\rangle = y'\langle\beta_{n-1}(y), \iota(h)\rangle.
  \]
  For the third summand, by Proposition \ref{sec:full-twist-jucys-1} and Lemma \ref{sec:gener-mark-trac}~\ref{item:9}, we have
  \[
    a\langle\beta_{n-1}(y)J_n^B, \iota(h)T_n\rangle = \overline{\langle\iota(h)T_n, \beta_{n-1}(y)\Se(B_{n-1})\rangle} = 0. 
  \]
  Collecting all three summands together, we get
  \[
    \langle\beta_n(y), \iota(h)T_n\rangle = (\alpha_0+y')\langle\beta_{n-1}(y),\iota(h)\rangle = y\langle\beta_{n-1}(y),\iota(h)\rangle,
  \]
  which completes the proof.
\end{proof}
\begin{proof}[Proof of Theorem \ref{sec:gener-mark-trac-2}.]
  It remains to check the properties \ref{item:5} and \ref{item:6}. Note that $j^B_n = t_{c}, j^B_nt_n^{-1} = t_{c'}$ for $c, c' \in W(B_n)\backslash W(B_{n-1})$. It follows from Corollary \ref{sec:trace-funct-pair-1}, that, for any $h\in \He(B_{n-1})$ we have
  \[
    \langle (\overline{y}+\alpha_0)\beta_{n-1}j_n^{B}, \iota(h) \rangle = 0 = \langle (\overline{y}+\alpha_0)\beta_{n-1}j_n^{B}, \iota(h)t_n\rangle,
  \]
  which reduces the proof to the proof of Theorem \ref{sec:markov-traces-via}.
\end{proof}
From Theorems \ref{sec:gener-mark-trac-1} and \ref{sec:gener-mark-trac-2} we get the following description of a Markov trace $\tr^D_{n,y}$.
\begin{corollary}
\label{sec:gener-mark-trac-4}  Let \[P_n(x_1, \dots, x_n;y) = \prod_{i=1}^n(1 + \overline{y}x_i + a^{-1}x_i^2),\] a symmetric polynomial in variables $(x_i)$ over $\mathcal{R}$. Write $P_n = P_n^+ + P_n^-$, a sum of even and odd monomial degree parts. Let $\delta_n(y) = P_n^+(j_1^D, \dots, j_n^D;y)$. Then $\tr_{n,y}^D = \tr_{\delta_n(y)}$.
\end{corollary}
\begin{proof}
  Recall that the trace $\tr_{n,(y_{\bullet})}^D$ is obtained by restriction of $\tr_{n,(y_{\bullet})}^B$ along the embedding $\iota_{D\to B}:\He(D_n) \to \He_{v,1}(B_n)$, so that we have
  \[
    \tr_{n,y}^D(h) = \langle \beta_n(y),\iota_{D\to B}(h)\rangle = \langle P(j_1^B,\dots,j_n^B;y),\iota_{D\to B}(h)\rangle.
  \]
  It remains to observe that for all $i$ we have $j_i^D = t_0j_i^B$, and so every even degree monomial in $j_i^B$ is equal to the same monomial in $j_i^D$, since $t_0^2 = 1$ in $\He_{v,1}(B_n)$ and $t_0$ commutes with $j_i^B$ for all $i$; and that every odd degree monomial in $j_i^B$ is orthogonal to $\iota_{D\to B}(h)$ with respect to $\langle\,,\rangle$. This completes the proof of the Corollary.
\end{proof}
We have the following analogue of Proposition \ref{sec:gener-mark-trac-5} in type $D$.
\begin{proposition}
  \label{sec:gener-mark-trac-6}
For $n \geq 1$ and any $h \in \He(D_{2n-2})$, we have \[\tr_{2n,y}^D(\iota\circ\iota(h)U_{2n-1}U_{2n}) = y^2\tr_{2n-2,y}^D(h).\]
\end{proposition}
\begin{proof}
 Note that we have $\iota_{D \to B}(U_k) = T_kt_0$, and so 
\[\tr_{2n,y}^D(\iota\circ\iota(h)U_{2n-1}U_{2n}) = \tr_{2n,y}^B(\iota\circ\iota(h)T_{2n-1}t_0T_{2n}t_0).\]
Using the property \ref{item:4} and Proposition \ref{sec:gener-mark-trac-5} twice, we get the result. 
\end{proof}
