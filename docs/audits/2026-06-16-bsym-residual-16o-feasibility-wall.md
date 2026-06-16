# B_sym residual — ¹²C extension + the ¹⁶O feasibility wall (2026-06-16)

**Branch:** `claude/lucid-curie-wmr42x` (PR #2349)
**Picks up:** the stalled `bsym_residual_shell_structure.py` follow-up on PR #2325
(`claude/vigilant-brown-x0tzat`, now `dirty` against the #2332 platform migration).
**Discipline:** exploratory shape-probe; derive-or-refute; **no fit; NOT wired.**

## Summary

The B_sym residual `Δ_λ^sym = B_AME / B_sym` (with `B_sym = E₀·ln(tr_free/tr_atom)`,
`E₀ = m_e/(q₀(q₀−1))` derived) was mapped through ⁹Be on #2325; the probe's explicit
follow-up was the **second doubly-magic point ¹⁶O**. With `pyhecke_native` 0.9.0 built
in this container, the probe was extended one feasible rung — to **¹²C** (3α,
α-conjugate) — and ¹⁶O was found to sit **behind an algorithmic feasibility wall**
(~2–3 h) that the Rust engine does **not** lift.

## A. The residual ladder (E₀ = 4.18598 MeV)

| nucleus | A | type | B_sym (MeV) | B_AME (MeV) | **Δ_λ^sym** | wall |
|---|---|---|---|---|---|---|
| D | 2 | pairing/halo | 3.89 | 2.225 | **0.57** | 0.6 s |
| T | 3 | normal | 9.07 | 8.482 | **0.94** | <0.1 s |
| ³He | 3 | normal | 6.80 | 7.718 | **1.14** | <0.1 s |
| ⁴He | 4 | **doubly-magic (2,2)** | 11.97 | 28.296 | **2.36** | 0.1 s |
| ⁵Li | 5 | resonance | 14.88 | 26.328 | **1.77** | 0.4 s |
| ⁶Li | 6 | non-magic | 20.06 | 31.994 | **1.59** | 1.2 s |
| ⁷Li | 7 | non-magic | 25.24 | 39.244 | **1.55** | 3.6 s |
| ⁸Be | 8 | 2α cluster | 28.15 | 56.500 | **2.01** | 9.8 s |
| ⁹Be | 9 | non-magic | 33.32 | 58.165 | **1.75** | 25.6 s |
| **¹²C** | 12 | **3α (α-conj, N=Z)** | 44.32 | 92.162 | **2.08** | **≈ 333 s** |
| ¹⁶O | 16 | doubly-magic (8,8) | — | 127.619 | — | **deferred (~2–3 h)** |

**Verdicts** (exploratory, derive-or-refute):
- **H1 (deuteron over-binds):** ✓ `Δ_λ^sym(D)=0.57 < 0.8` — the generic hyperbolic
  trace over-predicts the anomalously weakly-bound deuteron.
- **H2 (A=3 clean ≈ 1):** ✓ T 0.94, ³He 1.14.
- **H3 (doubly-magic ⁴He under-binding peak):** ✓ `Δ_λ^sym(⁴He)=2.36` exceeds both
  neighbours (³He 1.14, ⁶Li 1.59) and is the global maximum of the ladder.
- **H4 (α-cluster signature):** the α-conjugate nuclei form an elevated band —
  ⁴He 2.36, ⁸Be 2.01, ¹²C 2.08 — all above the non-magic trend (1.55–1.77).

**Honest nuance (do not over-read as "magic-number law").** ¹²C is **not** a magic
nucleus, yet it sits at 2.08, in the same band as the 2α ⁸Be (2.01) and below the
doubly-magic ⁴He (2.36). So the residual elevation tracks **α-clustering / even-even
N=Z**, not magic numbers *per se*. ¹⁶O cannot separate the two readings (it is both
doubly-magic **and** 4α); a magic-but-not-α-conjugate nucleus (e.g. ⁴⁸Ca) would be
the discriminating test. The clean takeaway is structural and modest: B_sym is the
**generic** hyperbolic binding, and its residual carries the SEMF pairing term below
(deuteron) and an α-conjugate/shell-closure surplus above — exactly the two features
the q₀⁵-vs-`B_pred` refutation pointed at.

## B. The ¹⁶O feasibility wall (and a correction to the 2026-06-15 optimization audit)

The trace is `tr_m_atom_via_transfer.tr_m_atom_zn`, a **lossless** sum
`Σ_{λ⊢3A} y_λ χ^λ` over **all `p(3A)` partitions** via the fine-Bratteli transfer
matrix (`chi_monotone_transfer` / `reduced_block_kernel`). Empirically the wall scales
≈ `p(3A)^1.5`:

| A | n=3A | p(3A) | wall |
|---|---|---|---|
| 4 | 12 | 77 | 0.09 s |
| 8 | 24 | 1 575 | ≈ 11 s |
| 9 | 27 | 3 010 | ≈ 26 s |
| 12 | 36 | 17 977 | ≈ 333 s (warm) / 421 s (cold) |
| 16 | 48 | **147 273** | **≈ 1.5–3 h (projected)** |

`p(48) ≈ 8.2× p(36)`; with the fitted exponent `k ≈ 1.4–1.5`, `8.2^k ≈ 17–23×`, so
`¹⁶O ≈ 333–421 s × (17–23) ≈ 1.5–3 h`. Infeasible in a normal session either way.

**Correction to the 2026-06-15 `compute-partial-wiring-and-optimization-audit.md`
(fix #2).** That audit ranked *"install/keep the Rust engine wired → unlocks heavy-A
exact `tr_M` (¹⁶O magic test)."* For **this** binding path that is **orthogonal**:

1. `tr_m_atom_zn` (and `compute_tr_m_via_branching` for A≥3, which simply **delegates
   to it** — see `canonical_tr_m_via_branching.py:392`) is **pure mpmath**:
   `reduced_block_kernel` imports `chi_monotone_transfer` + `mpmath` only, **no
   `pyhecke_native`**. Installing the Rust wheel does not change its wall.
2. The ¹⁶O cost is the **`p(3A)` partition enumeration**, not per-word reduction —
   precisely what the Rust kernel accelerates. So Rust addresses a different
   bottleneck (the `markov_peel` / native per-partition families), not this one.

The Rust install was still worth doing (it accelerates the `markov_peel` /
`laurent_q_rust` trace families used elsewhere), but it does **not** unlock the ¹⁶O
magic test.

## C. The genuine unlock for ¹⁶O

The cost-killer is enumerating all `p(3A)` partitions. The **operator-valued
per-nucleon Wenzl branching** recursion in `canonical_tr_m_via_branching.py` would
avoid it — it peels one nucleon at a time with cost
`Σ_level Σ_{ξ⊢n−3, ν⊢3} dim(ξ)·dim(ν)` (polynomial in A, not `p(3A)`). But that
recursion is **implemented only for A=2** (the H₆ deuteron extract;
`canonical_tr_m_via_branching.py:216` "only A=2 implemented"; the A≥3 recursive call
returns `None` with a diagnostic, and the A≥3 entry point falls back to the
full-`p(3A)` transfer sweep). **Extending the per-nucleon branching recursion to A≥3
is the genuine unlock** for ¹⁶O — not the Rust engine, and not the A≥3 transfer
fallback. This is a non-trivial piece of work (per-interface `A^λ_{ξν}(I)` extracts at
H₉, H₁₂, … must be generated and cached) and is filed as the follow-up.

## D. What landed in PR #2349

- `computations/qbeta/bsym_residual_shell_structure.py` — re-homed onto migrated main,
  extended to ¹²C, with a `--max-a` gate (default 12) that records ¹⁶O as deferred with
  its projected cost.
- `computations/ame-2020-binding-energies.witness.json` — added `B_c12_MeV=92.16173`,
  `B_o16_MeV=127.61931` (AME2020 mass-excess derivation; comparison-only, **not**
  calibration inputs — no 4-CAL inflation).
- `computations/bsym-residual-shell-structure.witness.json` — regenerated through ¹²C.

## E. Sibling cross-links — one coherent low→high story

This probe is the **high-A frontier** of a coordinated B_sym shell-structure study;
two sibling audits work the same residual from the other ends:

- **Low-isotope closed form** ([PR #2343](https://github.com/litlfred/qou/pull/2343),
  `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md`). Establishes that
  `B_sym` is **exactly** a linear-chain pairwise binding,
  `B_sym = α·[(Z−1)·L_pp + L_pn + (N−1)·L_nn]`, additive to the 50-dps floor
  (per-bond n-n 5.18 > p-n 3.89 > p-p 2.91 MeV).
- **Shell-structure framing** (`docs/audits/2026-06-16-binding-undershoot-is-shell-structure.md`).

**What the linear-chain result sharpens here.** Because the chain additivity is
*exact*, the Markov trace carries **zero** cooperative many-body binding — the 4-body
α-unit is *entirely absent* from `B_sym`, not merely under-weighted. So the elevated
α-conjugate band in §A (⁴He 2.36, ⁸Be 2.01, ¹²C 2.08) is measuring precisely the
**missing cooperative α-binding**, and there is no hidden cooperative term to recover
on the low-isotope side. This refines the §A "honest nuance": the residual surplus is
not a re-weighting artefact but the signature of physics the pairwise-exact trace
structurally omits — consistent with the §6 convergence on the **α-cluster recursion
(⁴He as magic input)** as the only non-fitted open lever (matching the #1706
"only α-cluster ships" decision and the §C genuine-unlock direction here).
