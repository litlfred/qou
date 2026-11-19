**Conjecture (cyclotomic boundary at the quintic order).**

The binding $q$-deformation of the na-Stokes period
$S(n) = \sum_{\lambda \vdash n} \dim_q(\lambda)$ satisfies the recurrence

$$
S(n) \;=\; S(n-1) \;+\; [n-1]_q\,S(n-2) \;+\; D(n),
$$

whose deviation term $D(n)$ — the **Habiro tail** — carries a universal
$(q-1)^2$ double root at $q=1$ and is bar-even ($D(1/q)=D(q)$). The
conjecture asserts that $D(n)$ is **cyclotomic** — a product of cyclotomic
polynomials (times the $(q-1)^2$ factor and a $q$-monomial) — **if and
only if $n \leq 5$**, where $5$ is the quintic order $S_5 \supset A_5$.

**The alignment.** The cyclotomic-pure regime $n \leq 5$ coincides exactly
with the framework's calibration orders and the quintic order:

$$
\{\,n \leq 5 : D(n)\text{ cyclotomic}\,\}
\;=\;
\underbrace{\{n=2,3,4\}}_{\text{calibration orders } c=1,2,3}
\;\cup\;
\underbrace{\{n=5\}}_{S_5\text{ quintic order}}.
$$

The first non-cyclotomic (non-$q$-holonomic) content appears at the first
body order $n=6$ that is *neither* a calibration *nor* the quintic order.

**The arithmetic mechanism.** At $q=1$ one has $S(n)|_{q=1} = \sum_{\lambda
\vdash n} f^\lambda = I(n)$, the involution / telephone numbers (OEIS
A000085; the Frobenius–Schur identity, proved for all $n$ by RSK:
involutions $\leftrightarrow$ SYT). So $S(n)$ is the $q$-deformed involution
number — a Rogers–Szegő / $q$-Hermite moment — and the recurrence above is
the $q$-lift of $I(n)=I(n-1)+(n-1)I(n-2)$, with $D(n)$ its deviation. Prior
analysis of this $q$-involution kernel establishes the tail's structure: a
$(q-1)^2$ double root times a bar-even cofactor that is cyclotomic through
$n=5$ and acquires a genuine non-cyclotomic, **non-$q$-holonomic** factor
from $n=6$ — the same non-holonomicity that obstructs any fixed-order closed
form for $S(n)$. This is the mechanism that governs $D(n)$: it is a property
of *cancellation in the alternating sum*, not of any individual quantum
dimension.

**Why the individual quantum dimensions do not locate the boundary.** Every
$\dim_q(\lambda) = [n]_q!/\prod_c [h(c)]_q$ is a **product of cyclotomic
polynomials for every $n$** (a ratio of cyclotomic products that is a
polynomial). So cyclotomic-purity of the individual dimensions does not
distinguish $n=5$ from $n=6$: at both orders all $\dim_q(\lambda)$ are
cyclotomic. In particular the McKay observation below — that at $n=5$ the
four classes carry *single* quantum integers while at $n=6$ most are
*compound* products of several $[m]_q$ — is a single-$[m]_q$-vs-product
distinction, **not** a cyclotomic-vs-non-cyclotomic one (a product of
several cyclotomics is still cyclotomic). It does not, by itself, supply the
arithmetic mechanism above.

**The McKay coincidence (rep-theory, link unproven).** At the quintic order $n=5$
the four conjugation classes $\{\lambda,\lambda'\}$ of $S_5$ carry quantum
dimensions equal to the **$E_8$ Coxeter marks** $[\mathrm{mark}]_q$:

$$
\dim_q(5)=[1]_q,\quad
\dim_q(4,1)=[4]_q,\quad
\dim_q(3,2)=[5]_q,\quad
\dim_q(3,1,1)=[5]_q+1,
$$

because $A_5 \cong 2I/\{\pm 1\}$ is the **icosahedral** group and $2I
\leftrightarrow \widehat{E}_8$ (McKay). The McKay–ADE ladder of alternating
groups is finite: $A_4 \cong$ tetrahedral ($2T \leftrightarrow
\widehat{E}_6$), $A_5 \cong$ icosahedral ($2I \leftrightarrow
\widehat{E}_8$), and $A_6 \cong \mathrm{PSL}(2,9)$ is **not** a binary
polyhedral group. Thus $A_5$ is the last alternating group that is the
rotation group of a Platonic solid, and $A_6$ ($n=6$) is the first
non-McKay. That the McKay-mark structure exits at the same order the tail
leaves the cyclotomic ring is a **coincidence of orders**; by the caveat
above it does not act *through* cyclotomic-purity of the dimensions, and its
bearing on the arithmetic mechanism is unproven.

**Status — three tiers of correlation, not to be conflated.**

1. *Arithmetic* (the substance): $D(n)$ is non-cyclotomic from $n=6$. This is
   **verified through $n=11$** but **not proved for all $n \geq 6$**; the
   cofactor's non-$q$-holonomic degree growth is the structural reason, not
   yet a proof. Generic high-degree bar-even integer polynomials are
   non-cyclotomic, so non-cyclotomicity is the *expected* outcome — the
   content is entirely that $n \leq 5$ *are* cyclotomic, and that "for all
   $n \geq 6$, with no exceptions" is what a proof must supply.
2. *Alignment*: that boundary coincides with {calibration $\cup$ quintic}
   orders $\{2,3,4\}\cup\{5\}$.
3. *Rep-theory*: the McKay-mark / $S_6$-outer-automorphism coincidence at
   $n=6$.

The **causation** — whether the $A_5 \to A_6$ McKay exit or the $S_6$ outer
automorphism *forces* the boundary — is unproved, and the route through the
single-vs-compound quantum dimensions does **not** establish it. What can be
said is the dovetail with $S(n)=\sum_{\lambda\vdash n}\dim_q(\lambda)=
\sum_\lambda W_\lambda$: the same $S_5$ whose quantum dimensions are the
$E_8$ marks carries the Verlinde measure $W_\lambda$. Specific root
magnitudes are not interpreted.

**Algebraic scope at $n = 6$.** The Tier-1 base-case
factorizations $D(4)=\Phi_1^2\Phi_3$ and $D(5)=2\,\Phi_1^2\Phi_2^2\Phi_3\Phi_6$,
the palindrome identity $C_6(z)=z^4\,\tilde C(z+z^{-1})$, and the $n = 6$
non-cyclotomicity of the degree-$8$ core $C_6$ — that $C_6$ is *not* a product of
cyclotomic polynomials — follow from the elementary direction of
Kronecker's dichotomy (roots of cyclotomics are roots of unity, hence of
modulus $1$), *not* the hard converse. The entire $n = 6$ chain rests on a
**single** classical input: that $\tilde C(y)=y^4+4y^3+2y^2-10y-8$ has a
non-real root (immediate from $\mathrm{disc}(\tilde C)=-44208<0$). The full Tier-2 claim (non-cyclotomic
for *all* $n\geq 6$) is verified computationally through $n=11$.
