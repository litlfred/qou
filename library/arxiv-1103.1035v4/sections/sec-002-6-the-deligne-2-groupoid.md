---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI"
section_id: sec-002-6-the-deligne-2-groupoid
section_title: "The Deligne 2-Groupoid"
section_number: 6
pages: 23-31
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
text_source: latex
latex_prose_ratio: 0.862
latex_coverage_ratio: 0.975
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








\section{$\mrm{L}_{\infty}$ Morphisms and Coalgebras}
\label{sec:L-infty}

We shall use the coalgebra approach to $\mrm{L}_{\infty}$ morphisms, following
\cite{Qu}, \cite[Section 4]{Ko2}, \cite{Hi2}, \cite[Section 3.7]{CKTB} and
\cite[Section 3]{Ye2}. 

Let us denote by $\cat{DGLie}(\K)$ the category of DG Lie algebras over $\K$,
and by $\cat{DGCog}(\K)$ the category of DG unital cocommutative coalgebras
over $\K$. Note that commutativity here is in the graded (or super) sense.
Recall that a unital coalgebra $C$ has a comultiplication 
$\Delta : C \to C \ot C$,
a counit $\ep : C \to \K$ and a unit $1 \in C$. The differential $\d$ has to be
a coderivation of degree $1$. The conditions on the unit are
$\Delta(1) = 1 \ot 1$, $\d(1) = 0$ and $\ep(1) = 1$ in $\K$. 
Morphisms in $\cat{DGCog}(\K)$ are $\K$-linear homomorphisms
$C \to D$ respecting
$\Delta$, $\ep$ and $1$. We write $C^+ := \opn{Ker}(\ep)$.

Let $V = \boplus_{i \in \Z} V^i$ be a graded $\K$-module. The 
symmetric algebra over $\K$ of the graded module $V$ is 
\[ \opn{Sym}(V) = \bigoplus_{i \in \N}\, \opn{Sym}^j(V) . \]
Note that we are in the super-commutative setting, so
$\opn{Sym}^j(V) = \bwedge^j(V[1])[-j]$.
We view $\opn{Sym}(V)$ as a Hopf algebra over $\K$, 
which is commutative and cocommutative. The unit is 
$1 \in \K = \opn{Sym}^0(V)$, and the counit is the projection
$\ep : \opn{Sym}(V) \to \K$.

The Hopf algebra $\opn{Sym}(V)$ is bigraded, with one grading coming from the
grading of $V$, which we call degree. The second grading is called order; by
definition the $j$-th order component of $\opn{Sym}(V)$ is $\opn{Sym}^j(V)$.
Let us write
\[ \opn{Sym}^+(V) := \bigoplus_{i \geq 1}\, \opn{Sym}^j(V) =
\opn{Ker}(\ep) . \]

The projection $\opn{Sym}(V) \to \opn{Sym}^1(V)$ is denoted by $\ln$.
So for an element $c \in \opn{Sym}(V)$, its first order term is $\ln(c)$.
Recall that giving a homomorphism of unital graded coalgebras
$\Psi : \opn{Sym}(V) \to \opn{Sym}(W)$ 
is the same as giving its sequence of Taylor coefficients 
$\{ \pa^j\Psi \}_{j \geq 1}$,
where the $j$-th Taylor coefficient of $\Psi$ is the $\K$-linear function 
\[ \partial^j \Psi := (\ln \circ \Psi)|_{\opn{Sym}^j(V)} : 
\opn{Sym}^j(V) \to W  \]
of degree $0$.

The free graded Lie algebra over the graded $\K$-module $V$ is denoted by \lb
$\opn{FrLie}(V)$. 

