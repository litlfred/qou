---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-010-10-cosimplicial-formality
section_title: "Cosimplicial Formality"
section_number: 10
pages: 42-45
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.946
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:cosim-form}

In this section we prove Theorem \ref{thm:221}. We work in Setup
\ref{setup:6}.

Recall the sheaves of DG Lie algebras 
$\mcal{T}_{\mrm{poly}, X}$ and 
$\mcal{D}_{\mrm{poly}, X}$ from Section \ref{sec:defs-DG-Lie}. 
The Lie brackets are not $\mcal{O}_X$-linear (they are differential operators),
but forgetting them, both $\mcal{T}_{\mrm{poly}, X}$ and 
$\mcal{D}_{\mrm{poly}, X}$ are bounded below complexes of quasi-coherent 
$\mcal{O}_X$-modules.

The antisymmetrization homomorphism (also called the HKR map)
\begin{equation} \label{eqn:TDQ.120}
\Upsilon_1 : \mcal{T}^p_{\mrm{poly}, X} \to \mcal{D}^p_{\mrm{poly}, X}
\end{equation}
is defined as follows. For $p \geq 0$ and for local sections 
$\xi_i \in \mcal{T}^0_{\mrm{poly}, X}$ and $c_i \in \mcal{O}_X$, we let
\[ \Upsilon_1(\xi_1 \wedge \cdots \wedge \xi_{p+1})(c_1, \ldots, c_{p+1}) :=
{\smfrac{1}{(p+1)!}} \sum_{\sigma} \opn{sign}(\sigma)
\xi_{\sigma(1)}(c_1) \cdots \xi_{\sigma(p+1)}(c_{p+1}) . \]
The summation is over permutations $\sigma$ of the set
$\{ 1, \ldots, p+1 \}$. 
For $p = -1$ we let $\Upsilon_1$ be the identity map of $\mcal{O}_X$. 
According to \cite[Corollary 4.12]{Ye2} the homomorphism
$\Upsilon_1 : \mcal{T}_{\mrm{poly}, X} \to \mcal{D}_{\mrm{poly}, X}$
is a quasi-isomorphism of sheaves of $\mcal{O}_X$-modules. Note that
$\Upsilon_1$ does not respect the Lie brackets; but
$\mrm{H}(\Upsilon_1) : \mcal{T}_{\mrm{poly}, X} \to 
\opn{H} (\mcal{D}_{\mrm{poly}, X})$
is an isomorphism of sheaves of graded Lie algebras. 

Let $\mcal{G}$ and $\mcal{H}$ be sheaves of DG Lie algebras on
$X$. We denote by $\boprod^i \mcal{G}$ the $i$-fold cartesian product of the
sheaf $\mcal{G}$. An $\mrm{L}_{\infty}$ morphism
$\Psi : \mcal{G} \to \mcal{H}$ is a sequence
$\Psi = \{ \Psi_i \}_{i \geq 1}$ of $\K$-multilinear
sheaf morphisms $\Psi_i : \boprod^i \mcal{G} \to \mcal{H}$, 
such that for any open set $U$ the sequence
$\{ \Gamma(U, \Psi_i) \}_{i \geq 1}$ is an $\mrm{L}_{\infty}$ morphism
$\Gamma(U, \mcal{G}) \to \Gamma(U, \mcal{H})$. 
We say that $\Psi$ is an $\mrm{L}_{\infty}$ quasi-isomorphism if 
$\Psi_1 : \mcal{G} \to \mcal{H}$ is a quasi-isomorphism of sheaves of
$\K$-modules. See Section \ref{sec:Lie-desc} for a reminder on
$\mrm{L}_{\infty}$ morphisms.

