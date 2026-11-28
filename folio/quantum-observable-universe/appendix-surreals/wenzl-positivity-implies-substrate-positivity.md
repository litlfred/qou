**Archimedean specialisation.** The companion conjecture [Osterwalder--Schrader reflection positivity from the Reeb $\mathbb{Z}_2$](#conj:os-reflection-positivity-from-reeb) isolates a single aether hypothesis for Euclidean reflection positivity: $C^*$-Frobenius positivity of the QOU Frobenius--Hopf aether at $q = q_0$. This conjecture posits that this hypothesis is **derivable** from Wenzl's positivity criterion for $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ at $q_0 \in \mathbb{R}_{>1}$.

**Conjecture (Wenzl positivity at $q_0$ implies aether
$C^*$-Frobenius positivity).** *Wenzl's positivity criterion for the
representation category $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ at
$q = q_0 \in \mathbb{R}_{>1}$ — the criterion that picks out unitary
fusion categories among the q-deformed semisimple ones — implies the
aether $C^*$-Frobenius positivity axiom of*
[Osterwalder--Schrader reflection positivity from the Reeb $\mathbb{Z}_2$](#conj:os-reflection-positivity-from-reeb).
*Equivalently, the Müger $C^*$-norm on the
[Frobenius–Hopf aether](#def:frobenius-hopf-aether)
$A$ at $q_0$, induced by the categorical trace of $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$,
makes the antipode-twisted Frobenius pairing $\langle\theta(\cdot),
\cdot\rangle_F$ positive-definite on the positive-time Reeb half.*

Here $\theta$ is the Reeb reflection (the antipodal
$\mathbb{Z}_2 \subset U(1)$ of
[Osterwalder--Schrader reflection positivity from the Reeb $\mathbb{Z}_2$](#conj:os-reflection-positivity-from-reeb))
and $\langle\cdot,\cdot\rangle_F$ the Frobenius form of $A$.

## The natural follow-up

The OS-reflection-positivity conjecture [Osterwalder--Schrader reflection positivity from the Reeb $\mathbb{Z}_2$](#conj:os-reflection-positivity-from-reeb) leaves the aether $C^*$-Frobenius positivity axiom as the sole genuinely new input. That axiom has three free parameters:

1. **Choice of $C^*$-norm** on $A$ at $q_0$. The aether algebra
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
That is exactly the content of Wenzl's positivity criterion.

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

The QOU aether parameter $q_0 \approx 1.10998$ lies in the second
region (real positive). Wenzl's criterion therefore applies, and
$\mathrm{Rep}(U_{q_0}(\mathfrak{sl}_2))$ is unitary. By the standard
Müger / BKLR theory, *every* Frobenius algebra in a unitary
$C^*$-tensor category is automatically a positive Frobenius algebra
(in the sense of the aether axiom of
[Osterwalder--Schrader reflection positivity from the Reeb $\mathbb{Z}_2$](#conj:os-reflection-positivity-from-reeb)).

## The conjecture's actual claim

The conjecture is therefore the **identification step** between two
positivity notions:

(a) Wenzl-positivity of $\mathrm{Rep}(U_{q_0}(\mathfrak{sl}_2))$ as
    a $C^*$-tensor category — established.
(b) Aether $C^*$-Frobenius positivity of $(A, \mu, \eta, \Delta,
    \varepsilon)$ as a Frobenius algebra in
    $\mathrm{Rep}(U_{q_0}(\mathfrak{sl}_2))$ — needed by
    [Osterwalder--Schrader reflection positivity from the Reeb $\mathbb{Z}_2$](#conj:os-reflection-positivity-from-reeb).

(a) is a theorem; (b) is the aether axiom, so the conjecture is
exactly the claim that (a) implies (b) via the categorical
Frobenius–algebra theory of Müger / BKLR.
## Structural role

If this conjecture holds, Euclidean reflection positivity of the categorical Frobenius pairing at $q_0$ follows from:

- [Chart-swap $U(1)$ equals the Reeb $U(1)$ as subgroups of $\mathrm{Aut}(\mathbb{P}(V))$](#prop:reeb-u1-chart-swap) — chart-swap $U(1)$ is the Reeb $U(1)$;
- Wenzl positivity at $q_0 \in \mathbb{R}_{>1}$ \cite{wenzl1988};
- Müger / BKLR positive-Frobenius theory;
- This bridge conjecture identifying the induced $C^*$-Frobenius structure on $A$.

Unitarity is compatible with $q = q_0$, but it does not single
$q_0$ out. Wenzl's unitarity range is the whole real positive line,
so every $q \in \mathbb{R}_{>0}$ satisfies it equally. The value of
$q_0$ is fixed by the weak-modulus aether calibration, not by unitarity.

