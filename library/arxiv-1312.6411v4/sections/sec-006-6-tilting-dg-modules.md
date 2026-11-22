---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-006-6-tilting-dg-modules
section_title: "Tilting DG Modules"
section_number: 6
pages: 30-35
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.977
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:tilting}

Recall that all DG rings here are commutative (Convention \ref{conv:100}). In 
particular all rings are commutative. 

\begin{dfn}
Let $A$ be a DG ring.
A DG $A$-module $P$ is called a {\em tilting DG module} if there 
exists some DG $A$-module $Q$ such that $P \ot^{\mrm{L}}_A Q \cong A$
in $\cat{D}(A)$.  
\end{dfn}

The DG module $Q$ in the definition is called a {\em quasi-inverse} of $P$.
Due to the symmetry of the operation $- \ot^{\mrm{L}}_A- $, $Q$ is also 
tilting. It is easy to see that the quasi-inverse $Q$ is unique, up to a 
nonunique isomorphism. If $P_1$ and $P_2$ are tilting then so is 
$P_1 \ot^{\mrm{L}}_A P_2$; this is because of the associativity of  
$- \ot^{\mrm{L}}_A- $. Hence the next definition makes sense. 

\begin{dfn} \label{dfn:350}
The {\em commutative derived Picard group} of $A$ is the abelian group \lb 
$\opn{DPic}(A)$, whose elements are the isomorphism classes, in $\cat{D}(A)$,
of tilting DG $A$-modules. The product is induced by the operation
$- \ot^{\mrm{L}}_A -$, and the unit element is the class of  $A$. 
\end{dfn}

\begin{lem} \label{lem:80}
Let $f : A \to B$ be a homomorphism of DG rings.
\begin{enumerate}
\item For any $M, N \in \cat{D}(A)$ there is an isomorphism 
\[  (B \ot^{\mrm{L}}_A M) \ot^{\mrm{L}}_B (B \ot^{\mrm{L}}_A N) \cong 
B \ot^{\mrm{L}}_A (M \ot^{\mrm{L}}_A N) \]
in $\cat{D}(A)$. 

\item If $P$ is a tilting DG $A$-module, then $B \ot^{\mrm{L}}_A P$ is a 
tilting DG $B$-module.

\item If $f$ is a quasi-isomorphism and $Q$ is a tilting DG $B$-module, then 
$\opn{rest}_f(Q)$ is a tilting DG $A$-module. 
\end{enumerate}
\end{lem}

\begin{proof}
(1) Choose K-flat resolutions $\til{M} \to M$ and $\til{N} \to N$
over $A$. Then $B \ot_A \til{M}$ and $B \ot_A \til{N}$ are K-flat over $B$, 
$\til{M} \ot_A \til{N}$ is K-flat over $A$, and 
\[ \begin{aligned}
& (B \ot^{\mrm{L}}_A M) \ot^{\mrm{L}}_B (B \ot^{\mrm{L}}_A N) \cong 
(B \ot_A \til{M}) \ot_B (B \ot_A \til{N}) 
\\
& \quad 
\cong B \ot_A (\til{M} \ot_A \til{N}) \cong
B \ot^{\mrm{L}}_A (M \ot^{\mrm{L}}_A N) .
\end{aligned} \]

\medskip \noindent
(2) Let $P, Q \in \cat{D}(A)$ be such that 
$P \ot^{\mrm{L}}_A Q \cong A$. By (1)  we have 
\[ (B \ot^{\mrm{L}}_A P) \ot^{\mrm{L}}_B (B \ot^{\mrm{L}}_A Q) \cong  B . \]

\medskip \noindent
(3) Say $Q_1, Q_2 \in \cat{D}(B)$ satisfy
$Q_1 \ot^{\mrm{L}}_B Q_2 \cong B$. Let 
$P_i := \opn{rest}_f(Q_i) \in \cat{D}(A)$. 
By the equivalence for DG ring  
quasi-isomorphisms (see \cite[Proposition 1.4]{YZ1}) we have 
\[ P_1 \ot^{\mrm{L}}_A P_2 \cong 
\opn{rest}_f( Q_1 \ot^{\mrm{L}}_B Q_2 ) \cong 
\opn{rest}_f(B) \cong A . \]
\end{proof}

