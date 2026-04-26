Every algebraic construction in the preceding sections has a
Markov chain counterpart
([Hecke transition operator](#prop:hecke-markov-transition)).
The two descriptions are the same mathematical object
viewed through different lenses: the Hecke algebra $H_n(R, q)$
is simultaneously an algebra of braid-group representations
and a space of stochastic transition operators.

## Overview: SYT paths on the Young graph

Fix an irrep $\lambda \vdash n$.  In the Hoefsmit seminormal
form ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)),
the irrep $\rho_\lambda \colon H_n(R, q) \to M_{d_\lambda}(R)$
is built on the basis of **standard Young tableaux** of shape
$\lambda$.  Each such tableau is a saturated chain

$$
  \varnothing = \lambda^{(0)} \nearrow \lambda^{(1)} \nearrow \cdots
    \nearrow \lambda^{(n)} = \lambda
$$

in the **Young graph** (Young lattice), where each step
$\lambda^{(k-1)} \nearrow \lambda^{(k)}$ adds a single box.
The space of all valid SYTs is therefore the space of all
length-$n$ paths from the empty diagram $\varnothing$ to
$\lambda$ on the Young graph, and it is this path space that
plays the role of the **discrete state space** of the chain.

The generator $\sigma_i \in B_n$ acts at step $i$ via the
Hecke-algebra image $\rho_\lambda(\sigma_i)$ (the same symbol
$\sigma_i$ is used for both the braid generator in $B_n$ and
its image in $H_n(R, q)$; context disambiguates), whose
matrix entries in the tableau basis are

$$
  \rho^\lambda_q(\sigma_i)_{T, T'}
  =
  \begin{cases}
    a_{\rho_i}(q) & T' = T, \\
    b(\rho_i, q) & T' = s_i \cdot T, \\
    0 & \text{otherwise},
  \end{cases}
  \qquad
  a_\rho(q) = \frac{q - q^{-1}}{1 - q^{-2\rho}},
  \quad
  b(\rho, q) = \sqrt{a_\rho(q)\,a_{-\rho}(q) + 1},
$$

where $\rho_i = c_T(i{+}1) - c_T(i)$ is the axial distance
between the cells carrying $i$ and $i{+}1$ in $T$
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)).
Every non-zero entry is an **explicit rational / radical
function of $q$**: this is a genuine quantum deformation of the
classical Young seminormal form, which is recovered at $q = 1$
by l'H\^{o}pital ($a_\rho(1) = 1/\rho$).  Because of this
$q$-deformation, the matrix $\rho^\lambda_q(\sigma_i)$ does
**not** contain classical probabilities: its entries are real
but can be negative, and they square to weights that sum to one
only after a Markov trace.  In the physicists' sense,
$\rho^\lambda_q(\sigma_i)$ is a matrix of **probability
amplitudes**, with $q$ playing the role of the deformation
parameter that distinguishes amplitudes from probabilities.

Two compatible pictures coexist on the same algebra:

1. **Amplitude picture.** On the SYT path space of irrep
   $\lambda$, amplitudes $\rho^\lambda(\sigma_i)_{T, T'}$
   evolve a complex state vector $\psi(T)$.  The Jones
   polynomial
   $J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$
   ([Jones--Markov trace](#thm:jones-markov-trace)) is the
   closed-path sum of these amplitudes over all SYT paths,
   weighted by the Markov trace weights $w_\lambda$ — exactly
   the shape of a Feynman path integral.

2. **Probability picture.** Summing the amplitudes through
   the spectral idempotents
   $e_\pm^{(i)} = (\sigma_i + q^{-1})/(q + q^{-1})$,
   $(q - \sigma_i)/(q + q^{-1})$
   ([Hecke transition operator](#prop:hecke-markov-transition))
   yields the classical stochastic operator
   $K_i = p_+ \cdot \mathrm{id} + p_- \cdot s_i$ with
   $p_\pm = q^{\pm 1}/(q + q^{-1})$.  This $K_i$ is the
   row-stochastic Markov kernel targeting the Mallows
   measure \cite{diaconis-ram2000}.

The two pictures are related by the quadratic Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$: the amplitudes living on SYT
edges square, via the idempotents, to the symmetric /
antisymmetric Boltzmann weights of the classical chain.  SYT
paths on the Young graph are therefore the **quantum sample
space**, and the Markov chain of §2 is its classical shadow.

### Jucys--Murphy / SYT cell reindexing

In the same SYT basis, the Jucys--Murphy elements
$L_k = \sigma_{k-1}\cdots \sigma_1 \sigma_1 \cdots \sigma_{k-1}$ act diagonally
with eigenvalue $q^{2 c_T(k)}$, where $c_T(k)$ is the content
of the cell added at step $k$ of the tableau.  Because
$[L_i, L_j] = 0$, pairs of SYT cells are on equal footing with
no adjacent/far distinction; this is the representation-
theoretic origin of the uniform all-pairs coupling seen in the
mass-tower empirical probes on the
`claude/fix-partitions-shell-operator-TFznx` branch (see the
SYT/Jucys--Murphy reindexing of the mass-tower pair set
developed there).  The amplitude-to-probability passage above
is therefore also a passage from the **generator indexing** of
the chain to the **cell indexing** of the Young graph paths.

## Dictionary

| Algebraic object | Markov chain reading |
|:-----------------|:---------------------|
| Hecke generator $\sigma_i$ | One-step transition operator at crossing $i$ |
| Eigenvalues $q$, $-q^{-1}$ | Boltzmann weights of symmetric / antisymmetric channels |
| Idempotents $e_+^{(i)}$, $e_-^{(i)}$ | Projectors onto the two outcomes |
| Markov property $\mathrm{tr}(x\sigma_n) = z\mathrm{tr}(x)$ | Memorylessness: step $n$ independent of history $x$ |
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
$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ impose
**correlations between non-adjacent generators**: the outcome
at crossing $i$ constrains the outcomes at crossings $i \pm 1$
through the Yang--Baxter equation.

Correlations between distant crossings arise from the
algebraic structure of $H_n(R, q)$ --- the braid relations and
their representation theory --- not from step-to-step memory.
Each crossing is a **local, memoryless transition** whose
outcome is determined by the eigenvalue structure
$p_+, p_-$ alone.  The non-local correlations are
representation-theoretic: they are consequences of the
constraints that $H_n(R, q)$ imposes on any consistent
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
structure of $H_n(R, q)$ and its quotient, the Temperley--Lieb
algebra.  The stationary distribution is the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$ --- the unique
probability measure on $S_n$ that weights each permutation
by $q$ raised to its number of inversions
\cite{diaconis-ram2000}.

## Consequences

The product factorization
([product factorization](#thm:markov-trace-product)) is exact
because the crossings are independent (memoryless).  The Jones
polynomial is a link invariant because it is the partition
function of a well-defined stochastic process.  The transfer
matrix eigenvalues are $q$ and $-q^{-1}$ because these are
the Boltzmann weights of the two channels.

In the language of Diaconis--Ram \cite{diaconis-ram2000}, the
nuclear physics of the QOU is a systematic-scan Metropolis
algorithm on $S_n$: $n$ is the number of strands in the
nuclear braid word, $q$ is the substrate parameter, and the
target distribution is the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$.  Physical
observables --- mass, binding energy, decay rates --- are
expectations under this measure, computed via the Markov trace.
