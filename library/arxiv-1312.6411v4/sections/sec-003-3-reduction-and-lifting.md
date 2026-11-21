---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-003-3-reduction-and-lifting
section_title: "Reduction and Lifting"
section_number: 3
pages: 16-19
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.989
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:lifting}

Recall that by default all DG modules are left DG modules, and all DG rings are 
nonpositive (Convention \ref{conv:305}).   
In this section we study the canonical DG ring homomorphism 
$A \to \bar{A}$, and the corresponding reduction functor 
$\cat{D}(A) \to \cat{D}(\bar{A})$, 
$M \mapsto \bar{A} \ot^{\mrm{L}}_{A} M$.
We do not make any finiteness assumptions on the cohomology modules 
$\opn{H}^i(M)$.

A triangulated functor $F$ is called {\em conservative} if for any object 
$M$, $F(M) = 0$ implies $M = 0$; or equivalently, if for any morphism 
$\phi$, $F(\phi)$ is an isomorphism implies $\phi$ is an isomorphism.
Cf.\ \cite[Section 1.4]{KaSc}. The following result is analogous to the 
Nakayama Lemma (cf.\ Remark \ref{rem:317}).

\begin{prop} \label{prop:92}
Let $A$ be a DG ring. The reduction functor 
\[ \bar{A} \ot^{\mrm{L}}_{A} - : \cat{D}^{-}(A) \to \cat{D}^-(\bar{A}) \]
is conservative. 
\end{prop}

