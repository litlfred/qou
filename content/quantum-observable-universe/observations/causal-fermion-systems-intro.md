Causal fermion systems (CFS), developed by Finster and collaborators
over the past two decades
[`finster2021`, `finster2022`, `finster2024`, `dappiaggi2024`], are a
parallel program for unifying quantum field theory with general
relativity by replacing the smooth spacetime continuum with operators
on a Hilbert space and a universal measure that minimises a causal
action. The framework derives effective linear dynamics for spinorial
wave functions, an effective collapse mechanism, a candidate
baryogenesis mechanism, and a holographic-mixing route to standard
Fock-space QED dynamics — all from variation of the causal action.

QOU and CFS share motivation, share structure, and — as we make
precise below — share carrier algebra and universality class. They
differ in machinery and in one structural respect. CFS works directly
over the complex numbers and encodes information as a Borel measure
$\rho$ on operators with a real-valued Lagrangian $\mathcal{L}(x, y)$.
QOU works pre-Archimedean: states are categorical, traces are
$R$-valued for $R = \mathbb{Z}[q^{\pm 1/2}]$, particles are knots in
the exceptional divisors of the Bring's-surface fibre, and time
evolution is Gröbner–Shirshov reduction on the Hecke algebra
$A_q = H_n(R, q)$.

This section establishes how the two frameworks relate. The
relationship is sharper than "parallel programs" and not quite
"identical theories":

- **Same carrier algebra**
  ([algebraic GNS embedding](#prop:algebraic-gns-embedding)).
  Under the Jones–Wenzl GNS construction, the inductive limit
  $H_\infty(q)$ embeds as a type II$_1$ factor on a Hilbert space —
  the same kind of object CFS operates on. This is *not* a
  conjecture; it is the subfactor machinery in standard form.

- **Same universality class**
  ([q-Plancherel asymptotic skeleton](#prop:q-plancherel-asymptotic-skeleton)).
  Under joint Faddeev / Kerov–Vershik scaling, both QOU and CFS
  asymptotic data sit in the free-probability universality class
  (Voiculescu–Biane). The spectral measure $\tilde w_\lambda$
  converges, in a sense made partly precise by Féray–Méliot, to a
  limit measure on a continuous Young-diagram space, and this limit
  is what CFS's universal measure $\rho$ also describes.

- **CFS is the traceful projection of QOU**
  ([CFS as traceful projection of QOU](#prop:cfs-as-traceful-projection-of-qou)).
  The natural map
  $\Pi_{\mathrm{tr}} \colon (A_q, \mathrm{tr}_M) \to
  (\widehat{A}_q, \tilde w_\lambda, \{\chi_\lambda\})$
  sends QOU's non-commutative algebra to its commutative spectral
  shadow, which is structurally a CFS-style measure + functional
  family. This projection is information-lossy: commutators, braid
  relations, knot crossing-order, and non-trace free-probability
  cumulants all live in the kernel. The QOU phenomena that CFS
  cannot natively express (knot topology, chirality, GS reduction)
  are exactly those that depend on pre-projection algebra structure.

- **The single residual conjecture: Lagrangian universality**
  ([μ_arch continuum limit](#conj:mu-arch-continuum-limit)).
  Both frameworks evaluate a real-valued functional on the same
  free-probability spectral limit: CFS via the max-of-pair-products
  causal Lagrangian, QOU via the Plancherel-weighted character
  generating function $Z_{\mathrm{Pl}}(x \cdot y) = \sum_\lambda
  \tilde w_\lambda \chi_\lambda(x \cdot y)$. Whether the two
  functionals agree on the limit is the open question. Agreement
  would make CFS the continuum realisation of QOU's trace
  projection; disagreement would localise a sharp falsifiable
  difference to a single functional-form mismatch.

Section roadmap. We first state the algebraic causal-action
structure on $A_q$ as a provable proposition assembled from existing
QOU infrastructure (Wedderburn decomposition, Markov trace,
q-Plancherel weight, LP duality). We then promote three previously
conjectural clauses to provable propositions: the GNS embedding
(Jones–Wenzl), the asymptotic Plancherel skeleton (Kerov–Vershik /
Féray–Méliot), and the traceful projection
$\Pi_{\mathrm{tr}}$. What remains conjectural is *one* structural
question — the Lagrangian-universality match — bifurcating into the
"theorem" and "falsifiable mismatch" outcomes above. The section
closes with a remark situating CFS as the post-wall shadow of the
measure-valued lift.
