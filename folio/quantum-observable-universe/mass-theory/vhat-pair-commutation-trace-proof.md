## Proof

The traced volume $\hat V_i(q) = z(q)\,a_i(q) + b_i(q)$ is, by
construction
([def:algebraic-quantum-volume §partial-product expansion](#def:algebraic-quantum-volume)),
an element of the **commutative** Laurent polynomial ring
$\mathbb{Z}[q^{\pm 1/2}, z]$ — the coefficients $a_i, b_i$ are
polynomials in $q^{\pm 1/2}$ and $z$ is a single transcendental
parameter (the Markov parameter, eliminated by
$z = q^{3}/(q^{2}+1)$ (**convention D**) at the end of every Markov peel,
[jones-markov-trace theorem](#thm:jones-markov-trace)).

Two elements of a commutative ring commute. Hence

$$
  \hat V_i \cdot \hat V_j \;=\; \hat V_j \cdot \hat V_i.
$$

Applying $\mathrm{tr}_M$ (which is $\mathbb{Z}[q^{\pm 1/2}, z]$-
linear) and invoking the pair Markov-trace identity
([prop:markov-pair-z2](#prop:markov-pair-z2)) gives the second
equality $\mathrm{tr}_M(\hat V_i \hat V_j) = z^2$ for **all**
$i, j$ — adjacent or not. $\square$

## Validity of the pentagon ascension

The pentagon identity
$\Phi_q(v)\,\Phi_q(u) = \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v)$
holds for operators $u, v$ satisfying $uv = q\,vu$ — for instance
the canonical pair on the **quantum plane**
$\mathbb{C}\langle u, v \rangle/(uv - q vu)$. For commuting
scalars, the pentagon identity collapses to
$\Phi_q(uv) = 1$, which is non-trivial only at very specific
$uv$ values and **does not hold generically**. So the pentagon
identity does *not* apply to scalar $\hat V$'s.

Hence the pentagon ascension argument as stated in
[mass-endomorphism-jet-tower remark](#rem:mass-endomorphism-jet-tower)
**describes the correct structure** (singletons + pairs at level $n$,
defects of order $\geq 3$ ascending to level $n+1$) but is **not
derived from the operator pentagon**. The actual derivation goes
through
Markov-trace factorization
([markov-trace-factorization theorem](#thm:markov-trace-factorization)):

1. The traced product $\mathrm{tr}_M(\prod_i \hat V_i)$ factors
   as a sum over subset structures on $\{i_1, \dots, i_n\}$, with
   subset weights determined by the Markov parameter $z$.
2. Singletons contribute $\sum_i \Phi_q(|\hat V_i|)$.
3. Pairs contribute $z^2 \sum_{i < j} \Phi_q(|\hat V_i \hat V_j|)$.
4. Order-$\geq 3$ subsets do **not** contribute as new level-$n$
   terms; instead, they reorganise into singleton/pair structures
   at jet level $n+1$ via the brane-tower :refterm[descent]{#descent} (which carries
   an explicit $q$-grading separating levels).

Step 4 is the categorical content of "ascension". The operator
pentagon is a heuristic; the rigorous version uses the
brane-tower's $q$-graded jet ascension, not a non-commutative
operator identity on $\hat V$'s.

## Operator lift (where pentagon would apply)

For completeness: the $q$-deformed brane tower
([def:recursive-brane-tower](../lifting-and-descent/recursive-brane-tower.md))
admits a non-commutative quantization in which the level-shift
operator $\hat\tau_n$ supplies the canonical pair $u, v$
satisfying $uv = q\,vu$. Specifically, if $\widehat U_i$ and
$\widehat V_j$ denote level-shift conjugates of $\hat V_i$ and
$\hat V_j$ at adjacent jet levels $n$ and $n+1$, the :refterm[descent]{#descent}
involution induces

$$
  \widehat U_i \widehat V_j
  \;=\;
  q\, \widehat V_j \widehat U_i.
$$

In this **operator lift** the pentagon does apply, and gives the
ascension between adjacent jet levels.  The traced volumes
$\hat V_i$ are the **scalar projections** of $\widehat U_i$ and
$\widehat V_j$ onto a single level (level $n$, say); in this
projection the q-grading collapses, the operators become scalars,
and the pentagon collapses to a tautology.

The apparent tension is therefore resolved as follows: the pentagon
identity is a feature of the **operator lift** (between adjacent
jet levels), not of the scalar $\hat V_i$'s within a single jet
level.
