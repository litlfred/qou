---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-011-11-twisted-quantization
section_title: "Twisted Quantization"
section_number: 11
pages: 45-48
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.978
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:TDQ}

Let $X$ be a smooth algebraic variety over $\K$, and $R$ a parameter algebra.
We have the stacks of crossed groupoids 
$\twocat{PoisDef}(R, \mcal{O}_X)$ and 
$\twocat{AssDef}(R, \mcal{O}_X)$ on $X$.
Recall that a twisted object of $\twocat{PoisDef}(R, \mcal{O}_X)$
is a twisted Poisson $R$-deformation of $\OX$, and 
a twisted object of $\twocat{AssDef}(R, \mcal{O}_X)$
is a twisted associative $R$-deformation of $\OX$.
We denote by $\ol{\opn{TwOb}}(-)$ the sets of twisted gauge equivalence classes
of twisted objects. First order brackets were defined in Definition
\ref{dfn:22}.

Here is the main result of our paper (the expanded form of Theorem
\ref{thm:14}).

\begin{thm} \label{thm:8}
Let $\K$ be a field containing the real numbers, let $R$ be a 
parameter $\K$-algebra, and let $X$ be a smooth algebraic variety over
$\K$. Then there is a bijection of sets
\[ \opn{tw{.}quant} : \
\ol{\opn{TwOb}} \bigl( \twocat{PoisDef}(R, \mcal{O}_X) \bigr) 
\ \iso \
\ol{\opn{TwOb}} \bigl( \twocat{AssDef}(R, \mcal{O}_X) \bigr) \] 
called  {\em twisted quantization}, having these
properties\tup{:}
\begin{enumerate}
\rmitem{i} If $g : X' \to X$ is an \'etale morphism of varieties, and
if $\sigma : R \to R'$ is a homomorphism of parameter algebras, then
the diagram
\[ \UseTips \xymatrix @C=9ex @R=5ex {
\ol{\opn{TwOb}} \bigl( \twocat{PoisDef}(R, \mcal{O}_X) \bigr)
\ar[r]^{\opn{tw{.}quant}}
\ar[d]_{\opn{ind}_{\sigma, g}}
& 
\ol{\opn{TwOb}} \bigl( \twocat{AssDef}(R, \mcal{O}_X) \bigr)
\ar[d]_{\opn{ind}_{\sigma, g}} 
\\
\ol{\opn{TwOb}} \bigl( \twocat{PoisDef}(R', \mcal{O}_{X'}) \bigr)
\ar[r]^{\opn{tw{.}quant}}
& 
\ol{\opn{TwOb}} \bigl( \twocat{AssDef}(R', \mcal{O}_{X'}) \bigr)
} \]
\tup{(}cf.\ Theorem \tup{\ref{thm:7})} is commutative.

\rmitem{ii} The bijection $\opn{tw{.}quant}$ preserves first order brackets.
Namely if 
$\gerbe{A}$ is a twisted Poisson $R$-deformation of
$\mcal{O}_X$, and $\gerbe{B} := \opn{tw{.}quant}(\gerbe{A})$, 
then 
\[ \{ -,- \}_{\gerbe{A}} = \{ -,- \}_{\gerbe{B}} . \]
\end{enumerate}
\end{thm}

\begin{proof}
We shall use the diagram in Figure \ref{fig:diagram}
(that appears in Subsection \ref{subsec:TDQ} of the Introduction).  
Let $(\bsym{U}, \bsym{s})$ be a finite affine open covering with \'etale
coordinates of $X$.
By Theorem \ref{thm:glu.1} and Corollary \ref{cor:4} we get the bijections
$\ol{\opn{dec}}$ in the diagram.
{}From Theorem \ref{thm:11} we get the bijections $\ol{\opn{geo}}$ in that
diagram. By applying Theorem \ref{thm:Lie-desc.101} to the diagram in Theorem 
\ref{thm:221} we obtain the bijections 
\[ \ol{\opn{mix}} := 
\ol{\opn{Desc}} (\opn{Del}) ( \mrm{C}(\bsym{U}, \opn{mix}), \bsym{1}_R) \]
and 
\[ \ol{\Psi}_{\bsym{s}} := 
\ol{\opn{Desc}} (\opn{Del}) (\mrm{C}(\bsym{U}, \Psi_{\bsym{s}}), \bsym{1}_R)
\]
in the diagram in Figure \ref{fig:diagram}.
We define $\opn{tw{.}quant}$ to be the unique bijection making this diagram
commutative. 

