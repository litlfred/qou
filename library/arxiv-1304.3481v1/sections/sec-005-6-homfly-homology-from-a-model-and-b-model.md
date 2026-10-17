---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-graded colored homology of knots Eugene Gorsky, Sergei Gukov, and Marko Stoˇsi´c"
section_id: sec-005-6-homfly-homology-from-a-model-and-b-model
section_title: "HOMFLY homology from A-model and B-model"
section_number: 6
pages: 55-68
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.983
---
\label{sec:mirror}

In this section, we wish to look for geometric and physical models for colored HOMFLY homology,
eventually formulating it in the language of symplectic geometry or the so-called A-model.

Indeed, in mirror symmetry, the so-called B-model is famous for its formulation in the language of
complex (algebraic) geometry, while the A-model side involves symplectic invariants, Fukaya category, and quantum cohomology \cite{KontsevichHMS}.
Clearly, the algebraic model described in the previous section is closer to the B-model, and therefore
it will be our natural starting point here.
Then, we will relate it to various problems --- that are interesting in their own right --- in mirror symmetry and in symplectic geometry.
We will give several reformulations, in terms of A-model and B-model, open and closed ({\it i.e.} with and without D-branes),
in all of which colored HOMFLY homology will be realized as cohomology of a suitable BRST operator $Q$, such that $Q^2 = 0$:
\be
\CH^{\lambda} (K) \quad = \quad  Q\text{-cohomology} \,.
\ee
In physics literature, $Q$ is often called ``supercharge'' and
its cohomology is often called the {\it space of BPS states} since its elements
are the so-called BPS states (= supersymmetric configurations).
Even though precisely this interpretation of knot homology was proposed in \cite{GSV} and studied from various
vantage points in \cite{AShakirov,DGH,GukovRTN,IK,fiveknots}, the A-model and B-model reformulations discussed here
appear to be completely new and do not make direct contact with any of the existent geometric / physical models of knot homologies.
Therefore, by pursuing some of these new geometric descriptions further one is likely to learn a lot about colored HOMFLY homology and, possibly, even about homological mirror symmetry.




\subsection{B-model on a supermanifold}
\label{sec:Bmodel}

With this goal in mind, we start by reformulating the Conjectures \ref{symmetric torus unreduced} and \ref{symmetric torus reduced}
in terms of B-model on a super-manifold $\C^{d|d}$ with a certain Landau-Ginzburg potential $W_{super} (K; \lambda)$, such that
\be
\CH^{\lambda} (K) \; \cong \; Jac (W_{super} (K;\lambda))
\label{HasJac}
\ee
Note, that $\C^{d|d}$ is a super-Calabi-Yau manifold (see \cite{AVsuper,Schwarz,Wtwistor}).

Specifically, consider the potential $W (T(p,q); S^r)$ on the $u$-space given by the formula
\be
W (T(p,q); S^r) =\Coef_{(p+q)r+1}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q+p}{p}}.
\label{WTpqr}
\ee
Let us rename $du_i$ by $\xi_i$ and introduce a potential $W_{super} (T(p,q); S^r)$ on the superspace $\C^{pr|pr}$
with coordinates $u_i,\xi_i$ by the formula
\be
W_{super} (T(p,q); S^r) :=\sum_{i}\frac{\partial W}{\partial u_{i}}\xi_{i} \,.
\label{WsuperTpqr}
\ee
The space of differential forms $\Omega^{\bullet}\left(\overline{\CM}_{p,q}(r)\right)$ is isomorphic to the Jacobi ring of $W_{super} (T(p,q); S^r)$:
\begin{equation}
\label{W super}
\Omega\left[\overline{\CM}_{p,q}(r)\right]=\C[u_1,\ldots,u_{pr},\xi_1,\ldots,\xi_{pr}]/\left(\frac{\partial W_{super}}{\partial u_{i}},\frac{\partial W_{super}}{\partial \xi_{i}}\right).
\end{equation}
According to the Conjecture \ref{symmetric torus unreduced}, both spaces represent the unreduced $S^r$-colored homology of the $(p,q)$ torus knot. Indeed, the partial derivatives of $W (T(p,q); S^r)$ are equal to
$$\frac{\partial W (T(p,q); S^r)}{\partial u_{i}}
=\Coef_{(p+q)r+1}\frac{\partial}{\partial u_{i}}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q+p}{p}}=$$
$$\frac{q+p}{p}\Coef_{(p+q)r}\left[z^{i}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q}{p}}\right]=$$
$$\frac{q+p}{p}\Coef_{(p+q)r+1-i}(1+u_1z+\ldots+u_{pr}z^{pr})^{\frac{q}{p}},\ i=1\ldots pr.$$
Therefore the ring of functions on $\overline{\CM}_{p,q}(r)$ coincides with the Jacobi ring of $W$:
\begin{equation}
\C\left[\overline{\CM}_{p,q}(r)\right]=\C[u_1,\ldots,u_{pr}]/\left(\frac{\partial W}{\partial u_{i}}\right).
\end{equation}

The full space of differential forms $\Omega^{\bullet}\left(\overline{\CM}_{p,q}(r)\right)$ is a quotient of the space 
of all differential forms on $\C^{pr}$ by the equations
\begin{equation}
\label{forms eq}
\frac{\partial W}{\partial u_{i}}=0,\quad \sum_{j}\frac{\partial^2 W}{\partial u_{i}\partial u_j}\cdot du_{j}=0.
\end{equation}
The Jacobi ring of $W_{super}$ is defined by the following equations:
$$\frac{\partial W_{super}}{\partial \xi_{i}}=\frac{\partial W}{\partial u_{i}}=0$$
$$\frac{\partial W_{super}}{\partial u_{i}}=\sum_{j}\frac{\partial^2 W}{\partial u_{j}\partial u_{i}}\xi_{j}=0.$$
Since these equations coincide with (\ref{forms eq}), we get the relation (\ref{W super}).

