The :defterm[identification of one $q$-bit with one Skein operation]{#q-bit-skein}
([glossary $q$-bit](#rem:glossary-q-bit)) unifies several structures in the paper.

### One $q$-bit $=$ one crossing resolution

Each application of the Skein relation
([skein generation](#prop:skein-generation))

$$
  qL_+ - q^{-1}L_- = (q - q^{-1})L_0
$$

resolves one crossing.  The resolution produces exactly
one $q$-bit ($= \eta_q$) of information: the choice between
the symmetric channel (eigenvalue $q$, coefficient
$q^{-2}$) and the antisymmetric channel (eigenvalue
$-q^{-1}$, coefficient $1 - q^{-2}$).  The Skein
relation is a convex combination — the $q$-bit is the
information content of this binary choice, weighted by
the Hecke eigenvalues.

### Transfer matrix as $q$-bit register

The categorical transfer matrix
([transfer matrix](#def:categorical-transfer-matrix))
factorizes the Markov trace over generators:

$$
  \mathrm{tr}_M(\rho(\beta))
  = 
  \prod_{i=0}^{n-2} \hat{V}_i(q).
$$

Each vertex volume $\hat{V}_i$ is a one-point correlation
function — the output of **one $q$-bit** evaluated at
the $i$-th insertion point.  The transfer matrix is a
register of $q$-bits: each generator $\sigma_i$ stores
one $q$-bit, and the Markov trace reads out the entire
register.

The transfer matrix product is the **exact factorization**
of the $n$-point function into $n-1$ single-$q$-bit
evaluations.  This is not an approximation — it follows
from the Markov property (the state-operator
correspondence in VOA language).

### Physical processes as $q$-bit computations

The identification makes every physical process in the
QOU a $q$-bit computation:

| Process | $q$-bits consumed | Mechanism |
|---------|-------------------|-----------|
| One Reeb iteration | $1$ $q$-bit ($= \eta_q$) | One $f_q$ evaluation on exceptional divisor |
| One Collatz cycle ($v = 2$) | $3$ $q$-bits | $1$ odd step $+ 2$ even steps |
| Beta decay ($T_{3,5}$) | $10$ $q$-bits | $10$-crossing Skein resolution |
| One Planck time | $n_R = q/(q-1)$ $q$-bits | Full Reeb circuit |
| Jones polynomial of $c$-crossing link | $c$ $q$-bits | Full resolution tree |

Beta decay consumes $10$ $q$-bits because the weak boson
$T_{3,5} = (\sigma_1 \sigma_2)^5$ has $10$ crossings, and
each crossing resolution is one $q$-bit.  The partition
of these $10$ $q$-bits into daughter products ($3$ for the
electron trefoil, $0$ for the antineutrino unknot, $7$
absorbed as R2 moves) is the Gröbner--Shirshov reduction — a
$q$-bit accounting ledger.

### Why this justifies $Q_{\mathrm{cat}}$

The categorical $Q$-value of a nuclear reaction
is the net $q$-bit balance: the difference between the
$q$-bits stored in the parent braid and the $q$-bits
stored in the daughter braids.  Since each crossing is
one $q$-bit, the $Q$-value is the crossing number
difference:

$$
  Q_{\mathrm{cat}}
  = 
  \bigl(c_{\mathrm{parent}} - c_{\mathrm{daughter}}\bigr)
   \cdot  \eta_q
  \quad q\text{-bits}.
$$

This is exact (not a heuristic): the crossing number is
the $q$-bit content of the braid, and the Skein relation
conserves $q$-bits at each resolution step (it's a convex
combination with coefficients summing to $1$).
