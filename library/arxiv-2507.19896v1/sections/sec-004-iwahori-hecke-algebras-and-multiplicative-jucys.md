---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-004-iwahori-hecke-algebras-and-multiplicative-jucys
section_title: "Iwahori-Hecke algebras and multiplicative Jucys-Murphy elements."
section_number: null
pages: 2-4
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
text_source: latex
latex_prose_ratio: 0.837
latex_coverage_ratio: 0.815
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — WegiveasimpleconstructionofMarkovtracesforIwahori-Heckealgebrasassociated with infinite series of crystallographic Coxeter groups."
---
\label{sec:iwah-hecke-algebr-2}
\subsection{Coxeter groups.}
Let $(W, S), S = \{s_1, \dots, s_n\},$ be a Coxeter system. Thus, $W$ is a group with a presentation $(s_0, \dots, s_n | (s_is_j)^{m_{ij}} = e)$, where $m_{ij} \in \mathbb{Z}^+ \cup \{\infty\}$, with $m_{ii} = 1, m_{ji} = m_{ij} \geq 2$ if $i \neq j$, and $m_{ij} = \infty$ means that there is no relation included for the pair $s_i, s_j$. Such a presentation is read off the Coxeter diagram of $(W,S)$ in a standard way: such a diagram is a non-oriented graph with $S$ as a set of vertices, and $m_{ij} - 2$ edges between the vertices $s_i$ and $s_j$. Let $l: W \to \mathbb{Z}_{\geq 0}$ be the Bruhat length function with respect to $S$.