In the mirror symmetry literature \cite{Schwarz,Sethi,AVsuper,Katzarkov},
the setup we just described is called a Landau-Ginzburg B-model with target space $\C^{d|d}$
and superpotential $W_{super} (K;\lambda)$. The function $W_{super} (K;\lambda)$ is called
{\it superpotential} even when the target space is an ordinary (bosonic) manifold,
{\it e.g.} $W(u_i)$ in our discussion might be called superpotential of a Landau-Ginzburg model on $\C^{pr}$.
As a final clarification of terminology, we should mention that a model is called {\it Landau-Ginzburg model}
when the superpotential is non-zero, and is referred to as the {\it sigma-model} (on a certain target manifold) when $W=0$.

In our case, the colored HOMFLY homology (of torus knots) is realized as the Jacobi ring\footnote{also known as
the ``chiral ring'' or ``ring of observables,'' see below} \eqref{HasJac} - \eqref{W super}
of a Landau-Ginzburg model on $\C^{pr|pr}$ with the superpotential $W_{super} (T(p,q); S^r)$.
There are several aspects of this B-model that make it rather special and interesting,
the main of which is undoubtedly the fact that the target space $\C^{pr|pr}$ is a supermanifold.

It is instructive, though, to start with a more familiar and conventional B-model with a target space $X$.
Then, we will extend it to a Landau-Ginzburg model with a superpotential $W$ and will see
why \eqref{HasJac} - \eqref{W super} can be interpreted as a ring of observables with and without D-branes
(called B-branes in the context of the B-model).
In general, we shall use $X$ for the target space of the B-model and $Y$ for the target space of the $A$-model,
so that $X$ and $Y$ are mirror manifolds in most of our applications.

First, as a warm-up and a lightning review of the relevant facts about B-model, let us consider
a B-model with target space $X$.
The space of observables --- or, to be more precise, the space of {\it closed (string) observables} ---
in such model is then identified with the $\bar \p$-cohomology of $X$ with values in $\bigwedge^p T_{X}$:
\be
\label{hom of polyvectors}
H^q \left( X, \bigwedge^p T^{1,0}_{X} \right)
\ee
Indeed, every $(0,q)$-form on $X$ with values in $\bigwedge^p T_{X}$
\be
A = d \bar z^{\bar k_1} \ldots d \bar z^{\bar k_q}
A^{j_1 \ldots j_p}_{\bar k_1 \ldots \bar k_q} \frac{\p}{\p z_{j_1}} \ldots \frac{\p}{\p z_{j_p}}
\ee
in the topological B-model defines an observable:
\be
\CO_A = \eta^{\bar k_1} \ldots \eta^{\bar k_q} A^{j_1 \ldots j_p}_{\bar k_1 \ldots \bar k_q} \theta_{j_1} \ldots \theta_{j_p}
\ee
Contracting this ``$(-p,q)$-form'' with the holomorphic $(n,0)$-form $\Omega$ on $X$ we obtain an isomorphism
between this space and $(n-p,q)$-forms, where $n$ is the total (complex) dimension of $X$.
Moreover, $\{ Q, \CO_A \} = - \CO_{\bar \p A}$, so that observables in the B-model are Dolbeault cohomology
of forms valued in exterior powers of the holomorphic tangent bundle, {\it i.e.} elements of \eqref{hom of polyvectors}.

Incorporating a superpotential $W \ne 0$ leads to a Landau-Ginzburg model where
the $Q$-operator acts as a differential $Q = \bar \p + Q_{\text{bdry}}$, such that
\be
Q^2 = W \cdot \text{id}
\ee
As a result, the space of closed string states in the Landau-Ginzburg model can be described
as a Hochschild homology or, equivalently, as a hypercohomology:
\be
HH_* (MF (X, W)) \cong \mathbb{H}^* (\Lambda^* \Omega_{X}, dW \wedge)
\ee
where $\Lambda^* \Omega_{X}$ denotes the exterior powers of the sheaf of differential forms.
The dual cohomology theory is
\be
HH^* (MF (X, W)) \cong \mathbb{H}^* (\Lambda^* T_{X}, [W, - ])
\ee
where $\Lambda^* T_{X}$ denotes exterior powers of the tangent sheaf and $[W, - ]$ denotes the Lie bracket with $W$.
In particular, if $f_1, \ldots, f_n$ are sections of line bundles $\CE_i$ on a smooth variety $V$,
then they define a function $W: \text{Tot} (\oplus \CE_i^*) \to \C$ and we have the following equivalence
of categories\footnote{The analogous statement for the topological A-model is:
$$
Fuk (Y,W) \cong Fuk (Sing (W)) \,.
$$}
\be
MF (\text{Tot} (\oplus \CE_i^*), W) \cong QCoh ( \{ f_i = 0 \} )
\ee
that allows to describe B-branes in a Landau-Ginzburg theory with the superpotential $W$
({\it i.e.} objects in the category of matrix factorizations of $W$)
in terms of the category of coherent sheaves on the critical variety of $W$.

\begin{theorem}[\cite{Orlov}]
\be
H^0 (MF (W)) \cong \CD^b_{sing} (W^{-1} (0))
\ee
\end{theorem}

Note, this brings us very close to our applications \eqref{HMunreduced} and \eqref{HMreduced},
where the moduli spaces $\overline{\CM}_{p,q}(r)$ and $\CM_{p,q}(r)$
are defined by polynomial equations $f_i (u_j) = 0$ in the space $X = \C^{pr}$ of $u$'s.
In situations like this, when the equations $f_i (u_j) = 0$ integrate to a superpotential $W (u_j)$
the chiral ring (also known as the $(c,c)$ ring) of the Landau-Ginzburg model on $X = \C^n$
is isomorphic to the quotient of the ring of polynomial functions $\C[u_1, ... , u_n]$ by $dW$,
\be
\CR_{\text{closed}} (\C^n, W) \; = \; \C [u_i] / (dW)
\label{Rclosed}
\ee
When $W$ is quasihomogeneous, this ring is graded by the R-charge symmetry $U(1)_R$.

