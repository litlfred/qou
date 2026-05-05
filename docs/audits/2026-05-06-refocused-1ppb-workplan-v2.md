# Refocused 1-ppb workplan v2 — post path-α-Bring refinement

**Date:** 2026-05-06 (UTC)
**Branch:** `claude/w3-followup-term6-integration`
**Predecessors:**
[`2026-05-05-refocused-1ppb-workplan.md`](2026-05-05-refocused-1ppb-workplan.md) (v1),
[`2026-05-05-path-alpha-bring-refinement.md`](2026-05-05-path-alpha-bring-refinement.md),
[`2026-05-05-nv-categorical-impasse.md`](2026-05-05-nv-categorical-impasse.md).

This version supersedes v1. Major changes since v1:

- W-2 numerical-search line on $N_v$ **closed as null result** (constrained PSLQ on $\mathrm{tr}_{\rm pure}$-based basis returns 0 hits at CODATA tolerance for 116 k-element bar-symmetric basis; FDR ≈ 0.06).
- Path-α-Bring refinement landed: $T(2, 2k)$ for $k = 2, 3, 4$ all embed on Bring; host-distinctness premise dropped; categorical-ring discipline ($q$ generic in $R$, not a root of unity) codified in the affected blocks.
- Plancherel weight **demoted to degenerate special case**; bar-self-dual cell-content trace
  $\mathrm{tr}_{\rm pure}(\sigma_1^4 \sigma_3^6 \sigma_5^8) = 4(q^{18} + q^{-18}) + 2(q^{10} + q^{-10}) + (q^6 + q^{-6}) + 3(q^2 + q^{-2})$
  is the operative quantity.
- Hoefsmit cell-content identification at $n = 6$ authored; eight pure-pattern projectors with multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ summing to 20.
- All Lean class-hypothesis fields now use concrete propositional predicates (no vacuous `True`), per Gemini review on PR #545.

## 1. The 1-ppb floor — current state

The hard floor identified in v1 — $^4\text{He}$ at $+5.87\%$ relative deviation — remains the gating numerical gap. It is now better understood:

