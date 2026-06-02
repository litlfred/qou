**Purpose.**
This appendix bridges the categorical derivation chain
(propositions, lemmas, theorems in the body of the paper) to the
executable compute layer used to generate every numerical
prediction. For each step of the substrate-to-observable chain we
name (i) the algorithm, (ii) the propositions that justify its
correctness, (iii) the canonical Python API entry point, and
(iv) the witness-JSON record that captures its output.

**Layered compute stack.**
The Python API is itself a thin facade over a layered stack:

1. **Layer 1 — Rust core** (`hecke-engine` crate): the
   Gröbner–Shirshov reducer, Hoefsmit representation, Markov
   trace, and Clarabel SDP backend.
2. **Layer 2a — `qou-substrate`** (Python): substrate constant
   $q_0$, mpmath precision discipline (default 65 dps compute /
   50 dps serialisation), and the `WitnessBuilder` interchange
   schema.
3. **Layer 2b — `pyhecke`** (Python) and **`pyhecke-native`**
   (PyO3 wheel): Hecke / Gram / Markov-trace bindings; native
   bindings invoke the Rust core directly.
4. **Layer 3 — `qou-mass`** (Python facade): external-researcher
   API. Exposes `predict()`, `compute_tr_M()`, and
   `canonical_braid()`.

**Conventions used throughout the appendix.**
*Precision* is reported in two legs: L1 (internal compute
agreement, target $10^{-15}$) and L2 (per-observable absolute
accuracy, target $\sigma_{\mathrm{pred}} \leq \sigma_{\mathrm{exp}} / 100$).
*Status flags* mirror the canonical derivation table: ✅ proved
(sorry-free Lean), 🟢 derived (categorical, no fit),
🟡 conjecture-conditional, 🔴 open gate.
*Witness JSON* paths are relative to `folio-assistant/computations/`
unless stated otherwise.

**Reading order.**
The chain-map section is a single table that maps each step to
its propositions and its API call; the subsequent sections expand
each step into a per-algorithm block (pseudocode, correctness
conditions, complexity, the witness contract) and follow the
chain in dependency order. Sidecar algorithms — the $\Delta_\lambda$
closure attempts, the $c_k$ truncation ladder, the LP/SDP
dual-emission contract, and the witness-JSON pipeline — appear
after the eleven canonical steps.
