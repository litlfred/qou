---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-033-101-nonabelianization
section_title: "Nonabelianization"
section_number: 10.1
pages: 61-65
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.825
---
\label{subsec:PushAbelian}

We now explain how, given a nondegenerate spectral network $\wnet$ subordinate
to a covering $\Sigma \to C$, and given also a
twisted flat rank 1 connection over $\Sigma$, we
construct a corresponding twisted flat rank $K$ connection over $C$.

By a \ti{twisted flat rank $K$ connection}
over a real surface $S$ we mean a pair of a complex rank $K$ vector bundle
on $\tilde S$ and a flat connection therein, such that the
holonomy around each fiber of $\tilde S$ is $-1$.
This is a very small modification of the usual notion of a rank $K$ connection over $S$.
In particular, given a spin structure on $S$, there is a canonical
isomorphism between the moduli space of twisted flat connections and that
of ordinary connections.\footnote{To obtain this isomorphism we use the fact that
a spin structure is the same thing as a fiberwise double covering of $\tilde S$;
then given a twisted flat connection, pulling back to this double cover gives a new flat
connection with holonomy $+1$ around the fibers, which then descends to a flat connection
over $S$.}
Nevertheless, this slight twisting is important
in the construction we are about to describe.

Now suppose given a rank 1 twisted flat connection $(\CL,\nabla^\ab)$ over $\Sigma$.
Recall that $C'$ denotes $C$ minus the branch points of the covering $\Sigma \to C$.  Let
$\pi: \tilde \Sigma \to \tilde C'$ be the projection.  Then define the complex
rank $K$ vector bundle
\begin{equation}
 E = \pi_*(\CL).
\end{equation}
The fiber of $E$ at any $\tz \in \tilde C'$ is simply
\begin{equation}\label{eq:simple-pushforward}
E_{\tz} = \bigoplus_i \CL_{\tz^{(i)}}.
\end{equation}

Given the flat rank 1 connection $\nabla^\ab$ on $\CL$,
there is a canonical ``pushforward'' flat connection $\pi_*(\nabla^\ab)$ on $E$.
But the reader should beware that $\pi_*(\nabla^\ab)$  is \ti{not} the connection
we are trying to construct.  Indeed, while $\pi_*(\nabla^\ab)$ is flat on $\tilde C'$,
it has nontrivial holonomy around any small loop $\ell_\fb$ in $\tilde C'$ linking
the fiber over a branch point $\fb$; this monodromy is
induced by the permutation of sheets attached to $\fb$.
It follows that $\pi_*(\nabla^\ab)$ cannot be extended
to a flat connection over $\tilde C$, since on $\tilde C$ the loop $\ell_\fb$ would
be contractible.
Our construction will modify $(E, \pi_*(\nabla^\ab))$ in a way
which eliminates this holonomy.

The key is the path-lifting rule $\bF$ defined in \S \ref{subsec:Path-Lifting}.
Let $C'_\wnet := C' \setminus \wnet$.
Given any path $\tilde \wp$ from $\tz_1 \in \tilde C'_\wnet$ to $\tz_2 \in \tilde C'_\wnet$
we have built a formal sum of paths on $\tilde\Sigma$, given by \eqref{eq:F-expand}:
\begin{equation} \label{eq:F-expand-repeat}
 \bF(\tilde \wp, \wnet) = \sum_{\ba} \fro'(\tilde \wp, \wnet, \ba) \bX_{\ba}.
\end{equation}
Each $\ba$ in the sum \eqref{eq:F-expand-repeat}
is a homotopy class of paths on $\tilde\Sigma$ from $\tz_1^{(i)}$
to $\tz_2^{(j)}$ for some $i$, $j$.
Let
\begin{equation}
\bX_\ba(\nabla^\ab) \in \Hom(\CL_{\tz_1^{(i)}}, \CL_{\tz_2^{(j)}})
\end{equation}
denote the parallel transport of $\nabla^\ab$ along any path in the class $\ba$.
The fact that $\nabla^\ab$ is a flat connection implies that $\bX_\ba(\nabla^\ab)$ depends
only on the class $\ba$
and not on the particular path, and the fact that $\nabla^\ab$ has holonomy $-1$
around the fibers of $\tilde \Sigma$ implies that $\bX_\ba(\nabla^\ab)$
obeys the relation \eqref{eq:bold-winding-rule-2}.
Hence the map $\bX_\ba \to \bX_\ba(\nabla^\ab)$ is well defined.

