# q₀ hardcoded-constant inconsistency census (2026-06-21)

**Status:** audit — source-code census. Complements the existing witness-side
audit [`2026-05-30-q0-repin-stale-witness-audit.md`](2026-05-30-q0-repin-stale-witness-audit.md)
(which covered `*.witness.json`); this one covers the **Python source** surface
— the hardcoded `q₀` decimal literals across `computations/`. No code changed
here (mass q₀ edits churn every witness and collide with concurrent work); this
documents the inconsistency and the canonical fix path.

## Single source of truth

`computations/substrate/q_parameter.py` →
`Q = Q_50_DIGIT_STR = 1.1099785955573347198997632204832250266562084087802`
(the 2026-05-28 **proton-anchor** re-pin; `m_μ/m_e` is now a prediction).
Any script needing q₀ should `from q_parameter import Q` (or `Q_50_DIGIT_STR`),
**not** hardcode a decimal — exactly the discipline the CODATA-registry routing
(`codata_constants`) applies to masses.

## Census — 77 live (non-`_deprecated`) files hardcode a long q₀ decimal

| Cluster | Value (head) | Live files | Classification |
|---|---|--:|---|
| **C** | `1.1099785955573347…` | **3** | ✅ **canonical** (= `q_parameter.Q`, proton re-pin) |
| **A** | `1.1099785827513808…` | **61** | ⚠️ **stale** — pre-re-pin; differs from C at the **8th** sig-fig (~1.2e-8) |
| **B** | `1.1099785955541805…` | **6** | ◑ **muon anchor** (`m_μ/m_e = Vol(4₁)/ℏ_q²`); legit only in the canonical-CAL-2 layer, differs from C at the **12th** sig-fig (the μ–p tension ~2.9e-10) |
| **D** | `1.1099786876919310…` | **5** | ❌ **wrong** — matches **no** recognized anchor; diverges at the **7th** decimal (~8e-8) |

Only **3 / 77** files use the canonical value; **61** carry the stale
pre-re-pin q₀.

### Verification of the anchors
- Canonical proton C is read directly from `q_parameter.Q`.
- Muon anchor B re-derived here: `m_μ/m_e = 206.7682830`,
  `Vol(4₁) = 2·Cl₂(π/3) = 6·Λ(π/3) = 2.029883212819307…` (Clausen `Cl₂`,
  = `clsin(2,·)` in the code; Lobachevsky `Λ(θ) = ½·Cl₂(2θ)`), `ℏ_q = (q−1)/q` ⇒
  `q = 1.10997859555418057528159407961` — matches cluster B's 6 files to ~28
  digits. (B and C agree to 11 sig figs then split at the μ–p tension.)
- A (`1.10997858275138…`) matches neither the current proton nor the current
  muon derivation; it is the dominant **stale** hardcode (provenance: a
  pre-re-pin / pre-refinement value — owner to confirm).

## The novel finding — cluster D is a genuine bug

`Q_MUON_50 = mp.mpf("1.10997868769193107842185960213")` in **5 `qbeta/` files**:

- `qbeta/qbeta_chain4_demazure_fund_weights.py:54`
- `qbeta/qbeta_chain4_kashiwara_step4_n5.py:46`
- `qbeta/qbeta_chain4_mixed_wenzl_kashaev_kashiwara.py:70`
- `qbeta/qbeta_residue_followup_residual_2x.py:39`
- `qbeta/qbeta_residue_followup_sl6_demazure.py:45`

It is **labeled the muon anchor** but equals neither the muon value
(`1.10997859555418…`, cluster B) nor anything else canonical — it is off by
~8e-8 at the 7th decimal. In the same files `Q_PROTON_50 = 1.10997858275138…`
is the **stale** cluster-A value (not the current proton C). So **both** q₀
constants in these 5 exploratory probes are off from canonical; any numeric
result they produce inherits an ~1e-7 q₀ error. (These are EXPLORATORY probes,
not production — no production observable is affected.)

## Recommended fix path (not applied here)

1. **Priority — cluster D (5 files):** correct `Q_MUON_50` to the real muon
   anchor `1.10997859555418057528159407961`, or better, route both constants
   through `q_parameter` (`Q` for proton, a `Q_MUON` accessor for muon). These
   are the only files using a value that was *never* canonical.
2. **Cluster A (61 files):** the bulk stale-q₀ surface. Migrate to
   `from q_parameter import Q` in a dedicated sweep (mirrors the CODATA routing),
   **with witness regeneration**, coordinated to avoid the concurrent
   binding/qbeta work. This is the large, witness-churning piece — owner-gated
   sequencing.
3. **Cluster B (6 files):** confirm each is intentionally in the canonical-CAL-2
   (muon) layer; if so, route to a named `Q_MUON` accessor so the two-layer
   intent is explicit rather than a bare decimal.

## Caveats (critical-distance)

- The **two-layer convention** (CLAUDE.md): the muon-anchor q₀ (B) is the
  canonical *mathematical* CAL-2 value; the proton-anchor (C) is the
  Physical-Observations re-pin. So B is not "wrong" in CAL-2 contexts — but it
  must be the *correct* muon value (`…955541805`), which D is not.
- Mass-editing 77 files is **out of scope here** and is the known
  q₀-repin-staleness class — it requires coordinated witness regeneration. This
  audit's actionable, low-risk recommendation is the **cluster-D correction**;
  the cluster-A migration is a separate, owner-sequenced sweep.
