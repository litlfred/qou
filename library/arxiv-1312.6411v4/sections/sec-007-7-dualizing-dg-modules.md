---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-007-7-dualizing-dg-modules
section_title: "Dualizing DG Modules"
section_number: 7
pages: 35-43
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.976
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:dualizing}

Recall that all our DG rings are now commutative (Convention \ref{conv:100}),
and $\bar{A} = \opn{H}^0(A)$.
In this section we concentrate on cohomologically pseudo-noetherian  
DG rings (Definition \ref{dfn:391}). 

Here is a generalization of Grothendieck's definition of dualizing 
complex. \lb When $A$ is a ring, this is identical to the definition in
\cite[Section V.2]{RD}.

\begin{dfn} \label{dfn:253}
Let $A$ be a cohomologically pseudo-noetherian DG ring.
A DG $A$-module $R$ is called a {\em dualizing} if it satisfies these three 
conditions:
\begin{enumerate}
\rmitem{i} Each $\opn{H}^i(R)$ is a finite $\bar{A}$-module. 

\rmitem{ii} $R$ has finite injective dimension relative to 
$\cat{D}(A)$. 

\rmitem{iii} The adjunction morphism 
$A \to \opn{RHom}_A(R, R)$ in $\cat{D}(A)$
is an isomorphism. 
\end{enumerate}
\end{dfn}

In other words, condition (i) says that $R \in \cat{D}_{\mrm{f}}(A)$;
condition (ii) says that the functor 
$\opn{RHom}_A(-, R)$ has finite cohomological dimension relative to
$\cat{D}(A)$, as in Definitions \ref{dfn:10} and \ref{dfn:11}(2); and condition 
(iii) says that the canonical graded ring homomorphism 
\[ \opn{H}(A) \to 
\bigoplus_{k \in \Z} \, \opn{Hom}_{\cat{D}(A)}(R, R[k]) \]
is bijective. 

\begin{prop} \label{prop:250}
Suppose $R$ is a dualizing DG module over $A$, and consider the functor 
\[ D :=  \opn{RHom}_A(-, R) : \cat{D}(A) \to \cat{D}(A) . \]
Let $\cat{D}^{\star}$ denote either $\cat{D}$, 
$\cat{D}^{\mrm{b}}$, $\cat{D}^{+}$ or $\cat{D}^{-}$; and 
correspondingly let  $\cat{D}^{- \star}$ denote either $\cat{D}$, 
$\cat{D}^{\mrm{b}}$, $\cat{D}^{-}$ or $\cat{D}^{+}$.
\begin{enumerate}
\item For any $M \in \cat{D}^{\star}_{\mrm{f}}(A)$
we have $D(M) \in \cat{D}^{- \star}_{\mrm{f}}(A)$.
In particular, $R \in \cat{D}^{+}_{\mrm{f}}(A)$.

\item For any $M \in \cat{D}_{\mrm{f}}(A)$ the canonical morphism 
$M \to D(D(M))$ in $\cat{D}_{\mrm{f}}(A)$ is an isomorphism. 

\item The functor 
\[ D : \cat{D}^{\star}_{\mrm{f}}(A)^{\mrm{op}} \to 
\cat{D}^{- \star}_{\mrm{f}}(A) \]
is an equivalence of triangulated categories. 
\end{enumerate}
\end{prop}

\begin{proof}
(1) The functor $D$ has finite cohomological dimension,
so we can apply Theorem \ref{thm:30}(2).
Since $A \in \cat{D}^{-}_{\mrm{f}}(A)$, 
we get $R = D(A) \in \cat{D}^{+}_{\mrm{f}}(A)$. 

\medskip \noindent
(2) There is a morphism of triangulated functors 
$\eta : \opn{id}_{\cat{D}_{\mrm{f}}(A)} \to D \circ D$.
Both functors have finite cohomological dimensions, 
and $\eta_A$ is an isomorphism.  We can apply Theorem \ref{thm:10}(2). 

\medskip \noindent
(3) Combine items (1) and (2).  
\end{proof}

\begin{cor} \label{cor:380} 
Let $A$ be a cohomologically pseudo-noetherian DG ring, and let $R$ be a 
dualizing DG $A$-module. The following two conditions are equivalent\tup{:}
\begin{itemize}
\rmitem{i} The DG ring $A$ is cohomologically bounded.
\rmitem{ii} The DG module $R$ is cohomologically bounded.
\end{itemize}
\end{cor}

\begin{proof}
This is by Proposition \ref{prop:250}, since $R \cong D(A)$ and $A \cong D(R)$.
\end{proof}

In Example \ref{exa:400} we demonstrate the unbounded option. 

Given a homomorphism $f : A \to B$  of DG rings, 
we denote by $\bar{f} := \opn{H}^0(f)$ the induced ring homomorphism.

\begin{dfn} \label{dfn:252}
Let $f : A \to B$ be a homomorphism between cohomologically pseudo-noetherian 
DG rings. We say that $f$ is a {\em cohomologically pseudo-finite 
homomorphism} if $\bar{f} : \bar{A} \to \bar{B}$ is a finite ring homomorphism, 
i.e.\ $\bar{f}$ makes $\bar{B}$ into a finite $\bar{A}$-module. 
\end{dfn}

