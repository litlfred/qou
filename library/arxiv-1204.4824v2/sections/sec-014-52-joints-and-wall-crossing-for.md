---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-014-52-joints-and-wall-crossing-for
section_title: "Joints and wall-crossing for"
section_number: 5.2
pages: 23-25
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.995
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:wnet-basics}

Define a \ti{joint} to be a point $z \in C$ where at least two $\cS$-walls intersect.
A joint thus supports at least two charges, say $\bar a \in \Gamma_{ij}(z,z)$ and $\bar b \in \Gamma_{kl}(z,z)$.

\insfig{trajectories-meeting-commuting}{The local picture around a joint where exactly
two $\cS$-walls meet.  We also show two paths $\wp$, $\wp'$ on $C$
which are related to one another by regular homotopy across the joint.}
The simplest situation arises if the joint $z$ supports \ti{only} these two charges, so exactly two $\cS$-walls meet there.  This can only occur if
$i \neq l$ and $j \neq k$.  In that case the local picture around $z$ is as shown in Figure \ref{fig:trajectories-meeting-commuting}.

Now let us consider what happens to the soliton degeneracies $\mu$ as we
move across a joint.  As it turns out, we can answer this question completely
by considering the defect operators attached to the paths $\wp$, $\wp'$ on $C$ shown
in Figure \ref{fig:trajectories-meeting-commuting}.
The requirement of homotopy invariance says that
\begin{equation} \label{eq:flat-simple}
F(\wp, \vartheta) = F(\wp', \vartheta).
\end{equation}
To understand what this really means,
let us evaluate both sides using the rules of \S\ref{subsec:Compute-FP},
and then deform all the resulting paths on $\tilde\Sigma$ so that they run directly into
the joint $z$, with a common tangent vector $\tilde z$ at $z$.
Then we obtain
\begin{multline} \label{eq:x-simp}
\cD(\wp_+) (1 + \mu(a,p) X_{a_{\tilde z}}) (1 + \mu(b,q) X_{b_{\tilde z}}) \cD(\wp_-) = \\
\cD(\wp_+) (1 + \mu(b,q') X_{b_{\tilde z}}) (1 + \mu(a,p') X_{a_{\tilde z}}) \cD(\wp_-).
\end{multline}
The paths $a_{\tilde z}$ and $b_{\tilde z}$ are not composable in either direction
(since $a_{\tilde z}$ runs from $\tz^{(i)}$ to $\tz^{(j)}$ while $b_{\tilde z}$ runs from $\tz^{(k)}$ to $\tz^{(l)}$),
so we have $X_{a_{\tilde z}} X_{b_{\tilde z}} = X_{b_{\tilde z}} X_{a_{\tilde z}} = 0$.  Considering the terms linear in $X_{a_{\tilde z}}$ and $X_{b_{\tilde z}}$ in \eqref{eq:x-simp} then
gives
\begin{align}
 \mu(a,p) &= \mu(a,p'), \\ \mu(b,q) &= \mu(b,q').
\end{align}
In short:  when an $\cS$-wall of type $ij$ and an $\cS$-wall of type $kl$ meet transversely, they
cross without any changes in $\mu$.

\insfig{ijkl-collisions}{The local picture around a
generic collision between three $\cS$-walls.}
A more interesting situation arises when an $\cS$-wall of type $ij$ and an $\cS$-wall of type
$jk$ meet transversely.  Suppose the two walls support charges
$\bar a \in \Gamma_{ij}(z,z)$ and $\bar b \in \Gamma_{jk}(z,z)$.  (Note that in this case
we must have $i \neq k$; otherwise the two walls would obey the \ti{same} differential equation,
and it would be impossible for them to intersect transversely.)
In this case the joint $z$ supports both $\bar a$ and $\bar b$, which are \ti{composable} since $z^{(j)}$ is both
the end of $\bar a$ and the start of $\bar{b}$.  Hence the joint
also supports a third charge $\bar c = \bar a + \bar b \in \Gamma_{ik}(z,z)$, and
so there could be a third $\cS$-wall meeting $z$.  When $\mu$ is generic enough, the
picture is as shown
in Figure \ref{fig:ijkl-collisions}.\footnote{One might think that there is a second, inequivalent
possibility:  one could have
exchanged the $ij$ and $jk$ labels in Figure \ref{fig:ijkl-collisions}.  This gives a new picture, which is not
related to Figure \ref{fig:ijkl-collisions} by a rotation, but \ti{is}
related to Figure \ref{fig:ijkl-collisions} by an orientation-reversing map.  Fortunately, our rules
for computing $F(\wp, \vartheta)$ do not use the orientation of $C$.  So our analysis is fully general.}

The condition
\begin{equation} \label{eq:flat-simple-2}
F(\wp, \vartheta) = F(\wp', \vartheta)
\end{equation}
becomes
\begin{align} \label{eq:x-simp-2}
&\cD(\wp_+) (1 + \mu(a,p) X_{a_{\tilde z}}) (1 + \mu(c,q) X_{c_{\tilde z}}) (1 + \mu(b,r) X_{b_{\tilde z}}) \cD(\wp_-) = \\ \notag
&\cD(\wp_+) (1 + \mu(b,r') X_{b_{\tilde z}}) (1 + \mu(c,q') X_{c_{\tilde z}}) (1 + \mu(a,p') X_{a_{\tilde z}}) \cD(\wp_-).
\end{align}
Using $X_{a_{\tilde z}} X_{b_{\tilde z}} = (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} X_{c_{\tilde z}}$ and $X_{b_{\tilde z}} X_{a_{\tilde z}} = 0$,
\eqref{eq:x-simp-2} implies
\begin{align}
 \mu(a,p') &= \mu(a,p), \\
 \mu(b,r') &= \mu(b,r), \\
 \mu(c,q') &= \mu(c,q) + (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} \mu(a,p) \mu(b,r). \label{eq:cv-wcf}
\end{align}

The result \eqref{eq:cv-wcf}
says that the number of solitons carrying charge $\bar{c}$ changes as we move
the modulus $z$ of the surface defect $\bS_z$ across the joint.
This reflects the phenomenon of decay/formation of bound states between solitons of charges
$\bar{a}$ and $\bar{b}$.  Indeed \eqref{eq:cv-wcf} is the same wall-crossing formula which was
discovered in \cite{Cecotti:1993rm} in the context of pure 2d theories, and was reinterpreted in
the 2d-4d
context in \cite{Gaiotto:2011tf}.  Our derivation of it here, using consistency of the framed 2d-4d
BPS spectrum, is essentially the same as the one given in \cite{Gaiotto:2011tf}.

There are a few important special cases which deserve separate discussion.
One arises when $\mu(c,q)=0$, so that we actually have only two $\cS$-walls intersecting, of
types $ij$ and $jk$.
In this case the situation is as shown in Figure \ref{fig:ijkl-collision-birth}:
the wall $q'$ is born from the joint, and \eqref{eq:cv-wcf} reduces to
$\mu(c,q') = (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} \mu(a,p) \mu(b,r)$.

\insfig{ijkl-collision-birth}{A collision between $\cS$-walls, at which a new $\cS$-wall
is born.}
The reverse situation is also allowed:  if $\mu(c,q) = - (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} \mu(a,p) \mu(b,r)$, then \eqref{eq:cv-wcf} gives
$\mu(c,q') = 0$, so the wall $q$ ``dies'' at the joint,
as shown in Figure \ref{fig:ijkl-collision-death}.
\insfig{ijkl-collision-death}{A collision between $\cS$-walls, at which an $\cS$-wall
dies.}

So far we have described some local properties of $\wnet_\vartheta$ and $\mu$.  In the
next few sections we describe a recipe for explicitly \ti{constructing} them.
