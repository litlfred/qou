---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-017-43-boundary-bound
section_title: "Boundary bound"
section_number: 4.3
pages: 21-28
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.779
latex_coverage_ratio: 0.991
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
\label{subsec:bd}

In this subsection, we will show that

there exists a parameterization of the cone deformation such that the
sum of the terms $b_j$ is of order $n$.  We first need two lemmas.
Lemma \ref{lemma:b_j-bound} gives us an initial bound on each $b_j$.
Lemma \ref{lemma:choose-S} will allow us to improve this bound.  It is
in the proof of Lemma \ref{lemma:b_j-bound}, giving the initial bounds
on the $b_j$, that we use the positivity result of Lemma
\ref{lemma:Vnonempty}.

Finally, in Theorem \ref{thm:bound-bdry-time} at the end of this
subsection, we put these lemmas together to record the main result of
the section: the bound on the sum $\sum b_j$.

\begin{lemma}
  Suppose we have a cone deformation given as a linear combination of
  deformations, as above, where cone angles go from $0$ to $2\pi$
  along the singular locus.  Suppose also that $S=(s_1, \dots, s_n)$
  is chosen such that for each time $t$, $b_j(S)\geq 0$ for all $j$.
  Suppose the tube radius $R$ is bounded below by $R_1 \geq 0.56$ for
  each $t$.  Then
  $$b_j(S) \leq s_j^2 \,C(R_1),$$
  where $C(R_1)$ is a function of $R_1$
  alone which approaches $0$ as $R_1$ approaches infinity.
\label{lemma:b_j-bound}
\end{lemma}

\begin{proof}
  First, since we're considering a fixed $V_j$, we will drop the
  subscript $j$ in our notation throughout the proof (i.e. $V_j=V,$
  $(\eta_0)_j = \eta_0,$ $s_j=s,$ etc).
  
  Modify a calculation (p. 382 and 383 of \cite{hk:univ}) to include
  $s$, and equation (17) of that paper can be written:
$$\frac{b_j(S)}{\mbox{Area}(\partial V)}\; \leq \;\frac{s^2}{8m^4},$$
where
$m = \alpha\sinh^2 R$ is the length of a meridian on $\partial U$.

We will bound the term $\mbox{Area}(\partial V)\, s^2/(8m^4)$.

Let $A=\mbox{Area}(\partial V)$.  Let $h$ denote the height of
$\partial V$, i.e. the length of an arc perpendicular to the
meridian.  So $h=\ell\cosh R$, where $\ell$ is the length of the
singular locus of the solid torus $V$, and $A=mh$.

Consider
$$\Phi = \frac{8m^4}{A} = \frac{8m^3}{h} =
\frac{8\alpha^3\sinh^3R}{\ell\cosh R}.$$
We will bound $\Phi$ below, therefore bounding its reciprocal above.

Let
$$\Upsilon(R) = \frac{3.3957 \tanh R }{2\cosh 2R}.$$
It was shown in
\cite{hk:univ} (see Theorem 4.4, Corollary 5.1, and the comments on
the multicusp case on p. 411), that $\alpha\ell \geq \Upsilon(R)$.

Then
$$\Phi = \frac{8\alpha^3\sinh^3R}{\ell\cosh R} =
\frac{4\alpha^3}{\ell}\,\frac{1}{\Upsilon(R)}\,g(R)$$
where
$$g(R) = \frac{2\Upsilon(R)\sinh^3R}{\cosh R} = 2\Upsilon(R)\tanh R\sinh^2
R = \frac{3.3957 \tanh^4 R}{1+\tanh^2 R}.$$

So $$\Phi \geq \frac{4\alpha^3}{\ell}\,\frac{1}{\alpha\ell}\,g(R) =
4\left(\frac{\alpha}{\ell}\right)^2g(R).$$

Note that $g(R)$ is increasing with $R$.  Hence since $R\geq R_1$,
$g(R)$ is bounded below by $g(R_1)$.  Thus we focus on the term
$\alpha/\ell$ in $\Phi$.