In order to interpret the colored HOMFLY homology, though,
in the Landau-Ginzburg model we need not only to find a natural home for the moduli spaces
$\overline{\CM}_{p,q}(r)$ and $\CM_{p,q}(r)$
but also to describe the corresponding spaces of differential forms \eqref{HMunreduced} and \eqref{HMreduced} in the B-model language.
One way to do this is to replace the target space $\C^n$ by the supermanifold $X = \C^{n|n}$
and to replace the superpotential $W(u_i)$ by $W_{super} (u_i, \xi_i)$ defined in \eqref{WsuperTpqr}.
This gives then
\be
\CR_{\text{closed}} (\C^{n|n}, W_{super}) \; = \; \Omega^* (\CM)
\ee
where $\CM = \{ u \in \C \vert f_i (u) \equiv \p_i W (u) = 0 \}$.
Specifically, for the superpotential $W_{super}$ defined by \eqref{WTpqr} and \eqref{WsuperTpqr}
we get a B-model realization of the $S^r$-colored HOMFLY homology of torus knots.
For instance, from \eqref{s2 colored trefoil}, \eqref{tref3876}, and \eqref{knot34829054}
we find the following potentials in simple examples considered earlier:
$$W (3_1; \tableau1)=u_2^3,$$
$$W_{super} (3_1; \tableau1)=3u_2^2\xi_2,$$
$$W (8_{19}; \tableau1)=-\frac{7 u_2^4}{243} + \frac{14 u_2 u_3^2}{27},$$
$$W_{super} (8_{19}; \tableau1) = \left(-\frac{28 u_2^3}{243} + \frac{14 u_3^2}{27}\right) \xi_2+\frac{28 u_2 u_3}{27} \xi_3,$$
$$W (3_1; \tableau2)=\frac{5}{256}u_3 (3 u_2^4 - 8 u_2 u_3^2 - 24 u_2^2 u_4 + 48 u_4^2).$$


\vskip 0.25cm


Although conceptually this Landau-Ginzburg model should be the effective two-dimensional $\CN=2$ theory
on $D$ in the brane construction \eqref{theoryB} studied in \cite{DGH,FGS2,FGSS},
the setup appears to be surprisingly different.
Yet, in both cases, the Poincar\'e polynomial of the colored HOMFLY homology is realized as
a supersymmetric index (character) of the two-dimensional $\CN=2$ theory on $D$.
One important difference is that here we have a different 2d $\CN=2$ theory for each particular value of the color,
whereas in loc. cit. a single 2d $\CN=2$ theory determines $S^r$-colored superpolynomials for all values of $r$.
It would be interesting to understand better how the new Landau-Ginzburg realization of the colored HOMFLY homology
discussed here relates to the 2d $\CN=2$ theory on $D$ studied in \cite{DGH,FGS2,FGSS}.


\subsection{B-branes and open B-model}

There is another way, however, to describe the space of differential forms that is familiar to practitioners of mirror symmetry.
This will require introducing one more ingredient in our story, namely D-branes, and considering the space of open string states,
{\it i.e.} the states of open strings stretched between branes.
In the context of topological B-model branes are usually called B-branes.
Mathematically, B-branes are objects of the derived category of coherent sheaves $\CD^b (X)$ in the case of the sigma-model (when $W=0$),
or the category of matrix factorizations $MF (X, W)$ in the case of Landau-Ginzburg model with the target space $X$ and superpotential $W$.
We already saw both of these categories in our previous discussion and now we will spend more time discussing their objects, or B-branes.

Note that both the derived category of coherent sheaves and the category of matrix factorizations
are also familiar to practitioners of knot homology: these categories play a key role
in the constructions of {\it e.g.} \cite{CKamnitzer,KRa,KRb,Webster,Wu,Yonezawa}.

Now, let us describe the ``open'' analogue of \eqref{hom of polyvectors} and \eqref{Rclosed},
{\it i.e.} the space of states of open strings ending on a brane $\CB$ in the B-model,
starting with the sigma-model on $X$ (with $W=0$), as we did in our previous discussion,
and then extend it to branes in more general Landau-Ginzburg models.
In both cases, the conclusion will be that open strings ending on $\CB$ form an algebra, which is the Ext algebra\footnote{The algebra structure comes from the Yoneda product on the self-Ext groups.}
\be
\CR_{\text{open}} (\CB) \; = \; \Ext^* (\CB,\CB) \,.
\label{Ropen}
\ee
In order to see how it comes about, let us first consider two different branes, $\CB_1$ and $\CB_2$,
represented by shaves $\CE$ and $\CF$ supported on $S \subset X$.
Then, states of open strings stretched between $\CB_1$ and $\CB_2$ are elements of
\be
\label{homs of tensor prod}
H^q \left( S , \CE^{\vee} \otimes \CF \otimes \bigwedge^p \CN_{S/ X} \right)
\ee
There is a spectral sequence with \eqref{homs of tensor prod} as the second page that converges to \cite{Sharpe}:
\be
\Ext^{p+q}_{X} (\CE, \CF)
\ee
and in many cases one has
\be
\Ext^{n}_{X} (\CE, \CF) \; \cong \;
\bigoplus_{p+q=n} H^q \left( S , \CE^{\vee} \otimes \CF \otimes \bigwedge^p \CN_{S/ X} \right)
\ee
because the spectral sequence degenerates at $E_2$.



Now let us see how the boundary chiral ring \eqref{Ropen} can help us to produce
yet another interpretation of \eqref{HMunreduced} and \eqref{HMreduced} in {\it open} B-model.
The simplest example is the unknot colored by $\lambda = S^r$, whose HOMFLY homology
$\overline{\CH}^{S^r} (\unknot)$ is realized as the space of differential forms on
$V = \Spec\C[u_1,\ldots,u_r]$.
The corresponding choice of B-brane is closely related to SYZ brane \cite{SYZ} that plays an important role in mirror symmetry.
Namely, it is well known that for a ``zero-brane'' ({\it i.e.} a skyscraper sheaf $\CO_p$)
supported at a smooth point on a manifold $X$ of complex dimension $r$ the open string algebra \eqref{Ropen}
is the exterior algebra
\be
\Ext^* (\CO_p , \CO_p) \; \cong \; \Lambda^* (V)
\ee
where $V = T_p X  \cong  \Lambda^* \C^r$.
In order to upgrade $\Lambda^* (V)$ to the space of differential forms
$\Omega^* (V) = \C [V] \otimes \Lambda (V^{\vee})$,
one simply needs to replace $X \cong \C^r$ by its complexification $X_{\C} \cong X \times X$,
and consider a B-brane $\CB = \CO_{\Delta}$, where $\Delta \cong \C^r$
is the diagonal in $X \times X \cong \C^r \times \C^r$.
Note, the new target space $X \times X \cong \C^{2r}$
can be viewed as a SYZ torus fibration with a singular fiber at the origin.
To facilitate a discussion of the mirror A-model that will follow next,
it is convenient to replace $X = \C^r$ by $X = (\C^*)^r$.
Then, the target space $X \times X \cong (\C^*)^{2r}$ is also a $T^{2r}$
fibration, but without singular fibers and one has
\be
\CR_{\text{open}} (\CB) \; = \; \Ext^* (\CO_\Delta,\CO_\Delta) \; \cong \; \C [u_i^{\pm 1} , du_i]
\label{openDD}
\ee
Before we proceed to the mirror A-model, let us briefly discuss another interesting feature of this example.