\begin{prop} \label{prop:32}
Let $f : A \to B$ be a homomorphism of DG rings.
\begin{enumerate}
\item There is a group homomorphism
\[ \opn{DPic}(f) : \opn{DPic}(A) \to \opn{DPic}(B)  \]
with formula
$P \mapsto B \ot^{\mrm{L}}_A P$.

\item If $f$ is a quasi-isomorphism then $\opn{DPic}(f)$ is bijective.
\end{enumerate}
\end{prop}

\begin{proof}
(1) This follows from parts (1) and (2) of the lemma above. 

\medskip \noindent
(2) Part (3) of Lemma \ref{lem:80} shows that in case $f$ is a 
quasi-isomorphism, the function 
$Q \mapsto \opn{rest}_f(Q)$ is an inverse of  $\opn{DPic}(f)$.
\end{proof}

\begin{thm} \label{thm:76}
Let $A$ be a DG ring and $P \in \cat{D}(A)$. The following 
four conditions are equivalent.
\begin{enumerate}
\rmitem{i} The DG $A$-module $P$ is tilting.

\rmitem{ii} The functor $P \ot^{\mrm{L}}_A -$ is an equivalence of 
$\cat{D}(A)$. 

\rmitem{iii}  The functor $\opn{RHom}_{A}(P, -)$ is an equivalence of 
$\cat{D}(A)$. 

\rmitem{iv}  The DG $A$-module $P$ is perfect, and the adjunction morphism 
$A \to \opn{RHom}_A(P, P)$ in $\cat{D}(A)$ is an isomorphism.
\end{enumerate} 
\end{thm}

\begin{proof}
(i) $\Rightarrow$ (ii): Let $Q$ be a quasi-inverse of $P$. Then the functor  
$G(M) := Q \ot^{\mrm{L}}_A M$ is a quasi-inverse of the functor 
$F(M) := P \ot^{\mrm{L}}_A M$.

\medskip \noindent
(ii) $\Rightarrow$ (i): The functor $F := P \ot^{\mrm{L}}_A -$ is 
essentially surjective on objects, so there is some $Q \in \cat{D}(A)$
such that $F(Q) \cong A$. Then $Q$ is a quasi-inverse of $P$. 

\medskip \noindent
(ii) $\Leftrightarrow$ (iii): The functors 
$F := P \ot^{\mrm{L}}_A -$ and 
$G := \opn{RHom}_{A}(P, -)$
are adjoints, so $F$ is an equivalence iff $G$ is an equivalence.

\medskip \noindent 
(ii) $\Rightarrow$ (iv): 
Consider the auto-equivalence $F := P \ot^{\mrm{L}}_A -$ of $\cat{D}(A)$.
Since $A$ is compact and $P = F(A)$, it follows that $P$ is compact. 
Now according to Theorem \ref{thm:74}, perfect is the same as compact. 

For any $M \in \cat{D}(A)$, the adjunction morphism 
$A \to \opn{RHom}_A(M, M)$ is an isomorphism iff the canonical 
graded ring homomorphism 
\[ \al_M : \opn{H}(A) \to 
\bigoplus_{k \in \Z} \, \opn{Hom}_{\cat{D}(A)}(M, M[k]) \]
is bijective. The equivalence $F$ induces a commutative diagram of graded rings 
\[ \UseTips \xymatrix @C=5ex @R=5ex {
\opn{H}(A)
\ar[d]_{\al_M}
\ar[dr]^{\al_{F(M)}}
\\
\displaystyle\bigoplus_{k \in \Z} \, \opn{Hom}_{\cat{D}(A)}(M, M[k]) 
\ar[r]^(0.44){F}
&
\displaystyle\bigoplus_{k \in \Z} \, 
\opn{Hom}_{\cat{D}(A)} \bigl( F(M), F(M)[k] \bigr)
} \]
in which the horizontal arrow is an isomorphism. 
Now take $M := A$. Because $\al_A$ is an isomorphism, so is $\al_P$.

