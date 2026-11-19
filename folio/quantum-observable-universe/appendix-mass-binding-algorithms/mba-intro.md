**Purpose.**
This appendix bridges the categorical derivation chain to the executable compute layer that generates every numerical prediction. For each step of the substrate-to-observable chain, this appendix details the algorithm, its justifying propositions, the canonical Python API entry point, and the corresponding witness-JSON record.

**Layered compute stack.**
The Python API provides a facade over a layered stack:

1. **Layer 1 — Rust core** (`hecke-engine` crate): the Gröbner–Shirshov reducer, Hoefsmit representation, Markov trace, and Clarabel SDP backend.
2. **Layer 2a — `qou-substrate`** (Python): substrate constant $q_0$, mpmath precision discipline, and the `WitnessBuilder` schema.
3. **Layer 2b — `pyhecke` / `pyhecke-native`** (Python / PyO3): bindings invoking the Rust core directly.
4. **Layer 3 — `qou_mass.api`** (Python prediction facade): external-researcher API exposing `predict()`, `compute_tr_M()`, and `canonical_braid()`.

**Conventions.**
*Precision* reports in two legs: L1 (internal compute agreement, target $10^{-15}$) and L2 (per-observable absolute accuracy, target $\sigma_{\mathrm{pred}} \leq \sigma_{\mathrm{exp}} / 100$). *Status flags* mirror the canonical derivation table: *proved* (unconditional theorem), *derived* (categorical, no fit), *conditional* (conjecture-conditional), *open* (open question, no derivation yet). Witness filenames refer to the canonical numerical certificates.

**Reading order.**
A chain-map table maps each step to its propositions and API call. Subsequent sections expand each step into a per-algorithm block in dependency order. Sidecar algorithms appear after the eleven canonical steps.

**Maintenance contract.**
This appendix is the bridge between the theoretical propositions and the executable compute. A proposition (Steps 9a, 9b, 10, 11), its canonical script, its witness JSON and the algorithm block below are kept in step with one another, so that the algorithm stated here is the algorithm that was run.
