---
doc_id: arxiv-1010.4386v5
doc_title: "ON THE HOMOLOGY OF COMPLETION AND TORSION"
section_id: sec-006-6-mgm-equivalence
section_title: "MGM Equivalence"
section_number: 6
pages: 24-28
source_pdf: 1010.4386v5.pdf
source_sha256: 168226dbb5a479ed
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.96
doc_brief: "ON THE HOMOLOGY OF COMPLETION AND TORSION — Let A be a commutative ring, and a a weakly proregular ideal in A."
---
\label{sec:MGM}

In this section $A$ is a commutative ring. We do not assume
that $A$ is noetherian or complete.
Weak proregularity was defined in Definition \ref{dfn:250}.
Recall that any finite sequence in a noetherian ring is weakly proregular, and
any ideal in a noetherian ring is weakly proregular (Theorem \ref{thm:253}).

\begin{lem} \label{lem:4.1}
Let $\bsym{a}$ be a finite sequence in $A$, let $\a$ be the ideal generated 
by $\bsym{a}$, and let $M$ be
an $A$-module. Then the homomorphism 
\[ \Lambda_{\a}(e_{\bsym{a}, \infty}^{\vee} \ot 1_M) :
\Lambda_{\a} \bigl( \opn{K}^{\vee}_{\infty}(A; \bsym{a}) \otimes_A M \bigr) 
\to \Lambda_{\a} (M) \]
\tup{(}see \tup{(\ref{eqn:213}))} is an isomorphism of complexes.
\end{lem}

\begin{proof}
Since $\opn{K}^{\vee}_{\infty}(A; \bsym{a})^0 = A$, we have 
$\opn{K}^{\vee}_{\infty}(A; \bsym{a})^0 \otimes_A M \cong M$.
We will prove that 
$\Lambda_{\a} ( \opn{K}^{\vee}_{\infty}(A; \bsym{a})^i \otimes_A M ) = 0$
for $i > 0$. Now 
$\opn{K}^{\vee}_{\infty}(A; \bsym{a})^i$ is a direct sum of modules 
$N_{i, j}$, where $N_{i, j}$ is an $A[a_j^{-1}]$-module. 
Since 
\[ (A / \a^k) \otimes_A  N_{i, j} \otimes_A M = 0 \]
for any $k \in \N$, in the limit we get 
$\Lambda_{\a}(N_{i, j} \otimes_A M) = 0$.
\end{proof}

\begin{lem} \label{lem:263}  
Let $\a$ be a weakly proregular ideal in $A$.    
For any complex $M \in \cat{D}(\cat{Mod} A)$ the morphism 
\[ \mrm{L} \Lambda_{\a}(\sigma^{\mrm{R}}_M) : 
\mrm{L} \Lambda_{\a} (\mrm{R} \Gamma_{\a} (M)) \to \mrm{L} \Lambda_{\a} (M) \]
is an isomorphism.
\end{lem}

\begin{proof}
Choose a weakly proregular generating sequence $\bsym{a}$ for the ideal $\a$,
and a K-flat resolution $P \to M$ in $\cat{C}(\cat{Mod} A)$. The complex 
$\opn{K}^{\vee}_{\infty}(A; \bsym{a}) \otimes_A P$ is also K-flat. 
By  Corollary \ref{cor:kosz.1} and Proposition \ref{prop:26}, the morphism
$\mrm{L} \Lambda_{\a}(\sigma^{\mrm{R}}_M)$
can be replaced by the homomorphism of complexes
\begin{equation} \label{eqn:34}
\Lambda_{\a} (e_{\bsym{a}, \infty}^{\vee} \ot 1_P) : 
\Lambda_{\a} \bigl( \opn{K}^{\vee}_{\infty}(A; \bsym{a}) \otimes_A P \bigr) 
\to \Lambda_{\a} (P) .
\end{equation}
But by the previous lemma, the homomorphism (\ref{eqn:34}) is actually an
isomorphism in $\cat{C}(\cat{Mod} A)$.
\end{proof}

\begin{lem} \label{lem:202}
Let $\bsym{b} = (b_1, \ldots, b_n)$ be a sequence of nilpotent elements in a
ring $B$. Then 
$u_{\bsym{b}} : \opn{Tel}(B; \bsym{b}) \to B$
is a homotopy equivalence.
\end{lem}

