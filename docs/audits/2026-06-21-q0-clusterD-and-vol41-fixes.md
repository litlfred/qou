# q₀ cluster-D + vol(4₁) precision fixes (2026-06-21)

Follow-up to the census [`2026-06-21-q0-hardcoded-constant-census.md`](2026-06-21-q0-hardcoded-constant-census.md)
(#2569). Applies the two **clear, isolated** corrections the census flagged;
the large cluster-A migration (61 files) remains owner-sequenced.

## 1. Cluster-D — wrong `Q_MUON_50` in 5 qbeta probes (FIXED)

`Q_MUON_50 = 1.10997868769193107842185960213` matched **no** canonical anchor
(off ~8e-8 at the 7th decimal). Corrected to the canonical muon anchor
`1.1099785955541805752815940796095093779932822799587`
(`m_μ/m_e = Vol(4₁)/ℏ_q²`, `ℏ_q = (q−1)/q`; matches the 6 cluster-B files):

- `qbeta/qbeta_chain4_demazure_fund_weights.py`
- `qbeta/qbeta_chain4_kashiwara_step4_n5.py`
- `qbeta/qbeta_chain4_mixed_wenzl_kashaev_kashiwara.py`
- `qbeta/qbeta_residue_followup_residual_2x.py`
- `qbeta/qbeta_residue_followup_sl6_demazure.py`

All five **use** `Q_MUON_50` (2–4 refs) and carry committed witnesses; all five
were re-run (exit 0) and their witnesses regenerated. **No verdict changed** —
every probe was already a negative result (NO near-match / NO closure / density-
not-structure), robust to the ~1e-7 q₀ correction. (`Q_PROTON_50` in these files
is the stale cluster-A value; left to the cluster-A sweep.)

## 2. vol(4₁) precision divergence (one FIXED, one flagged)

Canonical `Vol(4₁) = 2·Cl₂(π/3) = 2.0298832128193072500424051085490405718833786…`.

- **FIXED:** `probes/t6_tau_h5_embedding_probe.py:55` had
  `2.0298832128193072500115978…` — **wrong at the 16th sig-fig** (~1e-16,
  borderline for the 1ppQ goal). Corrected to canonical. (No committed witness;
  `.py`-only fix.)
- **Flagged, not changed:** `substrate/experimental_constants.py` carries a
  vol(4₁) literal correct to ~28 digits then divergent (~1e-28 — far below the
  1ppQ/1ppb floors, so harmless for every current goal). It is a core substrate
  file with wide blast radius; the right fix is to source vol(4₁) from
  `2*clsin(2,π/3)` / `q_parameter`, deferred to avoid churn. `_deprecated/`
  occurrences ignored.

## Net

Two isolated correctness fixes (a never-canonical q₀ in 5 probes; a 1e-16-wrong
vol in 1 probe), no production observable affected, no probe conclusion changed.
The systemic hardcode anti-pattern (route q₀/vol through `q_parameter`) remains
the owner-sequenced follow-up per the census.