Clearly if $f$ is cohomologically finite, then $\opn{rest}_f$ sends 
$\cat{D}^{\star}_{\mrm{f}}(B)$ into $\cat{D}^{\star}_{\mrm{f}}(A)$,
where  $\star$ is either $+, -, \mrm{b}$ or blank.

\begin{prop} \label{prop:252}
Let $f : A \to B$ be a cohomologically pseudo-finite homomorphism between 
cohomologically pseudo-noetherian DG rings.
\begin{enumerate}
\item If $R_A$ is a dualizing DG $A$-module, then 
$R_B := \opn{RHom}_A(B, R_A)$ is a dualizing DG $B$-module.

\item If $f$ is a quasi-isomorphism and $R_B$ is a dualizing DG $B$-module, 
then $R_A := \lb \opn{rest}_f(R_B)$ is a dualizing DG $A$-module.
\end{enumerate}
\end{prop}

\begin{proof}
(1) The proof is almost the same as in the case of a ring; see 
\cite[Proposition V.2.4]{RD}. Viewing $B$ as an object of 
$\cat{D}^{-}_{\mrm{f}}(A)$, Proposition \ref{prop:250}(1) tells us that 
$R_B \in \cat{D}^{+}_{\mrm{f}}(A)$; and hence 
$R_B \in \cat{D}^{+}_{\mrm{f}}(B)$.
For any $N \in \cat{D}(B)$ we have 
\[ \opn{RHom}_B(N, R_B) \cong \opn{RHom}_A(N, R_A) \]
by adjunction, and hence the injective dimension of $R_B$ relative to 
$\cat{D}(B)$ is at most the injective dimension of A relative to 
$\cat{D}(A)$, which is finite. And finally 
\[ \opn{RHom}_B(R_B, R_B) \cong 
\opn{RHom}_A \bigl( \opn{RHom}_A(B, R_A), R_A \bigr) \cong B \]
by Proposition \ref{prop:250}(2). These isomorphisms are actually inside 
$\cat{D}(B)$, and they are compatible with the 
canonical morphism from $B$. 

\medskip \noindent
(2) This is because here
$\opn{rest}_f : \cat{D}(B) \to \cat{D}(A)$
is an equivalence, preserving boundedness and finiteness of cohomology. 
\end{proof}

In commutative ring theory, many good properties of a ring $A$ can be deduced 
if it is ``not far'' from a ``nice'' ring $\K$ (such as a field). This is the 
underlying reason for the next definition. 

Recall that a ring homomorphism $A \to B$ is called of {\em essentially finite 
type} if it can be factored as $A \to B_{\mrm{ft}} \to B$, where $A \to 
B_{\mrm{ft}}$ is finite type (i.e.\ $B$ is finitely generated as $A$-ring), and 
$B_{\mrm{ft}} \to B$ is the localization at some multiplicatively closed subset 
of $B_{\mrm{ft}}$. 

\begin{dfn} \label{dfn:510}
Let $\K$ be a noetherian ring, let $A$ be a cohomologically pseudo-noetherian 
DG ring, and let $u : \K \to A$ a homomorphism of DG 
rings. We say that $u$ is of {\em cohomologically essentially finite type}, and 
that $A$ is a {\em cohomologically essentially finite type DG $\K$-ring}, if 
the ring homomorphism $\bar{u} : \K \to \bar{A}$ is of essentially finite type.
\end{dfn}

\begin{dfn} \label{dfn:46}
A DG ring $A$ is called {\em tractable} if it is cohomologically 
pseudo-noetherian, and there exists a cohomologically 
essentially finite type homomorphism $\K \to A$ from some finite dimensional 
regular noetherian ring $\K$. Such a homomorphism $\K \to A$ is called a {\em 
traction} for $A$.
\end{dfn}

\begin{lem} \label{lem:380}
Let $A$ be a DG ring, let $\K$ be a noetherian ring, and suppose there is a 
cohomologically essentially finite type homomorphism $u : \K \to A$. Then there 
is a commutative diagram of DG rings 
\[  \UseTips \xymatrix @C=5ex @R=5ex {
\K
\ar[r]^{u}
\ar[d]_{v}
&
A 
\ar[r]^{\pi}
\ar[d]_{f}
& 
\bar{A}
\\
A_{\mrm{eft}}
\ar[r]^{g}
&
A_{\mrm{loc}}
\ar[ur]
} \]
such that $\pi$ is the canonical homomorphism\tup{;} 
$f$ and $g$ are quasi-isomorphism\tup{;} and
$\K \to A^0_{\mrm{eft}}$ is essentially finite type.
\end{lem}

\begin{proof}
Let $S := \pi^{-1}(\bar{A}^{\times}) \cap A^0$, namely $s \in S$ iff 
$\pi(s)$ is invertible in the ring $\bar{A}$.  
Define the DG ring 
$A_{\mrm{loc}} := (S^{-1} \cd A^0) \ot_{A^0} A$.
Then $\pi$ factors via $f$, and $f$ is a quasi-isomorphism. 