There is a functor 
\[ \opn{C} : \cat{DGLie}(\K) \to \cat{DGCog}(\K) \]
called the {\em bar construction}. Given a DG Lie algebra $\g$, the
corresponding DG coalgebra is 
$\opn{C}(\g) := \opn{Sym}(\g[1])$, with a coderivation that encodes both the
differential of $\g$ and its Lie bracket. 
There is another functor 
\[ \opn{L} : \cat{DGCog}(\K) \to \cat{DGLie}(\K)   \]
called the {\em cobar construction}. Given a DG coalgebra $C$, the
corresponding DG Lie algebra is $\opn{FrLie}(C^+[-1])$, with a derivation that
encodes both the differential of $C$ and its comultiplication. 
If $\g \in \cat{DGLie}(\K)$ and $C \in \cat{DGCog}(\K)$, then the set of graded
$\K$-linear homomorphisms $\opn{Hom}^{\mrm{gr}}(C, \g)$ 
is a DG Lie algebra, and there are functorial bijections
\begin{equation} \label{eqn:60}
\opn{Hom}_{\cat{DGLie}(\K)}(\opn{L}(C), \g) \cong
\opn{Hom}_{\cat{DGCog}(\K)}(C, \opn{C}(\g)) \cong
\opn{MC}(\opn{Hom}^{\mrm{gr}}(C, \g)) . 
\end{equation}
Thus the functors $\opn{C}$ and $\opn{L}$ are adjoint.
We denote the adjunction morphisms by
\[ \zeta_{\g} : (\opn{L} \circ \opn{C})(\g) \to \g \]
and 
\[ \th_C : C \to (\opn{C} \circ \opn{L})(C) .  \]

It is known that the functor $\opn{C}$ is faithful. 
Let $\g$ and $\h$ be DG Lie algebras.
By definition, an {\em $\mrm{L}_{\infty}$ morphism} $\Phi : \g \to \h$ 
is a morphism $\opn{C}(\g) \to \opn{C}(\h)$ in $\cat{DGCog}(\K)$.
Let us define $\cat{DGLie}_{\infty}(\K)$ to be the category whose objects are
the DG Lie algebras, and the morphisms are the  $\mrm{L}_{\infty}$ morphisms
between them. Composition of  $\mrm{L}_{\infty}$ morphisms is that of
$\cat{DGCog}(\K)$. Thus we get a full and faithful functor
\[ \opn{C}_{\infty} : \cat{DGLie}_{\infty}(\K) \to \cat{DGCog}(\K) \]
whose restriction to $\cat{DGLie}(\K)$ is $\opn{C}$.

Take an $\mrm{L}_{\infty}$ morphism 
$\Phi : \g \to \h$. Its $i$-th Taylor coefficient
$\pa^i \Phi := \pa^i (\opn{C}_{\infty}(\Phi))$ is a $\K$-linear function 
\[ \pa^i \Phi : \bwedge^i \g \to \h \]
of degree $1 - i$. Writing $\phi_i := \pa^i \Phi$, the sequence of 
functions $\{ \phi_i \}_{i \geq 1}$ satisfies these equations:
\[ \begin{aligned}
& \mrm{d} \bigl( \phi_i(\gamma_1 \wedge \cdots 
\wedge \gamma_i) \bigr) - \sum_{k = 1}^i \pm 
\phi_i \bigl( \gamma_1 \wedge \cdots \wedge 
\mrm{d}(\gamma_k) \wedge \cdots \wedge \gamma_i \bigr) = \\
& \quad {\smfrac{1}{2}} \sum_{\substack{k, l \geq 1 \\ k + l = i}}
{\smfrac{1}{k! \, l!}} \sum_{\sigma \in \mfrak{S}_i} \pm
\bigl[ \phi_k (\gamma_{\sigma(1)} \wedge \cdots \wedge 
\gamma_{\sigma(k)}),
\phi_l (\gamma_{\sigma(k + 1)} \wedge \cdots \wedge 
\gamma_{\sigma(i)}) \bigr] \\
& \qquad +
\sum_{k < l} \pm
\phi_{i-1} \bigl( [\gamma_k, \gamma_l] \wedge
\gamma_{1} \wedge \cdots \gamma_k \hspace{-1em} \diagup \cdots
\gamma_l \hspace{-1em} \diagup 
\cdots \wedge \gamma_{i} \bigr) .
\end{aligned} \]
Here $\gamma_k \in \mfrak{g}$ are homogeneous elements,
$\mfrak{S}_i$ is the permutation group of $\{ 1, \ldots, i \}$,
and the signs depend only on the indices, the permutations and the 
degrees of the elements $\gamma_k$. The
signs are written explicitly in \cite[Section 3.6]{CKTB}. 
Conversely, any sequence $\{ \phi_i \}_{i \geq 1}$ of homomorphisms satisfying
these equations determines an $\mrm{L}_{\infty}$ morphism.

