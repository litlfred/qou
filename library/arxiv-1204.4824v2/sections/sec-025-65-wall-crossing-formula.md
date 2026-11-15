---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-025-65-wall-crossing-formula
section_title: "Wall-crossing formula"
section_number: 6.5
pages: 38-40
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.76
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{subsec:2d4d-wcf}

In \S2.3 of \cite{Gaiotto:2011tf}, we wrote a \ti{2d-4d wall-crossing formula}
which should be obeyed by the degeneracies $\mu$ and $\omega$ in any coupled 2d-4d system.
We have given an explicit description of $\mu$ and $\omega$ in the theories we are now considering.
So it is natural to ask whether one can show directly that the $\mu$ and $\omega$ defined here indeed obey this formula.
In a sense, our definition of $\omega$ above was engineered so that this will be true.
We will not be able to give a complete proof here, but let us at least explain the idea.

The basic strategy of proof was already explained in \cite{Gaiotto:2011tf},
as follows.  Let $u = (\phi_2, \dots, \phi_K)$ denote a point of the Coulomb branch.
Let $\wp$ denote a path in $C$ which both begins and ends at
some point $z$.  As we vary the basepoint $z$ we can likewise
deform the path $\wp$ (in a unique way up to homotopy), giving a family of paths $\wp(z)$.
Now let $z$, $\vartheta$ and $u$ vary along small contractible loops $z(t)$, $\vartheta(t)$, $u(t)$
$(0 \le t \le 1)$ in parameter space, with $z(0) = z$,
and consider the corresponding generating functions
$F(\wp(z(t)), \vartheta(t), u(t))$,\footnote{Up until now we have usually represented
these generating functions as $F(\wp, \vartheta)$, holding $u$ fixed and implicit;
but to recover the usual statement of the wall-crossing
formula we have to let $u$ vary.} which we denote simply as $F(\wp, t)$.

Since $t$ is a closed contractible loop we have
\begin{equation} \label{eq:F-conserved}
 F(\wp, t=0)\ =\ F(\wp, t=1).
\end{equation}
On the other hand, as $t$ varies, $F(\wp, t)$ jumps at various critical $t_c$.
These jumps occur either when $z(t)$ crosses an $\cS$-wall in $\wnet_{\vartheta(t)}$
or when $\vartheta(t)$ crosses a $\cK$-wall.  At each critical $t_c$,
the jump of $F(\wp, t)$ is given by an explicit transformation $J(t_c)$ of the formal variables $X_a$.
Writing the total jump as ${\bf J} = \prod_{t_c} J(t_c)$ (with the product taken in order of increasing $t_c$),
\eqref{eq:F-conserved} thus says
\begin{equation} \label{eq:j-f}
 {\bf J}[ F(\wp, t=0) ]\ =\ F(\wp, t=0).
\end{equation}

Now, the statement of the 2d-4d wall-crossing formula is that  ${\bf J}$ is the identity, or more concretely,
\begin{equation} \label{eq:2d4d-wcf}
 {\bf J}[X_a] = X_a \text { for every } a \in \Gamma(z,z).
\end{equation}

The most direct way to obtain \eqref{eq:2d4d-wcf} from \eqref{eq:j-f} would be to show that
any $X_a$ for $a \in \Gamma(z,z)$
can be obtained as a linear combination of the $F(\wp, t=0)$ for various paths $\wp$
from $z$ to $z$.  We have not proven this, and indeed (as one sees by considering simple examples)
it cannot literally be true except under some
restrictions on the type of surface defects $D_n$ we allow; in general we expect to have to extend the set of
allowed $\wp$ to include some paths which run into the surface defects, as we did in \cite{Gaiotto:2010be}.

Even after extending the set of allowed $\wp$ appropriately, it does not appear to be straightforward
to show that any $X_a$ can be obtained as a linear combination of the $F(\wp, t=0)$.  We believe this is
an interesting and important question (related to conjectures of Fock-Goncharov on the relation between
universally positive Laurent polynomials and tropical points; we discussed the $K=2$ case of this connection
in \cite{Gaiotto:2010be}.)
However, we can also propose an alternative ``poor man's'' approach to proving \eqref{eq:2d4d-wcf}.
The idea is that even if we
cannot show that we can express $X_a$ literally as a function of the $F(\wp, t=0)$, we can at least
do so up to at most a finite ambiguity.  More precisely, we claim that
the group $G$ of automorphisms obeying the equation \eqref{eq:j-f} is \ti{finite}.
This point will be explained in \S\ref{sec:dimensions} below.  Assuming it for now, we conclude in particular that ${\bf J}$ is of finite order.
But the automorphisms $J(t_c)$ are all ``upper triangular'', in the sense that each $J(t_c)$
is of the form $1 + X$ where all of the $X$ belong to a common pronilpotent group.
It follows that ${\bf J}$ is also of this form; but then
${\bf J}$ cannot have finite order without being the identity.