Let $\bsym{U}$ finite affine open covering of $X$.
Recall the mixed resolution
$\opn{mix} : \mcal{M} \to \opn{Mix}_{\bsym{U}}(\mcal{M})$
of any quasi-coherent $\mcal{O}_X$-module $\mcal{M}$ 
from \cite[Section 6]{Ye1}. This is a functorial quasi-isomorphism, which is a
``mix'' of the commutative \v{C}ech resolution relative to the covering 
$\bsym{U}$, and the jet resolution (with its Grothendieck connection). 
The complex $\opn{Mix}_{\bsym{U}}(\mcal{M})$ is acyclic for the functor 
$\Gamma(V, -)$ for any affine open set $V \subset X$. 
Hence the homomorphism of cosimplicial $\K$-modules 
\[ \opn{C}(\bsym{U}, \opn{mix}) :
\opn{C}(\bsym{U}, \mcal{M}) \to 
\opn{C}(\bsym{U}, \opn{Mix}_{\bsym{U}}(\mcal{M})) \]
(cf.\ (\ref{eqn:Lie-Geo.103}))
is a cosimplicial quasi-isomorphism (i.e.\ it is a quasi-isomorphism in each
simplicial dimension).
Taking the sheaves $\mcal{T}_{\mrm{poly}, X}$ and $\mcal{D}_{\mrm{poly}, X}$,
we obtain quasi-isomorphisms of sheaves of DG Lie algebras
$\mcal{T}_{\mrm{poly}, X} \to  \opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X})$
and 
$\mcal{D}_{\mrm{poly}, X} \to  \opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})$.
See \cite[Proposition 6.3]{Ye1}.

