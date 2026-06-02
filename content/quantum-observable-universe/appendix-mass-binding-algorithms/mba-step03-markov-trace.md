**Algorithm (Markov trace on $H_n(q)$).**
*Compute the categorical observation
$\mathrm{tr}_M\colon H_n(q) \to R[q, q^{-1}]$ of a braid word
$w \in B_n$ in Hecke normal form.*

### Input

- *Braid word $w = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_k}^{\varepsilon_k}$ in
  $B_n$ (the closure of $w$ is the knot or link whose mass we
  predict).*
- *Substrate parameter $q \in R$ — either symbolic
  (for an algebraic identity) or pinned to $q_0$
  for a numerical evaluation.*

### Output

- *The Markov trace
  $\mathrm{tr}_M(\rho(w)) \in R[q, q^{-1}]$ as a Laurent polynomial
  (symbolic mode) or as an arbitrary-precision scalar evaluation at
  $q = q_0$ (numerical mode).*

### Algorithm

```
1. Reduce w to its Hecke normal form NF(w) via the
   Gröbner–Shirshov rewriter (Algorithm 2).
2. Decompose NF(w) along the Wedderburn isotypic components
   H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(R) (Algorithm 5).
3. For each partition λ ⊢ n with multiplicity y_λ(q), evaluate the
   irreducible character χ^λ(σ_w) on the Hoefsmit representation.
4. Return the Frobenius pairing tr_M(σ_w) = Σ_λ y_λ(q) · χ^λ(σ_w).
```

### Correctness conditions

*Correctness follows from three upstream results.*

1. *Existence and uniqueness of the trace is established by the
   axiomatic closed form
   ([`prop:markov-trace-axiomatic-closed-form`](#prop:markov-trace-axiomatic-closed-form)):
   $\mathrm{tr}_M$ is the unique $R$-linear functional on $H_n(q)$
   satisfying (i) cyclicity, (ii) the Markov axiom
   $\mathrm{tr}_M(a\sigma_n) = z \cdot \mathrm{tr}_M(a)$ for
   $a \in H_n(q)$, and (iii) normalisation
   $\mathrm{tr}_M(1) = 1$.*
2. *The recursive-reducer formula
   ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer))
   gives a terminating reduction strategy by descent on braid index,
   so step 1 always terminates.*
3. *The Frobenius pairing in step 4 is justified by the Wedderburn
   decomposition; cyclicity makes the trace partition-respecting,
   so the sum is well-defined and independent of the chosen
   representative within each conjugacy class.*

### Complexity

*Polynomial in the braid index $n$ and the word length $|w|$ in
the symbolic regime. The dominant cost is the GS reduction in
step 1 (worst case exponential in $n$, polynomial in $|w|$ after
caching cycle-equivalent words). The Wedderburn sum in step 4 has
$|\{\lambda \vdash n\}|$ terms — for nucleon-scale knots
($n \leq 9$) the partition count is at most 30.*

### Python API entry point

```python
from qou_mass import compute_tr_M, canonical_braid

word = canonical_braid(Z=1, N=0)              # proton braid 𝓑₃
trM  = compute_tr_M(Z=1, N=0)                 # Decimal at q = q_0
```

*The lower-level `pyhecke` and `pyhecke-native` bindings expose
the same trace under names
`pyhecke.tr_M(word, q)` (Python reference implementation) and
`pyhecke_native.markov_trace(word, q)` (PyO3 wheel into the
Rust core).*

### Witness contract

*Canonical witness:
[`markov-free-energy-qvalues.witness.json`](../../../folio-assistant/computations/markov-free-energy-qvalues.witness.json).
Per-particle assembly traces are emitted separately as
`markov-trace-assembly-{proton,neutron,deuteron}.derivation.json`.
Each witness records the input braid word, the chosen $q$
evaluation, the resulting Laurent polynomial (symbolic mode) or
mpmath scalar (numerical mode, default 65 dps compute /
50 dps serialisation), and a SHA-256 digest of the canonical
script source for reproducibility.*

### Notes

*Precision regime: the symbolic mode is exact (L1 met
trivially). The numerical mode at $q = q_0$ meets L1 to
$10^{-50}$ by the precision discipline of `qou-substrate`. The
per-observable L2 target inherits the calibration floor of the
downstream mass identity (step 9a).*

*Edge cases: the identity braid $1 \in B_n$ has
$\mathrm{tr}_M(1) = 1$; closure of any braid containing a full
twist $\Delta_n^2$ in the centre acquires a factor
$(q^{n(n-1)})$ from the central character (Schur–Weyl).*
