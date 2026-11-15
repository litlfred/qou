---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-006-6-the-deligne-2-groupoid
section_title: "The Deligne 2-Groupoid"
section_number: 6
pages: 21-24
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.963
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:del-2-grpd}

\begin{dfn}
A DG Lie algebra $\g =  \bigoplus_{i \in \Z}\, \g^i$ is
said to be of {\em quantum type} if $\g^i = 0$ for all $i < -1$. 

A DG Lie algebra
$\til{\g} =  \bigoplus_{i \in \Z}\, \til{\g}^i$ is said to be of
{\em quasi quantum type} if there exists
a quantum type DG Lie algebra $\g$, and a DG Lie algebra quasi-isomorphism 
$\til{\g} \to \g$.
\end{dfn}

\begin{exa} \label{exa:102}
Let $C$ be a commutative $\K$-algebra. The DG Lie algebras 
$\mcal{T}_{\mrm{poly}}(C)$ and $\mcal{D}_{\mrm{poly}}(C)$
that occur in deformation quantization are of quantum type (and hence the
name). 

Let $\g$ be a quantum type DG Lie algebra. Consider the DG Lie algebra 
$\til{\g} := (\opn{L} \circ \opn{C})(\g)$;
this is the bar-cobar construction discussed in Section \ref{sec:L-infty}. 
There is a quasi-isomorphism 
$\zeta_{\g} : \til{\g} \to \g$,
so $\til{\g}$ is of quasi quantum type (but is unbounded in the negative
direction). 
\end{exa}

Suppose $\g$ is a quantum type DG Lie algebra, and $R$ is artinian. Then the 
{\em Deligne $2$-groupoid} of $\m \ot \g$ is defined; see \cite{Ge}. 
In this section we show how this construction can be extended in two ways: 
$\g$ can be of quasi quantum type, and $R$ can be complete (i.e.\ not artinian).

Now let $\g$ be any DG Lie algebra, and $(R, \m)$ any parameter algebra. We have
the set $\opn{MC}(\m \hot \g)$ of MC elements, and the gauge
group $\opn{exp}(\m \hot \g^0)$.

Given $\om \in \opn{MC}(\m \hot \g)$ there is an $R$-bilinear function 
$[-,-]_{\om}$ on $\m \hot \g^{-1}$, whose formula is 
\begin{equation}
[\al_1, \al_2]_{\om} := [ \d_{\om}(\al_1), \al_2 ] , 
\end{equation}
where $\d_{\om} = \d + \opn{ad}(\om)$.

Define  
\begin{equation}
 \a_{\om} := \opn{Coker}(\d_{\om} : \m \hot \g^{-2} \to 
\m \hot \g^{-1}) ,
\end{equation}
so there is an exact sequence of $R$-modules
\begin{equation} \label{eqn:107}
\m \hot \g^{-2} \xar{\d_{\om}} \m \hot \g^{-1} \to \a_{\om} \to 0 .
\end{equation}

\begin{prop} \label{prop:110}
Take any $\om \in \opn{MC}(\m \hot \g)$.
\begin{enumerate}
\item Let $\al \in \m \hot \g^{-1}$ and 
$\be \in \m \hot \g^{-2}$.
Write $\al' := \d_{\om}(\be) \in \m \hot \g^{-1}$.
Then 
\[ [\al, \al']_{\om} , \ [\al', \al]_{\om} \in \d_{\om}(\m \ot \g^{-2}) . \]

\item The induced $R$-bilinear function $[-,-]_{\om}$ on $\a_{\om}$ is a Lie
bracket. Thus $\a_{\om}$ is a Lie algebra.