Let $g : X' \to X$ be a morphism of varieties, $\mcal{M}$ (resp.\ 
$\mcal{M}'$) a quasi-coherent $\mcal{O}_X$-module (resp.\ 
$\mcal{O}_{X'}$-module), $\phi : \mcal{M} \to g_* (\mcal{M}')$ an 
$\mcal{O}_X$-linear map, $\bsym{U}$ (resp.\ $\bsym{U}'$) a finite affine
open covering of $X$ (resp.\ $X'$), and 
$\rho : \bsym{U}' \to \bsym{U}$ a morphism of coverings extending $g$. 
The construction of mixed resolutions (see \cite[Section 6]{Ye1} or
\cite[Section 4]{Ye3}) shows that there is an induced sheaf homomorphism 
\[ \opn{Mix}_{\rho}(\phi) : \opn{Mix}_{\bsym{U}}(\mcal{M}) \to 
g_* (\opn{Mix}_{\bsym{U}'}(\mcal{M}')) \]
on $X$. 
And of course globally there is a homomorphism of cosimplicial $\K$-modules 
\[ \opn{C}(\rho, \phi) : \opn{C}(\bsym{U}, \mcal{M}) \to
\opn{C}(\bsym{U}', \mcal{M}') . \]

Now assume $g : X' \to X$ is an \'etale morphism. Let $\mcal{G}$ denote either 
$\mcal{T}_{\mrm{poly}}$ or $\mcal{D}_{\mrm{poly}}$, so that 
$\mcal{G}_X$ is either $\mcal{T}_{\mrm{poly}, X}$ or
$\mcal{D}_{\mrm{poly}, X}$.
As we already saw in Section \ref{sec:Lie-Geo}, there is a homomorphism of 
sheaves of DG Lie algebras 
$g^* : \mcal{G}_X \to g_* (\mcal{G}_{X'})$ on $X$.  
Then there is an induced homomorphism of sheaves of DG Lie algebras
\[ \opn{Mix}_{\rho}(g^*) : \opn{Mix}_{\bsym{U}}(\mcal{G}_{X}) \to 
g_* (\opn{Mix}_{\bsym{U}'}(\mcal{G}_{X'})) \]
on $X$. Globally there is a commutative diagram of homomorphism of cosimplicial
DG Lie algebras
\begin{equation} \label{eqn:TDQ.101}
\UseTips \xymatrix @C=15ex @R=5ex {
\opn{C}(\bsym{U}, \mcal{G}_{X})
\ar[r]^{\opn{C}(\rho, g^*)}
\ar[d]_{\opn{C}(\bsym{U}, \opn{mix})}
&
\opn{C}(\bsym{U}', \mcal{G}_{X'})
\ar[d]^{\opn{C}(\bsym{U}', \opn{mix})}
\\
\opn{C} \bigl( \bsym{U}, \opn{Mix}_{\bsym{U}}(\mcal{G}_{X}) \bigr)
\ar[r]^{\opn{C}(\rho, \opn{Mix}_{\rho}(g^*))}
&
\opn{C} \bigl( \bsym{U}', \opn{Mix}_{\bsym{U}'}(\mcal{G}_{X'}) \bigr)
}
\end{equation}
where the vertical arrows are cosimplicial quasi-isomorphisms.
If $g : X' \to X$ is an isomorphism (e.g.\ $X' = X$ and 
$\bsym{U}' \to \bsym{U}$ is a refinement), then the horizontal arrows are also 
cosimplicial quasi-isomorphisms.

Let $n$ be the dimension of $X$.
An {\em \'etale coordinate system} on an open set $U \subset X$ is 
an \'etale morphism $s : U \to \mbf{A}^n_{\K}$.
Since $X$ is smooth, it is possible to find a
finite affine open covering 
$\bsym{U} = \{U_k \}_{k \in K}$, with an \'etale coordinate system
$s_k : U_k \to \mbf{A}^n_{\K}$ for each $k$. Let us write
$\bsym{s} := \{s_k \}_{k \in K}$. We refer to
$(\bsym{U}, \bsym{s})$ succinctly as a {\em covering with \'etale coordinates}.

Suppose $g : X \to X'$ is an \'etale morphism of varieties, and we are given a
covering with \'etale coordinates
$(\bsym{U}', \bsym{s}')$ of $X'$, where the indexing set is $K'$. A {\em
morphism of coverings with coordinates
extending $g$} is a function 
$\rho : K' \to K$,
such that $g(U'_{k'}) \subset U_{\rho(k')}$ and
$s_{\rho(k')} \circ g = s'_{k'}$ for every $k' \in K'$.
We refer to this morphism by 
$\rho : (\bsym{U}', \bsym{s}') \to (\bsym{U}, \bsym{s})$. 

The next result is a slight improvement of \cite[Theorem 0.2]{Ye1}. 
A similar result is \cite[Theorem 1.1]{VdB}.

\begin{thm}[Sheaf Formality] \label{thm:13}
Let $X$ be a smooth algebraic variety over $\K$, and assume $\R
\subset \K$. Let $(\bsym{U}, \bsym{s})$ be a finite affine open covering with
\'etale coordinates of $X$. Then\tup{:}
\begin{enumerate}
\item There is an $\mrm{L}_{\infty}$ quasi-isomorphism
\[ \Psi_{\bsym{s}} = \{ \Psi_{\bsym{s}; i} \}_{i \geq 1} :
\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X}) \to 
\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})  \]
between sheaves of DG Lie algebras on $X$. 

\item The diagram of isomorphisms of sheaves of graded Lie algebras 
\[ \UseTips \xymatrix @C=9ex @R=5ex {
\mcal{T}_{\mrm{poly}, X}
\ar[r]^{\mrm{H}(\Upsilon_1)}
\ar[d]_{\mrm{H}(\opn{mix})}
&
\mrm{H} (\mcal{D}_{\mrm{poly}, X})
\ar[d]^{\mrm{H}(\opn{mix})}
\\
\mrm{H} (\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X}))
\ar[r]^{\mrm{H}(\Psi_{\bsym{s}; 1})}
&
\mrm{H} (\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})) \ 
} \]
on $X$ is commutative.

\item Suppose $g : X \to X'$ is an \'etale morphism of varieties, 
$(\bsym{U}', \bsym{s}')$ is a finite affine open covering with \'etale
coordinates of $X'$, and 
$\rho : (\bsym{U}', \bsym{s}') \to (\bsym{U}, \bsym{s})$
is a morphism of coverings with coordinates extending $g$.
Then the diagram of $\mrm{L}_{\infty}$ morphisms on $X$
\[ \UseTips \xymatrix @C=9ex @R=5ex {
\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X})
\ar[r]^{\Psi_{\bsym{s}}}
\ar[d]_{\opn{Mix}_{\rho}(g^*)}
&
\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})
\ar[d]^{\opn{Mix}_{\rho}(g^*)}
\\
g_* (\opn{Mix}_{\bsym{U}'}(\mcal{T}_{\mrm{poly}, X'}))
\ar[r]^{g_*(\Psi_{\bsym{s}'})}
&
g_* (\opn{Mix}_{\bsym{U}'}(\mcal{D}_{\mrm{poly}, X'}))
} \]
is commutative. 
\end{enumerate} 
\end{thm}

\begin{proof}
Part (1) is the content of \cite[Theorem 0.2]{Ye1}, which is repeated in
greater detail (and with a correct proof) as \cite[Erratum, Theorem 1.2]{Ye1}.
Part (3) is a direct consequence of the construction of the 
 $\mrm{L}_{\infty}$ quasi-isomorphism $\Psi_{\bsym{s}}$
in the proof of \cite[Erratum, Theorem 1.2]{Ye1}.

The idea for the proof of part (2) was communicated to us by M. Van den Bergh.
Let $\mcal{M}$ be a bounded below complex of quasi-coherent
$\mcal{O}_X$-modules. For $p \geq 0$ let
\[ G^p (\opn{Mix}_{\bsym{U}}(\mcal{M})) :=
\boplus_{i \geq p} \opn{Mix}^i_{\bsym{U}}(\mcal{M}) . \]
This gives a decreasing filtration $G = \{ G^p \}_{p \geq 0}$
of $\opn{Mix}_{\bsym{U}}(\mcal{M})$
by subcomplexes. Note that 
$\opn{gr}_G^p (\opn{Mix}_{\bsym{U}}(\mcal{M})) = 
\opn{Mix}^p_{\bsym{U}}(\mcal{M})[-p]$
as complexes. 
The filtration $G$ gives rise to a convergent spectral sequence
$E_r^{p, q}(\mcal{M}) \Rightarrow 
\mrm{H}^{p+q} (\opn{Mix}_{\bsym{U}}(\mcal{M}))$,
and its first page is
\[ E_1^{p, q}(\mcal{M}) =
\mrm{H}^{p+q} \bigl( \opn{gr}_G^p (\opn{Mix}_{\bsym{U}}(\mcal{M})) \bigr)
\cong \opn{Mix}^p_{\bsym{U}}(\mrm{H}^q (\mcal{M})) . \]
The differential 
$E_1^{p, q}(\mcal{M}) \to E_1^{p+1, q}(\mcal{M})$
is the differential of the mixed resolution. 
Note that all these objects are quasi-coherent sheaves on $X$. 
Because of the quasi-isomorphism 
$\opn{mix} :   \mrm{H}^q (\mcal{M}) \to
\opn{Mix}_{\bsym{U}}(\mrm{H}^q (\mcal{M}))$
we have 
\begin{equation} \label{eqn:33}
E_2^{p, q}(\mcal{M}) \cong
\begin{cases}
\mrm{H}^q (\mcal{M}) & \text{if } p = 0 \\
0 & \text{if } p \neq 0 . 
\end{cases} 
\end{equation}
We see that the spectral sequence collapses, and 
$E_{\infty}^{p, q}(\mcal{M}) = E_2^{p, q}(\mcal{M})$.
In particular the induced filtration on the limit 
$\mrm{H}^{p+q} (\opn{Mix}_{\bsym{U}}(\mcal{M}))$
of the spectral sequence has only one nonzero jump (at level $G^0$).

According to \cite[Erratum, Theorem 1.2]{Ye1} the homomorphism of complexes
\[ \Psi_{\bsym{s}; 1} :
\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X}) \to 
\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X}) \]
respects the filtrations $G$, and for every $p$ there is equality
of homomorphisms of complexes
\begin{equation} \label{eqn:34}
\opn{gr}^p_G(\Psi_{\bsym{s}; 1})[p] = \opn{Mix}^p_{\bsym{U}}(\Upsilon_1) :
\opn{Mix}^p_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X}) \to 
\opn{Mix}^p_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X}) .
\end{equation}
Moreover, by \cite[Theorem 4.17]{Ye3}, 
$\opn{Mix}^p_{\bsym{U}}(\Upsilon_1)$ is a quasi-isomorphism.

