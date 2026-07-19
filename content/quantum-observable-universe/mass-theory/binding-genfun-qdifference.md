**Proposition (q-difference recurrence of the binding generating function).**

Let $G(x;q)=\sum_{n\geq 0} B_n(K)\,x^n$ be the generating function of the
body-order binding terms
([`thm:binding-manybody-eq-jet-filtration`](#thm:binding-manybody-eq-jet-filtration)).
Suppose $G$ satisfies a fibre-level $q$-difference equation

$$
G(qx;q) \;=\; R(q,x)\,G(x;q),
\qquad R(q,x)\in\mathbb{Q}(q)[x,x^{-1}]\ \text{of bounded depth }d .
$$

Then:

1. **Linear recurrence.** The body terms satisfy a depth-$d$ linear
   recurrence $B_{n+d} = \sum_{j=0}^{d-1} a_j(q)\,B_{n+j}$, with kernel
   $\{a_j\}$ read off from $R$. In particular the empirical "$\rho\cdot A$"
   scale rule governing the growth of the terms is the **solution of the
   recurrence — an output of $R$, not a fitted constant**.
2. **Archimedean image.** Under the realisation functor $\tau$ at $q=q_0$,
   the $q$-difference equation passes to a linear (Dirac-type) differential
   equation on the realised generating function: the fibre $q$-shift becomes
   a derivation in the archimedean limit.

The implications (1)--(2) are the standard passage from a $q$-holonomic
generating function to a $P$-recursive coefficient sequence and its
confluent (differential) limit; they hold for *any* such $R$. 

The existence and identity of the kernel $R$ for the binding $G$ was previously **open** due to the precision-floor obstruction. Because the $c_k$ information bound makes empirical term data unmeasurable beyond low order, $R$ **cannot** be fixed by fitting the $B_n$. Instead, it has now been **derived exactly** from the fibre root-of-unity singularity structure of the Seiberg--Witten differential via the Reeb-twisted jet filtration ([`thm:qdifference-kernel-prolongation-symbol`](#thm:qdifference-kernel-prolongation-symbol)). This successfully sidesteps the precision limit, completely determining the binding scale rules. This is the same $q$-difference machinery as the $\mathfrak{Q}_\beta$ precision ladder, applied to the binding series.
