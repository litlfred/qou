---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.897
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
The {\em \KLRs}\ (sometimes called the {\em quiver Hecke algebras})  are
a family of $\mathbb Z$-graded algebras which {\em categorifies}
the negative half of a quantum group (\cite{KL09, KL11, R08}). More
precisely, if $U_q(\g)$ is a quantum group associated with a
symmetrizable Cartan datum, then there exists a  family of algebras
$\{R(n)\}_{n \in \Z_{\ge 0}}$ such that the Grothendieck group of
the direct sum $\soplus\nolimits_{n\in\Z_{\ge0}}R(n)\gproj$ of
the categories of finitely generated projective graded $R(n)$-modules
is isomorphic to the integral form
$U^-_{\A}(\g)$ of the negative half of $U_q(\g)$. Here, the
multiplication of the
Grothendieck group is given by the convolution product and
the action of $q$ is given by the
grading shift functor. Moreover, the cyclotomic
quotient $R^{\Lambda}(n)$ of $R(n)$ provides a categorification of the
integrable highest weight module $V(\Lambda)$ of $U_q(\g)$
(\cite{KK12}).

One of the motivations of these categorification theorems originated
from the so-called {\em LLT-Ariki theory}. In 1996,
Lascoux-Leclerc-Thibon (\cite{LLT}) conjectured that the irreducible
representations of Hecke algebras of type $A$ are controlled by the
upper global basis (\cite{Kas90, Kas91})
 (or dual canonical basis (\cite{Lus93}))
 of the basic representation of the quantum affine algebra $U_q(A^{(1)}_{N-1})$.
Soon after, Ariki (\cite{Ariki})  proved this conjecture by showing that the
cyclotomic quotients of affine Hecke algebras categorify the
irreducible highest weight modules over $U(A^{(1)}_{N-1})$, the
universal enveloping algebra of
 affine Kac-Moody algebra of type $A^{(1)}_{N-1}$.
 In \cite{BK09, R08}, Brundan-Kleshchev and Rouquier showed that
the affine Hecke algebra of type $A$ is isomorphic to the \KLR\ of
type A or of type $A_\infty$ up to a specialization and a
localization. Thus the \KLRs\ can be understood as a graded version
of the affine Hecke algebras of type $A$ and Kang-Kashiwara's
cyclotomic categorification theorem is a generalization of Ariki's
theorem on type $A$ and $A_\infty$ to all symmetrizable Cartan
datum.

The purpose of this paper is to show that the \KLR\ can be regarded
as a generalization of the affine Hecke algebra of type $A$ in
another context: the {\em quantum affine Schur-Weyl duality}.
In \cite{Jimbo86}, M.\ Jimbo  extended the classical
Schur-Weyl duality to the quantum case:
the duality between the
category of finite-dimensional modules over the Hecke algebra $H_q(n)$ and
the category of finite-dimensional modules over the quantum group
$U_q(\mathfrak{gl}_N)$.
In
\cite{CP96, Che, GRV94}, Chari-Pressley, Cherednik and
Ginzburg-Reshetikhin-Vasserot introduced a quantum affine version of
Schur-Weyl duality: they
defined a functor between the category of
finite-dimensional modules over the affine Hecke algebra $H_q^{\aff}(n)$
and the category of finite-dimensional
integrable modules over $\UA$.


There are two key ingredients in defining this functor: (1) the
R-matrices on the $n$-fold tensor product of the fundamental
representation $V(\varpi_1)$ which satisfy the  Yang-Baxter
equations,  (2) a set of elements in $H_q^{\aff}(n)$, called the {\em
intertwiners}, which satisfy the braid relations. Roughly speaking,
by assigning  intertwiners to  R-matrices, we obtain the quantum
affine Schur-Weyl duality functor.

Now it is quite natural to ask whether this functor can be
generalized to the case of quantum affine algebras $\uqpg$ of other
types or not.
Our answer to this question can be explained in the following way.

Let $\{V_s\}_{s\in \mathcal{S}}$ be a family of good $\uqpg$-modules
and let $J$ be a subset of $\mathcal{S}\times \C(q)^{\times}$. An
element $i \in J$ is denoted by $i=({S(i)}, X(i))$. We define a
quiver $\Gamma_J$ as follows:
\be[{1)}]
\item The set of vertices is taken to be $J$.

\item For $i,j\in  J $, let $$\Rnorm_{V_{S(i)},V_{S(j)}}\colon
(V_{S(i)})_u\tens (V_{S(j)})_v \to  (V_{S(j)})_v\tens(V_{S(i)})_u$$
be the normalized R-matrix. We put $d$ many arrows from $i$ to $j$
where $d$ is the order of poles of $\Rnorm_{V_{S(i)},V_{S(j)}}(v/u)$
at $v/u=X(j)/X(i)$.
\ee

