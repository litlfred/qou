---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-008-8-cohen-macaulay-dg-modules
section_title: "Cohen-Macaulay DG Modules"
section_number: 8
pages: 43-47
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.958
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:cm}

In this section we work with cohomologically pseudo-noetherian
commutative DG rings (see Convention \ref{conv:100} and Definition 
\ref{dfn:391}).  

Let $A$ be such a DG ring. Recall that $\bar{A} = \opn{H}^0(A)$,  
and $\cat{D}^0(A)$ is the full subcategory of $\cat{D}(A)$ 
consisting of the DG modules $M$ such that $\opn{H}^i(M) = 0$ for all 
$i \neq 0$. 
Inside $\cat{D}^{0}(A)$ we have 
$\cat{D}^{0}_{\mrm{f}}(A) =
\cat{D}_{\mrm{f}}(A) \cap \cat{D}^{0}(A)$.

\begin{lem} \label{lem:530} 
Consider the canonical DG ring homomorphism $\pi :A \to \bar{A}$. 
The functor 
\[ \opn{Q} \circ \opn{rest}_{\pi} : \cat{Mod} \bar{A} \to 
\cat{D}^0(A) \]
is an equivalence. It restricts to an equivalence 
\[ \opn{Q} \circ \opn{rest}_{\pi} : \cat{Mod}_{\mrm{f}} \bar{A} \to 
\cat{D}^0_{\mrm{f}}(A) . \]
\end{lem}

\begin{proof}
Smart truncation shows that any object of $\cat{D}^0(A)$ is isomorphic to an 
object of $\cat{Mod} \bar{A}$. Finiteness of $\bar{A}$-modules is preserved. It 
remains to show that $\opn{Q} \circ \opn{rest}_{\pi}$ is a fully faithful 
functor. 

So take $M, N \in \cat{Mod} \bar{A}$, and let 
$\til{M} \to M$ be a semi-free resolution over $A$ with 
$\opn{sup}(\til{M}) \leq 0$. Then 
\[ \opn{Hom}_{\cat{D}(A)}(M, N) \cong 
\opn{H}^0 \bigl( \opn{Hom}_{A}(\til{M}, N) \bigr) \cong
\opn{Hom}_{\bar{A}}(\opn{H}^0 (\til{M}), N) \cong
\opn{Hom}_{\bar{A}}(M, N) . \]
\end{proof}

\begin{dfn}
Let let $R$ be a dualizing DG $A$-module. A 
DG module $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$ is called
{\em Cohen-Macaulay with respect to $R$} if 
$\opn{RHom}_A(M, R) \in \cat{D}^0_{\mrm{f}}(A)$.
\end{dfn}

In other words, the condition is that $\opn{RHom}_A(M, R)$ is 
isomorphic, in $\cat{D}(A)$, to an object of $\cat{Mod}_{\mrm{f}} \bar{A}$. 
As usual ``Cohen-Macaulay'' is abbreviated to ``CM''. Let us denote by 
$\cat{D}^{\mrm{b}}_{\mrm{f}}(A)_{\mrm{CM} : R}$
the full  subcategory of $\cat{D}^{\mrm{b}}_{\mrm{f}}(A)$ consisting of DG 
modules that are CM w.r.t.\ $R$. 

\begin{rem}
Observe that the functor $\opn{RHom}_A(-, R)$
gives rise to a duality between 
$\cat{D}^{\mrm{b}}_{\mrm{f}}(A)_{\mrm{CM} : R}$
and $\cat{D}^0_{\mrm{f}}(A)$. And the latter is equivalent to 
$\cat{Mod}_{\mrm{f}} \bar{A}$. Therefore 
$\cat{D}^{\mrm{b}}_{\mrm{f}}(A)_{\mrm{CM} : R}$
is an artinian abelian category.

If $A \to \bar{A}$ is not a quasi-isomorphism, then $A$ does not belong to 
$\cat{D}^0(A)$, and therefore $R$ is not a CM DG module w.r.t.\ itself. 

We do not know any definition of Cohen-Macaulay DG rings; except when 
$A \to \bar{A}$ is a quasi-isomorphism, in which case the condition is that the 
ring $\bar{A}$ should be CM. 

For a comparison to Cohen-Macaulay modules and Grothendieck's notion of 
Cohen-Macaulay complexes, see \cite[Theorem 6.2]{YZ3} and 
\cite[Section 7]{YZ4}.
\end{rem}

