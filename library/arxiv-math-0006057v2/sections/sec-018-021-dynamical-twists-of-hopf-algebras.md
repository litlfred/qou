---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-018-021-dynamical-twists-of-hopf-algebras
section_title: "Dynamical twists of Hopf algebras"
section_number: 0.21
pages: 24-27
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.975
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
We describe a method of constructing twists of quantum groupoids,
which is a  finite-dimensional modification of the construction
proposed in \cite{Xu} and is dual to that of \cite{EV}, cf.\ \cite{EN}.

Dynamical twists  first appeared in the work of Babelon \cite{Ba},
see also \cite{BBB}.

Let $U$ be a Hopf algebra and $A=\Map(\mathbb{T},\, k)$
be a commutative and cocommutative Hopf algebra
of functions on a finite Abelian group $\mathbb{T}$
which is a Hopf subalgebra of $U$. Let $P_\mu,\, \mu\in \mathbb{T}$
be the minimal idempotents in $A$. 


\begin{definition} 
\label{zero weight}
We say that an element $x$ in $U^{\otimes n},\, n\geq 1$
has {\em zero weight} if $x$ commutes with
$\Delta^n(a)$ for all $a\in A$, where $\Delta^n: A \to A^{\otimes n}$
is the iterated comultiplication.
\end{definition}

\begin{definition}
\label{dynamical twist}
An invertible, zero-weight  $U^{\otimes 2}$-valued function
$J(\lambda)$ on $\mathbb{T}$ is called a {\em dynamical twist }
for $U$ if it satisfies
the following functional equations :
\begin{eqnarray}
\label{dynamical equation}
(\Delta\otimes \id)J(\lambda) (J(\lambda+h^{(3)}) \otimes 1)
&=& (\id \otimes\Delta) J(\lambda) (1\otimes J(\lambda) ), \\
(\eps\otimes \id)J(\lambda) = (\id \otimes \eps)J(\lambda)  &=& 1.
\end{eqnarray}
Here an in what follows the notation $\lambda+ h^{(i)}$ means that   
the argument $\lambda$ is shifted by the weight of the $i$-th component,
e.g., $J(\lambda+h^{(3)}) =\sum_\mu\, J(\lambda+\mu) \otimes P_\mu
\in U^{\otimes 2} \otimes_k A$.
\end{definition}  

Note that for every fixed $\lambda\in \mathbb{T}$ the element
$J(\lambda)\in U\otimes U$ does not have to be a twist for $U$
in the sense of Drinfeld.
It turns out that an appropriate object for which $J$
defines a twisting is a certain quantum groupoid that
we describe next.

Observe that the simple algebra $\End_k(A)$ has a natural
structure of a cocommutative quantum groupoid given as follows
(cf.\ Section~\ref{groupoid algebras}) : 

Let $\{ E_{\lambda\mu} \}_{\lambda,\mu\in \mathbb{T}}$ be a basis
of $\End_k(A)$ such that
\begin{equation}
(E_{\lambda\mu}f)(\nu) = \delta_{\mu\nu}f(\lambda), \qquad
f\in A,\, \lambda,\mu,\nu\in \mathbb{T},
\end{equation}
then the comultiplication, counit, and antipode of
$\End_k(A)$ are given by
\begin{equation}
\Delta(E_{\lambda\mu}) = E_{\lambda\mu} \otimes E_{\lambda\mu},
\quad \eps(E_{\lambda\mu}) =1, \quad 
S(E_{\lambda\mu}) = E_{\mu\lambda}.
\end{equation}

