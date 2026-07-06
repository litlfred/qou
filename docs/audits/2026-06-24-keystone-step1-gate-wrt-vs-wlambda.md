# Keystone Step-1 gate (run): the SU(2)/WRT(S³/2I) modular data does NOT reproduce the full `W_λ` family — full-Hecke arena forced

**Date:** 2026-06-24
**Branch:** `claude/keystone-step1-gate-wrt-vs-wlambda-2026-06-24`
**Status:** the DG attack plan's ([#2503](https://github.com/litlfred/qou/pull/2503)) "Step-1 gate" — *does the WRT(S³/2I) per-block weight equal `W_λ` at q₀ for n = 3,4,5?* — **run systematically** (it had only been spot-checked at n=5 in [#2608](https://github.com/litlfred/qou/pull/2608)). EXPLORATORY, **zero free parameters**, no production rewire. Inside the 2026-06-19 narrow owner-reversal scope (keystone geometric `W_λ`); the no-fit / no-7th-ansatz rule is respected.
**Script:** [`keystone_step1_gate_wrt_vs_wlambda.py`](scripts/keystone_step1_gate_wrt_vs_wlambda.py) · **Witness:** [`keystone-step1-gate-wrt-vs-wlambda.witness.json`](../../computations/keystone-step1-gate-wrt-vs-wlambda.witness.json)

## What was tested (and the trap avoided)

`W_λ = d_q(λ)²/[n]_q!` (the Ocneanu / q-Plancherel weight) lives on the **Hecke `S_n` side**: its numerator is the `S_n` q-dimension `d_q(λ)` (q-hook-length formula). WRT(S³/2I) is a Chern–Simons / RT invariant whose colour data is the **SU(2)-side modular data**: a block `λ ⊢ n` with **≤ 2 rows** corresponds (classical Schur–Weyl `(ℂ²)^{⊗n} = ⊕_{λ:≤2 row} S^λ ⊗ V_λ`) to the SU(2) irrep of spin `j = (λ₁−λ₂)/2`, balanced q-dimension `[2j+1]_q = [λ₁−λ₂+1]_q`.

The **#2608 category-error trap** is to compare a normalized weight `W_λ` to a quantum dimension. The gate avoids it by comparing the **two q-dimensions** of the *same* block: `d_q(λ)` (S_n side, the `W_λ` numerator) vs `[2j+1]_q` (SU(2) side, the WRT datum). Two independent ways the SU(2)/WRT route can fail:

- **(COVERAGE)** `≥3`-row blocks lie outside the GL₂(=spinor ℂ²) Schur–Weyl image — the SU(2) side assigns them **no weight at all**;
- **(VALUE)** even on `≤2`-row blocks, `[2j+1]_q` can differ from `d_q(λ)`.

## Result (q₀ ≈ 1.10998, 50 dps)

| n | block λ | rows | `d_q(λ)` (S_n) | `[2j+1]_q` (SU(2)) | equal? |
|---|---------|:----:|---------------:|-------------------:|:------:|
| 3 | (2,1) | 2 | 2.0108969 | 2.0108969 | **YES** |
| 3 | (3),(1,1,1) | 1,3 | 1.0 | 4.1097 / — | no / — |
| 4 | (3,1) | 2 | 3.0437062 | 3.0437062 | **YES** |
| 4 | (2,2) | 2 | 2.0437062 | 1.0 | no |
| 4 | (4);(2,1,1),(1⁴) | 1;3,4 | 1.0;3.04,1.0 | 5.22; —,— | no;— |
| 5 | (4,1) | 2 | 4.1096824 | 4.1096824 | **YES** |
| 5 | (3,2) — muon | 2 | 5.2204413 | 2.0108969 | no |
| 5 | (5) | 1 | 1.0 | 6.3881 | no |
| 5 | (3,1,1) — **electron** | 3 | 6.2204413 | — (≥3 row) | — |
| 5 | (2,2,1),(2,1,1,1),(1⁵) | 3,4,5 | 5.22,4.11,1.0 | — | — |

Totals across n=3,4,5: **7 blocks** sit at `≥3` rows (no SU(2) weight); of the **8** `≤2`-row blocks, only **3** satisfy `d_q = [2j+1]_q`.

