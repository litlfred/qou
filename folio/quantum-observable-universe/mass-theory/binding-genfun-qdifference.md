**Proposition (q-difference recurrence of the binding generating function; conditional on [binding manybody equals jet filtration conjecture](#conj:binding-manybody-eq-jet-filtration)).**

Let $G(x;q)=\sum_{n\geq 0} B_n(K)\,x^n$ be the generating function of the
body-order binding terms
([binding manybody equals jet filtration conjecture](#conj:binding-manybody-eq-jet-filtration)).
Suppose $G$ satisfies a fibre-level $q$-difference equation

$$
G(qx;q) \;=\; R(q,x)\,G(x;q),
\qquad R(q,x)\in\mathbb{Q}(q)[x,x^{-1}]\ \text{of bounded depth }d .
$$

Then:

1. **Linear $q$-recurrence.** Writing $R = \sum_j r_j(q)\,x^j$, the body terms
   satisfy an order-$d$ linear recurrence whose coefficients depend on the
   position through $q^n$; for polynomial $R$,
   $(q^n - r_0)\,B_n = \sum_{j=1}^{d} r_j\,B_{n-j}$. Every term is fixed by
   $R$ and the first $d$ terms, so whatever growth the $B_n$ show is an
   output of $R$, not a fitted constant. The coefficients are **not**
   constant in $n$: for $R = 1 - x$ the solution $B_n = 1/(q;q)_n$ gives
   $1, -1, 1/3, -1/21, 1/315$ at $q = 2$, which satisfies no constant-coefficient
   recurrence of depth $1$ or $2$.
2. **Archimedean image.** Under the realisation functor $\tau$ at $q=q_0$,
   the $q$-difference equation passes to a linear (Dirac-type) differential
   equation on the realised generating function: the fibre $q$-shift becomes
   a derivation in the archimedean limit.

The implications (1)--(2) are the standard passage from a $q$-holonomic
generating function to a $q$-recursive coefficient sequence (coefficients
polynomial in $q^n$) and its
confluent (differential) limit; they hold for *any* such $R$. What is
**open** is the existence and identity of the kernel $R$ for the binding
$G$. By the precision-floor obstruction — the $c_k$ information bound, which
makes term data unmeasurable beyond low order — $R$ **cannot** be fixed by
fitting the $B_n$; it must be derived from the fibre root-of-unity
singularity structure of the Seiberg--Witten differential
([Seiberg–Witten period residue sum proposition](#prop:sw-period-residue-sum)). This is the
same $q$-difference machinery as the $\mathfrak{Q}_\beta$ precision ladder, applied to
the binding series.

> **Scope of the rank-1 hypothesis — unsatisfiable on both
> proposed carriers; the proposition survives only in rank $2$.** The
> supposition above is a *first-order* (rank-1) $q$-difference relation. Two
> carriers have been proposed for $G$, and neither admits one.
>
> The **raw** carrier — the ordinary generating function of the raw body terms
> $B_n = I(n)/n$ — was excluded by the confluent/Gevrey growth argument
> (no bounded-depth first-order kernel can match the Gevrey growth).
> That exclusion explicitly re-targeted the conjecture at the
> **$q$-Borel / Gevrey-normalized** carrier $b_n = f_n/[n]_q!$, predicting depth
> $d = 2$. The normalized carrier provably satisfies
> $[m+2]_q\,b_{m+2} = b_{m+1} + b_m$, i.e. the operator
> $L_{\mathcal{K}} = (q^2x-1)\sigma^2 - (q-1)\sigma - (q-1)$ named by
> [$q$-difference kernel prolongation symbol conjecture](#conj:qdifference-kernel-prolongation-symbol).
>
> A scalar kernel is a first-order right factor $\sigma - a$ of
> $L_{\mathcal{K}}$, i.e. a solution $a\in K(x)$ of the $q$-Riccati equation
> $(q^2x-1)\,a(qx)\,a(x) - (q-1)\,a(x) - (q-1) = 0$. Writing $a = P/Q$ and
> clearing denominators, the three terms have degrees $1+2p$, $p+u$ and $2u$
> with $p = \deg P$, $u = \deg Q$. The first is odd-shaped and the third even,
> so $1+2p = 2u$ is impossible over $\mathbb{Z}$; a two-line case split then
> gives that the maximum is attained **exactly once** for every $(p,u)$, and a
> lone top-degree term cannot cancel. Hence no rational $a$ exists,
> $\mathcal{K}$ is irreducible of rank $2$, and **no nonzero solution of
> $L_{\mathcal{K}}$ obeys any scalar relation $G(qx) = R(q,x)G(x)$ with
> $R \in K(x)$** — a fortiori none with $R\in\mathbb{Q}(q)[x,x^{-1}]$ of any
> depth $d$; the depth never enters the argument, only the degrees do.
>
> **Scope (b), structural exclusion, invariant cited.** The parity is the
> Newton-slope invariant: $L_{\mathcal{K}}$ is pure isoclinic of slope
> $\tfrac12$ at infinity, every rank-1 $q$-difference module has *integer*
> slope, and Newton slopes are additive on sub- and quotient modules.
> Independently corroborated by the van der Put--Reversat classification of
> pure modules \cite{vanderput-reversat2007,vanderput2006}: a pure module of
> non-integral slope $d/r$, $\gcd(d,r)=1$, and rank $r$ is $E(r,d,b)$ in
> Bugeaud's notation \cite{bugeaud2011}, and it is irreducible.
>
> **What survives.** Implications (1)--(2) are unaffected and the depth-$2$
> prediction stands — but *depth $2$ means rank $2$*: the kernel is a $2\times2$
> matrix $A(q,x)$ acting on $(G, \sigma G)$, whose $\tau$-image is a first-order
> two-component system, which is what "Dirac-type" already asks for. Restated
> in rank $2$ the proposition is intact; restated in rank $1$ it is vacuous.
> The exclusion is over $K(x)$: after a degree-$2$ **ramified** base change
> (adjoining $q^{1/2}$, $x^{1/2}$) the slope becomes the integer $1$ and a
> scalar kernel does exist on the double cover, relating half-shifts — that is,
> even and odd body orders separately. That ramification is the missing
> structure, not a gap in the argument.
