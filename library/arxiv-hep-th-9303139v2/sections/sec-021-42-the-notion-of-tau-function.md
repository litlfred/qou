---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-021-42-the-notion-of-tau-function
section_title: "The notion of $\tau$-function"
section_number: 4.2
pages: 75-83
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.991
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
There are several different definitions of $\tau$-functions, but all of them
are particular realizations of the following idea:
$\tau$-function is a generating functional of all the correlation functions in
the theory of free particles in 1+1 dimensions. This basic quantity is a kind
of "$det \ D$", where "$D$" is a time-evolution operator (continuous or
discrete) and "$det$" is a sort of a product over eigenvalues of "$D$",
which is usually expressed in the form of a functional integral, associated
with free particles (it is not $a\ priori$ Gaussian in original variables).
This quantity is the most general definition of $\tau$-function.

In practice one is usually more specific. The mostly well studied version of
$\tau$-function arises if one thinks about free particles of a peculiar type:
free fermions with quadratic Hamiltonian and continuous time evolution, i.e.
one considers a theory of spin-1/2 $b,c$-system (fermions) $\tilde \psi(\bar
 z, z), \psi(\bar z, z)$, described by the functional
integral
\be
\new
\begin{array}{c}
\tau\{A\} \sim \ Det(\bar\partial + {\cal A}) \sim \nn \\
\sim \int D\tilde\psi D\psi
\exp\left({ \int_{d^2 z} \tilde\psi\bar\partial\psi}\right)
\exp\left({\int_{d^2 z}\int_{d^2\tilde z} A( z,\tilde z)
\delta(\bar{\tilde z}-\bar z)\psi( z)\tilde\psi(\tilde z)}
\right)



\end{array}
\label{fftf}
\ee
where $\bar z$ plays the role of time and
${\cal A} = A( z,\tilde z)\delta(\bar{\tilde z}-\bar z)
d\bar{\tilde z}d\bar z$ is some $(\frac{1}{2},1; \frac{1}{2},
1)$-bidifferential (i.e. contains a factor of
$d\tilde z^{1/2}d\bar{\tilde z}d z^{1/2}d\bar z$).

Of course, one can think about more general $\tau$-functions, involving many
fermions (this is often done), and more general $b,c$- and $\beta,
\gamma$-systems, in particular, arising in the context of WZNW model,
associated to any Kac-Moody algebra of any level.\footnote{The main technical
difference between generic and "free-fermion" cases is that Lagrangian of
generic free field theory is not just quadratic in scalar fields $\phi$, but
can also contain particular combinations of exponents $e^\phi$. It also
deserves noting that the most general expresiion, {\it quadratic} in {\it
scalar} fields, if rewritten in terms of fermions is in fact {\it quartic}
(but of course $not$ a generic quartic interaction arises in this way).
Integrable nature of certain quartic-fermion interactions is well known from
the theory of Thirring models (in this class of models interactions are usually
local).
}
Also of
interset is consideration of $discrete$ time evolution (described by
difference rather than differential equations), though, as usual in the $2d$
theories, this is not a really independent problem.

In the language of matrix models the restriction to $free-fermion$
$\tau$-functions is essentially equivalent to restriction to $eigenvalue$
models. Serious consideration of non-eigenvalue models, aimed at revealing
their integrable (solvable) structure will certainly involve the theory of
generic $\tau$-functions, but both these things are matters of the future
research, and we"ll not go into details about them in these notes.


\subsection{$\tau$-function, associated with the free fermions}

Because of specific form of the Lagrangian in (\ref{fftf}) the functional
integral can be easily represented in Hamiltonian form, provided topology of
the 2-surface on which $\bar z, z$ are coordinates, is trivial
(genus 0: sphere or annulus). Namely, consider $\tilde\psi$ and $\psi$ as
operator-valued functions of $ z$ only (not of the time $\bar z$).
Then the only reminiscent of kinetic term $\int_{d^2 z}
\tilde\psi\bar\partial\psi$ is canonical commutation relation:
\be
\phantom. [\tilde\psi(\tilde z),\psi( z)]_+ =
\delta(\tilde z -  z) d\tilde z^{1/2}d z^{1/2}.
\ee
Then
\be
\tau\{A\} \sim
\langle 0 \mid \exp\left({\oint_{d\tilde z}\oint_{d z}
A( z,\tilde z)\psi( z)\tilde\psi(\tilde z)}\right)
\mid 0 \rangle.
\label{hrtf}
\ee

