---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-009-010-hopf-modules
section_title: "Hopf modules"
section_number: 0.10
pages: 11-13
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.809
latex_coverage_ratio: 0.947
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
Since a quantum groupoid $H$ is both algebra and coalgebra, one 
can consider modules and comodules over $H$. As in the theory of 
Hopf algebras, an $H$-Hopf module is an $H$-module which is also 
an $H$-comodule such that these two structures are compatible 
(the action ``commutes'' with coaction) :

\begin{definition}
\label{Hopf module}
A right $H$-Hopf module is such a $k$-vector space $M$ that
\begin{enumerate}
\item[(i)]
$M$ is a right $H$-module via $m\otimes h \mapsto m\cdot h$,
\item[(ii)]
$M$ is a right  $H$-comodule via $m\mapsto \rho(m) = m\0 \otimes m\I$,
\item[(iii)]
$(m\cdot h)\0 \otimes (m\cdot h)\I = m\0 \cdot h\1 \otimes m\I h\2$
\end{enumerate}
for all $m\in M$ and $h\in H$.
\end{definition}

\begin{remark}
Condition (iii) above means that $\rho$ is a right $H$-module map,
where $(M\otimes H)\Delta(1)$ is a right $H$-module via
$(m\otimes h)\Delta(1)\cdot h = (m\cdot h\1)\otimes (h\cdot h\2)$.
\end{remark} 

\begin{example}
$H$ itself is an $H$-Hopf module via $\rho =\Delta$.
\end{example}

\begin{example}
\label{dual Hopf module}
The dual vector space $\widehat H$
becomes a right $H$-Hopf module :
$$
\phi\cdot h = S(h)\act \phi \qquad 
\phi\0 \la \psi,\, \phi\I \ra =\psi\phi,
$$
for all $\phi,\psi\in \widehat H,\, h\in H$. Indeed, we need to check that
$$
(\phi\cdot h)\0 \otimes (\phi\cdot h)\I =
\phi\0\cdot h\1 \otimes \phi\1 h\2, \qquad \phi\in \widehat H, h\in H.
$$ 
Evaluating both sides against $\psi\in \widehat H$ in the first factor
we have :
\begin{eqnarray*}
(\phi\0\cdot h\1) \la \psi,\, \phi\1h\1 \ra
&=& (\psi\1 \phi)\cdot h\1 \la \psi\2,\, h\2 \ra \\
&=& \psi\1 \phi\1 \la S(\psi\2\phi\2),\, h\1 \ra \la \psi\3,\, h\2 \ra \\
&=& \psi\1 \phi\1 \la S^{-1}\eps_s(\psi\2)\phi\2,\,S(h) \ra \\
&=& \psi\phi\1 \la \phi\2,\, S(h) \ra \\ 
&=& \psi (S(h)\act \phi) = \psi(\phi\cdot h) \\
&=& (\phi\cdot h)\0 \la \psi,\, (\phi\cdot h)\I \ra.
\end{eqnarray*}
where we used Proposition~\ref{separability} and that
$S^{-1}\eps_s(\psi) \in \widehat H_t$ for all $\psi\in \widehat H$. 
\end{example}

The fundamental theorem for Hopf modules over Hopf algebras
([M], 1.9.4) generalizes to quantum groupoids as follows :

\begin{theorem}[\cite{BNSz}, 3.9]
\label{fundamental theorem}
Let $M$ be a right $H$-Hopf module
and 
\begin{equation}
N= Coinv M = \{m\in M \mid m\0\otimes m\I = m1\1 \otimes 1\2 \}
\end{equation}
be the set of coinvariants. The $H_t$-module tensor product $N\otimes_{H_t} H$
(where $N$ is a right $H_t$-submodule) is a right $H$-Hopf module via
\begin{equation}
(n\otimes h)\cdot g =n\otimes hg,
\qquad
(n\otimes h)\0 \otimes (n\otimes h)\I = (n\otimes h\1)\otimes h\2,
\end{equation}
for all $h,g\in H$ and $n\in N$. Then the map
\begin{equation}
\alpha : N\otimes_{H_t} H \to M : n\otimes h \mapsto n\cdot h
\end{equation}
is an isomorphism of right Hopf modules.
\end{theorem}

