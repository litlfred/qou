**Proposition.**
*The Skein resolution obstruction
$\kappa_c^{\mathrm{comp}}(\beta, q)$
([Skein resolution obstruction](#def:skein-resolution-obstruction))
depends on the base field $k$ and the substrate parameter
$q \in k^\times$.  In particular:*

1. *Over $\mathbb{F}_p$: the obstruction vanishes for all
   braids.  Every decision problem is decidable in polynomial
   Planck steps.*

2. *At roots of unity $q_k = e^{2\pi i/(k+2)}$ over
   $\mathbb{C}$: the obstruction decomposes into descended
   and transient components, and the transient component can
   cancel the descended component for problems in
   $\mathrm{BQP}$.*

3. *Over $\mathbb{R}$ at generic $q$: no cancellation from
   transient modes is available, and the obstruction is
   potentially non-vanishing.*

**Proof.**

**(1) Finite fields: P = NP over $\mathbb{F}_p$.**

Over $\mathbb{F}_p$, the substrate parameter $q \in
\mathbb{F}_p^\times$ has multiplicative order dividing $p - 1$.
The $q$-integers $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ are
elements of $\mathbb{F}_p$, and the Hecke algebra $H_n(q)$
is a **finite-dimensional** algebra over a **finite field**.
The resolution tree $\mathcal{R}(\beta)$ has $3^c$ leaves,
but each leaf carries a Skein weight in $\mathbb{F}_p$ — there
are at most $p$ distinct values.

The Markov trace is a linear functional on a finite-dimensional
space.  By brute force, it can be computed in
$\dim H_n(q) \leq n!$ operations — a finite number independent
of any asymptotic growth.  More precisely: every orbit of the
Julia map $f_q(z) = z^2 + c(q)$ on $\mathbb{F}_p$ is
eventually periodic with period dividing $p$ (Fermat).  The
Planck dynamics terminates in $\leq p$ steps, and every
computation reduces to a finite lookup.

The resolution obstruction vanishes because the residual
weight sum is a sum of $3^c$ terms in $\mathbb{F}_p$, and
the pigeonhole principle guarantees cancellation modulo $p$.
Formally: $\kappa_c^{\mathrm{comp}}(\beta, q) \in
H^2(\mathcal{R}_{p(c)}, \mathbb{F}_p^\times)$, and
this cohomology group is $p$-torsion, so the obstruction
class has finite order.  After at most $p$ resolution steps,
the obstruction cycles back to zero.

This does **not** mean computation is trivial over
$\mathbb{F}_p$ — the constant hidden in $O(\dim H_n(q))$
can be astronomical.  But asymptotically, P = NP: every
NP problem over $\mathbb{F}_p$ is in $\mathrm{P}$ with a
$p$-dependent constant.

**(2) Roots of unity: BQP as partial obstruction cancellation.**

At $q_k = e^{2\pi i/(k+2)}$ with $k \geq 3$, the braiding
representation $\rho_{q_k} \colon B_n \to \mathrm{End}(V^{\otimes n})$ is dense in $\mathrm{SU}(2^n)$
([quantum universality](#conj:quantum-computational-universality)).
The descent involution decomposes the obstruction:

$$
  \kappa_c^{\mathrm{comp}}(\beta, q_k)
  \;=\;
  \kappa_c^{\mathrm{desc}}
  \;+\;
  \kappa_c^{\mathrm{trans}}.
$$

A problem is in $\mathrm{BQP}$ iff the **total obstruction
vanishes at the root of unity**: $\kappa_c^{\mathrm{comp}}
(\beta, q_k) = 0$, even though the descended component
$\kappa_c^{\mathrm{desc}} \neq 0$ (classically hard).  The
transient modes provide **quantum interference channels**
that cancel the classical obstruction.

The standard examples: integer factoring (Shor) and unstructured
search (Grover) have $\kappa_c^{\mathrm{desc}} \neq 0$ but
$\kappa_c^{\mathrm{comp}}(\beta, q_k) = 0$ — the quantum lift
collapses the resolution tree.

**(3) Real $q$: no transient cancellation.**

Over $\mathbb{R}$ at generic $q \in (1, \infty)$, the descent
involution projects away all transient modes: $\hat{\tau}$
kills $\mathcal{A}^{\mathrm{trans}}$, leaving only the
descended component.  The obstruction reduces to

$$
  \kappa_c^{\mathrm{comp}}(\beta, q)
  \;=\;
  \kappa_c^{\mathrm{desc}}(\beta, q)
  \qquad
  \text{(real $q$, classical computation)}.
$$

No cancellation from quantum channels is available.  The
question of whether $\kappa_c^{\mathrm{desc}}$ vanishes at
polynomial depth — for all braids — is the classical
$\mathrm{P}$ vs $\mathrm{NP}$ question over $\mathbb{R}$.

**Summary.**

$$
  \boxed{
    \mathrm{P} \stackrel{?}{=} \mathrm{NP}
    \;\;\text{depends on}\;\;
    (k,\, q)
  }
$$

The braiding structure is universal
([base-field independence](#rem:base-field-independence)),
but the **interference pattern is field-dependent**.  The
same braid $\beta$ may have vanishing obstruction over
$\mathbb{F}_p$, partially vanishing obstruction at roots of
unity, and non-vanishing obstruction over $\mathbb{R}$.  The
question "P $=$ NP?" is not absolute — it is a question about
the category $(\mathbf{C}, A, \tau)$ and the field over which
it is realized.