Now it is usual to expand around $ z = 0$:
\be
&\psi( z) = \sum_{n\in Z}\psi_n z^n d z^{1/2}; \ \ \
\tilde\psi( z) = \sum_{n\in Z}\tilde\psi_n z^{-n-1}d z^{1/2};
\nn \\
&\phantom. [\tilde\psi_m,\psi_n]_+ = \delta_{m,n}; \nn  \\
&\psi_m\mid 0 \rangle = 0 \ \ {\rm for}\ m<0; \ \ \
\tilde\psi_m \mid 0 \rangle = 0 \ \ {\rm for}\ m\geq 0; \nn \\
&A( z,\tilde z) = \sum_{m,n\in Z}  z^{-m-1}\tilde z^n
A_{mn}d z^{1/2}d\tilde z^{1/2}; \nn
\ee
so that
\be
\oint_{d\tilde z}\oint_{d z}
A( z,\tilde z)\psi( z)\tilde\psi(\tilde z) =
\sum_{m,n\in Z}  A_{mn}\psi_m\tilde\psi_n.
\nn
\ee
In fact this expansion could be around $any$ point $ z_0$ and on a
2-surface of any topology: topological effects can be easily included as
specific shifts of the functional $A( z,\tilde z)$ - by combinations
of the "hadle-gluing operators". Analogous shifts can imitate the change of
basic functions $ z^n$ for $ z^{n+\alpha}$ and more complicated
expressions (holomorphic 1/2-differentials with various boundary conditions on
surfaces of various topologies).

One can now wonder, whether $local$ functionals $A( z,\tilde z) =
U( z)\delta(\tilde z- z)d z^{1/2}d\tilde z^{1/2}$
play any special role. The corresponding contribution to the Hamiltonian looks
like\footnote{
Note that normalization factor here is different by a factor of
$\frac{1}{\sqrt{2}}$ from that in discussion of discrete models in sections
2.3, 2.7 and 2.8. This is not just a change of {\it notations}, since Miwa
transformation can lead to different results when this normalization is
changed. See a footnote in section 4.6 below for more detailed discussion.
}
\be
H_{Cartan} =

\oint_{d z}U( z)\psi( z)\tilde\psi( z) =
\oint_{d z} U( z)J( z),
\ee
where
\be
J( z) = \psi( z)\tilde\psi( z) =
\sum_{n\in Z}J_n z^{-n-1}d z
\ee
is the $U(1)_{k=1}$ Kac-Moody current;
\be
J_n = \sum_{m\in Z}\psi_m\tilde\psi_{m+n}; \ \ \ [J_m,J_n] = m\delta_{m+n,0}.
\ee
If scalar function (potential) $U( z)$ is expanded as
$U( z) = \sum_{k\in Z} t_k z^k$, then
\be
H_{Cartan} =