Since $\K \to \bar{A}$ is essentially finite type, there is a polynomial ring 
$\K[\bsym{t}]$ in finitely many variables of degree $0$, and a 
homomorphism $h : \K[\bsym{t}] \to \bar{A}$ which is essentially surjective,
i.e.\ it is surjective after a localization.
Thus, letting $T := h^{-1}(\bar{A}^{\times}) \lb \subseteq \K[\bsym{t}]$,
and defining 
$A_{\mrm{eft}}^0 := T^{-1} \cd \K[\bsym{t}]$,
the homomorphism  
$h_T : A_{\mrm{eft}}^0 \to \bar{A}$ 
is surjective.

Now the ring  $A_{\mrm{eft}}^0$ is noetherian.
The homomorphism $h_T : A_{\mrm{eft}}^0 \to \bar{A}$ factors via a homomorphism 
$g^0 : A_{\mrm{eft}}^0 \to A^0_{\mrm{loc}}$, 
and the composed homomorphism 
$A_{\mrm{eft}}^0 \to  \opn{H}^0(A_{\mrm{loc}})$ is surjective. 
Since the the modules $\opn{H}^i(A_{\mrm{loc}})$ are finite over 
$A_{\mrm{eft}}^0$, we can extend $A_{\mrm{eft}}^0$ to a DG ring 
$A_{\mrm{eft}}$, and simultaneously extend $g^0$
to a quasi-isomorphism 
$g : A_{\mrm{eft}} \to A_{\mrm{loc}}$,
by inductively introducing finitely many new variables (free ring generators) 
in negative degrees.
The process is the same as in the proof of 
\cite[Proposition 1.7(2)]{YZ1}. 
\end{proof}


\begin{thm} \label{thm:51}
Let $A$ be a tractable  DG ring.  Then $A$ has a dualizing DG module. 
\end{thm}

\begin{proof}
Let $\K \to A$ be a traction for $A$. 
Consider the diagram of homomorphisms in Lemma \ref{lem:380}.
Since $A \to A_{\mrm{loc}}$ is a quasi-isomorphism, and 
$A_{\mrm{eft}}^0 \to A_{\mrm{eft}} \to A_{\mrm{loc}}$
are cohomologically pseudo-finite, it suffices (by Proposition \ref{prop:252})
to show that $A_{\mrm{eft}}^0$ has a dualizing DG module 
(which is the same as a dualizing complex over this ring, in the sense of 
\cite{RD}). But the ring homomorphism $\K \to A_{\mrm{eft}}^0$ can be factored 
into 
$\K \to \K[\bsym{t}] \to B \to A_{\mrm{eft}}^0$,
where $\K[\bsym{t}]$ is a polynomial ring in $n$ variables, 
$\K[\bsym{t}] \to B$ is surjective, and $B \to A_{\mrm{eft}}^0$
is a localization. Thus, using \cite[Theorem V.8.3]{RD} and Proposition 
\ref{prop:252}(1) above, the DG module 
\[ A_{\mrm{eft}}^0 \ot_B \opn{RHom}_{\K[\bsym{t}]}
(B, \Om^n_{\K[\bsym{t}] / \K}[n]) \]
is a dualizing DG module over $A_{\mrm{eft}}^0$.
\end{proof}

\begin{thm} \label{thm:43}
Let $A$ be a cohomologically pseudo-noetherian DG ring, and let
$R$ be a dualizing DG module over $A$. 
\begin{enumerate}
\item If $P$ is a tilting DG module, then
$P \ot^{\mrm{L}}_A R$ is a dualizing DG module. 

