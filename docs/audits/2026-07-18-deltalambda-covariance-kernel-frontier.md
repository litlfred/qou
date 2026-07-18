# The Δ_λ covariance kernel: attack log, free-cumulant framing, and Lean infrastructure

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-covariance-kernel-frontier-2026-07-18` ·
**Tier:** frontier map + verified framing + Lean infrastructure (kernel carried as an open
conjecture) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7).
**Follows:** #3959 (the reduction of the Δ_λ sub-lemma (D) to this kernel).

## The open kernel

The Δ_λ super-exponential growth bound (#3939) reduces (via #3959) to a single inequality:

> **`T₃ = Σ_λ (f^λ)² χ^λ(3-cycle) ≤ 0`**, equivalently **`Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`**,
> equivalently (content form) **`∀ k, Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0`**.

This note pushes the attack, records the framing that situates it correctly, and adds Lean
infrastructure — but the kernel remains **open**.

## A. Extended verification

`T₃ < 0` strictly for **all k = 3…40** (computed from hook dimensions + contents only). The margin
`−4T₃/T₁` decreases monotonically (0.800 at k=3 → 0.00756 at k=30 → 0.00493 at k=40), matching the
sharp asymptotic `E[f^{λ/(2,1)}]/E[f^λ] → 1/3⁺` — so (D)'s bound is tight, not slack.

## B. Free-cumulant framing (verified exactly)

With `Σ̂₃(λ) = (k)₃·χ^λ(3-cycle)/f^λ = 3(C₂(λ) − C(k,2))`, `C₂ = Σ_□c(□)²`, and `R_j` the free
cumulants of the transition measure of `λ` (`R₂ = M₂ = k`, `R₄ = M₄ − 2M₂²`), verified for **all λ,
k ≤ 14**:

    Σ̂₃ = R₄ + R₂          (Kerov polynomial),
    E_Planch[R₄] = −k       (exact),

so the kernel is **equivalent to `Cov_Planch(f^λ, R₄) ≤ 0`** — dimension anti-correlates with the
4th free cumulant of the shape. This re-expresses (not closes) the kernel, but places it in the
correct Biane–Śniady setting. The **RSK form** is `T₃ = Σ_{w∈S_k} χ^{sh(w)}(3-cycle)` — the 3-cycle
character averaged over the RSK shape of a uniform permutation (a Kerov-CLT observable).

## Why elementary approaches do not close it (recorded, so they are not retried)

- **Per-λ sign is false** — the row shape `(k)` gives `χ^λ(3-cycle) = +1 > 0`; the sign holds only
  on the `(f^λ)²`-weighted average.
- **No positivity model** — `T₃ = Σ(f^λ)²χ³` is the *undivided* character sum (`Σχ³`, not
  `Σχ³/f^λ`), so it is **not** a connection-coefficient count and has no manifestly-nonnegative
  interpretation.
- **Crude character-ratio bounds fail** — `|χ³/f^λ| ≤ 1` is *attained* (=1) at the extremes, so no
  uniform `< 1/3` bound exists; the sign is genuinely needed.

Mechanism: the two extreme shapes (row, column) each contribute exactly `+1`; the balanced bulk
(large `(f^λ)²`, contents concentrated ⇒ `C₂ < C(k,2)` ⇒ `χ₃ < 0`) supplies the dominant negative.

## Lean infrastructure (added)

Full `S_k`-character theory / free probability is a large upstream Mathlib project. But the kernel's
**elementary content form** needs only hook dimensions + contents, which are built self-contained:

- [`QOU/BraidsAndKnots/DeltaLambdaDReduction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDReduction.lean)
  — **`D_of_T3_nonpos`** (sorry-free, lean-direct exit 0): from the exact moment identity
  `6(W−E) = T₁ − 4T₃ − 3T₂`, `T₂ = 0`, `0 ≤ T₁`, the sub-lemma (D) `E ≤ W` follows from `T₃ ≤ 0`.
  With #3939's `wstd_ge_quarter_lower_bound`, the entire chain **from the kernel `T₃ ≤ 0` to the
  growth bound is Lean-proved**, leaving only `T₃ ≤ 0` open.
- [`QOU/BraidsAndKnots/YoungDiagramKernel.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean)
  — elementary Young-diagram machinery on `List ℕ` (`partsOf`, `contentSq`, `conj`, `hookProd`,
  `sytDim`, `kernelValue`) and the kernel stated as the content-bearing conjecture
  **`covariance_kernel_conjecture : kernelValue k ≤ 0`** (§3b `sorry`-conjecture, OPEN). The defs are
  **positive-controlled** against the Python: `#eval` gives `partsOf 4` = the 5 partitions,
  `sytDim [2,2] = 2`, `contentSq [2,2] = 2`, and `kernelValue 3,4,5 = −4,−16,−320` — matching the
  probe exactly. So the conjecture is a faithful, well-typed statement of the open kernel, not a
  placeholder.

## Verdict

The covariance kernel is a **Biane–Śniady / Kerov-CLT character-ratio anti-correlation**; the
closing machinery is Śniady's genus expansion of the joint cumulants of characters, or the Kerov
CLT covariance structure. **Not closed** here. What is delivered: verification `k ≤ 40`, the exact
free-cumulant framing, a sorry-free Lean reduction from the kernel to the growth bound, and a
faithful (positive-controlled) Lean statement of the open kernel. No fit; nothing wired.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_kernel_frontier.py`](../../computations/deltalambda/wlambda_covariance_kernel_frontier.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-kernel-frontier.witness.json`
- Lean: `DeltaLambdaDReduction.lean` (sorry-free), `YoungDiagramKernel.lean` (kernel conjecture, positive-controlled)

## Cross-references

- The reduction to this kernel: [`2026-07-18-deltalambda-D-reduction-content-covariance.md`](2026-07-18-deltalambda-D-reduction-content-covariance.md) (#3959)
- The growth bound + its Lean core: [`2026-07-18-wstd-superexp-lower-bound.md`](2026-07-18-wstd-superexp-lower-bound.md) (#3939)
- Literature: Biane (Adv. Math. 1998), Śniady (PTRF 2006), Morales–Pak–Panova (arXiv:1610.07561), Fulman (arXiv:math/0305423)