We will be primarily interested in Coxeter groups that are Weyl groups of classical types $A, B = C, D$. To fix the numeration of the generators, their Coxeter diagrams are presented below, with a vertex corresponding to $s_i \in S$ marked by $i$. The Coxeter diagram of type $A_n$ is \[\dynkin[arrows=false, edge length=0.6cm, backwards, labels={n,n-1,2,1}]A{},\] of type $B_n = C_n$ is
\[
  \dynkin[arrows=false, edge length=0.6cm, backwards, labels={n-1,,,1,0}]B{},
\]
and of type $D_n$ is 
\[
\dynkin[arrows=false, edge length=0.6cm, backwards, labels={n-1,,,2,1,1'}]D{}.
\]
When $n$ is small, these are interpreted in a standard way as follows: the Coxeter system $A_1 = B_1 = D_1$ has a single vertex, $D_2 = A_1 \times A_1$, $D_3 = A_3$. We also adopt the convention $A_0 = B_0 = D_0$ corresponding to the empty Coxeter graph and the trivial Coxeter group.

Many of the results and definitions in this paper are valid in types all types $A, B, D$, with definitions for type $A_{n-1}$ naturally fitting with definitions in types $B_n, D_n$. In this case, we will write ``type $X_n$, where $X$ is $A_{-1}$, $B$ or $D$'' (or something in a similar vein).  

\subsection{Iwahori-Hecke algebras.}
Let $\mathcal{A} = \mathbb{Q}(v)$. The Iwahori-Hecke algebra $\He_v(W,S) = \He(W,S)$ associated to a Coxeter system $(W,S)$ is a unital $\mathcal{A}$-algebra with generators $t_s, s \in S,$ subject to the relations
\begin{enumerate}[label=(\roman*).,ref=(\roman*)]
\item $\langle t_{s_i},t_{s_j}\rangle_{m_{ij}} = \langle t_{s_j},t_{s_i}\rangle_{m_{ij}}$, where $\langle x,y \rangle_{m}$ is an alternating product $xyx\dots$ of $x$ and $y$ with $m$ factors.
\item \label{item:1} $(t_s - v)(t_s + v^{-1}) = 0.$
\end{enumerate}
When $(W,S)$ is of type $B_n$ we will also be interested in the Iwahori-Hecke algebra $\He_{v,v_0}(W,S)$ with unequal parameters $v, v_0 \in \mathcal{A}$. This is a unital algebra over the ring $\mathcal{A}$, with the relation \ref{item:1} replaced by the relations
\begin{enumerate}[]
\item[(ii\textquotesingle).] $(t_{s_i} - v)(t_{s_i} + v^{-1}) = 0$ for $i > 1$,
\item[(ii\textquotesingle\textquotesingle).] $(t_{s_i} - v_0)(t_{s_i} + v_{0}^{-1}) = 0$.
\end{enumerate}


When $(W,S)$ is of type $X_n$ with $X \in \{A, B=C, D\}$, we will write $W(X_n)$ and $\He(X_n)$ for $W$ and $\He(W,S)$, or $\He_{v,v_0}(B_n)$ if we need to emphasize that we use unequal parameters. In each of these cases, we will write $t_i$ for $t_{s_i}$.

Let $w = s_{i_1}\dots s_{i_r}, w \in W, s_{i_k} \in S$ be a reduced expression. Then the element $t_w = t_{s_{i_1}}\dots t_{s_{i_r}}$ in $\He(W,S)$ is independent of the choice of a reduced expression, and $\He(W,S)$ is a free $\mathcal{A}$-module with a basis $t_w, w \in W$. The elements $t_w$ are invertible, and the collection $t_{w}^{-1}, w \in W,$ gives another basis of $\He(W,S)$ over $\mathcal{A}$. 

\subsection{Trace functional and a pairing on $\He(W,S)$.} Let $x \mapsto \overline{x}$ be the Kazhdan-Lusztig involution on $\He(W,S)$. It is a $\mathbb{Q}$-algebra involution, defined by the assignments $\overline{v} = v^{-1}, \overline{t_w} = t_{w^{-1}}^{-1}.$ Let $i:\He(W,S)$ stand for the $\mathcal{A}$-linear algebra anti-involution defined by $i(t_w) = t_{w^{-1}}$. 

For $h \in \He(W,S), x \in W,$ let $h_x$ stand for the $t_x^{-1}$-coefficient of $h$ in the basis $t_w^{-1},$ where $w$ runs through $W$. Let $\tau: \He(W,S) \to \mathcal{A}$ be a functional defined by  $\tau(h) = h_e,$ where $e \in W$ is the unit.  For $h, h' \in \He(W,S)$, define a pairing $\langle h, h' \rangle = \tau(i(\overline{h})h')$. We have the following standard proposition, see, for example, \cite[Chapter 8]{geck2000characters}.
\begin{proposition}[]
  \label{sec:trace-funct-pair}
  The functional $\tau$ and the pairing $\langle\, , \rangle$ satisfies the following properties.
  \begin{enumerate}[label=(\alph*)., ref=(\alph*)]
  \item The functional $\tau$ is an $\mathcal{A}$-linear trace on $\He(W,S),$ that is $\tau(hh') = \tau(h'h).$
  \item The pairing $\langle\, , \rangle$ is $\mathcal{A}$-antilinear in the first argument, $\mathcal{A}$-linear in the second argument and satisfies the orthogonality relation
    \(   \langle t_{w_1} , t^{-1}_{w_2} \rangle = \delta_{w_1, w_2^{-1}}.
    \)
   \item \label{item:3} We have \(\langle h_1h_2, h_3 \rangle = \langle h_1, h_3 i(\overline{h_2})\rangle = \langle h_2,  i(\overline{h_1})h_3\rangle\) for any $h_1, h_2, h_3 \in \He(W,S).$
  \end{enumerate}
\end{proposition}
We will use the following straightforward corollary of this proposition repeatedly.
\begin{corollary}
  \label{sec:trace-funct-pair-1}
  Let $(W',S')$ be a parabolic subgroup of $W$. Assume that $x, y \in \He(W',S') \subset \He(W,S)$, and assume that $z \in \mathrm{span}_\mathcal{A}\langle t_w, w \in W\backslash W'\rangle$ (resp. $z \in \mathrm{span}_\mathcal{A}\langle t_w^{-1}, w \in W\backslash W'\rangle$). Then $\langle xz, y \rangle = \langle zx, y \rangle = 0$ (resp. $\langle x, yz \rangle = \langle x, zy \rangle =0$).
\end{corollary}

\subsection{``Full twist'' and Jucys-Murphy elements.}\label{sec:full-twist-jucys} Assume that $(W, S)$ is of finite type. Let $w_0$ stand for the longest element in $W$ with respect to the Bruhat length. Let $\Se(W,S) = t_{w_0}^{-2} \in \He(W,S)$. In classical types, we will write $\Se(X_n) \in \He(X_n)$, when $X$ is $A, B$ or $D$, or simply $\Se$ when the type is clear from the context.  

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

\subsection{Some central elements in the classical Iwahori-Hecke algebras.}
\label{sec:some-centr-elem}
In this section we follow \cite{Ram2003}.
Let $\He^{\aff}(A_{n-1})$ be the affine Hecke algebra associated to the root datum of $\mathrm{GL}_n$. It is a unital algebra over $\mathcal{A}$ generated by the elements $t_1, \dots, t_{n-1}$ and $\Theta_1^{\pm 1}$, where $t_1, \dots, t_{n-1}$ satisfy the relations of the Iwahori-Hecke algebra of type $A_{n-1}$ and, additionally, the following relations hold:
\begin{enumerate}
\item[(iii).] $t_1\Theta_1 t_1\Theta_1 = \Theta_1 t_1 \Theta_1 t_1$,
\item[(iv).] $t_i\Theta_1 = \Theta_1 t_i$ for $i > 1$.
\end{enumerate}
Inductively define $\Theta_i = t_i\Theta_{i+1}t_i \in \He^{\aff}(A_{n-1}), i = 2, \dots, n$. It is well-known that $\Theta_i^{\pm 1}$ generate a commutative subalgebra of $\He^{\aff}(A_{n-1})$, called the Bernstein subalgebra. We have the following particular case of a classical theorem, proved in \cite[Theorem 8.1]{lusztigSingularitiesCharacterFormulas1983} for all affine types.  
\begin{theorem}
 The center of $\He^{\aff}(A_{n-1})$ consists of the symmetric Laurent polynomials in $\Theta_1, \dots, \Theta_{n}$. 
\end{theorem}

Fix $n \geq 2$. Note that
\begin{enumerate}[label=(\roman*).,ref=(\roman*)]
\item The Hecke algebra $\He(A_{n-1})$ is the quotient of the affine Hecke algebra $\He^{\aff}(A_{n-1})$ by the relation $\Theta_1 = 1$.
\item\label{item:11} The Hecke algebra $\He_{v,v_0}(B_n)$ is the quotient of $\He^{\aff}(A_{n-1})$ by the relation \[(\Theta_1 - v_0)(\Theta_1 + v_0^{-1}) = 0.\] Here $t_0$ is the image of $\Theta_1$.
\item The Hecke algebra $\He(D_n)$ is the subalgebra of the quotient \ref{item:11} with $v_0 = 1$,  ge\-ne\-ra\-ted by the images of $\Theta_1 t_1 \Theta_1^{-1}, t_1, \dots, t_{n-1}$. Here $t_{1'}$ is the image of $\Theta_1 t_1 \Theta_1^{-1}$.
\end{enumerate}
Note that this exhibits $\He(D_n)$ as a subalgebra of $\He_{v,1}(B_n)$.
Note also that $J^A_i$ is the image of $\Theta_i$ in $\He(A_{n-1})$ for $i = 1, \dots, n$. We have \[J^A_{i} = t_{i-1}\dots t_1t_1 \dots t_{i-1}.\]

\begin{definition}
  We define the following families of elements in the Hecke algebras of finite types $B, D$:
  \begin{enumerate}[]
  \item[(B).] Let $j^B_i$ be the image of $\Theta_i, i = 1, \dots, n,$ in $\He(B_{n})$. We have \[j^B_{i} = t_{i-1}\dots t_1t_0t_1 \dots t_{i-1}.\]
    and $J^B_i = (j^B_i)^2.$
  \item[(D).] Let $j^D_i$ be the image of $\Theta_i\Theta_1^{-1}, i = 1, \dots, n,$ in $\He(D_{n})$. We have \[j^D_{i} = t_{i-1}\dots t_2t_1't_1t_2 \dots t_{i-1}, i \geq 2, j_1^D = 1.\]
    and $J^D_i = (j^D_i)^2.$
  \end{enumerate}
\end{definition}
We have the following
\begin{corollary}
 \label{sec:jucys-murphy-central} 
 The elements $J^A_i$ (resp. $j^B_i, j^D_i$) commute with each other. If $P$ is a symmetric polynomial in $n$ variables, $P(J^A_1, \dots, J^A_n)$ (resp. $P(j^B_1, \dots, j^B_n)$) is central in $\He(A_n)$ (resp. in $\He_{v,v_0}(B_n)$). If $P$ is homogeneous of even degree, then $P(j^D_1, \dots, j^D_n)$ is central in $\He(D_n)$. 
\end{corollary}