\sum_{n\in Z} t_kJ_k.
\ee
This contribution to the whole Hamiltonian can be considered distinguished for
the following reason. Let us return to original expression (\ref{hrtf}) and
try to consider it as a generating functional for all the correlation
functions of $\tilde\psi$ and $\psi$.
Naively, variation w.r.to $A( z,\tilde z)$ should produce bilinear
combination $\psi( z)\tilde\psi(\tilde z)$ and this would solve the
problem. However, things are not just so trivial, because operators involved
do not commute (and in particular, the exponential operator in (\ref{hrtf})
should still be defined less symbolically, see next subsection). Things would
be much simpler, if we can consider $commuting$ set of operators: this is
where abelian $\hat{U(1)}_{k=1}$ subgroup of the entire $GL(\infty)_{k=1}$
(and even its purely commuting Borel subalgebra) enters the game. Remarkably,
it is sufficient to deal with this abelian subgroup in order to reproduce all
the correlation functions.\footnote{
We once again emphasize that this trick is specific for the free fermions and
for the level $k=1$ Kac-Moody algebras, which can be expressed entirely in
terms of free fields, associated with Cartan generators (modulo some
unpleasant details, related to "cocycle factors" in the Frenkel-Kac
representations \cite{FK},
which are in fact reminiscents of free fields associated with the non-Cartan
generators (parafermions) \cite{Turb}, - but can, however, be put under the
carpet or/and taken into account "by hands" as "unpleasant but
non-essential(?) sophistications).
}
The crucial point is the identity for free fermions (generalizable to any $b,
c$-systems):
\be
:\psi( \lambda)\tilde\psi(\tilde \lambda):\ = \ :\exp\left({

\int_{ \lambda}^{\tilde \lambda} J}\right):
\label{bosid}
\ee
which is widely known in the form of bosonization formulas:\footnote{
Formulas in brackets are indeed correct, before them the usual symbolic
relations are written. Using these formulas we get:
\be
:\psi(\lambda)\tilde\psi(\tilde \lambda):\  = \  :e^{

\phi(\tilde \lambda)-\phi( \lambda)}:\ = \ :e^{

\int_{ \lambda}^{\tilde \lambda} \partial\phi}: \ = \ :e^{

\int_{ \lambda}^{\tilde \lambda} J}:
\nn
\ee
This identity can be of course obtained within fermionic theory, one should
only take into account that $\psi$-operators are nilpotent, so that exponent
of a single $\psi$-operator would be just a sum of two terms (polinomial).
}
if $J( z) = \partial\phi( z)$,
\be
\tilde\psi(\tilde \lambda) \sim \ :e^{

\phi(\tilde \lambda)}:
\ \ \ \left(\ :\psi(\infty)\tilde\psi(\tilde \lambda):\ =\ :e^{

(\phi(\tilde \lambda) - \phi(\infty))}:\ \right); \nn \\
\psi( \lambda) \sim \ :e^{-

\phi( \lambda)}:
\ \ \ \left(\ :\psi( \lambda)\tilde\psi(\infty):\ =\ :e^{

(\phi(\infty) - \phi( \lambda))}:\ \right).
\nn
\ee
This identity implies that one can generate any bilinear combinations of
$\psi$-operators by variation of potential $U( z)$ only, moreover this
variation should be of specific form:
\be
\Delta\oint UJ = \Delta\left( \sum_{k\in Z} t_kJ_k \right) =
\int_{ z}^{\tilde z} J = \sum_{k \in Z}
\int_{ z}^{\tilde z}   z^{-k-1} d z = \nn \\
= \sum_{k \in Z} \frac{1}{k}J_k \left(\frac{1}{ z^k} -
\frac{1}{\tilde z^k}\right),
\nn
\ee
i.e.
\be
\Delta t_k = \frac{1}{k}\left(\frac{1}{ z^k} -
\frac{1}{\tilde z^k}\right)
\ee
Note that this is {\it not} an infinitesimal variation and that it has
exactly the
form, consistent with Miwa parametrization used in the previous section 3.

Since any bilinear combination can be generated in this way from $U( z)$,
it is clear that the entire Hamiltonian $\sum A_{mn}\tilde\psi_m\psi_n$ can be
also considered as resulting from some transformation of $V$ (i.e. of
"time-variables" $t_k$). In other words,
\be
\tau\{A\} = {\cal O}_A[t] \tau\{A = U\}.
\nn
\ee
These operators ${\cal O}_A$ are naturally interpreted as elements of the
group $GL(\infty)$, acting on the "Universal Grassmannian" \cite{SeWi},
\cite{Kac},\cite{Orlov}, parametrized by
the matrices $A_{mn}$ modulo changes of coordinates $ z \rightarrow
f( z)$. This representation for $\tau\{A\}$ is, however, not very
convenient, and usually one considers {\it infinitesimal} version of the
transformation, which just shifts $A$
\be
\tau\{t\mid A+\delta A\} = \hat{\cal O}_{\delta A}[t] \tau\{t\mid A\},
\label{trtf}
\ee
note that this transformation clearly distinguishes between the dependencies
of $\tau$ on $t$ and on all other components of $A$. The possibility of such
representation with the privileged role of Cartan generators is the origin of
all simplifications, arising in the case of free-fermion
$\tau$-functions.\footnote{
It is also the reason, why these are free-fermion $tau$-functions, that appear
in the study of ordinary integrable hierarchies: the Hamiltonian flows,
which describe evolution in different $t$-directions just commute, because
$t$'s are associated with the commuting Cartan generators of $GL(\infty)$. In
the more general situation the flows would form closed but $non-abelian$
algebra.
}