We now define a
new operator $\bF(\tilde \wp, \wnet, \nabla^\ab)$
just by replacing $\bX_\ba \to \bX_\ba(\nabla^\ab)$
in \eqref{eq:F-expand-repeat}:
\begin{equation} \label{eq:pt-exp}
 \bF(\tilde \wp, \wnet, \nabla^\ab) := \sum_{\ba} \fro'(\tilde \wp, \wnet, \ba) \bX_\ba(\nabla^\ab) \in \Hom(E_{\tz_1}, E_{\tz_2}).
\end{equation}
$\bF(\tilde \wp, \wnet, \nabla^\ab)$ has precisely
the formal properties one would expect
if it were the parallel transport operator in some flat vector bundle:  it is homotopy invariant
and behaves properly under composition.
The key to our construction is that indeed
\ti{$\bF(\tilde \wp, \wnet, \nabla^\ab)$ is the parallel
transport operator from $\tz_1$ to $\tz_2$ for a twisted rank $K$
flat connection $({\hat E}, \nabla)$ over $C$.}
$({\hat E}, \nabla)$ will be constructed in an essentially
tautological way to make this sentence true.

The most direct way of building $({\hat E}, \nabla)$ is to construct its
sheaf ${\mathbb F}$ of flat sections, as follows.  For
any open set $\CU \subset \tilde C$, ${\mathbb F}(\CU)$ consists of all sections $\psi$
of $E$ over $\CU \cap \tilde C'_\wnet$ such that
for any path $\tilde \wp \subset \CU$
with endpoints $\tz_1, \tz_2 \in \tilde C'_\wnet$, we have
\begin{equation}
\psi(\tz_1) \bF(\tilde \wp, \wnet, \nabla^\ab) = \psi(\tz_2).
\end{equation}
(Note that the parallel transport acts from the right, in accordance
with Appendix \ref{app:Conv-conv}.)
Any $\psi \in {\mathbb F}(\CU)$ is obviously determined by its value at a single
$\tz_0 \in \CU \cap \tilde C'_\wnet$.  Conversely,
if $\CU$ is contractible, then any chosen $\psi(\tz_0) \in E_{\tz_0}$ can
be extended to $\psi \in {\mathbb F}(\CU)$ (to prove this one uses
the invariance of $\bF(\tilde \wp, \wnet, \nabla^\ab)$ under homotopies of $\tilde \wp$
and the composition law \eqref{eq:composition-bold}.)
So $\mathbb F$ is a locally constant sheaf of $K$-dimensional vector spaces.
Giving such a sheaf is equivalent to giving a rank $K$ vector bundle with
connection; this is our desired $({\hat E}, \nabla)$.

It will be useful in what follows to have a more concrete description of $({\hat E}, \nabla)$.
The stalk of $\mathbb F$ at any $\tz \in \tilde C'_\wnet$ is just $E_{\tz}$, so
on $\tilde C'_\wnet$ we have a canonical isomorphism ${\hat E} \simeq E$.  Moreover, for
paths $\tilde \wp \subset \tilde C'_\wnet$ we have $\bF(\tilde \wp, \wnet) = \bD(\tilde \wp)$,
from which it follows that $\bF(\tilde \wp, \wnet, \nabla^\ab)$ is just the
parallel transport of $\pi_*(\nabla^\ab)$.  So on $\tilde C'_\wnet$ we have
simply $({\hat E}, \nabla) \simeq (E, \pi_* \nabla^\ab)$.
Now, $\tilde C'_\wnet$ is divided into various connected components $\CU_{\alpha}$,
separated from one another by the lifts of walls of $\wnet$, which are topologically cylinders in $\tilde C$.
We want to know how to patch together the bundle ${\hat E}$ across these cylinders.
Given a wall $p_c$ whose lift $\tilde p_c$ separates components $\CU_{\alpha}$ and $\CU_{\beta}$, we define
a section of $\End(E) \vert_{\tilde p_c}$ by
\begin{equation}\label{eq:tran-fn}
 \CT_c^{\alpha,\beta}(\tz) = 1 + \sum_{\nu \in {\CS}_c(z)} \bX_{\ba(\nu, \twp)}(\nabla^\ab)
