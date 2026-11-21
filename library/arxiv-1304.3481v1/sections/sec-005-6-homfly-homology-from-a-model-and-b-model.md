---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-005-6-homfly-homology-from-a-model-and-b-model
section_title: "HOMFLY homology from A-model and B-model"
section_number: 6
pages: 55-61
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.974
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
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