Define $u=\alpha/\ell$.  In our hyperbolic cone deformation, the
initial cone angle $\alpha$ is zero.  As $\alpha$ approaches $0$, $u$
approaches $L_0^2$, where $L_0$ is the normalized length of the
curve which becomes the meridian (i.e. bounds a singular solid disc)
under the cone deformation (see equation (37) of \cite{hk:univ}).  We
will estimate $u=(u_0 + \Delta u) = (L_0^2+\Delta u)$.

Reworking the calculations of \cite{hk:univ} to include the speed $s$,
and taking derivatives with respect to cone angle $\alpha$ rather than
time, we may rewrite Proposition 5.6 of that paper as:
$$\frac{1}{\alpha}\,\frac{du}{d\alpha} \geq -\frac{2(1+\tanh^2 R)}
{3.3957\tanh^3R} = -\frac{2\tanh R}{g(R)},$$
provided that $R\geq
R_1\geq 0.531$.

It is at this step, to use Proposition 5.6 of \cite{hk:univ}, that we
have required $S$ to be chosen so that $b_j(S) > 0$.

Thus
$$\Delta u \geq \int_{\alpha=0}^{\alpha=2\pi} -2\alpha\frac{\tanh
  R}{g(R)} d\alpha \geq
-\frac{\tanh R_1}{g(R_1)}\int_{0}^{2\pi} 2\alpha d\alpha =
-(2\pi)^2\frac{\tanh R_1}{g(R_1)}.$$

So
$$u^2 \geq (L_0^2 - (2\pi)^2\tanh(R_1)/g(R_1))^2,$$
provided the term
$L_0^2 - (2\pi)^2\tanh(R_1)/g(R_1)$ is non--negative.  We can ensure
this quantity is non--negative by ensuring $L_0^2$ is large.  This can
be done following \cite{hk:univ}.  The following result is essentially
equation (47) of that paper.

\begin{equation}
L_0^2 \geq \frac{2(2\pi)^2}{3.3957(1-\tanh R)}
  \exp\left( \int_1^{\tanh R} F(w) dw\right) = I(R),
  \label{eq:Lhat_int}
\end{equation}
provided the tube radius is at least $R$ throughout the deformation.
Here $F(w) = -(1+4w+6w^2+w^4)/((w+1)(1+w^2)^2)$ is an integrable
function.

The right hand side $I(R)$ of (\ref{eq:Lhat_int}) is increasing with
$R$, so it can be bounded below by a constant in terms of $R_1$.
$$L_0^2 \geq I(R_1)$$

Now if $R_1\geq 0.56$, then 
$I(R_1) - 2(2\pi)^2\tanh(R_1)/g(R_1) \geq 0$.

Putting this together,
$$\Phi \geq 4\left(I(R_1)-(2\pi)^2\frac{\tanh R_1}{g(R_1)}\right)^2
g(R_1).$$
The right hand side of the above equation is a constant,
$\tild{C}_0(R_1)$.

Thus we have
$$b_j(S) \leq \frac{A}{8m^4}\,s^2 =
  \frac{1}{\Phi}\,s^2 \leq \frac{s^2}{\tild{C}_0(R_1)} = s^2\,C(R_1).$$
\end{proof}




The result of Lemma \ref{lemma:b_j-bound} gives us a bound on the sum
of the $b_j$ in terms of $\bar{s}$.  If we could choose $\bar{s} = (1,
\dots, 1)$ (all cone angles increasing at the same rate), then Lemma
\ref{lemma:b_j-bound} would give a bound on $\sum b_j$ of order $n$.
However, our choice of $\bar{s}$ comes from Lemma
\ref{lemma:Vnonempty}.  By the proof of that lemma, we may assume only
that $\bar{s}$ is in the simplex $T=\{\bar{s}\, |\, \sum s_j=n,
s_j\geq 0\}$.  A priori, $\bar{s}$ could be close to a vertex of $T$,
say $(n, 0, \dots, 0)$, in which case Lemma \ref{lemma:b_j-bound}
gives only a bound of order $n^2$ on $\sum b_j$.

