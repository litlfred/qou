---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-005-22-weyl-modules-dual-weyl-modules-and-simple-mod
section_title: "Weyl modules, dual Weyl modules and simple modules"
section_number: 2.2
pages: 6-8
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.913
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-wsmod}



\begin{defn}(\textbf{Weyl, dual Weyl and simple modules})\label{defn-weyl}
Let $i\in\bN$ and denote 
by $\Vn i$ the $i$\textit{-th Weyl module}. 
This is the $\bC$-vector space 
with basis $m_0,\dots,m_i$ and an $\Uq$-action defined by
\[
Km_k=q^{i-2k}m_k,\quad\quad E^{(j)}m_k=\qbin{i-k+j}{j}m_{k-j},\quad\quad F^{(j)}m_k=\qbin{k+j}{j}m_{k+j},
\]
with the convention that $m_{<0}=m_{>i}=0$. 
The \textit{$i$-th dual Weyl module}, 
denoted by $\dVn i$, is obtained from 
$\Vn i$ by taking the dual, that is, 
$\Hom_{\mathbb{Q}(q)}(\Vn i,\bC)=(\Delta_q(i))^*=\dVn i$.
\end{defn}


It is easy to check directly that 
$\Vn i$ has a \textit{unique simple head} $\Ln i$ which 
is also the \textit{unique simple socle} of $\dVn i$. 
See also~\cite[Section~4]{apw}.



\begin{ex}\label{ex-weyl}
Let $q=\frac{-1+\sqrt{-3}}{2}$ (we use this $q$ in all examples with $l=3$ in what follows).



The Weyl module $\Vn 3$ can be visualized as
\begin{equation}\label{eq-example1}
\xymatrix{
  m_3  \ar@<2pt>[r]^{+1}\ar@(ul,ur)|{q^{-3}}  &  {\color{colormy}m_2}  \ar@[mycolor]@<2pt>[l]^{{\color{mycolor} 0}}\ar@[colormy]@<2pt>[r]^{{\color{colormy} -1}}\ar@[colormy]@(ul,ur)|{{\color{colormy}q^{-1}}} & {\color{colormy}m_1}  \ar@[mycolor]@<2pt>[r]^{{\color{mycolor} 0}}\ar@[colormy]@<2pt>[l]^{{\color{colormy}-1}}\ar@[colormy]@(ul,ur)|{{\color{colormy}q^{+1}}}  &  m_0.  \ar@<2pt>[l]^{+1}\ar@(ul,ur)|{q^{+3}} \\
}
\end{equation}
Here the action of 
$E$ points right, the action of 
$F$ left, $E^{(3)}m_3=m_0$, $F^{(3)}m_0=m_3$, $K$ acts as a loop 
and all other actions are zero. 
Thus, the $\mathrm{A}$-span of $\{m_1,m_2\}$ is now, 
in contrast to the classical case, stable under the action of $\Uq$. The complement 
however is not an $\Uq$-submodule.



Another example (where we have excluded the actions of the divided powers) is $\Vn{4}$:
\begin{equation}\label{eq-example2}
\xymatrix{
  m_4  \ar@<2pt>[r]^{+1}\ar@(ul,ur)|{q^{-4}}  &  m_3  \ar@<2pt>[l]^{+1}\ar@<2pt>[r]^{-1}\ar@(ul,ur)|{q^{-2}} & {\color{green} m_2}  \ar@[mycolor]@<2pt>[r]^{{\color{mycolor} 0}}\ar@[red]@<2pt>[l]^{{\color{mycolor} 0}}\ar@[colormy]@(ul,ur)|{{\color{colormy}q^{0}}} & m_1  \ar@<2pt>[r]^{+1}\ar@<2pt>[l]^{-1}\ar@(ul,ur)|{q^{+2}} &  m_0.  \ar@<2pt>[l]^{+1}\ar@(ul,ur)|{q^{+4}} \\
}
\end{equation}
We note that $\Vn{4}$ has the 
trivial $\Uq$-module spanned by $m_2$ as a $\Uq$-submodule.
\end{ex}




$K$ acts on $\Vn i$ via the eigenvalues $q^{-i},q^{-i+2},\dots,q^{i-2},q^{+i}$. 
Thus, by~\eqref{eq-eigen}, the same is 
true for $\dVn i$. Moreover, the 
$\Ln i$ are self-dual, see e.g.~\cite[Section~4]{apw}.




\begin{prop}\label{prop-weyl}
We have the following.
\begin{itemize}
\item[(a)] $\Vn i\cong\Ln i$ iff $i<l$ or $i\equiv -1\mod l$.
\item[(b)] Suppose $i=al+b$ for 
some $a,b\in\bN$ with $b\leq l-2$. 
Set $i^{\prime}=(a+2)l-b-2$. Then there exists a short exact sequence
\[
0\longrightarrow \Ln i\hooklongrightarrow\Vn{i^{\prime}}\twoheadlongrightarrow \Ln{i^{\prime}}\longrightarrow 0.
\]
Moreover, $\Ln{i^{\prime}}$ is the 
head and $\Ln i$ is the socle of $\Vn{i^{\prime}}$.\makeqed
\end{itemize}
\end{prop}


\begin{proof}
This is~\cite[Corollary~4.6]{apw}.
\end{proof} 
\begin{cor}\label{cor-weyl}
We have the following.
\begin{itemize}
\item[(a)] $\dVn i\cong\Ln i$ iff $i<l$ or $i\equiv -1\mod l$.
\item[(b)] Suppose $i=al+b$ for some 
$a,b\in\bN$ with $b\leq l-2$. Set $i^{\prime}=(a+2)l-b-2$. 
Then there exists a short exact sequence
\[
0\longrightarrow L_q(i^{\prime})\hooklongrightarrow\nabla_q(i^{\prime})\twoheadlongrightarrow \Ln i\longrightarrow 0.
\]
Moreover, $\Ln{i^{\prime}}$ is the socle and 
$\Ln i$ is the head of $\dVn{i^{\prime}}$.\makeqed
\end{itemize}
\end{cor}



\begin{proof}
This follows from $\Ln i\cong(\Ln i)^*$ and 
the fact that ${}^*$ is an exact, contravariant functor.
\end{proof}



\begin{ex}\label{ex-weyl2}
For $i=0$ and $l=3$ we have $i^{\prime}=4$. 
The trivial $\Uq$-module $\Ln 0$ appears as a 
submodule of $\Vn 4$, compare to~\eqref{eq-example2}.
\end{ex}



We should note here that 
there are two different 
types of $\Uq$-modules known as \textit{type} $1$ \textit{and} $-1$, 
see for example~\cite[Section 1]{apw}. 
For us the difference between the two types is not important 
in this paper and we \textit{only} consider $\Uq$-modules of type $1$. 
The (more general) treatment in~\cite[Section 1]{apw} 
ensures that the consideration of only type 
$1$ is still enough to get results for both types.



\begin{cor}\label{cor-simples}
The set $\{\Ln i\mid i\in\bN\}$ is a  
complete set of simple, pairwise non-isomorphic, 
finite-dimensional $\Uq$-modules (of type $1$).\makeqed
\end{cor}


\begin{proof}
See~\cite[Corollary~6.3]{apw}.
\end{proof}



\begin{rem}\label{rem-semisimple}
The category of $\Uq$-modules is 
\textit{far} from being semisimple: Proposition~\ref{prop-weyl} 
says that $\Vn i$ is never simple whenever we are in the case (b). 
See also~\eqref{eq-example1}.
\end{rem}
