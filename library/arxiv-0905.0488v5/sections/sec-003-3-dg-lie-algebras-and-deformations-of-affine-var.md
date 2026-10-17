---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-003-3-dg-lie-algebras-and-deformations-of-affine-var
section_title: "DG Lie Algebras and Deformations of Affine Varieties"
section_number: 3
pages: 19-21
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.972
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:defs-DG-Lie}

We now recall some facts on DG Lie algebras from \cite{Ye7, Ye9}. 

\begin{dfn} \label{dfn:220}
\begin{enumerate}
\item A DG Lie algebra 
$\g = \bigoplus_{i \in \mbb{Z}} \mfrak{g}^{i}$
is said to be of {\em quantum type} if $\g^i = 0$ for $i < -1$.

\item A {\em quasi quantum type DG Lie algebra} is a DG Lie algebra 
$\til{\mfrak{g}}$ that admits a DG Lie quasi-isomorphism
$\til{\g} \to \g$ to some quantum type DG Lie algebra $\g$.
\end{enumerate}
\end{dfn}

Fix a quasi quantum type DG Lie $\K$-algebra $\g$, and a parameter $\K$-algebra 
$(R, \m)$. There is an induced Lie $R$-algebra 
$\m \hot \g = \bigoplus_i \m \hot \g^i$.
The Lie bracket is $[-,-]$ and the differential is $\d$.
A solution $\om \in \m \hot \g^1$ of the Maurer-Cartan equation 
$\d(\om) + \smfrac{1}{2} [\om, \om] = 0$
is called an {\em MC element}, and the set of such elements is denoted by
$\opn{MC}(\m \hot \g)$.
The group $\opn{Exp}(\m \hot \g^0)$ is called the {\em gauge group}.
For $\ga \in \m \hot \g^0$ there is an affine action $\opn{af}(\ga)$ on 
the $R$-module $\m \hot \g^1$, 
namely $\opn{af}(\ga)(\om) := [\ga ,\om] - \d(\ga)$.
So for 
$g := \exp(\ga) \in \opn{Exp}(\m \hot \g^0)$
there is an affine automorphism 
$\opn{Af}(g) := \exp(\opn{af}(\ga))$ of $\m \hot \g^1$.
It is known that $\opn{Af}(g)$ preserves the set $\opn{MC}(\m \hot \g)$.
See \cite{GM}, \cite{CKTB}, \cite[Section 3]{Ye1} or \cite[Section 1]{Ye7} for
details.