\medskip \noindent
(iv) $\Rightarrow$ (i): 
Define $Q := \opn{RHom}_A(P, A) \in \cat{D}(A)$.
The implication (i) $\Rightarrow$ (iii) of Theorem \ref{thm:74} 
shows that 
\[ Q \ot^{\mrm{L}}_A P =  \opn{RHom}_A(P, A) \ot^{\mrm{L}}_A P
\cong \opn{RHom}_A(P, P) \cong A \]
in $\cat{D}(A)$. So $P$ is tilting, with quasi-inverse $Q$. 
\end{proof}

\begin{cor} \label{cor:405}
Let $P$ be a tilting DG $A$-module. Then the DG $A$-module 
$Q := \lb \opn{RHom}_A(P, A)$ is a quasi-inverse of $P$. 
\end{cor}

\begin{proof}
This was shown in the proof of the implication 
(iv) $\Rightarrow$ (i) above.
\end{proof}

\begin{rem} \label{rem:510}
A DG $A$-module $M$ for which the adjunction 
morphism $A \to \lb \opn{RHom}_A(M, M)$ is an isomorphism, is sometimes called 
{\em semidualizing}; cf.\ \cite{AIL}. Indeed, this condition is part of the 
definition of a {\em dualizing DG module} (see Definition \ref{dfn:253} below). 
But as we saw in Theorem \ref{thm:76}, this condition is also characteristic of 
tilting DG modules -- so the name semidualizing might be confusing. 
\end{rem}

\begin{cor} \label{cor:73}
Let $P$ be a tilting DG $A$-module, and let 
$F := P \ot^{\mrm{L}}_A -$
be the corresponding auto-equivalence of $\cat{D}(A)$.
\begin{enumerate}
\item The functor $F$ has finite cohomological dimension, and it preserves 
$\cat{D}^+(A)$, $\cat{D}^-(A)$ and 
$\cat{D}^{\mrm{b}}(A)$.

\item If $A$ is cohomologically pseudo-noetherian, then the auto-equivalence 
$F$ preserves the subcategory $\cat{D}_{\mrm{f}}(A)$. 
\end{enumerate}
\end{cor}

\begin{proof}
(1) The theorem says that $P$ is perfect. 
Let $s_1, \ldots, s_n \in \bar{A}$ and $P_1, \ldots, P_n$ be as in Definition 
\ref{dfn:25}.
Let $d_0 \leq d_1$ be integers such that each $P_i$ is generated in 
the integer interval $[d_0, d_1]$. Then the functor $F$
has cohomological displacement at most $[d_0, d_1]$ relative to 
$\cat{D}(A)$, and cohomological dimension at most $d_1 - d_0$. The claim about 
$\cat{D}^{\star}(A)$ is now clear. 

\medskip \noindent
(2) Use Theorem \ref{thm:30}(2), noting that 
$F(A) = P \in \cat{D}^-_{\mrm{f}}(A)$,
by Theorems \ref{thm:76} and \ref{thm:50}.
\end{proof}

\begin{prop} \label{prop:313}
Let $A$ be a DG ring, and let 
$\bsym{e} = (e_1, \ldots, e_n)$ be an idempotent covering sequence of 
$\bar{A} = \opn{H}^0(A)$. For 
any $i$ we have the localized DG ring $A_i = A_{e_i}$ from Definition 
\tup{\ref{dfn:40}}, and the DG ring homomorphism
$\la_i : A \to A_i$.
Then the group homomorphisms 
\[ \opn{DPic}(\la_i) : \opn{DPic}(A) \to \opn{DPic}(A_i) \]
induce a group isomorphism
\[ \opn{DPic}(A) \iso \prod_{i = 1}^n \, \opn{DPic}(A_i) . \]
\end{prop}

