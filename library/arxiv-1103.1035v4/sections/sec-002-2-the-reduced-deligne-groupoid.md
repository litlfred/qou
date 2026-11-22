---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-002-2-the-reduced-deligne-groupoid
section_title: "The Reduced Deligne Groupoid"
section_number: 2
pages: 7-10
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.958
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
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
