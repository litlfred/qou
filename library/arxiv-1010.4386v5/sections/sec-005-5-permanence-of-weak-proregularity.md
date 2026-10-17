---
doc_id: arxiv-1010.4386v5
doc_title: "ON THE HOMOLOGY OF COMPLETION AND TORSION"
section_id: sec-005-5-permanence-of-weak-proregularity
section_title: "Permanence of Weak Proregularity"
section_number: 5
pages: 22-24
source_pdf: 1010.4386v5.pdf
source_sha256: 168226dbb5a479ed
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.932
doc_brief: "ON THE HOMOLOGY OF COMPLETION AND TORSION — Let A be a commutative ring, and a a weakly proregular ideal in A."
---
\label{sec:permanence}

In this section we show that derived completion and derived torsion are
independent of the ring, when the the ideal is weakly proregular (Theorem 
\ref{thm:6.2}). 

\begin{thm} \label{thm:290}
Let $A$ be a ring, let $\bsym{a}$ and $\bsym{b}$ be finite sequences of elements
of $A$, and let $\a := (\bsym{a})$ and $\b := (\bsym{b})$, the ideals generated
by these sequences. Assume that $\sqrt{\a} = \sqrt{\b}$. 
Then the complexes $\opn{Tel}(A; \bsym{a})$ and $\opn{Tel}(A; \bsym{b})$
are homotopy equivalent.
\end{thm}

Note that these sequences are not assumed to be weakly proregular.

\begin{proof}
For a sufficiently large positive integer $p$ we have $b_i^p \in \a$ and 
$a_j^p \in \b$ for all $i, j$. Hence there are finitely many $c_{i,j}, d_{j,i}
\in A$ such that 
$b_i^p = \sum_j c_{i,j} a_j$ and $a_j^p = \sum_i d_{j,i} b_i$.
Define
$\til{A}$ to be the quotient of the polynomial ring 
$\Z[ \{ s_i, t_j, u_{i, j}, v_{j, i} \} ]$ in finitely many variables, modulo
the relations 
$t_i^p = \sum_j u_{i,j} s_j$ and $s_j^p = \sum_i v_{j,i} t_i$.
Let $\til{a}_i \in \til{A}$ and $\til{b}_j \in \til{A}$ be the images of $s_i$
and $t_j$ respectively. 
There is a ring homomorphism $f : \til{A} \to A$ such that 
$f(\til{a}_i) = a_i$ and $f(\til{b_j}) = b_j$.

Define the finite sequences $\til{\bsym{a}} := (\til{a}_1, \ldots)$ and 
$\til{\bsym{b}} := (\til{b}_1, \ldots)$. There are corresponding ideals 
$\til{\a} := (\til{\bsym{a}})$ and $\til{\b} := (\til{\bsym{b}})$ in
$\til{A}$. Since the ring $\til{A}$ is noetherian, the sequences 
$\til{\bsym{a}}$ and  $\til{\bsym{b}}$ are weakly proregular.  
By construction we have $\sqrt{\til{\a}} = \sqrt{\til{\b}}$, and therefore 
$\Ga_{\til{\a}} = \Ga_{\til{\b}}$ as functors. According to Proposition
\ref{prop:251} there are isomorphisms 
\[ \opn{Tel}(\til{A}; \til{\bsym{a}}) \cong \mrm{R} \Ga_{\til{\a}} (\til{A})
\cong \mrm{R} \Ga_{\til{\b}} (\til{A}) \cong 
\opn{Tel}(\til{A}; \til{\bsym{b}}) \]
in $\cat{D}(\cat{Mod} \til{A})$.
Now $\opn{Tel}(\til{A}; \til{\bsym{a}})$ and 
$\opn{Tel}(\til{A}; \til{\bsym{b}})$
are bounded complexes of free $\til{A}$-modules, so there is a homotopy
equivalence 
$\til{\phi} : \opn{Tel}(\til{A}; \til{\bsym{a}}) \to 
\opn{Tel}(\til{A}; \til{\bsym{b}})$.
Applying base change along  $f$ to $\til{\phi}$ we get a homotopy
equivalence 
$\phi : \opn{Tel}(A; \bsym{a}) \to \opn{Tel}(A; \bsym{b})$
over $A$.
\end{proof}