Since $\Psi_{\bsym{s}; 1}$ respects the filtrations, there is an induced 
map of spectral sequences
$E_r^{p, q}(\Psi) : E_r^{p, q}(\mcal{T}) \to E_r^{p, q}(\mcal{D})$,
where we abbreviate 
$\mcal{T} := \mcal{T}_{\mrm{poly}, X}$ etc. 
{}From (\ref{eqn:34}) we see that there is an isomorphism in the first pages of
the spectral sequences
\[ E_1^{p, q}(\Psi) :
\opn{Mix}^p_{\bsym{U}}(\mcal{T}^q_{\mrm{poly}, X})  \cong
E_1^{p, q}(\mcal{T}) \to E_1^{p, q}(\mcal{D}) \cong
\opn{Mix}^p_{\bsym{U}}(\mrm{H}^{q}  (\mcal{D}_{\mrm{poly}, X})) . \]
Since the differentials are the same, it follows that
$E_2^{p, q}(\Psi) : E_2^{p, q}(\mcal{T}) \to E_2^{p, q}(\mcal{D})$
is an isomorphism.

Finally let's examine the diagram of isomorphisms
\[ \UseTips \xymatrix @C=9ex @R=5ex {
\mcal{T}^q_{\mrm{poly}, X}
\ar[r]^{\mrm{H}^q(\Upsilon_1)}
\ar[d]_{\alpha}
&
\mrm{H}^q (\mcal{D}_{\mrm{poly}, X})
\ar[d]^{\alpha}
\\
E_2^{0, q}(\mcal{T}) 
\ar[r]^{E_2^{0, q}(\Psi)}
\ar[d]_{\be}
&
E_2^{0, q}(\mcal{D}) 
\ar[d]^{\be}
\\
\mrm{H}^q (\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X}))
\ar[r]^{\mrm{H}^q(\Psi_{\bsym{s}; 1})}
&
\mrm{H}^q (\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})) \ .
} \]
The arrows $\al$ come from (\ref{eqn:33}); and the top square commutes
because of (\ref{eqn:34}) with $p = 0$.
The arrows $\be$ come from the collapse of the spectral sequence, and for
this reason the bottom square is commutative. So the whole diagram is
commutative.
\end{proof}