- $^4\text{He}$ deviation is structurally tied to the **W-2 / $N_v$ derivation gap**: every β-decay rate scales as $G_F^2 \propto N_v^{-4}$, so any error in $N_v$ propagates to all $A \geq 4$ binding-energy predictions.
- The $\rho_F = 2$ scaling factor in the magic-A formula (flagged in v1 §3) is structurally tied to **Wedderburn-pair volumes** $|V_X V_Y|_{\rm Wedd}$ (PR #534's `wedderburn_pair_volumes.py`).
- Both ties go through the same set of open categorical-physics inputs (path-α-Bring + Hoefsmit cell-content).

The 1-ppb closure therefore reduces to **two chained gaps**:

1. Categorical derivation of $N_v$ (and $\theta_W$, the Weinberg angle, by parallel construction).
2. Categorical derivation of the linked-cluster $|V_X V_Y|_{\rm Wedd}$ structure (PR #534's Piece 2).

Both feed the same downstream — the six-term mass formula at $A \geq 4$ — and resolving either provides a strong cross-check on the other.

## 2. Inventory of authored blocks (this branch)

Recently authored on `claude/w3-followup-term6-integration`:

| Block | Status |
|-------|--------|
| `prop:knot-operator-lp-selection` | Open prop, Lean class with concrete LP-witness predicates (Schrijver §7.2/§7.4) |
| `prop:weak-symmetric-normalization` | Demoted as Plancherel-degenerate; carries explicit "Demoted 2026-05-05" banner |
| `conj:hoefsmit-ew-cell-content` | Open conj, n=6 disjoint-strand-pair identification + multiplicities |
| `conj:categorical-higgs-mechanism` | Skeleton, four open inputs identified |
| `conj:force-carrier-knot-vs-link-dichotomy` | Refined to categorical form (drop host-arithmetic Steps 4–5) |
| `conj:weak-spectral-completeness` | Refined to Hoefsmit n=6 form, bar-self-dual cell-content trace replaces Plancherel weight |
| `conj:electroweak-higgs-torus-link-triplet` | Refined to Bring-internal even-twist complement |
| Audit `2026-05-05-path-alpha-bring-refinement.md` | Pushed; full prioritization plan recorded |
| Audit `2026-05-05-nv-categorical-impasse.md` | Pushed; W-2 numerical-search line closed |

All Lean siblings now use concrete propositional predicates (`IsRootOfUnity`, `EWSpectralCompletenessHolds`, `LinkingOperationDefined`, etc.) — class hypotheses are typed `Prop`, not `True`.

## 3. Open gaps (priority-ordered)

**Tier A — gating for everything else:**

1. **Discharge `conj:hoefsmit-ew-cell-content`'s structural assignment**
   $W \leftrightarrow \sigma_1^4, Z \leftrightarrow \sigma_3^6, H \leftrightarrow \sigma_5^8$.
   Currently a structural proposal motivated by disjoint-strand-pair commutativity + matching twist parameters $k = 2, 3, 4$ to the EW link triplet. Needs:
   - Categorical-physics block tying boson identity to specific $\sigma_i^{2k}$.
   - Either via `conj:categorical-higgs-mechanism` (Step C, Goldstone-eating ↔ ribbon linking) or via Yekutieli rigidity on $\mathbb{Q}(q)$-linear weak-coupling normalisation.

2. **Author `conj:linking-operation`** — categorical analog of topological linking number $\mathrm{lk}$ as ribbon-braiding raised to integer power.
   - Currently a placeholder predicate `LinkingOperationDefined` in the categorical-Higgs Lean class.
   - Connects to Mathlib's `BraidedCategory`/`RibbonCategory` (if available; otherwise an authored definition).

3. **Author `conj:weinberg-angle-categorical`** — $\theta_W$ realised as Hecke eigenvalues / Frobenius traces.
   - Standard physics: $\sin\theta_W \cdot \cos\theta_W = $ specific component of EW gauge-coupling matrix.
   - Categorical: identify $\sin\theta_W, \cos\theta_W$ as $R$-elements computed from the Hoefsmit projector data on $\sigma_1, \sigma_3, \sigma_5$ in $H_6(q)$.

**Tier B — sibling-coordination dependent:**

4. **Pull in `prop:rho-k-graded-expansion`** from PR #534 (commit `076d6d88e`). This factors out $1/(m_e |\mathrm{tr}_M|)$ to expose the term-by-term six-term mass-formula structure. Once integrated, my W-3 closed-form $D(u) = 2^{2A+1} u^{18Z + 21N + 1} (1 + u^2)^{3A - 1}$ slots directly into their graded series.

5. **Pull in `wedderburn_pair_volumes.py`** from PR #534 (commit `06305f30c`). Compute $|V_W V_Z|_{\rm Wedd}, |V_Z V_H|_{\rm Wedd}, |V_W V_H|_{\rm Wedd}$ — these are the **LP/SDP-dual inputs** for the EW-sector operator-selection in `prop:knot-operator-lp-selection`. With the pair amplitudes in hand, the six EW projector multiplicities $(2, 1, 3, 3, 1, 2)$ get concrete physics interpretation.

6. **Cross-validate Hoefsmit multiplicities against PR #546's symbolic engine**. PR #546 has produced closed-form symbolic $\chi^\lambda$ for proton and deuteron; extending to $\sigma_1^4 \sigma_3^6 \sigma_5^8$ on $V^{\otimes 6}$ supplies an independent ground-truth check on my $(4, 2, 1, 3, 3, 1, 2, 4)$ pattern multiplicities and the bar-self-dual closed form $\mathrm{tr}_{\rm pure}$.

**Tier C — once Tier A + B are done:**

7. **Re-run constrained PSLQ for $N_v$ on the cross-sector basis**:
   $\{[2k]_q\,(k = 1\ldots 4), q^k, h^k, \mathrm{tr}_{\rm pure}, \cos\theta_W, \sin\theta_W, |V_W V_Z|_{\rm Wedd}, \ldots\}$.
   The basis is now categorically determined; FDR is small. The **bar-self-duality constraint** persists (any closed form must satisfy $\iota: q \mapsto q^{-1}$ invariance).

8. **Close the $^4\text{He}$ hard floor.** With $N_v$ derived (7) and `wedderburn_pair_volumes.py` integrated (5), the magic-A binding-energy formula's $\rho_F = 2$ factor becomes derived (not empirical). Test the ⁴He prediction at full precision.

## 4. Critical-path graph

```
                                    ┌──────── PR #534 ─────────┐
                                    │ prop:rho-k-graded-       │
                                    │   expansion              │
                                    │ wedderburn_pair_volumes  │
                                    └────────────┬─────────────┘
                                                 │
  conj:hoefsmit-ew-cell-content [me]             │
       │                                         │
       ├── conj:categorical-higgs-mechanism      │
       │       ├── conj:linking-operation        │
       │       └── conj:weinberg-angle-          │
       │             categorical                 │
       │                                         │
       ├── conj:weak-spectral-completeness ◄─────┤
       │                                         │
       └── prop:knot-operator-lp-selection ◄─────┤
                              │                  │
                              ▼                  ▼
                          N_v derivation (constrained PSLQ)
                                       │
                                       ▼
                          Closes:  G_F decomposition
                                   β-decay half-lives
                                   ⁴He +5.87% hard floor
```

## 5. Sibling-PR coordination plan

| PR | Action |
|----|--------|
| **#534** (`claude/categorical-mass-divergence-audit`) | Cross-link cell-content `tr_pure` derivation; offer `wedderburn_pair_volumes.py` for the LP/SDP duals on the EW sector; ask for `prop:rho-k-graded-expansion` integration into my term6 closed-form pipeline |
| **#546** (`claude/hoefsmit-2x2-fix`) | Ask for symbolic per-partition $\chi^\lambda$ at $\sigma_1^4 \sigma_3^6 \sigma_5^8$ on $V^{\otimes 6}$ — independent verification of cell-content multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ and the bar-self-dual closed form; offer my Lean class encoding for their $A^\lambda_{\mu\nu}(I)$ operator-valued form |
| **AXKIA** (merged) | $\alpha_{\rm EM}$ derivation pipeline is the template for $N_v$; nothing pending |

## 6. What this workplan does NOT do

Per the user's "no fitting" direction (turn 2026-05-05):

- **No more brute-force PSLQ over monomial bases** — fitting, not derivation.
- **No more Plancherel-weight ansatze** — degenerate special case of cell-content data.
- **No host-distinctness arithmetic for EW carriers** — superseded by Bring-internal embedding.
- **No promotion of A1-style PSLQ candidates** ($v_w/m_e \approx [4]_q^3 \cdot [6]_q \cdot [8]_q^4 \cdot q^{-17}$) without categorical justification of their exponents.

The N_v derivation route is now strictly through categorical authoring (Tier A + B), with PSLQ as a uniqueness witness only after the basis is structurally constrained.

## 7. Estimated path to 1-ppb closure

| Tier | Items | Effort | Blocker |
|------|-------|--------|---------|
| **A (3 conjectures)** | `linking-operation`, `weinberg-angle-categorical`, Hoefsmit assignment justification | Each is research-grade content authoring (1–3 weeks per conjecture) | Categorical Higgs mechanism content |
| **B (sibling integration)** | Pull `rho-k-graded-expansion`, `wedderburn_pair_volumes.py`; cross-validate Hoefsmit | Integration + validation, 1–2 weeks | Sibling PR merge timing |
| **C (PSLQ + closure)** | Re-run on cross-sector basis; close ⁴He | If Tiers A+B clean, days; else iterate | Bar-self-duality may force further structural authoring |

**Estimated total:** 4–10 weeks of authoring effort spread across tiers, with the major risk being whether the bar-self-duality + cross-sector basis converges on a clean $N_v$ closed form. If it does not, a **deeper categorical input** (e.g. cosmological boundary condition, motivic-Galois action) becomes required, pushing the timeline further.

## 8. Files

- This audit:
  [`docs/audits/2026-05-06-refocused-1ppb-workplan-v2.md`](2026-05-06-refocused-1ppb-workplan-v2.md)
- v1 predecessor:
  [`docs/audits/2026-05-05-refocused-1ppb-workplan.md`](2026-05-05-refocused-1ppb-workplan.md)
- Path-α-Bring audit:
  [`docs/audits/2026-05-05-path-alpha-bring-refinement.md`](2026-05-05-path-alpha-bring-refinement.md)
- $N_v$ impasse audit:
  [`docs/audits/2026-05-05-nv-categorical-impasse.md`](2026-05-05-nv-categorical-impasse.md)
- Sibling PRs:
  [#534](https://github.com/litlfred/qou/pull/534),
  [#546](https://github.com/litlfred/qou/pull/546)