The next result was already proved by Schenzel \cite[Lemma 3.3]{Sc}.

\begin{cor} \label{cor:300}  
In the situation of Theorem \tup{\ref{thm:290}}, the sequence  $\bsym{a}$ is
weakly proregular if and only if the sequence $\bsym{b}$ is weakly proregular.
\end{cor}

\begin{proof}
By Lemma \ref{lem:201} there are quasi-isomorphisms 
$w_{\bsym{a}}  : \opn{Tel}(A; \bsym{a}) \to 
\opn{K}^{\vee}_{\infty}(A; \bsym{a})$
and 
$w_{\bsym{b}}  : \opn{Tel}(A; \bsym{b}) \to 
\opn{K}^{\vee}_{\infty}(A; \bsym{b})$.
Now all these complexes are K-flat; therefore for any $A$-module $I$
there is a diagram of quasi-isomorphisms
\[
\begin{aligned}
& \opn{K}^{\vee}_{\infty}(A; \bsym{a}) \ot_A I 
\xleftarrow{w_{\bsym{a}} \ot 1_I}
\opn{Tel}(A; \bsym{a}) \ot_A I
\\
& \qquad \xar{\phi \ot 1_I}
\opn{Tel}(A; \bsym{b}) \ot_A I
\xar{w_{\bsym{b}} \ot 1_I}
\opn{K}^{\vee}_{\infty}(A; \bsym{b}) \ot_A I .
\end{aligned} \]
Here $\phi : \opn{Tel}(A; \bsym{a}) \to \opn{Tel}(A; \bsym{b})$
is a homotopy equivalence, that exists by Theorem \ref{thm:290}.
Taking $I$ to be an arbitrary injective $A$-module, Theorem \ref{thm:252} says
that $\bsym{a}$ is weakly proregular if and only if 
$\bsym{b}$ is weakly proregular.
\end{proof}

\begin{cor} \label{cor:290}
Let $\a$ be a weakly proregular ideal in a ring $A$. Then any finite sequence
that generates $\a$ is weakly proregular.
\end{cor}

\begin{proof}
Let $\bsym{a}$ be any finite sequence that generates $\a$. Since $\a$ is weakly
proregular, it has some weakly proregular generating sequence $\bsym{b}$. 
By Corollary \ref{cor:300}, $\bsym{a}$ is also weakly proregular.
\end{proof}

\begin{cor} \label{cor:291}
Let $\a$ and $\b$ be finitely generated ideals in a ring $A$, such that 
$\sqrt{\a} = \sqrt{\b}$. 
Then $\a$ is weakly proregular if and only if $\b$ is weakly
proregular.
\end{cor}

\begin{proof}
Say $\a$ is weakly proregular. Choose a weakly proregular generating sequence
$\bsym{a}$ for $\a$. Let $\bsym{b}$ be any finite sequence that generates
$\b$. By Corollary \ref{cor:300}, $\bsym{b}$ is weakly proregular. Therefore the
ideal $\b$ is weakly proregular. 
\end{proof}

Let $f :A \to B$ be a ring homomorphism. There is a forgetful functor 
(restriction of scalars)
$F : \cat{Mod} B \to \cat{Mod} A$. 
Suppose $\a \subset A$ and $\b \subset B$ are finitely generated ideals such
that 
$\sqrt{\b} = \sqrt{B \cdot f(\a)}$ in $B$.
It is easy to see that there are isomorphisms 
$F \circ \Gamma_{\b} \cong \Gamma_{\a} \circ F$
and 
$F \circ \Lambda_{\b} \cong \Lambda_{\a} \circ F$,
as functors $\cat{Mod} B \to \cat{Mod} A$. 