\begin{thm}[Cosimplicial Formality] \label{thm:221}
In the situation of Theorem \tup{\ref{thm:13}} there is a diagram
\[ \UseTips \xymatrix @C=12ex @R=5ex {
\mrm{C}(\bsym{U}, \mcal{T}_{\mrm{poly}, X})
\ar[d]_{\opn{C}(\bsym{U}, \opn{mix})}
&
\mrm{C}(\bsym{U}, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}})
\ar[d]^{\opn{C}(\bsym{U}, \opn{mix})}
\\
\mrm{C} \bigl( \bsym{U} , \opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X})
\bigr)
\ar[r]^{\mrm{C}(\bsym{U} , \Psi_{\bsym{s}})} 
&
\mrm{C} \bigl( \bsym{U} , \opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})
\bigr) \ ,
} \]
where the objects are cosimplicial quantum type DG Lie algebras, the
vertical arrows are cosimplicial DG Lie quasi-isomorphisms, and the arrow 
$\Psi_{\bsym{s}}$ is a cosimplicial $\mrm{L}_{\infty}$ quasi-isomorphism. 

This diagram is functorial with respect to 
\'etale morphisms $g : X' \to X$ and morphisms of coverings 
$\rho : (\bsym{U}', \bsym{s}') \to (\bsym{U}, \bsym{s})$
extending $g$, as in diagram \tup{(\ref{eqn:TDQ.101})}. 
\end{thm}

\begin{proof}
The diagram is obtained by applying the \v{C}ech cosimplicial
construction $\mrm{C}(\bsym{U} , -)$ to the  $\mrm{L}_{\infty}$
quasi-isomorphism $\Psi_{\bsym{s}}$
in  Theorem \ref{thm:13}(1), to the mixed resolutions 
$\mcal{T}_{\mrm{poly}, X} \to 
\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X})$
and 
$\mcal{D}_{\mrm{poly}, X} \to 
\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})$, 
and to the inclusion 
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}} \to 
\mcal{D}_{\mrm{poly}, X}$.

Functoriality is guaranteed by Theorem \ref{thm:13}(3), and by the 
\'etale functoriality of $\mcal{T}_{\mrm{poly}, X}$,
$\mcal{D}_{\mrm{poly}, X}$ and $\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$
from \cite[Proposition 4.6]{Ye2}.
\end{proof}
