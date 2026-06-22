# q₀ cluster-A migration — analysis, proof, and batched plan (2026-06-21)

Execution of the cluster-A migration flagged in
[`2026-06-21-q0-hardcoded-constant-census.md`](2026-06-21-q0-hardcoded-constant-census.md).
**Batch 1 landed here; the bulk is sequenced below.** First, the analysis that
settles the migration direction — because the corpus was internally
contradictory about it.

## The direction is EMPIRICALLY settled: A (stale) → C (canonical)

The proton anchor is defined by `m_p/m_e = (2·(Vol(4₁)/ℏ_q²)·F_Bor(q) − 12)·habiro_ratio`
(`q_parameter._solve_q_proton` / `q_at`). Plugging in the two candidate q₀:

| q₀ | proton relation → m_p/m_e | vs CODATA `1836.15267343` |
|---|---|---|
| **C = `1.1099785955573347…`** (q_parameter.Q, "…955") | **1836.152673426** | ✅ matches to ~10 sig-figs |
| **A = `1.1099785827513808…`** (cluster-A, "…827") | 1836.153118 | ❌ off at the 7th sig-fig |

So **C is the canonical proton anchor** and **A is stale**. A is the
*pre-`habiro_ratio`* proton value (≈ #1422, 2026-05-29); the later habiro
refinement of the proton solve moved the anchor `…827 → …955`, and the
cluster-A files never updated.

## ⚠ `q0_consistency_audit.py` is itself STALE/INVERTED (prerequisite fix)

`computations/audits/q0_consistency_audit.py` predates the habiro refinement and
has the labels **backwards**:
- docstring: *"q₀ moved from the muon pin (1.10997859555…) to the proton pin (1.10997858275…)"*
- `OLD_Q0_PATTERNS = [re.compile(r"10997859555"), re.compile(r"859555")]` — i.e. it
  **flags the canonical C (…955) as the stale value**, and treats stale A (…827)
  as canonical.

Per the proof above this is inverted: the patterns should flag **`10997858275` /
`858275`** (A), not `…955`. **This must be corrected before any CI gate**, else
the migration's own (correct) output would be mis-flagged. *Not rewritten here* —
the audit also tracks "stale-q₀ tr_M leaf literals" (`1.0653062285…` etc.) whose
pre/post-habiro provenance needs owner review; a blind label-swap could mis-handle
those. Flagged for a dedicated, owner-reviewed fix.

## Scope (true size)

100 live (non-`_deprecated`) files hardcode an A-literal (`1.1099785827…` at
various precisions). Of these:
- **~50 are in `computations/qbeta/`** — the cluster under heavy concurrent
  sibling work (8+ active branches); migrating them now would collide.
- **~75 carry committed witnesses** — each needs regeneration (re-run the probe)
  and a per-file check that the ~1.2e-8 q₀ shift does **not** flip a recorded
  "near-match" conclusion.

This is therefore a **coordinated, batched** operation, not a single sweep (an
initial blind 100-file regex sweep was reverted for exactly this reason).

## Batch 1 (this PR) — 9 safe files

Migrated A→C (length-preserving) in the **no-witness, non-`qbeta/` files** — pure
`.py` value corrections, no witness churn, no conclusion-flip surface:

`definitive_q0_shift_for_mp.py`, `habiro/habiro_interpolate_cross_validator.py`,
`probe_q_beta_wenzl_projectors.py`, `probes/_gap_a4_qsafe.py`,
`probes/difference_knot_binding_probe.py`,
`probes/qbeta_c3_habiro_3rung_crossanchor_rigidity_probe.py`,
`probes/qbeta_habiro_cyclotomic_probe.py`, `probes/qbeta_root_of_unity_probe.py`,
`witness_polynomial.py`. All `py_compile`-clean.

## Recommended remaining batches (owner-sequenced)

1. **Fix `q0_consistency_audit.py`** (invert the patterns to flag `…827`; owner-review the tr_M-leaf logic) — prerequisite for any CI gate.
2. **Non-`qbeta/` witness-bearing files (~40):** migrate A→C, regenerate each witness, verify no conclusion flip (the cluster-D batch #2576 showed the ~1e-8 shift left all negative-result verdicts intact — likely holds, but check per-file).
3. **`qbeta/` files (~50):** migrate **after** the active qbeta swarm settles, to avoid collision; coordinate via the qbeta branches.
4. **Endgame:** route q₀ through `from q_parameter import Q` rather than re-hardcoding C, so a future re-pin can't re-stale these files (the CODATA-registry pattern).