Relation (\ref{trtf}) is the basis of the orbit interpretation of
$\tau$-functions \cite{Kac}. It is also important to understand the role of
the "string equation" and othert constraints, imposed on $\tau$-functions in
the theory of matrix models. These arise as some particular subalgebras in the
set of $\hat{\cal O}$-operators, and their role is to specify particular
points $A$ in the Grassmannian, of which this subalgebra is a
stabilizer.\footnote{
This relation is straightforward in the case of Virasoro constraints, since
Virasoro algebra is just a subalgebra of the $GL(\infty)$ acting on
$\tau$-functions, and thus is a symmetry (covariance) of associated integrable
hierarchies \cite{Orlov}. $W$-constraints do not form Lie-subalgebra of this
$GL(\infty)$, they arise after certain reduction, which in turn exists in a
simple form $not$ everywhere on the Grassmannian
(in particular $W$ is {\it not} a symmetry
of entire KP hierarchy \cite{KodeVo}): here we deal with a more
sophisticated self-consistency relation, which remains to be understood in
full details (e.g., it is unknown, whether reduction exists at least at {\it
any}
Virasoro-stable point, which would significantly simplify this kind of
consideration). In fact, the entire relation between the constraints and
$\tau$-functions is not exhaustively worked out: for example, there is still
no clear and satisfactory proof, that the full set of Virasoro and/or
$W$-constraints implies that partition function is a $\tau$-function, which
would be pure algebraic and not refer to the uniqueness of solutions to the
constraints. Result, widely discussed in the literature, see \cite{FKN},
is that string equation (the lowest Virasoro constraint $L_{-1}Z = 0$), if
imposed on $Z$, which is somehow known to be the properly reduced
$\tau$-function, implies the entire set of Virasoro and $W$-constraints
(though even this proof can still have some loopholes).
}
The simplest examples are in fact provided by formulas from the section 2.3
above, where combinations of the screening charges describe $A$'s, which are
stable points of {\it discrete} Virasoro- and $W$-constraints (in the latter
case the {\it multi}-fermion system is used).

The fact that the $\tau$-function at all the points $A$ of Grassmannian can be
obtained by the group action from $\tau\{0\}$, has an implication, known as
Hirota equation. The idea \cite{Kac} is just that there are Casimir operators
in the group, which commute with the group action and thus the eigenvalue of
the Casimir operator is the same for $\tau\{A\}$ at all $A$. In the
free-fermion case the simplest example of Casimir operator is given by
\be
J_0 = \oint J = \oint\psi\tilde\psi = \sum_{n\in Z} \psi_n\tilde\psi_n.
\ee
The eigenvalue of this operator for the vacuum state $\mid 0 \rangle$ is an
infinite subtraction constant, and this makes equation
$J_0 {\cal O}_A\mid 0 \rangle = {\cal O}_A J_0 \mid 0 \rangle =
{\rm const} \cdot{\cal O}_A\mid 0 \rangle$, or
$J_0\tau\{A\} = {\rm const}\cdot\tau\{A\}$ not very interesting. However, this
operator is represented in bilinear form and in such cases the following trick
is usually usefull.