For our applications, we need the bound of order $n$.  We will obtain
this better estimate by again revisiting the choice of the point
$\bar{s}=(s_1, s_2, \dots, s_n)$.  This is done in Lemma
\ref{lemma:choose-S}.  


\begin{lemma}
  There exists a point $S=(s_1, \dots, s_n)$ in $T$ such that each
  $b_j(S)\geq 0$, $j=1, \dots, n$, and for any index $j$ with $s_j
  \neq \min\{s_1, \dots, s_n\}$, we have $b_j(S)=0$.
\label{lemma:choose-S}
\end{lemma}

\begin{proof}

First we set up some notation.

\begin{notation}
  Let $B = \{\bar{s}\, |\, b_j(\bar{s}) \geq 0, j=1, \dots, n\}$ (so
  the interior of $B$ is the set $B_n$ of Lemma
  \ref{lemma:sub-vnonempty}).  Again we may normalize such that the
  points $\bar{s}$ lie in the simplex $T= \{(s_1,\dots,s_n)| \sum s_i
  = n, s_i\geq 0\}$.
  
  We define some sets in $B$.  For each $j=1, 2, \dots, n$, let $e_j$
  be the set of all points in $B$ such that $b_j>0$ and for $i\neq j$,
  $b_i=0$.  Note for $j=n$, $e_n$ corresponds to the set $E_n$ in
  Lemma \ref{lemma:sub-vnonempty}.  (So in particular, $e_n$ consists
  of an odd number of points.)
  
  Let $b_{\{i,j\}}$ be the set $b_{\{i,j\}} = B\cap (\cap_{k\neq i,j}
  \{b_k=0\})$.  Note $b_{\{i,j\}}$ has dimension $1$, with components with
  boundary in $e_i$ and $e_j$.
  
  In general, let $I$ be a $k$-element subset $I= \{i_1, i_2, \dots,
  i_k\} \subseteq \{1, \dots, n\}$.  Let $b_I = B\cap(\cap_{j\notin I}
  \{b_j=0\})$.  Notice $b_I$ is bounded by components $b_{I_j}$ where
  $j\in I$, and $I_j$ is the $(k-1)$-element set obtained by removing
  $j$ from $I$.
  
  Now we define some sets in the simplex $T = \{\bar{s}| \sum
  s_i=n\}$.  Let $T_i$ be the region in which $s_i\leq s_j$ for all
  indices $j$.  $T_i$ has dimension $n-1$.  Let $T_{\{i,j\}} = T_i
  \cap T_j$.  Thus each $T_i$ is bounded by faces $T_{\{i,j\}}$ where
  $j$ ranges over all elements of $\{1, \dots, n\}-\{i\}$, as well as
  faces on $\partial T$.  Generally,
  let $I$ be a $k$-element subset of $\{1, \dots, n\}$.  Let $T_I =
  \cap_{j\in I} T_j$.  Note the boundary faces of $T_I$ are the faces
  given by $T_{I\cup\{k\}}$, where $k$ ranges over all elements of
  $\{1, \dots, n\} - I$, as well as faces in $\partial T$.  See Figure
  \ref{fig:lemma-fix} for an illustration when $n=3$.
\end{notation}

\begin{figure}
	
	\caption{Faces $T_I$ illustrated when $n=3$.}
	\label{fig:lemma-fix}
\end{figure}

We will make transversality assumptions that allow us to ignore the
boundary faces of $T_I$ on $\partial T$.  In particular, assume that
$B$ lies in the interior of $T$, so the sets $b_I$ do not meet
$\partial T$.  If this is not the case, we may apply the argument
below to level sets $b_I = \epsilon$, then take the limit as $\epsilon
\to 0$.  Since $B$ is closed, we will obtain the desired result.
Similarly, we will assume that the $b_I$'s and the $T_I$'s all
intersect transversely.