Let $\Phi : \g \to \h$ be  an $\mrm{L}_{\infty}$ morphism.
The first Taylor coefficient  $\pa^1 \Phi : \g \to \h$ is a homomorphism of
complexes of $\K$-modules (forgetting the Lie brackets). 
If $\pa^i \Phi = 0$ for all $i \geq 2$, then 
$\pa^1 \Phi$ is a DG Lie algebra homomorphism. 
If $\pa^1 \Phi$ is a quasi-isomorphism, then $\Phi$ is called an 
{\em $\mrm{L}_{\infty}$ quasi-isomorphism}.

\begin{lem} \label{lem:20}
Let $\g \in \cat{DGLie}(\K)$, and define
$C := \opn{C}(\g)$, $\til{\g} := \opn{L}(C)$ and $\til{C} := \opn{C}(\til{g})$.
Consider the coalgebra homomorphisms 
$\th_C : C \to \til{C}$ and $\opn{C}(\zeta_{\g}) : \til{C} \to C$. 
Then 
\[ \opn{C}(\zeta_{\g}) \circ \th_C = \bsym{1}_C , \]
the identity automorphism of $C$.
\end{lem}

\begin{proof}
This is true for any pair of adjoint functors; see 
\cite[Section IV.1 Theorem 1]{Ma}.
\end{proof}

\begin{lem} \label{lem:21}
Let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ quasi-isomorphism. Then 
\[ (\opn{L} \circ \opn{C}_{\infty})(\Phi) : 
(\opn{L} \circ \opn{C})(\g) \to (\opn{L} \circ \opn{C})(\h) \]
is a DG Lie algebra quasi-isomorphism.
\end{lem}

\begin{proof}
Let us write
$C := \opn{C}(\g)$, $D := \opn{C}(\h)$ and $\Psi := \opn{C}_{\infty}(\Phi)$. 
Put on $C$ the ascending filtration 
$F_j C := \boplus_{k = 0}^j \opn{Sym}^k(\g[1])$; 
so that $\{ F_j C \}_{j \geq 0}$ is an admissible coalgebra filtration, in the
sense of \cite[Definition 4.4.1]{Hi2}. Likewise there is an 
admissible coalgebra filtration $\{ F_j D \}_{j \geq 0}$ on $D$.
According to step 2 of the proof of \cite[Proposition 4.4.3]{Hi2}, the
coalgebra homomorphism $\Psi$ is a filtered quasi-isomorphism. 
Hence by \cite[Proposition 4.4.4]{Hi2} the DG Lie algebra homomorphism 
$(\opn{L} \circ \opn{C}_{\infty})(\Phi) = \opn{L}(\Psi)$
is a quasi-isomorphism.
\end{proof}








\section{$\mrm{L}_{\infty}$ Quasi-isomorphisms between Pronilpotent Algebras}
\label{sec:L-infty-cplt}

Let $(R, \m)$ be a parameter $\K$-algebra, and let
$\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ morphism between DG Lie algebras. 
Then $\Phi$ extends uniquely to an $R$-multilinear $\mrm{L}_{\infty}$ morphism 
\[ \Phi_{R} : R \hot \g \to R \hot \h , \]
whose $i$-th Taylor coefficient
\[ \partial^i \Phi_{R} :
\underset{i}{\underbrace{(R \hot \g) \times \cdots \times 
(R \hot \g)}} \to R \hot \h \]
is the $R$-multilinear homogeneous extension of 
$\partial^i \Phi$. See \cite[Section 3]{Ye2} for more details. 

\begin{dfn} \label{dfn:6}
Let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ morphism, and let 
$(R, \m)$ be a parameter algebra. For an element 
$\om \in \m \hot \g^1$ we define
\[ \opn{MC}(\Phi, R)(\om) := 
\sum_{i \geq 1} \, \smfrac{1}{i!} (\partial^i \Phi_{R})
(\underset{i}{\underbrace{\om, \ldots, \om}}) \in \m \hot \h^1 . \]
\end{dfn}

Note that the sum above converges in the $\m$-adic topology of 
$\m \hot \h^1$, since 
\[ (\partial^i \Phi_{R})(\om, \ldots, \om)
\in \m^i \hot \h^1 = \m^{i-1} \cdot (\m \hot \h^1) . \]

