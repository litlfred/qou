> **DEPRECATED on 2026-05-24.** Undated audit document classified as workplan / status snapshot / migration-handoff / one-off investigation whose findings have been integrated into main or whose plan has been executed. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T5 for the deprecation rationale.

# ³H structural investigation — α\* = 0.424 anomaly

**Source data.** `computations/joint-tower-sdp-rust.witness.json`,
`per_atom_certificates[name = "tritium-3H"]`. Methodology tag:
`manual-historical-volume-match` (the historical 8_11 ID flowed
through to a 14-letter braid word in B_5).

## Per-block PSD breakdown at q_0 = 1.10998

³H lives in H_5 with native strand count `n_0 = 5`. The 7 Wedderburn
blocks of H_5 split as:

| λ | d_λ | min eig of ρ_λ(T_w) | PSD? |
|---|---|---|---|
| (5)         | 1 |  +0.6594 | ✓ |
| (4, 1)      | 4 |  **−1.0316** | ✗ |
| (3, 2)      | 5 |  **−0.8320** | ✗ |
| (3, 1, 1)   | 6 |  **−1.1841** | ✗ |
| (2, 2, 1)   | 5 |  **−1.3577** | ✗ |
| (2, 1, 1, 1)| 4 |  **−1.3228** | ✗ |
| (1, 1, 1, 1, 1) | 1 |  +1.5164 | ✓ |

α\* = 0.4241; gap = 0.5759.

**Pattern — exactly the 1-dimensional blocks pass.** All five
multi-dimensional blocks (d_λ ≥ 4) fail with negative min
eigenvalues of order O(1). The two passing blocks are the trivial
(5) and sign (1,1,1,1,1) representations — both 1d and structurally
forced to be PSD whenever the trace and antitrace of T_w are
non-negative.

The eigenvalues are not numerically tiny, so this is **not** a
precision issue. The historical 8_11 ID + 14-letter braid word
`[-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2]` produces a
Hecke element whose multi-dimensional Wedderburn projections are
genuinely indefinite at q_0.

## Three hypotheses

**H1 — wrong historical knot ID.** 8_11 may simply not be the
correct ³H knot. The α\* = 1 entries (proton, neutron, ³He) all
agree with their historical IDs; the α\* < 1 entries (²H, ³H) do
not. ²H is α\* = 0.546 with `markov_trace = 0` reported in
[`atom-nf-symbolic-D.witness.json`](../../computations/atom-nf-symbolic-D.witness.json),
which is also strongly suggestive that 6_2 is wrong for ²H.

**H2 — sign-convention bug at d_λ ≥ 4.** The 1d blocks pass and
the multi-d blocks all fail with similar-magnitude negative
eigenvalues. If the Hoefsmit seminormal projection at d_λ ≥ 4 has
a sign error, the failure pattern is exactly this. The fix is in
[`tools/hecke-engine/src/seminormal.rs`](../../tools/hecke-engine/src/seminormal.rs)
or [`seminormal_mn.rs`](../../tools/hecke-engine/src/seminormal_mn.rs).
Spot-check: re-evaluate ρ_(4,1)(σ_1) at q_0 against the published
Hoefsmit table (Hoefsmit's thesis §3.4) at d=4.

**H3 — Markov-stabilization sign error.** The 14-letter word
contains `…4, … −4 …` — Markov stabilization from H_4 to H_5. The
canonical Markov-stabilization rule is
`tr_M(x · σ_{n−2}) = z · tr_M(x)` with z = 1/(q^{1/2} + q^{-1/2}).
A sign-flip on z (or on the sigma_{n-2} insertion) would leave
the 1d blocks invariant (their eigenvalues only depend on the
trace and antitrace) and flip the multi-d block eigenvalues.

**Discriminating between H2 and H3:** apply the same evaluator to
proton (also B_3, but α\* = 1). If proton's multi-d block at λ=(2,1)
remains PSD, then the bug is specific to the H_5 Markov-stabilization
path (H3). If proton has the same artefact, the bug is in
seminormal projection (H2).

**Discriminating from H1:** if either H2 or H3 produces a fix that
makes ³H/8_11 also become α\* = 1 with B_pred close to B_AME =
8.4818 MeV, then 8_11 is the right ID and there was a code bug.
If the fix moves α\* up but B_pred away from B_AME, then 8_11 is
wrong (H1).

## Concrete next steps

1. **Spot-check Hoefsmit ρ_λ(σ_i) at d_λ = 4** against
   `tools/hecke-engine/src/hoefsmit_witness.py` output and the
   published Hoefsmit table. If a sign discrepancy at d ≥ 4
   appears, fix in `seminormal.rs` and re-run.
2. **Test the proton Borromean braid through the same evaluator**
   at H_5 (extend by Markov stabilization). If proton remains PSD,
   the H_5-specific Markov-stabilization sign convention is the
   bug (H3). If proton's d_λ = 4 block fails, it's H2.
3. **If H2/H3 fixes don't restore α\*, search alternative knot IDs
   for ³H** — start with 8_5, 8_6, 8_7 (other 8-crossing knots
   with similar volumes), and 9_2, 9_3 (9-crossing). Re-run the
   joint-tower SDP for each candidate, pick the one with the
   highest α\* and best B_pred fit.
4. **Re-emit the witness** with whichever fix lands and update
   `prop:atom-knot-mass-derivation`'s α\* table accordingly.

## Effort estimate

- Step 1 (Hoefsmit spot-check): 1–2 hours, no infrastructure
  changes.
- Step 2 (proton at H_5): 2–3 hours, requires running the existing
  binary on a modified input.
- Step 3 (alternative knot ID search): 1–2 days, requires R5-full
  SDP-as-solver to derive canonical T_w for each candidate without
  AME anchoring (otherwise the search is circular).
- Step 4 (witness re-emit + α\* table update): 1 hour.

If H2 or H3 lands, total residual reduction on ³H is open — could
be the full 4.7 ppm → sub-1 ppb if the fix produces the genuine
canonical T_w, or a smaller reduction if 8_11 is structurally
wrong but close to the truth.
