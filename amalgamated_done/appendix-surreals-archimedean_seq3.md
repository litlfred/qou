<!-- FILE_START: wenzl-positivity-implies-substrate-positivity.md -->
The companion conjecture [`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb) reduces the Wightman-axiom portion of the Yang–Mills millennium statement to a single substrate axiom: $C^*$-Frobenius positivity of the QOU Frobenius–Hopf substrate at $q = q_0$. This conjecture takes the natural next step. The axiom should be **derivable** from Wenzl's positivity criterion for $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ at $q_0 \in \mathbb{R}_{>1}$. It is not an independent posit, but a consequence of existing unitarity.

**Conjecture (Wenzl positivity at $q_0$ implies substrate
$C^*$-Frobenius positivity).** *Wenzl's positivity criterion for the
representation category $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ at
$q = q_0 \in \mathbb{R}_{>1}$ — the criterion that picks out unitary
fusion categories among the q-deformed semisimple ones — implies the
substrate $C^*$-Frobenius positivity axiom of*
[`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb).
*Equivalently, the Müger $C^*$-norm on the
[Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)
$A$ at $q_0$, induced by the categorical trace of $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$,
makes the antipode-twisted Frobenius pairing $\langle\theta(\cdot),
\cdot\rangle_F$ positive-definite on the positive-time Reeb half.*