\begin{prop} \label{prop:4}
Let 
$\om \in \opn{MC}(\g, R) = \opn{MC}(\m \hot \g)$.
Then the element
$\opn{MC}(\Phi, R)(\om)$ belongs to $\opn{MC}(\h, R)$.
Thus we get a function 
\[ \opn{MC}(\Phi, R) : \opn{MC}(\g, R) \to \opn{MC}(\h, R) . \]
\end{prop}

\begin{proof}
Let $R_j := R / \m^{j+1}$, and let $p_j : R \to R_j$ be the projection.
According to \cite[Theorem 3.21]{Ye2}, which refers to the artinian case, we
have
\[ \opn{MC}(\Phi, R_j)(p_j(\om)) \in \opn{MC}(\h , R_j) \]
for every $j$. And by Lemma \ref{lem:6}(2) we know that 
\[ \opn{MC}(\h, R) \cong 
\lim_{\leftarrow j}\, \opn{MC}(\h, R_j) . \]
\end{proof}

Let $\Om_{\K[t]} = \K[t] \oplus \Om^1_{\K[t]}$ be the algebra of polynomial
differential forms
in the variable $t$ (relative to $\K$). This is a commutative DG
algebra. For $\la \in \K$ there is a DG algebra homomorphism
$\sg_{\la} : \Om_{\K[t]} \to \K$, namely $t \mapsto \la$.
There is an induced homomorphism of DG Lie algebras 
\begin{equation} \label{eqn:2}
\sg_{\la}  :  \m \hatotimes \Om_{\K[t]} \hatotimes \g \to 
\m \hatotimes \g ,
\end{equation}
and an induced function
\begin{equation} \label{eqn:61}
\ol{\opn{MC}}(\sg_{\la}) : 
\ol{\opn{MC}} ( \m \hatotimes \Om_{\K[t]} \hatotimes \g) 
\to \ol{\opn{MC}}(\m \hatotimes \g) 
\end{equation}

We shall often think of elements of $\Om_{\K[t]}$ as 
``functions of $t$'', as in Section \ref{sec:facts}. Given elements
$f(t) \in \Om_{\K[t]}$ and $\la \in \K$,
we shall use the substitution notation  
$f(\la) := \sg_{\la} (f(t)) \in \K$.

\begin{lem} \label{lem:16}
Here $\lambda = 0, 1$. 
\begin{enumerate}
\item The homomorphisms $\sg_0, \sg_1$ in formula \tup{(\ref{eqn:2})}
are quasi-iso\-morphisms.

\item The functions $\ol{\opn{MC}}(\sg_0)$ and $\ol{\opn{MC}}(\sg_1)$
in formula \tup{(\ref{eqn:61})} are bijections.

\item The bijections 
$\ol{\opn{MC}}(\sg_0)$ and $\ol{\opn{MC}}(\sg_1)$ are equal.
\end{enumerate} 
\end{lem}

\begin{proof}
(1) This is because the homomorphisms $\sg_i : \Om_{\K[t]} \to \K$ are
homotopy equivalences (of complexes of $\K$-modules).

\medskip \noindent
(2) This is by item (1) and Theorem \ref{thm:2}.

\medskip \noindent
(3) Note that the inclusion
\[ \phi : \m \hot \g \to \m \hatotimes \Om_{\K[t]} \hatotimes \g \]
is also a quasi-isomorphism, and that 
$\sg_0 \circ \phi = \sg_1 \circ \phi$ is the identity automorphism of 
$\m \hot \g$. Hence 
\[ \ol{\opn{MC}}(\sg_0) \circ \ol{\opn{MC}}(\phi) = 
\ol{\opn{MC}}(\sg_1) \circ \ol{\opn{MC}}(\phi) , \]
and canceling the bijection $\ol{\opn{MC}}(\phi)$ we obtain our result.
\end{proof}

\begin{lem} \label{lem:17}
Let $\om_0, \om_1 \in \opn{MC}(\m \hatotimes \g)$. The following two
conditions are equivalent:
\begin{enumerate}
\rmitem{i} There exists an element 
$g \in \opn{exp}(\m \hatotimes \g^0)$ such that 
\[ \opn{Af}(g)(\om_0) = \om_1 . \]
\rmitem{ii} There exists an element 
\[ \om(t) \in 
\opn{MC}( \m \hatotimes \Om_{\K[t]} \hatotimes \g) \]
such that 
$\om(0) = \om_0$ and $\om(1) = \om_1$. 
\end{enumerate}
\end{lem}

