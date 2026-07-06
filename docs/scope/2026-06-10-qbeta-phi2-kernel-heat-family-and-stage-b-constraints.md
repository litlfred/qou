# Φ₂ / kernel R scope addendum — heat-family gate verdict + Stage-B parity constraints

**Status:** scope addendum (constraint-record only — no probe beyond the two
already-landed tranches, no tier change, nothing wired).
**Owner direction:** 2026-06-10 session — queue items approved as "1 y / 2 y /
3 y" (merge #2090 synthesis; run Hoefsmit Stage B; update the kernel/Φ₂ scope).
**Parents:** [`2026-06-09-qbeta-phi2-watcher-post-alpha-eff-refutation.md`](2026-06-09-qbeta-phi2-watcher-post-alpha-eff-refutation.md)
(constraint-survival record) and
[`2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md)
(standing constraints 1–6).
**Disciplines:** *corpus-grep* (both parents read; no overlap — this doc only
appends), *coordinate* (new filename, no file overlap), *formalize-first*
(every new row below is a gate that prunes candidate kernels before any scan).

---

## 1. What changed on 2026-06-10

Two tranches landed:

1. **PR #2090 §3-bis (q-heat depth-1 backbone, Lean
   `QOU.BraidKnot.QBetaPreArchHeatDepthOneKernel`):** the corpus `exp_q`
   Jackson equation is an exact depth-1 q-difference kernel
   `exp_q(qx) = (1+(q−1)x)·exp_q(x)`; per-Peter–Weyl-mode q-heat kernels
   `R_λ(q,t) = 1−(q−1)·μ_λ(q)·t` with the content-Casimir spectrum
   `μ_λ = ℏ_q²·Σ_cells [c]_q[c+1]_q`; division-free two-mode depth-2
   composition. Entered as a **candidate FAMILY for `R`, ungated**.
2. **PR #2106 (Hoefsmit Stage B,
   [`qbeta_hoefsmit_stage_b_per_block_ck_probe.py`](../../folio-assistant/computations/qbeta/qbeta_hoefsmit_stage_b_per_block_ck_probe.py)):**
   per-block, per-level decomposition of the exact decay operator
   `ΔT = T_n − T_p` over the canonical normal forms, with the recombination
   gate `Σ_λ y_λ·χ^λ(w) = tr_M(w)` passing **symbolically** for all 6 H₃
   basis words, plus the heat-family gate-check.

## 2. Heat-family gate verdict (the §3-bis family, after #2106)

| candidate | gate (a₁ bar-ODD) | gate (|a₁| ≈ √2·Φ₂ ≈ 2.069) | verdict |
|---|---|---|---|
| per-mode `a₁ = −(q−1)·μ_λ(q)`, λ=(3) | **bar-MIXED** ✗ | 8.8×10⁻³ ✗ | **REFUTED as the direct a₁ source** |
| per-mode, λ=(2,1) | bar-MIXED ✗ | 2.2×10⁻³ ✗ | refuted as above |
| per-mode, λ=(1³) | bar-MIXED ✗ | 2.2×10⁻³ ✗ | refuted as above |
| two-mode depth-2 composition | t-dependent coefficients | not yet evaluated | **OPEN** — outside the constant-depth-2 class refuted by #1900; survives structurally, unforced |

Witness: [`qbeta-hoefsmit-stage-b-per-block-ck-probe.witness.json`](../../folio-assistant/computations/qbeta/qbeta-hoefsmit-stage-b-per-block-ck-probe.witness.json)
§`heat_trace_r_lambda_gate_check`.

**Read:** the heat family's *raw per-mode* kernels cannot supply `a₁ = √2·Φ₂`
— wrong parity AND three orders of magnitude small. Any surviving heat-route
must go through an **assembly** (the `Z_q` trace / multi-mode composition /
the f-map) that re-mixes parity and rescales. The family stays a candidate at
the assembled level only.

## 3. New constraints (append to the standing table as rows 7–9)

| # | Constraint | Provenance | Force on the kernel hunt |
|---|------------|-----------|--------------------------|
| 7 | **Level bar-parity ladder:** the Markov level components of `ΔT` alternate `L₀` bar-ODD, `L₁` bar-EVEN, `L₂` bar-ODD, `L₃` bar-MIXED (odd fraction ≈ 9.45 % at q₀) | #2106 witness §`level_bar_parity` (exact symbolic objects) | The f-map from operator levels to ladder rungs **must re-mix bar-parity**: the rung-3 source `a₁` is bar-ODD but the raw ℓ=3 level is 90.5 % bar-even. Kills any candidate that reads rungs directly off raw level components. |
| 8 | **Wedderburn trefoil selection:** the (2,1) block carries exactly 0 at the trefoil level ℓ=3 of `ΔT` | #2106 witness §`per_block_per_level_at_q0` (symbolic zero) | The deepest decay level lives entirely in (3) ⊕ (1³) — the kernel's rung-3 action factors through the 1-dimensional blocks. A candidate `R` whose rung-3 content needs the 2-dim standard block is refuted at H₃. |
| 9 | **H₃ level ceiling + scalar saturation (constructive):** H₃ NF words stop at length 3, and a single-reference scalar peel saturates after ĉ₃ (ĉ₄..ĉ₈ ≡ 0 to 65 dps at both anchors) | #2106 assertions `h3_level_structure_max_word_length`, `scalar_peel_saturates_after_first_free_rung` | `c₄..c₈` are reachable ONLY via H_{n≥4} towers or the kernel recursion — the kernel `R` is not just the cleanest route to `Φ₂`, it is the **only** route to the k ≥ 4 rungs that does not require building the A ≥ 4 canonical-word towers. Raises the kernel's priority relative to Stage-C tower work. |

Standing constraints 1–6 are untouched (see the 2026-06-09 survival record);
nothing here overturns any of them.

## 4. Open path (updated, keystone unchanged)

The single remaining keystone is still PR #1871's
`conj:qdifference-kernel-prolongation-symbol` → closed-form `R(q,ξ)` →
`a₁ = √2·Φ₂` → `Φ₂`. Today's additions change the *shape* of admissible
candidates, not the path:

- any candidate `R` must, after assembly through the f-map, produce a bar-ODD
  `a₁` from level data that is predominantly bar-even at ℓ=3 (row 7);
- its rung-3 content must factor through the 1-dim Wedderburn blocks (row 8);
- the heat family remains admissible **only at the assembled `Z_q` level**
  (§2) — the per-mode shortcut is closed.

## 5. Anti-pattern additions

- ❌ **Reading raw level components as rungs.** Row 7: the parities don't
  match; the f-map re-mixes. (This closes the most tempting "next probe".)
- ❌ **Re-running per-mode heat-family a₁ gates.** Done in #2106; refuted.
  The open heat question is the assembled composition only.
- ❌ **Tower-first detours for c₄..c₈.** Row 9 makes the trade explicit:
  towers are the *other* route, and they are A ≥ 4 compute-heavy. The kernel
  keystone stays first unless the owner re-prioritises.

## 6. Cross-references

- Stage-B probe + witness: PR #2106 (this branch)
- Heat backbone Lean + synthesis: PR #2090
  ([synthesis doc](../audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md) §3-bis, §6)
- Standing constraints: [`2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md)
- Survival record: [`2026-06-09-qbeta-phi2-watcher-post-alpha-eff-refutation.md`](2026-06-09-qbeta-phi2-watcher-post-alpha-eff-refutation.md)
- Preflight gates: [`2026-06-05-qbeta-formalize-first-gates-consolidation.md`](../audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md)
- Q_β master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