\begin{proof}
Recall that 
$u_{\bsym{b}} = e_{\bsym{b}, \infty}^{\vee} \circ w_{\bsym{b}}$,
where 
$ w_{\bsym{b}} : \opn{Tel}(B; \bsym{b}) \to 
\opn{K}^{\vee}_{\infty}(B; \bsym{b})$
is a quasi-isomorphism.
By formulas (\ref{eqn:202}) and (\ref{eqn:210}) we see that 
$\opn{K}^{\vee}_{\infty}(B; \bsym{b})^i = 0$ for $i > 0$,
so $e_{\bsym{b}, \infty}^{\vee}$ is an isomorphism.
We conclude that $u_{\bsym{b}}  : \opn{Tel}(B; \bsym{b}) \to B$ is a
quasi-isomorphism. 
But these are bounded complexes of free $B$-modules, and hence 
$u_{\bsym{b}}$ is a homotopy equivalence.
\end{proof}

\begin{lem} \label{lem:tel.2}
Let $\bsym{a}$ be a finite sequence in $A$, and let 
$B := A / (\bsym{a}^j)$ for some $j \geq 1$.
Let $N$ be a complex of $A$-modules, whose cohomology $\mrm{H}(N)$ is
bounded, and such that each $\mrm{H}^k(N)$ is a $B$-module. Then  the
homomorphism
\[ \opn{Hom}(u_{\bsym{a}}, 1_N) : N \to 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), N \bigr) \]
is a quasi-isomorphism.
\end{lem}

\begin{proof}
Using smart truncation and induction on $\opn{amp}(\mrm{H}(N))$, 
i.e.\ by the way-out argument of \cite[Proposition I.7.1]{RD}, we may assume
that $N$ is a single $B$-module.

Let $\bsym{b}$ denote the image of the sequence $\bsym{a}$ in $B$. Then
$\opn{Tel}(B; \bsym{b}) \cong B \otimes_A \opn{Tel}(A; \bsym{a})$
as complexes. By Hom-tensor adjunction there is an isomorphism of complexes 
\[ \opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), N \bigr) \cong 
\opn{Hom}_{B} \bigl( \opn{Tel}(B; \bsym{b}), N \bigr) . \]
It suffices then to prove that 
\[  \opn{Hom}(u_{\bsym{b}}, 1_N) : N \cong \opn{Hom}_B(B, N)  \to 
\opn{Hom}_B \bigl( \opn{Tel}(B; \bsym{b}), N \bigr)  \]
is a quasi-isomorphism. By Lemma  \ref{lem:202} we know that 
$u_{\bsym{b}}$ is a homotopy equivalence; and therefore 
$\opn{Hom}(u_{\bsym{b}}, 1_N)$ is a quasi-isomorphism. 
\end{proof}

\begin{lem}  \label{lem:264}  
Let $\a$ be a weakly proregular ideal in $A$. 
For any complex $M \in \cat{D}(\cat{Mod} A)$ the morphism 
\[ \mrm{R} \Gamma_{\a}(\tau^{\mrm{L}}_M) : 
\mrm{R} \Gamma_{\a} (M) \to \mrm{R} \Gamma_{\a} (\mrm{L} \Lambda_{\a} (M)) \]
is an isomorphism.
\end{lem}

\begin{proof}
By Corollary \ref{cor:tel.1} we can replace $\tau^{\mrm{L}}_M$ with 
\[ \opn{Hom}(u_{\bsym{a}}, 1_M) : M \to 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), M \bigr) \]
And by Proposition \ref{prop:251} we can replace 
$\mrm{R} \Gamma_{\a}(\tau^{\mrm{L}}_M)$ with 
\begin{equation} \label{eqn:257}
\begin{aligned}
& 1_{\opn{Tel}} \ot \opn{Hom}(u_{\bsym{a}}, 1_M) :
\opn{Tel}(A; \bsym{a}) \ot_A M
\\ & \quad  \qquad 
\to \opn{Tel}(A; \bsym{a}) \ot_A 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), M \bigr) .
\end{aligned} 
\end{equation}
We will prove that (\ref{eqn:257}) is a quasi-isomorphism.

