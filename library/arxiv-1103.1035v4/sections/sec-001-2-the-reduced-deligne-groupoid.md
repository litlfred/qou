---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI"
section_id: sec-001-2-the-reduced-deligne-groupoid
section_title: "The Reduced Deligne Groupoid"
section_number: 2
pages: 9-23
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.914
---
\label{sec:red-del}

As before, $\K$ is a field of characteristic $0$,
$(R, \m)$ is a parameter algebra over $\K$, and 
$\g = \boplus_{i \in \Z} \g^i$ is a DG Lie algebra over $\K$. 

Let us write 
\begin{equation} \label{eqn:44}
\opn{MC}(\g, R) := \opn{MC}(R \hatotimes \g)
\end{equation}
and 
\begin{equation} \label{eqn:45}
\opn{G}(\g, R) := \exp(\m \hatotimes \g^0) .
\end{equation} 
Given $\om, \om' \in \opn{MC}(\g, R)$, let
\begin{equation} \label{eqn:43}
\opn{G}(\g, R)(\om, \om') :=
\{ g \in \opn{G}(\g, R) \mid \opn{Af}(g)(\om) = \om' \} .
\end{equation}
As in \cite{GM} we define the {\em Deligne groupoid} 
$\mbf{Del}(\g, R)$ to be the transformation \lb groupoid
associated to the action of the gauge group $\opn{G}(\g, R)$ on
the set $\opn{MC}(\g, R)$. 
So the set of objects of $\mbf{Del}(\g, R)$ is $\opn{MC}(\g, R)$, and the set
of morphisms $\om \to \om'$ in this groupoid is 
$\opn{G}(\g, R)(\om, \om')$. Identity morphisms and composition in the
groupoid are those of the group $\opn{G}(\g, R)$. 

Now suppose $\om, \om' \in \opn{MC}(\g, R)$ and 
$g \in \opn{G}(\g, R)(\om, \om')$. 
Since  
\[ \opn{Af}(g \circ h \circ g^{-1}) = 
\opn{Af}(g) \circ \opn{Af}(h) \circ \opn{Af}(g)^{-1}  \]
for any $h$, and in view of (\ref{eqn:10}), there is a group isomorphism
\begin{equation}
\opn{Ad}(g) : \opn{G}(\g, R)(\om, \om) \to \opn{G}(\g, R)(\om', \om') .
\end{equation}

Given $\om \in \opn{MC}(\g, R)$ there is the derivation 
$\d_{\om}$ of formula (\ref{eqn:17}). Let us define
\begin{equation} \label{eqn:14}
\a^{\mrm{r}}_{\om} := \opn{Im} \bigl( \d_{\om} : 
\m \hatotimes \g^{-1} \to  \m \hatotimes \g^0 \bigr)
\end{equation}
and 
\begin{equation} \label{eqn:15}
(\m \hatotimes \g^0)(\om) := \opn{Ker} \bigl( \d_{\om} : 
\m \hatotimes \g^{0} \to  \m \hatotimes \g^1 \bigr) . 
\end{equation}
These are $R$-submodules of $\m \hatotimes \g^0$.

\begin{lem} \label{lem:4}
Let $\om \in \opn{MC}(\g, R)$.
Consider the bijection of sets
\[ \exp : \m \hatotimes \g^0 \iso \exp(\m \hatotimes \g^0) = 
\opn{G}(\g, R) . \]
\begin{enumerate}
\item The module 
$(\m \hatotimes \g^0)(\om)$ is a Lie subalgebra of 
$\m \hatotimes \g^0$, and 
\[ \exp \bigl( (\m \hatotimes \g^0)(\om) \bigr) = 
\opn{G}(\g, R)(\om, \om)  \]
as subsets of $\opn{G}(\g, R)$.

\item The module $\a^{\mrm{r}}_{\om}$ is a Lie ideal of the Lie algebra 
$(\m \hatotimes \g^0)(\om)$, and the subset
\[ N^{\mrm{r}}_{\om} = N^{\mrm{r}}(\g, R)_{\om} :=
\exp(\a^{\mrm{r}}_{\om}) \]
is a normal subgroup of $\opn{G}(\g, R)(\om, \om)$.

\item Let $g \in \opn{G}(\g, R)$ and
$\om' := \opn{Af}(g)(\om)$. Then 
\[ \opn{Ad}(g) \bigl( N^{\mrm{r}}_{\om} \bigr) = N^{\mrm{r}}_{\om'} . \]
\end{enumerate}
\end{lem}

\begin{proof}
(1) Since $\d_{\om}$ is a graded derivation of the  graded Lie
algebra $\m \hatotimes \g$, its kernel is a graded Lie subalgebra, and its image
is a graded Lie ideal in the kernel. In degree $0$ we get a Lie subalgebra 
$(\m \hatotimes \g^0)(\om)$, and a Lie ideal $\a^{\mrm{r}}_{\om}$ in it.

Because $\d_{\om}$ is a continuous homomorphism between complete $R$-modules,
its kernel $(\m \hatotimes \g^0)(\om)$ is closed; so this is a closed Lie
subalgebra of $\m \hatotimes \g^0$. This implies that the subset 
$\exp \bigl( (\m \hatotimes \g^0)(\om) \bigr)$ is a closed subgroup of 
$\opn{G}(\g, R)$. 
Moreover, let $\ga \in \m \hot \g^0$ and $g := \exp(\ga)$.  
In the proof of  \cite[Theorem 2.2]{Ge} it is shown that 
$\d_{\om}(\gamma) = 0$ iff 
$\opn{Af}(g)(\om) = \om$. This shows that  
\[ \exp \bigl( (\m \hatotimes \g^0)(\om) \bigr) = 
\opn{G}(\g, R)(\om, \om) . \]

\medskip \noindent
(2) We already know that $\a^{\mrm{r}}_{\om}$ is a Lie ideal of 
$(\m \hatotimes \g^0)(\om)$; but since this is not a closed ideal in general,
it is not immediate that the subset $\exp(\a^{\mrm{r}}_{\om})$ is a normal
subgroup of 
$\exp \bigl( (\m \hatotimes \g^0)(\om) \bigr)$.

Consider the CBH series
\[ F(x_1, x_2) = \sum_{j \geq 1}\, F_j(x_1, x_2) , \]
where $F_j(x_1, x_2)$ are homogeneous elements of degree $i$ in the 
free Lie algebra in the variables $x_1, x_2$ over $\Q$. 
It is known (cf.\ \cite{Bo}) that 
\begin{equation} \label{eqn:53}
\exp(\ga_1) \cdot \exp(\ga_2)  = \exp(F(\ga_1, \ga_2))
\end{equation}
for $\ga_1, \ga_2 \in \m \hot \g^0$. 

Let us define a bracket $[-,-]_{\om}$ on $\m \hot \g^{-1}$ as follows:
\[ [\al_1, \al_2]_{\om} := [ \d_{\om}(\al_1), \al_2] . \]
In general this is not a Lie bracket (the Jacobi identity may fail). However,
since $\d_{\om}$ is a square zero derivation of
the graded Lie algebra $\m \hot \g$, we have 
\[ \d_{\om}([\al_1, \al_2]_{\om}) = [\d_{\om}(\al_1), \d_{\om}(\al_2)] . \]

For any $j \geq 1$ and $\al_1, \al_2 \in \m \hot \g^{-1}$  consider 
the element 
$F_{j, \om}(\al_1, \al_2) \in \m \hot \g^{-1}$
gotten by evaluating the Lie polynomial $F_j(x_1, x_2)$
at $x_i \mapsto \al_i$, using the bracket $[-,-]_{\om}$. 
Now take any $\ga_1, \ga_2 \in \a^{\mrm{r}}_{\om}$, and choose 
$\al_1, \al_2 \in \m \hot \g^{-1}$ such that $\ga_i = \d_{\om}(\al_i)$. Then 
\[ \d_{\om}(F_{j, \om}(\al_1, \al_2)) = 
F_j(\ga_1, \ga_2) \in \m \hot \g^0 . \]
Let 
\[ \al :=  \bosum_{j \geq 1}\,  F_{j, \om}(\al_1, \al_2) \in 
\m \hot \g^{-1}  \]
and $\ga := \d_{\om} (\al) \in \a^{\mrm{r}}_{\om}$. 
By continuity we get
$F(\ga_1, \ga_2) = \ga$. 
{}From this and formula (\ref{eqn:53}) we see that 
$N^{\mrm{r}}_{\om} = \exp(\a^{\mrm{r}}_{\om})$ is a
subgroup of $\opn{G}(\g, R) = \exp (\m \hatotimes \g^0)$.

Similarly, Lemma \ref{lem:3}(2) implies that the subset
$\exp(\a^{\mrm{r}}_{\om})$ is
invariant under the operations $\opn{Ad}(g)$, 
$g \in \opn{G}(\g, R)(\om, \om)$. Therefore $N^{\mrm{r}}_{\om}$ is a
normal subgroup of $\opn{G}(\g, R)(\om, \om)$.

(3) According to Lemma \ref{lem:3}(2) we know that 
$\opn{Ad}(g)(\a^{\mrm{r}}_{\om}) = \a^{\mrm{r}}_{\om'}$.
\end{proof}

Note that the set 
$\opn{G}(\g, R)(\om, \om')$ has a left action by the group 
$N^{\mrm{r}}_{\om'}$, and a right action by the group
$N^{\mrm{r}}_{\om}$. Define
\begin{equation} \label{eqn:16}
\opn{G}^{\mrm{r}}(\g, R)(\om, \om') := 
\opn{G}(\g, R)(\om, \om') / N^{\mrm{r}}_{\om} \, ,
\end{equation}
the quotient set. So there is a surjective function 
\begin{equation} \label{eqn:51}
\eta_1 : \opn{G}(\g, R)(\om, \om') \to \opn{G}^{\mrm{r}}(\g, R)(\om, \om') . 
\end{equation}

By Lemma \ref{lem:4}(3), the multiplication map of 
$\opn{G}(\g, R)$ induces maps
\begin{equation} \label{eqn:68}
\opn{G}^{\mrm{r}}(\g, R)(\om, \om') \times 
\opn{G}^{\mrm{r}}(\g, R)(\om', \om'') \to
\opn{G}^{\mrm{r}}(\g, R)(\om, \om'')
\end{equation}
for any $\om, \om', \om'' \in \opn{MC}(\g, R)$.
If $\om' = \om$ then 
$\opn{G}^{\mrm{r}}(\g, R)(\om, \om)$ is a group.

\begin{dfn}
The {\em reduced Deligne groupoid} associated to $\g$ and $(R, \m)$
is the \lb groupoid $\mbf{Del}^{\mrm{r}}(\g, R)$ defined as follows. 
The set of objects of this groupoid is $\opn{MC}(\g, R)$. For any 
$\om, \om' \in \opn{MC}(\g, R)$, the set of morphisms $\om \to \om'$ is 
the set $\opn{G}^{\mrm{r}}(\g, R)(\om, \om')$
from formula (\ref{eqn:16}). The composition in $\mbf{Del}^{\mrm{r}}(\g, R)$
is given by formula (\ref{eqn:68}), and the identity morphisms are those of the
groups $\opn{G}^{\mrm{r}}(\g, R)(\om, \om)$.
\end{dfn}

There is a morphism of groupoids (i.e.\ a functor)
\begin{equation} \label{eqn:13}
\bsym{\eta} = (\eta_0, \eta_1) : \mbf{Del}(\phi, R) \to
\mbf{Del}^{\mrm{r}}(\phi, R) ,
\end{equation}
where $\eta_0$ is the identity on the set of objects
$\opn{MC}(\g, R)$, and $\eta_1$ is the surjective function in formula
(\ref{eqn:51}).  Hence 
\begin{equation} \label{eqn:5}
\pi_0 \bigl( \mbf{Del}^{\mrm{r}}(\g, R) \bigr) =
\pi_0 \bigl( \mbf{Del}(\g, R) \bigr) =
\ol{\opn{MC}}(\m \hatotimes \g)  ,
\end{equation}
where $\pi_0(-)$ denotes the set of isomorphism classes of objects of a
groupoid.

Given a homomorphism $f : (R, \m) \to (S, \n)$ of parameter algebras, and a
homomorphism 
$\phi : \g \to \h$ of DG Lie algebras, there is an induced 
DG Lie algebra homomorphism 
\[ f \otimes \phi : \m \hatotimes \g \to \n \hatotimes \h . \]
Hence there are induced morphisms of groupoids 
$\mbf{Del}(\phi, f)$ and $\mbf{Del}^{\mrm{r}}(\phi, f)$
such that the diagram 
\[ \UseTips \xymatrix @C=11ex @R=6ex {
\mbf{Del}(\g, R)
\ar[r]^{\mbf{Del}(\phi, f)}
\ar[d]_{\bsym{\eta}}
&
\mbf{Del}(\h, S)
\ar[d]^{\bsym{\eta}}
\\
\mbf{Del}^{\mrm{r}}(\g, R)
\ar[r]^{\mbf{Del}^{\mrm{r}}(\phi, f)}
&
\mbf{Del}^{\mrm{r}}(\h, S) 
} \]
is commutative. And there is an induced function 
\[ \pi_0 \bigl( \mbf{Del}^{\mrm{r}}(\phi, f) \bigr) :
\pi_0 \bigl( \mbf{Del}^{\mrm{r}}(\g, R) \bigr) \to 
\pi_0 \bigl( \mbf{Del}^{\mrm{r}}(\h, S) \bigr) . \]
Under the equality of sets (\ref{eqn:5}), and the corresponding one for 
$\h$ and $S$, we have equality of functions
\begin{equation} \label{eqn:18}
\pi_0 \bigl( \mbf{Del}^{\mrm{r}}(\phi, f) \bigr) =
\pi_0 \bigl( \mbf{Del}(\phi, f) \bigr) =
\ol{\opn{MC}}(f \otimes \phi) . 
\end{equation}

\begin{prop} \label{prop:2}
Let $\om \in \opn{MC}(\g, R)$. 
The bijection 
\[ \exp : \m \hot \g^0 \to  \opn{G}(\g, R) \] 
induces a bijection \tup{(}of sets\tup{)}
\[ \exp : \mrm{H}^0( (\m \hot \g)_{\om} ) \to 
\opn{G}^{\mrm{r}}(\g, R)(\om, \om) . \]
This bijection is functorial w.r.t.\ homomorphisms $(R, \m) \to (R, \n)$ of
parameter algebras and homomorphisms $\g \to \h$ of DG Lie algebras.
\end{prop}

\begin{proof}
This is an immediate consequence of Lemma \ref{lem:4}(1,2) and formula 
(\ref{eqn:16}).
\end{proof}

\begin{rem}
After writing an earlier version of this paper, we were told by M. Manetti that
M. Kontsevich had mentioned the idea of a reduced Deligne groupoid already in
1994. See \cite[page 19]{Ko1} and \cite{Mt}.
\end{rem}







\section{DG Lie Quasi-isomorphisms -- Nilpotent Algebras}
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









\section{DG Lie Quasi-isomorphisms -- Pronilpotent Algebras}
\label{sec:dg-quasi-comp}

In this section we extend \cite[Theorem 2.4]{GM} (attributed to Deligne) to the
case of complete noetherian local rings and unbounded DG Lie algebras. 
This is Theorem \ref{thm:2}.

Let $(R, \m)$ be a complete parameter algebra, and let
$\phi : \g \to \h$ be a DG Lie algebra quasi-isomorphism. 
As in Section \ref{sec:facts}, for any $j \in \N$ we write 
$R_j := R / \m^{j+1}$ and $\m_j := \m / \m^{j+1}$. We denote by 
$p_j : R \to R_j$ and $p_{j, i} : R_j \to R_i$ the canonical projections 
(for $j \geq i$).
Let $\n_j := \m^{j} / \m^{j + 1}$, which is an ideal in $R_j$ satisfying \lb
$\m_j \n_j = 0$ and 
\[ \n_j = \opn{Ker}(p_{j, j-1} : R_j \to R_{j - 1}) . \]
Thus $R_{j - 1} \cong R_j / \n_j$.

\begin{lem} \label{lem:6}
\begin{enumerate}
\item Let $\om \in  \opn{MC}(\g, R)$ and
$\chi := \phi(\om) \in \opn{MC}(\h, R)$.
Then the homomorphism of DG Lie algebras
\[ \phi :  (\m \hatotimes \g)_{\om} \to 
(\m \hatotimes \h)_{\chi} \]
is a quasi-isomorphism. 

\item The canonical function 
\[ \opn{MC}(\g, R) \to \lim_{\leftarrow j}\, \opn{MC}(\g, R_j) \]
is bijective.

\item For any $\om, \om' \in \opn{MC}(\g, R)$ the canonical function 
\[ \opn{G}^{\mrm{r}}(\g, R)(\om, \om') \to \lim_{\leftarrow j}\, 
\opn{G}^{\mrm{r}} ( \g, R_j) \bigl( p_j(\om), p_j(\om') \bigr) \]
is surjective.
\end{enumerate}
\end{lem}

Of course items (2-3) refer also to $\h$.

\begin{proof}
(1) We forget the Lie brackets. Let $M$ be the mapping cone of the homomorphism
of complexes of $R$-modules
\[ \phi :  (\m \hatotimes \g)_{\om} \to (\m \hatotimes \h)_{\chi} . \]
So 
\[ M = (\m \hatotimes \g)_{\om}[1] \oplus (\m \hatotimes \h)_{\chi} , \]
with a suitable differential. 
For any $j \geq 0$ let $\om_j := p_j(\om)$ and $\chi_j := p_j(\chi)$.
We have an inverse system of homomorphisms of complexes
\[ \phi_j :  (\m_j \hatotimes \g)_{\om_j} \to 
(\m_j \hatotimes \h)_{\chi_j} , \]
and we denote by $M_j$ the mapping cone of $\phi_j$.  
Then each $p_j : M \to M_j$ is surjective, and 
$M \cong \lim_{\leftarrow j}\, M_j$.
According to Lemma \ref{lem:5}(1) the complexes $M_j$ are acyclic. 
Therefore, using the Mittag-Leffler argument, the complex $M$ is also acyclic.

\medskip \noindent
(2) This is because $\m \hatotimes \g^1$ is $\m$-adically complete, and 
$\opn{MC}(\g, R)$ is a closed subset in it (w.r.t.\ the $\m$-adic metric).

\medskip \noindent
(3) Write $\om'_j := p_j(\om')$. 
Suppose we are given a sequence $\{ g_j \}_{j \in \N}$ of elements
\[ g_j \in \opn{G}^{\mrm{r}} ( \g, R_j)(\om_j, \om'_j ) \]
such that $p_{j, j-1}(g_j) = g_{j-1}$.
We are going to find a sequence $\{ \til{g}_j \}_{j \in \N}$ of elements
\[ \til{g}_j \in \opn{G} ( \g, R_j)(\om_j, \om'_j ) \]
such that $p_{j, j-1}(\til{g}_j) = \til{g}_{j-1}$
and $\eta_1(\til{g}_j) = g_j$ for all $j$.
Since the group $\opn{G}(\g, R)$ is 
complete w.r.t.\ its $\m$-adic filtration, the limit
\[ \til{g} := \lim_{\leftarrow j}\, \til{g}_j \in \opn{G}(\g, R) \]
exists; and by continuity 
$\til{g} \in \opn{G}(\g, R)(\om, \om')$.
Then the element
\[ g := \eta_1(\til{g}) \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om') \]
satisfies $p_j(g) = g_j$ for all $j$.

Here is the recursive construction of the sequence 
$\{ \til{g}_j \}_{j \in \N}$.
For $j = 0$ we take $\til{g}_0 := 1$. Now assume that $j \geq 1$ and we have a 
sequence $(\til{g}_0, \ldots, \til{g}_{j-1})$ as required.
Choose any element 
$\til{g}'_j \in \opn{G}(\g, R_j)(\om_j, \om'_j)$
such that $\eta_1(\til{g}'_j) = g_j$. 
Then 
\[ \eta_1(p_{j, j-1}(\til{g}'_j)) = p_{j, j-1}(\eta_1(\til{g}'_j)) = 
p_{j, j-1}(g_j) = g_{j-1} = \eta_1(\til{g}_{j-1}) . \]
There is some $\bar{a} \in N^{\mrm{r}}(\g, R_{j-1})_{\om_{j-1}}$
such that 
$\bar{a} \cdot p_{j, j-1}(\til{g}'_j) = \til{g}_{j-1}$.
Choose any $a \in N^{\mrm{r}}(\g, R_j)_{\om_j}$
lifting $\bar{a}$. Then 
$\til{g}_j := a \cdot \til{g}'_j$ will satisfy 
$p_{j, j-1}(\til{g}_j) = \til{g}_{j-1}$ and
$\eta_1(\til{g}_j) = g_j$.
\end{proof}

Here is the main result of this section. We denote the identity automorphism of
$R$ by $\bsym{1}_R$.

\begin{thm} \label{thm:2}
Let $(R, \m)$ be a parameter algebra over $\K$, and let $\phi : \g \to \h$ be a
DG Lie algebra quasi-isomorphism over $\K$. Then the function 
\[ \ol{\opn{MC}}(\bsym{1}_R \otimes \phi) : \ol{\opn{MC}}(\m \hatotimes \g) \to
\ol{\opn{MC}}(\m \hatotimes \h)  \]
is bijective. Moreover, the morphism of groupoids
\[ \mbf{Del}^{\mrm{r}}(\phi, R) : \mbf{Del}^{\mrm{r}}(\g, R) 
\to \mbf{Del}^{\mrm{r}}(\h, R)  \]
is an equivalence. 
\end{thm}

Observe that there are no finiteness nor boundedness conditions on $\g$ and
$\h$. 

\begin{proof}
We will prove these assertions:
\begin{enumerate}
\rmitem{a} The function $\ol{\opn{MC}}(\bsym{1}_R \otimes \phi)$
is surjective.

\rmitem{b}  The function $\ol{\opn{MC}}(\bsym{1}_R \otimes \phi)$
is injective.

\rmitem{c} For any 
$\om \in \opn{MC}(\g, R)$ the group homomorphism 
\[ \opn{G}^{\mrm{r}}(\phi, R) : \opn{G}^{\mrm{r}}(\g, R)(\om, \om) \to 
\opn{G}^{\mrm{r}}(\h, R) \bigl( \phi(\om), \phi(\om) \bigr) \]
is bijective. 
\end{enumerate}

Assertions (a-b) say that the function
$\ol{\opn{MC}}(\bsym{1}_R \otimes \phi)$
is bijective. Then assertion (c) implies that the function 
\[ \phi :  \opn{G}^{\mrm{r}}(\g, R)(\om, \om') \to 
\opn{G}^{\mrm{r}}(\h, R)(\phi(\om), \phi(\om')) \]
is bijective for every $\om, \om' \in \opn{MC}(\g, R)$.
Hence $\mbf{Del}^{\mrm{r}}(\phi, R)$ is an equivalence.

\medskip \noindent
Proof of (a). Here it is more convenient to work with the groupoids
$\mbf{Del}(-, -)$. 
Suppose we are given $\chi \in \opn{MC}(\h, R)$. We will find 
elements $\om \in \opn{MC}(\g, R)$ and 
$h \in \opn{G}(\h, R)(\phi(\om), \chi)$. 

Define $\chi_j := p_j(\chi) \in \opn{MC}(\h, R_j)$.
We are going to find a sequence $\{ \om_j \}_{j \in \N}$ of elements
$\om_j \in \opn{MC}(\g, R_j)$, and a sequence $\{ h_j \}_{j \in \N}$ of
elements
\[ h_j \in  \opn{G}(\h, R_j)(\phi(\om_j), \chi_j) , \]
such that $p_{j, j-1}(\om_j) = \om_{j-1}$ and 
$p_{j, j-1}(h_j) = h_{j-1}$ for all $j$.
This is done by induction on $j$.
For $j = 0$ we take $\om_0 := 0$ and $h_0 := 1 = \exp(0)$. 
Now consider $j \geq 1$. Assume that we have found sequences 
$(\om_0, \ldots, \om_{j-1})$ and 
$(h_0, \ldots, h_{j-1})$ satisfying the required conditions. 
By Lemma \ref{lem:1}, applied to the artinian local ring $R_j$,
and the elements $\chi_j, \om_{j-1}$ and $h_{j-1}$, 
there exist elements $\om_j$ and $h_j$ as required. 

Now the $R$-module $\m \hatotimes \g^1$ is $\m$-adically complete, 
and the set $\opn{MC}(\g, R)$ is closed inside 
$\m \hatotimes \g^1$ (with respect to the $\m$-adic metric). 
Hence the limit 
$\om := \lim_{\leftarrow j}\, \om_j$
belongs to $\opn{MC}(\g, R)$. 
The gauge group $\opn{G}(\h, R)$ is complete, since it is pronilpotent 
(with respect to its $\m$-adic filtration).
We get an element 
\[ h := \lim_{\leftarrow j}\, h_j \in \opn{G}(\h, R) . \]
By continuity we see that 
$\opn{Af}(h)(\phi(\om)) = \chi$.

\medskip \noindent
Proof of (b). Here we prefer to work with the groupoids
$\mbf{Del}^{\mrm{r}}(-,-)$.
Take $\om, \om' \in \opn{MC}(\g, R)$, and define 
$\chi := \phi(\om)$ and $\chi' := \phi(\om')$. 
Suppose we are given 
$h \in \opn{G}^{\mrm{r}}(\h, R)(\chi, \chi')$;
we will find 
$g \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om')$. 
(We do not care whether $\phi(g) = h$ or not.)

Define 
$\om_j := p_j(\om)$,
$\om'_j := p_j(\om')$,
$\chi_j := p_j(\chi)$,
$\chi'_j := p_j(\chi')$
and 
$h_j := p_j(h)$. 
We will find a sequence $\{ g_j \}_{j \in \N}$ of elements 
$g_j \in  \opn{G}^{\mrm{r}}(\g, R_j)(\om_j, \om'_j)$
such that 
$\phi(g_j) = h_j$
and 
$p_{j, j-1}(g_j) = g_{j-1}$.
Then, by Lemma \ref{lem:6}(3) there is an element 
$g \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om')$
such that $p_j(g) = g_j$ for every $j$. 

We construct the sequence $\{ g_j \}_{j \in \N}$ by induction on $j$. For
$j = 0$ we take $g_0 := 1$. 
Now let $j \geq 1$, and suppose that we have a sequence 
$(g_0, \ldots, g_{j-1})$ as required. According to Lemma \ref{lem:2}, applied
to the artinian local ring $R_j$, there exists an element 
$g_j \in \opn{G}^{\mrm{r}}(\g, R_j)(\om_j, \om'_j)$
such that $p_{j, j-1}(g_j) = g_{j-1}$ and $\phi(g_j) = h_j$.

\medskip \noindent
Proof of (c). This is the complete version of the proof of Lemma \ref{lem:5}(2).
By Lemma \ref{lem:6}(1) the function 
$\mrm{H}^0(\phi_{R, \om})$ is bijective. The claim now follows from Proposition 
\ref{prop:2}.
\end{proof}

\begin{rem}
Assume $\g$ is abelian (i.e.\ the Lie bracket is zero), so that 
$\m \hot \g$ is just a complex of $R$-modules, and 
\[ \ol{\opn{MC}}(\g, R) = \mrm{H}^1 (\m \hot \g) . \]
In this case the Deligne groupoid $\mbf{Del}(\g, R)$ is the truncation 
\[ \cdots \to 0 \to \m \hot \g^0 \to 
\opn{Ker} \bigl( \d : \m \hot \g^{1} \to \m \hot \g^2 \bigr)
\to 0 \to \cdots , \]
whereas as the reduced Deligne groupoid $\mbf{Del}^{\mrm{r}}(\g, R)$
is the truncation
\[ \cdots \to 0 \to 
\opn{Im} \bigl( \d : \m \hot \g^{-1} \to \m \hot \g^0 \bigr)
\to 
\opn{Ker} \bigl( \d : \m \hot \g^{1} \to \m \hot \g^2 \bigr)
\to 0 \to \cdots , \]
both concentrated in the degree range $[0, 1]$.
Let $\h$ be another abelian DG Lie algebra. 
It is clear that a quasi-isomorphism of complexes $\phi : \g \to \h$ will
induce a quasi-isomorphism 
\[ \mbf{Del}^{\mrm{r}}(\phi, R) : 
\mbf{Del}^{\mrm{r}}(\g, R) \to \mbf{Del}^{\mrm{r}}(\h, R) . \]
This is a special case of Theorem \ref{thm:2}.
\end{rem}

\begin{rem} \label{rem:11}
Presumably Theorem \ref{thm:2} can be extended to the following more general
situation: $\g$ and $\h$ are $R$-linear DG Lie algebras, such that all the
$R$-modules $\g^i$ and $\h^i$ are $\m$-adically complete, and the graded Lie
algebras $\opn{gr}_{\m} (\g)$ and $\opn{gr}_{\m} (\h)$ are abelian. 
We are given an $R$-linear DG Lie algebra homomorphism 
$\phi : \g \to \h$ such that 
\[ \opn{gr}_{\m}(\phi) : \opn{gr}_{\m} (\g) \to \opn{gr}_{\m} (\h) \]
is a quasi-isomorphism. Then 
\[ \ol{\opn{MC}}(\phi) : \ol{\opn{MC}}(\g) \to \ol{\opn{MC}}(\h) \]
is bijective. Cf.\ \cite[Theorem 2.1]{Ge} for the corresponding nilpotent case.
\end{rem}










\section{Some Facts on $2$-Groupoids}
\label{sec:2-grpd}

Let us recall that a (strict) {\em $2$-groupoid} $\bsym{G}$ is a groupoid
enriched in the monoidal category of groupoids. Another way of saying this is
that a $2$-groupoid $\bsym{G}$ is a $2$-category in which all $1$-morphisms and
$2$-morphisms are invertible. A comprehensive review of $2$-categories and
related constructions is available in \cite[Section 1]{Ye3}. 
See also \cite{Ma, Bw, Ge}.

We wish to make things as explicit as possible, to make calculations
(both in Section \ref{sec:del-2-grpd} of this paper, and in the new
version of \cite{Ye4}) easier.
A (small strict) $2$-groupoid $\bsym{G}$ is made up of the following
ingredients: there
is a set $\opn{Ob}(\bsym{G})$, whose elements are the {\em objects}
of $\bsym{G}$. For any $x, y \in \opn{Ob}(\bsym{G})$ there is a set 
$\bsym{G}(x, y)$, whose elements are called the {\em $1$-morphisms} from $x$
to $y$. Given $f \in \bsym{G}(x, y)$, we write $f : x \to y$. 
For any $f, g \in \bsym{G}(x, y)$ there is a set 
$\bsym{G}(x, y)(f, g)$, whose elements are called the {\em $2$-morphisms} from
$f$ to $g$. For $a \in \bsym{G}(x, y)(f, g)$ we write 
$a : f \twoto g$. 

There are three types of composition operations in $\bsym{G}$. There is {\em
horizontal composition of $1$-morphisms}: given $f_1 : x_0 \to x_1$ and 
$f_2 : x_1 \to x_2$, their composition is
$f_2 \circ f_1 : x_0 \to x_2$. Suppose we are also given $1$-morphisms 
$g_i : x_{i-1} \to x_i$ and $2$-morphisms $a_i : f_i \twoto g_i$. Then there is
a $2$-morphism 
\[ a_2 \circ a_1 : f_2 \circ f_1 \twoto g_2 \circ g_1 . \]
This is {\em horizontal composition of $2$-morphisms}. 
If we are also given \lb $1$-morphisms 
$h_i : x_{i-1} \to x_i$ and $2$-morphisms $b_i : g_i \twoto h_i$,
then there is the {\em vertical composition} (of $2$-morphisms) 
$b_i \ast a_i : f_i \twoto h_i$. 
There are pretty diagrams to display all of this (see \cite[Section 1]{Ye3} or
many other references). 

For every $x \in \opn{Ob}(\bsym{G})$ there is the identity $1$-morphism 
$\bsym{1}_x : x \to x$, and for every 
$f \in \bsym{G}(x, y)$ there is the identity $2$-morphism 
$\bsym{1}_f : f \twoto f$. 

Here are the conditions required for the structure $\bsym{G}$ to be a 
$2$-groupoid: 
\begin{itemize}
\item The set $\opn{Ob}(\bsym{G})$, together with the $1$-morphisms
$f : x \to y$, horizontal composition $g \circ f$, and the identity morphisms 
$\bsym{1}_x$, is a groupoid. 
We refer to this groupoid as the $1$-truncation of $\bsym{G}$. 

\item For every $x, y \in \opn{Ob}(\bsym{G})$, the set 
$\bsym{G}(x,y)$, together with the $2$-morphisms 
$a : f \twoto g$, vertical composition
$b \ast a$, and the identity morphisms $\bsym{1}_f$, is a groupoid. We refer
to it as the vertical groupoid above $(x, y)$. 

\item Horizontal composition of $2$-morphisms is associative, 
$\bsym{1}_{g \circ f} = \bsym{1}_g \circ \bsym{1}_f$ whenever $g$ and $f$ are
composable, and the $2$-morphisms $\bsym{1}_{\bsym{1}_x}$ are identities for
horizontal composition.

\item The exchange condition: given $f_i, g_i, h_i : x_{i-1} \to x_i$,
$a_i : f_i \twoto g_i$ and $b_i : g_i \twoto h_i$, one has
\[ (b_2 \ast a_2) \circ (b_1 \ast a_1) = 
(b_2 \circ b_1) \ast (a_2 \circ a_1) , \]
as $2$-morphisms $f_2 \circ f_1 \twoto h_2 \circ h_1$.
\end{itemize}

A consequence of these four conditions is that $2$-morphisms are invertible for
horizontal composition. Indeed, given $a : f \twoto g$ in 
$\bsym{G}(x, y)$,  its horizontal inverse 
$a^{- \circ} : f^{-1} \twoto g^{-1}$ is given by the formula
$a^{- \circ} = \bsym{1}_{g^{-1}} \circ a^{- \ast} \circ \bsym{1}_{f^{-1}}$,
where 
$a^{- \ast} : g \twoto f$ is the vertical inverse of $a$. 

Suppose $\bsym{H}$ is another $2$-groupoid. A (strict) {\em $2$-functor} 
$F : \bsym{G} \to \bsym{H}$ is a collection of functions 

\[ \begin{aligned}
F & : \opn{Ob}(\bsym{G}) \to \opn{Ob}(\bsym{H})
\\
F & : \bsym{G}(x_0, x_1) \to \bsym{H} \bigl( F(x_0), F(x_1) \bigr)
\\
F & : \bsym{G}(x_0, x_1)(g_0, g_1) \to 
\bsym{H} \bigl( F(x_0), F(x_1) \bigr) \bigl( F(g_0), F(g_1) \bigr) 
\end{aligned} \]
that respect the various compositions and identity morphisms. We denote by
$\cat{2-Grpd}$ the category consisting of $2$-groupoids and $2$-functors between
them.  

Consider a $2$-groupoid $\bsym{G}$. There is an equivalence relation on the set 
$\opn{Ob}(\bsym{G})$, given by existence of $1$-morphisms, i.e.\ $x \sim y$ if 
$\bsym{G}(x, y) \neq \emptyset$. We let 
$\pi_0(\bsym{G}) := \opn{Ob}(\bsym{G}) / {\sim}$. 

For objects $x, y \in \opn{Ob}(\bsym{G})$ there is an equivalence relation on
the set $\bsym{G}(x, y)$, given by existence of $2$-morphisms:
$f \sim g$ if $\bsym{G}(x, y)(f, g) \neq \emptyset$. We let 
\[ \pi_1(\bsym{G}, x, y) := \bsym{G}(x, y) / {\sim} . \]
We define $\pi_1(\bsym{G})$ to be the  groupoid with object set
$\opn{Ob}(\bsym{G})$, \lb
morphism sets $\pi_1(\bsym{G}, x, y)$, and composition induced by horizontal
composition in $\bsym{G}$. Thus $\pi_1(\bsym{G})$ is a quotient groupoid of the
$1$-truncation of $\bsym{G}$, and \lb
$\pi_0(\pi_1(\bsym{G})) = \pi_0(\bsym{G})$.
We write $\pi_1(\bsym{G}, x) := \pi_1(\bsym{G}, x, x)$, which is a group.
We also define 
\[ \pi_2(\bsym{G}, x)  := \bsym{G}(x, x)(\bsym{1}_x, \bsym{1}_x) . \]
This is an abelian group. 

The homotopy set $\pi_0(\bsym{G})$ and groups $\pi_i(\bsym{G}, x)$ are
functorial in an obvious way. 
A morphism $F : \bsym{G} \to \bsym{H}$ in 
$\cat{2-Grpd}$ is called a {\em weak equivalence} if the functions 
\[ \begin{aligned}
\pi_0(F) & : \pi_0(\bsym{G}) \to \pi_0(\bsym{H})
\\
\pi_1(F, x) & : \pi_1(\bsym{G}, x) \to \pi_1(\bsym{H}, F(x))
\\
\pi_2(F, x) & : \pi_2(\bsym{G}, x) \to \pi_2(\bsym{H}, F(x))
\end{aligned} \]
are bijective for all $x \in \opn{Ob}(\bsym{G})$. 

It will be useful to relate the concept of $2$-groupoid to the less
familiar concept of {\em crossed module over a groupoid}, recalled below.

For a groupoid $\bsym{G}$ and an object $x \in \opn{Ob}(\bsym{G})$
we denote by $\bsym{G}(x) := \bsym{G}(x, x)$, the automorphism group of $x$. 
The composition in $\bsym{G}$ is $\circ = \circ_{\bsym{G}}$.

Let $\bsym{G}$ and $\bsym{N}$ be groupoids, such that 
$\opn{Ob}(\bsym{G}) = \opn{Ob}(\bsym{N})$. An {\em action} $\Psi$ of $\bsym{G}$
on 
$\bsym{N}$ is a collection of group isomorphisms 
\[ \Psi(g) : \bsym{N}(x) \iso \bsym{N}(y) \]
for all $x, y \in \opn{Ob}(\bsym{G})$ and $g \in \bsym{G}(x, y)$, 
such that 
\[ \Psi(h \circ g) = \Psi(h) \circ \Psi(g) \]
whenever $g$ and $h$ are composable, and 
$\Psi(\bsym{1}_x) = \bsym{1}_{\bsym{N}(x)}$.

\begin{exa}
Let $\bsym{G}$ be any groupoid. The adjoint action $\opn{Ad}_{\bsym{G}}$ of
$\bsym{G}$ on itself is defined by
\[ \opn{Ad}_{\bsym{G}}(g)(h) := g \circ h \circ g^{-1} \]
for $g \in \bsym{G}(x, y)$ and $h \in \bsym{G}(x)$.
\end{exa}

A {\em crossed module over a groupoid}, or a {\em crossed groupoid} 
for short, is data \lb
$(\bsym{G}, \bsym{N}, \Psi, \opn{D})$ consisting of:
\begin{itemize}
\item Groupoids $\bsym{G}$ and $\bsym{N}$, such that
$\bsym{N}$ is totally disconnected, and  
$\opn{Ob}(\bsym{N}) = \opn{Ob}(\bsym{G})$.

\item An action $\Psi$ of $\bsym{G}$ on $\bsym{N}$, called the {\em twisting}.

\item A morphism of groupoids (i.e.\ a functor)
$\opn{D} : \bsym{N} \to \bsym{G}$, called the {\em feedback}, which is the 
identity on objects.
\end{itemize}

These are the conditions:
\begin{enumerate}
\rmitem{i} The morphism $\opn{D}$ is $\bsym{G}$-equivariant with respect to
the actions $\Psi$ and $\opn{Ad}_{\bsym{G}}$. Namely 
\[ \opn{D}(\Psi(g)(a)) = \opn{Ad}_{\bsym{G}}(g)(\opn{D}(a)) \]
in the group $\bsym{G}(y)$, for any $x, y \in \opn{Ob}(\bsym{G})$, 
$g \in \bsym{G}(x, y)$ and $a \in \bsym{N}(x)$.

\rmitem{ii} For any $x \in \opn{Ob}(\bsym{G})$ and 
$a \in \bsym{N}(x)$ there is equality
\[ \Psi(\opn{D}(a)) = \opn{Ad}_{\bsym{N}(x)}(a) , \]
as automorphisms of the group $\bsym{N}(x)$.
\end{enumerate}

\begin{exa}
If $\bsym{G}$ and $\bsym{N}$ are groups, namely 
$\opn{Ob}(\bsym{G}) = \opn{Ob}(\bsym{N}) = \{ 0 \}$, then 
a crossed groupoid is just a crossed module.
\end{exa}

\begin{exa} \label{exa:100}
Let $G$ be a group acting on a set $X$. For $x \in X$ let $G(x)$ denote the
stabilizer of $x$. Let $\{ N_x \}_{x \in X}$ be a 
collection of groups. Assume that for every $g \in G$ and $x \in X$ there is
given a group isomorphism $\Psi(g) : N_x \iso N_{g(x)}$, and these satisfy the
functoriality conditions of an action. 
Also assume there are
group homomorphisms $\opn{D}_x : N_x \to G(x)$ such that 
\[ \opn{Ad}_{G}(g) \circ \opn{D}_x = \opn{D}_{g(x)} \circ \, \Psi(g) \]
for any $g \in G$ and $x \in X$. 

Define $\bsym{G}$ to be the transformation groupoid associated to the
action of $G$ on $X$. And define $\bsym{N}$ to be the totally
disconnected groupoid with $\opn{Ob}(\bsym{N}) := X$ and 
$\bsym{N}(x) := N_x$. Then 
$( \bsym{G}, \bsym{N}, \Psi, \opn{D})$ is a crossed
groupoid, which we call the {\em transformation crossed groupoid} associated to
the action of $G$ on $\{ N_x \}_{x \in X}$.
\end{exa}

\begin{exa}
Suppose $\bsym{G}$ is any groupoid, and $\bsym{N}$ is a {\em normal subgroupoid}
of $\bsym{G}$, in the sense of \cite{Bw, Ye4}. Let 
$\opn{D} : \bsym{N}\to \bsym{G}$ be the inclusion, and let 
$\Psi$ be the restriction of $\opn{Ad}_{G}$ to $\bsym{N}$. Then 
$(\bsym{G}, \bsym{N}, \Psi, \opn{D})$ is a crossed groupoid.
\end{exa}

It is known that crossed groupoids are the same as $2$-groupoids
(cf.\ \cite{Bw}). We will now give a precise statement of this fact. 

\begin{prop} \label{prop:102}
Let $(\bsym{H}, \bsym{N}, \Psi, \opn{D})$ 
be a crossed groupoid. Then there is a unique $2$-groupoid 
$\bsym{G}$ with these properties:
\begin{enumerate}
\rmitem{i} The $1$-truncation of $\bsym{G}$ is the same groupoid as
$\bsym{H}$. Namely $\opn{Ob}(\bsym{G}) = \opn{Ob}(\bsym{H})$,
$\bsym{G}(x, y) = \bsym{H}(x, y)$, the identity morphisms $\bsym{1}_x$ are the
same, and the horizontal composition is 
$g \circ_{\bsym{G}} f = g \circ_{\bsym{H}} f$
for $f : x \to y$ and $g : y \to z$.

\rmitem{ii} For any $f, g : x \to y$ in $\bsym{G}$ we have
\[ \bsym{G}(x, y)(f, g) = 
\{ a \in \bsym{N}(x) \mid g = f \circ_{\bsym{H}} \opn{D}(a) \} . \]
The identity morphism $\bsym{1}_f \in \bsym{G}(x, y)(f, f)$ is 
$\bsym{1}_x \in \bsym{N}(x)$.
Given $h : x \to y$, $a : f \twoto g$ and $b : g \twoto h$,
the vertical composition is 
$b \ast_{\bsym{G}} a = a \circ_{\bsym{N}} b$.

\rmitem{iii} For any $x_0, x_1, x_2 \in \opn{Ob}(\bsym{G})$, any
$f_i, g_i : x_{i-1} \to x_i$ and any
$a_i : f_i \twoto g_i$ in $\bsym{G}$, 
the horizontal composition $a_2 \circ_{\bsym{G}} a_1$ satisfies
\[ a_2 \circ_{\bsym{G}} a_1 =  
\Psi(f_1^{-1})(a_2) \circ_{\bsym{N}} a_1 . \]
\end{enumerate}

Moreover, any $2$-groupoid $\bsym{G}$ arises this way. 
\end{prop}

\begin{proof}
It is easy to verify that the conditions of a $2$-groupoid hold. 

Conversely, suppose $\bsym{G}$ is any $2$-groupoid. Define the groupoid
$\bsym{G}_1$ to be the $1$-truncation of $\bsym{G}$. 

For any $x \in \opn{Ob}(\bsym{G})$ consider the set of $2$-morphisms
\begin{equation} \label{eqn:105}
\bsym{G}_2(x) := \coprod_{g \in \bsym{G}(x, x)} 
\bsym{G}(x, x)(\bsym{1}_x, g) .
\end{equation}
This is a group under horizontal composition $\circ_{\bsym{G}}$
of $2$-morphisms, with identity element 
$\bsym{1}_{\bsym{1}_x}$. There is a group homomorphism 
$\opn{D} : \bsym{G}_2(x) \to \bsym{G}_1(x)$, defined by 
\begin{equation} \label{eqn:104}
\opn{D}(a : \bsym{1}_x \twoto g) := g  .
\end{equation}
Let $\bsym{G}_2$ be the totally disconnected groupoid with set of objects 
$\opn{Ob}(\bsym{G})$, and automorphism groups $\bsym{G}_2(x)$ as defined above.
Then $\opn{D} : \bsym{G}_2 \to \bsym{G}_1$
is a morphism of groupoids.

A $1$-morphism $f : x \to y$ in $\bsym{G}$ induces a group isomorphism 
\[ \opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}(f) : 
\bsym{G}_2(x) \to \bsym{G}_2(y) , \]
with formula
\begin{equation} \label{eqn:106}
\opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}(f)(a) := 
\bsym{1}_f \circ a \circ \bsym{1}_{f^{-1}} 
\end{equation}
for $a \in \bsym{G}_2(x)$.
It is a simple verification that
$(\bsym{G}_1, \bsym{G}_{2}, 
\opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}, \opn{D})$
is a crossed groupoid.
\end{proof}

\begin{rem}
An amusing consequence of the proof above is that the vertical
composition in a $2$-groupoid can be recovered from the horizontal
compositions.
\end{rem}

In view of Proposition \ref{prop:102}, in a $2$-groupoid $\bsym{G}$ 
we can talk about the group of $2$-morphisms 
$\bsym{G}_2(x)$ for any object $x$. There is a feedback homomorphism 
\[ \opn{D} :  \bsym{G}_2(x) \to \bsym{G}_1(x) , \]
and a twisting 
\[ \opn{Ad}(g) =  
\opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}(g) :
\bsym{G}_2(x) \to \bsym{G}_2(y)  \]
for any $g : x \to y$.
These satisfy the conditions of a crossed groupoid.
