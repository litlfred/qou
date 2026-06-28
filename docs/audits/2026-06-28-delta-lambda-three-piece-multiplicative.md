# 2026-06-28 — Δ_λ three-piece test: the fibre kernel MODULATES the bulk (multiplicative), additive is refuted

**Branch:** `claude/delta-lambda-three-piece-test-2026-06-28`
**Goal:** Δ_λ binding-closure (Track-A / Option-E)
**Scope tag:** (a) scope-limited — fixes the *combination law* of two derived pieces + hands z2bn a concrete multiplicative target. **No 7th fit; no closure.**
**Producer:** [`computations/delta_lambda_three_piece_test.py`](../../computations/delta_lambda_three_piece_test.py)
**Witness:** `computations/delta-lambda-three-piece-test.witness.json`
**Builds on:** [`2026-06-28-delta-lambda-borromean-ascaling-diagnostic.md`](2026-06-28-delta-lambda-borromean-ascaling-diagnostic.md) (PR #3027, merged — the extensive-bulk + q-Askey synthesis).

## The lead

The merged A-scaling diagnostic decomposed Δ_λ closure into three pieces:
**extensive bulk** (A-linear `2·m_e·8G ≈ 7.49 MeV/nucleon`) + **fibre q-Askey
per-λ kernel** (z2bn `R(q,x)`) + liquid-drop surface/Coulomb. The obvious next
question — *how do the bulk and the kernel combine?* — has a sharp, fit-free
answer.

## Result

| iso | A | B_AME | bulk | net/target bulk | net/target (bulk+tower) | r = B_AME/bulk |
|-----|--:|------:|-----:|----------------:|------------------------:|---------------:|
| D   | 2 | 2.225 | 14.98 | 6.73 | 7.85 | **0.149** |
| ⁴He | 4 | 28.30 | 29.96 | 1.06 | 1.28 | 0.945 |
| ⁶Li | 6 | 32.00 | 44.93 | 1.40 | 1.73 | 0.712 |
| ¹²C | 12 | 92.16 | 89.87 | 0.98 | 1.33 | 1.026 |
| ¹⁶O | 16 | 127.6 | 119.8 | 0.94 | 1.38 | 1.065 |
| ⁴⁰Ca | 40 | 342.1 | 299.6 | 0.88 | 1.88 | 1.142 |
| ⁵⁶Fe | 56 | 492.3 | 419.4 | 0.85 | 2.24 | 1.174 |

**1. Additive combination is REFUTED.** `B_bulk + B_tower` over-binds *every*
isotope (net/target 2.2–190×). The extensive bulk already carries the magnitude,
so adding the per-braid kernel **double-counts**. The three pieces are **not**
independent additive terms — a naive `bulk + kernel + surface` sum is the wrong
combination law.

**2. The kernel MODULATES the bulk (multiplicative).** The reshape target

$$ r(K) \;=\; \frac{B_{\mathrm{AME}}(K)}{B_{\mathrm{bulk}}(K)}, \qquad B_{\mathrm{bulk}} = A\cdot 2 m_e\,(8G) $$

runs **D 0.15 → A=4–16 ≈ 0.94–1.07 → heavy 1.17**. A per-λ kernel `R(q,x)` that
closes the A-scaling must reproduce this **multiplicative** `r(K)` on the
extensive bulk — `B(K) = B_bulk(K) · R_eff(K)` — not be an additive correction.

**3. The deuteron `r=0.15` is the under-saturation signature.** The extensive
bulk treats A=2 as two full shell-bound nucleons (`2·7.49 = 14.98 MeV`), but the
deuteron is a single loose bond (2.22 MeV) — so the kernel must *suppress* the
bulk by 6.7× at A=2. `r(K)` rising from 0.15 (D) through ~1 (the bulk-saturated
A=4–16 region) to 1.17 (heavy, where the bulk slightly under-binds) is the full
A-shape the kernel owes.

## Consequence for the lever map (handed to z2bn)

This sharpens the target for z2bn's `R(q,x)` fibre kernel: it must be a
**multiplicative modulation** `R_eff(K)` reproducing `r(K)` (the measured
D→mid→heavy profile above), **not** an additive `Σ_λ` term on top of the bulk —
the additive route double-counts and is refuted here. Concretely:

- the kernel must **suppress** the bulk hard at low A (D `r=0.15`, ⁶Li `0.71` —
  the under-saturated, surface-dominated light nuclei),
- pass through `~1` in the bulk-saturated `A=4–16` band, and
- **lift** slightly at heavy A (`1.17`), where the bulk under-binds — the regime
  the liquid-drop surface/Coulomb piece (the third element) refines.

## Closure check pre-wired — and R(q,x) has not landed

The direct test "R(q,x) vs r(K)" cannot run yet: the z2bn Lever-1 fibre kernel is
the **open keystone**. `z2bn_prolongation_qdifference_constraint.py` proves (b)
that the λ_SW prolongation must be q-difference (not classical jet); the
single-element / contiguity form is refuted (#3009, #2985); the core `R_m(q)` is
characterized (Stage 8) — but the explicit operator producing per-isotope binding
via `a_D^(n)=∮λ_SW^(n)` is flagged the open keystone (`mba-step09b`), with the
anchors `a_D^(2)=1`, `a_D^(3)=(q+1)²/(3q)`, `a_D^(4)=Family-A` still wired (a_D^(4)
a CODATA near-match). There is no per-isotope `R_eff(K)` to test, and nothing to
cherry-pick.

So [`delta_lambda_rK_closure_test.py`](../../computations/delta_lambda_rK_closure_test.py)
pre-wires the check: pass any candidate `R_eff(Z,N)` to `check()`; it reports
max/RMS deviation from r(K). The baseline `R_eff≡1` (extensive bulk alone) is
**max|Δ|=0.85, RMS=0.35** — the deuteron drives the gap (r=0.15 vs 1). **Bridge
spec for when R(q,x) lands:** `R(q,x) → a_D^(n)=∮λ_SW^(n) jet anchors →
per-isotope binding (mba-step09b) → R_eff(K)`, which must reproduce r(K).

## Scope guard

`r(K)` is a **measured residual target**, explicitly *not* a fitted kernel — per
the AGENTS.md Δ_λ gate, no 7th ansatz is proposed. This test establishes the
*combination law* (multiplicative, not additive) and the *target profile* a
derived kernel must hit; it does **not** derive the kernel or claim closure.
