---
# qou-wtny
title: 'SW-3: dimension identity Σ_{λ⊢n} d_λ² = n! (RSK)'
status: todo
type: task
priority: normal
created_at: 2026-08-02T19:30:46Z
updated_at: 2026-08-19T13:41:54Z
parent: qou-59vq
blocked_by:
    - qou-rsbf
---

Depends SW-2. The Robinson-Schensted-Knuth count Σ_λ (#SYT λ)² = n!. Mathlib may have RSK (Combinatorics.RSK?). This is the surjectivity/dimension anchor for the Wedderburn iso. Ref: [macdonald1995].

## Refinement (2026-08-02, from SW-2 agent)
Partly done in-repo: `QOU.Mathlib.rskBurnsideHolds_le12` proves Σ_{λ⊢n} dimSYT²=n!
for n≤12 by `decide` (via hook-length bridge dimSYT_eq_dimHLF); Schensted stack
(SchenstedInsertion/Recording/RSKBridge) exists. General RSK (S_n ≃ Σ_λ SYT²) is
the missing piece — NOT in Mathlib v4.24.0. `sum_dLambda_sq_eq_iff` (YoungTableaux.lean)
connects the SW `dLambda` form to `QOU.Mathlib.RSKBurnsideHolds n`.


## Measured 2026-08-19 — THREE routes exist; a sibling owns the closest one

Do not start this cold. Corpus-grepped, the identity has three live attacks:

1. **`OVTopAssembly.sum_numSYT_sq_eq_factorial`** (BraidKnot/OVTopAssembly.lean:222)
   — *states* it, carries a `sorryAx` (the RSK bijection). `BurnsideDischarge`
   consumes it and says so honestly. This is the thing to retire, not to reprove.
2. **`qou-3c2j` (sibling, PRs #5139/#5151/#5156)** — representation-theoretic:
   k[S_n] isotypic decomposition, m_mu = dim Hom_G(k[G], S^mu) = dim S^mu, so
   n! = sum_mu (dim S^mu)^2. Both equalities landed sorry-free
   (`SpechtSchurDiagonal.finrank_homG_specht`, `RegularHom.homGRegularEquiv`);
   one brick left (sSup_isotypicComponents -> a finrank sum over PartitionIndex).
   **Closest to done — this is the one to expect.**
3. **`Mathlib/BurnsideViaBranching.lean`** — combinatorial, RSK-free. The
   *reduction* is done and sorry-free (`sum_sq_step` for an abstract bipartite
   incidence + `sum_sq_factorial_of_step`). Remaining: instantiate on the Young
   lattice, i.e. **hdown** (f^lambda = sum over corners, easy) and **hup**
   (sum_{lambda > mu} f^lambda = n . f^mu, the DU - UD = I identity — substantial).
   That file's own header says hup is the LARGER of the two remaining obligations
   and recommends this be a verification route, not the primary attack.

So SW-3 stays open but is **not unowned**. Anyone picking it up should either
help land route 2's last brick, or take route 3's `hup` as a deliberate second
independent confirmation (permitted — open-outcome research) and say so.