\begin{proof}
Proposition~\ref{counital properties}(iii) implies that 
the $H$-Hopf module structure on $M$ is well defined, and it is 
easy to check that $\alpha$ is a well defined homomorphism of 
$H$-Hopf modules. We will show that
\begin{equation}
\beta : M\to N\otimes_{H_t} H : m \mapsto (m\0 \cdot S(m\I))\otimes m\II
\end{equation}
is an inverse of $\alpha$. First, we observe that 
$m\0 \cdot S(m\I) \in N$ for all $m\in M$, since
\begin{eqnarray*}
\rho(m\0 \cdot S(m\I))
&=& (m\0 \cdot S(m\III)) \otimes m\I S(m\II) \\
&=& (m\0 \cdot S(1\2m\I) \otimes S(1\1) \\
&=& (m\0 \cdot S(m\I)1\1) \otimes 1\2,
\end{eqnarray*}
so $\beta$ maps to $N\otimes_{H_t} H$. Next, we check that it is both
module and comodule map :
\begin{eqnarray*}
\beta(m\cdot h) 
&=& m\0 \cdot h\1 S(m\I h\2) \otimes m\II h\3 \\
&=& m\0 \cdot \eps_t(h\1) S(m\I) \otimes m\II h\2 \\
&=& m\0 \cdot S(m\I 1\1) \otimes m\II  1\2h =\beta(m) \cdot h, \\
\beta(m\0) \otimes  m\I
&=& m\0 \cdot S(m\I) \otimes m\II \otimes m\III \\
&=& \beta(m)\0 \otimes \beta(m)\I,  
\end{eqnarray*}
Finally, we verify that $\alpha\circ \beta =\id$
and $\beta\circ\alpha = \id$ :
\begin{eqnarray*}
\alpha\circ \beta(m)
&=& m\0 \cdot S(m\I)m\II = m\0 \cdot \eps_s(m\I) \\
&=& m\0 \cdot 1\1\eps(m\I 1\2) = m\0 \eps(m\I) = m, \\
\beta\circ\alpha(n\otimes h)
&=& \beta(n\cdot h) = \beta(n) \cdot h \\
&=& n \cdot 1\1S(1\2) \otimes 1\3h = n \otimes h, 
\end{eqnarray*}
which completes the proof.
\end{proof}

\begin{remark}
\label{integrals are invariants}
$\int_{\widehat H}^l = \Coinv \widehat H$ where $\widehat H$ is 
an $H$-Hopf module as in Example~\ref{dual Hopf module}.
Indeed, the condition
$$
\lambda\I \otimes \lambda\II = \lambda\cdot 1\1 \otimes 1\2
$$
is equivalent to $\phi\lambda\ =(S(1\1)\act \lambda)\la \phi,\, 1\2\ra
= \eps_t(\phi)\lambda$.
\end{remark}

\begin{corollary}
\label{FT for integrals}
$\widehat H \cong \int_{\widehat H}^l \otimes_{H_t} H$ as right $H$-Hopf 
modules. In particular,  $\int_{\widehat H}^l$ is a non-zero subspace 
of $\widehat H$.
\end{corollary}

\begin{proof}
Take $M=\widehat H$ in Theorem \ref{fundamental theorem} and
use Remark~\ref{integrals are invariants}.
\end{proof}


\subsection{Maschke's Theorem}
The existence of left integrals in quantum groupoids
leads to the following generalization of Maschke's Theorem,  
well-known for Hopf algebras ([M], 2.2.1).

\begin{theorem}[\cite{BNSz}, 3.13]
\label{maschke}
Let $H$ be a finite quantum groupoid, then the following conditions
are equivalent :
\begin{enumerate}
\item[(i)] $H$ is semisimple,
\item[(ii)] There exists a normalized left integral $l$ in $H$, 
\item[(iii)] $H$ is separable. 
\end{enumerate}
\end{theorem}

\begin{proof}
(i) $\Rightarrow$ (ii) : Suppose that $H$ is semisimple, 
then since $\Ker\eps_t $ is a left ideal in $H$ we have 
$\Ker\eps_t =Hp$ for some idempotent $p$. Therefore,
$\Ker\eps_t (1-p) =0$ and $l=1-p$ is a left integral
by Lemma~\ref{integral properties}(iv). It is normalized since
$\eps_t(l) = 1-\eps_t(p) =1$. (ii) $\Rightarrow$ (iii) :
if $l$ is normalized then $l\1 \otimes S(l\2)$ is a separability
element of $H$ by Lemma~\ref{integral properties}(ii). 
(iii) $\Rightarrow$ (i) : this is a standard result \cite{P}.
\end{proof}

\begin{corollary}
\label{kG is semisimple}
Let $G$ be a finite groupoid and for every $e\in G^0$,
where $G^0$ denotes the unit space of $G$, let
$|e|=\#\{g\in G\mid gg^{-1}=e\}$. Then $kG$ is semisimple
iff $|e|\neq 0$ in $k$ for all $e\in G^0$.
\end{corollary}

\begin{proof}
In the notation of Example~\ref{examples of integrals}(i)
the element $l=\sum_{e\in G^0}\, \frac{1}{|e|}l_e$ is a normalized
integral in $kG$.
\end{proof}

Given a left integral $l$, one can show (\cite{BNSz}, 3.18) that 
if there exists $\lambda\in \widehat H$ such that $\lambda\act l=1$, then it 
is unique, it is a left integral in $\widehat H$ and $l\act\lambda=\widehat 1$. 
Such a pair $(l,\lambda)$ is called a {\em dual pair} of left integrals. 
One defines dual pairs of right integrals in a similar way.

\end{section}






\begin{section} 
{Actions and smash products}
