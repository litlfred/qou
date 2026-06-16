# CODATA-2022 precision-pipeline audit (2026-05-23)

**Context**: user pushback on the 1ppb-gap-closure audit
(2026-05-23) — *"are you using the downloaded codata .dat file?
those aren't higher precision? review constants are pulled
directly from source file (through help library)."*

This audit traces the CODATA-precision pipeline end-to-end:
where values are stored, at what precision, against what published
NIST values, and where derived-vs-direct ambiguities exist.

## Headline findings

| finding | severity |
|---------|----------|
| **No CODATA `.dat` fetcher in the repo.** All values are hardcoded Python literals. | low (intentional; vendoring is OK) |
| **`codata_constants.M_E_MEV = 0.51099895` truncates the CODATA-2022 value `0.51099895069`** by 3 sig figs. | medium (4 scripts already re-define at full precision — inconsistent) |
| **`codata_constants.M_N_MEV = 939.56542052` is the AME-DERIVED neutron mass**, NOT the CODATA-2022 direct value `939.56542194`. Diff: 1.5 ppb. | low (documented in the source comment but the distinction isn't surfaced module-wide) |
| **My earlier audit said "150 ppb" m_n discrepancy** — wrong (units error). Actual: 1.5 ppb. | corrected here |
| **Q_β framework residual of 11 ppb against AME is REAL**, not an anchor-precision artifact. | corrected from earlier audit |

## Constant-by-constant precision audit

| constant | stored (`codata_constants`) | NIST CODATA 2022 | gap | source |
|----------|----------------------------|------------------|----:|--------|
| m_e c² | `0.51099895` | `0.51099895069(15)` | -3 sig figs | NIST allascii |
| m_p c² | `938.27208816` | `938.27208816(29)` | 0 (matches) | NIST allascii |
| m_n c² | `939.56542052` (AME-derived) | `939.56542194(48)` direct, `939.56542052(60)` AME | derived ≠ direct (1.5 ppb apart) | NIST allascii / AME 2020 |
| m_μ c² | (not in primary file) | `105.6583755(23)` | n/a | NIST allascii |
| m_μ/m_e | `206.7682830` | `206.7682830(46)` | 0 (matches) | NIST allascii |
| Q_β(n) | `0.78233341` (CAL-3 anchor) | n/a (not in CODATA; AME 2020) | 0 (matches AME) | AME 2020 |

The truncation of `M_E_MEV` is the only meaningful storage gap.
The m_n derived-vs-direct discrepancy is a real choice with
known consequences (Q_β consistency vs absolute m_n).

## Deliverable: `codata_2022_source.py`

New module
[`computations/codata_2022_source.py`](../../computations/codata_2022_source.py)
is the vendored snapshot — single source of truth for high-precision
CODATA-2022 values, with:

- Per-constant role tags (CAL-1/2/3 vs VALIDATION)
- Two-value disambiguation for m_n (`M_N_MEV_CODATA_DIRECT` vs
  `M_N_MEV_AME_DERIVED`)
- Q_β computed three ways (AME direct, derived from CODATA-direct
  m_n, derived from AME m_n) — surfaces the 1.8 ppm consistency
  band between paths
- `summary()` diagnostic for debug/dashboards

Provenance: snapshot date `2026-05-23`, edition year 2022, source
URL `https://physics.nist.gov/cuu/Constants/`.

## Q_β residual correction (from earlier audit)

My **2026-05-23-1ppb-gap-closure-analysis.md** earlier framed
the Q_β residual as a CAL-3 anchor-precision artifact. **That
was wrong.**  After this audit:

- CAL-3 anchor: `0.78233341` (AME 2020, σ = 0.61 eV = 779.7 ppb)
- Framework Q_pred (with c_3 = -2 = J_Hopf(q=1) applied):
  `0.782333418708`
- **Real residual: 8.7 × 10⁻⁹ MeV = 11.13 ppb (1.43× over 100×
  target of 7.8 ppb).**
- This is a **framework gap**, not an anchor-precision floor.

The "Q_AME = 0.782333414" the probe used is a higher-precision
write-out of the same AME value (m_n - m_p - m_e at the full
stored precision), but the AME measurement itself is only good
to 0.61 eV, so the extra digits are not a tighter anchor.

**Honest status: Q_β framework prediction is 1.43× over the 100×
L2 target, structurally bounded by the framework's c_k expansion
ceiling (c_3 = -2 closed; c_4..c_7 already extracted in
`qbeta-decay-sdp-full-ck-derivation.witness.json`).**

## Recommendations

### Tractable (mechanical migrations)

1. **Update `codata_constants.M_E_MEV`** from `0.51099895` to
   `0.51099895069` (the full 11-sig-fig CODATA-2022 value).
   Currently 4 scripts redefine M_E_MEV with the higher precision —
   the cal4-disguise-hunt audit (2026-05-22) flagged these as
   "Pattern C" violations.  Updating the module source unifies them.
2. **Have `codata_constants.py` import from `codata_2022_source.py`**
   instead of carrying its own literals.  Single source of truth.
3. **Add a m_n DUAL-SOURCE accessor** — when a script needs m_n,
   it should explicitly choose CODATA-direct vs AME-derived rather
   than relying on the implicit default.
4. **Replace `cal-3-q-beta.witness.json` storage with a generator
   from `codata_2022_source.py`** — eliminates the chance of the
   witness drifting from CODATA when an edition update lands.

### Out-of-scope for this PR

- Building a NIST-allascii.txt fetcher with cache + diff against
  vendored snapshot.  Useful when CODATA-2026 lands but not needed
  for current precision.
- Pulling `scipy.constants` as an alternative source.  scipy uses
  CODATA-2018 (one edition behind) so it would be redundant with
  the vendored snapshot anyway.
- Closing the framework's 11 ppb Q_β residual.  That's a separate
  research question (c_k beyond N=7 extracted, framework prediction
  is at the algebraic ceiling).

## Q_β 100×-target closure summary

After this audit + the prior 1ppb gap closure:

| observable | framework status | 100× target | meets? |
|------------|------------------|------------|:------:|
| m_e | anchor | 0.003 ppb | ✓ |
| m_μ | 0.06 ppb (CAL-2 anchor) | 0.218 ppb | ✓ |
| **Q_β** | **11.13 ppb (c_3 = -2 closed)** | **7.797 ppb** | **✗ (1.43× over)** |
| m_p | 2.89 × 10⁷ ppb (Family A ceiling) | 0.003 ppb | ✗ |
| m_n | same | 0.006 ppb | ✗ |
| Δ_pn | 2.86 × 10⁷ ppb (substrate flavor split) | 4.74 ppb | ✗ |

**3 of 6 meet 100× by anchor; 0 of 3 framework predictions meet
100× under current categorical infrastructure.** Closing the
remaining 3 requires research-level work (Bring-Bloch substrate
derivation, GAP-A-3/4 categorical brane-tower selection, or
Option E Kashiwara crystal — all out-of-scope per
coord-ledger 2026-05-08).

## Cross-references

- `docs/audits/2026-05-23-1ppb-gap-closure-analysis.md` — earlier
  audit (this one corrects a precision-pipeline misreading)
- `docs/audits/2026-05-22-cal4-disguise-hunt.md` — flagged the
  scripts that re-define M_E_MEV at higher precision
- `docs/audits/codata-reconciliation.md` — existing CODATA-vs-
  prediction reconciliation infrastructure
- `computations/substrate/codata_constants.py` — existing
  storage (to be updated)
- `computations/codata_2022_source.py` — new
  source-of-truth module (this PR)
- NIST CODATA 2022: https://physics.nist.gov/cuu/Constants/