We will use the transversality assumption that $B$ does not meet
$\partial T$ in the arguments below.  In particular, we will be
considering the intersection of subsets of $B$ with boundary faces of
$T_I$.  Since $B$ does not meet $\partial T$, this allows us to ignore
the faces of $T_I$ which lie on $\partial T$ in our argument.





Now, note the lemma will be immediately true if we can find some index
$j$ such that $e_j$ is in the region $T_j$: for on $e_j$, $b_i=0$ for
all $i\neq j$, and in $T_j$, $s_j$ is minimum.  So assume this never
happens.

Generally, if for some $k$-element set $I \subseteq \{1, \dots, n\}$,
$b_I \cap T_I$ is nonempty, we obtain a point which satisfies the
lemma.  So we will assume this also never happens.  We will show that
in this case, the point $(1, 1, \dots, 1)$ is in $B$, thus concluding
the proof.  To prove this, we need another sublemma.

\begin{lemma}
Let $\#(\cdot)$ denote the number of elements of a finite set.
Assuming that 
each 
$b_I \cap T_I$ is empty, 
$$\sum_I \#(b_{I\cup\{n\}} \cap \partial T_I) \equiv \sum_{J}
\#(b_{J\cup\{n\}} \cap \partial T_J) \equiv 1 \mod 2,$$
where the first
sum is over all $(k+1)$-element subsets $I$ of $\{1, \dots, n-1\}$,
and the second sum is over all $k$-element subsets $J$ of $\{1, \dots,
n-1\}$.
\label{lemma:inductive-S}
\end{lemma}

Check that the statement of the lemma makes sense:  Note if $J$ is a
$k$-element set, then $b_{J\cup\{n\}}$ is $k$-dimensional.  $T_J$ is
$(n-k)$ dimensional, so its boundary faces are $(n-k-1)$-dimensional.
Thus the intersections in the statement of the lemma are
$0$-dimensional manifolds, consisting of a finite number of
points.

Also notice that when $k=(n-2)$ in the above lemma, there exists only
one $(k+1)$-element subset $I$, namely $I=\{1, \dots, n-1\}$.  So
$b_{I\cup\{n\}}$ is the whole set $B$.  On the other hand, the
boundary $\partial T_I$ in this case must be the point in the
intersection of all the $T_i$, or the point $(1, \dots, 1)$.  Thus the
first sum counts the number of times the point $(1, \dots, 1)$ appears
in $B$.  Hence showing this number is odd will finish the
proof of Lemma \ref{lemma:choose-S}.


\begin{proof}
We prove Lemma \ref{lemma:inductive-S} by induction on $k$.

We start by showing what essentially is the case $k=0$.  That is, we
show
$$\sum_{i=1}^{n-1} \#(b_{\{i,n\}} \cap \partial T_i) \equiv
\sum_{i=1}^{n-1} \#(e_n \cap T_i) \mod 2.$$

Since we are assuming $e_n \cap T_n = \emptyset$, the second sum in
the above equation is just the number of points of $e_n$ (since $e_n$
is disjoint from each $T_i \cap T_j$ by transversality).  That number
of points is odd by Lemma \ref{lemma:sub-vnonempty}, so this will give
us the basis step of our induction.

Consider $b_{\{i, n\}} \cap T_i$.  This is a 1--manifold, consisting
of closed curves and arcs.  Each arc has two endpoints.  So
$$\sum_{i=1}^{n-1} \#\partial(b_{\{i,n\}} \cap T_i) \equiv 0 \mod 2$$

On the other hand,
$$\sum_{i=1}^{n-1} \#\partial(b_{\{i,n\}} \cap T_i) =
\sum_{i=1}^{n-1} \#(\partial b_{\{i,n\}} \cap T_i) +
\sum_{i=1}^{n-1} \#(b_{\{i,n\}} \cap \partial T_i).$$
So $\sum_{i\neq n} \#(b_{\{i,n\}} \cap \partial T_i)$ has the same
parity as $\sum_{i\neq n} \#(\partial b_{\{i,n\}} \cap T_i)$.