The whole diagram in Figure \ref{fig:diagram} is
functorial w.r.t.\ $R$ and $(\bsym{U}, \bsym{s})$; this is a consequence of
Theorems \ref{thm:7} and \ref{thm:221}.

Consider another finite affine open covering with \'etale coordinates
$(\bsym{V}, \bsym{t})$ of $X$, and a morphism of coverings with coordinates
$(\bsym{V}, \bsym{t}) \to (\bsym{U}, \bsym{s})$. 
The functoriality of the diagram in Figure \ref{fig:diagram} implies that 
the bijection $\opn{tw{.}quant}$ is the same when defined with respect 
$(\bsym{V}, \bsym{t})$.

Now suppose $(\bsym{V}, \bsym{t})$ is any finite affine open covering with
\'etale coordinates of $X$. As in the proof of Theorem \ref{thm:7}, 
we get a third covering with \'etale coordinates
$(\bsym{W}, \bsym{r})$, where 
$\bsym{W} := \bsym{U} \coprod \bsym{V}$ and  
$\bsym{r} := \bsym{s} \coprod \bsym{t}$. There are morphisms of coverings 
$(\bsym{U}, \bsym{s}) \to (\bsym{W}, \bsym{r})$
and $(\bsym{V}, \bsym{t}) \to (\bsym{W}, \bsym{r})$.
By the previous paragraph, the bijection $\opn{tw{.}quant}$ is the same when
defined with respect to any of these three coverings with \'etale coordinates.
We conclude that $\opn{tw{.}quant}$ is independent of the choices made. 

Let  $g : X' \to X$ be an \'etale morphism of varieties, and let
$\sigma : R \to R'$ be a homomorphism of parameter algebras. Choose any
morphism of coverings with coordinate 
$\rho : (\bsym{U}', \bsym{s}') \to (\bsym{U}, \bsym{s})$
extending $g$. The functoriality of the diagram in Figure \ref{fig:diagram}
implies that there is a commutative diagram as stated in property (i). 

It remains to prove that property (ii) holds. Let $\gerbe{A}$ and 
$\gerbe{B}$ be such twisted $R$-deformations. 
Consider the corresponding Lie descent data 
\[ (\om, g, a) \in 
\opn{Desc} \bigl( \opn{Del} (\mrm{C}(\bsym{U}, \mcal{T}_{\mrm{poly},X}), R)
\bigr) \]
and 
\[ (\chi, h, b) \in 
\opn{Desc} \bigl(  \opn{Del} (\mrm{C}(\bsym{U}, 
\mcal{D}^{\mrm{nor}}_{\mrm{poly},X}) , R) \bigr) . \]
They are related by the equation
\[ \begin{aligned}
& \ol{(\chi, h, b)} = \ol{\opn{Desc}} (\opn{Del})
(\mrm{C}(\bsym{U}, \Psi_{\bsym{s}}), \bsym{1}_R) ( \ol{(\om, g, a)} ) 
\\
& \qquad \qquad \qquad \in 
\ol{\opn{Desc}} \bigl(  \opn{Del}(\mrm{C} (\bsym{U}, 
\opn{Mix}_{\bsym{U}} (\mcal{D}_{\mrm{poly},X})), R) \bigr) ,
\end{aligned} \]
where $\ol{(\chi, h, b)}$ and $\ol{(\om, g, a)}$ are the equivalence classes.
We have to show that the first order brackets
$\{ -,- \}_{\gerbe{A}}$ and $\{ -,- \}_{\gerbe{B}}$ on 
$\mcal{O}_X$ are equal.

