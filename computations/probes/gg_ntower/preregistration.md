# γγ production climbing the strand-count tower: pre-registration

Written and committed **before any character was computed**. Owner request, 2026-10-11 (thread: O'Hara / γγ selection): "3 / resolve — climbing n is planned but unfinished (`sdp_gamma_gamma_to_qqbar.py`: H₂ → H₃ → … → H₆)". Owner ruling the same day: **reading 3 applies at every level of the tower.** Issue #7727. Beans `qou-ales`, `qou-99qc`.

Nothing here ranks, selects, or compares with Q_β, CODATA, AME or any mass. Every fork has a default fixed below. Anything computed under a non-default choice is reported in its own column and labelled.

## 0. What the scaffold actually contains

`computations/sdp_gamma_gamma_to_qqbar.py` is an outline. It solves nothing above H₂. Its H₃ section is a dictionary describing the Wedderburn blocks, and its "path forward" lists H₄ (diquark), H₅ (uud), H₆ (deuteron) as future work, each with a Littlewood–Richardson embedding. So there is no existing n-tower construction to finish. This probe defines the smallest one the corpus supports and tests it.

## 1. The construction (fixed)

**Vertex.** One γγ collision on three adjacent strands i, i+1, i+2 is

    V_i = σ_i σ_{i+1}⁻¹,

which is the reading the selection uses (`gamma_gamma_pair_production_decomposition.py`). The bare Breit–Wheeler product U_i = σ_i σ_{i+1} (the other reading that coexists in the corpus, see `GammaGammaWordSelection.lean`) is computed in a **secondary** column, never mixed with V.

**Climbing.** The j-th collision (j = 0, 1, …, k−1) acts at position p_j = s·j, where the integer **shift** s fixes how far each collision moves along the strands. Products are read left to right in time order, as V³ is. The element after k collisions is

    W_k^(s) = V_{p_0} V_{p_1} ⋯ V_{p_{k−1}} ∈ H_n(q),   n = |s|(k−1) + 3.

For s < 0 the positions are offset so the lowest is 0. The shifts computed are s ∈ {0, +1, −1, +2, −2, +3}:

- s = 0 is the existing h-tower (all collisions on the same three strands). It is the baseline and the cross-check.
- s = ±1 adds one strand per collision.
- s = ±2 adds two strands per collision; consecutive collisions share one strand.
- s = +3 puts the collisions on disjoint strands (a tensor product).

Range: every (s, k) with k ≥ 1 and n ≤ 9.

**Default for the direction fork.** No default is chosen between s = +1 and s = −1, or +2 and −2. Both are computed and reported side by side.

## 2. A structural fact found while designing (before computing)

For s = +1 the collisions telescope **in the braid group**, before any Hecke relation is used:

    V_0 V_1 = σ_0 σ_1⁻¹ σ_1 σ_2⁻¹ = σ_0 σ_2⁻¹,   and generally   W_k^(+1) = σ_0 σ_k⁻¹  (k ≥ 1).

So the upward one-strand staircase is two crossings at opposite ends, for every k. This holds in any group: ∏_{j<k} g_j g_{j+1}⁻¹ = g_0 g_k⁻¹. It is stated and proved in Lean (`QOU/QBeta/GammaGammaStaircaseTelescopes.lean`) before the probe runs. It is reported as a **structural observation about this construction** (scope a: this placement alone degenerates). It is not an exclusion of climbing n. The s = +1 rows are still computed, as a check of the identity.

## 3. Closing strands: the Markov conditional expectation (fixed)

Convention D (z = q³/(q²+1)) is the canonical trace. Its Markov weights are

    y_λ = [λ₁ − λ₂ + 1]_q / [2]_q^n   for two-row λ ⊢ n,   y_λ = 0 for three or more rows,

(the SU(2) Schur–Weyl weights; checked below against `markov_weights_symbolic.y_lambda_symbolic`). The conditional expectation E: H_{m+1} → H_m closes the **top** strand: E(a) = a and E(a σ_m b) = z·ab for a, b ∈ H_m. On characters, for two-row μ ⊢ m,

    χ_μ(E(x)) = Σ_{λ ⊢ m+1} (y_λ / y_μ) · Σ_{T ∈ SYT(λ), T restricted to {1..m} has shape μ} ρ_λ(x)_{TT},

using Young's seminormal form, whose basis is restriction-compatible. Closing several strands iterates this sum over chains.

**Default for the closing fork.** Strands are closed from the top (the standard Jones tower H_m ⊂ H_{m+1} on the first m strands). Closing from the bottom is not computed.

## 4. Reading 3 at every level (fixed, owner ruling)

At level m (3 ≤ m ≤ n), let x_m = E_{n→m}(W) (x_n = W). Reading 3 at level m holds if χ_μ(x_m) ≥ 0 for every λ ⊢ m with y_λ > 0, i.e. every partition with at most two rows. The element is **admissible** if reading 3 holds at every level from 3 to n.

Signs are reported in two ways:

- at the proton pin q₀ (`qou_substrate.constants.Q_50_DIGIT_STR`);
- as exact rational functions of q, with the sign on all of (1, ∞) and the real roots in (1, 2).

Exact zeros count as passing (≥ 0) and are listed.

## 5. The h-expansion check against the h-tower table (fixed)

With t = q − 1 (h = 2t + O(t²), so leading orders in t and h coincide), for each (s, k) report:

- the q = 1 value of each χ_μ at each level;
- the leading order in t of χ_μ(q) − χ_μ(1).

The h-tower table (`/mnt/project-files/qbeta-ohara/gg-production-walkthrough.md`) states that for the same-strand core V³: V³ − 1 = O(h²), and χ_(2,1)(V³) − 2 = −h⁴(3 + h²). The pre-stated comparison:

- for each s, does χ_μ(E_{n→3}(W_3^(s))) depart from its q = 1 value at the **same** leading order as χ_μ(V³), for μ = (3) and (2,1)? Answer **agree** or **differ**, per s.

Flavour and binding are not in this construction (it has no quark letters and only one nucleon's worth of collisions), so the table's "flavour at h¹" and "binding at h⁴" rows are **not tested**. That is a stated limit, not a result.

## 6. Checks (pass/fail fixed in advance)

- C1. The seminormal matrices satisfy σ_i² = hσ_i + 1 and the braid relations, exactly, for every two-row λ ⊢ n, n ≤ 9.
- C2. y_λ as above equals `y_lambda_symbolic(n)` for n = 3..6; Σ_λ y_λ f^λ = 1; and tr(σ) = z_D at n = 2.
- C3. The character formula for E satisfies E(a) = a and E(aσ_m b) = z·ab, on characters, for a sample of words a, b ∈ H_m, m = 3..5.
- C4. s = 0 reproduces the h-tower: χ_(2,1)(V³) − 2 = −h⁴(3 + h²) exactly, and for k ≤ 6 reading 3 at n = 3 holds iff 3 | k.
- C5. s = +1 reproduces the telescoping: the characters of W_k^(+1) equal those of σ_0 σ_k⁻¹, exactly.

## 7. Outcomes (stated before computing)

- (i) For some s ≠ 0, some k gives an element admissible at every level. Reported with its k-pattern; nothing is adopted.
- (ii) For no s ≠ 0 is any k admissible at every level.
- (iii) Admissibility at the top level and at the closed-down levels disagree (an element passes at n but fails at some m < n, or the reverse). This is the case the "every level" ruling exists to catch, and it is reported per (s, k).

Each outcome is reported separately for the primary vertex V and the secondary vertex U.

## 8. What this does not do

It does not build quarks, gluons or flavour. It does not build two nucleons. It does not use the open tower classes of `HeckeTowerBasicConstruction.lean` as hypotheses; E is computed concretely from the trace. Exact sympy arithmetic over ℚ(q); mpmath at 60 dps for values at q₀; no float64.