Note that \eqref{openDD} can be identified with $HH^* (\CD^b (X)) \cong \C [u_i^{\pm 1} , du_i]$
which, according to our previous discussion, describes {\it closed} string states, not {\it open}.
This is an illustration of a more general phenomenon:
open string states \eqref{Ropen} of a B-brane supported on the diagonal $\Delta \subset X \times X$
can be identified with the closed string states \eqref{hom of polyvectors} of a B-model on $X$.
The mathematical content of this statement is summarized in the following:

\begin{theorem}[Hochschild-Kostant-Rosenberg isomorphism \cite{HKR}]
\be
\Ext^{n}_{X \times X} (\CO_{\Delta}, \CO_{\Delta}) \; \cong \;
\bigoplus_{p+q=n} H^q \left( X , \bigwedge^p T_{X} \right)
\ee
where $\Delta$ is the diagonal in $X \times X$.
\end{theorem}

Moreover, Yekutieli \cite{Yekutieli} shows that there is an isomorphism from the hypercohomology to self-Ext:
\be
\mathbb{H}^n (X, D_{poly} (X)) = \Ext^n_{X \times X} (\CO_X, \CO_X)
\ee
which is compatible with the cup product on the left and the Yoneda product on the right.
And using the isomorphism between the Hochschild cohomology and the polyvector field cohomology \cite{GSchack}, one has
\be
HH^* (\CD^b (X)) \; \cong \; \Ext^*_{X \times X} (\CO_\Delta,\CO_\Delta) \; \cong \; H^* (X, \Lambda^* T_X )
\label{HHExtDD}
\ee




\subsection{HOMFLY homology from symplectic geometry}
\label{sec:Amodel}

Now, let us see what kind of A-models one gets by applying mirror symmetry to the open and closed B-models in the above discussion.

In general, we denote by $Y$ the mirror of $X$.
The simplest example is $X = (\C^*)^r$ viewed as a (trivial) $T^r$ fibration over $\R^r$.
Then, mirror symmetry is simply a T-duality (a ``Fourier transform'') along the fibers,
and the mirror manifold is $Y \cong T^* T^r$.
The mirror of the statement $HH^* (\CD^b (X)) \cong \C [u_i^{\pm 1} , du_i]$
is the statement about the Hochschild cohomology of the Fukaya category $\CF (Y)$,
\be
HH^* \left( \CF (T^* T^r) \right) \; \cong \; \C [u_i^{\pm 1} , du_i]
\label{HHTTex}
\ee
which, by analogy with \eqref{HHExtDD}, can be also realized as the boundary OPE algebra
in the A-model of $Y \times \bar Y$, where $\bar Y$ denotes the space $Y$ with the symplectic form $- \omega$.
Indeed, in general, when a symplectic manifold $Y$ has ``enough'' Lagrangians,
the Hochschild cohomology its Fukaya category $\CF (Y)$ is expected \cite{Abouzaid,KontsevichHMS,Costello}
to be isomorphic to the Lagrangian Floer cohomology of the (anti-)diagonal $\Delta_Y \hookrightarrow Y \times \bar Y$,
\be
HH^* \left( \CF (Y) \right) \; \cong \; HF^* (\Delta_Y , \Delta_Y)
\label{HHHFdiag}
\ee
Thus, in our basic example of \eqref{openDD} and \eqref{HHTTex} mirror symmetry maps a B-brane $\CB = \CO_{\Delta_X}$
to a Lagrangian A-brane supported on the conormal bundle $T_{\Delta}^{\vee}$ to $T_{\Delta} \subset T^n \times T^n$
in $Y \times Y = T^* T^r \times T^* T^r$, so that
\be
HF^* (T_{\Delta}^{\vee},T_{\Delta}^{\vee}) \; \cong \; \C [u_i^{\pm 1} , du_i]
\ee
This is an open A-model version of \eqref{HHTTex} and a concrete illustration of \eqref{HHHFdiag}.

In general, this leads us to the following picture, where the (colored) HOMFLY homology is realized
either in terms of closed A-model of a symplectic manifold $Y$
\be
\CH^{S^r} (K) \; = \; HH^* \left( \CF (Y) \right)
\ee
or in terms of open A-model (Floer homology) of a certain Lagrangian submanifold $L$,
\be
\CH^{S^r} (K) \; = \; HF^* (L,L)
\label{HKLL}
\ee
(In our previous discussion, $L$ was the (anti-)diagonal $\Delta_Y \hookrightarrow Y \times \bar Y$,
but we allow more general Lagrangian submanifolds and more general symplectic manifolds here.)
For torus knots, the closed A-model version can be obtained by applying
the supermanifold version of mirror symmetry \cite{AVsuper,Katzarkov,Sethi}
to the B-model in section \ref{sec:Bmodel}.
We plan to return to a systematic study of this mirror symmetry elsewhere.

Here, let us simply point out that even for non-torus knots one might hope to find a realization of the form \eqref{HKLL}.
For example, for the figure-eight knot $K=4_1$ and $r=1$ a natural guess is
\be
L = {\bf S}^2 \text{~with 3 punctures}
\ee
embedded in some symplectic manifold $Y$, such that $HF^* (L,L) \cong H^* (L)$.






\section{``Bottom row'' of the colored HOMFLY homology}
\label{sec:bottom}

