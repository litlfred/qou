---
doc_id: arxiv-1112.0030v2
doc_title: "Homological Algebra of Knots and BPS States"
section_id: sec-001-2-algebra-of-bps-states-and-its-representations
section_title: "Algebra of BPS states and its representations"
section_number: 2
pages: 7-10
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.971
doc_brief: "Homological Algebra of Knots and BPS States — It is known that knot homologies admit a physical description as spaces of open BPS states. We study operators and algebras acting on these spaces."
---
\label{sec:algebra}

Differentials in knot homology form a part of a larger
algebraic structure that has an elegant interpretation in the geometric / physical framework.
Because this algebraic structure has analogs in more general string / M-theory compactifications,
in this section we shall consider aspects of such structure for an arbitrary Calabi-Yau 3-fold $X$
with extra branes supported on a general Lagrangian submanifold $L \subset X$, {\it e.g.}
\bea
\text{space-time} & : & \qquad \R \times X \times M_4 \label{theoryC} \\
\text{M5-brane} & : &  \qquad \R \times L \times D \nonumber
\eea
For applications to knot homologies, one should take $X$ to be the total space of the $\CO (-1) \oplus \CO (-1)$ bundle over $\cp^1$
and $L_K$ to be the Lagrangian submanifold determined by a knot $K$ \cite{OoguriV,Taubes,Koshkin}.
Then, \eqref{theoryC} becomes precisely the setup \eqref{theoryB},
in which homological knot invariants are realized as spaces of refined BPS states, {\it cf.} \eqref{HHBPS}.

In fact, there are {\it two} spaces of BPS states relevant to this particular problem
and its variants based on a more general 3-fold $X$.
One is the space of refined {\it closed} BPS states, denoted as $\CH_{\text{BPS}}^{\text{closed}}$,
and the other is called the space of refined {\it open} BPS states, $\CH_{\text{BPS}}^{\text{open}}$.
The difference is that, while the latter contains BPS particles in the presence
of defects\footnote{M5-branes in the M-theory setup \eqref{theoryC}},
the former comprises only those BPS states which are still present in a theory when all defects are removed.
In the description~\cite{DGH} via equivariant instanton counting on a 4-manifold $M_4$,
the defect (M5-brane) corresponds to a particular ramification along the divisor $D \subset M_4$,
the so-called surface operator.

On the other hand, if one looks at the general setup \eqref{theoryC} from the vantage point
of the Calabi-Yau space $X$, then $\CH_{\text{BPS}}^{\text{closed}}$ and $\CH_{\text{BPS}}^{\text{open}}$
can be formulated in terms of enumerative invariants of $X$ and $(X,L)$ that ``count'', respectively,
closed holomorphic curves embedded in $X$
and bordered holomorphic Riemann surfaces $(\Sigma, \partial \Sigma) \hookrightarrow (X,L)$
with boundary on the Lagrangian submanifold $L$. As a way to remember this, it is convenient to keep in mind that

\medskip

\begin{itemize}

\item
$\CH_{\text{BPS}}^{\text{closed}}$ depends only on the Calabi-Yau space $X$

\bigskip

\item
$\CH_{\text{BPS}}^{\text{open}}$ depends on both the Calabi-Yau space $X$ and the Lagrangian submanifold $L \subset X$

\end{itemize}

\medskip
\noindent
In applications to knots, open (resp. closed) BPS states are represented by open (resp. closed)
membranes in the M-theory setup \eqref{theoryB} or by bound states of D0 and D2 branes in its reduction to type IIA string theory.
It is the space of open BPS states that depends on the choice of the knot $K$ and, therefore,
provides a candidate for homological knot invariant in \eqref{HHBPS}.

In general, the space of BPS states is $\Gamma \oplus \Z$-graded, where $\Gamma$ is the ``charge lattice''
and the extra $\Z$-grading comes from the (half-integer) spin of BPS states, such that $2j_3 \in \Z$.
For example, in the case of closed BPS states, the charge lattice
is usually just the cohomology lattice of the corresponding Calabi-Yau 3-fold $X$,
\be
\Gamma \; = \; H^{\text{even}} (X;\Z) \,.
\ee
In the case of open BPS states, $\Gamma$ also depends on the choice of the Lagrangian submanifold $L \subset X$.