\end{equation}
where $\twp$ denotes a short path which crosses from
$\tz_1 \in \CU_{\alpha}$ to $\tz_2 \in \CU_{\beta}$,
and we take the limit
as $\tz_1$ and $\tz_2$ approach the common point $\tz$ of $\tilde p_c$.
Recall here that $\CS_c(z)$ is the soliton set of $\wnet$ at $z$ ($\wnet$
is nondegenerate, so only one of the soliton sets is nonempty.)
The bundle ${\hat E}$ can be realized by extending $E$ to the closure of each component
and then gluing along the boundary cylinders:
\begin{equation}
 {\hat E} = \left( \bigsqcup_\alpha E \vert_{\bar \CU_{\alpha}} \right) / \sim
\end{equation}
where the equivalence relation $\sim$ identifies $(\psi, \tz) \in E \vert_{\bar \CU_{\alpha}}$
with $(\CT_{c}^{\alpha,\beta} \psi, \tz) \in E \vert_{\bar \CU_{\beta}}$ whenever $\tz$ lies on the cylinder
$\tilde p_c$.




\subsection{Singularities and flags} \label{sec:flags}

The twisted flat connection $({\hat E}, \nabla)$
produced by our nonabelianization construction carries a
bit of extra structure which will be important in what follows.
In this section we briefly describe it.

Let us consider
$({\hat E}, \nabla)$ in a neighborhood $\CU \subset \tilde C$ of one of the singular points
$\mathfrak{s}_n$.  On $\CU$ we can trivialize the covering $\tilde\Sigma \to \tilde C$ and hence
there is a decomposition into line bundles (cf. \eqref{eq:simple-pushforward}),
\begin{equation} \label{eq:e-simp-decomp}
E = \bigoplus_i \CL^{(i)},
\end{equation}
preserved by the connection $\pi_* \nabla^\ab$.
We do not generally have such a decomposition for
${\hat E}$, because the gluing transformations $\CT^{\alpha,\beta}_c$ mix the
different $\CL^{(i)}$.  Still, the $\CT^{\alpha,\beta}_c$ do preserve some structure, as follows.
Recall that the walls $p_c$ of $\wnet$ which end at $\fs_n$ carry labels $ij$ which
obey a constraint:  both $i$ and $j$ must belong to $o(\fs_n)$ and we must
have $i < j$.  Using \eqref{eq:tran-fn} it then follows that all the
$\CT^{\alpha,\beta}_c$ are ``upper triangular'':
for $i \notin o(\fs_n)$ they preserve $\CL^{(i)}$, and for $i \in o(\fs_n)$ they
preserve the subspace
\begin{equation}
 F^{(i)} = \bigoplus_{j \ge i} \CL^{(j)}.
\end{equation}
So we find that ${\hat E}$ decomposes
over $\CU$ as
\begin{equation} \label{eq:e-decomp}
{\hat E} = \left( \bigoplus_{i \notin o(\fs_n)} \CL^{(i)} \right) \oplus \hat E_{\fs_n}
\end{equation}
where each $\CL^{(i)}$ is $\nabla$-invariant, and
$\hat E_{\fs_n}$ has rank $\abs{o(\fs_n)}$ and
carries various $\nabla$-invariant subbundles $F^{(i)}$.  The ranks of these subbundles
and of their intersections are determined by the structure of the partial ordering in $o(\fs_n)$.

In the simplest case $o(\fs_n)$ is a totally ordered set containing all $K$ sheets.
In that case we may as well identify the labels with integers $1 \le i \le K$,
and write the ordering as $1 < 2 < \cdots < K$.  Then the
extra structure just discussed is simply a $\nabla$-invariant filtration of ${\hat E}$,
\begin{equation}
 0 = F^{(K)}  \subset F^{(K-1)} \subset F^{(K-2)} \subset \cdots \subset F^{(0)} = {\hat E},
\end{equation}
where $F^{(i)}$ has dimension $K-i$.  If the monodromy of $\nabla$ around $\fs_n$ is diagonalizable
with all eigenvalues distinct, then there exist $K!$ such invariant filtrations, and
our construction picks one out of those $K!$.

What we have found is that our construction naturally produces not just $({\hat E}, \nabla)$, but a bit of extra structure around each $\fs_n$, namely the decomposition \eqref{eq:e-decomp} and
the subbundles $F^{(i)}$.  We refer to this extra structure as \ti{flag data}.