Consider $\partial b_{\{i,n\}} \cap T_i$.  Note $\partial b_{\{i,n\}}$
consists of points in $e_i$ and $e_n$.  By assumption, $e_i$ is never
in $T_i$.  Thus
$$\sum_{i=1}^{n-1} \#(\partial b_{\{i,n\}} \cap T_i)
= \sum_{i=1}^{n-1} \#(e_n \cap T_i) = \#(e_n).$$
So $\sum_{i\neq n} \#(b_{\{i,n\}} \cap \partial T_i)$ is odd.

Our proof for general $k$ follows essentially the same lines as the
proof above.

Suppose $1\leq k \leq n-2$.  We need to show
$$\sum_I \#(b_{I\cup\{n\}} \cap \partial T_I) \equiv \sum_{J}
\#(b_{J\cup\{n\}} \cap \partial T_J) \mod 2,$$
where the first sum is over $(k+1)$-element subsets of $\{1, \dots,
n-1\}$ and the second is over $k$-element subsets.

Fix some $(k+1)$-element subset $I$, and again consider
$b_{I\cup\{n\}} \cap T_I$.  This is a 1--manifold.  Its components are
closed curves and arcs.  Again the number of endpoints of
these arcs is even.  So when we sum over all such $I$, 
$$\sum_I \#\partial(b_{I\cup\{n\}} \cap T_I) \equiv 0 \mod 2.$$

On the other hand, 
$$\sum_I \#\partial(b_{I\cup\{n\}} \cap T_I) =
\sum_I \#(\partial b_{I\cup\{n\}} \cap T_I) +
\sum_I \#(b_{I\cup\{n\}} \cap \partial T_I).$$

Thus we consider $\sum_I \#(\partial b_{I\cup\{n\}} \cap T_I).$ We
want it to have the same parity as $\sum_J \#(b_{J\cup\{n\}} \cap
\partial T_J)$, where $J$ ranges over all $k$-element subsets of $\{1,
\dots, n-1\}$.  We show now that the two sums are actually equal,
which concludes the proof.

Consider $\partial b_{I\cup \{n\}}$.  This consists of $b_I$, as well
as things of the form $b_{{I_j}\cup\{n\}}$ where $I_j$ is the
$k$-element set obtained from $I$ by removing the element $j\in I$.
Since by assumption, $b_I \cap T_I$ is empty, $\partial b_{I\cup\{n\}}
\cap T_I$ is the union of sets $b_{{I_j}\cup\{n\}} \cap T_I$, where
$j$ ranges over all elements of $I$.

Then
\begin{equation}
\sum_I \#(\partial b_{I\cup\{n\}} \cap T_I) = \sum_I \sum_{j\in I}
\#(b_{{I_j}\cup\{n\}} \cap T_I).
\label{eqn:count1}
\end{equation}

We will change our method of counting in (\ref{eqn:count1}) above.
Replace the terms $I_j$ with $k$-element subsets $J$ of $\{1, \dots,
n-1\}$.  We will run through all such $J$.  Then $I$ will run through
the $(k+1)$-element subsets given by $J\cup\{i\}$, where $i$ is some
element of $\{1, \dots, n-1\} - J$.  So the right hand side of
equation (\ref{eqn:count1}) is equal to
$$\sum_J \sum_{i\in\{1,\dots,n-1\}-J} \#(b_{J\cup\{n\}} \cap
T_{J\cup\{i\}}).$$

On the other hand, we know the boundary $\partial T_J$ is equal to the
union of all faces $T_{J\cup\{j\}}$, where $j$ ranges over all
elements of $\{1, \dots, n\}-J$.  The only such face we are missing in
our sum above is $T_{J\cup\{n\}}$.  But by assumption, the
intersection of $b_{J\cup\{n\}}$ with $T_{J\cup\{n\}}$ is trivial.
Thus
$$\sum_J \sum_{i\in\{1,\dots,n-1\}-J} \#(b_{J\cup\{n\}} \cap
T_{J\cup\{i\}}) = \sum_J \#(b_{J\cup\{n\}} \cap \partial T_J).$$
\end{proof}