Define the tensor product quantum groupoid $H = \End_k(A)\otimes_k U$
and observe that the elements
\begin{equation}
\Theta = \sum_{\lambda\mu}\, E_{\lambda\lambda+\mu} \otimes
E_{\lambda\lambda}P_\mu  \quad \mbox{ and } \quad
\bTheta = \sum_{\lambda\mu}\, E_{\lambda+\mu\lambda } \otimes
E_{\lambda\lambda}P_\mu
\label{eqn: Xu's theta}
\end{equation}
define a twist for $H$. Thus, according to Proposition~\ref{twisting},
$H_\Theta = (\End_k(A)\otimes_k U)_\Theta$ becomes
a quantum groupoid . It is non-commutative, non-cocommutative,
and not a Hopf algebra if $|\mathbb{T}|>1$.

It was shown in \cite{EN}, following \cite{Xu}, that $H_\Theta$ can be further
twisted by means of a dynamical twist $J(\lambda)$ on $U$. Namely,
if $J(\lambda)$ is a dynamical twists on $U$ embedded in $H\otimes_k H$ as 
\begin{equation}
J(\lambda) = \sum_{\lambda} E_{\lambda\lambda}
J\I(\lambda) \otimes E_{\lambda\lambda}J\II(\lambda),
\end{equation}
then  the pair ($F(\lambda), \bF(\lambda)$), where
$$
F(\lambda) = J(\lambda)\Theta \quad \mbox{ and }\quad
\bF(\lambda) = \bTheta J^{-1}(\lambda)
$$
defines a twist for $H=\End_k(A)\otimes_k U$.
Thus, every dynamical twist $J(\lambda)$ for a Hopf algebra $U$
gives rise to a quantum groupoid $H_J = H_{J(\lambda)\Theta}$.
     
\begin{remark}
According to Proposition~\ref{twisting}, the antipode $S_J$ of $H_J$
is given by $S_J(h) = v^{-1}S(h)v$ for all $h\in H_J$, where $S$
is the antipode of $H$ and
$$
v = \sum_{\lambda \mu} E_{\lambda+\mu \lambda}
    (S(J^{(1)}) J^{(2)})(\lambda) P_\mu.
$$
\end{remark}

\begin{remark}
There is a procedure dual to the one described above. It was shown in
\cite{EV} that given a dynamical twist  $J(\lambda)$ it is possible 
to deform the multiplication on the vector space 
$D = \Map(\mathbb{T}\times\mathbb{T},\, k)\otimes_k U^*$ and 
obtain a {\em dynamical quantum group} $D_{J}$. The relation between
$H_J$ and $D_{J}$ in the case when $\dim{U}<\infty$
was established in \cite{EN}, where it was proven that
$D_J$ is isomorphic to $H_J^{*op}$.
\end{remark}



\subsection{Dynamical twists for $U_q(\g)$ at roots of $1$}

Suppose that $\g$ is a simple Lie algebra of type
$A$, $D$ or $E$ and $q$ is a primitive $\ell$th root of unity in $k$,
where $\ell\geq 3$ is odd and coprime with the determinant
of the Cartan matrix $(a_{ij})_{ij=1,\dots,m}$ of $\g$.

Let $U=U_q(\g)$ be the corresponding quantum group
which is a finite dimensional Hopf algebra with generators
$E_i,F_i, K_i$, where $i=1,\dots,m$ and relations as in \cite{L}.

Let $\mathbb{T} \cong (\mathbb{Z}/\ell\mathbb{Z})^m$ be the abelian
group generated by $K_i,\,i=1,\dots,m$. For any $m$-tuple of integers
$\lambda =(\lambda_1,\dots,\lambda_m)$
we will write $K_\lambda = K_1^{\lambda_1}\dots K_m^{\lambda_m}\in\mathbb{T}$.

Let $\R$ be the universal $R$-matrix of $U_q(\g)$ and $\Omega$
be the ``Cartan part'' of $\R$ (\cite{T}).

For arbitrary non-zero constants $\Lambda_1,\dots, \Lambda_m$
define a Hopf algebra automorphism $\Lambda$ of $U$ by
setting
\begin{equation*}
\Lambda(E_i) = \Lambda_i E_i,\quad
\Lambda(F_i) = \Lambda_i^{-1} F_i,\quad  \mbox{ and } \quad
\Lambda(K_i) = K_i \quad\mbox{ for all } i=1,\dots,m.
\end{equation*}
We will say that $\Lambda=(\Lambda_1,\dots,\Lambda_m)$ is {\em generic}
if the spectrum of $\Lambda$ does not contain $\ell$th roots of unity.

Note that the algebra $U$ is $\mathbb{Z}$-graded with
\begin{equation}
\deg(E_i) =1, \quad \deg(F_i) = -1, \quad \deg(K_i) = 0,
\qquad i=1,\dots,m,
\end{equation}
and $\deg(XY)= \deg(X)+\deg(Y)$ for all $X$ and $Y$. Of course,
there are only finitely many non-zero components of $U$   
since it is finite dimensional.   

Let $U_+$ be the subalgebra of $U$ generated by
the elements $E_i,\,K_i,\,i=1,\dots,m$, $U_-$ be
the subalgebra  generated by $F_i,\,K_i,\,i=1,\dots,m$, and
$I_\pm$ be the kernels of the projections from $U_\pm$
to the elements of zero degree.

The next Proposition was proven in \cite{ABRR}, \cite{ES}, \cite{ESS}
for generic values of $q$ and in \cite{EN} for $q$ a root of unity :

\begin{proposition}
\label{equation for J}
For every generic $\Lambda$ there exists a unique element
$J(\lambda) \in 1 + I_+ \otimes I_-$ that satisfies the
following ABRR relation \cite{ABRR}, \cite{ES}, \cite{ESS} :
\begin{equation}
\label{eqn: ABRR}
(\Ad K_\lambda \circ \Lambda \otimes \id) (\R J(\lambda) \Omega^{-1})
= J(\lambda),\quad  \lambda\in \mathbb{T}.
\end{equation}
The element
\begin{equation}
\tJ(\lambda)= J(2\lambda+h^{(1)}+h^{(2)})
\end{equation}
is a dynamical twist for $U_q(\g)$
in the sense of Definition~\ref{dynamical twist}.
\end{proposition}

\begin{proof}
The existence and uniqueness of the solution of (\ref{eqn: ABRR})
and the fact that $\tJ(\lambda)$ satisfies  (\ref{dynamical equation})
are established by induction on the degree of the first component
of $J(\lambda)$, see (\cite{EN}, 5.1).
\end{proof}

\begin{remark}
(a) The reason for introducing the ``shift'' automorphism $\Lambda$
is to avoid singularities in equation \cite{ABRR}.  Thus, we have
a family of dynamical deformations of $U_q(\g)$ (and, therefore,
a family of quantum groupoids depending on $m$ parameters). 
\newline (b) One can generalize the above construction and associate
a  dynamical twist $\tJ_T(\lambda)$ with any 
{\em generalized Belavin-Drinfeld triple} which consists of subsets
$\Gamma_1,\Gamma_2$ of the set $\Gamma=(\alpha_1,\dots,\alpha_m)$ 
of simple roots of $\g$ together with an inner product preserving
bijection $T: \Gamma_1 \to \Gamma_2$, see \cite{EN}, \cite{ESS}.
\end{remark}

\begin{example}
\label{sl 2}
Let us give an explicit expression for the twists
$J(\lambda)$ and $\tJ(\lambda)$ in the case
$\g=sl(2)$. $U_q(\g)$ is then generated by $E,F,K$ with the standard
relations. The element analogous to
$J(\lambda)$ for generic $q$ was computed
already in \cite{Ba} (see also \cite{BBB}).
If we switch to our conventions, this element will take the form
$$
J(\lambda)=\sum_{n=0}^\infty q^{-n(n+1)/2}\frac{(1-q^2)^n}{[n]_q!}
(E^n\otimes F^n)
\prod_{\nu=1}^n\frac{ \Lambda q^{2\lambda}}{1-\Lambda q^{2\lambda+2\nu}
(K\otimes K^{-1})}.
$$
It is obvious that the formula for
$q$ being a primitive $\ell$-th root of unity is simply obtained
by truncating this formula:
$$
J(\lambda)=\sum_{n=0}^{\ell-1} q^{-n(n+1)/2}\frac{(1-q^2)^n}{[n]_q!}
(E^n\otimes F^n)
\prod_{\nu=1}^n\frac{ \Lambda q^{2\lambda}}{1-\Lambda q^{2\lambda+2\nu}
(K\otimes K^{-1})}.
$$
Therefore,
$$
\tJ(\lambda)=\sum_{n=0}^{\ell-1} q^{-n(n+1)/2}\frac{(1-q^2)^n}{[n]_q!}
(E^n\otimes F^n)
\prod_{\nu=1}^n\frac{\Lambda q^{4\lambda}K\otimes K}{1-\Lambda q^{4\lambda+2\nu}
(K^2\otimes 1)}.   
$$
\end{example}

An important new property of the resulting quantum groupoids
$H_\tJ = U_q(\g)_\tJ$, compared with quantum groups $U_q(\g)$ is their
selfduality.   
A twisting of a quasitriangular quantum groupoid 
is again quasitriangular (Remark~\ref{rem: twist}(c)), so the 
twisted $R$-matrix
\begin{equation*}
\R(\lambda)
= \bTheta_{21}\R \Theta
= \sum_{\lambda\mu\nu}\, E_{\lambda \lambda+\nu}P_\mu
\R^{\tJ(1)}(\lambda) \otimes E_{\lambda+\mu \lambda} 
\R^{\tJ(2)}(\lambda)P_\nu,
\end{equation*}
where $\R^{J}(\lambda) = \tJ^{-1}_{21}(\lambda)R \tJ(\lambda)$,
establishes a homomorphism between $D_\tJ = H_\tJ^{*op}$ and $H_\tJ$.
One can show that the image of $\R(\lambda)$ contains all the generators
of $U_q(\g)$,  i.e., that the above homomorphism is in fact an isomorphism, 
see (\cite{EN}, 5.3).

\begin{remark}
The same selfduality result holds for any generalized Belavin-Drinfeld triple
for which $T$ is an automorphism of the Dynkin diagram of $\g$ 
(\cite{EN}, 5.4).
\end{remark}

\end{section}





\begin{section}
{Semisimple and $C^*$-quantum groupoids}
