---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-003-3-dg-lie-quasi-isomorphisms-nilpotent-algebras
section_title: "DG Lie Quasi-isomorphisms – Nilpotent Algebras"
section_number: 3
pages: 10-14
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.976
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:dg-quasi-nilp}

In this section we prove several lemmas that will be used in Section 
\ref{sec:dg-quasi-comp}. We assume that 
$(R, \m)$ is an artinian parameter algebra, but $\m \neq 0$. Also we have a DG
Lie algebra quasi-isomorphism $\phi : \g \to \h$. 

Let 
\[ l(R) := \min\, \{ l \in \N \mid \m^{l+1} = 0 \} , \]
and define $\n := \m^{l(R)}$. Thus $\n$ is an ideal in $R$ satisfying 
$\m \n = 0$. Let 
$\bar{R} := R / \n$ and $\bar{\m} := \m / \n$. 
So $(\bar{R}, \bar{\m})$ is a parameter algebra, and there is a 
canonical surjection $p : R \to \bar{R}$.

Our assumption that $\m \neq 0$ implies that $l(R) \geq 1$, and that
$l(\bar{R}) < l(R)$.

The homomorphism $p : R \to \bar{R}$ induces a surjective homomorphism of DG Lie
algebras 
\[ p : \m \otimes \g \to \bar{\m} \otimes \g , \]
and likewise for $\h$. Thus we get a commutative diagram of morphisms of \lb
groupoids 
\[ \UseTips \xymatrix @C=9ex @R=6ex {
\mbf{Del}^{\mrm{r}}(\g, R)
\ar[r]^{\phi}
\ar[d]_{p}
&
\mbf{Del}^{\mrm{r}}(\h, R)
\ar[d]^{p}
\\
\mbf{Del}^{\mrm{r}}(\g, \bar{R})
\ar[r]^{\phi}
&
\mbf{Del}^{\mrm{r}}(\h, \bar{R}) \ ,
} \]
where, for the sake of brevity, we write $p$ instead of 
$\mbf{Del}^{\mrm{r}}(\g, p)$, etc. 