\begin{proof}
(i) $\Rightarrow$ (ii): Consider the elements $\ga := \log(g) \in \m \hot
\g^0$, 
\[ g(t) := \exp(t \ga) \in \exp(\m \hot (\Om_{\K[t]} \ot \g)^0) \]
and 
\[ \om(t) :=  \opn{Af}(g(t))(\om_0) \in 
\opn{MC}(\m \hot \Om_{\K[t]} \hot \g) . \]
Then 
\[ \om(0) = \opn{Af}(g(0))(\om_0) = \opn{Af}(1)(\om_0) = \om_0 \]
and
\[ \om(1) = \opn{Af}(g(1))(\om_0) =
\opn{Af}(g)(\om_0) = \om_1 . \]

\medskip \noindent
(ii) $\Rightarrow$ (i): Let us write $[\om_i]$ for the classes in 
$\ol{\opn{MC}}(\m \hatotimes \g)$.
We know that 
\[ \ol{\opn{MC}}(\sg_i)([\om(t)]) = [\om_i] \]
for $i = 0, 1$. By Lemma \ref{lem:16}(3) we know that 
$\ol{\opn{MC}}(\sg_0) = \ol{\opn{MC}}(\sg_1)$.
Therefore $[\om_0] = [\om_1]$; and by definition this says that 
$\opn{Af}(g)(\om_0) = \om_1$ for some $g$. 
\end{proof}

\begin{prop} \label{prop:5}
Let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ morphism.
The function 
\[ \opn{MC}(\Phi, R) : \opn{MC}(\g, R) \to \opn{MC}(\h, R) \]
respects gauge equivalences. Therefore there is an induced function 
\[ \ol{\opn{MC}}(\Phi, R) : \ol{\opn{MC}}(\g, R) \to 
\ol{\opn{MC}}(\h, R) . \]
\end{prop}

\begin{proof}
Let $A:= R \hot \Om_{\K[t]}$, which is a commutative DG algebra. There
are induced homomorphisms $\sg_i : A \to R$.
And there is an induced $A$-multilinear $\mrm{L}_{\infty}$ morphism 
\[ \Phi_{A} : \m \hot \Om_{\K[t]} \hot \g \to 
\m \hot \Om_{\K[t]} \hot \h  \]
(cf.\ \cite[Section 3]{Ye2}).
Let us write 
$\opn{MC}(\g, A) := \opn{MC}(\m \hot \Om_{\K[t]} \hot \g)$ etc.
There is a function $\opn{MC}(\Phi, A)$ whose formula is like in Definition
\ref{dfn:6}. Since the $\mrm{L}_{\infty}$ morphisms $\Phi_R$ and
$\Phi_A$ are induced from $\Phi$,
the diagram of functions 
\[ \UseTips \xymatrix @C=11ex @R=6ex {
\opn{MC}(\g, A) 
\ar[r]^{\opn{MC}(\Phi, A)}
\ar[d]_{\opn{MC}(\sg_i, R)}
&
\opn{MC}(\h, A) 
\ar[d]^{\opn{MC}(\sg_i, R)}
\\
\opn{MC}(\g, R) 
\ar[r]^{\opn{MC}(\Phi, R)}
&
\opn{MC}(\h, R) 
} \]
is commutative, for $i = 0, 1$.
Now suppose $\om_0, \om_1 \in \opn{MC}(\g, R)$ are gauge equivalent. By Lemma
\ref{lem:17} there is an element $\om(t) \in \opn{MC}(\g, A)$ such that 
$\om(i) = \om_i$. Define
$\chi_i := \opn{MC}(\Phi, R)(\om_i)$ and 
$\chi(t) := \opn{MC}(\Phi, A)(\om(t))$. 
Because the diagram above is commutative, we have
$\chi(i) = \chi_i$. Using Lemma \ref{lem:17} again we conclude that 
$\chi_0$ and $\chi_1$ are gauge equivalent.
\end{proof}