\item If $R'$ is a dualizing DG module, then 
$P := \opn{RHom}_A(R, R')$ is a tilting DG module, and 
$R' \cong P \ot^{\mrm{L}}_A R$ in $\cat{D}(A)$.

\item If $P$ is a tilting DG module, and if $R \cong P \ot^{\mrm{L}}_A R$
in $\cat{D}(A)$, then $P \cong A$ in $\cat{D}(A)$.
\end{enumerate}
\end{thm}

This is similar to \cite[Theorem V.3.1]{RD}, and the strategy of the proof 
is the same; cf.\ also \cite[Theorem 4.5]{Ye2}. 

\begin{proof}
(1) Assume $P$ is a tilting DG module, and let $R' := P \ot^{\mrm{L}}_A R$. 
According to Corollary \ref{cor:73} the functor $P \ot^{\mrm{L}}_A -$
is an auto-equivalence of $\cat{D}(A)$, it has finite cohomological dimension,
and it preserves $\cat{D}^{+}_{\mrm{f}}(A)$.
Therefore the DG module $R'$ is dualizing. 

\medskip \noindent (2)
Define the objects 
$P := \opn{RHom}_A(R, R')$ and 
$P' := \opn{RHom}_A(R', R)$, 
and the functors 
$D := \opn{RHom}_A(-, R)$, $D' := \opn{RHom}_A(-, R')$,
$F := P \ot^{\mrm{L}}_A -$ and $F' := P' \ot^{\mrm{L}}_A -$.
We know that the functors $D, D', D' \circ D, D \circ D'$ have finite 
cohomological dimensions relative to $\cat{D}(A)$; the DG modules 
$P, P' \in \cat{D}^{-}_{\mrm{f}}(A)$; and the functors $F, F'$ have 
bounded above cohomological displacements relative to 
$\cat{D}(A)$.
For any $M \in \cat{D}(A)$ there is a canonical morphism 
\[ \opn{RHom}_A(R, R') \ot^{\mrm{L}}_A M \to 
\opn{RHom}_A ( \opn{RHom}_A(M, R), R') , \]
so we get a morphism of triangulated functors 
$\eta : F \to D' \circ D$. By definition $\eta_A$ is an isomorphism, and 
Theorem \ref{thm:10}(1) says that $\eta_M$ is an isomorphism for every 
$M \in \cat{D}^{-}_{\mrm{f}}(A)$. Likewise there is 
an isomorphism $\eta'_M : F'(M) \to (D \circ D')(M)$ for every 
$M \in \cat{D}^{-}_{\mrm{f}}(A)$. 

Let us calculate $P \ot^{\mrm{L}}_A P'$~:
\[ \begin{aligned}
& P \ot^{\mrm{L}}_A P' \cong F(P') \cong (D' \circ D)(P') 
\\ & \quad 
\cong (D' \circ D)(F'(A)) \cong (D' \circ D \circ D \circ D')(A) \cong A .
\end{aligned} \]
This proves $P$ is tilting. And 
\[ P \ot^{\mrm{L}}_A R \cong F(R) 
\cong (D' \circ D)(D(A)) \cong D'(A) \cong R' . \]

\medskip \noindent (3)
If $P$ is tilting and $R \cong P \ot^{\mrm{L}}_A R$, then 
\[ \begin{aligned}
& A \cong \opn{RHom}_A(R, R) \cong 
\opn{RHom}_A(P \ot^{\mrm{L}}_A R, R)
\\
& \quad \cong^{*} \opn{RHom}_A(P, \opn{RHom}_A(R,  R)) 
\cong \opn{RHom}_A(P, A)  , 
\end{aligned}  \]
where the isomorphism $\cong^{*}$ is by adjunction. 
But then 
\[ P \cong A \ot^{\mrm{L}}_A P \cong 
\opn{RHom}_A(P, A) \ot^{\mrm{L}}_A P \cong^{\dag} 
\opn{RHom}_A(P, P) \cong^{\dag \dag} A , \]
where the isomorphism $\cong^{\dag}$ is by a combination of Theorems 
\ref{thm:76} and \ref{thm:74}, and the isomorphism $\cong^{\dag \dag}$ is by  
Theorem \ref{thm:76}.
\end{proof}

\begin{cor} \label{cor:50}
Assume $A$ has some dualizing DG module. 
The formula $R \mapsto P \ot^{\mrm{L}}_A R$
induces a simply transitive action of the group $\opn{DPic}(A)$ on 
the set of isomorphism classes of dualizing DG $A$-modules. 
\end{cor}

\begin{proof}
Clear from the theorem.
\end{proof}

\begin{cor} \label{cor:80}
Assume $A$ has some dualizing DG module  \tup{(}e.g.\ $A$ is tractable\tup{)}. 
The formula 
$R \mapsto \opn{RHom}_A(\bar{A}, R)$ 
induces a bijection 
\[ \frac{ \{  \tup{dualizing DG} \, A \tup{-modules} \} }
{ \tup{isomorphism} } \iso 
\frac{ \{ \tup{dualizing DG} \, \bar{A} \tup{-modules} \}  }
{ \tup{isomorphism} } . \]
\end{cor}

\begin{proof}
By Corollary \ref{cor:50} the actions of the groups $\opn{DPic}(A)$ and 
$\opn{DPic}(\bar{A})$ on these two sets, respectively, are simply transitive.
And by Theorem \ref{thm:40} the group homomorphism 
$\opn{DPic}(A) \to \opn{DPic}(\bar{A})$
induced by $P \mapsto \bar{A} \ot^{\mrm{L}}_A P$ is bijective. 
Thus it suffices to prove that the function induced by 
$R \mapsto \opn{RHom}_A(\bar{A}, R)$ is equivariant for the action of 
$\opn{DPic}(A)$. Here is the calculation:
\[ \begin{aligned}
& \opn{RHom}_A(\bar{A}, P \ot^{\mrm{L}}_A R) \cong^{\ddag}
P \ot^{\mrm{L}}_A  \opn{RHom}_A(\bar{A}, R) 
\\ & \qquad \cong 
(\bar{A} \ot^{\mrm{L}}_A P) \ot^{\mrm{L}}_{\bar{A}}  \opn{RHom}_A(\bar{A}, R) . 
\end{aligned} \]
The isomorphism $\cong^{\ddag}$ comes from Lemma \ref{lem:45}  
below, noting that the tilting DG module $P$ satisfies condition ($*$) of the 
lemma, since it is perfect.
\end{proof}

We say that a DG $A$-module $N$ has {\em bounded below generation} if it is 
generated in the integer interval $[i_0, \infty]$ for some integer $i_0$;
see Definition \ref{dfn:390}. 

\begin{lem} \label{lem:45}
Let $L \in \cat{D}^{-}_{\mrm{f}}(A)$ and $M, N \in \cat{D}^{+}(A)$.
Assume that $N$ satisfies this condition\tup{:}
\begin{enumerate}
\item[($*$)] There is a covering sequence $(s_1, \ldots, s_n)$ of 
$\bar{A}$, and for every $i$ there is 
an isomorphism $A_{s_i} \ot_A N \cong \til{N}_i$ in $\cat{D}(A_{s_i})$,
where $\til{N}_i$ is a K-flat DG $A_{s_i}$-module with bounded below 
generation.
\end{enumerate}
Then the canonical morphism 
\[ \psi_{L, M, N} : \opn{RHom}_A(L, M) \ot^{\mrm{L}}_A N \to 
\opn{RHom}_A(L, M \ot^{\mrm{L}}_A N) \]
in $\cat{D}(A)$, from formula \tup{(\ref{eqn:400})}, is an isomorphism.
\end{lem}

\begin{proof}
Step 1. Here we assume that $N \cong \til{N}$ in $\cat{D}(A)$, where $\til{N}$ 
is a K-flat DG $A$-module of bounded below generation. Using smart truncation 
if needed, we can assume that the DG 
$B$-module $M$ is bounded below. Let $\til{L} \to L$ be a pseudo-finite 
semi-free resolution over $A$ (see Proposition \ref{prop:101}).
The morphism $\psi_{L, M, N}$ is represented by the homomorphism 
\[ \til{\psi}_{\til{L}, M, \til{N}} :  \opn{Hom}_A(\til{L}, M) \ot^{}_A \til{N} 
\to \opn{Hom}_A(\til{L}, M \ot^{}_A \til{N}) \]
in $\cat{C}(A)$. 
Because the semi-free DG $A$-module $\til{L}$ is bounded above and has 
finitely many basis elements in each degree, and both $M$ and $M \ot_A \til{N}$ 
are bounded below, we see that $\til{\psi}_{\til{L}, M, \til{N}}$ is bijective. 

\medskip \noindent 
Step 2. 
Here $N$ satisfies condition ($*$).  We claim that the obvious morphisms
\begin{equation} \label{eqn:415}
\bigl( \opn{RHom}_A(L, M) \ot^{\mrm{L}}_A N \bigr) \ot_{A^0} A^0_{s_i} \to
\opn{RHom}_A(L, M) \ot^{\mrm{L}}_{A} \til{N}_i 
\end{equation}
and 
\begin{equation} \label{eqn:416}
\opn{RHom}_A(L, M \ot^{\mrm{L}}_A N) \ot_{A^0} A^0_{s_i} \to
\opn{RHom}_A(L, M \ot^{\mrm{L}}_{A} \til{N}_i) 
\end{equation}
in $\cat{D}(A)$, that come from the given isomorphisms 
$A_{s_i} \ot_A N \iso \til{N}_i$, are isomorphisms.
That  (\ref{eqn:415}) is an isomorphism is trivial.
As for the morphism  (\ref{eqn:416}): condition ($*$) implies that 
$M \ot^{\mrm{L}}_A N$ belongs to $\cat{D}^{+}(A)$. Since $A^0_{s_i}$ is a 
K-flat DG module over $A^0$ generated in degree $0$, we can use Step 1.

\medskip \noindent 
Step 3. Now we are in the general situation. 
Let $\psi_i$ be the morphism gotten from $\psi_{L, M, N}$ by the localization 
$A^0_{s_i} \ot_{A^0} - $, so $\psi_i$  goes from the first object in 
(\ref{eqn:415}) to the first object in (\ref{eqn:416}). 
Since $\bar{A} \to \prod_i \bar{A}_{s_i}$ is faithfully flat, it suffices to 
prove that all the $\psi_i$ are isomorphisms. 
But by step 2 it suffices to show that 
\[ \psi_{L, M, \til{N}_i} : \opn{RHom}_A(L, M) \ot^{\mrm{L}}_{A} \til{N}_i \to 
\opn{RHom}_A(L, M \ot^{\mrm{L}}_{A} \til{N}_i)  \]
is an isomorphism. Since $\til{N}_i$ is a K-flat DG $A$-module with bounded 
below generalization, we can use step 1.
\end{proof}

\begin{cor} \label{cor:41}
If the ring $\bar{A}$ is local, then any two dualizing DG $A$-modules 
$R$ and $R'$ satisfy $R' \cong R[m]$ for some integer $m$. 
\end{cor}

\begin{proof}
By Corollary \ref{cor:315} we have 
$\opn{DPic}(A) \cong \Z$, generated by the class of $A[1]$. Now use 
Corollary \ref{cor:50}.
\end{proof}

\begin{prop} \label{prop:80}
Let $A$ be a cohomologically noetherian  DG ring, and let 
$R$ be a dualizing DG $A$-module. Assume $A$ is cohomologically bounded.
Then $R$ is dualizing in the sense of 
\cite[Definition 1.8]{FIJ}.
\end{prop}

\begin{proof}
There are four conditions in \cite[Definition 1.8]{FIJ}. Condition (1) -- 
the existence of resolutions -- is trivial in our commutative situation. 
Condition (2) says that if $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$ then 
$\opn{RHom}_A(M, R) \in  \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$; and this is true by 
Proposition \ref{prop:250}(1). 
Condition (3) requires that for any $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$,
letting $N$ be either $M$ or $M \ot^{\mrm{L}}_{A} R$, 
the adjunction morphisms 
\[ N \to \opn{RHom}_A \bigl( \opn{RHom}_A(N, R), R \bigr) \]
are isomorphisms. Now by Corollary \ref{cor:380} we know that 
$R \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$.
A combination of Proposition \ref{prop:35} and Theorem \ref{thm:30}(1)
tells us that $M \ot^{\mrm{L}}_{A} R \in \cat{D}^{-}_{\mrm{f}}(A)$.
Thus in both cases $N \in \cat{D}^{-}_{\mrm{f}}(A)$, and 
according to Proposition \ref{prop:250}(2) the morphism in question is an 
isomorphism. Condition (4) is part of condition (3) in the commutative 
situation. 
\end{proof}

\begin{dfn} \label{dfn:405}
A cohomologically noetherian cohomologically bounded DG ring $A$ is 
called {\em Gorenstein} if the DG module $A$ has finite injective dimension 
relative to $\cat{D}(A)$.
\end{dfn}

\begin{prop} \label{prop:45}
Let $A$ be a cohomologically noetherian cohomologically bounded DG ring. The 
following conditions are equivalent\tup{:}
\begin{enumerate}
\rmitem{i} $A$ is Gorenstein. 
\rmitem{ii} The DG $A$-module $A$ is dualizing. 
\end{enumerate}
\end{prop}

\begin{proof}
Since conditions (i) and (iii) of Definition \ref{dfn:253}
are automatic for $R := A$, this is clear. 
\end{proof}

\begin{rem}
For DG rings that are not cohomologically bounded, a comparison like in 
Proposition \ref{prop:80}  does not seem to work nicely.  
Corollary \ref{cor:41} is very similar to \cite[Theorem III]{FIJ}; 
but of course the assumptions are not the same. 

We do not know a reasonable definition of Gorenstein DG rings that are not 
cohomologically bounded. 
\end{rem}

Here is a rather surprising result, that was pointed out to us 
by J{\o}rgensen. 

\begin{thm} \label{thm:73}
Let $A$ be a DG ring, which is cohomologically bounded and cohomologically 
essentially finite type over some noetherian ring $\K$. If $\bar{A}$ is a 
perfect DG $A$-module, then the canonical homomorphism $A \to \bar{A}$ is a 
quasi-isomorphism. 
\end{thm}

Example \ref{exa:400} shows that the assumption that $A$ is cohomologically 
bounded is really needed. 

\begin{proof}
We will prove that $\bar{A}_{\p} \ot_{\bar{A}} \opn{H}^i(A) = 0$
for every $i < 0$ and every $\p \in \opn{Spec} \bar{A}$. 

Fix such $i$ and $\p$. Because the assertion is invariant under DG ring 
quasi-iso\-morphisms, we may assume, by Lemma \ref{lem:380} (replacing 
$A$ with $A_{\mrm{eft}}$), that $A^0$ 
is a noetherian ring. Consider the ring 
$A_{\p}^0 := \til{S}^{-1} \cd A^0$, 
 where $\pi : A \to \bar{A}$ is the canonical homomorphism, 
$S := \bar{A} - \p$, and $\til{S} := \pi^{-1}(S) \cap A^0$. 
Next define the DG ring 
$A_{\p} := A_{\p}^0 \ot_{A^0} A$.
Then $A^0_{\p} \to \bar{A}_{\p}$ is surjective, and
$A^0_{\p}$ is a noetherian local ring. By Proposition \ref{prop:81}(2) 
the DG $A_{\p}$-module $\bar{A}_{\p} \cong A_{\p} \ot_A \bar{A}$ is perfect; 
and by Theorem \ref{thm:74} this is a compact object of 
$\cat{D}(A_{\p})$. Also $\bar{A}_{\p}$ is nonzero. 
According to \cite[Theorem 0.2]{Jo} we have 
$\opn{amp}(\opn{H}(A_{\p})) \leq \opn{amp}(\opn{H}(\bar{A}_{\p})) = 0$.
Therefore 
$\opn{H}^i(A_{\p}) = 0$ for all $i < 0$. 
But $\opn{H}^i(A_{\p}) \cong \bar{A}_{\p} \ot_{\bar{A}} \opn{H}^i(A)$.
\end{proof}

We conclude this section with several examples and remarks. 

\begin{exa}
Suppose $A$ is a Gorenstein noetherian ring, and 
$\bsym{a} = (a_1, \ldots, a_n)$ is a sequence of elements in $A$. 
Let $B := \opn{K}(A; \bsym{a})$, the Koszul complex, which is cohomologically 
noetherian and cohomologically bounded. The DG ring homomorphism 
$A \to B$ is cohomologically pseudo-finite, $R_A := A[n]$ is a dualizing DG 
$A$-module, and hence 
$R_B := \opn{RHom}_A(B, R_A)$ is a dualizing DG $B$-module. But $B$ is 
semi-free as DG $A$-module, and therefore 
\[ R_B = \opn{RHom}_A(B, A[n]) \cong \opn{Hom}_A(B, A[n]) \cong B \]
in $\cat{D}(B)$. We see that $B$ is Gorenstein, in the sense of Definition 
\ref{dfn:405}.
\end{exa}

\begin{exa} \label{exa:113}
Here is a comparison to Hinich's notion of dualizing DG module from \cite{Hi1}.
Let $A$ be a noetherian local ring, with maximal ideal $\m$. 
For the sake of simplicity, let us assume that $A$ contains a field $\K$, such 
that $\K \to A / \m$ is finite. 
Let $\bsym{a} = (a_1, \ldots, a_n)$ be a sequence of elements in $A$ that 
generates an $\m$-primary ideal, and let 
$B := \opn{K}(A; \bsym{a})$ be the associated Koszul complex. 
Thus $\K \to B$ is a cohomologically pseudo-finite homomorphism of DG rings, 
and according to Proposition \ref{prop:252} the DG $B$-module
$R_B := \opn{Hom}_{\K}(B, \K)$ is dualizing. Now 
$\opn{Hom}_{\K} \bigl( \opn{H}(R_B), \K \bigr) \cong \opn{H}(B)$
as graded $\opn{H}(B)$-modules, so $R_B$ is a dualizing DG module in the sense 
of Hinich. Taking Corollary \ref{cor:41} into consideration, we see that any 
dualizing DG $B$-module $R$ (in our sense) satisfies the condition of Hinich. 
\end{exa}

\begin{rem} \label{rem:317}
The results in our paper so far suggest an analogy between the 
following two scenarios:
\begin{itemize}
\item[(dg)] The {\em DG scenario}: a cohomologically pseudo-noetherian 
DG ring $A$, with reduction $\bar{A} := \opn{H}^0(A)$. 
\item[(ad)] The {\em adic scenario}: a noetherian ring $A$, 
$\a$-adically complete w.r.t.\ an ideal $\a$,  with reduction 
$\bar{A} := A / \a$.
\end{itemize}
We refer to this as the {\em DG vs.\ adic analogy}.
This analogy restricts to the ``degenerate cases'' in these scenarios:
\begin{itemize}
\item[(dg)] The cohomology $\opn{H}(A)$ is bounded.
\item[(ad)] The defining ideal $\a$ is nilpotent. 
\end{itemize}
Of course, this observation is not new (cf.\ \cite{Lu1}, \cite{Lu2}, \cite{TV} 
and \cite{AG}). 

The DG vs.\ adic analogy holds also for ``finite homomorphisms'':
\begin{itemize}
\item[(dg)] A cohomologically pseudo-finite homomorphism $f : A \to B$
between cohomologically pseudo-noetherian DG rings 
(Definition \ref{dfn:252}).
\item[(ad)] A {\em formally finite} or {\em pseudo-finite} 
homomorphism $f : A \to B$ between adically complete noetherian  
rings, as in \cite{Ye1} and  \cite{AJL2} respectively.
\end{itemize}
There is a further analogy between ``dualizing objects'' in the two scenarios:
\begin{itemize}
\item[(dg)] A dualizing DG module $R$ over a cohomologically pseudo-noetherian 
 DG ring $A$ (Definition \ref{dfn:253}).
\item[(ad)] A {\em t-dualizing complex} $R$ over an adically complete 
noetherian ring $A$, as in \cite{Ye1} and \cite{AJL1}.
\end{itemize}

The analogies above raise two questions: 
\begin{enumerate}
\item Is there a DG analogue of the {\em c-dualizing complex} of \cite{AJL1}?
\item Is there a DG analogue of the {\em GM Duality} of \cite{AJL1} and the
{\em MGM Equivalence} of \cite{PSY}?
\end{enumerate}
\end{rem}

\begin{rem} \label{rem:70}
Recall that a noetherian ring $A$ of finite Krull dimension is regular (i.e.\ 
all its local rings $A_{\p}$ are regular) iff it has finite global 
cohomological dimension. 

Now suppose $A$ is a cohomologically pseudo-noetherian DG ring. 
By ``Krull dimension'' we could mean that of $\bar{A}$, but 
``regular local ring'' has no apparent meaning here.
Hence we propose this definition:  $A$ is  called
{\em regular} if it has {\em finite global cohomological dimension}. By this we 
mean that there is a natural number $d$, such that if
$M \in \cat{C}(A)$ is generated in the integer interval $[i_0, i_1]$, then 
$M$ has projective dimension at most $d + i_1 - i_0$; cf.\ Definitions 
\ref{dfn:390} and \ref{dfn:11}, and Examples \ref{exa:390} and \ref{exa:520}.
According to Theorem \ref{thm:50}, we see that any 
$M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$, including $M = \bar{A}$, is perfect.

Now assume that $A$ is a regular DG ring, but with {\em bounded 
cohomology}. Then, taking $M = \bar{A}$, Theorem \ref{thm:73} says that 
$A \to \bar{A}$ is a quasi-isomorphism. The conclusion is that {\em 
the only regular DG rings with bounded cohomology are the regular rings} (up to 
quasi-isomorphism). 

Under the DG vs.\ adic analogy of Remark \ref{rem:317}, this corresponds 
to an adic ring $A$ with a nilpotent defining ideal $\a$. If $A$ is 
regular, then it cannot have nonzero nilpotent elements. Therefore $\a = 0$ 
here, and $A \to \bar{A}$ is bijective.
\end{rem}

\begin{exa} \label{exa:400}
Take a field $\K$, and let $A := \K[t]$, the polynomial ring in a variable $t$ 
of degree $-2$. We view $A$ as a DG ring with zero differential, so 
$\opn{H}(A) \cong A$, and it is cohomologically noetherian, but not 
cohomologically bounded below. The DG ring 
homomorphism $\K \to A$ is cohomologically pseudo-finite. Hence the DG 
$A$-module $R := \opn{Hom}_{\K}(A, \K)$ is dualizing. This DG module is not 
bounded above.
 
Note that here $\bar{A} \cong \K$ is a perfect DG $A$-module.
To show this, we shall produce a finite semi-free resolution of $\bar{A}$.
The DG module $A^{\leq -2}$, which is both the stupid 
and the smart truncation of $A$ at $-2$, is free, since 
$A^{\leq -2} \cong A[2]$ as DG $A$-modules. Let 
$\phi : A^{\leq -2} \to A$ be the inclusion, and let 
$P := \opn{cone}(\phi)$. There is an obvious quasi-isomorphism 
$P \to \bar{A}$.   

The adic analogue is the ring of formal power series 
$A := \K[[t]]$, with ideal of definition $\a := (t)$. The corresponding 
t-dualizing complex is $R := \opn{Hom}_{\K}^{\mrm{cont}}(A, \K)$,
which is an artinian $A$-module of infinite length. 
\end{exa}

\begin{rem} \label{rem:316}
Our definition of dualizing DG modules, Definition \ref{dfn:253}, might seem 
an almost straightforward generalization of Grothendieck's original definition 
in \cite{RD}. However there are at least two subtle points: (a) Finding 
the correct notion of injective dimension of a DG module (condition (ii) of 
Definition \ref{dfn:253}). (b) Allowing a dualizing DG module to have unbounded 
above cohomology (condition (i) of Definition \ref{dfn:253}; 
cf.\ Corollary \ref{cor:380} and Remark \ref{rem:317}).

All results in this section, up to and including Corollary 
\ref{cor:50}, might also seem to be straightforward generalizations of 
Grothendieck's corresponding results in \cite{RD}. But the technical 
difficulties (mainly when $A$ is cohomologically unbounded) cannot be 
neglected. 

We should mention that Theorem \ref{thm:51} can be made a bit stronger, by 
replacing the condition that $A$ is tractable with the weaker condition that 
there is a cohomologically essentially finite type homomorphism $\K \to A$, 
where $\K$ is a noetherian ring with a dualizing complex.
Theorem \ref{thm:73} can be similarly strengthened.

Some earlier papers, notably \cite{Hi1} and \cite{FIJ}, had adopted
other definitions of dualizing DG modules; see Example \ref{exa:113} and
Proposition \ref{prop:80} respectively. These definitions are not consistent 
with our definition in general, and there does not appear to be a 
well-developed theory for them.  

In \cite[Definition 4.2.5]{Lu2}, Lurie gives a definition of a
dualizing $\mrm{E}_{\infty}$ module 
over an $\mrm{E}_{\infty}$ ring. Now any DG ring $A$ can be viewed as an 
$\mrm{E}_{\infty}$ ring, and DG $A$-modules can be viewed $\mrm{E}_{\infty}$ 
$A$-modules. Under this correspondence, it seems that
a dualizing DG $A$-module, in the sense of Definition \ref{dfn:253} above,
becomes a dualizing module in the sense of \cite{Lu2}. (We are being careful, 
because a precise comparison of the definitions is not so easy.)
Thus our results in this section, up to and including Corollary 
\ref{cor:50}, might be viewed as special instances of Lurie's  
statements. Still, an attempt to produce a full proof of our results
based on the corresponding results in \cite{Lu2} (e.g.\ deducing our Theorem 
\ref{thm:51} from \cite[Theorem 4.3.14]{Lu2}, or deducing our Theorem 
\ref{thm:43} from \cite[Proposition 4.2.9]{Lu2}) might be nontrivial, and most 
likely it would be longer than our own direct proofs. This is because, as far 
as we know, there do not exist full comparison results for the monoidal 
operations between the $\mrm{E}_{\infty}$ and the DG setups. 
 
Our Corollary \ref{cor:80} appears to be totally new. We could not find 
anything resembling it in Lurie's papers, nor elsewhere in the literature. 
Likewise for Theorem \ref{thm:73} (except for J{\o}rgensen's original local 
result).
\end{rem}

\begin{rem} \label{rem:315}
A result that is noticeably missing from our paper is a DG analogue of 
\cite[Theorem 4.3.5]{Lu2}. Translated to the DG terminology, it states that if 
the ring $\bar{A}$ admits a dualizing DG module, then the DG ring $A$ 
admits a dualizing DG module. We do not know whether this result can be 
proved within the DG framework; this is a question that we find interesting.

Note however that the corresponding result in the adic case, namely when 
$A$ is a complete $\a$-adic ring extension of $\bar{A}$ (cf.\ Remark 
\ref{rem:317}), was proved a long time ago by Faltings \cite{Fa}.
The proof of the nilpotent case in \cite{Fa} is quite easy; but the  
passage to the complete adic case is somewhat involved there. The proof can be 
greatly simplified by first proving the existence of a t-dualizing complex
$R'_A$ over $A$, and then applying derived completion to obtain a c-dualizing 
complex $R_A := \mrm{L} \Lambda_{\a}(R'_A)$. 
See \cite{Ye1} \cite{AJL1}, \cite{AJL2} and \cite{PSY} for information on 
derived completion, and on dualizing complexes over adic rings.
\end{rem}
