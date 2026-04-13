Every algebraic construction in the preceding sections has a
Markov chain counterpart
([Hecke transition operator](#prop:hecke-markov-transition)).
The two descriptions are the same mathematical object
viewed through different lenses: the Hecke algebra $H_n(q)$
is simultaneously an algebra of braid-group representations
and a space of stochastic transition operators.

## Dictionary

| Algebraic object | Markov chain reading |
|:-----------------|:---------------------|
| Hecke generator $T_i$ | One-step transition operator at crossing $i$ |
| Eigenvalues $q$, $-q^{-1}$ | Boltzmann weights of symmetric / antisymmetric channels |
| Idempotents $e_+^{(i)}$, $e_-^{(i)}$ | Projectors onto the two outcomes |
| Markov property $\mathrm{tr}(xT_n) = z\mathrm{tr}(x)$ | Memorylessness: step $n$ independent of history $x$ |
| Vertex volume $\hat{V}_i = z a_i + b_i$ | One-step conditional expectation |
| Product $\prod_i \hat{V}_i$ | Product of independent random variables |
| Jones polynomial $J_L(q)$ | Partition function of the chain |
| Log-partition function $\log J_L = \sum_i \log\lvert\hat{V}_i\rvert$ | Free energy of the path |
| Transfer matrix eigenvalues $q$, $-q^{-1}$ | Boltzmann weights at each lattice site |
| Markov trace weights $w_\lambda$ | Probability measure on irreducible representations |

## Non-local correlations from local transitions

The memorylessness condition (iii) coexists with non-trivial
correlations.  In the Markov chain, each step depends only on
the current state, not the history.  Yet the braid relations
$T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}$ impose
**correlations between non-adjacent generators**: the outcome
at crossing $i$ constrains the outcomes at crossings $i \pm 1$
through the Yang--Baxter equation.

Correlations between distant crossings arise from the
algebraic structure of $H_n(q)$ --- the braid relations and
their representation theory --- not from step-to-step memory.
Each crossing is a **local, memoryless transition** whose
outcome is determined by the eigenvalue structure
$p_+, p_-$ alone.  The non-local correlations are
representation-theoretic: they are consequences of the
constraints that $H_n(q)$ imposes on any consistent
assignment of transition probabilities.

## Planck steps

Each step of the Markov chain is one Hecke evaluation --- one
braid crossing resolved into its symmetric or antisymmetric
channel.  In the Reeb flow picture
([information-theoretic time](#def:information-theoretic-time)),
this is one iteration of $f_q$ on the exceptional divisor,
i.e.\ one **Planck step**.

The per-step Shannon entropy $H(p_+, p_-)$ is bounded above
by $\ln 2$ (the fair-coin maximum at $q = 1$) and bounded
below by $0$ (the deterministic limit $q \to \infty$).  For
any $q > 1$, $p_+ > p_-$ and the entropy is strictly less than
$\ln 2$: the $q$-deformation away from the fair coin reduces
the information content per crossing.

## ASEP as the continuous-time limit

In the continuous-time limit, the Markov chain becomes the
**asymmetric simple exclusion process** (ASEP) with hopping
asymmetry $q$.  Bufetov \cite{bufetov2020} showed that the
ASEP generator is a sum of Hecke algebra elements:

$$
  \mathcal{L}_{\mathrm{ASEP}}
  =
  \sum_{i=1}^{n-1}
  \bigl(
    p_+ \cdot e_+^{(i)} + p_- \cdot e_-^{(i)} \cdot s_i
  \bigr),
$$

which is the generator built from the transition operators
$K_i$
([Hecke transition operator](#prop:hecke-markov-transition)).
The ASEP is integrable because it inherits the algebraic
structure of $H_n(q)$ and its quotient, the Temperley--Lieb
algebra.  The stationary distribution is the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$ --- the unique
probability measure on $S_n$ that weights each permutation
by $q$ raised to its number of inversions
\cite{diaconisram2000}.

## Consequences

The product factorization
([product factorization](#thm:markov-trace-product)) is exact
because the crossings are independent (memoryless).  The Jones
polynomial is a link invariant because it is the partition
function of a well-defined stochastic process.  The transfer
matrix eigenvalues are $q$ and $-q^{-1}$ because these are
the Boltzmann weights of the two channels.

In the language of Diaconis--Ram \cite{diaconisram2000}, the
nuclear physics of the QOU is a systematic-scan Metropolis
algorithm on $S_n$: $n$ is the number of strands in the
nuclear braid word, $q$ is the substrate parameter, and the
target distribution is the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$.  Physical
observables --- mass, binding energy, decay rates --- are
expectations under this measure, computed via the Markov trace.
