**Proposition (q-difference recurrence of the binding generating function; conditional on [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)).**

Let $G(x;q)=\sum_{n\geq 0} B_n(K)\,x^n$ be the generating function of the
body-order binding terms
([`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)).
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
confluent (differential) limit; they hold for *any* such $R$. What is
**open** is the existence and identity of the kernel $R$ for the binding
$G$. By the precision-floor obstruction — the $c_k$ information bound, which
makes term data unmeasurable beyond low order — $R$ **cannot** be fixed by
fitting the $B_n$; it must be derived from the fibre root-of-unity
singularity structure of the Seiberg--Witten differential
([`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum)). This is the
same $q$-difference machinery as the $\mathfrak{Q}_\beta$ precision ladder, applied to
the binding series.
