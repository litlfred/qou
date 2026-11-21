---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-005-15-relation-with-hyperbolic-geometry-and-asympto
section_title: "Relation with hyperbolic geometry, and asymptotically sharp bounds"
section_number: 1.5
pages: 5-7
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.965
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.hypgeom}

When $\a=2 \pi i$, the upper bound in Theorem \ref{thm.up} is not
optimal, and does not reveal any relationship between the $\limsup$
and hyperbolic geometry. Our next theorem fills this gap.

\begin{theorem}
\lbl{thm.4}
{\rm (Proof in Section \ref{sub.thm4})}
For every knot $K$ with $c+2$ crossings we have
$$
 \limsup_{n \to \infty} \frac{\log|f_{K,n}(2\pi i)|}{n}
\leq  \frac{v_8}{2 \pi} c,
$$
where
$$
v_8=8 \La(\pi/4) \approx 3.6638623767088760602 \dots
$$
is the volume of the {\em regular ideal octahedron}--see \cite{Th}.
\end{theorem}

Using an ideal decomposition of a knot complement by placing one octahedron
per crossing, it follows that for every knot $K$ with $c+2$ crossings, we have
\begin{equation}
\lbl{eq.vol8}
\vol(S^3-K) \leq v_8 c,
\end{equation}
where $\vol(S^3-K)$ is the hyperbolic volume of the knot complement.
On the other hand, if the volume conjecture holds for $\a=2 \pi i$, then
$$
 \lim_{n \to \infty} \frac{\log|f_{K,n}(2\pi i)|}{n}
= \frac{1}{2 \pi} \vol(S^3-K) \leq \frac{v_8}{2 \pi} c.
$$
One may ask whether \eqref{eq.vol8} (and therefore, whether the
bound in Theorem \ref{thm.4}) is optimal. This may be a little surprising,
since it involves all knots (and not just alternating ones)
and their number of crossings, an invariant that carries little known
geometric information.
In conversations with I.Agol and D.Thurston, it was communicated to us
that the upper bound in \eqref{eq.vol8} is indeed optimal. Moreover a class
of knots that achieves (in the limit) the optimal ratio of volume
to number of crossings is obtained by
taking a large chunk of the following {\em weave}, and closing it up to a knot:
$$
\psdraw{weavelink}{1.7in}
$$
The complement of the weave has a complete hyperbolic structure associated
with the {\em square tessellation} of the Euclidean plane:
$$
\psdraw{weavetilling}{1.7in}
$$
Optimality follows along similar lines as the Appendix of \cite{La},
using a stronger estimate for the lower bound of the volume of Haken
manifolds, cut along an incompressible surface: If M is a hyperbolic
finite volume 3-manifold containing a properly imbedded orientable,
boundary incompressible, incompressible surface $S$, then
$$
\vol(M) \geq \vol(\mathrm{Guts}(M-\mathrm{int(nbd(}S))),
$$
where $\vol$ stands for volume, and the $\mathrm{Guts}$ terminology
are defined in \cite{Ag}. The proof of this
 stronger statement (of
Agol-Dunfield-Storm-W.Thurston \cite{ADST}) uses, among other
things, work of Perelman.




The reader may compare \eqref{eq.vol8} with the following result of
Agol-Lackenby-D.Thurston \cite{La}:  If $K$ is an alternating knot
with  a planar projection having $t$ twist, then
$$
v_3 (t-1)/2 <  \vol(S^3-K) < 10 v_3 (t-1),
$$
where $v_3=2 \La(\pi/3)\approx 1.01494\dots$ is the volume of the regular ideal
tetrahedron.
Moreover, the class of knots obtained by Dehn filling on the {\em chain link}
has asymptotic ratio of volume by twist number equal to $10 v_3$.
The corresponding tessellation of the Euclidean plane is given by the
{\em star of David}.




So far, we have formulated a Generalized Volume Conjecture for $\a$
near $0$ and $\a$ near $2\pi i$, using representations near the
trivial or near the discrete faithful. How can we
connect these choices for other complex angles $\a$? A natural
answer to this question requires analyzing asymptotics of solutions
of difference equations with a parameter. This is a different
subject that we will not discuss here; instead we will refer the
curious reader to \cite{GG}, and forthcoming work of the first
author. For a further discussion, see also Section
\ref{sec.physics}.
