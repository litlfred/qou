---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-002-2-cohomological-dimension
section_title: "Cohomological Dimension"
section_number: 2
pages: 11-16
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.964
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:coh-dim}

We continue with the conventions of Section \ref{sec:resol}, namely our DG 
rings are nonpositive, and the DG modules are acted upon from the left. 
The concentration $\opn{con}(M)$ of a graded module $M$ was 
introduced in Definition \ref{dfn:550}.

\begin{dfn} \label{dfn:10}
Let $A$ and $B$ be DG rings, and let
$\cat{E} \subseteq \cat{D}(A)$ be a full subcategory.
\begin{enumerate}
\item Let  $F : \cat{E} \to \cat{D}(B)$ be an additive functor,
and let $[d_0, d_1]$ be an integer interval. We say that {\em $F$ has 
cohomological displacement at most $[d_0, d_1]$} if 
\[ \opn{con} \bigl( \opn{H}(F(M)) \bigr) \subseteq
\opn{con} \bigl( \opn{H}(M) \bigr) + [ d_0, d_1] \]
for every $M \in \cat{E}$.

\item Let $F : \cat{E}^{\mrm{op}} \to \cat{D}(B)$ be an additive functor,
and let $[d_0, d_1]$ be an integer interval. We say that {\em $F$ has 
cohomological displacement at most $[d_0, d_1]$} if 
\[ \opn{con} \bigl( \opn{H}(F(M)) \bigr) \subseteq
- \opn{con} \bigl( \opn{H}(M) \bigr) + [ d_0, d_1] \]
for every $M \in \cat{E}$.

\item Let $F$ be as in item (1) or (2).
The {\em cohomological displacement of $F$} is the smallest integer interval 
$[d_0, d_1]$ for which $F$ has cohomological displacement at most $[d_0, d_1]$.
If $d_0 \in \Z$ (resp.\ $d_1 \in \Z$, resp.\ $d_0, d_1 \in \Z$) then $F$ is 
said to have {\em bounded below} (resp.\ {\em bounded above}, 
resp.\ {\em bounded}) {\em cohomological displacement}.

\item Let $[d_0, d_1]$ be the cohomological displacement of $F$. 
The {\em cohomological dimension} of $F$ is 
$d := d_1 - d_0 \in \N \cup \{ \infty \}$. If $d \in \N$, then $F$ is said 
to have {\em finite cohomological dimension}.
\end{enumerate}
\end{dfn}

