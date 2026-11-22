---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-009-31-strong-forces
section_title: "Strong forces"
section_number: 3.1
pages: 7-8
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
\label{sect:strong-forces}

But how about \alert{Strong forces}?

We know the group we want here is $SU(3)$, but the mathematics of $SU(3)$ we were discussing just now, in either the approach given in the previous section, or Martin Roelf's version, is set in a 6d Euclidean space, in which we employ the `Lie groups as spin groups' approach in order to represent the action of unitary groups of order $N$ in a space of order $2N$. There are now two developments relative to this, which I want to talk about.

The first is earlier work (discussed in the talk at GAME2020) on how we can incorporate the strong force $SU(3)$ directly into the STA. Secondly, and linked, how it has become clear to me that \alert{Octonions} may have a very important role. Using what we show below, it is now possible to represent them just using the STA, and to show that their key feature, of preserving the norms of elements under multiplication, fits in with what both the electroweak and strong force STA approaches tell us so far.

So, to begin with this, how would we like to represent the strong force in STA? A model initially due Robert Lasenby, extends the Dirac spinor $\psi$ to be both a function of position $x$, and a linear function of a bivector argument $B$, so $\psi= \psi(B)$. The separate colour fields then arise as $\psi_i=\psi(\sigma_i)$, where $\sigma_i=\gamma_i\go$, $i=1,2,3$, are the unit norm spatial bivectors of the STA in the usual way. This means that $\psi=\psi(B,x)$, where $x$ is position, is intriguingly like a spinor version of the {\em Riemann tensor}!

Recently, I have made a definite proposal for the form of these transformations of $B$, which gives a nice picture, within the STA, of the particle physics version of the $SU(3)$ group. This is that we ask for transformations of {\em bivectors} $F$ in the STA that keep the Hermitian inner product of $F$ with itself invariant:

\be
\langle \go F \go F \rangle
\ee

(Remember the Hermitian adjoint is reversion followed by `reflection in time axis' and reversion for a bivector is just $F\mapsto -F$.)

How does this work? We do this by considering {\em double-sided} operation on $F$.
(Note a double-sided action to understand $SU(3)$ was first proposed by David Hestenes, in {\em Space-time structure of weak and electromagnetic interactions}\cite{1982FoPh...12..153H}.) 

We will not go through all the details here, but we form these from composing the single-sided actions
(for $i=1,2,3$)

\be
\begin{aligned}
\hat{e}_i &= \; \text{multiplication on the left by $\sigma_i$, so} \; \hat{e}_i(F) = \sigma_i F\\
\hat{f}_i &= \; \text{multiplication on the right by $I\sigma_i$, so} \ \hat{f}_i(F) = F I\sigma_i
\end{aligned}
\ee

and we claim the appropriate $U(n)$ generators are as follows.

\be
\begin{gathered}
\Ehat_{ij}= \ehat_i \ehat_j - \fhat_i \fhat_j,\quad i<j\\
\Fhat_{ij}= \ehat_i \fhat_j + \ehat_j \fhat_i,\quad i<j\\
\Jhat_i=\ehat_i\fhat_i, \quad i=1,2,3
\end{gathered}
\label{eqn:hats-def}
\ee

where there is no sum implied in the last line, i.e.\ each line contains three quantities, making up the expected 9 generators overall.

We restrict to $\sut$ in the same way as above. Let us look at the sum of the $\Jhat_i$,

\be
\Jhat = \Jhat_1+\Jhat_2+\Jhat_3
\ee

Since $\sigma_i F \sigma_i = -F$ (with a sum over the $i$), we have

\be
\Jhat(F)=-IF
\ee

for any bivector $F$. Thus $\Jhat$ acts like the generator of a global `phase rotation', but where the imaginary is the pseudoscalar. It is this part that is removed in making the transition to $\sut$ from $U(3)$

So as before we have to take linear combinations of the $\Jhat_i$ in which the overall sum is removed, i.e.\ the only combinations allowed are of the form

\be
\alpha_1 \Jhat_1 + \alpha_2 \Jhat_2 + \alpha_3 \Jhat_3, \quad \text{with} \quad \alpha_1+\alpha_2 +\alpha_3=0
\label{eqn:alpha-restriction}
\ee

This limits the number of independent generators to 8 instead of 9, giving the right number for $\sut$.

A really nice feature of the approach is the ease with which we can derive finite forms of the transformations. Looking at the two individual parts of the $\Ehat_{ij}$ generators, i.e.\ $\ehat_i\ehat_j$, and $\fhat_i\fhat_j$, where $i<j$, it is clear that they mutually commute, and each squares to $-1$.

Thus when we exponentiate $\Ehat_{ij}$ to obtain a finite transformation, we can immediately write (with $\alpha$ a scalar)

\be
\begin{aligned}
\exp\left(\frac{\alpha}{2} \Ehat_{ij}\right)(F)&=\exp\left(\frac{\alpha}{2}\ehat_i\ehat_j\right)\left(\exp\left(\frac{-\alpha}{2}\fhat_i\fhat_j\right)(F)\right)\\
&=\exp\left(\frac{\alpha}{2}\sigma_i\sigma_j\right) F \exp\left(\frac{\alpha}{2}\sigma_j\sigma_i\right)\\
&=R_{ij} F \Rrev_{ij}
\end{aligned}
\ee

where $R_{ij}$ is the spatial rotor $\exp\left(\frac{\alpha}{2}\sigma_i\sigma_j\right)$, which gives rotations through angle $\alpha$ about the $\epsilon_{ijk} \sigma_k$ axis.

Thus if $R$ is a general spatial rotor (and so has three d.o.f.), we can see that the $\Ehat$ sector amounts to the set of spatial rotations $RF\Rrev$. For the $\Fhat_{ij}$ generators, we again have that the two parts commute, and obtain

\be
\begin{aligned}
\exp\left(\frac{\alpha}{2} \Fhat_{ij}\right)(F)&=\exp\left(\frac{\alpha}{2}\ehat_i\fhat_j\right)\left(\exp\left(\frac{\alpha}{2}\ehat_j\fhat_i\right)(F)\right)\\
&=\cos^2 \frac{\alpha}{2} F + \half I \sin\frac{\alpha}{2}\cos\frac{\alpha}{2}\left(\sigma_i F \sigma_j + \sigma_j F \sigma_i\right)\\
&+\sin^2 \frac{\alpha}{2} \sigma_i \sigma_j F \sigma_j \sigma_i
\end{aligned}
\label{eqn:Fij-action}
\ee


To complete the set, the finite form for the $\Jhat_i$ is

\be
\exp\left(\alpha\Jhat_i\right)(F)=\cos\alpha \, F + \sin\alpha \,I\,\sigma_i F \sigma_i
\ee

with of course no sum on the r.h.s. For $\Jhat$ we have

\be
\exp\left(\alpha\Jhat\right)(F)=e^{-\alpha I}F
\ee

i.e.\ a global duality transformation. Further details will be given in Lasenby (2022, in preparation).
