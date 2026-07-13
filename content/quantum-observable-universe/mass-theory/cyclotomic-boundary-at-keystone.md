**Conjecture (cyclotomic boundary at the keystone order).**

The binding $q$-deformation of the na-Stokes period
$S(n) = \sum_{\lambda \vdash n} \dim_q(\lambda)$ satisfies the recurrence

$$
S(n) \;=\; S(n-1) \;+\; [n-1]_q\,S(n-2) \;+\; D(n),
$$

whose deviation term $D(n)$ — the **Habiro tail** — carries a universal
$(q-1)^2$ double root at $q=1$ and is bar-even ($D(1/q)=D(q)$). The
conjecture asserts that $D(n)$ is **cyclotomic** — a product of cyclotomic
polynomials (times the $(q-1)^2$ factor and a $q$-monomial) — **if and
only if $n \leq 5$**, where $5$ is the keystone order $S_5 \supset A_5$.

**The alignment.** The cyclotomic-pure regime $n \leq 5$ coincides exactly
with the framework's calibration and keystone data:

$$
\{\,n \leq 5 : D(n)\text{ cyclotomic}\,\}
\;=\;
\underbrace{\{n=2,3,4\}}_{\text{calibration orders } c=1,2,3}
\;\cup\;
\underbrace{\{n=5\}}_{S_5\text{ keystone}}.
$$

The first non-cyclotomic (non-$q$-holonomic) content appears at the first
body order $n=6$ that is *neither* a calibration *nor* the keystone.

**The mechanism.** Since $S(n)=\sum_{\lambda \vdash n}\dim_q(\lambda)$, the
arithmetic of $D(n)$ is governed by the quantum dimensions. At the keystone
$n=5$ the four conjugation classes $\{\lambda,\lambda'\}$ of $S_5$ carry
quantum dimensions equal to the **$E_8$ Coxeter marks** $[\mathrm{mark}]_q$:

$$
\dim_q(5)=[1]_q,\quad
\dim_q(4,1)=[4]_q,\quad
\dim_q(3,2)=[5]_q,\quad
\dim_q(3,1,1)=[5]_q+1,
$$

because $A_5 \cong 2I/\{± 1\}$ is the **icosahedral** group and the binary
icosahedral group satisfies the McKay correspondence $2I \leftrightarrow
\widehat{E}_8$. The McKay–ADE ladder of alternating groups is finite:
$A_4 \cong$ tetrahedral ($2T \leftrightarrow \widehat{E}_6$),
$A_5 \cong$ icosahedral ($2I \leftrightarrow \widehat{E}_8$), and
$A_6 \cong \mathrm{PSL}(2,9)$ is **not** a binary polyhedral group, so it
carries no McKay–ADE datum. Thus $A_5$ is the *last* alternating group that
is the rotation group of a Platonic solid. At $n=6$ the quantum dimensions
become genuine **compound** products of several cyclotomics — only four of
the eleven partitions of $6$ have $\dim_q$ a single quantum integer
$[m]_q$, against all seven at $n=5$ — the McKay-mark structure is gone, and
$D(6)$ leaves the cyclotomic (Habiro) ring.

**Two dovetailing candidate causes.** The keystone order is distinguished
as the last exceptional-Lie alternating group from two sides:

1. $A_5$ is the last McKay–ADE alternating group ($2I \leftrightarrow
   \widehat{E}_8$); its quantum dimensions are the $E_8$ marks, and $A_6$ is
   the first non-McKay alternating group — the McKay-mark structure exits
   exactly where $D(6)$ goes non-cyclotomic.
2. $S_6$ is the **unique** symmetric group with a nontrivial outer
   automorphism, and the non-cyclotomic core appears precisely at $n=6$.

This is an **open** conjecture and a **correlation**: the arithmetic
mechanism (the cyclotomic $\Phi_d$ first dividing $D(d+1)$) and the
rep-theory mechanism (the McKay-mark exit at $A_6$) are established, but the
**causation** — whether the $A_5 \to A_6$ McKay exit, equivalently the $S_6$
outer automorphism acting on the character sum $S(6)$, *forces* the boundary
— is not proved. If closed, it ties the binding $q$-deformation's arithmetic
directly to the keystone, dovetailing with the identity $S(n)=\sum_{\lambda
\vdash n}\dim_q(\lambda)=\sum_\lambda W_\lambda$ whose Verlinde measure
$W_\lambda$ lives at $S_5$: the *same* $S_5$ whose quantum dimensions are the
$E_8$ marks would control where the binding tail leaves the Habiro ring.
Specific root magnitudes are not interpreted.
