# Thread 2 — deuteron per-knot `VolDensity` is GATED (not clean engineering)

**Date:** 2026-06-06 · **Probe:** [`vol_density_deuteron_perknot_probe.py`](../../computations/vol_density_deuteron_perknot_probe.py) · **Follows:** the next-threads handover (#1908) + the vol-usage audit (2026-06-02).

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
  `vol_density_per_block_wiring.py` testbed verifies the per-block form for 𝓑₃.
- 🔴 **D and A≥3:** gated on (a) the §9.3 mass-link-volume assignment (**thread 4**),
  (b) the `chi-D-h6` naming fix, (c) resolving the historical-match kludge.

The probe is **ready** — once obstacles (a)+(b) clear, re-run
`vol_density_deuteron_perknot_probe.py` for the raw deuteron mass at the assigned Vol.

## Recommendation

Do **thread 4** (link-volume assignment) **before** thread 2's A≥2 mass wire-up; land the
`chi-D-h6` naming fix as an independent production cleanup. The handover's "deuteron
tractable" is corrected to "gated" by this note.

No fit; nothing wired; `c_3`/mass values cal-anchored.

---

## Update 2026-06-06 — obstacle (b) cleared; canonical `tr_M(D)` now computes + cross-checked

Obstacle **(b)** (the `chi-D-h6` naming bug) is **fixed**, and a second bug it
masked is fixed too:

1. **Alias normalization.** `canonical_tr_m()` now maps short aliases through
   `ATOM_ALIASES` (`"D"→"deuteron"`, idempotent on canonical names) before the
   chi-cache lookup, so `canonical_tr_m("D", 1, 1)` finds
   `chi-deuteron-h6-at-q0-50dps.witness.json`.
2. **Numerical fast-path schema bug (newly found).** The fast-path assumed a
   *pre-summed* cache (`y_lambda` / `contribution` / `tr_M_at_q0` keys), but the
   producer `chi_at_q0_via_hoefsmit_mpfr.py` writes **χ-only** caches → `KeyError`.
   The fast-path now combines the cached numerical χ^λ with `y_lambda_at`-computed
   `y_λ` and sums `Σ_λ y_λ·χ^λ` (the docstring recipe), matching the symbolic path's
   schema (and faster — no sympify).

**Result + cross-check (L1-grade):** `canonical_tr_m("D", 1, 1)` →
`|tr_M(β_D)| = 0.38828642407478887671153751312935209344259947275515…` at q₀
(numerical fast-path). Hiding the numerical cache to force the symbolic path gives
`…275513…` — the two agree to **50 dps** (rel diff 4.8e-50). So the canonical H₆
trace for the deuteron is now loadable *and* validated against the independent
symbolic combiner.

**Obstacle (a) sharpened — the `Vol(6₂)` discrepancy is a mislabel, not a 39 % physics gap.**
The `conj:canonical-knot-id-sdp` table pairs "6₂ (Miller's knot)" with `Vol = 3.16396`,
but `3.16396` is the SnapPy census volume of **6₁**; the **6₂** census volume is
`4.40083`, which is exactly the production `Vol_D` in
`per-atom-hyperbolic-volume.witness.json`. So production already uses `Vol(6₂)=4.40083`;
the conj `.md` table's *number* (3.16396) is stale/mislabeled (it is `Vol(6₁)`).
Reconciling the conj table — and deciding definitively whether the deuteron knot is `6₁`
or `6₂` — is **thread-4 / `conj:canonical-knot-id-sdp` scope** (knot identity from the SDP),
not a compute bug. Flagged for owner reconciliation.

**Still gated:** obstacle (c) — the per-knot mass demonstrator
(`per-knot-mass-table-demonstration.py`) computes **absolute masses**, not the deuteron
**binding** energy (it compares against the deuteron rest mass ≈1875 MeV, not B≈2.2246 MeV),
so the "+2.86 %→AME" binding delta is not directly emittable from it. Computing the binding
delta needs the binding pipeline (couples to thread 4's binding-K). With `tr_M(D)` now
available, that is the clean next step.

---

## Update 2026-06-12 — live SnapPy census verification: the fork is systematic (all 3 rows), orphan volumes identified

First in-sandbox SnapPy run (3.3.2 — every earlier audit was sandbox-blocked and relied
on literature/witness values). Script:
[`audits/snappy_census_volume_verification.py`](../../computations/audits/snappy_census_volume_verification.py),
witness `snappy-census-volume-verification.witness.json` (16/16 assertions), PR #2192.

1. **The historical-table mismatch is NOT deuteron-only.** All three rows of
   `conj:canonical-knot-id-sdp` §"Historical evidence" carry volumes of *other*
   census manifolds than the knots they name:

   | row | named knot | table Vol | census(named) | table Vol identifies as |
   |---|---|---|---|---|
   | ²H | 6₂ | 3.16396 | 4.40083 | **6₁** (m032/m033) |
   | ³H | 8₁₁ | 3.42721 | 8.28632 | **8₁** (m073/m074) |
   | ³He | L6a4 | 5.33349 | 7.32772 | **6³₁ family** (s772–s789; also 6²₃, 8³₈, …) |

   Every orphan is a subscript-neighbour of its named knot (6₁↔6₂, 8₁↔8₁₁,
   6³₁↔6³₂ = L6a4), and the three table values are internally consistent with a
   single 𝔈₀ ≈ 4.150 MeV — the signature of an earlier {6₁, 8₁, 6³₁}
   volume-matching assignment that a later renaming to {6₂, 8₁₁, L6a4} never
   reconciled. (`MostowRigidity.lean`'s `Vol(6_1) ≈ 3.16396` mention is a
   *legitimate* volume-spectrum statement — the next distinct value above
   Vol(5₂) — not a deuteron-table leak; an earlier draft of this note
   overstated that.)

2. **Production verifies clean against the names.**
   `per-atom-hyperbolic-volume.witness.json` matches the named knots' census
   volumes at the f64 floor (≤ 2.1e-15); `substrate/knot_volumes.py` constants
   verify to ≤ 1e-20 — except the literature-sourced `VOL_5_2` at 3.3e-12
   (~12 effective dps; upgradeable to 50 dps via ManifoldHP now that SnapPy
   runs in-sandbox).

3. **Thread-4 decision sharpened.** The volume-matching evidence stream
   *appeared* to support {6₁, 8₁, 6³₁}; the SDP partial closure + production
   wiring use {6₂, 8₁₁, L6a4}.
   **Adjudicated same day:** recomputing the match under the
   zero-free-parameter law `B_AME ≈ ρ·m_e·Vol(K)` shows the NAMED set
   reproduces the historical quality pattern (+1.09 %/−0.16 %/−2.97 %)
   while the orphan set fails (27–59 %; deuteron fails at every integer
   ρ ≤ 4) — the names are right, the digits are stale, production needs
   no change. See
   [`2026-06-12-knot-id-volume-match-adjudication.md`](2026-06-12-knot-id-volume-match-adjudication.md);
   the mechanical digit fixes stay owner-confirmed.

4. **Infra bug found en route — diagnosis CORRECTED 2026-06-13:** the
   `scriptCommitSha: "unknown"` serialisations were **not** a
   `WitnessBuilder` pathspec bug (the builder resolves absolute paths
   correctly). Root cause: fresh sandbox containers run as root on a
   checkout owned by another uid, git refuses with *dubious ownership*,
   and the builder's bare `except` silently normalised the failure to
   `"unknown"`. Fixes: `scripts/session-status.sh` now marks the repo
   `safe.directory` at session start, and `qou_substrate.witness`
   (v0.1.2) warns to stderr on git *invocation* failure instead of
   conflating it with the legitimate "file not yet committed" case.
   Content provenance via `scriptHash` was never affected.
