---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-015-51-gauge-transformations
section_title: "Gauge Transformations"
section_number: 5.1
pages: 44-46
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.876
latex_coverage_ratio: 0.975
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{gauge}

First consider ordinary gauge theory.  Suppose that $M$ is a manifold
and $G$ is a Lie group.  Then a \define{gauge transformation} on the
trivial principal $G$-bundle over $M$ simply amounts to a smooth
function
\[              g \maps M \to G , \]
while a connection on this bundle can be seen as a $\g$-valued 1-form.  
A gauge transformation $g$ acts on a connection $A$ to give a new connection
$A'$ as follows:
\[            A' = g A g^{-1} + g\, dg^{-1}   .\]
This formula makes literal sense if $G$ is a group of matrices: then
$\g$ also consists of matrices, so we can freely multiply
elements of $G$ with elements of $\g$.  If $G$ is an arbitrary 
Lie group the formula requires a bit more careful interpretation, but
it still makes sense.   A well-known calculation says the curvature
$F' = dA' + A' \wedge A'$ of the gauge-transformed connection is
just the curvature of the original connection conjugated by $g$:
\[          F' = g F g^{-1}  .\]

In higher gauge theory the formulas are similar, but a bit more
complicated.  Suppose $M$ is a manifold and $\G$ is a Lie 2-group with
crossed module $(G,H,t,\alpha)$.  It will be helpful to take
everything in this crossed module and differentiate it.  Doing this,
we get:
\begin{itemize}
\item
the Lie algebra $\g$ of $G$,
\item
the Lie algebra $\h$ of $H$,
\item 
the Lie algebra homomorphism $\dt \maps \h \to \g$ obtained by
differentiating $t \maps H \to G$, and
\item 
the Lie algebra homomorphism $\dalpha \maps \g \to \aut(H)$ obtained
by differentiating $\alpha \maps G \to \Aut(H)$.
\end{itemize}
Here $\aut(H)$ is the Lie algebra of $\Aut(H)$.  It is best to think 
of this as the Lie algebra of \define{derivations} of $\h$: that is, linear
maps $D \maps \h \to \h$ such that
\[          D[x,y] = [Dx,y] + [x,Dy] . \]
If we differentiate the two equations in the definition of a
crossed module, we obtain the \define{\boldmath $\g$-equivariance 
of $\dt$}:
\[      \dt(\dalpha(x)(y)) = [x,\dt(y)]  \]
and the \define{infinitesimal Peiffer identity}:
\[      \dalpha(\dt(y))(y') = [y,y']  \]
where $x \in \g$ and $y,y' \in \h$.  In case the reader is curious: we
write $\dt$ and $\dalpha$ instead of $dt$ and $d\alpha$ because later
we will do computations involving these maps and also differential
forms, where $d$ stands for the exterior derivatve.

A quadruple $(\g, \h, \dt, \dalpha)$ of Lie algebras and homomorphisms
obeying these two equations is called an \define{infinitesimal crossed
module}.  Just as crossed modules are a way of working with 2-groups,
infinitesimal crossed modules are a way of working with Lie 2-algebras
\cite{BaezCrans}.  Any infinitesimal crossed module comes from a Lie
2-group, and this Lie 2-group is unique if we demand that $G$ and $H$
be connected and simply connected.

But we digress!  We have introduced infinitesimal crossed modules in order
to say how gauge transformations act on 2-connections.  A {\bf gauge
transformation} of the trivial $\G$-2-bundle over $M$ consists of two
pieces of data:
\begin{itemize}
\item
a smooth function $g \maps M \to G$, 
\item
an $\h$-valued 1-form $a$ on $M$.
\end{itemize}
Why \emph{two} pieces of data?  Perhaps this should not be so
surprising.  Remember, a 2-connection also consists of two pieces of
data:
\begin{itemize}
\item
a $\g$-valued 1-form $A$ on $M$, 
\item
an $\h$-valued 2-form $B$ on $M$ satisfying $\dt(B) = F$.
\end{itemize}

Breen and Messing \cite{BreenMessing} worked out how gauge
transformations act on connections on nonabelian gerbes, and their
work was later generalized to 2-connections on arbitrary principal
2-bundles \cite{BaezSchreiber, SchreiberWaldorf:gerbes}.  Here we
merely present the formulas.  A gauge transformation $(g,a)$ acts on a
2-connection $(A,B)$ to give a new 2-connection $(A',B')$ as follows:
\[       
\begin{array}{ccl}
A' &=& g A g^{-1} \; + \; g\, dg^{-1} \; + \; \dt(a)  \\  \\
B' &=& \alpha(g)(B) \; + \; \dalpha(A') \wedge a \; + \; da \; - \; 
a \wedge a
\end{array}
\]
The second formula requires a bit of explanation.  In the first term
we compose $\alpha \maps G \to \Aut(H)$ with $g \maps M \to
G$ and obtain an $\Aut(H)$-valued function $\alpha(g)$, which then
acts on the $\h$-valued 2-form $B$ to give a new $\h$-valued 2-form
$\alpha(g)(B)$.  In the second term we start by composing $A'$ with
$\dalpha$ to obtain an $\aut(H)$-valued 1-form $\dalpha(A')$.  Then
we wedge this with $a$, letting $\aut(H)$ act on $\h$ as part of this 
process, and obtain an $\h$-valued 2-form.

As a kind of consistency check and test of our understanding, let us
see why the gauge-transformed 2-connection $(A',B')$ satisfies the
equation $\dt(B') = F'$.  First let us compute the curvature 2-form
$F'$ of the gauge-transformed 2-connection:
\[
\begin{array}{ccl}
F' &=& dA' + A' \wedge A'  \\
   &=& d(g A g^{-1} + g\, dg^{-1} + \dt(a)) \; + \\
   &&    (g A g^{-1} + g\, dg^{-1} + \dt(a)) \wedge
       (g A g^{-1} + g\, dg^{-1} + \dt(a)) 
\end{array}
\]
This looks like a mess---but except for the terms containing $\dt(a)$,
this is just the usual mess we get in ordinary gauge theory when
we compute the curvature of a gauge transformed connection.  So, we
have:
\[
\begin{array}{ccl}
F'    &=& gFg^{-1}\; + \; d(\dt(a)) \; + \; \dt(a) \wedge A' 
\; + \; A' \wedge \dt(a) - \dt(a) \wedge \dt(a)  \\
&=& gFg^{-1}\; + \; \dt(da) \; + \; [\dt(a), A'] - \dt(a) \wedge \dt(a)      
\end{array}
\]
where we use the fact that $d(\dt(a)) = \dt(da)$ and rewrite
$A' \wedge \dt(a) + \dt(a) \wedge A'$ as a graded commutator.

On the other hand, we have
\[
\begin{array}{ccl}
\dt(B') &=& \dt(\alpha(g)(B)) \; + \; \dt(\dalpha(A') \wedge a) \; + \;
\dt(da - a \wedge a) \qquad \qquad
\end{array}
\]
The $G$-equivariance of $t$ implies that
$\dt(\alpha(g)(B)) = g\dt(B)g^{-1}$, and
the $\g$-equivariance of $\dt$ implies that 
$\dt(\dalpha(A') \wedge a) = [A', \, \dt(a)]$.  So, we see that
\[
\begin{array}{ccl}
\dt(B') &=& g\dt(B)g^{-1} \; + \; [A',\, \dt(a)] \; + \;
\dt(da - a \wedge a) \qquad \qquad
\end{array}
\]
and thus $\dt(B') = F'$, as desired.