Here $\theta$ is the Reeb reflection (the antipodal
$\mathbb{Z}_2 \subset U(1)$ of
[`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb))
and $\langle\cdot,\cdot\rangle_F$ the Frobenius form of $A$.

## The natural follow-up

The OS-reflection-positivity conjecture [`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb) leaves the substrate $C^*$-Frobenius positivity axiom as the sole genuinely new input. That axiom has three free parameters:

1. **Choice of $C^*$-norm** on $A$ at $q_0$. The substrate algebra
   $A$ at $q_0 \in \mathbb{R}_{>1}$ admits several candidate
   $C^*$-completions:
   - the universal $C^*$-norm of $A$ as a $*$-algebra;
   - the GNS norm with respect to the Frobenius pairing;
   - the Müger norm built from the categorical trace of the ambient
     tensor category.
2. **Positivity of the antipode-twisted pairing** in the chosen norm.
3. **Compatibility with the antipode $S$.**

The Müger norm has properties (2) and (3) *by construction* for
*any* unitary $C^*$-tensor category $\mathbf{C}$ in the BKLR sense
(Müger 2003, Bischoff–Kawahigashi–Longo–Rehren). The only open
question is therefore whether $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$
at $q_0 \in \mathbb{R}_{>1}$ is unitary as a $C^*$-tensor category.
And that is exactly the content of Wenzl's positivity criterion.

## Wenzl's criterion (recall)

Wenzl proved (\cite{wenzl1988}, \cite{wenzl1990}, with the
$\mathrm{SU}(N)$ generalisation by Wenzl and the
$\mathfrak{sl}_n$-equivariant version by Kazhdan–Wenzl
\cite{kazhdanwenzl1993}): the representation category
$\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ admits a unitary structure
(positive $C^*$-trace + positive inner product on each Hom space)
iff $q$ lies in either:

- $\{q = e^{i\pi / N} : N \geq 3\}$ (the roots-of-unity range
  yielding the modular tensor categories at level $N - 2$); or
- $\{q \in \mathbb{R}_{>0}\}$ (the real positive range, in
  particular $q_0 \approx 1.10998$).

The criterion is sharp: outside these two regions, the categorical
trace fails to be positive, and no $C^*$-completion of the underlying
algebra makes $\mathrm{Rep}$ a $C^*$-tensor category.

The QOU substrate parameter $q_0 \approx 1.10998$ lies in the second
region (real positive). Wenzl's criterion therefore applies, and
$\mathrm{Rep}(U_{q_0}(\mathfrak{sl}_2))$ is unitary. By the standard
Müger / BKLR theory, *every* Frobenius algebra in a unitary
$C^*$-tensor category is automatically a positive Frobenius algebra
(in the sense of the substrate axiom of
[`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb)).

## The conjecture's actual claim

The conjecture is therefore the **identification step** between two
positivity notions:

(a) Wenzl-positivity of $\mathrm{Rep}(U_{q_0}(\mathfrak{sl}_2))$ as
    a $C^*$-tensor category — established.
(b) Substrate $C^*$-Frobenius positivity of $(A, \mu, \eta, \Delta,
    \varepsilon)$ as a Frobenius algebra in
    $\mathrm{Rep}(U_{q_0}(\mathfrak{sl}_2))$ — needed by
    [`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb).

(a) is a theorem; (b) is the substrate axiom, so the conjecture is
exactly the claim that (a) implies (b) via the categorical
Frobenius–algebra theory of Müger / BKLR.
## Strategic significance

If this conjecture is proved, the entire Yang–Mills millennium
statement reduces in the QOU framework to:

- [`thm:quantum-gap-collapse`](#thm:quantum-gap-collapse) — surreal
  mass gap (established);
- [`prop:reeb-u1-chart-swap`](#prop:reeb-u1-chart-swap) — chart-swap
  $U(1)$ is the Reeb $U(1)$ (proved);
- Wenzl positivity at $q_0 \in \mathbb{R}_{>1}$ (theorem
  \cite{wenzl1988});
- Müger / BKLR positive-Frobenius theory (theorem, off-the-shelf);
- This conjecture: the bridge.

The bridge is the *only* genuinely conjectural input. Closing it
discharges the OS-reflection-positivity-as-axiom assumption and
upgrades the QOU framework to a complete derivation of Yang–Mills
mass gap + Wightman compliance from the categorical substrate +
Bring's surface constraint.

This is the natural endgame programme. It also explains why the
QOU substrate has $q = q_0 \in \mathbb{R}_{>1}$ specifically: the
real positive range is precisely Wenzl's unitarity range. The
choice of $q_0$ is not free — it's locked by the unitarity
requirement that makes the Wightman QFT reconstruction possible.
<!-- FILE_END: wenzl-positivity-implies-substrate-positivity.md -->

<!-- FILE_START: collatz-hausdorff-comparison.md -->
The Hausdorff dimension recurrence ([Hausdorff recurrence](#rem:hausdorff-dimension-recurrence)) provides the only universal convergence proof in this paper. The map $q_{n+1} = (q_n^2 - q_n + 1)/q_n$ contracts for all $q > 3/4$, with $q = 1$ as a superattracting fixed point ($F'(1) = 0$). The $q$-Collatz conjecture shares a parallel structure, but with one critical difference.

### The Lyapunov function $\Phi = \log_q |P|$

The natural Lyapunov function for the Skein-Collatz uses
$q$ as the logarithm base:

$$
  \Phi(P)  :=  \log_q |P|.
$$

Why $q$?  Because the contraction gap is $q$ itself:
$[2]_q^2 - [3]_q = q$.  The base-$q$ logarithm converts
this gap into unit decrease: when a cycle has $v = 2$
halvings, $\Phi$ decreases by

$$
  |\Delta\Phi|
  = 
  \log_q \frac{[2]_q^2}{[3]_q}
  = 
  \log_q\!\left(1 + \frac{q}{[3]_q}\right).
$$

At $q_0 = 1.109978595554181\ldots$ (50 dps): $|\Delta\Phi| \approx 2.76$ per
cycle.  An orbit starting at $P$ with $\Phi_0 = \log_q |P|$
reaches the fixed point $\Phi = 0$ (i.e., $P = 1$) after
$\Phi_0 / |\Delta\Phi|$ cycles.

### Entropy cost of convergence

Each Collatz cycle with $v = 2$ halvings consists of $3$
Reeb steps ($1$ odd $+ 2$ even), each consuming
$\eta_q = (2q-1)/q^3$ $q$-bits of operational entropy
([operational entropy](#def:operational-entropy)).  The
total entropy budget to convergence is:

$$
  I_{\mathrm{total}}
  = 
  \frac{\Phi_0}{|\Delta\Phi|} \cdot 3\eta_q
   \approx 
  \Phi_0 \cdot \eta_q
  \quad q\text{-bits}.
$$

At $q_0$, converging from $|P| = 1000$ costs about $65$
$q$-bits — roughly $24$ Collatz cycles, each consuming
$\sim 2.7$ $q$-bits.  The orbit is an information-bounded
computation: it processes a finite, predictable amount
of entropy before terminating.

### The Hausdorff--Collatz comparison

See [Table](#tbl:collatz-hausdorff-comparison-table-data).

### The discrete phase transition at $v = 2$

The Hausdorff recurrence is smooth: the derivative
$F'(q) = 1 - 1/q^2$ varies continuously, reaching $0$
at the fixed point (superattraction).  The orbit
decelerates as it approaches $q = 1$ — each step costs
more entropy but covers less distance.

The Collatz contraction is **discrete**: the valuation
$v \in \{1, 2, 3, \ldots\}$ is an integer, and the
threshold $v^* \in (1, 2)$ falls between two integers.
There is no gradual approach.  The contraction ratio
jumps:

$$
  R(v) = \frac{[3]_q}{[2]_q^v}:
  \qquad
  R(1) \approx \tfrac{3}{2} > 1,
  \qquad
  R(2) \approx \tfrac{3}{4} < 1,
  \qquad
  R(3) \approx \tfrac{3}{8} < 1.
$$

This is a **discrete phase transition**: below $v = 2$
the orbit expands, at $v = 2$ it contracts by $3/4$,
and at $v \geq 3$ it contracts even faster.  There is
no critical slowing-down and no superattraction.

### Implications for the conjecture

The Hausdorff recurrence converges **unconditionally**
because $F'(q) < 1$ for all $q > 3/4$ — the derivative
is negative everywhere in the physical range, so every
orbit enters the basin of the superattracting fixed point.

The Collatz dynamics converge **conditionally**: the
contraction $R(2) < 1$ fires only when $v \geq 2$.  The
conjecture asks whether every orbit produces $v \geq 2$
often enough.  The algebra guarantees that $v = 2$
**suffices** ($[2]^2 > [3]$, gap $= q$); the
no-periodic-cycles theorem
([no cycles](#prop:collatz-no-cycles)) eliminates the
main alternative to convergence; and the classical
average $\mathbb{E}[v_2] = 2$ saturates the threshold.

### Connection via Planck steps

Both the Hausdorff recurrence and the Collatz cycle
advance by Planck-scale steps.  The Hausdorff map uses
$\delta q = \hbar_q$ as the step size (one Reeb phase
advance in $q$-space).  The Collatz cycle consumes
$n_R(q) = q/(q-1)$ Reeb iterations
([operations per Planck](#prop:reeb-operations-per-planck)).

The Hausdorff step and the Collatz Lyapunov step are
commensurate:

$$
  \frac{|\Delta\Phi|}{\hbar_q}
  = 
  \frac{\log_q([2]^2/[3])}{(q-1)/q}
   \approx  2.9
  \quad\text{at } q_0.
$$

Each Collatz cycle (at $v = 2$) covers about $3$ Planck
steps worth of Lyapunov decrease.  The Collatz orbit is
a discrete walk on the same parameter space that the
Hausdorff recurrence traverses smoothly, both using the
substrate parameter as their natural scale.
<!-- FILE_END: collatz-hausdorff-comparison.md -->