The first order brackets 
$\{ -,- \}_{\gerbe{A}}$ and $\{ -,- \}_{\gerbe{B}}$
depend only on $\om$ and $\chi$. Indeed, by Definitions \ref{dfn:22} and
\ref{dfn:20} we have
$\{ c_1, c_2 \}_{\gerbe{A}} = \{ c_1, c_2 \}_{\om}$
and 
$\{ c_1, c_2 \}_{\gerbe{B}} = \{ c_1, c_2 \}_{\chi}$
for local sections $c_1, c_2 \in \OO_X$,
where 
$\{ c_1, c_2 \}_{\om} := \psi^+(\Upsilon_1(\om)(c_1, c_2))$
and 
$\{ c_1, c_2 \}_{\chi} := \psi^+(\chi(c_1, c_2))$. 
Here $\psi^+$ is the homomorphism from equation (\ref{eqn:400}), and 
$\Upsilon_1$ is the antisymmetrization.
Property (iii) of Theorem \ref{thm:Lie-desc.101} says that
$\ol{\chi} = \ol{\opn{MC}}(\bsym{1}_R \ot \Psi_{\bsym{s}})( \ol{\om} )$
in 
\[ \ol{\opn{MC}} \bigl(\m \hot 
\mrm{C}^0(\bsym{U}, \opn{Mix}_{\bsym{U}} (\mcal{D}_{\mrm{poly},X}))  \bigr) . \]