In view of Proposition \ref{prop:1.1} we can assume that $M$ is a single
$A$-module. Since direct limits commute with cohomology, it suffices to prove
that 
\begin{equation} \label{eqn:258}
\begin{aligned}
& 1_{\opn{Tel}_j} \ot \opn{Hom}(u_{\bsym{a}}, 1_M) :
\opn{Tel}_j(A; \bsym{a}) \ot_A M
\\ & \quad  \qquad 
\to \opn{Tel}_j(A; \bsym{a}) \ot_A 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), M \bigr) .
\end{aligned} 
\end{equation}
is a quasi-isomorphism for every $j$. 
Now $\opn{Tel}_j(A; \bsym{a})$ is a bounded complex of finite rank free
$A$-modules, so we can replace (\ref{eqn:258}) with 
\[ \opn{Hom}(u_{\bsym{a}}, 1_N) : N \to
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), N \bigr) , \]
where 
$N := \opn{Tel}_j(A; \bsym{a}) \ot_A M$. 
The complex $N$ satisfies the assumption of Lemma \ref{lem:tel.2}, and
therefore $\opn{Hom}(u_{\bsym{a}}, 1_N)$ is a quasi-isomorphism.
\end{proof}

\begin{lem}  \label{lem:265}
For a finite sequence $\bsym{a}$ of elements of $A$, the homomorphisms
\[ u_{\bsym{a}} \otimes 1_{\opn{Tel}} , \, 
1_{\opn{Tel}} \otimes u_{\bsym{a}} :
\opn{Tel}(A; \bsym{a}) \otimes_A \opn{Tel}(A; \bsym{a}) 
\to \opn{Tel}(A; \bsym{a}) \]
are homotopy equivalences.
\end{lem}

\begin{proof}
Because of Lemmas \ref{lem:260} and \ref{lem:201} these are quasi-isomorphisms. 
But a quasi-isomorphism between K-projective complexes is a homotopy
equivalence.
\end{proof}

\begin{prop} \label{prop:260}
Let $\a$ be a weakly proregular ideal in $A$. 
For any $M \in \cat{D}(\cat{Mod} A)$ the morphism 
\[ \tau^{\tup{L}}_{\mrm{L} \Lambda_{\a} (M)}  : \mrm{L} \Lambda_{\a} (M) \to 
\mrm{L} \Lambda_{\a} (\mrm{L} \Lambda_{\a} (M))  \]
is an isomorphism. So the functor
\[ \mrm{L} \Lambda_{\a} : 
\cat{D}(\cat{Mod} A) \to \cat{D}(\cat{Mod} A) \]
is idempotent.
\end{prop}

\begin{proof}
Choose some weakly proregular sequence $\bsym{a}$ that generates $\a$. 
According to Corollary \ref{cor:tel.1} we can replace 
$\tau^{\tup{L}}_{\mrm{L} \Lambda_{\a} (M)}$
with 
\[ \opn{Hom}(1_{T}, \opn{Hom}(u_{\bsym{a}}, 1_M)) :
\opn{Hom}_A ( T , M ) \to
\opn{Hom}_A \bigl( T , \opn{Hom}_A (T , M) \bigr) , \]
where $T := \opn{Tel}(A; \bsym{a})$.
Using Hom-tensor adjunction this can be replaced by 
\[ \opn{Hom}(1_{T} \ot u_{\bsym{a}}, 1_M ) : \opn{Hom}_A ( T , M ) \to
\opn{Hom}_A (T \ot_A T , M) . \]
By Lemma \ref{lem:265} this is a quasi-isomorphism.
\end{proof}

\begin{thm}[MGM Equivalence] \label{thm:26}
Let $A$ be a ring, and let $\a$ be a weakly proregular ideal in it. 
\begin{enumerate}
\item For any $M \in \cat{D}(\cat{Mod} A)$ one has
$\mrm{R} \Gamma_{\a} (M) \in \cat{D}(\cat{Mod} A)_{\a \tup{-tor}}$
and 
$\mrm{L} \Lambda_{\a} (M) \in \cat{D}(\cat{Mod} A)_{\a \tup{-com}}$.

\item The functor 
\[ \mrm{R} \Gamma_{\a} : \cat{D}(\cat{Mod} A)_{\a \tup{-com}} \to 
\cat{D}(\cat{Mod} A)_{\a \tup{-tor}} \]
is an equivalence, with quasi-inverse $\mrm{L} \Lambda_{\a}$.
\end{enumerate}
\end{thm}

\begin{proof}
(1) This is immediate from the idempotence of the functors 
$\mrm{R} \Gamma_{\a}$ and $\mrm{L} \Lambda_{\a}$; see Corollary
\ref{cor:11} and Proposition \ref{prop:260}.

