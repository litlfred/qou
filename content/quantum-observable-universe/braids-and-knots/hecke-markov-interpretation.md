The stochastic reading of the Hecke algebra
([Hecke transition operator](#prop:hecke-markov-transition))
validates the algebraic framework from a probabilistic
perspective.  Every algebraic construction in the preceding
sections has a Markov chain counterpart, and the two descriptions
are not merely analogous --- they are the same mathematical object
viewed through different lenses.

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
| Quantum dilogarithm $\Phi_q = \sum_i \log\lvert\hat{V}_i\rvert$ | Log-likelihood (free energy) of the path |
| Transfer matrix eigenvalues $q$, $-q^{-1}$ | Boltzmann weights at each lattice site |
| Markov trace weights $w_\lambda$ | Probability measure on irreducible representations |

## Entanglement without information loss

The memorylessness condition (iii) has a striking physical
consequence.  In a Markov chain, each step depends only on
the current state, not the history.  Yet the braid relations
$T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}$ impose
**correlations between non-adjacent generators**: the outcome
at crossing $i$ constrains the outcomes at crossings $i \pm 1$
through the Yang--Baxter equation, even though no information
passes between steps.

This is exactly the mechanism of quantum entanglement in the
QOU framework.  Correlations between distant crossings arise
from the algebraic structure of $H_n(q)$ --- the braid
relations and their representation theory --- not from
step-to-step memory.  The Markov property ensures that each
crossing is a **local, memoryless computation** whose outcome
is determined by the eigenvalue structure $p_+, p_-$ alone.
The non-local correlations (entanglement) are structural:
they are consequences of the representation-theoretic
constraints that $H_n(q)$ imposes on any consistent assignment
of transition probabilities.

## Planck steps and information rate

Each step of the Markov chain is one Hecke evaluation --- one
braid crossing resolved into its symmetric or antisymmetric
channel.  In the Reeb flow picture
([information-theoretic time](#def:information-theoretic-time)),
this is one iteration of $f_q$ on the exceptional divisor,
i.e.\ one **Planck step**.  The Markov chain thus advances
at the Planck rate: $t_P(q_0) \approx 10$ crossings per Reeb
circuit.

The per-step information content is
$H(p_+, p_-) \approx 0.995$ bits --- nearly one bit per
crossing.  Each Planck step extracts almost the maximum
possible information from the binary
(symmetric/antisymmetric) channel.  The slight shortfall
($0.005$ bits) is the $q$-deformation away from the fair coin:
the same asymmetry that produces non-trivial physics
($q_0 \neq 1$) reduces the information rate by
$0.5\%$ per step.

## ASEP as the continuous-time limit

In the continuous-time limit, the Markov chain becomes the
**asymmetric simple exclusion process** (ASEP) with hopping
asymmetry $q$.  Bufetov \cite{bufetov2020} showed that the
ASEP generator is a sum of Hecke algebra elements:

$$
  \mathcal{L}_{\mathrm{ASEP}}
  =
  \sum_{i=1}^{n-1}
  \left[
    p_+ \cdot (\text{swap if in order at } i)
    + p_- \cdot (\text{swap if reversed at } i)
  \right],
$$

which is precisely the generator built from the transition
operators $K_i = e_+^{(i)}$
([Hecke transition operator](#prop:hecke-markov-transition)).
The ASEP is integrable because it inherits the algebraic
structure of $H_n(q)$ and its quotient, the Temperley--Lieb
algebra.  The stationary distribution is the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$ --- the unique
probability measure on $S_n$ that weights each permutation
by $q$ raised to its number of inversions
\cite{diaconis-ram2000}.

## Consequences for the algebraic framework

The Markov chain interpretation does not alter the algebraic
content of the preceding propositions --- it validates them.
The product factorization
([product factorization](#thm:markov-trace-product)) is exact
because the crossings are genuinely independent (memoryless).
The Jones polynomial is a link invariant because it is the
partition function of a well-defined stochastic process.  The
transfer matrix eigenvalues are $q$ and $-q^{-1}$ because
these are the Boltzmann weights of the two channels.

In the language of Diaconis--Ram \cite{diaconis-ram2000}, the
entire nuclear physics of the QOU is a systematic-scan
Metropolis algorithm on $S_n$, where $n$ is the number of
strands in the nuclear braid word, $q$ is the substrate
parameter, and the target distribution is the Mallows measure.
The physical observables --- mass, binding energy, decay
rates --- are expectations under this measure, computed via
the Markov trace.
