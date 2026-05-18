# m_p chain Items A/B/C — findings and next steps

**Date:** 2026-05-18
**Status:** Picks up PR #671's m_p chain closure gap analysis. PR #671
was closed without resolution; this audit summarises what PR #704's
probes found and proposes the next concrete steps.

## TL;DR

Three items were identified in PR #671 as the open R&D needed to close
the m_p chain (lift `m_p` from `derivation_pending` → `derived`). All
three have now been probed (PR #704):

| Item | Question | Probe | Finding |
|---|---|---|---|
| **A** | T2+T3 at A=1 — KeyError or structural emptiness? | `probe_proton_t2_t3_at_a1.py` | **KeyError was a consumer-side bug** (PR #684 fixed). T2+T3 ARE computable at A=1 under canonical Li_2^q. Proton: T1+T2+T3 = 4.34 (cat-units) → 2.22 MeV after m_e scaling, **99.76 % short of CODATA**. T2+T3 are structurally small at A=1. |
| **B** | What categorical object produces T5 = −7.79? | `probe_t5_chirality_categorical_audit.py` | **No simple categorical object on H_3 / V_(2,1) at q_0 matches T5 within 10 %.** Best candidate: `−[3]_q · [2]_q = −6.12` (21.4 % off). Supports PR #671 hypothesis #4: T5 is likely a **numerical artefact of double-counting** between T1+T2+T3 and the chirality channel. |
| **C** | T6 Habiro residue — convergent or truncated? | `probe_t6_habiro_residue_at_a1.py` | T6 at A=1 is small (~1 MeV) — ambiguous: convergent OR aggressively truncated. **T6 at A≥3 is wildly divergent**: A=3 gives −21,375 MeV, A=4 gives +692,957 MeV (vs ~2.8 GeV nucleon scale). Current cyclotomic truncation depth is too small for higher-A atoms. |

## Bottom-line workplan implication

**Item B is the dominant gap.** T5 = −7.79 dwarfs the entire T1+T2+T3 contribution (which sums to ~4.3 at A=1). With T5 included, the tower swings WAY below CODATA. With T5 dropped (or recognised as double-counting), the chain still has a 99% gap — meaning the bulk of m_p/m_e ~ 1836 must come from somewhere ELSE in the tower assembly.

The realistic closure path is **not** T1+T2+T3+T4+T5 alone, but **structural inputs from elsewhere** (e.g. the C2 inflection result, which gives m_p_pred = 938.92 MeV to 0.07 % from a completely different substrate route). PR #690 wires this into `atomic_mass_via_rho_k` already.

## Recommended sequence

### Phase 1 — confirm the double-counting hypothesis (Item B follow-up)

The `probe_t5_chirality_categorical_audit` finding (no categorical match within 10 %) supports but does not PROVE the double-counting hypothesis. A confirming probe would:

1. Read T1+T2+T3's per-generator structure from `terms-2-3-atom-per-gen-mpfr-50dps`.
2. Read T5's per-partition breakdown from `term5-v2-chirality` (if available) or compute via `term5_v2_chirality.aK_v2_full(Z, N)`.
3. Identify the overlapping Wedderburn blocks (BOTH paths sum over partitions λ ⊢ 3).
4. Compute the candidate over-counted contribution (= the term that appears in both).
5. Verify: T5 minus the over-count should approach a clean categorical value (e.g. small or zero).

If confirmed, the resolution is:
- Option A: **drop T5** from the tower assembly (cleanest).
- Option B: **subtract the identified over-count** from T5 (preserves T5 as a real contribution with adjusted value).

### Phase 2 — recognise that T1-T6 tower at A=1 will NOT close to m_p/m_e ~ 1836

The probes show T1+T2+T3 ~ 4 (cat-units) at A=1. Even with T4 (Frobenius) and a corrected T5, the sum is unlikely to reach 1836. The closure path through the tower alone is **structurally incomplete** at A=1.

The substrate-pure m_p closure is **available via a different route** (C2 inflection, 0.07 % residual). This is the path PR #690 takes. Wiring this into `low_isotope_mass_table.py` would lift ¹H from `derivation_pending` → `derived` without needing to close the T1-T6 tower at A=1.

### Phase 3 — Item C residue-depth sweep (deferred)

T6 at A≥3 is dramatically divergent (A=4 = 692,957 MeV). Either:
- The cyclotomic residue truncation depth `k` in `term6_residues_at_roots.py` needs to scale with A (currently fixed-k).
- Or T6 is fundamentally not a small correction at higher A — its role in the tower assembly needs revisiting.

Either way, this matters only after Item B is resolved, since T5 = −7.79 swings the proton answer by ~order-of-magnitude relative to T6 ≈ 1 MeV at A=1.

## Cross-references

- [PR #671](https://github.com/litlfred/qou/pull/671) — original gap analysis (closed without resolution)
- [PR #684](https://github.com/litlfred/qou/pull/684) — Item A consumer fix (KeyError unblocked; closed without merging)
- [PR #690](https://github.com/litlfred/qou/pull/690) — substrate m_p/m_n as production default (alternative closure route)
- [PR #704](https://github.com/litlfred/qou/pull/704) — Items A/B/C probes (this audit's basis)
- [`docs/audits/2026-05-17-m-p-chain-closure-gap-analysis.md`](2026-05-17-m-p-chain-closure-gap-analysis.md) — PR #671's original analysis

## Witness artefacts

- `probe-proton-t2-t3-at-a1.witness.json`
- `probe-t5-chirality-categorical-audit.witness.json`
- `probe-t6-habiro-residue-at-a1.witness.json`

## CAL discipline

All three probes are CAL-clean: m_e (CAL-1) is the only mass input;
CODATA m_p / m_n / m_D / m_T appear only as VALIDATION targets via
`codata_constants.M_*_MEV_VALIDATION` aliases, never as prediction
inputs. The structural findings depend only on q_0 (CAL-2) and the
Hecke / Wedderburn data at H_3.
