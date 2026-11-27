---
# qou-x08k
title: 'Session 2026-11-27: close the gaps in the eightfold-way and Standard Model derivation'
status: in-progress
type: epic
priority: high
tags:
    - 8f-index
created_at: 2026-11-27T14:25:39Z
updated_at: 2026-11-27T14:34:43Z
parent: qou-0uga
---

Session epic for the project thread "Close gaps in 8-fold and Standard Model derivation" (owner Carl, 2026-11-27). Arc index and fronts: `qou-8lxd`. This epic holds the session's work items; each child also gets an `8f-*` tag and is cross-linked from `qou-8lxd`.

Rules for this session (owner): no empirical inputs inside formal proofs; prefer Lean; do not merge (merges go through the merge-manager thread); beans are the primary tracker, GitHub issues are only for owner/reviewer submissions.

## Inventory, measured 2026-11-27 on main 52f9f88

- **Lean.** `QOU/EightfoldWay` (55 files) and `QOU/StandardModel` (105 files) carry **0 live `sorry`** (every textual hit is in a comment) and **0 `axiom` declarations** (the one hit, `CircleBundleBettiObstruction.lean:22`, is prose). The gaps are therefore not sorries; they are conjectures, cited-not-proved standard results, and missing constructions.
- **Paper.** Gap ledgers: `eightfold-way/eightfold-open-problems.md` (9 items) and `appendix-standard-model/sm-open-problems.md`. Four conjecture blocks: `conj:gauge-hecke-realization`, `conj:sm-colour-stabilizer-action`, `conj:sm-gauge-truncation`, `conj:sm-hypercharge-invariant`.
- **Beans.** `qou-8lxd` ready counts: flavour 12, ew 11, colour 8, mass 8, lit 7, gen 6, lean 6, qcd 6, arch 4, obs 3, tseries 2, decide 1 (`qou-j3w6`), open-research tag 15.
- **Open PRs touching the arc:** #8229, #8216, #8185, #8140, #8139 (batch-style `qou-8lxd-*` branches, 2026-11-16/17). Triage goes to the merge manager.

## Gap list

**A. Closable in Lean as pure mathematics (no empirical input)**
- A1. Octonionic triple is complex type: the stabilizer `su(3) ⊂ Der(O)` has no invariant symmetric bilinear form on `C^3` (singlet count of `Sym^2` is 0). Today this is a *cited* input (Günaydin–Gürsey) in the Sym² gate ledger row.
- A2. `G_2 = Aut(O)` infrastructure: `Der(O)` has dimension 14, stabilizer of a unit imaginary is the 8-dim `su(3)` (dim gate exists), toward `S^6 = G_2/SU(3)`. Ledger item "Continuous G_2 completion".
- A3. `conj:gauge-hecke-realization`: decide it on an instance. `B_n -> H_n(q)` has a kernel for n ≥ 3 (finite-dim target), so faithfulness on gauge automorphisms needs either an instance or a counterexample.
- A4. Row cap `l(λ) ≤ N` for the Schur–Weyl channel (cited; only the `C(N,3)` arithmetic is proved).

**B. Foundational, needs an owner decision**
- B1. The `N = 3` flavour object `W_3` (`qou-j3w6`, owner decision 4d 2026-10-10: stay conditional). Blocks meson octet, baryon multiplets, quark dictionary, hypercharge, the `z_3` Ocneanu level.

**C. Research conjectures (constructions missing)**
- C1. Hypercharge: second crossing invariant independent of writhe; twist multisets forced, not enumerated.
- C2. Colour algebra acting on the 3-strand Hecke state space (`qou-ni4b`).
- C3. Spin–flavour–colour selection rule (Young symmetriser from the braid structure); this is also the flavour/colour discriminator.
- C4. Gauge truncation containment `SU(3)×SU(2)×U(1) ↪ G_arch` and its `Z_6` global form.
- C5. Freeze-out / root-of-unity truncation mechanism.
- C6. Three generations (`qou-xtcl`; owner 2026-10-10: open problem, no criterion adopted).

**D. Comparison-only, kept out of formal proofs**
- Electroweak `W, Z, H = T(2,4), T(2,6), T(2,8)`, the 26-parameter map, GMO deviation magnitude, mass hierarchies.



## 2026-11-27 14:27Z — owner: tracks A, B and C all approved

Verbatim: *"A B C"*. B reopens `qou-j3w6` as option A (second fundamental $W$, $\Lambda^3 W\cong\mathbf 1$, axiom datum). Order: A1 → B scaffold → C.



## 2026-11-27 — A1 closed in PR #9444

`OctonionColourTripletComplexType.lean` (0 sorry): octonionic colour triple is complex type; `Sym²(3)` has no singlet; `3 ≇ 3̄`. Paper ledger rows updated from 'not excluded (cited)' to 'passes (proved)'. A2 finding: `dim Der(O) = 14` (`octonion_derivation_dim`) and stabilizer dim 8 (`finrank_su3_e1`) were already proved; the ledger row was stale and is corrected in the same PR. Remaining A2: continuous G2 / S^6 coset.