`Z(n) = Σ_λ d_q²/[n]_q!`: `Z(3)=0.98744`, `Z(4)=0.98217`, **`Z(5)=0.98222`** (reproduces the prior audit's value — cross-check). `d_q` is conjugation-symmetric (`d_q(3,2)=d_q(2,2,1)=5.2204`, etc.), confirming `W_λ = W_{λ'}`.

## The sharper structural finding (not just the #2608 spot-check)

The three value-matches are **not** an accident at `(4,1)`. They are the **standard-representation family `(n−1,1)`** for *every* `n`:

> `d_q(n−1,1) = [n]_q! / ([n]_q · [n−2]_q! · [1]_q) = [n−1]_q = [2j+1]_q` (spin `j=(n−2)/2`).

So the SU(2)-side q-dimension equals the `S_n`-side q-dimension **exactly on the standard rep `(n−1,1)`, and there only** (the trivial `(n)` gives `d_q=1≠[n+1−... ]_q`; `(2,2)` gives `2.04≠1`; the muon `(3,2)` gives `5.22≠2.01`). #2608's single-point "(4,1) coincidence" is the `n=5` instance of this `(n−1,1)` identity. This is a structural observation (both sides `=[n−1]_q`), not a numerical near-match — **no fit**.

## Verdict — (b) structural exclusion of the *SU(2)-side* route (the full-Hecke object stays open)

The naive **SU(2)/WRT(S³/2I) modular data cannot be the geometric origin of the full `W_λ` family**, on two structural grounds (both justified by a proved invariant, so this is a legitimate **(b) structural exclusion** per the refutation-scope discipline — *of the SU(2) route specifically*, not of the geometric programme):

1. **Coverage (the load-bearing one).** The GL₂ Schur–Weyl image is exactly the `≤2`-row partitions (proved invariant: `(ℂ^d)^{⊗n} = ⊕_{λ:≤d row} S^λ ⊗ V_λ^{GL_d}`). The lepton generation blocks include the **3-row electron `(3,1,1)`**, which therefore has **no SU(2) weight**. This is the rigorous form of the ledger's ✅-forced "spinor ℂ² kills the electron (3,1,1)" (#2406) and of #2608's higher-colour foreclosure.
2. **Value.** On the `≤2`-row blocks the SU(2) q-dim matches `d_q` only on the standard rep `(n−1,1)`; elsewhere they differ (Schur–Weyl duality, #2608).

**Therefore the geometric `W_λ` index must live on the full-Hecke (`S_n`, `d→∞` / principal-specialization) side**, not the SU(2)/WRT(S³/2I) modular data — confirming and *sharpening* #2406/#2608. The genuinely-open object is unchanged: whether an `S¹`-equivariant index on the **corrected full-Hecke arena** reproduces `W_λ` (multi-session DG; not in-session tractable). This gate **prunes** the SU(2)-side sub-route cleanly so that work is not wasted there.

## Normalization (the owner's question — *can the per-block `W_λ` ambiguity be fixed?*)

`W_λ = d_q²/[n]_q!` and the Plancherel-probability `d_q²/D²` (`D² = Σ_μ d_q²`) differ by the **global, λ-independent** factor `D²/[n]_q! = Z(n)`. Hence:

- **Per-block ratios within fixed `n` are normalization-invariant** (the factor cancels) — so the lepton mass *ratio* (electron/muon, both `⊢5`) does **not** depend on the fork. The `W_l/[n]!` and `W_l/D²` columns in the witness are proportional within each `n`.
- Only the **total `Z(n)`** is normalization-sensitive: `d_q²/D²` forces `Σ=1` (true probability measure), while `d_q²/[n]_q!` gives `Σ = Z(n) < 1`, whose **defect `1−Z(n)`** is the physical, falsifiable content (closed form `144·C(n) = −n(n−1)(2n−13)`, the `n=7` sign flip; #2620/#2527-era).

So the ambiguity is "fixed" by recognizing that the **defect `1−Z(n)` — not the absolute per-block value — is the invariant the geometric index must reproduce.** It is not a free parameter (no fit): `Z(n)` is computed.

## Discipline

No fit; `q₀` enters only as the evaluation point (never tuned). The `2I → E₈ → Lawrence–Zagier` correspondence chain is not invoked (pure balanced-q-integer arithmetic). (b)-exclusion cites the Schur–Weyl image invariant; the full-Hecke geometric object is **not** excluded (it is the open frontier). Corpus-grep: this *runs* the #2503 gate and *sharpens* #2406/#2608; it does not re-derive the refuted resonance / projector-shift / compact-Sasakian routes.

## Cross-references

- [#2503](https://github.com/litlfred/qou/pull/2503) — the DG attack plan whose Step-1 gate this executes.
- [#2608](https://github.com/litlfred/qou/pull/2608) — Schur–Weyl dual-sides (WRT SU(2) ≠ `W_λ` S_n); this gate sharpens its `(4,1)` spot-check to the `(n−1,1)` family.
- [#2524](https://github.com/litlfred/qou/pull/2524) — Beasley–Witten Seifert–CS mechanism (`d_q²/D²` normalization).
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger.
- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — the `144·C(n)` defect closed form.