Let $\Psi : C \to D$ be the morphism in $\cat{DGCog}(\K)$ gotten by applying
the functor $\opn{C}_{\infty}$ to the $\opn{L}_{\infty}$ morphism 
$\Phi : \g  \to \h$. And let 
$\til{\Psi} : \til{C} \to \til{D}$ be the morphism gotten by applying
the functor $\opn{C} \circ \opn{L}$ to $\Psi : C \to D$. 
Since $\th_-$ is a natural transformation, we get a
commutative diagram 
\begin{equation} \label{eqn:62}
\UseTips \xymatrix @C=7ex @R=5ex {
C
\ar[r]^{\Psi}
\ar[d]_{\th_C}
&
D
\ar[d]^{\th_D}
\\
\til{C}
\ar[r]^{\til{\Psi}}
&
\til{D}
} 
\end{equation}
in $\cat{DGCog}(\K)$.
There is a corresponding commutative diagram 
\begin{equation} \label{eqn:63}
\UseTips \xymatrix @C=7ex @R=5ex {
\g
\ar[r]^{\Phi}
\ar[d]_{\th_{\g}}
&
\h
\ar[d]^{\th_{\h}}
\\
\til{\g}
\ar[r]^{\til{\Phi}}
&
\til{\h}
} 
\end{equation}
in $\cat{DGLie}_{\infty}(\K)$. Namely 
$\til{\g} = (\opn{L} \circ \opn{C})(\g)$,
$\til{\h} = (\opn{L} \circ \opn{C})(\h)$, 
and the full faithful functor $\opn{C}_{\infty}$ sends the 
diagram (\ref{eqn:63}) to the diagram (\ref{eqn:62}).
Note that by the proof of Lemma \ref{lem:20}, the Taylor coefficients
$\pa^j \th_C$ are nonzero for all $j$; so the corresponding morphism 
$\th_{\g} : \g \to \til{\g}$ in $\cat{DGLie}_{\infty}(\K)$ is not a DG Lie
algebra homomorphism. The same for $\th_{\h}$.

\begin{lem} \label{lem:18}
The diagram of functions
\begin{equation} \label{eqn:65}
\UseTips \xymatrix @C=11ex @R=6ex {
\opn{MC}(\g, R)
\ar[r]^{\opn{MC}(\Phi, R)}
\ar[d]_{\opn{MC}(\th_{\g}, R)}
&
\opn{MC}(\h, R)
\ar[d]^{\opn{MC}(\th_{\h}, R)}
\\
\opn{MC}(\til{\g}, R)
\ar[r]^{\opn{MC}(\til{\Phi}, R)}
&
\opn{MC}(\til{\h}, R)
} 
\end{equation}
is commutative.
\end{lem}

\begin{proof}
Because of Lemma \ref{lem:6}(2) we can assume that $R$ is artinian.
Consider the commutative diagram of DG coalgebras over $R$
\begin{equation} \label{eqn:67}
\UseTips \xymatrix @C=11ex @R=6ex {
R \ot C
\ar[r]^{\Psi_R}
\ar[d]_{\th_{C, R}}
&
R \ot D
\ar[d]^{\th_{D, R}}
\\
R \ot \til{C}
\ar[r]^{\til{\Psi}_R}
&
R \ot \til{D}
} 
\end{equation}
induced from (\ref{eqn:62}) by tensoring with $R$. 

Take any $\om \in \m \ot \g^1 \subset R \ot C$, and define 
\[ e := \exp(\om) = \sum_{i \geq 0} \, \smfrac{1}{i!} \om^i \in R \ot C . \]
According to \cite[Lemma 3.18]{Ye2} we have
\[ \begin{aligned}
& \bigl( \opn{MC}(\th_{\h}, R) \circ \opn{MC}(\Phi, R) \bigr)(\om) =
\log \bigl( (\th_{D, R} \circ \Psi_R)(e) \bigr) = \\
& \qquad \log \bigl( (\til{\Psi}_R \circ \th_{C, R})(e) \bigr) =
\bigl( \opn{MC}(\til{\Phi}, R) \circ \opn{MC}(\th_{\g}, R) \bigr)(\om) . 
\end{aligned} \]
This proves commutativity of the diagram.
\end{proof}



\begin{thm} \label{thm:3}
Let $\g$ and $\h$ be DG Lie algebras, 
let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ quasi-isomorphism, and
let $R$ be a parameter algebra, all over the field $\K$. 
Then the function 
\[ \ol{\opn{MC}}(\Phi, R) : \ol{\opn{MC}}(\g, R) \to 
\ol{\opn{MC}}(\h, R) \]
\tup{(}see Proposition \tup{\ref{prop:5})} is bijective. 
\end{thm}