The first order brackets are functorial in $R$, and hence
we can assume that $\m^2 = 0$, so $\m / \m^2 = \m$. 
Now the contribution of the higher order terms $\Psi_{\bsym{s}; i}$, $i \geq 2$,
to $\opn{MC}(\bsym{1}_R \ot \Psi_{\bsym{s}})$ is zero, because 
$\m^2 = 0$. Therefore the elements
$\chi$ and 
$\chi' := (\bsym{1}_R \ot \Psi_{\bsym{s}; 1})(\om)$
of 
$\m \ot \mrm{C}^0(\bsym{U}, \opn{Mix}_{\bsym{U}} (\mcal{D}_{\mrm{poly},X}))$
are gauge equivalent.
We conclude that $\{ -,- \}_{\chi} = \{ -,- \}_{\chi'}$.

A little calculation shows that the first order bracket $\{ -,- \}_{\chi'}$
depends only on the cohomology class $[\chi']$ of $\chi'$ in
$\m \ot \mrm{C}^0 \bigl( \bsym{U}, 
\mrm{H}^1 ( \opn{Mix}_{\bsym{U}} (\mcal{D}_{\mrm{poly},X})) \bigr)$;
this is a manifestation of the gauge invariance of first order brackets.
But according to Theorem \ref{thm:13}(2) we have 
$[\chi'] = [\Upsilon_1(\om)]$.
We see that $\{ -,- \}_{\chi'} = \{ -,- \}_{\om}$.
\end{proof}

\begin{cor} \label{cor:TDQ.105}
In the situation of Theorem \tup{\ref{thm:8}}, 
assume the cohomology groups 
$\mrm{H}^1(X, \mcal{O}_X)$ and $\mrm{H}^2(X, \mcal{O}_X)$ vanish. 
Then there is a bijection
\[ \begin{aligned}
& \opn{quant} : 
\frac{ \{ \tup{Poisson $R$-deformations of $\mcal{O}_X$} \} }
{\tup{ gauge equivalence}} \\
& \hspace{9ex} \iso \
\frac{ \{ \tup{associative $R$-deformations of $\mcal{O}_X$} \} }
{\tup{ gauge equivalence}} . 
\end{aligned} \] 
It preserves first order brackets, and commutes with
homomorphisms $R \to R'$ and  \'etale morphisms $X' \to X$
\tup{(}such that $X'$ also has these cohomology vanishing properties\tup{)}.
\end{cor}

\begin{proof}
Combine Theorem \ref{thm:8} and Corollary \ref{cor:7}.
\end{proof}

A {\em formal Poisson bracket} on the augmented commutative $R$-algebra 
$R \hot \OX$ is an $R$-bilinear Poisson bracket $\{ -,- \}$ that vanishes modulo
$\m$; so it makes $R \hot \OX$ into a Poisson $R$-deformation of $\OX$. 
A {\em star product} on the augmented $R$-module $R \hot \OX$ is an 
associative unital $R$-bilinear multiplication, with unit 
$1 \ot 1$, that reduces modulo $\m$ to the commutative multiplication of $\OX$;
so it makes $R \hot \OX$ into an associative $R$-deformation of $\OX$. 

By definition 
$\mcal{T}^0_{\mrm{poly},X} = \mcal{T}_X$, the sheaf of derivations, and 
$\mcal{D}^{0}_{\mrm{poly},X} = \mcal{D}_X$, the sheaf of differential operators.

\begin{cor} \label{cor:TDQ.102}
In the situation of Theorem \tup{\ref{thm:8}}, 
assume the cohomology groups 
$\mrm{H}^1(X, \mcal{O}_X)$, $\mrm{H}^2(X, \mcal{O}_X)$, 
$\mrm{H}^1(X, \mcal{T}_X)$ and $\mrm{H}^1(X, \mcal{D}_X)$
all vanish. Then there is a canonical bijection
\[ \begin{aligned}
& \opn{quant} : 
\frac{ \{ \tup{formal Poisson brackets on $R \hot \mcal{O}_X$} \} }
{\tup{ gauge equivalence}} \\
& \hspace{9ex} \iso \
\frac{ \{ \tup{star products on $R \hot \mcal{O}_X$} \} }
{\tup{ gauge equivalence}} . 
\end{aligned} \] 
It preserves first order brackets, and commutes with
homomorphisms $R \to R'$ and  \'etale morphisms $X' \to X$ 
\tup{(}such that $X'$ also has these cohomology vanishing properties\tup{)}.
\end{cor}

\begin{proof}
Theorem \ref{thm:205} implies the following: if 
$\mrm{H}^1(X, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}, 0}) = 0$, then every
associative $R$-deformation $\mcal{A}$ of $\mcal{O}_X$ is sheaf theoretically
trivial, namely there is an isomorphism $\mcal{A} \cong R \hot \mcal{O}_X$ of
sheaves of $R$-modules, that commutes with the augmentations to $\mcal{O}_X$
and preserves the units. 
The proof is the same as that of \cite[Theorem 1.13]{Ye1}, using Remark
\ref{rem:defs-sh.110}. Since there is an isomorphism of sheaves of $\K$-modules 
$\mcal{D}_X \cong \mcal{O}_X \oplus \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}, 0}$,
our assumptions imply that 
$\mrm{H}^1(X, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}, 0}) = 0$.
Hence associative deformations are the same, up to gauge equivalence, as
star products. 

Similarly, the vanishing of $\mrm{H}^1(X, \mcal{T}_X)$ implies, via 
Theorem \ref{thm:205}, that Poisson deformations are the same as formal
Poisson brackets. 

The quantization statement is now the same as in Corollary \ref{cor:TDQ.105}.
\end{proof}

\begin{exa}
The conditions of Corollary \ref{cor:TDQ.102} hold for 
$X := \mbf{P}^n_{\K}$, $n \geq 1$. Indeed, since $X$ is a $\mcal{D}$-affine
variety, we know that $\mrm{H}^i(X, \mcal{D}_X) = 0$ for all $i > 0$. 
The vanishing of $\mrm{H}^i(X, \mcal{O}_X)$ and 
$\mrm{H}^i(X, \mcal{T}_X)$ for $i > 0$ follows from 
\cite[Theorem III.5.1 and Example II.8.20.1]{Ha}. 
We thank Van den Bergh for mentioning this to us.
\end{exa}

\begin{rem}
When $X$ is an affine variety, the quantization map of Corollary
\ref{cor:TDQ.102} coincides with that of \cite[Theorem 0.1]{Ye1}. This can be
seen by looking at the construction of these quantization maps. (For 
\cite[Theorem 0.1]{Ye1} please consult the corrected proof in the Erratum.)
\end{rem}

\begin{rem} \label{rem:TDQ.101}
The reason we require that $\K$ contains $\R$ is because we rely on the
original universal $\mrm{L}_{\infty}$ formality quasi-isomorphism 
\begin{equation} \label{eqn:extras.12}
\Upsilon = \{ \Upsilon_i \}_{i \geq 1} : 
\mcal{T}_{\mrm{poly}}(\R[\bsym{t}]) \to 
\mcal{D}_{\mrm{poly}}(\R[\bsym{t}])
\end{equation}
of Kontsevich for the polynomial ring $\R[\bsym{t}] = \R[t_1, \ldots, t_n]$; see
\cite{Ko1}. However $\Upsilon$ can be replaced with any other $\mrm{L}_{\infty}$
quasi-isomorphism
$\Upsilon'$ in the proof of \cite[Theorem 0.2]{Ye1}, as long as $\Upsilon'$ has
properties (P)-(P5) of \cite{Ko1}. 

Now D.E. Tamarkin found a construction of such an $\mrm{L}_{\infty}$
quasi-isomorphism $\Upsilon'$ over $\mbb{Q}$ (see \cite{Ta}, and
\cite[Appendix]{CV} for a complete proof.)
Therefore the condition $\R \subset \K$ can in fact be removed.
\end{rem}

