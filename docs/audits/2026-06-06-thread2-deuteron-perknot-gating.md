# Thread 2 — deuteron per-knot `Geom_full` is GATED (not clean engineering)

**Date:** 2026-06-06 · **Probe:** [`geom_full_deuteron_perknot_probe.py`](../../folio-assistant/computations/geom_full_deuteron_perknot_probe.py) · **Follows:** the next-threads handover (#1908) + the vol-usage audit (2026-06-02).

## Finding

The handover scoped the **deuteron** as thread 2's tractable first slice. Investigation
shows it is **research-gated + blocked by a production bug**, not a clean migration.
The proton/neutron cases remain the only cleanly-correct per-knot wiring (`Vol=8·G`).

### Three concrete obstacles

1. **The mass-`Vol(β_D)` is open (couples to thread 4).** `m(K)=m_e·[Vol(K)/ℏ_q²]·tr_M(K)`.
   The §9.3 "deuteron 6₂" assignment is **binding-context** (`B_D = m_e·Vol(6₂)·scale`,
   ~2 MeV). For the **mass**, `Vol(6₂)/Vol(𝓑₃) = 0.6006` (computed) — so using Vol(6₂)
   makes the deuteron **40 % lighter** than the uniform value (lighter than the proton),
   which is wrong **unless** `tr_M(β_D, H₆) ≈ 3.3 × tr_M(𝓑₃, H₃)`. Whether that holds is
   exactly the open §9.3 **link-volume assignment** (thread 4) — the deuteron mass-Vol is
   *not* cleanly `Vol(6₂)`.

2. **Production naming bug blocks the canonical trace.**
   `canonical_tr_m_via_chi_cache.canonical_tr_m("D", 1, 1)` constructs the cache name
   `chi-D-h6.witness.json`, but `per_irrep_pole_atom.py D` builds
   `chi-deuteron-h6-*.witness.json` (the "D" ↔ "deuteron" mapping is inconsistent). So the
   canonical H₆ trace can't be loaded by name. **Fix:** reconcile the atom-name → cache-name
   mapping (a one-line production fix, separable from the physics).

3. **The uniform baseline is itself a kludge.** `mass_table_comprehensive.py:104` tags the
   deuteron `"manual-historical-volume-match"` — so "uniform vs per-knot" has no clean
   uniform formula to diff against for D.

## Status of thread 2

- ✅ **p / n:** `Vol = 8·G = Vol(𝓑₃)` is **correct** (not part of the bug); the
  `geom_full_per_block_wiring.py` testbed verifies the per-block form for 𝓑₃.
- 🔴 **D and A≥3:** gated on (a) the §9.3 mass-link-volume assignment (**thread 4**),
  (b) the `chi-D-h6` naming fix, (c) resolving the historical-match kludge.

The probe is **ready** — once obstacles (a)+(b) clear, re-run
`geom_full_deuteron_perknot_probe.py` for the raw deuteron mass at the assigned Vol.

## Recommendation

Do **thread 4** (link-volume assignment) **before** thread 2's A≥2 mass wire-up; land the
`chi-D-h6` naming fix as an independent production cleanup. The handover's "deuteron
tractable" is corrected to "gated" by this note.

No fit; nothing wired; `c_3`/mass values cal-anchored.