This concludes the proof of Lemma \ref{lemma:choose-S}.
\end{proof}



Lemmas \ref{lemma:b_j-bound} and \ref{lemma:choose-S} together give
the desired bound on $\sum b_j$:

\begin{theorem}
  Let $X$ be a hyperbolic manifold with $n+k$ cusps connected to a
  manifold $M$ with $k$ cusps by a cone deformation.  (So in
  particular, there are $n$ components of the singular locus, and cone
  angles at each component go from $0$ to $2\pi$.)  Suppose during the
  deformation, the tube radius about the singular locus remains larger
  than $R_1 \geq 0.56$.


	Then the deformation can be parameterized so that at each time: $\min
	s_j =1$ and the sum of the boundary terms satisfies
  $$\sum_{j=1}^n b_j \leq n\,C(R_1).$$
  Moreover, we can assume the
  deformation has reached the hyperbolic structure on $M$ by time
  $t=(2\pi)^2$.
  \label{thm:bound-bdry-time}
\end{theorem}

\begin{proof}
  
  By Lemma \ref{lemma:choose-S}, we may find a value $S$ in $T$ such
  that each $b_j(S) \geq 0$ and such that if for any index $j$, $s_j
  \neq \min\{s_1, \dots, s_n\}$, then $b_j(S)=0$.  Denote the minimum
  value of the $s_j$ by $s$: $s=\min\{s_1,\dots, s_n\}$.  Then Lemma
  \ref{lemma:b_j-bound} implies that
\begin{equation}
  \sum_{j=1}^n b_j = \sum_{\{j|b_j\neq 0\}} b_j \leq \sum_{\{j|b_j\neq
  0\}} s^2\,C(R_1) \leq n s^2\,C(R_1).
\label{eqn:sum-b_j}
\end{equation}

First, we need to check that $s$ is not equal to zero.  Suppose not.
That is, suppose $s=0$.  Then by (\ref{eqn:sum-b_j}), $\sum_{j=0}^n
b_j = 0$.  Recall that by equation (\ref{eqn:b_j>0}) and the remark
right after it, the sum of all $b_j$'s equal zero only if the entire
deformation is trivial.  But this is possible only if each $s_j=0$.
Since the point $(0, 0, \dots, 0)$ is not in the simplex $T$, this is
impossible.

Now, recall the terms $s_j$ affect the rate of change of the
deformation.  Thus we may rescale them without changing the tube
radius.  For the point $S$ in $T$, divide each $s_j$ by $s$.
Replace $S$ by this rescaled point, and denote the rescaled
point by the same notation: $S=(s_1, \dots, s_n)$.  So each $s_j\geq
1$.  Also, $s=\min\{s_j\}=1$.

Thus equation (\ref{eqn:sum-b_j}) gives:
$$\sum_{j=1}^n b_j \leq n\,C(R_1).$$
  
Finally, to notice that the deformation is complete by time
$t=(2\pi)^2$ as claimed, recall that if $s_j=1$ throughout the
deformation, then the cone angle is changing at a rate at which
$\alpha_j$ will reach $2\pi$ at time $t=(2\pi)^2$.  (See the
discussion at the beginning of \S\ref{subsec:convex}.)  Since $s_j\geq
1$ always, the rate of change may only be faster.  Thus each cone
angle reaches $2\pi$ by the time $t=(2\pi)^2$.
\end{proof}

When we combine Theorem \ref{thm:bound-bdry-time} with the results of
Theorem \ref{thm:cusp-1} and Theorem \ref{thm:norm-length-1}, we have
completed the proofs of Theorems \ref{thm:main-cusp} and
\ref{thm:main-norm-length}.






\section{Bounding the meridian \label{sec:merbound}}
We now show that the length of the shortest nontrivial simple closed
curve on the cusp torus is bounded throughout the cone deformation,
provided the tube radius about the singular locus stays large.  Recall
here that we are calling this shortest curve the meridian of the
torus.  The following lemma is the last piece needed to complete the
proof of Theorem \ref{thm:main-norm-height}.