Note that if $\cat{E}' \subseteq \cat{E}$, and $F$ has 
cohomological displacement at most $[d_0, d_1]$, then $F|_{\cat{E}'}$ also 
has cohomological displacement at most $[d_0, d_1]$.

\begin{exa} \label{exa:391}
Consider a commutative ring $A = B$, and let $\cat{E} := \cat{D}^{}(A)$.
For the covariant case (item (1) in Definition \ref{dfn:10}) take a nonzero 
projective module $P$, and 
let $F := \opn{Hom}_A(P \oplus P[1], -)$. 
Then $F$ has cohomological 
displacement $[0, 1]$. 
For the contravariant case (item (2)) take a nonzero 
injective module $I$, and let 
$F := \lb \opn{Hom}_A(-, I \oplus I[1])$. 
Then $F$ has cohomological displacement $[-1, 0]$. 
In both cases the cohomological dimension of $F$ is $1$. 
\end{exa}

\begin{rem}
Suppose $A$ and $B$ are rings. If $\cat{E} = \cat{D}^+(A)$ and 
$F = \mrm{R} F_0$ (or $\cat{E} = \cat{D}^-(A)$ and $F = \mrm{L} F_0$) for some 
additive functor $F_0 : \cat{Mod} A \to \cat{Mod} B$, then the cohomological 
dimension of $F$ is the usual cohomological dimension of $F_0$. 

Assume that $\cat{E} = \cat{D}(A)$ and $F$ is a triangulated 
functor. The functor $F$ has bounded below (resp.\ above) cohomological 
displacement iff it is way-out right (resp.\ left), in the sense of 
\cite[Section I.7]{RD}.
\end{rem}

\begin{dfn} \label{dfn:11}
Let $A$ be a DG ring, let $M \in \cat{D}(A)$, and let $[d_0, d_1]$ be an integer
interval of length $d := d_1 - d_0$.
\begin{enumerate}
\item Given a full subcategory $\cat{E} \subseteq \cat{D}(A)$, 
we say that $M$ has {\em projective concentration $[d_0, d_1]$
and projective dimension $d$ relative to $\cat{E}$} if the functor
\[ \opn{RHom}_A(M, -) : \cat{E} \to \cat{D}(\Z) \]
has cohomological displacement $-[d_0, d_1]$ relative to $\cat{E}$.

\item Given a full subcategory $\cat{E} \subseteq \cat{D}(A)$, 
we say that $M$ has {\em injective concentration $[d_0, d_1]$ and 
injective dimension $d$ relative to $\cat{E}$} if the functor
\[ \opn{RHom}_A(-, M) : \cat{E}^{\mrm{op}} \to \cat{D}(\Z) \]
has  cohomological displacement $[d_0, d_1]$ relative to $\cat{E}$.

\item Given a full subcategory $\cat{E} \subseteq \cat{D}(A^{\mrm{op}})$, 
we say that $M$ has {\em flat concentration $[d_0, d_1]$  
and flat dimension $d$ relative to $\cat{E}$} if the functor
\[ - \ot^{\mrm{L}}_A M : \cat{E} \to \cat{D}(\Z) \]
has cohomological displacement $[d_0, d_1]$ relative to $\cat{E}$.
\end{enumerate}
\end{dfn}

\begin{exa} \label{exa:390}
Continuing with the setup of Example \ref{exa:391}, the DG module
$P \oplus P[1]$ (resp.\ $I \oplus I[1]$) has projective (resp.\ injective)
concentration $[-1, 0]$ relative to $\cat{D}(A)$. 
\end{exa}

\begin{exa} \label{exa:520}
Let $A$ be a DG ring, and consider the free DG module 
$P := A \in \cat{D}(A)$.
The functor 
\[ F := \opn{RHom}_{A}(P, -) : \cat{D}(A) \to \cat{D}(\Z) \]
is isomorphic to the forgetful functor 
$\opn{rest}_{A / \Z}$, so it has cohomological displacement 
$[0, 0]$ and cohomological dimension $0$ relative to $\cat{D}(A)$. Thus the DG 
module $P$ has projective concentration $[0, 0]$ and projective dimension $0$
relative to $\cat{D}(A)$.
Note however that the cohomology $\opn{H}(P)$ could be unbounded below. 
\end{exa}

The interval of generation of a DG module was introduced in Definition 
\ref{dfn:390}. 

\begin{prop} \label{prop:393}
Let $M \in \cat{D}(A)$. Assume there is an isomorphism 
$P \cong M$ in $\cat{D}(A)$, where $P$ is a K-flat \tup{(}resp.\ 
K-projective\tup{)} DG $A$-module generated in the integer interval 
$[d_0, d_1]$. Then  $M$ has flat \tup{(}resp.\ projective\tup{)} concentration 
at most $[d_0, d_1]$ relative to  $\cat{D}(A^{\mrm{op}})$
\tup{(}resp.\ $\cat{D}(A)$\tup{)}. 
\end{prop}

\begin{proof}
First consider the K-flat case. Take any $N \in \cat{D}(A^{\mrm{op}})$. 
After applying smart truncation, we can assume that 
$\opn{con}(N) = \opn{con}(\opn{H}(N))$.
Now  $N \ot_A^{\mrm{L}} M \cong N \ot_A P$, 
and by Proposition \ref{prop:390} the bounds on 
$N \ot_A P$ are as claimed. 

Next consider the K-projective case. Take any $N \in \cat{D}(A)$. As above, 
we can assume that 
$\opn{con}(N) = \opn{con}(\opn{H}(N))$.
We know that 
$\opn{RHom}_A(M, N) \cong \opn{Hom}_A(P, N)$.
The bounds on the DG module 
$\opn{Hom}_A(P, N)$ are as claimed, by Proposition \ref{prop:390}. 
\end{proof}

\begin{prop} \label{prop:35}
If $M \in \cat{D}^{[d_0, d_1]}(A)$, then $M$ has projective concentration at 
most  \lb $[-\infty, d_1]$ relative to $\cat{D}(A)$, 
injective concentration at most $[d_0, \infty]$  relative to $\cat{D}(A)$, 
and flat concentration at most  $[-\infty, d_1]$ relative to 
$\cat{D}(A^{\mrm{op}})$.
\end{prop}

\begin{proof}
First let's assume that  $M \neq 0$ and $d_1 < \infty$.
We know that $M$ admits a semi-free resolution $P \to M$ with 
$\opn{sup}(P) = \opn{sup}(\opn{H}(M)) \leq d_1$. 
Now we can use Proposition \ref{prop:393} for the flat and projective 
concentrations.

Now let's assume that $M \neq 0$ and $d_0 > -\infty$.
By Proposition \ref{prop:101} there is a K-injective 
resolution $M \to I$ with 
$\opn{inf}(I) = \opn{inf}(\opn{H}(M)) \geq d_0$. For any 
$N \in \cat{D}(A)$ we have 
$\opn{RHom}_A(N, M) \cong \opn{Hom}_A(N, I)$, and hence the bound on the 
injective concentration. 
\end{proof}

\begin{rem} \label{rem:50}
Let us write <att> for either of the attributes projective, 
injective or flat.
When $A$ is a ring,
$\cat{E} = \cat{D}^{0}(A) \approx \cat{Mod} A$
and $M \in \cat{Mod} A$,
we recover the usual definition of <att> dimension of modules in ring theory.
Furthermore, in the ring case, a DG $A$-module $M$ has <att> concentration in a 
bounded integer interval $[d_0, d_1]$ relative to $\cat{D}^{0}(A)$, iff $M$
isomorphic in $\cat{D}(A)$ to a complex $P$ of <att> $A$-modules with 
$\opn{con}(P) \subseteq [d_0, d_1]$. 
This implies that $M$ has finite <att> dimension relative to $\cat{D}(A)$. 
We do not know if this -- namely the <att> dimension of $M$ relative to 
$\cat{D}(A)$ is the same as that relative $\cat{D}^{0}(A)$ -- is true when $A$ 
is a genuine DG ring. 
\end{rem}

The next two theorems are variations of the opposite (in the categorical sense) 
of \cite[Proposition I.7.1]{RD}, the ``Lemma on Way-Out Functors''.
The canonical homomorphism $A \to \bar{A}$ lets us 
view any $\bar{A}$-module as a DG $A$-module.

\begin{thm} \label{thm:70}
Let $A$ and $B$ be DG rings, let 
$F, G : \cat{D}(A) \to \cat{D}(B)$ 
be triangulated functors, and let $\eta : F \to G$ be a morphism of 
triangulated functors. Assume that $\eta_M : F(M) \to G(M)$ is an 
isomorphism for every $M \in \cat{Mod} \bar{A}$. 
\begin{enumerate}
\item The morphism $\eta_M$ is an isomorphism for every 
$M \in \cat{D}^{\mrm{b}}(A)$.

\item If $F$ and $G$ have bounded above cohomological displacements, then 
$\eta_M$ is an isomorphism for every $M \in \cat{D}^{-}(A)$.

\item If $F$ and $G$ have finite cohomological dimensions, then 
$\eta_M$ is an isomorphism for every $M \in \cat{D}(A)$.
\end{enumerate}
\end{thm}

\begin{proof}
(1) The proof is by induction on $j := \opn{amp}(\opn{H}(M))$. 
If $j = 0$ then $M$ is isomorphic to a shift an object of $\bar{A}$, so 
$\eta_M$ is an isomorphism. If $j > 0$, then using smart truncation 
we obtain a distinguished triangle
$M' \to M \to M'' \xar{\vartriangle}$ in $\cat{D}(A)$ such that  
$\opn{amp}(\opn{H}(M'')) < j$ and $\opn{amp}(\opn{H}(M')) < j$. 
Since $\eta_{M''}$ and $\eta_{M'}$ are isomorphisms, so is 
$\eta_{M}$.

\medskip \noindent
(2) Here we assume that $F$ and $G$ have cohomological displacements at 
most \lb $[-\infty, d_1]$ for some integer $d_1$. 
Take any $M \in \cat{D}^{-}(A)$. 
In order to prove that $\eta_M$ is an isomorphism it suffices to show that 
\[ \opn{H}^i(\eta_M) : \opn{H}^i(F(M)) \to \opn{H}^i(G(M)) \]
is bijective for every $i \in \Z$. 

Fix an integer $i$. Let $M' \to M \to M'' \xar{\vartriangle}$ be a 
distinguished triangle such that 
$\opn{sup}(\opn{H}(M')) \leq i - d_1 - 2$
and 
$\opn{inf}(\opn{H}(M'')) \geq i - d_1 - 1$. This can be obtained using smart 
truncation.

The  cohomologies of $F(M')$ and $G(M')$ are concentrated in the degree range 
$\leq i - 2$. The distinguished triangle induces a commutative 
diagram of $\bar{A}$-modules with exact rows:
\[ \UseTips \xymatrix @C=5ex @R=5ex {
\opn{H}^{i}(F(M'))
\ar[r]
\ar[d]_{ \opn{H}^{i}(\eta_{M'}) }
&
\opn{H}^{i}(F(M))
\ar[r]
\ar[d]_{ \opn{H}^{i}(\eta_{M}) }
&
\opn{H}^{i}(F(M''))
\ar[r]
\ar[d]_{ \opn{H}^{i}(\eta_{M''}) }
&
\opn{H}^{i+1}(F(M'))
\ar[d]_{ \opn{H}^{i+1}(\eta_{M'}) }
\\
\opn{H}^{i}(G(M'))
\ar[r]
&
\opn{H}^{i}(G(M))
\ar[r]
&
\opn{H}^{i}(G(M''))
\ar[r]
&
\opn{H}^{i+1}(G(M')) \ .
} \]
The four terms involving $M'$ are zero. Since $M''$ has bounded cohomology, we 
know by part (1) that $\opn{H}^{i}(\eta_{M''})$ is an isomorphism. Therefore 
$\opn{H}^{i}(\eta_{M})$ is an isomorphism.

\medskip \noindent
(3) Here we assume that $F$ and $G$ have finite cohomological dimensions. 
So $F$ and $G$ have cohomological displacements at most $[d_0, d_1]$ for some 
$d_0 \leq d_1$ in $\Z$.
Take any $M \in \cat{D}(A)$, and fix $i \in \Z$. We want to show that 
$\opn{H}^i(\eta_M)$ is an isomorphism. 
Using smart truncations of $M$ we obtain a distinguished triangle
$M' \to M \to M'' \xar{\vartriangle}$ in $\cat{D}(A)$, such that
$\opn{sup}(\opn{H}(M')) \leq i - d_0 + 1$
and 
$\opn{inf}(\opn{H}(M'')) \geq i - d_0 + 2$.
The cohomologies of $F(M'')$ and $G(M'')$ are concentrated in degrees 
$\geq i + 2$. 
We have a commutative diagram of $\bar{A}$-modules with exact rows:
\[ \UseTips \xymatrix @C=5ex @R=5ex {
\opn{H}^{i-1}(F(M''))
\ar[r]
\ar[d]_{ \opn{H}^{i-1}(\eta_{M''}) }
&
\opn{H}^{i}(F(M'))
\ar[r]
\ar[d]_{ \opn{H}^{i}(\eta_{M'}) }
&
\opn{H}^{i}(F(M))
\ar[r]
\ar[d]_{ \opn{H}^{i}(\eta_{M}) }
&
\opn{H}^{i}(F(M''))
\ar[d]_{ \opn{H}^{i}(\eta_{M''}) }
\\
\opn{H}^{i-1}(G(M''))
\ar[r]
&
\opn{H}^{i}(G(M'))
\ar[r]
&
\opn{H}^{i}(G(M))
\ar[r]
&
\opn{H}^{i}(G(M''))
} \]
The four terms involving $M''$ are zero here. Since $M'$ has bounded above
cohomology, we know by part (2) that $\opn{H}^{i}(\eta_{M'})$ is an 
isomorphism. Therefore 
$\opn{H}^{i}(\eta_{M})$ is an isomorphism.
\end{proof}

\begin{thm} \label{thm:10}
Let $A$ and $B$ be DG rings, let 
$F, G : \cat{D}(A) \to \cat{D}(B)$ 
be triangulated functors, and let $\eta : F \to G$ be a morphism of 
triangulated functors. 
Assume that $A$ is cohomologically left pseudo-noetherian,
and $\eta_A : F(A) \to G(A)$ is an isomorphism.
\begin{enumerate}
\item If $F$ and $G$ have bounded above cohomological displacements, then 
$\eta_M : F(M) \to G(M)$ is an isomorphism for every 
$M \in \cat{D}^{-}_{\mrm{f}}(A)$.

\item If $F$ and $G$ have finite cohomological dimensions, then 
$\eta_M : F(M) \to G(M)$ is an isomorphism for every 
$M \in \cat{D}_{\mrm{f}}(A)$.
\end{enumerate}
\end{thm}

\begin{proof}
Step 1. Consider a finite free DG $A$-module $P$, i.e.\ 
$P \cong \bigoplus_{k = 1}^r A[-i_k]$ in $\cat{C}(A)$ for some 
$i_1, \ldots, i_r \in \Z$. 
Because the functors $F, G$ are triangulated, and $\eta_A$ is an isomorphism, 
it follows that $\eta_P$ is an isomorphism.

\medskip \noindent
Step 2. Now let $P$ be a finite semi-free DG $A$-module,
with finite semi-free filtration $\{ \nu_j(P) \}$ of length $j_1$
(see Definition \ref{dfn:100}). 
We prove that $\eta_{P}$ is an isomorphism by induction on $j_1$.
For $j_1 = 0$ this is step 1. Now assume $j_1 \geq 1$. 
Write $P' := \nu_{j_1 - 1}(P)$ and $P'' := \opn{gr}^\nu_{j_1}(P)$, so there is 
a distinguished triangle
$P' \to P \to P'' \xar{\vartriangle}$ in $\cat{D}(A)$. 
According to step 1 and the induction hypothesis, the morphisms 
$\eta_{P''}$ and $\eta_{P'}$ are isomorphisms. 
Hence $\eta_P$ is an isomorphism.

\medskip \noindent
Step 3. Here we assume that $F$ and $G$ have cohomological displacements at 
most $[-\infty, d_1]$ for some integer $d_1$. 
Take any $M \in \cat{D}^{-}_{\mrm{f}}(A)$. 
In order to prove that $\eta_M$ is an isomorphism it suffices to show that 
\[ \opn{H}^i(\eta_M) : \opn{H}^i(F(M)) \to \opn{H}^i(G(M)) \]
is bijective for every $i \in \Z$.  

We may assume that $M$ is nonzero. 
Let $i_1 := \opn{sup}(\opn{H}(M))$, which is an integer. 
There exists a pseudo-finite semi-free resolution $P \to M$ 
such that $\opn{sup}(P) = i_1$; see Proposition \ref{prop:101}.
We will prove that $\opn{H}^i(\eta_P)$ is an isomorphism for every $i$. 
Fix a pseudo-finite semi-free filtration $\{ \nu_j(P) \}$ of $P$. 

Take an integer $j$, and define $P' := \nu_{j}(P)$ and 
$P'' := P / \nu_{j}(P)$. So there is a  distinguished triangle
$P' \to P \to P'' \xar{\vartriangle}$
in $\cat{D}(A)$. The DG module $P''$ is concentrated in the degree range 
$\leq i_1 - j - 1$, and hence so is its cohomology.
Thus the  cohomologies of $F(P'')$ and $G(P'')$ are concentrated in the 
degree range $\leq i_1 - j - 1 + d_1$, or in other words 
$\opn{H}^i(F(P'')) = \opn{H}^i(G(P'')) = 0$ for all 
$i > i_1 - j - 1 + d_1$. 
On the other hand the DG module $P'$ is finite semi-free. 
The distinguished triangle above induces a commutative 
diagram of $\bar{A}$-modules with exact rows:
\begin{equation} \label{eqn:37}
\UseTips \xymatrix @C=5ex @R=5ex {
\opn{H}^{i-1}(F(P''))
\ar[r]
\ar[d]_{ \opn{H}^{i-1}(\eta_{P''}) }
&
\opn{H}^{i}(F(P'))
\ar[r]
\ar[d]_{ \opn{H}^{i}(\eta_{P'}) }
&
\opn{H}^{i}(F(P))
\ar[r]
\ar[d]_{ \opn{H}^{i}(\eta_{P}) }
&
\opn{H}^{i}(F(P''))
\ar[d]_{ \opn{H}^{i}(\eta_{P''}) }
\\
\opn{H}^{i-1}(G(P''))
\ar[r]
&
\opn{H}^{i}(G(P'))
\ar[r]
&
\opn{H}^{i}(G(P))
\ar[r]
&
\opn{H}^{i}(G(P''))
}
\end{equation}
For any $i > i_1 + d_1 - j$ the modules in this diagram involving $P''$ 
are zero. By step 2 we know that $\opn{H}^{i}(\eta_{P'})$ is an 
isomorphism for every $i$. Therefore 
$\opn{H}^{i}(\eta_{P})$ is an isomorphism for every 
$i > i_1 + d_1 - j$. Since $j$ can be made arbitrarily large, we conclude that 
$\opn{H}^{i}(\eta_{P})$ is an isomorphism for every $i$.

\medskip \noindent
Step 4. Here we assume that $F$ and $G$ have finite cohomological dimensions. 
So $F$ and $G$ have cohomological displacements at most $[d_0, d_1]$ for some 
$d_0 \leq d_1$ in $\Z$. 
This step is very similar to the proof of  Theorem \ref{thm:70}(3).

Take any $M \in \cat{D}^{}_{\mrm{f}}(A)$. Fix $i \in \Z$. We want to show that 
$\opn{H}^i(\eta_M)$ is an isomorphism. 
Using smart truncations of $M$, we obtain a distinguished triangle
$M' \to M \to M'' \xar{\vartriangle}$ in $\cat{D}_{\mrm{f}}(A)$, such that
$M' \in \cat{D}^{[-\infty, i - d_0 + 1]}_{\mrm{f}}(A)$ and
$M'' \in \cat{D}^{[i - d_0 + 1, \infty]}_{\mrm{f}}(A)$.
We get a commutative diagram like (\ref{eqn:37}).
The modules $\opn{H}^{i-1}(F(M''))$, $\opn{H}^{i}(F(M''))$, 
$\opn{H}^{i-1}(G(M''))$ and $\opn{H}^{i}(G(M''))$ are zero. 
Since $M' \in \cat{D}^{-}_{\mrm{f}}(A)$, step 3 says that \lb 
$\opn{H}^{i}(\eta_{M'})$ is an isomorphism. Therefore 
$\opn{H}^{i}(\eta_{M})$ is an isomorphism.
\end{proof}

The next theorem is a variant of the opposite of \cite[Proposition I.7.3]{RD}.
For a boundedness condition $\star$, we denote by $- \star$ the opposite 
boundedness condition. Thus if $\cat{D}^{\star}$ denotes either 
$\cat{D}^{}$, $\cat{D}^{+}$, $\cat{D}^{-}$ or $\cat{D}^{\mrm{b}}$, 
then $\cat{D}^{- \star}$ denotes either
$\cat{D}^{}$, $\cat{D}^{-}$, $\cat{D}^{+}$ or $\cat{D}^{\mrm{b}}$ 
respectively.

\begin{thm} \label{thm:30}
Let $A$ and $B$ be DG rings, and let 
$F : \cat{D}(A)^{\mrm{op}} \to \cat{D}(B)$ 
be a triangulated functor.
Assume that $A$ and $B$ are cohomologically left pseudo-noetherian, 
and $F(A) \in \cat{D}^+_{\mrm{f}}(B)$.
\begin{enumerate}
\item If $F$ has bounded below cohomological displacement, then 
$F(M) \in \cat{D}^+_{\mrm{f}}(B)$  for every $M \in \cat{D}^{-}_{\mrm{f}}(A)$.

\item If $F$ has finite cohomological dimension, then  
$F(M) \in \cat{D}^{- \star}_{\mrm{f}}(B)$  for every 
$M \in \cat{D}^{\star}_{\mrm{f}}(A)$.
\end{enumerate}
\end{thm}

\begin{proof}
The proof is very similar to that of Theorem \ref{thm:10}. We just outline the 
necessary changes. 

\medskip \noindent
Steps 1-2. $P$ is a finite semi-free DG $A$-module. By induction on the 
length $j_1$ of a semi-free filtration, we prove that 
$F(P) \in \cat{D}^+_{\mrm{f}}(B)$.
 
\medskip \noindent
Step 3. Here $F$ has cohomological displacement $[d_0, \infty]$ for some 
$d_0 \in \Z$, and $M \in \cat{D}^{-}_{\mrm{f}}(A)$.
Let $P \to M$ be a pseudo-finite semi-free resolution, with 
$\opn{sup}(P) = i_1$.
Take any $j \in \Z$, and consider the distinguished triangle 
$P' \to P \to P'' \xar{\vartriangle}$ where $P' := \nu_{j}(P)$. 
There is an exact sequence of $\bar{B}$-modules 
\begin{equation} \label{eqn:38}
\UseTips \xymatrix @C=5ex @R=5ex {
\opn{H}^{i-1}(F(P''))
\ar[r]
&
\opn{H}^{i}(F(P'))
\ar[r]
&
\opn{H}^{i}(F(P))
\ar[r]
&
\opn{H}^{i}(F(P'')) .
}
\end{equation}
By step 2 we know that 
$\opn{H}^{i}(F(P')) \in \cat{Mod}_{\mrm{f}} \bar{B}$ for every $i$.
If $i \leq d_0 - i_1 + j$ then 
$\opn{H}^{i-1}(F(P'')) = \opn{H}^{i}(F(P'')) = 0$. 
Therefore $\opn{H}^{i}(F(P)) \in \cat{Mod}_{\mrm{f}} \bar{B}$.
But $j$ can be made arbitrarily large. 
This proves that 
$F(M) \in \cat{D}^{}_{\mrm{f}}(B)$.
But on the other hand we know that 
$\opn{H}^{i}(F(M)) = 0$ for all $i < -i_1 + d_0$. 
We conclude that 
$F(M) \in \cat{D}^+_{\mrm{f}}(B)$.

\medskip \noindent
Step 4. Here $F$ has cohomological displacement at 
most $[d_0, d_1]$ for some $d_0 \leq d_1$ in $\Z$,
$M \in \cat{D}^{}_{\mrm{f}}(A)$, and $i \in \Z$. We truncate $M$ to obtain 
a distinguished triangle
$M' \to M \to M'' \xar{\vartriangle}$ in $\cat{D}_{\mrm{f}}(A)$, such that
$M' \in \cat{D}^{[-\infty, j + 1]}_{\mrm{f}}(A)$ and
$M'' \in \cat{D}^{[j + 1, \infty]}_{\mrm{f}}(A)$
for $j := i - d_1 - 3$.
We get an exact sequence like (\ref{eqn:38}).
The modules $\opn{H}^{i - 1}(F(M''))$ and $\opn{H}^{i}(F(M''))$ are zero, and 
$\opn{H}^{i}(F(M')) \in \cat{Mod}_{\mrm{f}} \bar{B}$ by step 3. 
Therefore $\opn{H}^{i}(F(M)) \in \cat{Mod}_{\mrm{f}} \bar{B}$. 
The condition on the boundedness of $\opn{H}(F(M))$ is established like in step 
3.
\end{proof}