If operator, which is bilinear in generators of the algebra, $T^aT^a$,
commutes with the action of the group, so does $T^a\otimes T^a$, if the group
action on tensor product of representations is defined as
$\mid\ \rangle\otimes\mid\ \rangle \rightarrow {\cal O}_A\mid\
\rangle\otimes {\cal O}_A\mid\ \rangle$. (Indeed, then
$(T^a\otimes I + I\otimes T^a)^2$ commutes with the group action and so does
$T^a\otimes T^a = \frac{1}{2}\left( (T^a\otimes I + I\otimes T^a)^2 -
T^aT^a\otimes I - I\otimes T^aT^a\right)$.)
If further, $T^a\otimes T^a$ annihilates the product of two vacuum states:
\be
\left(T^a\otimes T^a\right)\ \mid 0 \rangle\otimes\mid 0 \rangle  = 0,
\label{annvac}
\ee
then the same equation holds for all $A$:
\be
\left(T^a\otimes T^a\right)\
\mid {\cal O}_A \rangle\otimes\mid {\cal O}_A \rangle  = 0.
\ee
Condition (\ref{annvac}) is trivially valid in our case:
\be
\sum_{n\in Z} \psi_n \mid 0 \rangle\otimes\tilde\psi_n\mid 0 \rangle  = 0,
\ee
since in every term in the sum one of the vacuum states is annihilated: the
first one of $n\geq 0$ and the second one if $n<0$.\footnote{
It is easy to verify directly that $\sum_n \psi_n \otimes \tilde\psi_n$ is
indeed a Casimir operator in the tensor product:
\be
&\phantom. [\sum_n \psi_n \otimes \tilde\psi_n, \
I\otimes \sum_{l,m} A_{lm}\psi_l\tilde\psi_m +  \sum_{l,m}
A_{lm}\psi_l\tilde\psi_m \otimes I] = \nn \\
&=
\sum_n\left( \psi_n \otimes \sum_m A_{nm}\tilde\psi_m -
\sum_l A_{ln}\psi_l\otimes \tilde\psi_n \right) =
\sum_l\sum_m A_{lm} (\psi_l\otimes \tilde\psi_m - \psi_l\otimes\tilde\psi_m)
= 0. \nn
\ee
}
Thus we obtain the relation
\be
\sum_{n\in Z} \psi_n \mid {\cal O}_A \rangle \otimes
\tilde\psi_n \mid {\cal O}_A \rangle = 0,
\ee
which can be now multiplied from the left by
\be
\langle 0 \mid \psi(\infty) e^{H_{Cartan}(t)} \otimes
\langle 0 \mid\tilde\psi(\infty)  e^{H_{Cartan}(t')}
\nn
\ee
($t'_k$ do not need to coincide with $t_k$) and after insertions of
$\psi$-operators are expressed as the shifts of times, we obtain:
\be
\sum_{n\in Z}  D_n^- \tau\{t\mid A\} \otimes D_n^+ \tau\{t\mid A\} = 0,
\label{prehirota}
\ee
where $\sum_{n\geq 0}D^{\pm}_n z^{-n} =
\exp\left(\pm \sum_{k>0} \frac{1}{k z^k}
\frac{\partial}{\partial t_k}\right)$.
This is particular form of Hirota equation \cite{Hirota},
which is often used to {\it define} $\tau$-functions, associated
with integrable hierarchies. If one takes (\ref{hrtf})
for the definition, as it is more natural to do in the general "theory of
everything" and as we did above, eq.(\ref{prehirota}) is the starting
point for the path, leading to hierarchies in conventional form of
differential equations, the Lax and pseudodifferential representations
{\it naturally} appearing on the way. We do not go along this path in these
notes.

The last remark to be made, before we proceed to more detailed formulas,
is that $\tau$-functions can be considered as determinants $Det \bar\partial$
of the $\bar\partial$-operators acting on fields with some complicated
boundary conditions (like
$\psi( z) \sim \exp\left(\sum_{k>0} t_k z^{-k}\right)$
in the simplest case of $t$-dependencies). Entire A-dependence is usually
described in this context as that on the point of the "universal module space",
which once appeared in the study of string models on Riemann surface of
arbitrary genus \cite{UMS}. From this point of view more general
$\tau$-functions are sections of the bundles over universal module space,
associated with conformal models, more sophisticated then just the theory of
free fermions (and $b,c$-systems). The WZNW model is, of course, the most
important example to be studied in this context.

The crucial feature of all the quantites, associated in this way to conformal
models is applicability of Wick theorem, reducing multipoint correlation
functions to pair correlators. In the free fermion case this is just a
consequence of quadratic form of Lagrangian, in generic situation this follows
from existence of holomorphic operator algebra, which allows to define the
correlators by fixation of monodromy properties, dictated by pairwise
collision of points. Wick theorem is the concrete source of determinant
formulas for $tau$-functions, which are used in order to establish their
relations with matrix models and other branches of string theory.

After this discussion of the context where free-fermion $\tau$-functions
can and do appear, we turn now to more detailed and exact formulas, relevant
in this particular free-fermion case.
They are mostly due to Japanese school \cite{DJKM}, though many other people
contributed to this field after it was established. The only sophisticated
part of the work with these  formulas is accurate accounting for the normal
ordering routine which will be mostly unnecessary for our purposes.
We shall mostly follow the
presentation of papers \cite{KMMOZ},\cite{GKM},\cite{Toda}.