The idea for the proof was suggested to us by Van den Bergh.

\begin{proof}
By Lemma \ref{lem:21} the DG Lie algebra homomorphism 
$\til{\Psi} : \til{\g} \to \til{\h}$ is a quasi-isomorphism.
Therefore by Theorem \ref{thm:2} the function 
\[  \ol{\opn{MC}}(\til{\Phi}, R) : \ol{\opn{MC}}(\til{\g}, R) \to 
\ol{\opn{MC}}(\til{\h}, R) \]
is bijective.

Next, by \cite[Proposition 4.4.3(1)]{Hi2} the DG Lie algebra homomorphism
$\zeta_{\g} : \til{\g} \to \g$ is a  quasi-isomorphism.
Again using Theorem \ref{thm:2} we conclude that the function 
\[  \ol{\opn{MC}}(\zeta_{\g}, R) : \ol{\opn{MC}}(\til{\g}, R) \to 
\ol{\opn{MC}}(\g, R) \]
is bijective. On the other hand, by Lemma \ref{lem:20}, with the arguments in
the proof of Lemma \ref{lem:18}, we see that 
\[ \opn{MC}(\zeta_{\g}, R) \circ \opn{MC}(\th_{\g}, R) = 
\bsym{1}_{\opn{MC}(\g, R)} . \]
Therefore 
\[ \ol{\opn{MC}}(\zeta_{\g}, R) \circ \ol{\opn{MC}}(\th_{\g}, R) = 
\bsym{1}_{\ol{\opn{MC}}(\g, R)} . \]
Because $\ol{\opn{MC}}(\zeta_{\g}, R)$ is a bijection, the same is true for the
function $\ol{\opn{MC}}(\th_{\g}, R)$. 
The same line of reasoning says that 
$\ol{\opn{MC}}(\th_{\h}, R)$ is bijective. 

Finally consider the commutative diagram of functions
\[ \UseTips \xymatrix @C=11ex @R=6ex {
\ol{\opn{MC}}(\g, R)
\ar[r]^{\ol{\opn{MC}}(\Phi, R)}
\ar[d]_{\ol{\opn{MC}}(\th_{\g}, R)}
&
\ol{\opn{MC}}(\h, R)
\ar[d]^{\ol{\opn{MC}}(\th_{\h}, R)}
\\
\ol{\opn{MC}}(\til{\g}, R)
\ar[r]^{\ol{\opn{MC}}(\til{\Phi}, R)}
&
\ol{\opn{MC}}(\til{\h}, R)
} \]
induced from (\ref{eqn:65}). 
We know that three of the arrows are bijective; so the fourth arrow, namely 
$\ol{\opn{MC}}(\Phi, R)$, is also bijective.
\end{proof}

\begin{rem} \label{rem:1}
Lemma 3.5 in our earlier paper \cite{Ye1} says that the canonical function 
\[ \ol{\opn{MC}}(\g, R) \to \lim_{\leftarrow j} \,
\ol{\opn{MC}}(\g, R / \m^j) \]
is bijective. The proof of this Lemma
(which is actually omitted from the paper) is incorrect. Moreover, we
suspect that statement itself is false. The hidden assumption was that 
the gauge group $\opn{G}(\g, R)$ acts on the set $\opn{MC}(\g, R)$
with {\em closed} orbits. 

This lemma is used to deduce \cite[Corollary 3.10]{Ye1} (incorrectly) 
from the nilpotent case. The correction is to replace 
\cite[Corollary 3.10]{Ye1} with Theorem \ref{thm:3} above.
The same correction pertains also to \cite[formula (12.2)]{Ye4}.
\end{rem}

\begin{rem}
This is a good place to correct a typographical error (repeated several
times) in \cite[Section 3]{Ye2}. In Lemmas 3.14 and 3.18 of op.\ cit., instead
of ``$\m \g [1]$'' the correct expression should be ``$\m \g^1$'' or
``$(\m \g [1])^0$''.

Let us also mention that a ``colocal coalgebra homomorphism'', in the sense of 
\cite[Definition 3.3]{Ye2}, is the same as a ``unital coalgebra homomorphism''.
\end{rem}