\begin{lemma}
Suppose $M$ is a hyperbolic cone manifold with one cusp, and with
singular locus $\Sigma$.  Suppose the tube radius $R$ about the
singular locus is at least $\log(2/\sqrt{3})$.  Then there exists a
horoball neighborhood $U$ of the cusp such that the meridian of
$\partial U$ has length at least $1-e^{-2R}$.
  \label{lemma:meridian-bound}
\end{lemma}

\begin{proof}
Let $X = M-\Sigma$.  $X$ admits an incomplete hyperbolic metric.
Expand the tube $V = \cup V_i$ about the
singular locus $\Sigma$ until the tube hits itself.  Each $V_i$ has
the same tube radius $R$.  Next expand the horoball $U$ about
the cusp until it either becomes tangent to itself or to $V$.

We obtain a region $\Omega$ by continuing to expand $U$ as follows.
First, choose a particular lift $U_a$ of $U$ in the universal cover.
Because $U$ is embedded in $\HH^3$ by the developing map on the
universal cover $\widetilde{X}$ of $X$, we can assume the developing
map is one to one on $U_a$ and takes $\partial U_a$ to the plane $z=1$
in $\HH^3$.

Take $\Omega= U_a \cup S$, where $S$ is the set consisting of all
points $x$ in $\tild{X}$ such that the distance $\mbox{dist}(x,
\partial U_a) < \mbox{dist}(x, \partial U_b)$ for $U_b$ any other lift
of $U$, and also such that the distance $\mbox{dist}(\phi(x), \partial
U) < \mbox{dist}(\partial U,\Sigma)$, where $\phi$ is the covering
projection. Note that $\Omega$ is embedded in $\HH^3$ by the
developing map.  That is, the developing map is one to one on
$\Omega$.

Let $p$ be a point on $\partial U$ closest to $\Sigma$, and let $p_0$
and $p_1$ be lifts of $p$ on $\partial U_a$ such that the projection
of the path from $p_0$ to $p_1$ is shortest on $\partial U$.  Let
$a_0$ be the point in the universal cover on a lift of $\Sigma$ such
that the path from $p_0$ to $a_0$ has length equal to the minimum
distance from $p_0$ to $\Sigma$.  Similarly, let $a_1$ be the point on
a lift of $\Sigma$ such that the path from $p_1$ to $a_1$ has length
equal to the minimum distance from $p_1$ to $\Sigma$.  Note the
interiors of the paths between $p_0$ and $a_0$ and between $p_1$ and
$a_1$ are contained in $\Omega$. 

\begin{figure}
  \begin{center}
  
  \end{center}
  \caption{The top edge of the quadrilateral maps to the shortest path
  on $\partial U$ under the covering projection. }
  \label{fig:area-quad}
\end{figure}

Then note the interior of the geodesic $\beta$ from $a_0$ to $a_1$ is
also in $\Omega$, along with all the points in the quadrilateral with
sides given by $\beta$ and the paths from $p_0$ to $p_1$, from $p_0$
to $a_0$, and from $p_1$ to $a_1$.  This is because, first, all points
$x$ in this quadrilateral (except the endpoints of $\beta$) have
$\mbox{dist}(\phi(x), \partial U) < \mbox{dist}(\partial U, \Sigma)$.
Also, if any $x$ were closer to some other lift $U_b$ of $U$, then
there would be points in the quadrilateral equidistant to two
different lifts of $U$.  All points equidistant to two different lifts
of $U$ lie on some totally geodesic planes of $\HH^3$.  Hence some
geodesic must intersect $\beta$ but not the paths from $p_0$ to $a_0$,
$p_1$ to $a_1$, or the path on the horosphere $\partial U_a$ from
$p_0$ to $p_1$.  This is impossible.