\medskip \noindent
(2) By Lemma \ref{lem:264} and Definition \ref{dfn:8}, there are
functorial isomorphisms 
\[ M \cong \mrm{R} \Gamma_{\a} (M) \cong 
\mrm{R} \Gamma_{\a} (\mrm{L} \Lambda_{\a} (M)) \]
for $M \in \cat{D}(\cat{Mod} A)_{\a \tup{-tor}}$. 
By Lemma \ref{lem:263}  and Definition \ref{dfn:2} there are
functorial isomorphisms 
\[ N \cong \mrm{L} \Lambda_{\a} (N) \cong 
\mrm{L} \Lambda_{\a} (\mrm{R} \Gamma_{\a} (N)) \]
for $N \in \cat{D}(\cat{Mod} A)_{\a \tup{-com}}$. 
These isomorphisms set up the desired equivalence. 
\end{proof}

Here are a couple of related results. 

\begin{thm}[GM Duality] \label{thm:mgm.3}
Let $A$ be a ring, and $\a$ a weakly proregular ideal in $A$. 
For any $M, N \in \cat{D}(\cat{Mod} A)$ the morphisms 
\[ \begin{aligned}
& \opn{RHom}_A \bigl( \mrm{R} \Gamma_{\a} (M), \mrm{R} \Gamma_{\a} (N) \bigr)
\xar{\opn{RHom}(1, \sigma^{\mrm{R}}_N)}
\opn{RHom}_A \bigl( \mrm{R} \Gamma_{\a} (M), N \bigr) 
\\
& \qquad\xar{\opn{RHom}(1, \tau^{\mrm{L}}_N)}
\opn{RHom}_A \bigl( \mrm{R} \Gamma_{\a} (M), \mrm{L} \Lambda_{\a} (N) \bigr) 
\xleftarrow{\opn{RHom}(\sigma^{\mrm{R}}_M, 1)}
\\ & \qquad  \qquad
\opn{RHom}_A \bigl( M, \mrm{L} \Lambda_{\a} (N) \bigr)
\xleftarrow{\opn{RHom}(\tau^{\mrm{L}}_M, 1)}
\opn{RHom}_A \bigl( \mrm{L} \Lambda_{\a} (M), \mrm{L} \Lambda_{\a} (N) \bigr)
\end{aligned} \]
in $\cat{D}(\cat{Mod} A)$ are isomorphisms.
\end{thm}

\begin{proof}
Choose a weakly proregular sequence $\bsym{a}$ that generates $\a$, and write 
$T := \opn{Tel}(A; \bsym{a})$ and $u := u_{\bsym{a}}$.
Next choose a K-projective resolution $P \to M$ and a 
K-injective resolution $N \to I$. 
The complex $T \ot_A P$ is K-projective, and the complex 
$\opn{Hom}_A(T, I)$ is K-injective. 

By Corollary \ref{cor:tel.1} and Proposition \ref{prop:251} we can replace 
the diagram above with the diagram 
\[ \begin{aligned}
& \opn{Hom}_A \bigl( T \ot_A P, T \ot_A I \bigr)
\xar{\opn{Hom}(1, u \ot 1 )}
\opn{Hom}_A \bigl( T \ot_A P, I \bigr) 
\\
& \quad \xar{\opn{Hom}(1, \opn{Hom}( u, 1))}
\opn{Hom}_A \bigl( T \ot_A P, \opn{Hom}_A(T, I) \bigr)
\xleftarrow{\opn{Hom}( u \ot 1, 1)}
\\ & \quad  
\opn{Hom}_A \bigl( P, \opn{Hom}_A(T, I) \bigr)
\xleftarrow{\opn{Hom}(\opn{Hom}(1, u), 1)}
\opn{Hom}_A \bigl( \opn{Hom}_A(T, P), \opn{Hom}_A(T, I) \bigr)
\end{aligned} \]
in $\cat{C}(\cat{Mod} A)$. We will prove that all these morphisms are
quasi-isomorphisms. 

Consider the homomorphism of complexes 
\[ \opn{Hom}(u, 1) : 
T \ot_A P \to  \opn{Hom}_A(T, T \ot_A P) . \]
By Corollary \ref{cor:tel.1}, Proposition \ref{prop:251} and Lemma
\ref{lem:263} this is a quasi-isomorphism. 
Therefore, by Hom-tensor adjunction and the fact that $I$ is K-injective, we
see that $\opn{Hom}(1, u \ot 1)$ is a quasi-isomorphism.

By Lemma \ref{lem:265} and Hom-tensor adjunction it follows that 
$\opn{Hom}(1, \opn{Hom}( u, 1))$ and 
$\opn{Hom}(u \ot 1, 1)$ are quasi-isomorphisms.