\begin{proof}
(1) According to Proposition \ref{prop:20} there is a DG ring quasi-isomorphism 
$\la : A \to \prod_{i = 1}^n A_i$. By Proposition \ref{prop:32}(2) there is a 
group isomorphism 
\[ \opn{DPic}(\la) : \opn{DPic}(A) \iso 
\opn{DPic} \Bigl( \, \prod\nolimits_{i = 1}^n A_i \, \Bigr) . \]
And there is an obvious group isomorphism 
\[ \opn{DPic} \Bigl( \, \prod\nolimits_{i = 1}^n A_i \, \Bigr) \cong 
\prod_{i = 1}^n \, \opn{DPic}(A_i) . \]
\end{proof}

From here to Theorem \ref{thm:315} we consider a ring $A$. The first lemma 
goes back to \cite[Lemma V.3.3]{RD}, and it reappeared, in a noncommutative 
guise, in \cite{Ye2} and \cite{RZ}. But in the prior treatments the ring $A$ 
was assumed to be noetherian. Therefore we give a full proof of the general 
case. 

\begin{lem} \label{lem:575}
Let $A$ be a local ring, and let $P$ be a tilting DG $A$-module. 
Then $P \cong A[k]$ in $\cat{D}(A)$ for some integer $k$. 
\end{lem}

\begin{proof}
Since $P$ is a perfect complex of $A$-modules (Theorem \ref{thm:76}), it is 
iso\-morphic in $\cat{D}(A)$ to a bounded complex of finite projective 
$A$-modules. Say  $\opn{con}(\opn{H}(P)) = [i_0, i_1]$ for some integers $i_0 
\leq i_1$. By replacing $P$ with such a resolution, and then splitting off 
extra 
terms in high and low degrees, we can assume that $P$ is a complex of finite 
projective $A$-modules, concentrated in the degree interval $[i_0, i_1]$. Then 
$P' := \opn{H}^{i_1}(P)$ is a nonzero finitely presented $A$-module.  

Let $Q$ be a quasi-inverse of $P$. By the same reasoning, we can assume that 
$Q$ is a complex of finite projective $A$-modules, concentrated in a degree 
interval $[j_0, j_1]$, and $Q' := \opn{H}^{j_1}(Q)$ is a nonzero finitely 
presented $A$-module.

Now by the K\"unneth trick we have isomorphisms of $A$-modules
\[ P' \ot_A Q' \cong \opn{H}^{i_1 + j_1}(P \ot^{\mrm{L}}_A Q) \cong 
\opn{H}^{i_1 + j_1}(A) . \]  
On the other hand $P' \ot_A Q' \neq 0$, by Nakayama. The conclusion is that 
$i_1 + j_1 = 0$ and $P' \ot_A Q' \cong A$. 
This tells us that $P'$ and $Q'$ are flat $A$-modules. 
Again by Nakayama, we see that $P' \cong Q' \cong A$. 

