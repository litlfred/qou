By Pascal's rule $\binom{n+1}2 = n+\binom n2$, so by induction $2\binom A2 = A(A-1)$ in $\mathbb Z$. Hence
$$
2\tbinom A2-2(3A-6) = A^2-7A+12 = (A-3)(A-4).
$$
The right side is $0$ at $A=3,4$ and at least $2$ for $A\ge5$, so $\binom A2=3A-6$ for $A\in\{3,4\}$ and $\binom A2>3A-6$ for $A\ge5$. Also $\binom A3=0$ if and only if $A<3$. For $A\ge2$ the cases $A=2$, $A\in\{3,4\}$ and $A\ge5$ are exhaustive and disjoint, which gives the trichotomy. For $\kappa$: $\kappa(2)=1=\binom22$, $\kappa(3)=3=\binom32$, $\kappa(4)=6=\binom42$, and $\kappa(A)=3A-6<\binom A2$ for $A\ge5$.

$\blacksquare$