Finally consider the homomorphism of complexes 
\[ 1 \ot \opn{Hom}(u, 1) : 
T \ot_A P \to T \ot_A \opn{Hom}_A(T, P) . \]
By Corollary \ref{cor:tel.1}, Proposition \ref{prop:251} and Lemma
\ref{lem:264} this is a quasi-isomorphism. 
Therefore, by Hom-tensor adjunction and the fact that $I$ is K-injective, we
see that $\opn{Hom}(\opn{Hom}(1, u), 1)$ is a quasi-isomorphism.
\end{proof}

\begin{cor}  \label{cor:280}
There is a functorial isomorphism
\[ \rho^{\mrm{LR}}_N : \opn{RHom}_A( \mrm{R} \Gamma_{\a} (A), N)
\iso \mrm{L} \Lambda_{\a} (N) \]
for $N \in \cat{D}(\cat{Mod} A)$, such that 
$\rho^{\mrm{LR}}_N \circ \opn{RHom}( \sigma^{\mrm{R}}_A, 1_N) = 
\tau^{\mrm{L}}_N$
as morphisms $N \to \mrm{L} \Lambda_{\a} (N)$.
\end{cor}

\begin{proof}
Take $M := A$ in Theorem \ref{thm:mgm.3}. 
\end{proof}

\begin{rem} \label{rem:historical}
Here is a brief historical survey of the material in this paper.
GM Duality for derived categories was
introduced in \cite{AJL1}.
Precursors, in ``classical'' homological algebra,
were in the papers \cite{Ma1}, \cite{Ma2} and \cite{GM}. 

The construction of the total left derived completion functor $\mrm{L}
\Lambda_{\a}$ was first done in \cite{AJL1}. Recall that \cite{AJL1} dealt with
sheaves on a  scheme $X$, where K-projective resolutions are not available, and
certain operations work only for quasi-coherent $\mcal{O}_X$-modules. 
Hence there are some technical difficulties that do not arise when working
with rings. 

The derived torsion functor goes back to work of
Grothendieck in the late 1950's (see \cite{LC} and \cite[Chapter IV]{RD}). The
use of the infinite dual Koszul complex to prove that the
functor $\mrm{R} \Gamma_{\a}$ has finite cohomological dimension already appears
in \cite{AJL1}. 

The concept of ``telescope'' comes from algebraic topology, as a device to form
the homotopy colimit in triangulated categories. This is how it was treated in 
\cite{GM}. Its purpose there was the same as in our proof of 
Theorem \ref{thm:mgm.3}. We give a concrete treatment of the telescope complex,
resulting in our Theorem \ref{thm:250}. 

GM Duality (Theorem \ref{thm:mgm.3}) was already proved in \cite{AJL1}.
Perhaps because of the complications inherent to the geometric setup, the proofs
in \cite{AJL1} are not quite transparent. Moreover, there was a subtle mistake
in \cite{AJL1} involving the concept of proregularity, that was
discovered by Schenzel (see \cite[Correction]{AJL1} and \cite{Sc}).
On the other hand, the results in the later paper \cite{Sc} are not as
strong as those in \cite{AJL1}, and this is quite confusing. See
Remark \ref{rem:280} for details. One of our aims in this paper is to clarify
the foundations of the theory in the algebraic setting.

MGM Equivalence (Theorem \ref{thm:26}) is present, in essence, already in
\cite{AJL2} and \cite{Sc}. See a discussion of the various
statements and proofs in Remark \ref{rem:280}. 

Theorem \ref{thm:26} is similar to \cite[Theorem 2.1]{DG}; but the
relationship is not clear. In \cite{DG} the authors seem to {\em define} the
derived completion and torsion functors to be 
$\opn{Hom}_A(T, M)$ and $T \ot_A M$ respectively, where 
$\bsym{a}$ is a finite sequence and 
$T := \opn{Tel}(A; \bsym{a})$. There is no apparent comparison in \cite{DG} of
these functors to the derived functors $\mrm{L} \La_{\a}(M)$ and 
$\mrm{R} \Ga_{\a}(M)$
associated to the ideal $\a$ generated by $\bsym{a}$
(something like Proposition \ref{prop:251} and Corollary \ref{cor:tel.1}).
There is also no assumption that $A$ is noetherian, nor any
mention of weak proregularity of $\bsym{a}$. The same reservations 
pertain also to \cite{DGI}. 
\end{rem}
