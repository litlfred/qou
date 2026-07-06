We frame every Planck-time step as the application of a single transfer matrix on the brane fibre. The product of the matrices encountered along the braid word determines the total cost of a finite computation. The per-step entropy is the operational entropy $\eta_q$ of the substrate.

The technical components construct this computational model:

- [Toffoli transfer matrix](#prop:toffoli-transfer-matrix): We realize the universal classical gate as a $2 \times 2$ matrix on $\Sigma_3$.
- [Toffoli $q$-AND amplitudes](#rem:toffoli-q-and): We provide the explicit amplitude formula and its $q \to 1$ limit.
- [Toffoli LP stability](#prop:toffoli-lp-stability): We demonstrate the robustness of the gate's binding under noise.
- [$q$-Game of Life](#prop:q-game-of-life): We work through a discrete dynamical system on the substrate.
- [Substrate computation](#rem:substrate-computation): We explain why the combinatorics is medium-independent.
- [Quantum computational universality](#conj:quantum-computational-universality) and [Skein Turing machine](#rem:skein-turing-machine): We present the closure argument, showing every Turing machine of $N$ gates encodes as a braid with $c = 3N$ crossings.

Each Planck step applies one of these matrices. The bandwidth $\mathfrak{B}(q)$ bounds the information-theoretic cost ([information speed of light](#def:information-speed-of-light)).