Given $\om \in \opn{MC}(\m \hot \g)$ there is a square zero derivation
$\d_{\om} :=  \d + \opn{ad}(\om)$ of degree $1$ on $\m \hot \g$, and a bracket 
$[\al_1, \al_2]_{\om} := [ \d_{\om}(\al_1), \al_2 ]$
for $\al_1, \al_2 \in \m \hot \g^{-1}$ (that's not a Lie bracket in general).
Define the $R$-module
\begin{equation} \label{eqn:Lie-desc.110}
\a_{\om} := \opn{Coker}(\d_{\om} : \m \hot \g^{-2} \to 
\m \hot \g^{-1}) .
\end{equation}
By \cite[Proposition 6.6]{Ye7}, $\a_{\om}$ is an $R$-linear Lie algebra, with
bracket induced by  $[-,-]_{\om}$. And by \cite[Proposition 6.7]{Ye7},
$\a_{\om}$ is an $\m$-adically complete $R$-module (this is where we need $\g$
to be quasi quantum type!). So $\a_{\om}$ is a pronilpotent Lie algebra, and
there is an associated pronilpotent group $N_{\om} := \opn{Exp}(\a_{\om})$. 

The $R$-linear function 
$\d_{\om} : \a_{\om} \to \m \hot \g^0$
is a Lie algebra homomorphism, so it induces a group homomorphism 
\begin{equation} \label{eqn:Lie-desc.103}
\opn{D}_{\om} : N_{\om} \to \opn{Exp}(\m \hot \g^0) \ , \
\opn{D}_{\om} := \exp(\d_{\om}) .
\end{equation}
A short calculation shows that 
$\opn{af}(\d_{\om}(\al))(\om) = 0$
for any $\al \in \m \hot \g^{-1}$. The exponential of this formula is 
$\opn{Af}(\opn{D}_{\om}(a))(\om) = \om$ for any $a \in N_{\om}$.
We see that 
$\opn{D}_{\om}(a) \in \opn{Exp}(\m \hot \g^0)(\om)$,
where the latter is the stabilizer of $\om$ in the group $\opn{Exp}(\m \hot
\g^0)$.  

Now take $g \in \opn{Exp}(\m \hot \g^0)$, and let 
$\om' := \opn{Af}(g)(\om) \in \opn{MC}(\m \hot \g)$.
According to \cite[Corollary 6.9]{Ye7} there is a group isomorphism 
\begin{equation} \label{eqn:Lie-desc.104}
\opn{Ad}(g) : N_{\om} \iso N_{\om'} ,
\end{equation}
which is functorial in $g$, and the diagram 
\[ \UseTips \xymatrix @C=5ex @R=5ex {
N_{\om}
\ar[d]_{\opn{Ad}(g)}
\ar[r]^(0.34){\opn{D}_{\om}}
&
\opn{Exp}(\m \hot \g^0)
\ar[d]^{\opn{Ad}(g)}
\\
N_{\om'}
\ar[r]^(0.34){\opn{D}_{\om'}}
&
\opn{Exp}(\m \hot \g^0)
} \]
is commutative. By definition of the bracket $[-,-]_{\om}$, the adjoint
action in the Lie algebra $\a_{\om}$ is
$\opn{ad}_{\a_{\om}}(\al_1)(\al_2) = \opn{ad}(\d_{\om}(\al_1))(\al_2)$; 
hence, by exponentiating this equation, we see that conjugation in the group 
$N_{\om}$ is  
$\opn{Ad}_{N_{\om}}(a_1)(a_2) = \opn{Ad}(\opn{D}_{\om}(a_1))(a_2)$
for $a_i \in N_{\om}$.

Crossed groupoids were introduced in Definition \ref{dfn:cosim.101}.
The considerations above justify the next definition. 

\begin{dfn} \label{dfn:Lie-desc.101}
Let $\g$ be a quasi quantum type DG Lie algebra, and let $(R, \m)$ be a
parameter algebra, both over the field $\K$. The {\em Deligne crossed groupoid} 
is the crossed groupoid $\opn{Del}(\g, R)$ with these
components:
\begin{itemize}
\item The groupoid $\opn{Del}_1(\g, R)$ is the transformation groupoid 
associated to the action $\opn{Af}$ of the group $\opn{Exp}(\m \hot \g^0)$
on the set $\opn{MC}(\m \hot \g)$.
(This is the usual Deligne groupoid of $\m \hot \g$.)

\item  The groupoid $\opn{Del}_2(\g, R)$ is the totally disconnected
groupoid with set of objects $\opn{MC}(\m \hot \g)$.
For $\om \in \opn{MC}(\m \hot \g)$ its automorphism group 
in  $\opn{Del}_2(\g, R)$ is 
$N_{\om} = \opn{Exp}(\a_{\om})$, where $\a_{\om}$ is the pronilpotent Lie
algebra in
formula (\ref{eqn:Lie-desc.110}).

\item The twisting 
$\opn{Ad}_{\opn{Del}_1 \crvar \opn{Del}_2}(g)$,
for $g \in  \opn{Exp}(\m \hot \g^0)$, is the group isomorphism
$\opn{Ad}(g)$ in formula (\ref{eqn:Lie-desc.104}).

\item The feedback $\opn{D}$ is the group homomorphism in formula 
(\ref{eqn:Lie-desc.103}).
\end{itemize}
\end{dfn}

It is obvious from the construction that the crossed groupoid
 $\opn{Del}(\g, R)$ is functorial in both $\g$ and $R$. 
When $\g$ is a quantum type DG Lie algebra then 
$\a_{\om} = (\m \hot \g^{-1})_{\om}$ of course.
If $\g$ is of quantum type and $R$ is artinian, then $\opn{Del}(\g, R)$
is precisely the $2$-groupoid introduced by Deligne in \cite{De}; see also 
\cite{Ge1}.

Let $X$ be a smooth algebraic variety over $\K$. 
There are two important sheaves of DG Lie algebras on $X$: the sheaf
$\mcal{T}_{\mrm{poly}, X}$ of {\em polyderivations}, and the
sheaf $\mcal{D}_{\mrm{poly}, X}$ of {\em polydifferential operators}. 
Within $\mcal{D}_{\mrm{poly}, X}$ there is the subalgebra
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$ 
of {\em normalized polydifferential operators}. 
The sheaves $\mcal{T}_{\mrm{poly}, X}$, $\mcal{D}_{\mrm{poly}, X}$ and
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$
are quasi-coherent graded $\OX$-modules, and the inclusion 
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}} \to \mcal{D}_{\mrm{poly}, X}$
is a quasi-isomorphism. 
Full details on these DG Lie algebras can be found in \cite{Ye1, Ye2}. 
For any open set $U \subset X$ we get quantum type DG Lie algebras
$\Gamma(U, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}})$
and 
$\Gamma(U, \mcal{T}_{\mrm{poly}, X})$,
so Deligne crossed groupoids exist. 

Here is how the DG Lie algebras $\mcal{T}_{\mrm{poly}, X}$ and 
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$ control deformations of 
$\OX$. 

\begin{thm}[{Geometrization, \cite[Theorem 0.1]{Ye9}}] \label{thm:205}
Let $\K$ be a field of characteristic $0$, $X$ a smooth algebraic variety
over $\K$, $R$ a parameter algebra over $\K$, 
and $U$ an affine open set in $X$.
There are equivalences of crossed groupoids
\[  \opn{geo} : \
\opn{Del} \bigl( \Gamma(U, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}) , R \big)
\to \cat{AssDef}(R, \mcal{O}_U) \]
and
\[  \opn{geo} : \
\opn{Del} \bigl( \Gamma(U, \mcal{T}_{\mrm{poly}, X}) , R \big)
\to \cat{PoisDef}(R, \mcal{O}_U) \]
which we call {\em geometrization}. The equivalences $\opn{geo}$ 
commute with homomorphisms $R \to R'$ of parameter algebras, and with inclusions
of affine open sets $U' \to U$.
\end{thm}