Given elements $\om, \om' \in \opn{MC}(\g, R)$, let
$\bar{\om} := p(\om)$ and $\bar{\om}' := p(\om')$ in 
$\opn{MC}(\g, \bar{R})$. For any element 
$\bar{g} \in \opn{G}(\g, \bar{R})(\bar{\om}, \bar{\om}')$
we define 
\begin{equation} \label{eqn:4}
\opn{G}(\g, R)(\om, \om') / \bar{g} :=  
\{ g \in \opn{G}(\g, R)(\om, \om') \mid p(g) = \bar{g} \} .
\end{equation}

Next, given an element $\bar{\om} \in \opn{MC}(\g, \bar{R})$, 
let us denote by $\mbf{Del}(\g, R) / \bar{\om}$ 
the fiber over $\bar{\om}$ of the morphism of groupoids 
\[ p : \mbf{Del}(\g, R) \to \mbf{Del}(\g, \bar{R}) . \]
Thus the set of objects of  $\mbf{Del}(\g, R) / \bar{\om}$ is the set 
\begin{equation}
\opn{MC}(\g, R) / \bar{\om} := \{ \om \in \opn{MC}(\g, R) \mid 
p(\om) = \bar{\om} \} .
\end{equation}
The set of morphisms $\om \to \om'$ in $\mbf{Del}(\g, R) / \bar{\om}$ 
is 
\begin{equation}
\opn{G}(\g, R)(\om, \om') / 1 :=  
\{ g \in \opn{G}(\g, R)(\om, \om') \mid p(g) = 1 \} . 
\end{equation}

We shall need some of this construction also for the groupoid 
$\mbf{Del}^{\mrm{r}}(\g, R)$.
Given elements $\om, \om' \in \opn{MC}(\g; R)$, let
$\bar{\om} := p(\om)$ and $\bar{\om}' := p(\om')$ in 
$\opn{MC}(\g, \bar{R})$.
Suppose 
$\bar{g} \in \opn{G}^{\mrm{r}}(\g, \bar{R})(\bar{\om}, \bar{\om}')$.
We define the subset 
\begin{equation}
\opn{G}^{\mrm{r}}(\g, R)(\om, \om') / \bar{g} := 
\{ g \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om') \mid p(g) = \bar{g} \} . 
\end{equation}

We now recall the obstruction functions $o_2$ and $o_1$ introduced in
\cite[Section 2.6]{GM}. Let us denote by 
$\mrm{Z}^i(\g)$ the $\K$-module of $i$-cocycles in $\g$. 
For $\al \in \m \otimes \mrm{Z}^i(\g)$ we shall denote its cohomology class by 
$[\al] \in \m \otimes \mrm{H}^i(\g) \cong \mrm{H}^i(\m \ot \g)$.

Let 
\[ \opn{cur} : \m \otimes \g^1 \to \m \otimes \g^2 \]
be the function 
\begin{equation} \label{eqn:36}
\opn{cur}(\om) := \d(\omega) + \smfrac{1}{2} [\omega, \omega] .
\end{equation}
(``$\opn{cur}$'' stands for ``curvature''.)
Thus $\om$ is an MC element iff $\opn{cur}(\om) = 0$.
Given $\bar{\om} \in \opn{MC}(\g, \bar{R})$, 
choose any lift to an element 
$\om \in \m \otimes \g^1$.
Then 
$\opn{cur}(\om) \in \n \otimes \mrm{Z}^2(\g)$,
and we define 
\begin{equation} \label{eqn:41}
o_2(\bar{\om}) := [\opn{cur}(\om)] \in \n \otimes \mrm{H}^2(\g) .
\end{equation}
It is shown in \cite{GM} that $o_2(\bar{\om})$
is independent of the choice, and the resulting obstruction function
\[ o_2 : \opn{MC}(\g, \bar{R}) \to 
\n \otimes \mrm{H}^2 (\g) \]
has the property that an element 
$\bar{\om} \in \opn{MC}(\g, \bar{R})$ 
lifts to an element of $\opn{MC}(\g, R)$
iff $o_2(\bar{\om}) = 0$.

Consider an element $\bar{\om} \in \opn{MC}(\g, \bar{R})$.
The set 
$\opn{MC}(\g, R) / \bar{\om}$, if it is nonempty, 
has a simply transitive action by the additive group 
$\n \otimes \mrm{Z}^1(\g)$, namely 
$\om \mapsto \om + \beta$ for $\beta \in \n \otimes \mrm{Z}^1(\g)$.
Given $\om, \om' \in \opn{MC}(\g, R) / \bar{\om}$, define 
\begin{equation} \label{eqn:42}
o_1(\om, \om') := [\om - \om'] \in \n \otimes \mrm{H}^1 (\g) .
\end{equation}
The obstruction function
\[ o_1 : \opn{MC}(\g, R) / \bar{\om} \ \times \ 
\opn{MC}(\g, R) / \bar{\om} \to 
\n \otimes \mrm{H}^1 (\g)  \]
has the property that the set 
$\opn{G}(\g, R)(\om, \om') / 1$ 
is nonempty  iff 
$o_1(\om, \om') = 0$. 

The obstruction functions $o_2$ and $o_1$ are functorial in $\g$ (in the
obvious sense).

\begin{rem}
It is possible to define the obstruction $o_0$ here too, but we will not use it.
Consider the exact sequence of complexes 
\[ 0 \to \n \otimes \g \to (\m \otimes \g)_{\om} \xar{ \ p \ }
(\bar{\m} \otimes \g)_{\bar{\om}} \to 0 . \]
{}From the cohomology  exact sequence we get a homomorphism
\[ \mrm{H}^{-1} ((\bar{\m} \otimes \g)_{\bar{\om}}) \to
\n \otimes \mrm{H}^{0}(\g) . \]
For 
$g, g' \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om') / \bar{g}$,
the obstruction class $o_0(g, g')$ lives in the cokernel of this homomorphism.
\end{rem}

\begin{lem} \label{lem:1}
Let 
$\bar{\chi} \in \opn{MC}(\h, \bar{R})$,
$\bar{\om} \in \opn{MC}(\g, \bar{R})$,
$\chi \in \opn{MC}(\h, R) / \bar{\chi}$ 
and
\[ \bar{h} \in \opn{G}(\h, \bar{R})(\phi(\bar{\om}), \bar{\chi} ) . \]
Then there exist 
\[ \om \in \opn{MC}(\g, R) / \bar{\om} \]
and 
\[ h \in \opn{G}(\h, R)(\phi(\om), \chi) / \bar{h} . \]
\end{lem}

\begin{proof}
The proof is very similar to the proof of ``Surjective on isomorphism \lb
classes'' in \cite[Subsection 2.11]{GM}. It is illustrated in Figure
\ref{fig:1}.

Let 
\[ \bar{\chi}' := \opn{Af}(\bar{h})^{-1}(\bar{\chi}) 
=\phi(\bar{\om}) \in \opn{MC}(\h, \bar{R}) . \]
Choose any $h' \in \opn{G}(\h, R)$ lying above 
$\bar{h}$, and let 
\[ \chi' := \opn{Af}(h')^{-1}(\chi) \in \opn{MC}(\h, R) / \bar{\chi}' . \]
Since $\chi'$ exists, the obstruction class 
$o_2(\bar{\chi}')$ is zero. Now 
$\phi(\bar{\om}) = \bar{\chi}'$, so by functoriality of the obstruction classes
we get 
\[ \mrm{H}^2 (\phi)(o_2(\bar{\om})) = o_2(\bar{\chi}') = 0 . \]
The assumption is that $\mrm{H}^2 (\phi)$ is injective; 
hence $o_2(\bar{\om}) = 0$, and we can find 
$\om'' \in \opn{MC}(\g, R)$ lying above $\bar{\om}$. 

Let $\chi'' := \phi(\om'') \in \opn{MC}(\h, R) / \bar{\chi}'$. 
Consider the pair of elements 
$\chi'', \chi' \in \opn{MC}(\h, R) / \bar{\chi}'$.
There is an obstruction class 
\[ o_1(\chi'', \chi') \in \n \otimes \mrm{H}^1 (\h) . \]
By assumption the homomorphism $\mrm{H}^1 (\phi)$ is surjective, so there is 
is a cohomology class 
$c \in \n \otimes \mrm{H}^1 (\g)$
such that 
$\mrm{H}^1 (\phi)(c) = o_1(\chi'', \chi')$. 
Let 
$\gamma \in \n \otimes \mrm{Z}^1 (\g)$
be a cocycle representing $c$, and define
\[ \om := \om'' - \gamma \in \m \otimes \g^1 . \]
Then 
$\om \in \opn{MC}(\g, R) / \bar{\om}$
(it is an easy calculation done in \cite{GM}).
Let 
\[ \chi''' := \phi(\om) \in \opn{MC}(\h, R) / \bar{\chi}' . \]
Now $o_1(\om'', \om') = c$, so
\[ o_1(\chi''', \chi') = o_1(\chi'', \chi') - o_1(\chi'', \chi''') = 
o_1(\chi'', \chi') - \mrm{H}^1 (\phi)(o_1(\om'', \om')) = 0 . \]
Therefore there exists 
$h''' \in \opn{G}(\g, R)(\chi''', \chi') / 1$. 
And we have
\[ h := h' \cdot h''' \in \opn{G}(\g, R)(\chi''', \chi) / \bar{h} . \]
\end{proof}

\begin{figure}
\includegraphics[scale=0.35]{figure-1.jpg}
\caption{Illustration for the proof of Lemma \ref{lem:1}.
The diagram is commutative.} 
\label{fig:1}
\end{figure}

\begin{lem} \label{lem:5}
Let $\om \in \opn{MC}(\g, R)$ and 
$\chi := \phi(\om) \in \opn{MC}(\h, R)$.
\begin{enumerate}
\item The homomorphism of DG Lie algebras 
\[ \phi : (\m \otimes \g)_{\om} \to (\m \otimes \h)_{\chi} \]
is a quasi-isomorphism.

\item The group homomorphism 
\[ \phi : \opn{G}^{\mrm{r}}(\g, R)(\om, \om) \to 
\opn{G}^{\mrm{r}}(\h, R)(\chi, \chi) \]
is an isomorphism.
\end{enumerate}
\end{lem}

\begin{proof}
(1) This is done by induction on $l(R)$. If $l(R) = 1$ then 
$\m^2 = 0$, so $\d_{\om} = \d$ and $\d_{\chi} = \d$. 
Since $\phi : \g \to \h$ is a 
quasi-isomorphisms, and since $\m$ is flat over $\K$, the assertion is true.

Now assume that $l(R) \geq 2$. Since $\m \n = 0$ it follows that 
$\d_{\om}|_{\n \otimes \g} = \d|_{\n \otimes \g}$; 
and likewise for $\n \otimes \h$. 
Let $\bar{\om} := p(\om)$ and $\bar{\chi} := p(\chi)$. 
We get a commutative diagram of complexes of $R$-modules 
\[ \UseTips \xymatrix @C=6ex @R=6ex {
0
\ar[r]
&
\n \otimes \g
\ar[r]
\ar[d]^{\phi}
&
(\m \otimes \g)_{\om}
\ar[r]^{p}
\ar[d]^{\phi}
&
(\bar{\m} \otimes \g)_{\bar{\om}}
\ar[r]
\ar[d]^{\phi}
& 
0
\\
0
\ar[r]
&
\n \otimes \h
\ar[r]
&
(\m \otimes \h)_{\chi}
\ar[r]^{p}
&
(\bar{\m} \otimes \h)_{\bar{\chi}}
\ar[r]
&
0
} \]
with exact rows. By induction the right vertical arrow is a quasi-isomorphism;
and the left vertical arrow is a quasi-isomorphism by the same argument given
in the case $l(R) = 1$.
Therefore the middle vertical arrow is a quasi-isomorphism.

\medskip \noindent
(2) Combine item (1) above and Proposition \ref{prop:2}.
\end{proof}

\begin{lem} \label{lem:2}
Let $\om, \om' \in \opn{MC}(\g, R)$, and define 
$\bar{\om} := p(\om)$, 
$\bar{\om}' := p(\om')$, 
$\chi := \phi(\om)$,
$\chi' := \phi(\om')$, 
$\bar{\chi} := \phi(\bar{\om})$ and 
$\bar{\chi}' := \phi(\bar{\om}')$.
Let 
\[ \bar{g} \in \opn{G}^{\mrm{r}}(\g, \bar{R})(\bar{\om}, \bar{\om}') , \]
\[ \bar{h} := \phi(\bar{g}) \in \opn{G}^{\mrm{r}}(\h, \bar{R})
(\bar{\chi}, \bar{\chi}') , \]
and
\[ h \in \opn{G}^{\mrm{r}}(\h, R)(\chi, \chi')  / \bar{h} . \]
Then there exists a unique element
\[ g \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om') / \bar{g} \]
such that $\phi(g) = h$.
\end{lem}

\begin{proof}
The proof is very similar to the proof of ``Full''
in \cite[Subsection 2.11]{GM}. (Note however that there is a mistake in loc.\
cit. In our notation, what is done there is referring to the obstruction class 
$o_1(\om, \om')$, but this is not defined since 
$p(\om) \neq p(\om')$ in general.) The proof is illustrated in Figure
\ref{fig:2}.

Choose an arbitrary lift $g'' \in \opn{G}(\g, R)$ of $\bar{g}$, 
namely $\bar{g} = p(\eta_1(g''))$.
Define 
\[ \om'' := \opn{Af}(g'')(\om) \in \opn{MC}(\g, R) , \]
\[ h'' := \phi(g'') \in \opn{G}(\h, R) , \]
\[ \chi'' := \phi(\om'') \in \opn{MC}(\h, R) \]
and
\[ h' := h \cdot (h'')^{-1} \in 
\opn{G}(\h, R)(\chi'', \chi') / 1 . \]
Since $\om'', \om' \in \opn{MC}(\g, R) / \bar{\om}'$
the obstruction class 
$o_1(\om'', \om')$
is defined, and it satisfies 
\[ \mrm{H}^1 (\phi)(o_1(\om'', \om')) = 
o_1(\chi'', \chi') = 0 \]
because $h'$ exists. By assumption the homomorphism
$\mrm{H}^1 (\phi)$ is injective, and we conclude that 
$o_1(\om'', \om') = 0$. So there exists some 
$g' \in \opn{G}(\g, R)(\om'', \om') / 1$.
Let 
\[ g''' := g' \cdot g'' \in \opn{G}(\g, R)(\om, \om') . \]
Then $p(\eta_1(g''')) = \bar{g}$, and hence
\[ \eta_1(g''') \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om') / \bar{g} . \]

By Lemma \ref{lem:5}(2) we have a group isomorphism 
\[ \phi : \opn{G}^{\mrm{r}}(\g, R)(\om, \om) / 1 \to 
\opn{G}^{\mrm{r}}(\h, R)(\chi, \chi) / 1 . \]
Since the set 
$\opn{G}^{\mrm{r}}(\g, R)(\om, \om') / \bar{g}$
is nonempty (it contains $\eta_1(g''')$), it admits a simply transitive action
by the group 
$\opn{G}^{\mrm{r}}(\g, R)(\om, \om) / 1$. 
Therefore the function
\[ \phi : \opn{G}^{\mrm{r}}(\g, R)(\om, \om') / \bar{g} \to 
\opn{G}^{\mrm{r}}(\h, R)(\chi, \chi') / \bar{h} \]
is bijective. We see that there is a unique element 
$g \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om') / \bar{g}$
such that 
$\phi(g) = h$.
\end{proof}

\begin{figure}
\includegraphics[scale=0.35]{figure-2.jpg}
\caption{Illustration for the proof of Lemma \ref{lem:2}.
Some of the arrows, like $g$ and $h$, belong to the groupoid
$\mbf{Del}^{\mrm{r}}(-, -)$. 
Other arrows, like $g''$ and $h''$, belong to the groupoid
$\mbf{Del}(-, -)$. 
The function $\phi$  sends $\om \mapsto \chi$,
$\bar{\om} \mapsto \bar{\chi}$, $g \mapsto h$, etc. 
The whole diagram is commutative.} 
\label{fig:2}
\end{figure}
