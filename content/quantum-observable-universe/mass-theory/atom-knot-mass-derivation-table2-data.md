| Step | Implementation | Status |
|---|---|---|
| 1a (canonical $T_w$ — joint-tower SDP for *unknown* $T_w$) | R5-full pending — research-grade | ✗ |
| 1b (GB-filtration certificate) | Python the formal derivation (PoC) + Rust `gb_nf_reducer.rs` (R2; 6 unit tests; bit-for-bit match) | ✓ |
| 1c (jet-order log) | same modules | ✓ |
| 1d (Wedderburn-block PSD evaluator) | Python cvxpy at $H_3$ + Rust `wedderburn_psd.rs` (R3; 2 unit tests; scales to $H_5+$) | ✓ |
| 1e (cross-level embedding LR) | Rust `cross_level_embedding.rs` (R4; multi-LR; 2 unit tests including 77-partition $H_{12}$ identity) | ✓ |
| 1f (PSD-cone $\alpha^*$ verifier) | Rust `sdp_verifier.rs` (R5-minimal; bisection equivalent to SDP value function; 2 unit tests) | ✓ |
| 2 (Markov trace symbolic) | the canonical formalism + the canonical formalism | ✓ for $n \leq 12$ |
| 3 ($\nu_{\mathrm{SDP}}(Z, N)$ rule from Wedderburn multiplicity) | downstream of 1a — read off SDP solution multiplicity | ✗ |
| 4 ($M(\mathfrak{H}) = \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H}) \in \mathbb{Q}(q)$) | algebraically trivial once 2 + 3 are in | partial |
| 5 (Archimedean realization at $q_0$ + $m_e$) | MPFR via SymPy/exact algebraic structures | ✓ |
| 6 (AME comparison) | mass-table-ppb witness + the canonical formalism | ✓ |
| 7 (methodology tag) | [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/methodology-deprecation.witness.json) | ✓ |
| 8 (post-Archimedean naming via volume conjecture) | borrowed; not in QOU derivation | ✓ as theorem |
