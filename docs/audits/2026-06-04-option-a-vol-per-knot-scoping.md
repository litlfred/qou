# Option A scoping — per-knot Vol(β_K) for the light isotope series

**Date:** 2026-06-04
**Trigger:** PR #1762 ("1ppQ roadmap + VolDensity bridge derivation gap") §5
Option A — *"Wire up Vol(β_K) for the light series (infrastructure). Win:
separates the Vol-uniform bug from the linking_weight question."*
**Scope of THIS document:** read-only code map + a **safe, diagnostic-only**
implementation plan. No production code is changed by this document. The
production-switch decision is escalated to the owner (see §5).

---

## §1. The current production path (uniform Vol)

| Concern | Location | Behaviour |
|---|---|---|
| Uniform `VolDensity` | [`_li_2_q_util.py:292`](../../computations/_li_2_q_util.py) `vol_density_borromean(q)` | `Vol(𝓑₃)/ℏ_q² · linking_weight_family_a(q)`, with `Vol(𝓑₃) = 8·G` hardcoded (`:344`) for **every** atom |
| Family-A linking weight | [`_li_2_q_util.py:172`](../../computations/_li_2_q_util.py) `linking_weight_family_a(q)` | `5/2 + (3/4)·h²` (the H₄ half-Wedderburn count ≈ 2.53) |
| Mass-table consumer | [`mass_table_comprehensive.py:208`](../../computations/mass_table_comprehensive.py) `borromean_mass_prediction(Z,N,q)` | line 208 `vol_density = vol_density_borromean(q)` — **same call for p, n, D, T, ³He, ⁴He** |
| Bug acknowledgement | [`mass_table_comprehensive.py:100`](../../computations/mass_table_comprehensive.py) `ATLAS_TAG` | D/T/³He tagged `"manual-historical-volume-match"`, ⁴He `"magic-A-formula"` — explicit KLUDGE markers |
| Prior audit | [`docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`](2026-06-02-vol-usage-audit-uniform-vs-per-knot.md) | 87 scripts use uniform Vol; 64 atom-touching scripts carry the bug |

## §2. The per-knot infrastructure already exists (just unwired)

| Piece | Location | Status |
|---|---|---|
| Per-knot `VolDensity` | [`_li_2_q_util.py:372`](../../computations/_li_2_q_util.py) `vol_density_per_block(vol_K, tr_M_K, q)` | **ready** — `Vol(K)/ℏ_q² · tr_M(K,q)` |
| Bare hyperbolic factor | [`_li_2_q_util.py:358`](../../computations/_li_2_q_util.py) `geom_leading(vol_K, q)` | ready |
| Per-atom braid words | [`mass_at_3A_proper.py:255`](../../computations/mass_at_3A_proper.py) `atom_braid_word_3A(Z,N)` | ready — canonical `H_{3A}` words for every isotope |
| Per-knot volume table | [`qou-mass/.../knot_volumes.py`](../../qou-mass/src/qou_mass/_internal/knot_volumes.py) | partial — Borromean (8·G), 6₂, 8₁₁, 7²₁, 4₁ at 50 dps |
| Per-atom Markov traces | `computations/chi-{atom}-h{3A}-at-q0-50dps.witness.json` | exist for p/n; higher A needs `markov_peel.tr_M_atomic(Z,N)` |

## §3. ⚠ Critical safety constraint — Option A is DIAGNOSTIC, not a production flip

The source docstring is explicit
([`_li_2_q_util.py:298-313`](../../computations/_li_2_q_util.py)):

> This routine multiplies the bare hyperbolic `Geom_leading = Vol(𝓑₃)/ℏ_q²`
> by a GLOBAL scalar `linking_weight_family_a(q)` ≈ 2.53 … For 𝓑₃ the
> paper's per-block sum is the H₃ Markov trace **tr_M(𝓑₃) ≈ 1.065 (proton)
> / 0.923 (neutron), not 2.53. The two differ by ≈ 2.38×** … the 2.53 is a
> CODATA-implied-λ near-match … This routine is retained ONLY until the
> per-block version is validated and **the owner approves a production
> switch (the switch changes the m_p computation).**

**Consequence:** naïvely replacing `vol_density_borromean` with
`vol_density_per_block` in `mass_table_comprehensive.py` would multiply the
proton mass by ≈ 1.065/2.53 ≈ 0.42 — i.e. **break m_p (the CAL-2 anchor)
by ≈ 2.38×** (this is exactly PR #1762 §2's "Form 2 = −57 % vs CODATA").
m_p is a *calibration input*, not a free prediction, so this is not a
permissible autonomous change.

Therefore Option A, done correctly, is an **infrastructure / diagnostic**
step: compute per-knot `Vol(β_K)` and the per-block `VolDensity` for the
light series **alongside** production, emit a comparison witness, and
**report the gap** — without flipping production. This matches #1762 §5's
own framing ("separates the Vol-uniform bug from the linking_weight
question") and respects the production-vs-exploratory + Δ_λ-gate discipline
(no fit, no ansatz, no silent recalibration).

## §4. Safe implementation plan (diagnostic-only, no production change)

1. **New EXPLORATORY script** `computations/probes/option_a_vol_per_knot_light_series.py`:
   - For each light isotope K ∈ {p, n, D, T, ³He, ⁴He}: look up `Vol(β_K)`
     (from `knot_volumes.py`; for any missing isotope, record it as a
     `TODO`/`null` with the canonical braid word from `atom_braid_word_3A`
     rather than inventing a value).
   - Load `tr_M(β_K, q₀)` from the chi-cache witnesses (p/n available;
     higher A flagged `needs markov_peel.tr_M_atomic`).
   - Compute three numbers per isotope at q₀: the **uniform**
     `vol_density_borromean(q₀)`, the **per-knot**
     `vol_density_per_block(Vol_K, tr_M_K, q₀)` (full three-argument
     signature per [`_li_2_q_util.py:372`](../../computations/_li_2_q_util.py)),
     and their ratio + the resulting m(K) under each.
   - **Precision:** the inputs are the canonical 50-dps witness values
     (`knot_volumes.py` volumes and the `...q0-50dps...` chi-caches), so
     the comparison is meaningful only to the **50-dps input floor**.
     The probe runs mpmath at the `_precision.py` default 65-dps working
     precision (to avoid intermediate round-off) but reports/serialises
     results at 50 dps, matching the input witnesses and the standard
     50-dps serialization floor. No input is "upgraded" beyond its
     witnessed precision.
   - Emit `option-a-vol-per-knot-light-series.witness.json` recording all
     three per isotope, with `discipline: "EXPLORATORY"`, `production_wired: false`.
2. **No edit** to `mass_table_comprehensive.py`, `vol_density_borromean`, or
   any Tier-1 production path.
3. **Appendix contract:** because production is untouched, the
   `mba-step09a-mass-identity.md` `alg:` block does **not** change in this
   PR. (The appendix-sync contract triggers only on a production-algorithm
   or production-witness change; a clearly-labelled exploratory probe does
   not.) The eventual production switch — if the owner approves it — is the
   PR that must update `mba-step09a` + the per-observable witnesses.

## §5. Owner decision (escalated — see PR description)

Option A as scoped here is the safe path: a diagnostic that quantifies the
per-knot-vs-uniform gap for the light series without touching the m_p
calibration. The genuinely owner-gated question is whether/when to **flip
production** to the per-block formula — which is the GAP-A territory (it
needs the linking_weight question resolved first, since per-block tr_M
alone under-shoots m_p by 2.38×). This document does **not** make that
flip; it builds the measurement that informs it.