\noi Then the quiver $\Gamma_J$ defines a Cartan datum
$(A=(a_{ij})_{i,j \in J}, P, \Pi, P^{\vee}, \Pi^{\vee})$, where $A$
is determined by \eqref{eq:quiver}. Hence we obtain a
Khovanov-Lauda-Rouquier algebra $R^J(\beta)$ $(\beta \in \rtl^+)$
with the parameters  $Q_{i,j}(u,v) =\delta(i\not=j)
(u-v)^{d_{ij}}(v-u)^{d_{ji}} \in \cor[u,v]$. Here,
$\rtl^+=\sum_{i\in J} \Z_{\ge 0} \alpha_i$ denotes the positive root
lattice.


Let $\beta = \sum_{i \in J} k_i \alpha_i \in \rtl^{+}$ with
$|\beta|:=\sum_{i \in J} k_i =n$ and let $J^{\beta} = \{ \nu =
(\nu_1, \ldots, \nu_n) \in J^n \,;\, \alpha_{\nu_1} + \cdots +
\alpha_{\nu_n} = \beta \}$. For each sequence
$\nu=(\nu_1,\ldots,\nu_n) \in J^{\beta}$, set
$$V_\nu = (V_{S(\nu_1)})_{\rm aff} \otimes \cdots \otimes (V_{S(\nu_n)})_{\rm aff}$$
and let $\widehat{V}^{\otimes \beta}$ be a certain completion of
$\soplus_{\nu \in J^{\beta}} V_{\nu}$. Then $\widehat{V}^{\otimes
\beta}$ is endowed with a structure of $(U'_q(\g),
R^J(\beta))$-bimodule. Hence we can define a functor
$$\mathcal{F}_{\beta} \colon  \Modg(R^J(\beta)) \rightarrow \Mod(U'_q(\g)) $$
by
$$M \longmapsto \widehat{V}^{\otimes \beta}  \otimes_{R^J(\beta)} M,$$
where $\Modg(R^J(\beta))$ denotes the category of graded
$R^J(\beta)$-modules and $\Mod(U'_q(\g))$ denotes the category of
$U'_q(\g)$-modules. We would like to emphasize that, in general, the
type of the quiver $\Gamma_J$ is  irrelevant to  the type of
the affine Lie algebra $\g$ or its underlying finite-dimensional
simple Lie algebra $\g_0$.

We denote by $R^{J}(\beta)\gmod$  the category of finite-dimensional
graded $R^{J}(\beta)$-modules and set $R^{J}\gmod = \soplus_{\beta
\in \rtl^{+}} R^{J}(\beta)\gmod$. We also denote by $\CC_{\g}$ the
category of finite-dimensional integrable $U'_q(\g)$-modules.

The functor $\mathcal F_{\beta}$ enjoys two important properties:

\begin{itemize}
\item[(1)] $\F:=\soplus_{\beta \in \rtl^{+}}\F_{\beta}$ is a tensor functor; i.e.,
$\F$ sends a convolution product of objects in $R^{J}\gmod$ to a
tensor product of $\uqpg$-modules in $\CC_{\g}$.

\item[(2)] $\mathcal F_{\beta}$ is exact if $R^J(\beta)$ is of finite type $A,D,E$.
\end{itemize}

\vskip1em


One of the most important features of the functor $\mathcal F$ is that the category $R^{J}\gmod$, domain of the functor, has a $\Z$-grading.
For many years, it has been asked if the category  $\CC_{\g}$, the codomain of $\mathcal F$, has a $\Z$-grading or not.
This question has arisen after the works of Varagnolo-Vasserot \cite{VV02}, Nakajima \cite{Nak04} and Hernandez \cite{Her04},
in which it was shown that the Grothendieck ring $K(\CC_{\g})$ of $\CC_{\g}$  has interesting $t$-deformations. In particular, Nakajima provided an algorithm of calculating  {\em $q$-characters} of simple representations \cite{Nak04} using $t$-deformation.
Thus one would expect that there might be a $\Z$-graded tensor category whose Grothendieck ring is isomorphic to one of such  $t$-deformations of $K(\CC_{\g})$.
We will see in the last half of this paper that the functor $\mathcal F$ helps us construct such a category  in type $A_{N-1}^{(1)}$ case.


 Precisely speaking, this is  the case when $J=\set{(V(\varpi_1), q^{2i})}{i\in \Z}$,
where $V(\varpi_1)$ is the fundamental representation of
$\UA$ of weight $\varpi_1$. Then, by the construction, the
corresponding \KLR\  is of type $A_\infty$ and the functor
$\F_{n}:=\soplus_{|\beta|=n} \F_{\beta}$ recovers the quantum affine
Schur-Weyl duality functor if  we identify the objects in
$R^{J}(n)\gmod:= \soplus_{|\beta|=n} R^{J}(\beta)\gmod$ with
finite-dimensional  $H_q^{\rm aff}(n)$-modules in an appropriate way
(\cite{Kim12, R08}).


 Let $\As = R^{J}\gmod$ and let ${\mathcal C}_{J}$ be the full
subcategory of $\CC_{\g}$ consisting of $\UA$-modules $M$ such that
every composition factor of $M$ appears as a composition factor of a
tensor product of modules of the form $V(\varpi_1)_{q^{2s}}$ $(s \in
\Z)$. Then ${\mathcal C}_{J}$ is an abelian category and is stable
under taking submodules, quotients, extensions and tensor products.
Moreover, ${\mathcal C}_{J}$ contains all the modules of the form
$V(\varpi_i)_{(-q)^{s}}$ for $1 \le i \le N-1$ and $s \in i-1+2\Z$
(see \S\;\ref{subsec:CJ}). Then  $\F$ restricts to a functor from
$\As$ to $\mathcal C_J$.





Next,  we construct a tensor category $\T_J$
in two steps.
 Let $\Ss$ be the kernel of the functor $\F$.
Then $\Ss$ is a \ Serre subcategory of $\AA$. 
 The quotient category $\As/\Ss$
has a structure of a tensor category  with the convolution as tensor product.
Secondly, we localize the category $\AA
/\Ss$ one step further to obtain a category $\T_J$, where the
$R^J$-modules mapped  to  the trivial representations of $\UA$
 by $\F$  are  isomorphic to the unit object in $\T_J$.
 We then show that the category $\T_J$ is an abelian
rigid tensor category; i.e., every object in $\T_J$ has a right dual
and a left dual. To prove our assertions, we develop a general
process of localization of tensor categories through a {\em
commuting family of central objects}.  We summarize this process in
 Appendix A.


Moreover, the functor  $\mathcal F\col \As\to\mathcal C_J$
factors through the category $\T_J$. Hence, roughly speaking, $\T_J$
can be regarded as a graded version of $\mathcal C_J$. Note that the
category $\T_J$ is $\Z$-graded (i.e., endowed with a grading shift
functor), while the category $\mathcal C_J$ is not. Thus the
structure of the category $\T_J$ is definitely richer than that of
$\mathcal C_J$.

 One of our main results is  that $\mathcal F$ induces  a ring isomorphism
between $K(\T_J)_{q=1}$, the Grothendieck ring of $\T_J$ forgetting
the grading and  the Grothendieck ring $K(\mathcal C_J)$ of the
category $\mathcal C_J$.  
 Indeed, as proved in Theorem~\ref{th:def},
$K(\T_J)$ is isomorphic to the $t$-deformation $\mathcal K_t$ of 
$K(\mathcal C_J)$ introduced by Hernandez-Leclerc in \cite{HL11}
(cf.\ \cite{VV02, Nak04, Her04}). 
Therefore $\T_J$ provides a
$\Z$-graded lifting of ${\mathcal C}_{J}$ as a rigid
tensor category.


As we have seen so far, even the simplest case yields many
interesting and deep applications of the functor $\mathcal F$. We
expect  that a lot more exciting developments will follow as
we take various choices of  the affine algebra $\g$  and $J$.


This paper is organized as follows. In the first section, we recall
the notions of quantum groups and \KLRs.\ Next, we introduce the
R-matrices for \KLRs\ and study their basic properties. In the
second section, we recall the quantum affine algebras and their
representation theory. The notion of normalized R-matrices are also
recalled. In the third section, we define an $(R^J(\beta)),\uqpg
)$-bimodule $\widehat{V}^{\otimes \beta}$ and a functor $\F_{\beta}$
between the category of graded $R^J(\beta)$-modules and the category
of $\uqpg$-modules. In the last section, we construct a category
$\T_J$ and investigate its fundamental properties. In the
appendices, we gather necessary lemmas and propositions on the
localization of tensor categories and the quotient categories of an
abelian category by a Serre subcategory.

\smallskip


\noi
{\bf Acknowledgements.} We would like to express our gratitude to
Bernard Leclerc for his kind explanations of his works
and many fruitful discussions.
The first and the third author gratefully acknowledge
the hospitality of RIMS (Kyoto)
 during their visit in 2011 and 2012.
