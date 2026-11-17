*For $A\ge2$ let $K_A$ be the complete graph on $A$ vertices. Define the pair-graph regime of $A$ by*
$$
r(A)=\begin{cases}
\mathrm{I} & \binom A3 = 0,\\
\mathrm{II} & \binom A3>0 \text{ and } \binom A2\le 3A-6,\\
\mathrm{III} & \binom A2 > 3A-6.
\end{cases}
$$
*Here $\binom A3=0$ says that $K_A$ has no triangle, and $3A-6$ is the number of edges of a triangulated 2-sphere on $A$ vertices. Then, for every natural number $A$,*
$$
2\Bigl(\tbinom A2-(3A-6)\Bigr)=(A-3)(A-4),
$$
*and for $A\ge2$ exactly one of the following holds:*

1. *$A=2$, so $r(A)=\mathrm I$;*
2. *$A\in\{3,4\}$, with $\binom A2 = 3A-6$, so $r(A)=\mathrm{II}$;*
3. *$A\ge5$, with $\binom A2>3A-6$, so $r(A)=\mathrm{III}$.*

*In particular the deltahedral max-contact count $\kappa(A)$ ($\kappa(2)=1$, $\kappa(A)=3A-6$ for $A\ge3$) equals $\binom A2$ if and only if $A\le4$.*

The statement is integer arithmetic. It shows that the boundaries $2\mid3$ and $4\mid5$ used in [`conj:mass-formula-regime-switching`](#conj:mass-formula-regime-switching) are determined by $A$ alone. It does not say which evaluation belongs to which regime; that assignment remains a selection against the measured target. The criterion was identified after the selected cut-offs were known, and is recorded as such.

Geometrically (classical, not used above): for $A\ge3$, $\binom A2\le3A-6$ says $K_A$ is the 1-skeleton of a triangulated 2-sphere (the doubled triangle at $A=3$, the tetrahedron at $A=4$); for $A\ge5$, $K_A\supseteq K_5$ is not planar. Equivalently, $A$ equal spheres in $\mathbb{R}^3$ can be pairwise tangent if and only if $A\le4$.