Finally, we can split the complexes $P$ and $Q$ into 
$P \cong P'[-i_1] \oplus P^{\mrm{ex}}$
and 
$Q \cong Q'[-j_1] \oplus Q^{\mrm{ex}}$,
where $P^{\mrm{ex}}$ and $Q^{\mrm{ex}}$ are complexes of finite projective 
$A$-modules, concentrated in the degree intervals $[i_0, i_1 - 1]$ and 
$[j_0, j_1 - 1]$ respectively. 
Then $\opn{H}(P^{\mrm{ex}} \ot_A Q'[-j_1])$
is a direct summand of the graded module
$\opn{H}(P \ot^{\mrm{L}}_A Q) \cong \opn{H}(A)$. 
Since $\opn{H}(P^{\mrm{ex}} \ot_A Q'[-j_1])$ is concentrated in the interval
$[i_0 + j_1, -1]$,
it must be zero. So $P^{\mrm{ex}} = 0$ in $\cat{D}(A)$, and
$P \cong P'[-i_1]$. 
\end{proof}

Recall that an $A$-module $P$ is called {\em invertible} if it is projective of 
rank $1$. In other words, if $P$ is locally free of rank $1$.  
See \cite[Section II.5.2, Theorem 1]{Bo}. 








\begin{prop} \label{prop:590}
The following conditions are equivalent for an $A$-module $P$~\tup{:}
\begin{enumerate}
\rmitem{i} $P$ is invertible.
\rmitem{ii} When viewed as a DG module, $P$ is tilting. 
\end{enumerate}
\end{prop}

\begin{proof}
The implication (i) $\Rightarrow$ (ii) is trivial. For the other direction: 
the arguments in the first paragraph of the proof of Lemma 
\ref{lem:575} show that $P$ is a finitely presented $A$-module. 
Take any prime ideal $\p$. By Lemma \ref{lem:80}, the DG $A_{\p}$-module 
$P_{\p} := A_{\p} \ot_A P$ is tilting. Hence, by Lemma \ref{lem:575},
we have $P_{\p} \cong A_{\p}$.  
According to \cite[Section II.5.2, Theorem 1]{Bo} the module $P$ is 
invertible.
\end{proof}

\begin{lem} \label{lem:570}
Let $A$ be a ring, and let $P$ be a tilting DG $A$-module. 
Write $X := \opn{Spec} A$, and for any integer $i$ define the set 
\[ Y_i := \{ \p \in X \mid \opn{H}^i(P)_{\p} \neq 0 \} . \]
Then:
\begin{enumerate}
\item Only finitely many of the $Y_i$ are nonzero.
\item $Y_i \cap Y_j = \varnothing$ if $i \neq j$.
\item $X = \bigcup\nolimits_{i} \, Y_i$.
\item For any $i$, the set $Y_i$ is open-closed.
\end{enumerate}
\end{lem}

\begin{proof}
We may assume that  $A \neq 0$, i.e.\ that $X \neq \varnothing$.
This implies that $P \neq 0$. 
We know from Theorem \ref{thm:76} that $P$ is a perfect complex of 
$A$-modules. Therefore the cohomology $\opn{H}(P)$ is bounded, and thus
$\opn{con}(\opn{H}(P)) = [i_0, i_1]$
for some integers $i_0 \leq i_1$. This proves claim (1). 

Take any prime $\p \in X$. By Lemma \ref{lem:80} the DG $A_{\p}$-module 
$P_{\p} := A_{\p} \ot_A P$ is tilting. So by Lemma \ref{lem:575} we have 
$P_{\p} 
\cong A_{\p}[k]$ for some integer $k$. We see that $\p \in Y_{-k}$, and 
$\p \notin Y_{i}$ for $i \neq -k$. This proves claims (2) and (3). 

It remains to prove claim (4). By induction on 
$i_1 - i_0 = \opn{amp}(\opn{H}(P))$, it suffices to prove that $Y' := Y_{i_1}$
is open-closed in $X$. The reason is this: once we know that $Y'$ is 
open-closed, then so is its complement $Y'' := \bigcup_{i_0 \leq i < i_1} Y_i$. 
So $X = Y' \coprod Y''$ as schemes, and correspondingly 
$A = A' \times A''$ as rings, and $P \cong P' \oplus P''$ in $\cat{D}(A)$. 
But $\opn{amp}(\opn{H}(P'')) < i_1 - i_0$. 

As explained in the proof of Lemma \ref{lem:575}, we can 
assume that $P$ is a complex of finite projective $A$-modules, concentrated in 
the degree interval $[i_0, i_1]$. So $Q := \opn{H}^{i_1}(P)$ is a finitely 
presented $A$-module. Because $Y'$ is the support of the module 
$Q$, it is closed in $X$. 

Take a prime $\p \in Y'$. As we have already seen above, the 
$A_{\p}$-module $Q_{\p}$ is isomorphic to $A_{\p}$. According to \cite[Section 
II.5.1, Corollary]{Bo} there is an open neighborhood $U$ of $\p$ in $X$ such 
that $Q_{\q} \cong A_{\q}$ for all $\q \in U$. This shows that $U \subset Y'$. 
Therefore $Y'$ is open in $X$. 
\end{proof}

For a ring $A$ we have the following theorem, due to Negron 
\cite{Ng}. It is a refinement of earlier results, that are due (independently) 
to the author \cite{Ye2} and to Rouquier-Zimmermann \cite{RZ}. 
The earlier results focused on noetherian rings, and hence there was an 
assumption that $\opn{Spec} A$ has finitely many connected components. 
Negron recently noticed that this assumption is superfluous. 

As usual, $\opn{Pic}(A)$ denotes the (commutative) Picard group of $A$, whose 
elements are the isomorphism classes of invertible $A$-modules. 

The abelian group $\opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$
was introduced in Definition \ref{dfn:560}.
As shown in Proposition \ref{prop:550}, each
function $f \in \opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$ 
determines a decomposition 
$A = \prod_{i = 1}^n \, A_i$ of the ring $A$, 
and a nondecreasing sequence of integers $\bsym{k} = (k_1, \ldots, k_n)$. 
The relation is this: $f(\opn{Spec} A_i) = k_i$. 

\begin{thm} \label{thm:315}
Let $A$ be a commutative ring. 
There is a canonical group isomorphism
\[ \opn{DPic}(A) \cong 
\opn{Pic}(A) \times \opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z) \, , \]
characterized as follows\tup{:}
\begin{itemize}
\item The homomorphism 
$\opn{Pic}(A) \to \opn{DPic}(A)$
sends the class of an invertible $A$-module $P$ to its class as a tilting DG 
$A$-module. 

\item Let $f \in \opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$,
with corresponding ring decomposition
$A = \prod_{i = 1}^n \, A_i$
and integer sequence $(k_1, \ldots, k_n)$.
The tilting DG $A$-module associated to $f$ is 
$\bigoplus_{i = 1}^n  A_i[k_i]$.
\end{itemize}
\end{thm}

\begin{proof}
For an invertible $A$-module $Q$ and a function 
$f \in \opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$
let 
\[ G(Q, f) := Q \ot_A \bigl( \bigoplus\nolimits_{i = 1}^n  A_i[k_i] \bigr) , \]
which is a tilting DG $A$-module. We have to prove that the group homomorphism 
\[ \opn{Pic}(A) \times \opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z) \to 
\opn{DPic}(A) \]
induced by $G$ is bijective. 
It is certainly injective: if 
$G(Q, f) \cong A$, then $f$ must be the constant function $0$, as can be 
checked in $\opn{DPic} (A_{\p})$ for each $\p \in \opn{Spec} A$. 
But then $Q \cong A$ in $\cat{D}(A)$, which implies that 
$Q \cong A$ in $\cat{Mod} A$. 