We end the paper with a few questions. 
A twisted $\K[[\hbar]]$-deformation $\gerbe{A}$ of $\mcal{O}_X$
is called {\em symplectic} if the first order bracket
$\{ -,- \}_{\gerbe{A}}$ is a symplectic Poisson bracket on
$\mcal{O}_X$ (cf.\ Proposition \ref{prop:20}(3)). 
This is the most noncommutative deformation possible: the center of a local
object $\mcal{A}$ of $\gerbe{A}$ is the subsheaf 
$\K[[\hbar]] \subset \mcal{A}$. 

\begin{que}
It is easy to construct an example of a {\em commutative} twisted
associative $\K[[\hbar]]$-deformation of $\mcal{O}_X$ that is
really twisted -- see Definition \ref{dfn:25} and Example \ref{exa:18}. But
does there exist a variety $X$, with  a  {\em symplectic} twisted associative
$\K[[\hbar]]$-deformation $\gerbe{A}$ of $\mcal{O}_X$ which is {\em really
twisted}? Perhaps the results of \cite{BK} can be useful here.
\end{que}

A more concrete (but perhaps much more challenging) question is:

\begin{que} \label{que:1}
Let $X$ be a Calabi-Yau surface over $\K$ (e.g.\ an abelian surface or
a K3 surface), and let
$\alpha$ be a symplectic Poisson bracket on $\mcal{O}_X$ (namely any
nonzero section of $\Gamma(X, \bwedge^{2}_{\mcal{O}_X} \mcal{T}_X)$).
Consider the Poisson $\K[[\hbar]]$-deformation 
$\mcal{A} := \mcal{O}_X[[\hbar]]$, with formal Poisson bracket
$\hbar \alpha$, and let $\gerbe{A}$ be the corresponding twisted
deformation (see Example \ref{exa:19}). 
Let $\gerbe{B} := \opn{tw{.}quant}(\gerbe{A})$. Is $\gerbe{B}$ really
twisted? 
If so, what is the significance of this phenomenon?
Note that the obstruction classes for $\gerbe{B}$
can be calculated explicitly; but these calculations look quite
complicated. 
Kontsevich [private communication] appears to think that the twisted
deformation $\gerbe{B}$ is really twisted, and he has an indirect
argument for that.
\end{que}

\begin{que}
The construction of the $\mrm{L}_{\infty}$ quasi-isomorphism 
$\Psi_{\bsym{s}}$ in Theorem \ref{thm:13} relied on the explicit universal
formality quasi-isomorphism $\Upsilon$ of Kontsevich; see (\ref{eqn:extras.12})
above. But suppose another universal formality quasi-isomorphism $\Upsilon'$
is used. Then the twisted quantization map 
$\opn{tw{.}quant}$ may change. Indeed, it is claimed by Kontsevich
\cite{Ko3} that the Grothendieck-Teichm\"uller group acts on the
quantizations by changing the formality quasi-iso\-morphism (or in
other words, the Drinfeld associator), and sometimes this action is
nontrivial. The question is: does this action change the geometric
nature of the resulting twisted associative deformation -- namely can
it change from being really twisted to being not really twisted?
\end{que}