\item Let $g \in \opn{exp}(\m \hot \g^0)$, and let 
$\om' := \opn{Af}(g)(\om) \in \opn{MC}(\m \hot \g)$. Then 
\[ \opn{Ad}(g) : \a_{\om} \to \a_{\om'} \]
is an isomorphism of Lie algebras.
\end{enumerate}
\end{prop}

\begin{proof}
(1) and (2) are easy direct calculations. (3) is a consequence of Proposition
\ref{prop:100}.
\end{proof}

\begin{prop} \label{prop:103}
Assume either of these two conditions holds\tup{:}
\begin{itemize}
\rmitem{i} $R$ is artinian.  
\rmitem{ii} $\g$ is of quasi quantum type.
\end{itemize}
Then for any $\om \in \opn{MC}(\m \hot \g)$ the 
$R$-module $\a_{\om}$ is $\m$-adically complete. Hence 
$\a_{\om}$ is a pronilpotent Lie algebra.
\end{prop}

\begin{proof}
If $R$ is artinian then any $R$-module is $\m$-adically complete.

Now assume $R$ is not artinian (namely it is a complete noetherian ring). 
If $\g$ is of quantum type then 
$\a_{\om} = \m \hot \g^{-1}$, which is $\m$-adically complete (cf.\ 
\cite[Corollary 3.5]{Ye5}). 

For any DG Lie algebra $\g$ the canonical homomorphism 
\begin{equation} \label{eqn:108}
\tau_{\om} : \a_{\om} \to \what{\a_{\om}} = 
\lim_{\leftarrow i}\, (R_i \ot_R \a_{\om})
\end{equation}
is surjective. Here is the reason: the completion functor $M \mapsto \what{M}$
is not exact (neither right nor left exact), but it does preserve surjections
(see \cite[Proposition 1.2]{Ye5}). Combining this with the
exact sequence (\ref{eqn:107}), and the fact that $\m \hot \g^{-1}$ is
complete, it follows that the homomorphism $\tau_{\om}$ is surjective.

It remains to prove that if there exists a DG Lie algebra quasi-isomorphism
$\phi : \g \to \h$, for some quantum type DG Lie algebra $\h$, then the
homomorphism $\tau_{\om}$ is injective. Since 
$\d_{\om} : \a_{\om} \to \m \hot \g^{0}$ factors through 
$\what{\a_{\om}}$, it follows that 
\[ \opn{Ker}(\tau_{\om}) \subset 
\opn{Ker}(\d_{\om} : \a_{\om} \to \m \hot \g^{0}) = 
\mrm{H}^{-1}(\m \hot \g)_{\om} . \]
Let $\chi := \phi(\om)$. We have a commutative diagram with exact rows 
\[ \UseTips \xymatrix @C=5ex @R=5ex {
0
\ar[r]
&
\mrm{H}^{-1}(\m \hot \g)_{\om}
\ar[r]
\ar[d]_{\mrm{H}^{-1}(\bsym{1} \hot \phi)}
&
\a_{\om}
\ar[r]^(0.35){\d_{\om}}
\ar[d]
&
(\m \hot \g^0)_{\om}
\ar[d]
\\
0
\ar[r]
&
\mrm{H}^{-1}(\m \hot \h)_{\chi}
\ar[r]
&
\a_{\chi}
\ar[r]^(0.35){\d_{\chi}}
&
(\m \hot \h^0)_{\chi} \ .
} \]
Because $\phi$ is a quasi-isomorphism, so is 
\[ \bsym{1} \hot \phi : (\m \hot \g)_{\om} \to 
(\m \hot \h)_{\chi} \]
(we are using Lemma \ref{lem:6}(1)).
Hence the vertical arrow $\mrm{H}^{-1}(\bsym{1} \hot \phi)$ in the diagram is an
isomorphism of $R$-modules. It sends $\opn{Ker}(\tau_{\om})$ bijectively to 
$\opn{Ker}(\tau_{\chi} : \a_{\chi} \to \what{\a_{\chi}})$.
We know that $\a_{\chi}$ is complete, so  $\opn{Ker}(\tau_{\chi}) = 0$.
\end{proof}

\begin{cor} \label{cor:101}
In the situation of Proposition \tup{\ref{prop:103}}, for every 
$\om \in \opn{MC}(\m \hot \g)$
there is a pronilpotent group 
$N_{\om} := \opn{exp}(\a_{\om})$, and a group homomorphism 
\[ \opn{D}_{\om} :=  \opn{exp}(\d_{\om}) : N_{\om} \to 
\opn{exp}(\m \hot \g^0)(\om)  . \]

Given any $g \in \opn{exp}(\m \hot \g^0)$
and $\om \in \opn{MC}(\m \hot \g)$, let 
$\om' := \opn{Af}(g)(\om) \in$ \lb $\opn{MC}(\m \hot \g)$. Then there is a
group isomorphism
\[ \Psi(g) := \opn{exp}(\opn{Ad}(g)) : N_{\om} \iso N_{\om'} , \]
and the diagram 
\[ \UseTips \xymatrix @C=5ex @R=5ex {
N_{\om}
\ar[d]_{\Psi(g)}
\ar[r]^(0.34){\opn{D}_{\om}}
&
\opn{exp}(\m \hot \g^0)(\om)
\ar[d]^{\opn{Ad}(g)}
\\
N_{\om'}
\ar[r]^(0.34){\opn{D}_{\om'}}
&
\opn{exp}(\m \hot \g^0)(\om')
} \]
is commutative.
The isomorphisms $\Psi(g)$ are an action of the group 
$\opn{exp}(\m \hot \g^0)$ on the collection of groups 
$\{ N_{\om} \}_{\om \in \opn{MC}(\m \hot \g)}$.

Moreover, for any $a, a' \in N_{\om}$ we have 
\[ \Psi( \opn{D}_{\om}(a))(a') = 
\opn{Ad}_{N_{\om}}(a)(a') . \]
\end{cor}

\begin{proof}
Combine Propositions \ref{prop:100}, \ref{prop:110} and \ref{prop:103}.
\end{proof}

\begin{rem}
The Lie algebra $\a_{\om}^{\mrm{r}}$ and the group $N_{\om}^{\mrm{r}}$ that
occur in Section 
\ref{sec:red-del} are quotients, respectively, of the Lie algebra $\a_{\om}$ and
the group $N_{\om}$ that occur here. 
\end{rem}

\begin{dfn} \label{dfn:103}
Let $\g$ be a DG Lie algebra and $R$ a parameter algebra. 
Assume either of these two conditions holds:
\begin{itemize}
\rmitem{i} $R$ is artinian.  
\rmitem{ii} $\g$ is of quasi quantum type.
\end{itemize} 
The {\em Deligne $2$-groupoid} $\mbf{Del}^2(\g, R)$
is the transformation $2$-groupoid (see Example \ref{exa:100} and Proposition 
\ref{prop:102}) associated to the action of the group 
$\opn{exp}(\m \hot \g^0)$
on the collection of groups 
$\{ N_{\om} \}_{\om \in \opn{MC}(\m \hot \g)}$.
The feedback $\opn{D}_{\om}$ and the twisting $\Psi(g)$ are specified in
Corollary \ref{cor:101}.
\end{dfn}

\begin{prop}
Consider pairs $(\g, R)$ such that Deligne $2$-groupoid $\mbf{Del}^2(\g, R)$
is defined, i.e.\ either of the two conditions in Definition \tup{\ref{dfn:103}}
holds. 
\begin{enumerate}
\item The Deligne $2$-groupoid $\mbf{Del}^2(\g, R)$ depends functorially on 
$\g$ and $R$. 

\item The reduced Deligne groupoid satisfies
\[ \mbf{Del}^{\mrm{r}}(\g, R) = \pi_1(\mbf{Del}^2(\g, R)) . \]
\end{enumerate}
\end{prop}

\begin{proof}
This is immediate from the constructions.
\end{proof}

\begin{thm} \label{thm:105}
Let $R$ be a parameter algebra, let $\g$ and $\h$ be
DG Lie algebras, and let $\phi : \g \to \h$ be a DG Lie algebra
quasi-isomorphism. Assume either of these two conditions holds:
\begin{itemize}
\rmitem{i} $R$ is artinian.  
\rmitem{ii} $\g$ and $\h$ are of quasi quantum type.
\end{itemize}  
Then the morphism of $2$-groupoids
\[ \mbf{Del}^2(\phi, R) : \mbf{Del}^2(\g, R) \to \mbf{Del}^2(\h, R) \]
is a weak equivalence.
\end{thm}

\begin{proof}
Since 
\[ \pi_0(\mbf{Del}^2(\phi, R)) = \pi_0(\mbf{Del}^{\mrm{r}}(\phi, R)) \]
and 
\[ \pi_1(\mbf{Del}^2(\phi, R), \om) = 
\pi_1(\mbf{Del}^{\mrm{r}}(\phi, R), \om) \]
for all $\om \in \opn{MC}(\m \hot \g)$,
these are bijections by Theorem \ref{thm:2}.

Next, there is a functorial bijection 
\begin{equation} \label{eqn:110}
\begin{aligned}
\exp & : \mrm{H}^{-1}(\m \hot \g)_{\om} \iso 
\\
& \qquad 
\opn{Ker} \bigl( \opn{D}_{\om} : N_{\om} \to \opn{exp}(\m \hot \g^0) \bigr) =
\pi_2(\mbf{Del}^2(\g, R), \om) ;
\end{aligned}
\end{equation}
cf.\ the commutative diagram in the proof of Proposition \ref{prop:103}. 
So 
\[ \pi_2(\mbf{Del}^2(\phi, R), \om) = 
\mrm{H}^{-1}(\bsym{1}_{\m} \hot \phi) \]
is bijective. 
\end{proof}

\begin{rem}
It is possible to define a Deligne $2$-groupoid $\mbf{Del}^2(\g, R)$ even when
both conditions in Definition \ref{dfn:103} fail, by taking 
$N_{\om} := \exp(\what{\a_{\om}})$. 
However the function $\exp$ in (\ref{eqn:110}) might fail to be bijective.
Hence, in the situation of Theorem \ref{thm:105}, the homomorphism 
$\pi_2(\mbf{Del}^2(\phi, R), \om)$ might fail to be bijective.
\end{rem}