When $X$ is the total space of the $\CO (-1) \oplus \CO (-1)$ bundle over $\cp^1$ and $L = L_K$,
as in application to knot homologies, the lattice $\Gamma$ is two-dimensional for both open and closed BPS states.
As a result, both $\CH_{\text{BPS}}^{\text{closed}}$ and $\CH_{\text{BPS}}^{\text{open}}$
are $\Z \oplus \Z \oplus \Z$-graded.
In particular, the space of open BPS states
is graded by spin $2j_3 \in \Z$ and by charge $\gamma = (n,\beta) \in \Gamma$, where the degree $\beta \in H_2 (X,L_K) \cong \Z$
is sometimes called the ``D2-brane charge'' and $n \in \Z$ is the ``D0-brane charge.''
In relation to knot homologies \eqref{HHBPS}, these become the three gradings of the theory categorifying the colored HOMFLY polynomial:
\be
\begin{array}{rcl}
``\a-\text{grading}" & = & \beta \in H_2 (X,L_K) \cong \Z \;  \\[.2cm]
``q-\text{grading}" & = & n \in \Z \;  \\[.2cm]
``t-\text{grading}" & = & 2 j_3 \in \Z
\end{array}
\label{aqtgradings}
\ee
\\

Now, let us discuss the algebraic structure that will help us understand the origin of differentials
acting on the triply-graded vector space $\CH_{\text{knot}} = \CH_{\text{BPS}}^{\text{open}}$.
The fact that $\CH_{\text{BPS}}^{\text{closed}}$ forms an algebra is well appreciated
in physics \cite{HarveyMoore} as well as in math literature \cite{KSCOHA}.
Less appreciated, however, is the fact that $\CH_{\text{BPS}}^{\text{open}}$
forms a representation of the algebra $\CH_{\text{BPS}}^{\text{closed}}$:
\be
\boxed{\phantom{\int}
\begin{array}{rcl}
\text{refined open BPS states}: &  & \CH_{\text{BPS}}^{\text{open}} \\
 & & \circlearrowleft \\
\text{refined closed BPS states}: &  & \CH_{\text{BPS}}^{\text{closed}}
\end{array}
\phantom{\int}}
\label{HHrep}
\ee
Indeed, two closed BPS states, $\CB_1$ and $\CB_2$, of charge $\gamma_1, \gamma_2 \in \Gamma$
can form a bound state, $\CB_{12}$ of charge $\gamma_1 + \gamma_2$, as a sort of ``extension'' of $\CB_1$ and $\CB_2$,
\be
0 \; \to \; \CB_2 \; \to \; \CB_{12} \; \to \; \CB_1 \; \to \; 0 \,,
\label{extBBB}
\ee
thereby defining a product on $\CH_{\text{BPS}}^{\text{closed}}$:




\be
\begin{array}{ccl}
\CH_{\text{BPS}}^{\text{closed}} \; \otimes \; \CH_{\text{BPS}}^{\text{closed}} & \longrightarrow & \CH_{\text{BPS}}^{\text{closed}} \;  \\[.4cm]
(\; \CB_1 \;, \;\; \CB_2 \;) & \mapsto & \CB_{12}
\end{array}
\label{clcl}
\ee
$$
{\,\raisebox{-.5cm}{\includegraphics[width=5cm]{closed}}\,}
$$
Similarly, a bound state of a closed BPS state $\CB_1^{\text{closed}} \in \CH_{\text{BPS}}^{\text{closed}}$
with an open BPS state $\CB_2^{\text{open}} \in \CH_{\text{BPS}}^{\text{open}}$
is another open BPS state $\CB_{12}^{\text{open}} \in \CH_{\text{BPS}}^{\text{open}}$:
\be
(\; \CB_1^{\text{closed}} \;, \;\; \CB_2^{\text{open}} \;) \quad \mapsto \quad \CB_{12}^{\text{open}}
\label{opclosed}
\ee
$$
{\,\raisebox{-.5cm}{\includegraphics[width=5cm]{open}}\,}
$$
This defines an action of the algebra of closed BPS states on the space of open BPS states.

