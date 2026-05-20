This section frames every Planck-time step as the application of a
single transfer matrix on the brane fibre.  The total cost of a
finite computation is the product of the matrices encountered along
its braid word, and the per-step entropy is the operational entropy
$\eta_q$ of the substrate.

The technical content is split across the rest of the section:

- [Toffoli transfer matrix](#prop:toffoli-transfer-matrix) — the
  universal classical gate as a $2 \times 2$ matrix on $\Sigma_3$.
- [Toffoli $q$-AND amplitudes](#rem:toffoli-q-and) — the explicit
  amplitude formula and its $q \to 1$ limit.
- [Toffoli LP stability](#prop:toffoli-lp-stability) — robustness of
  the gate's binding under noise.
- [$q$-Game of Life](#prop:q-game-of-life) — a worked discrete
  dynamical system on the substrate.
- [Substrate computation](#rem:substrate-computation) — why the
  combinatorics is medium-independent ("computers from stones").
- [Quantum computational universality](#conj:quantum-computational-universality)
  and [Skein Turing machine](#rem:skein-turing-machine) — the closure
  argument: every Turing machine of $N$ gates encodes as a braid with
  $c = 3N$ crossings.

Each Planck step is an application of one of these matrices; the
information-theoretic cost is bounded by the bandwidth $\mathfrak{B}(q)$
([information speed of light](#def:information-speed-of-light)).