The groups $\opn{DPic}^0(A) \subseteq \opn{DPic}(A)$ were introduced in 
Definitions \ref{dfn:350} and \ref{dfn:330}.

\begin{lem} \label{lem:525} 
Let $P$ be a tilting DG $A$-module. The following are equivalent\tup{:}
\begin{enumerate}
\rmitem{i} The auto-equivalence $P \ot^{\mrm{L}}_A -$ of $\cat{D}(A)$ preserves 
the subcategory $\cat{D}^0_{\mrm{f}}(A)$. 

\rmitem{ii} The class of $P$ is in $\opn{DPic}^0(A)$.
\end{enumerate}
\end{lem}

\begin{proof}
(i) $\Rightarrow$ (ii): 
Let $\bar{P} := \bar{A} \ot^{\mrm{L}}_A P$. By assumption it belongs to 
$\cat{D}^0_{\mrm{f}}(A)$. But then the class of $\bar{P}$ is in  
$\opn{Pic}(\bar{A}) = \opn{DPic}^0(\bar{A})$, 
so by definition the class of $P$ is in $\opn{DPic}^0(A)$.

\medskip \noindent 
(ii) $\Rightarrow$ (i): Here $\bar{P} := \bar{A} \ot^{\mrm{L}}_A P$
is isomorphic to an invertible $\bar{A}$-module, so 
$\bar{P} \ot^{\mrm{L}}_{\bar{A}} -$ preserves 
$\cat{D}^0_{\mrm{f}}(\bar{A})$.
Now take any $M \in \cat{D}^0_{\mrm{f}}(A)$. 
By Lemma \ref{lem:530} we can assume that $M \in 
\cat{Mod}_{\mrm{f}}(\bar{A})$. Then 
\[ P \ot^{\mrm{L}}_A M \cong 
P \ot^{\mrm{L}}_A \bar{A} \ot^{\mrm{L}}_{\bar{A}} M \cong 
\bar{P} \ot^{\mrm{L}}_{\bar{A}} M \in \cat{D}^0_{\mrm{f}}(\bar{A}) . \]
We see that $\opn{H}^i(P \ot^{\mrm{L}}_A M) = 0$ for all $ i \neq 0$. 
\end{proof}

Recall the connected component idempotent functors of a DG ring from Definition 
\ref{dfn:343}.