The process of formation or fragmentation of a bound state in \eqref{clcl} and \eqref{opclosed} takes place
when the binding energy vanishes.
Since the energy of a BPS state is given by the absolute value of the central charge\footnote{The central
charge function is a linear function in the sense that $\CZ (\gamma_1 + \gamma_2) = \CZ (\gamma_1) + \CZ (\gamma_2)$,
{\it i.e.} it defines a homomorphism $\CZ \in \text{Hom} (\Gamma, \C)$.}
function $\CZ : \Gamma \to \C$ this condition can be written as
\be
\big| \CZ (\gamma_1 + \gamma_2) \big|
- \big| \CZ (\gamma_1) \big| - \big| \CZ (\gamma_2) \big| \; = \; 0
\label{binding}
\ee
for a process that involves either $\CB_{12} \to \CB_1 + \CB_2$ or its inverse $\CB_1 + \CB_2 \to \CB_{12}$.
A particular instance of the relation \eqref{binding} is when the central charge of the fragment vanishes:
\be
\CZ (\gamma_{\text{fragment}}) \; = \; 0
\ee
Then, a fragment becomes massless and potentially can bind to any other BPS state of charge $\gamma$.
When combined with \eqref{HHrep},
it implies that closed BPS states of zero mass correspond to operators
acting on the space of open BPS states $\CH_{\text{BPS}}^{\text{open}}$.
The degree of the operator is determined by the spin and charge of the corresponding BPS state, as in \eqref{aqtgradings}.

For example, when $X$ is the total space of the $\CO (-1) \oplus \CO (-1)$ bundle over $\cp^1$,
as in application to knot homologies, we have
\be
\exp (\CZ) \; = \; \a^{\beta} q^n \,,
\ee
where we used the relation \eqref{NvolCP1} between $\a$ and ${\rm Vol} (\cp^1)$.
Therefore, for special values of $\a$ and $q$ we have the following massless fragments, {\it cf.} \eqref{walltypes}:
\be
\begin{array}{lll}
\a=q^{-N} & : & \quad D2/D0 \text{ fragments} \;  \\[.1cm]
\a=q^N & : & \quad \overline{D2}/D0 \text{ fragments} \;  \\[.1cm]
q=1 & : & \quad D0 \text{ fragments}
\end{array}\label{frogtypes}
\ee
Moreover, the D2/D0 fragments obey the Fermi-Dirac statistics (see {\it e.g.} \cite{Refined,JafferisM})
and, therefore, lead to anti-commuting operators ({\it i.e.} differentials) on $\CH_{\text{BPS}}^{\text{open}}$.

To summarize, we conclude that various specializations of the parameters (stability conditions)
are accompanied by the action of commuting and anti-commuting operators on $\CH_{\text{BPS}}^{\text{open}}$.
The algebra of these operators is precisely the algebra of closed BPS states $\CH_{\text{BPS}}^{\text{closed}}$.
Mathematical candidates for the algebra of closed BPS states include variants of the Hall algebra \cite{Schiffmann},
which by definition encodes the structure of the space of extensions \eqref{extBBB}:
\be
[\CB_1] \cdot [\CB_2] \; = \; \sum_{\CB_{12}} |0 \to \CB_2 \to \CB_{12} \to \CB_1 \to 0| \; [\CB_{12}]
\ee
In the present case, the relevant algebras include the motivic Hall algebra \cite{KS1},
the cohomological Hall algebra \cite{KSCOHA},
and its various ramifications, {\it e.g.} cluster algebras.
Therefore, the problem can be approached by studying representations of these algebras, as will be described elsewhere.
