<!-- FILE_START: p-vs-np-conjecture.md -->
**Conjecture ($q$-complexity separation).** *Let $\varepsilon$ be the
Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and
$q = 1 + \varepsilon$ the associated substrate parameter.  Let
$\mathrm{BQP}_q$ denote the class of decision problems solvable in
polynomial time on a $q$-deformed computational substrate — i.e. on
a topological quantum computer whose anyonic model is the
$R$-matrix of $\mathbf{C}_q$.  Then*

$$
  \mathbf{P} \;\neq\; \mathbf{NP}
$$

*in classical complexity theory, recovered as the standard part
$\mathrm{st}_{\varepsilon \to 0}$ of the strict inclusion*

$$
  \mathbf{P} \;\subsetneq\; \mathrm{BQP}_q
  \qquad
  (\text{for every } \varepsilon > 0 \text{ in } \mathbb{R}(\varepsilon)).
$$

**Formulation.** The Reeb period
$\Omega_q \asymp \varepsilon^{-1}$
([surreal rate calculus](#prop:surreal-rate-calculus))
measures the natural time budget of a computation on the
$q$-substrate: a polynomial-time $q$-algorithm executes
$\mathrm{poly}(n) \cdot \Omega_q^{O(1)}$ elementary skein moves
in a Reeb period, which is a transfinite quantity in
$\mathbb{R}(\varepsilon) \subset \mathbf{No}$.  A polynomial-time
classical algorithm has at most $\mathrm{poly}(n)$ elementary
moves in the same period — a standard-real quantity.

The conjecture asserts that the **classical-limit functor**
($\varepsilon \to 0$, equivalently the standard-part map
applied to the $q$-substrate computation, see
[calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon))
collapses the transfinite Reeb budget to a bounded finite budget,
thereby losing the $q$-advantage: the standard part of
$\mathrm{BQP}_q$ is strictly larger than $\mathbf{P}$ only if there
exist NP-complete problems whose $q$-algorithms do not admit a
convergent $\varepsilon \to 0$ expansion.

**Heuristic argument (non-proof).** The mass-gap dissipation
$\Delta_q \asymp \varepsilon^3$ is the energy the substrate can
absorb per computational step.  An NP-complete search with $2^n$
witnesses requires, classically, $2^n$ elementary tests; on the
$q$-substrate the search is a single Reeb-flow holonomy, which
takes Reeb time $\asymp \Omega_q = \varepsilon^{-1}$.  For the
$q$-algorithm to classically accelerate to polynomial time as
$\varepsilon \to 0$, each elementary test would have to be absorbed
in mass-gap energy $\Delta_q$, with classical budget $2^n \cdot \Delta_q
\asymp 2^n \cdot \varepsilon^3$ per computation.  The available
$q$-algorithm cost is the per-step efficiency dressed by the Reeb
period: $2^n \cdot \delta_n^2 \cdot \Omega_q \asymp 2^n \cdot \varepsilon^{-1}$.
By [surreal squeeze](#lem:surreal-squeeze), the cost strictly
exceeds the budget — equivalently $\ordw(\text{cost}) = 1 > -3 =
\ordw(\text{budget})$ — so the $q$-algorithm **cannot** be classically
compressed: the $2^n$-fold speedup cannot fit inside the classical
mass-gap budget.

**Caveat.** This conjecture is speculative. It is stated in a form
compatible with the Reeb--surreal framework but does not yet
admit a Lean formalisation beyond the statement.  A formal
proof would reduce the $q$-to-classical compression obstruction
to the structural non-existence of a $\mathrm{BQP}_q \to \mathbf{P}$
functor, consistent with the Freedman--Kitaev--Larsen--Wang
topological model \cite{freedman2003} at $q$-generic.

**See also.**
[Surreal bound for P vs NP](#rem:p-vs-np-surreal-bound) for the
squeeze-inequality statement that this conjecture implies.
<!-- FILE_END: p-vs-np-conjecture.md -->

<!-- FILE_START: p-vs-np-surreal-bound.md -->
This remark expresses the Reeb-period complexity argument of
[P vs NP in the QOU](#conj:p-vs-np-qou) as a literal surreal
inequality.

**Setup.** Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb
infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)),
$q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)).
A $q$-substrate computation has access to the Reeb-period budget
$\Omega_q \asymp \varepsilon^{-1}$
([surreal rate calculus](#prop:surreal-rate-calculus));
a classical computation has access to the mass-gap budget
$\Delta_q \asymp \varepsilon^3$ per elementary step.

**The surreal bound.** For an NP-complete instance of size $n$,
let $\delta_n > 0$ denote the per-step standard-real efficiency of
the $q$-algorithm.  A classical simulation of the $q$-algorithm
requires $2^n \cdot \delta_n^2 \cdot \Omega_q$ elementary steps to
replicate a full Reeb holonomy, while the mass-gap budget available
over the same Reeb period is $2^n \cdot \Delta_q$.  By
[surreal squeeze](#lem:surreal-squeeze),

$$
  \delta_n^2 \cdot \Omega_q
   \;\asymp\; \delta_n^2 \cdot \varepsilon^{-1}
   \;>\; \varepsilon^3 \;\asymp\; \Delta_q
  \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Multiplying through by the standard-real factor $2^n$ preserves the
inequality.  In $\omega$-adic form
([Big-O via $\ordw$](#rem:conway-normal-form)),
$\ordw(2^n \cdot \delta_n^2 \cdot \Omega_q) = 1 > -3 = \ordw(2^n \cdot \Delta_q)$:
the classical simulation sits at strictly higher $\omega$-order
than the classical budget.

**Conclusion.** The classical simulation of any non-trivial
$q$-algorithm (standard-real efficiency $\delta_n > 0$) exceeds its
classical budget by a full $\omega$-order.  Taking the standard part
([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon))
collapses the transfinite advantage of the $q$-algorithm: under
$\mathrm{st}_{\varepsilon \to 0}$, the $2^n$-fold Reeb speed-up is
lost.  Therefore the classical complexity classes $\mathbf{P}$ and
$\mathbf{NP}$ cannot be identified via the standard-part functor,
which is the content of [P vs NP in the QOU](#conj:p-vs-np-qou).

**Interpretation.** The remark does not prove $\mathbf{P} \neq \mathbf{NP}$
classically; it shows that the QOU framework, assuming
$\mathbf{P} \subsetneq \mathrm{BQP}_q$ at positive $\varepsilon$
(a widely-believed non-classical separation under the topological
quantum computation model \cite{freedman2003}), propagates to the
classical separation under the standard-part functor.

**Relation to Cook--Levin.**  The classical
NP-completeness structure \cite{cook1971} is preserved by the standard part, so
any Cook--Levin reduction on the $q$-substrate descends to a
Cook--Levin reduction classically.  Combined with the surreal
squeeze above, the separation $\mathbf{P} \neq \mathbf{NP}$ follows
from the strict inclusion at positive $\varepsilon$ and the
non-compressibility witness of
[P vs NP in the QOU](#conj:p-vs-np-qou).

**Caveat.** Unlike the RH, NS, and Collatz bounds, the P-vs-NP
squeeze is conditional on an independent conjecture
(non-compressibility of $\mathrm{BQP}_q \to \mathbf{P}$ as $\varepsilon \to 0$).
This places P-vs-NP in the *conditional* millennium-problem column
rather than the *unconditional* one; see
[millennium unification](#rem:millennium-unification) for the
side-by-side table.
<!-- FILE_END: p-vs-np-surreal-bound.md -->

<!-- FILE_START: q-collatz-conjecture.md -->
**Conjecture ($q$-Collatz).**
Let $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ be a substrate parameter
([torsion avoidance](#rem:substrate-gm-torsion)) and let
$\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$ be the Skein module
of the Reeb bundle $\mathcal{R}_p = (S^3 \to S^2, \xi_q)$
([Reeb bundle](#def:reeb-bundle)).

**Convention.** This section uses the combinatorial $q$-integer
$[n]_q = (q^n - 1)/(q - 1)$, giving $[2]_q = q + 1$ and
$[3]_q = q^2 + q + 1$.  The paper's Iwahori--Hecke algebra convention
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$ (symmetric, giving
$[2]_q = q + q^{-1}$) differs by a factor of $q^{(n-1)/2}$.
The combinatorial convention is used here because the Skein
divisibility identity $[3]_q = q[2]_q + 1$ and the contraction
gap $[2]_q^2 - [3]_q = q$ require it.

### $q$-parity in the Skein module

An element $P \in \mathbb{Z}[q^{\pm 1}]$ is **$q$-even** if
$[2]_q \mid P$ and **$q$-odd** if $[2]_q \mid (P + 1)$.
At $q = 1$: $[2]_1 = 2$, and these recover integer parity.

### The Skein-Collatz map

Define $\mathcal{C}_q \colon \mathbb{Z}[q^{\pm 1}] \to
\mathbb{Z}[q^{\pm 1}]$ by:

$$
  \mathcal{C}_q(P)
  = 
  \begin{cases}
    P / [2]_q
      & P \text{ is } q\text{-even},\\[4pt]
    \bigl([3]_q P + 1\bigr) / [2]_q
      & P \text{ is } q\text{-odd}.
  \end{cases}
$$

The odd branch is well-defined by the **Skein divisibility
identity**:

$$
  [3]_q =  q[2]_q + 1,
$$

which gives $[3]_q P + 1 = q[2]_q P + (P + 1)$.
Since $P$ is $q$-odd ($[2]_q \mid P + 1$), the numerator
is divisible by $[2]_q$.  Writing $P + 1 = [2]_q Q$:

$$
  \mathcal{C}_q(P)
  =  qP + Q
  =  [3]_qQ - q.
$$

**Classical limit.**  At $q = 1$: $\mathcal{C}_1(n) = n/2$
(even) or $(3n+1)/2$ (odd) — the Syracuse map.

### Skein-theoretic interpretation

Each application of $\mathcal{C}_q$ corresponds to a
**crossing resolution** in the Skein module
([skein generation](#prop:skein-generation)):

- **Even branch** ($P/[2]_q$): Markov destabilization —
  remove one strand from the braid closure, dividing
  the Jones polynomial by the Markov parameter.
  This is the $q$-analog of "halving."

- **Odd branch** ($([3]_q P + 1)/[2]_q$): apply the
  Hecke relation $T^2 = (q - q^{-1})T + 1$ to reduce
  a quadratic crossing word to linear, then destabilize.
  The three generators in $T^3 = [3]_q \cdot T + \cdots$
  reduce to one via the Hecke relation, then the Markov
  move removes it.

The Skein relation
$qL_+ - q^{-1}L_- = (q - q^{-1})L_0$ ensures
each resolution step is a **convex combination**:

$$
  J(L_+) = q^{-2}J(L_-) + (1 - q^{-2})J(L_0).
$$

For $q > 1$ both coefficients are positive and sum to $1$.
The crossing resolution is **non-expansive** on the
Jones polynomial.

### The contraction estimate

The algebraic identity $[2]_q^2 - [3]_q = q$
gives the contraction.  Over one Collatz cycle
(one odd step followed by enough even steps to
exhaust $[2]_q$-divisibility):

- The odd step maps $P \mapsto [3]_qQ - q$, where
  $Q = (P+1)/[2]_q$.  The ratio $|P|/|Q| \approx [2]_q$.

- The subsequent even steps divide by $[2]_q$ as many
  times as $[2]_q$ divides the result.

If each tripling is followed by at least **two halvings**
on average, the orbit contracts.  Two halvings multiply
by $1/[2]_q^2$; one tripling multiplies by $[3]_q/[2]_q$.
The net factor per cycle is $[3]_q / [2]_q^3 < 1$, with
margin:

$$
  [2]_q^2 - [3]_q =  q.
$$

The margin is the substrate parameter itself.  Two
halvings beat one tripling by a factor
$[2]_q^2 / [3]_q = 1 + q/[3]_q \approx 4/3$.

### The conjecture

$$
  \boxed{
  \text{For all } q > 1 \text{ and all }
  P \in \mathbb{Z}[q^{\pm 1}]_{>0},
  \text{the orbit }
  \{\mathcal{C}_q^k(P)\}_{k \geq 0}
  \text{ reaches } 1.
  }
$$

### Connection to the obstruction framework

The Collatz obstruction
$\kappa_C := \mathrm{res}_{C_q}(\kappa_0) \in
H^2(\mathcal{S}_{C_q}, \mathbb{G}_m)$
([classical limit obstruction](#def:classical-limit-obstruction),
[QOU obstruction reduction](#thm:qou-obstruction-reduction))
measures the failure of Skein-Collatz orbits to converge.

The conjecture $\kappa_C = 0$ is equivalent to:
every element of the Skein module
$\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$ reduces
to the unknot polynomial $1$ under iterated crossing
resolution via $\mathcal{C}_q$.
<!-- FILE_END: q-collatz-conjecture.md -->

<!-- FILE_START: two-q-adic-valuation.md -->
For an element $P \in \mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$
of the Skein module, the **$[2]_q$-adic valuation** is

$$
  v_{[2]}(P)  :=  \max\bigl\{k \geq 0 :
  [2]_q^k \mid P \text{ in } \mathbb{Z}[q^{\pm 1}]\bigr\}.
$$

This counts how many times $[2]_q = q + 1$ divides $P$ in the
Laurent polynomial ring — the $q$-analog of the $2$-adic
valuation $v_2(n)$ that counts trailing zeros in the
binary expansion of an integer.

The **contact order** of $P$ with the $[2]_q$-divisor
$D_{[2]} = \{q : [2]_q = 0\} = \{-1\}$ is $v_{[2]}(P)$: the
order to which $P(q)$ vanishes at $q = -1$. High contact
order means the orbit "grazes" the divisor closely — it
is very divisible by $[2]_q$, meaning many halvings can be
extracted.

At $q = 1$: $[2]_1 = 2$, and $v_{[2]}(n) = v_2(n)$
recovers ordinary $2$-adic valuation. The number
$n = 24 = 2^3 \cdot 3$ has $v_2(24) = 3$: three halvings
before hitting an odd number.
<!-- FILE_END: two-q-adic-valuation.md -->

<!-- FILE_START: collatz-contact-boundary-defn.md -->
The **orbit contact average** of $P \in \mathcal{S}(q)$ measures,
over the first $N$ steps of the Skein-Collatz map
([conj:q-collatz](#conj:q-collatz)), the average
$[2]_q$-adic valuation ([$[2]_q$-adic valuation](#def:two-q-adic-valuation))
of the results of the odd steps. Restricting to the odd steps
(there are $N_{\mathrm{odd}}$ of them):

$$
  \langle v_{[2]} \rangle_N(P)
   := 
  \frac{1}{N_{\mathrm{odd}}}
  \sum_{\substack{0 \leq k < N \\
    \mathcal{C}_q^k(P) \text{ is } q\text{-odd}}}
  v_{[2]}\bigl(\mathcal{C}_q^{k+1}(P)\bigr),
$$

with $\langle v_{[2]} \rangle(P) := \lim_{N \to \infty}
\langle v_{[2]} \rangle_N(P)$ the **orbit contact average**.

The **Collatz contact boundary** is the codimension-$1$
locus where the orbit's contact with $D_{[2]}$ is exactly
critical:

$$
  \mathcal{H}_{Col}(q)
  = 
  \bigl\{P \in \mathcal{S}(q) :
  \langle v_{[2]} \rangle(P) = v^*(q)\bigr\},
$$

where $v^*(q) = \log [3]_q / \log [2]_q$ is the sharp contact
threshold. Elements **above** the boundary (high contact, many
halvings) converge; elements **below** (insufficient
contact, too few halvings) diverge.
<!-- FILE_END: collatz-contact-boundary-defn.md -->

<!-- FILE_START: collatz-parity-to-divisor.md -->
### From integer parity to the $[2]_q$-divisor

Classical Collatz hinges on parity: is $n$ even or odd? Parity is residue modulo $2$. The number $2$ is the smallest prime, the only even prime, and the denominator of the halving step $n/2$.

In the QOU, the integer $2$ lifts to the quantum integer $[2]_q = q + 1$ (see [q-Collatz conjecture](#conj:q-collatz)). The $[2]_q$-divisor is the locus where $[2]_q = 0$:

$$
  D_{[2]}  :=  \{q : [2]_q = 0\}
  =  \{-1\}.
$$

This locus degenerates the $q$-analog of "dividing by $2$". The halving step ceases to exist.

**Kummer obstruction at the divisor.** The point $q = -1$ belongs to $\mu_2$. The Kummer obstruction ([root-of-unity truncation](#prop:root-of-unity-truncation)) at level $n = 2$ asks whether $2$ divides $\chi(A) = -6$. It does. The obstruction vanishes. The QOU axioms resolve the singularity. At $q = -1$, the residue ring is $\mathbb{Z}[q^{\pm 1}]/(q+1) \cong \mathbb{Z}$, and the $[2]_q$-adic valuation ([$[2]_q$-adic valuation](#def:two-q-adic-valuation)) specializes to the ordinary $2$-adic valuation.

### Necessity of orbit–divisor contact

The Skein-Collatz map ([conj:q-collatz](#conj:q-collatz)) has two branches:

- **Even branch** ($P/[2]_q$): Each application decreases $\log|P|$ by $\log [2]_q$. The orbit moves toward $1$.
- **Odd branch** ($([3]_q P + 1)/[2]_q$): Multiplication by $[3]_q$ increases $\log|P|$ by $\log([3]_q/[2]_q)$, despite the single built-in division by $[2]_q$.

Tripling inflates the orbit. Halving deflates it. Convergence requires the halvings to dominate on average.

After each odd step, the result $\mathcal{C}_q(P)$ is $q$-even, guaranteed by the Skein divisibility identity $[3]_q = q[2]_q + 1$. The integer $v_{[2]}(\mathcal{C}_q(P))$ measures contact order with $D_{[2]}$. It dictates how many consecutive halvings follow before the next odd step.

### The margin

| Quantity | Formula | At $q = 1$ | At $q_0$ |
|----------|---------|-----------|----------|
| Two halvings beat one tripling? | $[2]_q^2 > [3]_q$ | $4 > 3$ | $4.45 > 3.34$ |
| Margin | $[2]_q^2 - [3]_q = q$ | $1$ | $1.110$ |
| Relative margin | $q / [3]_q$ | $1/3$ | $0.332$ |
| Empirical $\langle v \rangle$ at $q=1$ | — | $2$ (exact) | — |

Two halvings overpower one tripling by a factor $[2]_q^2 / [3]_q = 1 + q/[3]_q \approx 4/3$. The margin $q/[3]_q \approx 1/3$ isolates the substrate parameter.
<!-- FILE_END: collatz-parity-to-divisor.md -->

<!-- FILE_START: collatz-contact-boundary.md -->
**Proposition (conditional on
[`conj:q-collatz`](#conj:q-collatz);
"$[2]_q$-contact boundary").**
Let $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2, \xi_q)$
be the Reeb bundle
([Reeb bundle](#def:reeb-bundle)) with $U(1)$ fiber
parametrized by $q = e^{i\varTheta}$, $\varTheta \in [0, 2\pi)$.
The $q$-Collatz orbit of $P \in \mathcal{S}(q)_{>0}$ converges if and
only if its orbit contact average
([Collatz contact boundary](#def:collatz-contact-boundary))
attains the threshold $\langle v_{[2]} \rangle(P) \geq 2$;
equivalently, the $q$-Collatz conjecture
([conj:q-collatz](#conj:q-collatz)) is the contact condition

$$
  \boxed{
  \bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle
   \geq  2
  \quad\text{for all } P \in \mathcal{S}(q)_{>0}.
  }
$$

### Proof

The condition is simplest without logarithms.  Since
$1 < v^*(q) < 2$ (proved: $[2]_q < [3]_q < [2]_q^2$),
the orbit converges whenever each tripling is followed
by **at least two halvings on average**, i.e.
$\langle v_{[2]} \rangle(P) \geq 2$.

Two halvings multiply by $[2]_q^{-2}$; one tripling
multiplies by $[3]_q / [2]_q$.  The net factor per cycle
(one tripling + two halvings) is

$$
  \frac{[3]_q}{[2]_q} \cdot \frac{1}{[2]_q^2}
  = 
  \frac{[3]_q}{[2]_q^3}.
$$

This is contractive because $[3]_q < [2]_q^2 < [2]_q^3$.
The contraction ratio is

$$
  \frac{[3]_q}{[2]_q^3}
  = 
  \frac{[2]_q^2 - q}{[2]_q^3}
  = 
  \frac{1}{[2]_q} - \frac{q}{[2]_q^3},
$$

so the orbit shrinks by slightly more than $1/[2]_q$
per cycle.  The **margin** — the gap between two halvings
and the minimum needed — is

$$
  [2]_q^2 - [3]_q =  q,
$$

the substrate parameter itself, which is positive; hence the
per-cycle factor is strictly contractive and the threshold
$\langle v_{[2]} \rangle \geq 2$ is sufficient for convergence.

The sharp threshold is $v^* = \log [3]_q / \log [2]_q$, but
since $v^* < 2$ is proved algebraically, the integer condition
$\langle v_{[2]} \rangle \geq 2$ is sufficient and avoids
transcendental quantities.

At $q = 1$ the average $2$-adic valuation of $3n+1$ for odd $n$ is
**exactly $2$** (the probability $\Pr(v_2(3n+1) = k) = 2^{-k}$ gives
$\mathbb{E}[v_2] = 2$): two halvings per tripling, exactly at the
integer threshold. $\qquad\blacksquare$
<!-- FILE_END: collatz-contact-boundary.md -->

<!-- FILE_START: collatz-no-cycles.md -->
**Proposition (conditional on
[`conj:q-collatz`](#conj:q-collatz);
"no periodic Collatz cycles").**
The Skein-Collatz map $\mathcal{C}_q$ on
$\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$
has no periodic orbits other than the fixed point $P = 1$.
<!-- FILE_END: collatz-no-cycles.md -->

<!-- FILE_START: collatz-three-forms.md -->
The contact boundary
([prop:collatz-contact-boundary](#prop:collatz-contact-boundary))
establishes that the $q$-Collatz orbit contracts if and only
if each tripling is followed by at least two halvings on
average.  This condition has three equivalent faces — one
categorical, one arithmetic, one number-theoretic — and the
equivalence reveals why the classical Collatz conjecture
sits at a critical threshold.

### (a) The categorical face: Markov trace convergence

In the Iwahori--Hecke algebra $H_n(q)$, the Collatz step composes
two operations: Hecke reduction ($T^2 = (q-q^{-1})T + 1$,
which simplifies crossing words) and Markov destabilization
($\mathrm{tr}_M(xT_n) = z \cdot \mathrm{tr}_M(x)$, which
removes a strand).  The Markov trace
$\mathrm{tr}_M \colon H_n(q) \to \mathbb{Z}[q^{\pm 1}]$
sends braid words to Jones polynomials.

The conjecture in this language: for every $h \in H_n(q)$,
the iterated Markov trace converges to the unknot:

$$
  \mathrm{tr}_M\bigl(\mathcal{C}_q^k(h)\bigr)
  \xrightarrow{k \to \infty} 1.
$$

The identity braid is the unique attractor of the
Hecke--Collatz dynamics.  Every braid, no matter how
tangled, untangles to the unknot under iterated crossing
resolution and destabilization.  The Jones polynomial
$J_L(q)$ of the link $L$ decays to $J_{\bigcirc}(q) = 1$
step by step.

This is the most intrinsic formulation: it lives
entirely inside the Iwahori--Hecke algebra and the Markov trace,
with no reference to integers, parity, or divisibility.
The "convergence to $1$" is convergence to the unknot
polynomial — the categorical unit.

### (b) The arithmetic face: two halvings per tripling

The contact boundary translates (a) into a divisibility
condition on the Skein module
$\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$.

Each odd step produces $[3]_q P + 1$.  The Skein
divisibility identity $[3]_q = q[2]_q + 1$ guarantees
this is divisible by $[2]_q$ — one halving is built in.
The question is whether a **second** halving follows:
is the result divisible by $[2]_q^2$?

The accounting per cycle:
- One tripling: multiply by $[3]_q$ (expansion)
- The built-in halving: divide by $[2]_q$ once
  (part of the accelerated map)
- Additional halvings: divide by $[2]_q$ as many
  more times as $[2]_q$ divides the result

The net contraction per cycle with $v$ total halvings:

$$
  \text{factor} = \frac{[3]_q}{[2]_q^v}.
$$

This is contractive iff $[2]_q^v > [3]_q$.  Since
$[2]_q^1 < [3]_q$ (one halving is not enough) and
$[2]_q^2 > [3]_q$ (two halvings suffice, gap $= q$),
the integer threshold is exactly $v = 2$:

$$
  \bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle
   \geq  2.
$$

Two halvings per tripling.  Not one, not three — two.
The margin between "one is not enough" and "two is
enough" is $[2]_q^2 - [3]_q = q$, the substrate
parameter.

### (c) The residue face ($q = -1$)

The $[2]_q$-divisor is $q = -1$ (where $[2]_q = q + 1 = 0$).
Evaluating the Collatz output at this divisor: since
$[3]_q|_{q=-1} = (-1)^2 + (-1) + 1 = 1$ and $[2]_q|_{q=-1} = 0$,
the condition $v_{[2]} \geq 2$ becomes $(q+1)^2$-divisibility
of $[3]_q P + 1$ at $q = -1$.

At $q = 1$ (classical limit): $[2]_1 = 2$, and the
$(q+1)$-adic valuation specializes to the $2$-adic
valuation $v_2$ on $\mathbb{Z}$.

### Equivalence and the saturation phenomenon

The three faces are equivalent because they measure the
same quantity from different vantage points:

| Face | What it measures | Where it lives |
|------|-----------------|---------------|
| (a) Categorical | Markov trace decay | $H_n(q)$ |
| (b) Arithmetic | $[2]_q$-adic valuation | $\mathbb{Z}[q^{\pm 1}]$ |
| (c) Residue | $(q+1)$-adic valuation | $\mathbb{Z}$ (at $q=-1$) |

The passage (a) $\to$ (b) is the Markov trace: it sends
Iwahori--Hecke algebra elements to Laurent polynomials, converting
braid untangling to divisibility.  The passage (b) $\to$
(c) is evaluation at the $[2]_q$-divisor ($q = -1$): it
specializes the Laurent polynomial to an integer, converting
$[2]_q$-adic valuation to the ordinary $2$-adic valuation.

**The saturation.**  At $q = 1$ (the classical limit), the
expected $2$-adic valuation of $3n+1$ for uniformly
distributed odd $n$ is:

$$
  \mathbb{E}[v_2(3n+1)]
  =  \sum_{k=1}^{\infty} k \cdot 2^{-k}
  =  2.
$$

Exactly $2$ — the threshold itself.  The classical Collatz
conjecture lives at the knife-edge where the average number
of halvings per tripling exactly equals the minimum needed.
There is no margin.

For $q > 1$: the algebraic gap $[2]_q^2 - [3]_q = q > 1$
provides positive margin.  But $q = 1$ is a torsion point
($\mu_1$), and the QOU axioms fail there.  The classical
hardness of Collatz is the shadow of this torsion
degeneration: the gap collapses to $q = 1$, the margin
vanishes, and the question becomes whether every
**specific** orbit (not the ensemble average) achieves
the threshold.

This is the $q$-deformed diagnosis of why the Collatz
conjecture resists proof: the contraction mechanism works
on average ($\mathbb{E}[v_2] = 2 \geq 2$) but the margin
is zero, so individual orbits might fail.  The conjecture
asserts they never do.
<!-- FILE_END: collatz-three-forms.md -->

<!-- FILE_START: q-collatz-interpretation.md -->
The $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz))
lives in the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$,
where parity is $[2]_q$-divisibility and crossing resolution
replaces arithmetic.  Three algebraic identities control
the dynamics, and the $(p_1^{k_1}, p_2^{k_2})$ family reveals
why the classical Collatz map $(2, 3)$ is arithmetically special.

### Three identities

| Identity | Formula | Role |
|----------|---------|------|
| Skein divisibility | $[3]_q = q[2]_q + 1$ | "$3n+1$ is even for odd $n$" |
| Contraction gap | $[2]_q^2 - [3]_q = q$ | Two halvings beat one tripling |
| Hecke reduction | $T^2 = (q-q^{-1})T + 1$ | Crossing words reduce |

The first ensures the odd branch is well-defined in
$\mathbb{Z}[q^{\pm 1}]$.  The second says two halvings
overpower one tripling, with margin $q$ — the substrate
parameter itself.  The third reduces quadratic crossing
words to linear, the algebraic engine of the Skein relation.

### Skein convexity

The Skein relation rewrites as:

$$
  J(L_+) = q^{-2}J(L_-) + (1-q^{-2})J(L_0).
$$

For $q > 1$ both coefficients are positive and sum to $1$:
a convex combination.  Crossing resolution is
non-expansive on Jones polynomial values.

### The $(p_1^{k_1}, p_2^{k_2})$ family

The Collatz map $(2, 3)$ — divide by $2$, multiply by $3$
— belongs to a family of generalized maps $(p_1, p_2)$:
divide by $p_1$ when divisible, apply $p_2 n + 1$ otherwise.
The $q$-deformed contraction condition requires $k_1$
halvings to overpower $k_2$ triplings:

$$
  [p_1]_q^{k_1}  >  [p_2]_q^{k_2}.
$$

The **contraction gap** $[p_1]_q^{k_1} - [p_2]_q^{k_2}$
is a polynomial in $\mathbb{Z}[q^{\pm 1}]$.  Its
coefficient structure determines the contraction regime.

**Trivial cases.** When $p_1^{k_1} \gg p_2^{k_2}$
classically, the gap polynomial has all positive
coefficients and contraction holds for all $q > 0$.
The $(a, a+1)$ family with $k_1 = 2$, $k_2 = 1$ is
always contractive: $[a]_q^2 - [a+1]_q$ has all
non-negative coefficients for every $a \geq 2$.

**Critical cases.** At the boundary
$p_1^{k_1} = p_2^{k_2} + 1$ (classical margin of $1$),
the $q$-gap polynomial may develop **negative
high-degree coefficients**, breaking contraction for
large $q$:

| $(p_1^{k_1}, p_2^{k_2})$ | Classical gap | $q$-gap | All $q > 0$? |
|--------------------------|--------------|---------|-------------|
| $(2^2, 3^1)$ — **Collatz** | $4 - 3 = 1$ | $q$ | **Yes** (monomial) |
| $(3^2, 8^1)$ | $9 - 8 = 1$ | $q + 2q^2 + q^3 - q^5 - q^6 - q^7$ | No |
| $(4^2, 15^1)$ | $16 - 15 = 1$ | negative high-degree terms | No |

### Uniqueness of $(2, 3)$

Collatz $(2^2, 3^1)$ is the **unique** critical case
where the $q$-gap is a monomial.  The identity
$[2]_q^2 - [3]_q = q$ produces a gap with a single term
— the substrate parameter $q$ — which is positive for
all $q > 0$.  Every other critical case has a gap
polynomial with both positive and negative coefficients,
and the negative terms dominate for sufficiently large $q$.

This is not a coincidence.  The identity $[3]_q = q[2]_q + 1$
(Skein divisibility) forces $[2]_q^2 - [3]_q = [2]_q^2 - q[2]_q - 1
= [2]_q([2]_q - q) - 1 = [2]_q \cdot 1 - 1 = q$.  The
monomial form arises because $[3]_q$ is the **next**
$q$-integer after $[2]_q$, and the quadratic-minus-linear
structure of $[2]_q^2 - [3]_q$ cancels all but the
linear term.  For $[a]_q^2 - [a^2-1]_q$ with $a \geq 3$,
the gap polynomial has degree $2(a-1)$ vs $a^2 - 2$, and
the high-degree terms of $[a^2-1]_q$ overwhelm $[a]_q^2$.

### Proved results and remaining conjectures

**Proved (in Lean):**
- $[3]_q = q[2]_q + 1$ — Skein divisibility (`skein_divisibility`)
- $[2]_q^2 - [3]_q = q$ — contraction gap (`qInt_gap`)
- $[3]_q < [2]_q^2$ for $q > 0$ — contraction (`qInt3_lt_qInt2_sq`)
- $\sqrt{[3]_q/[2]_q^2} < 1$ — geometric mean (`geometric_mean_contraction`)
- $(3, 4)$ gap positive for $q > 0$ — trivial case (`qInt_gap_3_4`)
- $(3, 8)$ gap fails for $q > 2$ — critical failure (`qInt_gap_3_8_fails`)

**Remaining conjectures:**
the orbit structure provides the two halvings.
The $[2]_q$-adic valuation of $\mathcal{C}_q(P)$ — how
deeply the result of each odd step is divisible by $[2]_q$
— must average to at least $2$
([contact boundary](#prop:collatz-contact-boundary)).
At $q = 1$ this average is exactly $2$ (a theorem).
The conjecture is that this holds for all $q > 1$.
<!-- FILE_END: q-collatz-interpretation.md -->

<!-- FILE_START: collatz-surreal-bound.md -->
This translates the contact-boundary argument of the $q$-Collatz conjecture ([$q$-Collatz](#conj:q-collatz), [Collatz no cycles](#prop:collatz-no-cycles)) into a literal surreal inequality in $\mathbb{R}(\varepsilon)$.

**Setup.** Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). The $q$-Collatz conjecture translates the integer orbit $n \mapsto n/2$ (even) / $n \mapsto 3n + 1$ (odd) into a skein-module resolution on the Reeb contact boundary. A **rogue orbit** is a non-trivial cycle (other than $1 \to 4 \to 2 \to 1$) or an unbounded hailstone. The "rogue drift" $\delta$ measures the excess contact volume produced per step.

**The surreal bound.** The Reeb period of the contact boundary is $\Omega_q \asymp \varepsilon^{-1}$ ([surreal rate calculus](#prop:surreal-rate-calculus)). A standard-real drift $\delta > 0$ per step produces an accumulated contact-volume deviation over one Reeb period:

$$
  V(\delta) \;\asymp\; \delta^2 \cdot \Omega_q \;\asymp\; \delta^2 \cdot \varepsilon^{-1}
$$

The mass-gap dissipation available to re-absorb the deviation is $\Delta_q \asymp \varepsilon^3$. By [surreal squeeze](#lem:surreal-squeeze), $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ strictly in $\mathbb{R}(\varepsilon)$. Hence:

$$
  V(\delta) \;>\; \Delta_q
  \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Equivalently, $\ordw(V(\delta)) = 1 > -3 = \ordw(\Delta_q)$ in the $\omega$-adic order of [Big-O via $\ordw$](#rem:conway-normal-form).

**Conclusion.** No rogue orbit with standard-real drift $\delta > 0$ can persist. The Reeb period sweeps a contact-volume transfinite larger than the mass-gap infinitesimal. No budget exists to dissipate the accumulated excess. This is the surreal-arithmetic form of the [$q$-Collatz](#conj:q-collatz) conjecture, consistent with the contact-geometric argument of [Collatz no cycles](#prop:collatz-no-cycles).

**Relation to the standard-part map.** The classical Collatz orbit on $\mathbb{N}$ is the standard part $\mathrm{st}\bigl(\cdot \,|_{q = 1 + \varepsilon}\bigr)$ of the $q$-deformed skein resolution ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)). Every infinitesimal drift vanishes under $\mathrm{st}$. Every standard-real drift is prohibited by the squeeze above. Therefore $\mathrm{st}(\delta) = 0$ for every admissible surreal drift. All orbits terminate at $1$.

**Non-trivialisation of Collatz.** This argument shows that the $q$-Collatz statement upgrades to a surreal inequality that rules out all standard-real drifts. We recover the classical conjecture only by assuming the $q$-Collatz skein-module resolution admits a well-defined standard part. This acts as the Collatz analogue of the Hasse--Weil alignment hypothesis.
<!-- FILE_END: collatz-surreal-bound.md -->