\begin{proof}
Take $M \in \cat{D}^{-}(A)$ not isomorphic to $0$, and let 
$i_1 := \opn{sup}(\opn{H}(M))$.
We can find a K-flat resolution (e.g.\ a semi-free resolution) $P \to M$ over 
$A$ such that $\opn{sup}(P) = i_1$.
Then $\bar{A} \ot^{\mrm{L}}_A M \cong \bar{A} \ot^{}_A P$, and  
(by the ``K\"unneth trick'')
\[ \opn{H}^{i_1}(\bar{A} \ot^{\mrm{L}}_A M) \cong 
\opn{H}^{i_1}(\bar{A} \ot^{}_A P) \cong 
\bar{A} \ot^{}_A \opn{H}^{i_1}(P) \cong \opn{H}^{i_1}(M) \]
is nonzero. Hence $\bar{A} \ot^{\mrm{L}}_A M$ is nonzero. 
\end{proof}

Given a homomorphism $\phi : P \to Q$ in $\cat{C}(A)$, we denote by 
$\opn{cone}(\phi)$ the corresponding cone, which is also an object of 
$\cat{C}(A)$. 

\begin{lem} \label{lem:33}
Suppose $\phi : P \to Q$ is a homomorphism in $\cat{C}(A)$,
where $P$ and $Q$ are pseudo-finite \tup{(}resp.\ finite\tup{)} semi-free DG 
modules. Then $\opn{cone}(\phi)$ is a pseudo-finite \tup{(}resp.\ finite\tup{)} 
semi-free DG module. 
\end{lem}

\begin{proof}
Clear from Proposition \ref{prop:100}.
\end{proof}

\begin{prop} \label{prop:305}  
Let $M \in \cat{D}^-(A)$. We write
$\bar{M} := \bar{A} \ot^{\mrm{L}}_A M \in \cat{D}^-(\bar{A})$. 
\begin{enumerate}
\item If $\bar{M}$ is isomorphic in $\cat{D}(\bar{A})$ to 
$\bar{A}^{\oplus r}$ for some cardinal number $r$, then 
$M$ is isomorphic in $\cat{D}(A)$ to $A^{\oplus r}$.

\item If $\bar{M}$ is isomorphic in $\cat{D}(\bar{A})$ to a semi-free DG 
$\bar{A}$-module $\bar{P}$ of semi-free length $d$, then $M$ is 
isomorphic in $\cat{D}(A)$ to a semi-free DG $A$-module $P$ of semi-free 
length $d$.
\end{enumerate}
\end{prop}

Observe that the DG $\bar{A}$-module $\bar{P}$ in (2) above is nothing but a
bounded complex of free $\bar{A}$-modules; cf.\ Proposition \ref{prop:100}.
The semi-free length was introduced in Definition \ref{dfn:311}.

\begin{proof}
Step 1. 
In view of Proposition \ref{prop:92} we can assume that $\bar{A}$ and $M$ are 
nonzero. Define $i_1 := \opn{sup}(\opn{H}(M))$. 
By replacing $M$ with a suitable resolution of it, we can assume that $M$ is a 
K-flat DG $A$-module satisfying $\opn{sup}(M) =  i_1$.
After that we can also assume that $\bar{M} = \bar{A} \ot_A M$. 
The K\"unneth formula says that
\[ \opn{H}^{i_1}(\bar{M}) \cong 
\opn{H}^{i_1}(\bar{A} \ot_{A} M) \cong \bar{A} \ot_{A} \opn{H}^{i_1}(M)
\cong \opn{H}^{i_1}(M) \]
as $\bar{A}$-modules. Therefore  
$\opn{sup}(\opn{H}(\bar{M})) = \opn{sup}(\bar{M}) = i_1$.

We are given an isomorphism $\bar{\phi} : \bar{P} \to \bar{M}$ in 
$\cat{D}(\bar{A}^0)$, where $\bar{P}$ is a bounded complex of free 
$\bar{A}$-modules. 
Since $\bar{P}$ is K-projective, we can assume that the isomorphism 
$\bar{\phi} : \bar{P} \to \bar{M}$ in $\cat{D}(\bar{A})$
is in fact a quasi-isomorphism in $\cat{C}(\bar{A})$.
The proof continues by induction on $j := \opn{amp}(\bar{P}) \in \N$.
Note that in item (1) we have $i_1 = 0$, $\bar{P} = \bar{A}^{\oplus r}$ and 
$j = 0$. 

\medskip \noindent
Step 2. In this step we assume that $j = 0$. This means that the 
only nonzero term of $\bar{P}$ is
in degree $i_1$, and it is 
the free module $\bar{P}^{i_1} \cong \bar{A}^{\oplus r_1}$
for some cardinal number $r_1$. In other words, 
$\bar{P} \cong \bar{A}[-i_1]^{\oplus r_1}$ in $\cat{C}(\bar{A})$.
So $\opn{H}^{i_1}(\bar{M}) \cong \bar{P}^{i_1}$, and 
$\opn{H}^{i}(\bar{M}) = 0$ for all $i \neq i_1$.
Recall the isomorphism of $\bar{A}$-modules
$\opn{H}^{i_1}(\bar{M}) \cong \opn{H}^{i_1}(M)$ from Step 1.  
There are canonical surjections 
$M^{i_1} \to \opn{H}^{i_1}(M)$ and
$\bar{M}^{i_1} \to \opn{H}^{i_1}(\bar{M})$.
We can write the quasi-isomorphism $\bar{\phi}$ as 
$\bar{\phi} : \bar{A}[-i_1]^{\oplus r_1} \to \bar{M}$.
 
Consider the nonderived reduction functor
$F : \cat{C}(A) \to \cat{C}(\bar{A})$, $F(-) := \bar{A} \ot_{A} -$.
Let $P := A[-i_1]^{\oplus r_1}$, a free DG $A$-module
satisfying $F(P) \cong \bar{P}$.  
There exists a homomorphism 
$\phi : P \to M$ in $\cat{C}(A)$ that lifts 
the quasi-isomorphism
$\bar{\phi} : \bar{P} \to \bar{M}$,
namely $\bar{\phi} = F(\phi)$. 
Now the DG modules $P$ and $M$ are K-flat, so 
$\bar{\phi} = \mrm{L} F(\phi)$. 
Since $\bar{\phi}$ is an isomorphism, and since the functor 
$\mrm{L} F$ is conservative, we conclude that $\phi$ is an isomorphism.
This proves item (1).

\medskip \noindent
Step 3. Here we suppose that $j \geq 1$.
Let $i_2 := \opn{sup} (\bar{P})$, which is of course $\geq i_1$. 
Say $\bar{P}^{i_2} \cong \bar{A}^{\oplus r_2}$ for some natural number $r_2$.
Define DG modules $\bar{P}' := \bar{A}[-i_2]^{\oplus r_2}$ and 
$P' := A[-i_2]^{\oplus r_2}$; these satisfy
$\bar{P}' \cong \bar{A} \ot_A P'$. 
The inclusion $\bar{P}^{i_2} \subseteq \bar{P}$ is viewed as a DG module 
homomorphism $\bar{\al} : \bar{P}' \to \bar{P}$.
We also have a quasi-isomorphism 
$\bar{\phi} : \bar{P} \to \bar{M}$ and an equality 
$\bar{M} = \bar{A} \ot_A M$ in $\cat{C}(\bar{A})$.
In this way we obtain a homomorphism 
$\bar{\psi} :  \bar{P}' \to \bar{M}$,
$\bar{\psi} := \bar{\phi} \circ \bar{\al}$. 
Because $P'$ is a free DG $A$-module, there is a homomorphism 
$\psi :  P' \to M$ in $\cat{C}(A)$ lifting $\bar{\psi}$, namely 
$\bar{\psi} = F(\psi)$, where $F$ is the functor $\bar{A} \ot_A -$. 

Let $M'' \in \cat{C}(A)$ be the cone of $\psi$, so there is a distinguished 
triangle 
\begin{equation} \label{eqn:30}
P' \xar{\psi} M \xar{\chi} M'' \xar{} P'[1] 
\end{equation}
in $\cat{D}(A)$. Define $\bar{M}'' := F(M'')$ and $\bar{\chi} := F(\chi)$,  
which are an object and a morphism in $\cat{C}(\bar{A})$, respectively.  
Since all three DG modules in this triangle are K-flat, it follows that 
\[ \bar{P}' \xar{\bar{\psi}} \bar{M} \xar{\bar{\chi}} \bar{M}'' 
\xar{} \bar{P}'[1] \]
is a distinguished triangle in $\cat{D}(\bar{A})$.
On the other hand, let $\bar{P}''$ be the cokernel of the inclusion 
$\bar{\al} : \bar{P}' \to \bar{P}$. So there is a distinguished triangle
\[ \bar{P}' \xar{\bar{\al}} \bar{P} \xar{\bar{\be}} \bar{P}'' 
\xar{} \bar{P}'[1] \]
in $\cat{D}(\bar{A})$. 
Consider the diagram of solid arrows in $\cat{D}(\bar{A})$~: 
\[  \UseTips \xymatrix @C=5ex @R=5ex {
\bar{P}'
\ar[r]^{\bar{\al}} 
\ar[d]^{=}
&
\bar{P} 
\ar[r]^{\bar{\be}} 
\ar[d]^{\bar{\phi}} 
&
\bar{P}'' 
\ar[r]^{}
\ar@{-->}[d]^{\bar{\phi}''} 
&
\bar{P}'[1]
\ar[d]^{=}
\\
\bar{P}'
\ar[r]^{\bar{\psi}} 
&
\bar{M} 
\ar[r]^{\bar{\chi}} 
&
\bar{M}'' 
\ar[r]^{}
&
\bar{P}'[1]
} \]
The square on the left is commutative, and therefore it extends to an 
isomorphism of distinguished triangles. So there is an isomorphism
$\bar{\phi}'' : \bar{P}'' \to \bar{M}''$
in $\cat{D}(\bar{A})$.

Finally, the complex $\bar{P}''$ is a bounded complex of finite free 
$\bar{A}$-modules, of amplitude $j-1 \geq 0$. According to the induction 
hypothesis (step 2 for $j > 1$, and step 1 for $j = 1$) there is an isomorphism 
$\phi'' : P'' \iso M''$ in $\cat{D}(A)$ for some finite semi-free DG 
$A$-module $P''$. From (\ref{eqn:30}) we obtain a distinguished triangle 
\[ P' \xar{\psi} M \xar{\psi} P'' \xar{\ga} P'[1] \]
in $\cat{D}(A)$. We can assume that $\ga$ is a homomorphism in 
$\cat{C}(A)$. Turning this triangle we get a distinguished triangle 
\[ P''[-1] \xar{- \ga[-1]} P' \xar{\psi} M \xar{\vartriangle} . \]
Define $P$ to be the cone on the homomorphism 
$- \ga[-1] : P''[-1] \to P'$. Then $P \cong M$ in $\cat{D}(A)$,
and by Lemma \ref{lem:33}, $P$ is a finite semi-free DG $A$-module. 
\end{proof}


We learned the next proposition from B. Antieau and J. Lurie. Cf.\ 
\cite[Corollary 7.2.2.19]{Lu1} for a more general statement. 

\begin{prop} \label{prop:310}
Let $\bar{P}$ be a projective $\bar{A}$-module. Then there exists a DG 
$A$-module $P$ with these properties:
\begin{enumerate}
\rmitem{i} $P$ is a direct summand, in $\cat{D}(A)$, of a direct sum of copies 
of $A$.
\rmitem{ii} 
$\bar{A} \ot^{\mrm{L}}_A P \cong \bar{P}$
in $\cat{D}(\bar{A})$.
\end{enumerate} 
\end{prop}

\begin{proof}
Say $\bar{P}$ is a direct summand, in $\cat{Mod} \bar{A}$, of a free 
$\bar{A}$-module $\bar{F}$. So $\bar{P}$ is the image of an idempotent 
endomorphism $\bar{\phi} : \bar{F} \to \bar{F}$. Let $F$ be the direct sum 
in $\cat{C}(A)$ of copies of $A$, as many as there are copies of $\bar{A}$ in 
$\bar{F}$. There is a canonical surjection $F \to \bar{F}$. Choose any 
homomorphism $\phi : F \to F$ in $\cat{C}(A)$ lifting $\bar{\phi}$.
Note that many such $\phi$ exist; and they aren't necessarily idempotents. Let 
$P$ be the homotopy colimit construction on $\phi$. Namely we let
\[ \Phi : \bigoplus\nolimits_{i \in \N} \, F \ \to \ 
\bigoplus\nolimits_{i \in \N} \, F \]
be the homomorphism
\[  \Phi(a_0, a_1, a_2, ...) := (a_0, a_1 - \phi(a_0), a_2 - \phi(a_1), ...) \]
in $\cat{C}(A)$, and then we define 
$P := \opn{cone}(\Phi) \in \cat{C}(A)$. 
Because $P$ is K-flat over $A$, we see that  
$\bar{A} \ot^{\mrm{L}}_A P \cong \bar{A} \ot_A P \cong 
\opn{cone}(\bar{\Phi})$,
where 
\[ \bar{\Phi} : \bigoplus\nolimits_{i \in \N} \, \bar{F} \ \to \ 
\bigoplus\nolimits_{i \in \N} \, \bar{F} \]
is the homotopy colimit construction on $\bar{\phi}$.
An easy calculation, using the fact that $\bar{\phi}$ is an idempotent with 
image $\bar{P}$,  shows that 
$\opn{cone}(\bar{\Phi}) \cong \bar{P}$ in $\cat{D}(\bar{A})$. 
This proves (ii).

As for (i): say $\bar{Q}$ is the other direct summand of $\bar{F}$
in $\cat{Mod} \bar{A}$.
We can lift it to a DG $A$-module $Q$ as above. Now
$\bar{P} \oplus \bar{Q} \cong \bar{F}$
in $\cat{D}(\bar{A})$. By Proposition \ref{prop:305}(1) we deduce that
$P \oplus Q \cong F$ in $\cat{D}(A)$.
\end{proof}