The dependence of $\cat{AssDef}(R, \mcal{O}_U)$ and 
$\cat{PoisDef}(R, \mcal{O}_U)$ on $R$ and $U$ is shown in Proposition
\ref{prop:206}.  

\begin{rem} \label{rem:defs-sh.110}
Suppose $R = \K[[\hbar]]$. In our earlier
paper \cite{Ye1} we referred to an associative $R$-deformation of 
$\mcal{O}_X$ as a ``deformation quantization of $\mcal{O}_X$''. In
retrospect this name seems inappropriate,
and hence the new name used here.

Another, more substantial, change is that in 
\cite[Definition 1.6]{Ye1}
we required that the associative deformation $\mcal{A}$
shall be endowed with a differential structure. This turns out to be
redundant -- indeed, Theorem \ref{thm:205} implies that any
associative $R$-deformation $\mcal{A}$ of $\mcal{O}_X$ admits a differential
structure. Moreover, any two such differential structures are equivalent.
\end{rem}

\begin{rem} \label{rem:221}
In \cite{KS2} Kashiwara and Schapira consider associative
$\mbb{C}[[\hbar]]$-defor\-mations $\mcal{A}$ of $\OX$, for a complex manifold
$X$. Their definition is very similar to our Definition \ref{dfn:230} (for 
$R = \mbb{C}[[\hbar]]$), except that they do not require an augmentation 
$\mcal{A} \to \OX$.
\cite[Proposition 2.2.3]{KS2} is very similar to the fullness of the functor 
$\opn{geo}$ on $1$-morphisms (in the associative case of Theorem \ref{thm:205}
above). However it is not known whether $\opn{geo}$ is essentially surjective
on objects in the complex analytic setting -- this is  \cite[Remark 2.2.7]{KS2}.
\end{rem}