In this part we wish to study the ``bottom row'' of the colored superpolynomial, defined as
\be
\CP^{\lambda}_{\text{bottom}} (q,t) \; : = \; \lim_{\a \to 0} \, \a^{\#} \, \CP^{\lambda} (\a,q,t) \,,
\label{bottomrow}
\ee
where $\a^{\#}$ denotes the appropriate power of $a$, such that the product $\a^{\#} \, \CP^{\lambda} (\a,q,t)$
contains only non-negative $a$-degrees starting from zero.


\subsection{Combinatorial interpretation for torus knots}
\label{sec:combbot}

First, let us recall the conjectural combinatorial description of the uncolored triply graded homology
for a $(p,q)$ torus knot \cite{G,GM,ORS}. Consider a $p\times q$ rectangle and a $NW-SE$ diagonal in it.

\begin{proposition}(\cite{G})
\label{prop:bottom1}
The dimension of the ``bottom row'' of the reduced uncolored homology equals to the number of lattice paths
in this rectangle strictly below the diagonal:
$$\dim \CH_{\text{bottom}} (T(p,q)) \; = \; c_{p,q}=\frac{(p+q-1)!}{p!q!}.$$
\end{proposition}

For example, if $q=p+1$, this dimension equals to the $p$-th Catalan number.

\begin{proposition}(\cite{G})
The dimension of the ``$k$-th row'' of the reduced uncolored homology equals to the number of lattice paths
below the diagonal with $k$ marked corners:
$$\dim \CH_{a=k} (T(p,q)) \; = \; \frac{(p+q-k-1)!}{ p\cdot q\cdot k!\cdot (p-k-1)!(q-k-1)!}.$$
\end{proposition}

A $q$-analogue of this formula was discussed in \cite[eq. (3.46)]{BEM}.
Both of these propositions motivate the following combinatorial construction,
completed in \cite{ORS} where it was matched to the algebro-geometric constructions of \cite{os}.

The basis in $\CH_{p,q}$ is enumerated by the lattice paths in the $p\times q$ rectangle with marked corners. To every such path we assign three gradings, where $a$-grading corresponds to the number of marked corners. Let us describe $q-$ and $t-$ gradings.
For simplicity, we will focus on the bottom row, considered in details in \cite{GM}. Corrections for the higher rows can be found in \cite{ORS}.

Let us interpret a lattice path as a Young diagram $D$. Consider the $\C^{*}\times \C^{*}$ action on the Hilbert scheme of
$N$ points on $\C^2$, and let us restrict it to a one-parameter subgroup $(t^p,t^q)$. One can check (see {\it e.g.} \cite{Nakajima})
that the action of this subgroup has isolated fixed points parametrized by the Young diagrams with $N$ boxes. Therefore the corresponding moment map is a Morse function on $\Hilb^{N}(\C^2)$, and its gradient flow induces the Bialynicki-Birula cell decomposition of the Hilbert scheme \cite{Nakajima,Elstro}. We are interested in the dimension of the cell $C_{D}$ labelled by the fixed point $D$, which is given by the following formula:
$$\dim C_{D}=|D|+h^{+}_{p/q}(D),$$
where
\begin{equation}
\label{hplus}
h^{+}_{p/q}(D)=\sharp\left\{c\in D~~ \vline~~ \frac{a(c)}{l(c)+1}\le \frac{p}{q}< \frac{a(c)+1}{l(c)}\right\}.
\end{equation}
Here $a(c)$ and $l(c)$ denote the arm and the leg of a cell $c$ in a diagram $D$:

\begin{tikzpicture}
\draw  (0,0)--(0,4)--(5,0)--(0,0);
\draw  (1.5,0.5)--(1.5,0.7)--(1.7,0.7)--(1.7,0.5)--(1.5,0.5);
\draw [thick] (0,3)--(0.5,3) -- (0.5,2) -- (2.3,2)--(2.3,1.3)--(3,1.3)--(3,0.5)--(4,0.5)--(4,0)--(0,0)--(0,3);
\draw [<->,>=stealth] (1.7,0.6) -- (3,0.6);
\draw [<->,>=stealth] (1.6,0.7) -- (1.6,2);
\draw (2.3,0.4) node {${a(c)}$};
\draw (1.3,1.3) node {${l(c)}$};
\draw (2.5,-0.2) node {$p$};
\draw (-0.2,2) node {$q$};
\draw [->,>=stealth] (2.6,-0.15) -- (5,-0.15);
\draw [->,>=stealth] (2.4,-0.15) -- (0,-0.15);
\draw [->,>=stealth] (-0.15,1.8) -- (-0.15,0);
\draw [->,>=stealth] (-0.15,2.2) -- (-0.15,4);
\end{tikzpicture}

The statistics $h^{+}_{p/q}(D)$ was introduced in \cite{LW} in connection with some combinatorial models of the bigraded Catalan numbers.

\begin{proposition}
\label{prop:bottom3}
The gradings of Dyck paths are given by the following equations:
\begin{enumerate}

\item{The $q$-grading assigned to $D$ equals to $2\left[|D|+2h^{+}_{p/q}(D)\right]$.}

\item{The $t$-grading assigned to $D$ equals to $2|D|$.}
\end{enumerate}
\end{proposition}


Motivated the refined exponential growth conjecture, we assume that the dimension of the $S^r$-colored homology is equal to the $r$-th power of the uncolored homology, {\it i.e.} the $r$-th power of the generalized Catalan number $c_{p,q}$.
Therefore it is natural to assume that one can find a basis in the $S^r$-colored homology labelled by all possible $r$-tuples of Young diagrams in $p\times q$ rectangle below the diagonal.

\begin{conjecture}
\label{prop:bottom4}
The bottom row of the $S^r$ colored homology of the $(p,q)$ torus knot has a basis labeled by the $r$-tuples $(D_1,\ldots,D_r)$ of the Dyck paths in $p\times q$ rectangle. The $(Q,t_r)$ gradings of Dyck paths are given by the following equations:
\begin{enumerate}

\item{The $Q$-grading assigned to $D$ equals to $2\sum_{i=1}^{r}\left[|D_i|+2h^{+}_{p/q}(D_i)\right]$.}

\item{The $t_r$-grading assigned to $D$ equals to $2\sum_{i=1}^{r}|D_i|$.}
\end{enumerate}
\end{conjecture}

The $q$-grading (and, therefore, the $t_c$-grading) has yet to be constructed. We expect it to be related to the combinatorial constructions of \cite{BDZ} and \cite{HMZ}.




\subsection{Coupled instanton-vortex counting}
\label{sec:inst-surf}

The ``bottom row'' \eqref{bottomrow} has a simple and beautiful interpretation in terms of instanton / vortex counting.
As a warm-up, let us start with a simple vortex counting problem that is easy to do ``by hand''
and that has all the essential features. Then, we shall upgrade it to the equivariant instanton counting relevant to arbitrary knots and links.

Let $\CV_m$ be the moduli space of $m$ abelian vortices on a two-dimensional plane, $D = \R^2$.
In other words, $\CV_m$ is the moduli space of solutions to the PDEs
\be
\begin{array}{rl}
* F_A & =~ i |\phi|^2 - it \\
\bar \partial_A \phi & =~ 0
\end{array}
\label{abelianvorteq}
\ee
where $A$ is a connection on a $U(1)$ bundle of first Chern class $m$, and $t$ is a parameter.
These equations describe supersymmetric configurations (BPS states) in a two-dimensional theory
on $D$ with $\CN=(2,2)$ supersymmetry:
\be
\CT_{\text{vortex}}~:~ U(1)~\text{gauge theory with a single charged field}~\phi
\ee

It is well known that $\CV_m$ is a K\"ahler manifold of (real) dimension $2m$. Namely,
\be
\CV_m \; = \; \Sym^m (\C) \; \equiv \; \C^m / S_m \,,
\label{vortsymm}
\ee
where one can think of coordinates on $\CV_m$ as vortex positions on $D = \R^2 \cong \C$.

Since $D$ admits a circle action, one can consider the equivariant character, $Ch_q (\CV_m)$,
with respect to the rotation group $U(1)_q$ acting on $D$.
Indeed, $U(1)_q$ acts on $\CV_m$ in a natural way, by equal phase rotations on all factors in the symmetric product \eqref{vortsymm}.
Moreover, identifying the vortex moduli space $\CV_m = \Sym^m (\C)$
with the space of monic polynomials of degree $m$,
\be
f (x) \; = \; \prod_{j=1}^m (x - x_j) = x^m + a_1 x^{m-1} + \ldots + a_m \,,
\ee
we immediately deduce the isomorphism $\CV_m \cong \C^m = (\{ a_1, \ldots, a_m \})$
and also learn that $U(1)_q$ acts on the space $\CV_m$ with weights $(1, 2, \ldots, m)$.
Therefore, the $U(1)_q$-equivariant character of $\CV_m$ is
\be
Ch_q (\CV_m) \; = \; \frac{1}{(1-q)(1-q^2) \ldots (1-q^m)} \,,
\label{unknotvortchar}
\ee
in which a careful reader will recognize the ``bottom row'' of the \textsl{unnormalized} $S^m$-colored HOMFLY polynomial of the unknot.

This is not an accident, of course, and the physics setup \eqref{theoryB} predicts that the ``bottom row''
of any $\lambda$-colored HOMFLY homology of any knot $K$ has a similar interpretation in terms
of equivariant vortex counting on $D = \R^2$.
In order to explain this relation, we need to generalize our warm-up example in two important ways:
first, we need to introduce the homological $t$-grading, and secondly we need a generalization to arbitrary knots.
Both of these problems can be achieved by embedding $D = \R^2$ into a larger space $M_4 = \R^4$,
and realizing our vortex counting problem on $D$ as a special case of counting solutions
to coupled \textsl{instanton-vortex equations} or, equivalently, via equivariant instanton
counting on the 4-manifold $M_4$ in the presence of ramification along $D \subset M_4$.

However, before we proceed to generalizations, let us stay a bit longer in the world of vortex equations
and explore the picture which seems to emerge:
\be
\text{knot}~K \quad \leadsto \quad \text{2d vortex theory}~\CT_{\text{vortex}} (K) \quad \leadsto \quad \CV_m (K)
\ee
so that a suitable version $Ch_{q,t} (\CV_m)$ of the equivariant character computes the bottom row of
the colored superpolynomial \eqref{bottomrow} with $\lambda = S^m$,
\be
Ch_{q,t} (\CV_m) \; = \; \CP^{S^m}_{\text{bottom}} (q,t) \,.
\label{naiveVmP}
\ee
Already at this stage the reader might suspect that incorporating the $t$-grading and passing to knot homologies
can be addressed by considering equivariant cohomology or K-theory of the vortex moduli space,
\be
H^*_{U(1)_q} (\CV_m (K)) \,,
\label{naiveHvort}
\ee
where $t$-grading is identified with the homological grading.
Although this idea is a little too naive, it is actually on the right track, and it is instructive to pursue it a little further.

Therefore, as the natural next step let us consider a non-abelian generalization of \eqref{abelianvorteq}
that describes supersymmetric solutions in the 2d theory:
\be
\CT_{\text{vortex}}~:~ U(p+1)~\text{gauge theory with}~p+1~\text{fundamental fields}~\phi_i
\ee
The corresponding vortex equations
\be
\begin{array}{rl}
* F_A & =~ i\sum_{i=1}^{p+1} \phi_i \phi_i^{\dagger} - i t \\
\bar \partial_A \phi_i & =~ 0
\end{array}
\label{vortexeq}
\ee
involve a $U(p+1)$ gauge connection and $p+1$ Higgs fields $\phi_i$ in the fundamental
representation of the gauge group. Again, the $m$-vortex moduli space is a K\"ahler manifold
of real dimension
\be
\dim~ \CV_m^{U(p+1)} = 2 m (p+1) \,,
\label{mmndimension}
\ee
In particular, the single-vortex moduli space is well known to be a $(2p+2)$-dimensional space
\be
\CV_1^{U(p+1)} \; \cong \; \C \times \cp^p
\ee
where the factor $\C$ parametrized by the ``center-of-mass'' position,
while $\cp^p$ encodes the ``internal degrees of freedom'' of a single non-abelian vortex.
The rotation symmetry $U(1)_q$ acts on $\C$ with weight 1,
so we expect that it contributes to the equivariant character a factor $\frac{1}{1-q}$.
However, unlike our first example (related to the unknot), now the moduli space $\CV_1^{U(p+1)}$
has non-trivial topology and, therefore, if $t$-grading is simply the homological grading on \eqref{naiveHvort}
the suitable generalization of the equivariant character should be a product of $\frac{1}{1-q}$
and the Poincar\'e polynomial of $\cp^p$,
\be
\frac{1}{1-q} \sum_{i=0}^p t^{2i}
\ee
This turns out to be the correct answer for the bottom row of the HOMFLY homology of the $(2,2p+1)$ torus knot.


Now let us explain why all these examples are ``working'' and where the connection with vortex equations come from.
The reason, in fact, is already contained in section~\ref{sec:geomphys}
where we reviewed the interpretation~\eqref{HHBPS} of homological knot invariants
in terms of supersymmetric configurations (BPS states) in the string theory setup~\eqref{theoryB}.
What this interpretation tells us is that specializing to the bottom row \eqref{bottomrow},
{\it i.e.} taking the limit $\a \to 0$, means the ``large volume limit.''
Indeed, according to the identification of the parameters \eqref{NvolCP1},
in this limit the interesting geometry (and topology) of the Calabi-Yau space $X$
is replaced by the simplest Calabi-Yau 3-fold, namely a flat space:
\be
X \;\overset{\a \to 0}{\leadsto}\; \C^3 \,.
\label{Xatozero}
\ee

In other words, the bottom row of the colored HOMFLY homology is described by
a much simpler ``toy model'' of \eqref{theoryB} in which the pair $(X,L_K)$ is replaced by $(\C^3, L_K)$.
(Not much happens to the Lagrangian submanifold $L_K$ in this limit.)

The next step is to look at this system from the vantage point of the 4-manifold $M_4 \cong \R^4$
and the defect (called the ``surface operator'' \cite{Ramified}) supported on $D \cong \R^2$.
Before we took the limit $\a \to 0$, the compactification on $X$ produces abelian gauge theory
on $M_4$ with gauge group $U(1)$ \cite{KKV}.
Incorporating an extra brane in this setup means including the so-called surface operator supported on $D$
or, mathematically speaking, ramification in the gauge theory on $M_4$.

Let $\CM_{k,m}$ be the moduli space of abelian instantons on $M_4 = \R^4$ with ramification along $D \subset M_4$.
In other words, $\CM_{k,m}$ is the moduli space of solutions to the self-duality equation on $M_4 \setminus D$,
\be
F_A^+ \; = \; 0
\label{sdeq}
\ee
with the second Chern class $k$, with the monopole number $m = \frac{1}{2\pi} \int_D F_A$,
and with the prescribed behavior along $D$.
The latter is what we call the ramification data;
{\it e.g.} a simple example of the so-called \textsl{tame} ramification
can be obtained by introducing a $\delta$-function source
in the self-duality equation \eqref{sdeq} on $M_4$:
\be
F_A^+ \; = \; 2\pi \alpha (\delta_D)^+ \,.
\ee
The gauge connections which solve this equation have a first-order pole at $D$.
More generally, one can study solutions to self-duality equations with singularities of arbitrarily high order,
\be
A = dz  \left( \frac{\alpha_1}{z} + \frac{\alpha_2}{z^2} + \ldots \right) + d \bar z \left( \ldots \right) \,.
\ee
This is called \textsl{wild} ramification and is precisely how the dependence on the knot $K$ will enter,
via the choice of the ramification data.\footnote{For instance, it was conjectured~\cite{DGH} that $(2,2p+1)$ torus knots
correspond to wild ramification of order $p$.}
Let us denote the corresponding moduli space by $\CM_{k,m} (K)$.

Much like the vortex moduli space $\CV_m$ enjoyed an action of the rotation group $U(1)_q$,
the moduli space of ``ramified instantons'' on $M_4 \setminus D \cong \C \times \C^*$
has an action of the rotation group $U(1)_q \times U(1)_t$,
where $U(1)_q$ acts by rotations of $D = \C$ and $U(1)_t$ acts by rotations of its normal bundle, $\C^*$.

Then, in the limit \eqref{Xatozero} the physical interpretation \eqref{HHBPS} of the colored HOMFLY homology predicts
\be
Ch_{q,t} (\CM_{0,m} (K)) \; = \; \bar \CP^{S^m}_{\text{bottom}} (K; q,t)
\ee
which is very close to \eqref{naiveVmP} and, in fact, is exactly the sought-after proper generalization of it.











The connection with vortex equations is now easy to see. At least for some knots
the moduli space $\CM_{k,m} (K)$ can be equivalently described as the moduli space of solutions
to the coupled \textsl{instanton-vortex equations}:
\begin{eqnarray}
F_A^+ & = & 2\pi \phi \otimes \phi^{\dagger} \; (\delta_D)^+  \nonumber \\
*_{D} F_B & = & i \phi^{\dagger} \otimes \phi - i t {\bf 1}_E \label{coupledvort} \\
\bar \partial_{A,B} \phi & = & 0 \nonumber
\end{eqnarray}
where $A$ is a unitary connection on the line bundle $\CL$ over $M_4$,
$B$ is a unitary connection on the bundle $E$ over $D \subset M_4$,
$\phi$ is an element $\phi \in H^0 (\Hom (E,\CL \vert_D ))$, and $\phi^{\dagger}$ is its adjoint.


As far as we know the instanton-vortex equations \eqref{coupledvort} are new and have not appeared in the literature previously.
Their closest cousin is a set of the so-called coupled vortex equations studied {\it e.g.} in~\cite{BGP1,BGP2},
where both $E$ and $\CL$ are bundles over $D$. In other words, our equations \eqref{coupledvort} can be viewed
as analogs of the coupled vortex equations where one of the bundles is extended over $M_4$.
For instance, for a $(2,2p+1)$ torus knot $T^{2,2p+1}$ one takes $E$ to be a unitary bundle of rank $p+1$.

Then, as before, to get the ``bottom row'' of the \textsl{unreduced} $S^m$-colored HOMFLY homology we need to consider
the equivariant character of $\CM_{0,m} (K)$ with instanton number $k=0$ and vortex number $m$.
In situations where $\CM_{k,m} (K)$ can be identified with the moduli space of solutions to \eqref{coupledvort}
this boils down to studying non-abelian vortex equations on $D$.
Thus, for $2p+1$ torus knots we end up with $U(p+1)$ vortex equations,
so that the equivariant character of $\CM_{0,m} (T^{2,2p+1}) \cong \CV_m^{U(p+1)}$
essentially consists of $p+1$ copies of the abelian vortex character that we discussed earlier, {\it cf.} \eqref{unknotvortchar}.

Our prediction is that the equivariant character of the $m$-vortex moduli space $\CV_m^{U(p+1)}$
is the ``bottom row'' of the $S^m$-colored HOMFLY homology of the $(2,2p+1)$ torus knot, {\it i.e.}
\begin{eqnarray}\nonumber
\!\!\!\!\!\!\!\!Ch_{q,t} (\CV_m^{U(p+1)})  &=& \frac{q^{-pm}}{(q;q)_m}  \sum_{0\le k_p \le \ldots \le k_2 \le k_1 \le m}
\left[\!\begin{array}{c} m \\k_1 \end{array}\!\right]\left[\!\begin{array}{c} k_1\\k_2 \end{array}
\!\right]\cdots\left[\!\begin{array}{c} k_{p-1}\\k_p \end{array}\!\right]  \times\\
& & \nonumber \!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \times \,\,\, q^{(2m+1)(k_1+k_2+\ldots+k_p)-\sum_{i=1}^p k_{i-1}k_i}
t^{2(k_1+k_2+\ldots+k_p)} ,
\end{eqnarray}
with the convention $k_0:=m$.
For example, when $m=2$ and $p=1$, {\it i.e.} for the $(2,3)$ torus knot (= trefoil knot $3_1$) colored by $\lambda = \tableau{2}$ we have
\be
Ch_{q,t} (\CV_2^{U(2)}) \; = \; q^{-2} \frac{1 + q^3 t^2 + q^4 t^2 + q^6 t^4}{(1-q)(1-q^2)}
\label{S2chtref}
\ee
which can be verified using equivariant $U(2)$ action on $\CV_2^{U(2)}$, see {\it e.g.} \cite{DGH} and \cite{Taipale}.

It would be interesting to understand better the relation between vortex moduli spaces
and the combinatorics of the Bialynicki-Birula cell decomposition discussed in Section \ref{sec:combbot}
that also determines the bottom row of the colored HOMFLY homology.
Thus, in the above example \eqref{S2chtref} of the $S^2$-colored trefoil, the corresponding
moduli space of two $U(2)$ vortices $\CV_2^{U(2)}$ has been studied in the literature \cite{Tong,Shifman,Baptista}
and is known to have two strata, which correspond to separated vortices and coincident vortices.
The first stratum --- of complex dimension 4 --- is simply the product of two single-vortex moduli spaces $\CV_1^{U(2)}$,
modulo the permutation of the two vortices,
\be
\CU_1 ( \CV_2^{U(2)} ) \; \cong \; \C \times \frac{\C \times \cp^1 \times \cp^1}{\Z_2}
\ee
with the ``diagonal'' removed.
The second stratum --- of complex dimension 3 ---  is known to be the space of Hecke modifications
(times the center of mass position),
\be
\CU_2 ( \CV_2^{U(2)} ) \; \cong \;  \C \times \mathbb{W} \cp^2_{(1,1,2)} \,.
\ee
See \cite{GS} for color graphics illustrating the bottom row of the $S^2$-colored HOMFLY homology
and the role of $\mathbb{W} \cp^2_{(1,1,2)}$ in its construction.
In this, and more general examples, it would be interesting to match the geometry of these strata
with the Bialynicki-Birula cell decomposition discussed in Section \ref{sec:combbot}.

Another direction for future work, already mentioned in Section \ref{sec:Bmodel},
is the relation between theory $\CT_{\text{vortex}} (K)$ and the surface operator theory considered in \cite{FGS2,FGSS}.
Indeed, here, in Section \ref{sec:Bmodel}, and in \cite{FGS2,FGSS} the Poincar\'e polynomial
of the colored HOMFLY homology (a.k.a. the superpolynomial) is realized as a certain index (or, character)
of a two-dimensional $\CN=2$ theory that describes the physics on $D$ in the brane construction \eqref{theoryB}.
Yet, the key difference is that here and in Section \ref{sec:Bmodel} there is a different $\CN=2$ theory
for each choice of ``color'' $\lambda$; the index of such theories determines colored superpolynomials
and {\it a priori} all such theories are unrelated.
In \cite{FGS2,FGSS}, on the other hand, a single $\CN=2$ theory $\CT_K$ (that depends only on the knot $K$)
determines the entire tower of $S^m$-colored homological invariants, via specializations of its supersymmetric index:
\be
\bar \CP^{S^m}_K (a,q,t) \; = \; \CI_{\CT_K} (x = q^m; a,q,t) \,.
\ee
Moreover, recursion relations found in \cite{FGS2,Nawata,FGSS}, which have a natural meaning\footnote{{\it e.g.} the characteristic
variety of the corresponding $q$-difference equations has a nice interpretation as the moduli space of SUSY parameters, {\it etc.}}
in the $\CN=2$ theory $\CT_K$, relate equivariant characters $Ch_{q,t} (\CM_{0,m} (K))$
with different values of the ``vortex number'' $m = \frac{1}{2 \pi} \int_D F$.
Similarly, from the vantage point of Section \ref{sec:Bmodel}, the recursion relations of \cite{FGS2,Nawata,FGSS}
relate B-models with target manifolds of different (super-)dimension
in a way reminiscent of the notions of ``endoscopy'' and ``transfer'' in the geometric Langlands correspondence \cite{FW}.
Thus, in the case of the trefoil knot we have:
\begin{align}
\CP^{S^{m+2}}_{\text{bottom}}
- (q^{-1} - t^2 q^m + (1+q) q^{2m} t^2) \CP^{S^{m+1}}_{\text{bottom}}
& \\
+ t^4 q^{3m-1} (q^m - 1) \CP^{S^{m}}_{\text{bottom}} & = 0 \notag
\end{align}



\begin{appendix}
