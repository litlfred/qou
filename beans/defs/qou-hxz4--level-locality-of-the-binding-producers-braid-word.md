---
# qou-hxz4
title: 'Level-locality of the binding producer''s braid words (unified_iterative_correction / hecke_core_legacy): if the per-atom words factor by seminormal level, apply the #7160 path-sum and collapse the O(dim³) wall of qou-sv7h'
status: completed
type: task
priority: normal
created_at: 2026-09-08T07:51:54Z
updated_at: 2026-09-08T08:18:02Z
parent: qou-vyvt
---

Continues qou-sv7h (binding compute cannot scale; 11/11 py-spy samples in hecke_core_legacy.py:1102 dense matmul). #7160 proved χ^λ(T_β) = Σ_{T∈SYT(λ)} Π_j ⟨T|F_j|T⟩ for LEVEL-LOCAL words (each seminormal level touched in one contiguous factor) and shipped computations/chi_path_sum_seminormal.py (raises NotLevelLocal otherwise). Task: (1) extract the exact braid words unified_iterative_correction builds per atom (D, T, ³He, ⁴He at least); (2) test level-locality with the shipped checker; (3) if local, route the binding trace through the path-sum and cross-check against the existing dense route on the atoms it can finish (≤1e-40); (4) if NOT local, state precisely which letters break it and whether a conjugation/reordering restores it (proved, not assumed — Markov trace is conjugation-invariant, the seminormal product is not). mpmath 70 dps, proton pin, no float64. Honest negative is a result.


## ANSWERED 2026-09-08 (bind-local, branch claude/binding-word-level-locality-2026-09-08) — NOT level-local; no trace-preserving reordering restores it; honest negative

Probe `computations/probes/uic_word_level_locality_probe.py` (11/11, 29 s, mpmath 70 dps, proton pin as string); audit `docs/audits/2026-09-08-binding-word-not-level-local.md`.

**Words, captured by instrumenting `_lp_kernel_steps`** (the exact `(c, d, gen)` triples the Rust kernel receives; identical for every partition of a given `k`, equal to `_step_chain_generic(ordering[i], ordering[:i], k-1)`). `L = 11A + C(A,2)`: ²H 23, ³H/³He 36, ⁴He 50, ⁵Li 65. `c = 1` throughout, `d ∈ {0, −h, −h/2, _PN_D_MP}` (pn is the colour-weighted `−0.104458…`, not `−h/2`). Generator index cycles `g mod (k−1)` through every letter of every step: first step at k=4 is `1 2 3 1 2 3 1 2 3 1 2`.

**Level-locality: NO for every atom and every k = 3..11.** `segments_of` returns ONE segment covering all k−1 generators; the first break is letter k (σ_1 recurring after σ_2…σ_{k−1}); every adjacent pair (g, g+1) interleaves, so far-commutation cannot separate any of them.

**Reorderings, both trace identities tested and excluded.**
- Cyclic rotation (tr AB = tr BA): 0 of L rotations has > 1 segment, all atoms, all k. Analytic reason: every window of k−1 consecutive letters holds every generator and L > 2(k−1).
- Hecke-relation rewriting (seminormal rep is a homomorphism): the T_w-support of the word's element lies in NO 2-block parabolic product W_J·W_K / W_K·W_J — min support-outside 2/6, 12/24, 72/120, 480/720, 3600/5040 at k=3..7 (²H smaller supports, still all positive: 2, 6, 46, 334, 480); every rotation at k ≤ 5 likewise. Invariant: supp(T_u T_v) ⊆ {u′v′ : u′ ≤ u, v′ ≤ v}, so a ≥2-interval product's support sits in a 2-block set (reduction checked exhaustively k ≤ 6). scope-(b) for k ≤ 7 and for rotations at every k; scope-(a) for rewriting at k ≥ 8. NOTE the T_{w0}-coefficient test alone is NOT decisive — it is zero for ²H at k=6,7 (23 letters cannot reach w0) — which is why the support test is the one asserted.

**Cost of the degenerate route:** on a single-segment word the path-sum is the O(L·dim²) direct seminormal trace in mpmath — 23×/30×/40× SLOWER than the Rust kernel at k=6/7/8 (dim 16/35/90). It reproduces the kernel to 8.6e-50 (k ≤ 6, D/T/³He/⁴He) — that validates the transcription and buys nothing. Nothing wired, no flag, no recorded number moves.

**Why, structurally:** the producer embeds all crossings of an A-nucleon atom into a FIXED H_k(q), k ≤ 11, by cycling the generator index; a level-local word needs each nucleon on its own strands (n = 3A, the `atom_braid_word_3A` family), which is a DIFFERENT Hecke element with different traces — a re-derivation of the binding producer, not an optimisation.

**Decision framed for the owner (default = no-op):** (1) leave as is — the wall stays at kernel speed (deuterium 942 s kernel-live); (2) re-embed the binding word on 3A strands and use the path-sum — a new producer, every recorded binding number moves (hadron-knot-table, the A-series −7.27…−8.14), the fixed partition table and C_λ / Pass-2 gate need re-definition on λ ⊢ 3A; whether the 3A-strand element is the right binding object is the owner's call and NOT chosen here because it is faster; (3) kernel-side speedups per qou-sv7h. Judgement: 1 now, 2 only as owner-authorised re-derivation.

Calibration: reversing the cycle (s_i ↦ s_{k−i}, conjugation by T_{w0}) preserves every χ^λ to ≤ 3e-50 on the kernel — a genuine trace identity, and still single-segment.

PR: https://github.com/litlfred/qou/pull/7173