\begin{thm} \label{thm:250}
Let $f : A \to B$ be a cohomologically pseudo-finite homomorphism between 
cohomologically pseudo-noetherian DG rings. Assume that $A$ and 
$B$ have dualizing DG modules $R_A$ and $R_B$ respectively, and that $\bar{B}$ 
is nonzero. Let $E_1, \ldots, E_n$ be the connected component decomposition 
functors of $B$. 
\begin{enumerate}
\item There are unique integers $k_1, \ldots, k_n$ such that, letting 
\[ R'_B := \bigoplus_{i = 1}^n E_i(R_{B})[k_i] \in \cat{D}(B) , \] 
the class of the tilting DG $B$-module $\opn{RHom}_A(R'_B, R_A)$ 
is inside $\opn{DPic}^0(B)$. 

\item Let $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(B)$. 
The following conditions are equivalent\tup{:}
\begin{enumerate}
\rmitem{i} $M$ is CM w.r.t.\ to $R'_B$. 
  
\rmitem{ii} $\opn{rest}_f(M)$ is CM w.r.t.\ to $R_A$. 
\end{enumerate}
\end{enumerate}
\end{thm}

Note that $R'_B$ and $R''_B := \opn{RHom}_A(B, R_A)$ are dualizing DG 
$B$-modules, so 
\[ \opn{RHom}_A(R'_B, R_A) \cong \opn{RHom}_B ( R'_B, R''_B)  \]
is a tilting DG $B$-module (by Theorem \ref{thm:43}(2)), and hence item (1) 
above makes sense.

\begin{proof}
(1) Let $R''_B$ be as above.
By the classifications in Corollaries \ref{cor:50} and \ref{cor:330},
there are unique $k_1, \ldots, k_n \in \Z$, and a tilting DG $B$-module 
$Q$ whose class in $\opn{DPic}^0(B)$ is unique, such that 
$R''_B \cong Q \ot^{\mrm{L}}_B R'_B$. 
Let $P := \opn{RHom}_B(Q, B)$, which by Corollary \ref{cor:405}
is the quasi-inverse of $Q$. Then  
$R'_B \cong P \ot^{\mrm{L}}_B R''_B$. 
Using adjunction we get isomorphisms
\[  \begin{aligned}
& \opn{RHom}_A(R'_B, R_A) \cong \opn{RHom}_B(R'_B, R''_B)
\cong \opn{RHom}_B(P \ot^{\mrm{L}}_B R''_B, R''_B)
\\
& \quad \cong 
\opn{RHom}_B \bigl(P, \opn{RHom}_B(R''_B, R''_B) \bigr)
\cong \opn{RHom}_B(P, B) \cong Q
\end{aligned} \]
in $\cat{D}(B)$. This proves (1). 

\medskip \noindent 
(2) By Lemma \ref{lem:525} the
functor $Q \ot^{\mrm{L}}_B -$ preserves 
$\cat{D}^0_{\mrm{f}}(B)$.
Take any $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(B)$.
Then, using Lemma \ref{lem:45}, we get isomorphisms
\[ \begin{aligned}
& \opn{RHom}_A(M, R_A) \cong \opn{RHom}_B(M, R''_B)
\\
& \quad 
\cong \opn{RHom}_B(M, Q \ot^{\mrm{L}}_B R'_B) 
\cong \opn{RHom}_B(M, R'_B) \ot^{\mrm{L}}_B Q . 
\end{aligned} \]
This gives (i) $\Rightarrow$ (ii). The converse is very similar. 
\end{proof}

\begin{cor}
Let $f : A \to B$ be a cohomologically finite homomorphism between tractable DG 
rings. Assume $\opn{Spec} \bar{B}$ is connected. The following are equivalent 
for $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(B)$~\tup{:}
\begin{enumerate}
\rmitem{i} $M$ is CM w.r.t.\ some dualizing DG $B$-module.
\rmitem{ii} $\opn{rest}_f(M)$ is CM w.r.t.\ some dualizing DG $A$-module.
\end{enumerate}
\end{cor}

\begin{proof}
The implication (ii) $\Rightarrow$ (i) comes from Theorem \ref{thm:250}(2) -- 
and does not require $\opn{Spec} \bar{B}$ to be connected.

For the implication (i) $\Rightarrow$ (ii), let $R_B$ be a dualizing DG 
$B$-module such that $M$ is CM with respect to it. Take any dualizing DG 
$A$-module $R_A$, and let $k \in \Z$ be such that 
$\opn{RHom}_A(R_B[k], R_A)$ 
is inside $\opn{DPic}^0(B)$. See Theorem \ref{thm:250}(1). Then by 
Theorem \ref{thm:250}(2) we know that $\opn{rest}_f(M)$ is CM w.r.t.\ 
$R_A[-k]$. 
\end{proof}

\begin{thm} \label{thm:251}
Let $f : A \to B$ be a homomorphism between 
cohomologically pseudo-noetherian DG rings, such that 
$\bar{f} : \bar{A}  \to \bar{B}$
is surjective. Assume $A$ and $B$ have dualizing DG modules.
Let $R_B$ be a dualizing DG $B$-module and let  
$M, N \in \cat{D}^{\mrm{b}}_{\mrm{f}}(B)$. 
\begin{enumerate}
\item If $M$ is CM w.r.t.\ $R_B$, and there is an isomorphism
$\opn{rest}_f(M) \cong \opn{rest}_f(N)$ in $\cat{D}(A)$, then 
$N$ is also CM w.r.t.\ $R_B$. 

\item If $M$ and $N$ are CM w.r.t.\ $R_B$, then the homomorphism 
\[ \opn{rest}_f : \opn{Hom}_{\cat{D}(B)}(M, N) \to 
\opn{Hom}_{\cat{D}(A)} \bigl( \opn{rest}_f(M), \opn{rest}_f(N) \bigr) \]
is bijective. 
\end{enumerate}
\end{thm}

\begin{proof}
(1)  We may assume that $\bar{B} \neq 0$. 
Let $E_1, \ldots, E_n$ be the connected component decomposition functors 
of $B$. Write $F := \opn{rest}_f$, $M_i := E_i(M)$ and $N_i := E_i(N)$.
Choose some dualizing DG $A$-module $R_A$, and let 
$k_1, \ldots, k_n$ be the integers from Theorem \ref{thm:250}(1). 
Thus the dualizing DG $B$-module 
$R'_B := \bigoplus_{i = 1}^n E_i(R_{B})[k_i]$
satisfies this: the tilting DG $B$-module $Q := \opn{RHom}_A(R'_B, R_A)$ 
is inside $\opn{DPic}^0(B)$. 
Define $M' := \bigoplus_i M_i[k_i]$ and $N' := \bigoplus_i N_i[k_i]$.

We are given that $M$ is CM w.r.t.\ $R_B$. 
Using the equivalence of Corollary \ref{cor:22} we see that 
$M'$ is CM w.r.t.\ $R'_B$. Thus by Theorem \ref{thm:250}(2) 
the DG $A$-module $F(M')$ is CM w.r.t.\ $R_A$.
Proposition \ref{prop:21} implies that 
$F(M') \cong F(N')$ in $\cat{D}(A)$, and hence  $F(N')$ is CM w.r.t.\ $R_A$.
Using Theorem \ref{thm:250}(2) once more we conclude that 
$N'$ is CM w.r.t.\ $R'_B$; and hence $N$ is CM w.r.t.\ $R_B$. 

\medskip \noindent
(2) Let us write
$R''_B := \opn{RHom}_A(B, R_A)$, $D''_B := \opn{RHom}_B(-, R''_B)$ and 
$D_A := \lb \opn{RHom}_A(-, R_A)$. 
Define $M' := \bigoplus_i M_i[k_i]$ and $N' := \bigoplus_i N_i[k_i]$
as above, so these are CM w.r.t.\ $R''_B$. There are isomorphisms 
\[ \begin{aligned}
& \opn{Hom}_{\cat{D}(B)}(M, N) \cong^1
\opn{Hom}_{\cat{D}(B)}(M', N') 

\cong^2 \opn{Hom}_{\cat{D}(B)} \bigl( D''_B(N'), D''_B(M') \bigr) 
\\ & \quad 
\cong^3 \opn{Hom}_{\cat{Mod} \bar{B}} \bigl( D''_B(N'), D''_B(M') \bigr) 

\cong^{4} \opn{Hom}_{\cat{Mod} \bar{A}} \bigl( F(D''_B(N')), F(D''_B(M')) 
\bigr) 
\\ & \quad 
\cong^5 \opn{Hom}_{\cat{Mod} \bar{A}} \bigl( D_A(F(N')), D_A(F(M')) \bigr)

\cong^{2, 3} \opn{Hom}_{\cat{D} (A)} \bigl( F(M'), F(N') \bigr)
\\ & \quad 
\cong^{6} \opn{Hom}_{\cat{D} (A)} \bigl( F(M), F(N) \bigr) \ .
\end{aligned} \]
They are gotten as follows:
the isomorphism $\cong^{1}$ is by Corollary \ref{cor:22} and Proposition 
\ref{prop:90};
the isomorphism $\cong^{2}$ is by Proposition \ref{prop:250}(3);
the isomorphism $\cong^{3}$ is by Lemma \ref{lem:530};
the isomorphism $\cong^{4}$ is because
$\opn{H}^0(f) : \bar{A}  \to \bar{B}$ is surjective;
the isomorphism $\cong^{5}$ is because 
$F \circ D''_B \cong D_A \circ F$ as functors;
and isomorphism $\cong^{6}$ is due to Proposition \ref{prop:21}. 
The composition of all these isomorphisms is $F$.
\end{proof}

\begin{cor}
Let $f : A \to B$ be a homomorphism between 
cohomologically pseudo-noetherian DG rings, such that 
$\bar{f} : \bar{A}  \to \bar{B}$ is bijective. 
Let $R_A$ be a dualizing DG $A$-module, and define 
$R_B := \opn{RHom}_{A}(B, R_A)$. Then the functor
\[ \opn{rest}_f : \cat{D}^{\mrm{b}}_{\mrm{f}}(B)_{\mrm{CM} : R_B} \to 
\cat{D}^{\mrm{b}}_{\mrm{f}}(A)_{\mrm{CM} : R_A} \]
is an equivalence.
\end{cor}

\begin{proof}
In view of the last theorem, it suffices to show that $\opn{rest}_f$ is 
essentially surjective on objects. Take any 
$M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)_{\mrm{CM} : R_A}$.
Then 
$N :=  \opn{RHom}_{A}(M, R_A)$ is (isomorphic to) a module in 
$\cat{Mod}_{\mrm{f}} \bar{A}$. Because 
$\opn{rest}_{\bar{f}} : \cat{Mod}_{\mrm{f}} \bar{B} \to
\cat{Mod}_{\mrm{f}} \bar{A}$
is an equivalence, there is $N' \in \cat{Mod}_{\mrm{f}} \bar{B}$
that is sent to $N$. Therefore the DG module 
\[ M' := \opn{RHom}_{A}(N', R_B) \in 
\cat{D}^{\mrm{b}}_{\mrm{f}}(B)_{\mrm{CM} : R_B} \]
satisfies 
$\opn{rest}_f(M') \cong M$. 
\end{proof}

\begin{rem} \label{rem:120}
Here is a quick explanation of the role of CM DG modules in \cite{Ye5}. 
Suppose $\K \to A \to B$ are ring homomorphisms, $M \in \cat{D}(A)$ and 
$N \in \cat{D}(B)$. Under suitable assumptions we want to have a canonical 
isomorphism 
\[  \smallsmile \, : \opn{Sq}_{A / \K}(M) \ot^{\mrm{L}}_A   
\opn{Sq}_{B / A}(N) \iso
\opn{Sq}_{B / \K} (M \ot^{\mrm{L}}_A N) \]
in $\cat{D}(B)$, that we call the {\em cup product}. 
This isomorphism was already constructed in \cite[Theorem 4.11]{YZ1}; but 
unfortunately this part of \cite{YZ1} also contained a serious mistake. 

The construction in \cite{Ye5} goes like this. We choose a semi-free DG ring 
resolution $\K \to \til{A}$ of $\K \to A$, and then a semi-free DG ring 
resolution $\til{A} \to \til{B}$ of $\til{A} \to B$. 
So 
\[ \opn{Sq}_{A / \K}(M) = 
\opn{RHom}_{\til{A} \ot_{\K} \til{A}} (A, M \ot^{\mrm{L}}_{\K} M) \]
etc. The construction goes through a few ``standard moves'' (adjunction 
formulas mostly), until we arrive at the following situation. 
Consider the surjective DG ring homomorphism 
$f : \til{B} \ot_{\K} \til{B} \to \til{B} \ot_{\til{A}} \til{B}$,
and the DG modules 
\[ K := N \ot^{\mrm{L}}_A N \ot^{\mrm{L}}_A \opn{Sq}_{A / \K}(M) \]
and 
\[ L := \opn{RHom}_{\til{B} \ot_{\K} \til{B}}
\bigl( \til{B} \ot_{\til{A}} \til{B} , 
(M \ot^{\mrm{L}}_{A} N) \ot^{\mrm{L}}_{\K}
(M \ot^{\mrm{L}}_{A} N) \bigr) \]
in $\cat{D}(\til{B} \ot_{\til{A}} \til{B})$.
The ``standard moves'' give us a canonical isomorphism  \lb 
$\chi : \opn{rest}_f(K) \iso \opn{rest}_f(L)$
in $\cat{D}(\til{B} \ot_{\K} \til{B})$; but what we need to continue the 
construction is a canonical isomorphism
$\bar{\chi} : K \iso L$ in $\cat{D}(\til{B} \ot_{\til{A}} \til{B})$
such that $\opn{rest}_f(\bar{\chi}) = \chi$. 
The only conceivable hope was that something like Theorem \ref{thm:251} should 
appear. 

Fortunately, in the situation where we require the cup product, the ring $\K$ 
is a regular noetherian ring; $\K \to A$ is essentially finite type; 
$A \to B$ is essentially Gorenstein (i.e.\ essentially finite type, 
flat, and the fibers are Gorenstein rings); $M$ is a rigid dualizing complex 
over $A$ relative to $\K$; and $N$ is a tilting complex over $B$ (and hence it 
is a relative dualizing complex for $A \to B$). These assumptions imply that 
$K$ is a dualizing DG module over the DG ring 
$\til{B} \ot_{\til{A}} \til{B}$, and therefore it is a CM DG module w.r.t.\ 
itself. Now Theorem \ref{thm:251} says that there 
exists a unique isomorphism $\bar{\chi} : K \iso L$ satisfying 
$\opn{rest}_f(\bar{\chi}) = \chi$. 
\end{rem}
