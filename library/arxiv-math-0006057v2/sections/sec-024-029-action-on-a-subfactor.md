---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-024-029-action-on-a-subfactor
section_title: "Action on a subfactor"
section_number: 0.29
pages: 35-37
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.945
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
Equation~(\ref{good property}) suggests the following definition 
of the action of $B$ on $M_1$.

\begin{proposition}
\label{the action}
The map $\lact : B \otimes_\mathbb{C} M_1 \to M_1$ :
\begin{equation}
b \lact x = \lambda^{-1} E_{M_1}(b x e_2)
\end{equation}
defines a left action of $B$ on $M_1$ (cf.\ \cite{S}, Proposition 17).
\end{proposition}

\begin{proof}
The above map defines a left $B$-module structure
on $M_1$, since $1\lact x =x$ and
$$
b \lact (c \lact x) 
= \lambda^{-2}  E_{M_1}(b  E_{M_1}(c x e_2)  e_2) 
= \lambda^{-1}  E_{M_1}( bc x e_2 ) = (bc) \lact x.
$$
Next, using equation~(\ref{good property}) we get
\begin{eqnarray*}
b \lact xy 
&=& \lambda^{-1} E_{M_1}( b xy e_2)  
= \lambda^{-2} E_{M_1}( b\1 x e_2) E_{M_1}( b\2 y e_2) \\
&=& ( b\1 \lact x)( b\2 \lact y).
\end{eqnarray*}
By \cite{NV2}, 4.4 and properties of $S_B$ we also get
\begin{eqnarray*}
S(b)^\star \lact x^*
&=& \lambda^{-1} E_{M_1}( S(b)^\star x^* e_2 ) 
 = \lambda^{-1} E_{M_1}( S_B(w)^{-1} S_B(wbw^{-1})^* S_B(w) x^* e_2 ) \\
&=& \lambda^{-1} E_{M_1}( S_B(b^*)  x^* e_2 ) 
 =  \lambda^{-1} E_{M_1}( e_2  x^* b^* )  \\
&=&  \lambda^{-1} E_{M_1}( bx e_2)^* = (b \lact x)^*.
\end{eqnarray*}
Finally,
$$
b \lact 1 = \lambda^{-1} E_{M_1}( b e_2) = 
\lambda^{-1} E_{M_1}( \lambda^{-1} E_{M_1}(b e_2)e_2)
= \eps_t(b) \lact 1,
$$ 
and $b\lact 1 =0$  iff $\eps_t(b) = \lambda^{-1} E_{M_1}(b e_2)= 0$.
\end{proof}

\begin{proposition}
\label{fixed point}
$M_1^B = M$, i.e. $M$ is the fixed point subalgebra of $M_1$.
\end{proposition}

\begin{proof}
If $x\in M_1$ is such that $b\lact x = \eps_t(b)\lact x$ for all
$b \in B$, then $ E_{M_1}(bxe_2) = E_{M_1}(\eps_t(b)xe_2) =
E_{M_1}(be_2) x$. Taking $b =e_2$, we get $E_{M}(x) =x$ which
means that $x \in M$. Thus, $M_1^B \subset M$.

Conversely, if $x\in M$, then $x$ commutes with $e_2$ and 
$$
b\lact x = \lambda^{-1} E_{M_1}(b e_2 x) = 
\lambda^{-1} E_{M_1}( \lambda^{-1} E_{M_1}(be_2)e_2 x)
= \eps_t(b) \lact x,
$$
therefore $M_1^B = M$. 
\end{proof} 

\begin{proposition}
\label{crossproduct}
The map $\theta : [x\otimes b] \mapsto x S(w)^\half b S(w)^{-\half}$
defines a von Neumann algebra isomorphism between $M_1\rtimes B$ and $M_2$.
\end{proposition}

\begin{proof}
By definition of the action $\lact$ we have :
\begin{eqnarray*}
\theta([x(z\lact 1) \otimes b]) 
&=& x S(w)^{\half} \lambda^{-1} E_{M_1}(ze_2)b S(w)^{-\half} \\
&=& x S(w)^{\half} zb S(w)^{-\half} = \theta([x\otimes zb]),
\end{eqnarray*}
for all $x \in M_1,\, b\in B,\, z\in B_t$, so
$\theta$ is a well defined linear map from
$M_1\rtimes B = M_1 \otimes_{B_t} B$  to $M_2$.
 It is surjective since  an orthonormal basis of 
 $B=M^\prime \cap M_2$
over $B_t=M^\prime \cap M_1$ is also a basis of $M_2$ over $M_1$
(\cite{Po}, 2.1.3).
Finally, one can check that 
$\theta$ is a von Neumann algebra isomorphism (\cite{NV2}, 6.3).
\end{proof}
  
\begin{remark}
\label{minimality}
\begin{enumerate}
\item[(i)]
The action of $B$ constructed in Proposition~\ref{the action}
is minimal, since we have $M_1^\prime \cap M_1\rtimes B = M_1^\prime \cap M_2 
=B_s$ by Proposition~\ref{crossproduct}. 
\item[(ii)]
If $N'\cap M=\mathbb{C}$, then $B$ is a usual
Kac algebra (i.e., a Hopf $C^*$-algebra) and we recover the well-known
result proved in \cite{S}, \cite{L}, and \cite{D}.
\item [(iii)]
It is known (\cite{Po}, Section 5) that 
there are exactly 3 non-isomorphic subfactors of depth 2 
and index 4 of the hyperfinite II${}_1$ factor $R$ such that 
$N'\cap M \neq \mathbb{C}$. 
One of them is $R\subset R\otimes_\mathbb{C} M_2(\mathbb{C})$, 
two others can be viewed as diagonal subfactors of the form 
$$
\{  \begin{pmatrix} x & 0 \cr 0 & \alpha(x) \end{pmatrix}
\vert x\in R \} \subset R\otimes M_2(\mathbb{C}),
$$
where $\alpha$ is an outer automorphism of $R$  such that  
$\alpha^2 =\id$, resp.\ $\alpha^2$ is inner and $\alpha^2 \neq\id$. 

An explicit description of the corresponding quantum groupoids
can be found in (\cite{NV1}, 3.1, 3.2), (\cite {NV2}, 7). 
Also, in (\cite {NV2}, 7)  we describe the $C^*$-quantum groupoid 
$B=M_2(\mathbb{C}) \oplus M_3(\mathbb{C})$
corresponding to the subfactor with the principal graph $A_3$ (\cite{GHJ}, 
4.6.5) having  the index $\lambda^{-1} = 16\cos^4\frac{\pi}{5}$.
\end{enumerate}
\end{remark}

\end{section}





\begin{section} 
{$C^*$-quantum groupoids and subfactors : the finite depth case}

Here we show that
quantum groupoids give a description of  
arbitrary finite index and finite depth II$_1$ subfactors via
a Galois correspondence and  
explain how to express subfactor invariants such as bimodule
categories and principal graphs in quantum groupoid terms. 
Recall that the {\em depth} (\cite{GHJ}, 4.6.4) 
of a subfactor $N\subset M$ with finite index $\lambda^{-1}=[M:N]$ is
\begin{eqnarray*}
n &=& \min\{ k\in \mathbb{Z}^+ \mid \dim Z(N'\cap M_{k-2}) = \dim
Z(N'\cap M_k) \} \in \mathbb{Z}_+ \cup \{\infty\},
\end{eqnarray*}
where $N\subset M\subset M_1\subset M_2\subset\cdots$
is the corresponding Jones tower.