It remains to prove that the group homomorphism induced by $G$ is surjective.
Take any tilting DG $A$-module $P$. Let 
$\opn{Spec} A = \coprod_{i = i_0}^{i_1} \, Y_i$ 
be the decomposition into open-closed sets induced by $P$, from Lemma 
\ref{lem:570}. Consider the locally constant function $f : X \to \Z$ 
defined by $f|_{Y_i} := i$. 
Then the tilting DG module 
$Q := P \ot^{\mrm{L}}_A G(A, f)$ 
has the property that 
$\opn{H}^i(Q) = 0$ for all $i \neq 0$.
By Proposition \ref{prop:590} we know that $Q$ is isomorphic to an invertible 
$A$-module, say $Q'$. But then $P \cong G(Q', -f)$. 
\end{proof}

Let $A$ be a noetherian ring, $\a$-adically complete with respect to some ideal 
$\a$, with reduction $\bar{A} := A / \a$. It is known that the group 
homomorphism $\opn{Pic}(A) \to \opn{Pic}(\bar{A})$ is bijective. For a proof 
see \cite[Exercises II.9.6 and III.4.6]{Ha}. 

The next theorem is a DG analogue of this fact. 
Recall that for a DG ring $A$ there is a canonical homomorphism 
$A \to \bar{A}$.

\begin{thm} \label{thm:40}
Let $A$ be a commutative DG ring.
Then the canonical group homomorphism 
\[ \opn{DPic}(A) \to \opn{DPic}(\bar{A}) \]
is bijective.
\end{thm}
 