Now let $H$ be the length of the paths from $p_0$ to $a_0$ and from
$p_1$ to $a_1$.  Let $L$ be the length of $\beta$.  We know that
$H\geq R$ and $L\geq 2R$ since the distance between any two components
of the lift of $\Sigma$ is greater than or equal to $2R$.  We let $d$
be the length of the path on the horosphere $\partial U_a$ between
$p_0$ and $p_1$.  Since $\Omega$ is embedded by the developing map, we
can assume the quadrilateral is of the form shown in Figure
\ref{fig:area-quad}.

Then solving for $d$ in terms of $H$ and $L$, $d= 2e^{-H}\sinh(L/2)$.

Case 1:  $H=R$.  Then $d \geq 2e^{-R}\sinh(R) = 1-e^{-2R}$.

Case 2: $H>R$ Then $U$ must be tangent to itself, say at a point $q$,
and not necessarily tangent to the tube about $\Sigma$.  Then the
image of $\Omega$ under the developing map must contain some portion
of the region above the geodesic surface equidistant from a horizontal
plane (the lift of $\partial U_a$) and some other horosphere.

This geodesic surface is some portion of the (Euclidean) hemisphere
with radius $1$, tangent to the lift of $\partial U_a$ at a lift $q_0$
of $q$.  See Figure \ref{fig:d-long}.  The image of $\Omega$ under the
developing map contains a neighborhood of points on this hemisphere
about $q_0$.  If it were to contain all the points on the hemisphere
between the dotted lines in Figure \ref{fig:d-long} (that is, points
whose projection to $\CC$ have Euclidean distance at most $1/2$ from
the projection of $q_0$ to $\CC$), then $d\geq 1$.

Let $x$ be one of these points.  That is, the projection of $x$ to
$\CC$ has Euclidean distance at most $1/2$ from the projection of
$q_0$ to $\CC$.  Note $x$ will lie in $\Omega$ provided
$\mbox{dist}(\phi(x), \partial U) < \mbox{dist}(\partial U, \Sigma) =
H$, or provided $H$ is large enough.  But now, $\mbox{dist}(\phi(x),
\partial U) = \log( 1/\mbox{height}(x))$, where $\mbox{height}(x)$
denotes the $z$--coordinate of $x$ in $\HH^3$.  Thus this distance is
at most $\log(2/\sqrt{3})$.

\begin{figure}
	
\caption{}
\label{fig:d-long}
\end{figure}

Since $H>R$, we can ensure $d\geq 1$ by restricting to $R\geq
\log(2/\sqrt{3})$.
\end{proof}

When we plug the result of Lemma \ref{lemma:meridian-bound} into
Theorem \ref{thm:norm-height-mer}, along with the bound on $\sum b_j$
of the previous section, we may complete the proof of Theorem
\ref{thm:main-norm-height}.

\medskip

\noindent\textbf{Theorem \ref{thm:main-norm-height}.} \emph{
  Let $M=X_\tau$ be a hyperbolic 3--manifold with a cusp, and let
  $X=X_0$ be a hyperbolic 3--manifold which can be joined to $M$ by a
  smooth family of hyperbolic cone manifolds $X_t$ with tube radius at
  least $R_1 \geq 0.56$, and with $n$ components of the singular
  locus. Let $U_t$ be a horoball neighborhood about
  the cusp.  Let $h(M)$ denote the normalized height of the cusp torus
  $\partial U_\tau$.  Let $h(X)$ denote the normalized height of
  $\partial U_0$.  Then the

	hyperbolic cone deformation can be parameterized such that the

	change in normalized height is bounded in
  terms of $R_1$ alone:
$$-(2\pi)^2\frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}} \leq
 h(M) - h(X) \leq
(2\pi)^2\frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}}.$$
}

\begin{proof}
  Theorem \ref{thm:norm-height-mer}, combined with Theorem
  \ref{thm:bound-bdry-time} and Lemma \ref{lemma:meridian-bound}
  imply that
$$
  -\frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}} \leq \dot{h} \leq
\frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}}
$$
and that the total time of the deformation is $t=(2\pi)^2$.  We
integrate the above inequality over the deformation.  The bounds on
the left and right are independent of $t$.  Thus we obtain the
conclusion of the theorem.
\end{proof}
