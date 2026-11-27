# m_K/m_π: the (3,4) pair and the EM addend stay **Selected** (compute-accuracy C5)

**Date:** 2026-11-27 · **Branch:** `claude/mk-mpi-status-2026-11-27` · **Beans:** `qou-mk34`, `qou-mkem`
(epic `qou-myts`, parent `qou-3l2l`) · **Builds on, does not re-derive:**
[`2026-11-20-mk-mpi-derivation-status.md`](2026-11-20-mk-mpi-derivation-status.md),
[`2026-11-24-mK-mpi-post-9360-derivation-adjudication.md`](2026-11-24-mK-mpi-post-9360-derivation-adjudication.md),
[`2026-08-22-mK-mpi-l2-red-team.md`](2026-08-22-mK-mpi-l2-red-team.md).

## Verdict (label for the scorecard status column)

**m_K/m_π = Selected.** Two choices remain premises, not consequences of the meson braid words:

1. **The pair (3,4)** in the strong core `m_K²/m_π² = [3]_q[4]_q`. Not derived.
2. **The EM addend** `(α_em/π)·(1+log(1+ℏ_q))`: its scale and its UV endpoint are chosen.
   (α_em itself is not the blocker: the 2026-11-24 Lipschitz bound shows every sorry-free α_em arm
   moves the row by at most 0.048 ppb.)

No number changes. The total (+51.48 ppb) and the core alone (−101,553 ppb) are as recorded on 2026-11-20.

## What is new in this PR: the formal statement of why the selection cannot be removed

Lean: `folio/quantum-observable-universe/lean/QOU/EightfoldWay/MesonRatioSelectionStatus.lean`
(generic `Field K`, §7c, no ℝ, no measured constant). `lean -DautoImplicit=false` exit 0; `#print axioms`
on all four theorems: `[propext, Classical.choice, Quot.sound]` or less, no `sorryAx`. Wired into `QOU.lean`.

| declaration | statement |
|---|---|
| `p34_eval_one`, `p34_eval_eq_qInt` | `p34 = (q⁴+q²+1)(q⁶+q⁴+q²+1) = q⁵[3]_q[4]_q`, and `p34(1) = 12` |
| `clasp_reading_pion_eq_kaon` | in **any** monoid with involutive generators (the `q = 1` image `H₃(1)`), **every** function takes the same value on the pion clasp word `s₁³s₂³s₁s₂` and the kaon clasp word `s₁³s₂⁵s₁s₂` |
| `unit_ratio_reading_ne_p34` | if `N, D ∈ K[q]` with `N(1) = D(1) ≠ 0`, then `q⁵N ≠ p34·D`: no such ratio equals `[3]_q[4]_q` as an identity in `q` (uses only `11 ≠ 0` in `K`) |
| `claspHecke21_trace_ratio_ne_qInt34_at_one` | the concrete case: the `S^{(2,1)}` traces of the kaon and pion clasps are not in ratio `[3]_1[4]_1 = 12` |

**Scope, stated as (b) with its invariant.** Excluded: every reading of `m_K²/m_π²` as a ratio of values of the
gluon-clasp meson words that is polynomial in `q` and specializes at `q = 1` through `H₃(1)`. The invariant is the
`q = 1` collapse of the odd clasp words (`involutive_odd_clasp_eq_sq`) against `[3]_1[4]_1 = 12 ≠ 1`.
**Not excluded:** a reading that picks a channel, e.g. `dim_q(V₂ ⊗ Sym²_q W₃*) = [3]_q[4]_q`
(`MesonThreeByFourCharacterization.splitBundle_sym2_w3_tensor_v2_eq_3x4`). That reading is consistent; choosing that
channel for the kaon/pion ratio is the premise. Likewise the "minimal among factorizations of 12" ordering
(`twelve_factorizations_strict_ordering_real`) ranks pairs once the integer 12 is given, and no corpus meson object
supplies 12 (pion total 6, kaon total 8, constituents (3,3) and (3,5); `scanPair_four_not_dictionary_index`).

## Bookkeeping found on the way

`MesonThreeByFourCharacterization.lean` (the 2026-11-24 formalization) was not reachable from the `QOU.lean` root.
It checks (`scripts/lean-verify.sh`, exit 0, measured this session) and is now in the root's import cone through the
new file. `MesonKaonPionSchwingerBridge.lean` is still not wired; not touched here.

## What would move the label

- **(3,4) → Derived:** a definition of K and π (Hecke/Wedderburn objects, strands and quark content) from which the
  `V₂ ⊗ Sym²_q W₃*` channel, or `[3]_q[4]_q` directly, follows without reference to the measured ratio. Bean `qou-mk34`.
- **EM addend → Derived:** a worldline boundary argument fixing the UV endpoint (`1+ℏ_q` vs `q`) and the scale
  `(α/π)·m_π²`, and saying which object the term is (it is not the Dashen leading EM shift, which lowers the ratio).
  Bean `qou-mkem`.