\begin{proof}
Let us denote by $\pi : A \to \bar{A}$ the canonical DG ring homomorphism.
We begin by proving that the homomorphism $\opn{DPic}(\pi)$ is injective.
Suppose $P$ is a tilting DG $A$-module such that 
$\bar{A} \ot^{\mrm{L}}_A P \cong \bar{A}$ in $\cat{D}(\bar{A})$. 
By Corollary \ref{cor:73}(1) we know that $P \in \cat{D}^{-}(A)$.
Then Proposition \ref{prop:305}(1) says that $P \cong A$ in $\cat{D}(A)$. 

Now let us prove that  $\opn{DPic}(\pi)$ is surjective.
Take any tilting DG $\bar{A}$-module $\bar{P}$. By Theorem \ref{thm:315} there 
is an isomorphism 
$\bar{P} \cong G(\bar{P}_0, f)$ for some invertible $\bar{A}$-module 
$\bar{P}_0$ and some function $f \in \opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$.

By Proposition \ref{prop:310}, there exists some DG module 
$P_0 \in \cat{D}^{-}(A)$ such that  \lb
$\bar{A} \ot^{\mrm{L}}_A P_0 \cong \bar{P}_0$ in $\cat{D}(\bar{A})$.
Let $\bar{Q}_0 \in \cat{Mod} \bar{A}$ be a quasi-inverse of the invertible 
module $\bar{P}_0$. By the same reason, there exists
$Q_0 \in \cat{D}^{-}(A)$ such that  
$\bar{A} \ot^{\mrm{L}}_A Q_0 \cong \bar{Q}_0$ in $\cat{D}(\bar{A})$.
Now by Lemma \ref{lem:80}(1) we have
\[ \bar{A} \ot^{\mrm{L}}_A (P_0 \ot^{\mrm{L}}_A Q_0) \cong 
\bar{P}_0 \ot^{\mrm{L}}_{\bar{A}} \bar{Q}_0 \cong \bar{A} \]
in $\cat{D}(\bar{A})$. Since 
$P_0 \ot^{\mrm{L}}_A Q_0 \in \cat{D}^{-}(A)$,
by Proposition \ref{prop:305}(1) we know that 
$P_0 \ot^{\mrm{L}}_A Q_0 \cong A$ in $\cat{D}(A)$. This shows that $P_0$ is a 
tilting DG $A$-module. 

Finally, let $\bsym{e} = (e_1, \ldots, e_n)$ and 
$\bsym{k} = (k_1, \ldots, k_n)$ be the data corresponding to $f$ from 
Proposition \ref{prop:550}, and let 
$A \to \prod_{i = 1}^n A_i$ be the $\bsym{e}$-induced decomposition of 
$A$ from Definition \ref{dfn:343}.
Consider the tilting DG $A$-module 
\[ P := P_0 \ot_A \bigl( \bigoplus\nolimits_{i = 1}^n  A_i[k_i] \bigr) . \]
Then 
$\bar{P} \cong \bar{A} \ot^{\mrm{L}}_A P$. 
\end{proof}

\begin{cor} \label{cor:330}
Let $A$ be a DG ring. There is a canonical group isomorphism 
\[ \opn{DPic}(A) \cong  \opn{Pic}(\bar{A}) \times 
\opn{F}_{\mrm{lc}}(\opn{Spec} \bar{A}, \Z) \, . \]
\end{cor}

\begin{proof}
Combine Theorems \ref{thm:40} and \ref{thm:315}.
\end{proof}

\begin{dfn} \label{dfn:330}
Let $A$ be a DG ring. We define $\opn{DPic}^0(A)$ to be the subgroup of 
$\opn{DPic}(A)$ that corresponds to $\opn{Pic}(\bar{A})$, under the 
canonical group isomorphism of Corollary \ref{cor:330}.
\end{dfn}

\begin{cor} \label{cor:315}
If $\bar{A}$ is a local ring, then $\opn{DPic}(A) \cong \Z$.
\end{cor}

\begin{proof}
We know that $\opn{Pic}(\bar{A})$ is trivial, and 
$\opn{Spec} \bar{A}$ is connected. Now use Corollary \ref{cor:330}.
\end{proof}