Sometimes such isomorphisms exist also for the derived functors. Note that the
forgetful functor $F$ is exact, so it extends to a triangulated functor 
$F : \cat{D}(\cat{Mod} B) \to \cat{D}(\cat{Mod} A)$. 

\begin{thm} \label{thm:6.2}
Let $f :A \to B$ be a homomorphism of rings, 
let $\a$ be an ideal in $A$, and let $\b$ be an ideal in $B$. 
Assume that the ideals $\a$ and $\b$ are weakly proregular, and that
$\sqrt{\b} = \sqrt{B \cdot f(\a)}$.
Then there are isomorphisms
\[ F \circ \mrm{R} \Gamma_{\b} \cong \mrm{R} \Gamma_{\a} \circ F \]
and 
\[ F \circ \mrm{L} \Lambda_{\b} \cong \mrm{L} \Lambda_{\a} \circ F \]
of triangulated functors 
$\cat{D}(\cat{Mod} B) \to \cat{D}(\cat{Mod} A)$. 
\end{thm}

\begin{proof}
In view of Corollary \ref{cor:291} we can assume that 
$\b = B \cdot f(\a)$. 
Choose a sequence $\bsym{a} = (a_1, \ldots, a_n)$ that generates $\a$,
and let 
$\bsym{b} := (f(a_1), \ldots, f(a_n))$. According to Corollary \ref{cor:290} 
the sequences $\bsym{a}$ and $\bsym{b}$ are weakly proregular, in $A$ and $B$
respectively. 

We know that 
$\opn{Tel}(B; \bsym{b}) \cong B \otimes_A \opn{Tel}(A; \bsym{a})$
as complexes of $B$-modules. 
Take any $N \in \cat{D}(\cat{Mod} B)$. 
Using Corollary \ref{cor:tel.1} and Hom-tensor adjunction we get isomorphisms 
\[ (F \circ \, \mrm{L} \Lambda_{\b}) \, (N) \cong 
\opn{Hom}_B \bigl( \opn{Tel}(B; \bsym{b}) , N \bigr) \cong
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}) , N \bigr) \cong 
(\mrm{L} \Lambda_{\a} \circ F) (N) . \] 
Likewise, using Proposition \ref{prop:251}, there are isomorphisms
\[ (F \circ \mrm{R} \Gamma_{\b}) \, (N) \cong 
\opn{Tel}(B; \bsym{b}) \otimes_B N \cong 
\opn{Tel}(A; \bsym{a}) \otimes_A N \cong 
(\mrm{R} \Gamma_{\a} \circ F) \, (N) . \]
\end{proof}

\begin{exa} \label{exa:280}
This is a continuation of Example \ref{exa:251}.
Let us assume that the ring homomorphisms $\K \to A$ and $\K \to B$ are
of formally finite type, in the sense of \cite{Ye1}.
(In the terminology of \cite{AJL2} these are pseudo finite type
homomorphisms.) Let $\c$ be the ideal in $C$ generated
by the sequence $\bsym{c}$, and define $\what{C} := \La_{\c}(C)$. 
According to \cite[Corollary 1.23]{Ye1} the ring $\what{C}$ is noetherian, and 
the homomorphism $\K \to \what{C}$ is of formally finite type. 
(E.g.\ if $A = \K[[s]]$ and $B = \K[[t]]$, with defining ideals
$\a := (s)$ and $\b := (t)$, then $\what{C} \cong \K[[s, t]]$.)
Let us denote by $\hat{\bsym{c}}$ the image of the sequence 
$\bsym{c}$ in the ring $\what{C}$, and by $\hat{\c}$ the ideal it generates.
By Theorem \ref{thm:253} the sequence 
$\hat{\bsym{c}}$ is weakly proregular. Theorem \ref{thm:6.2} says that
there are isomorphisms 
$\mrm{R} \Ga_{\c} \cong \mrm{R} \Ga_{\hat{\c}}$
and 
$\mrm{L} \La_{\c} \cong \mrm{L} \La_{\hat{\c}}$
between the derived functors. 
\end{exa}
