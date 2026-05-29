# Low-mass sweep — full audit + brane-tower wiring assessment (2026-05-29)

## Headline

There is **no single mass sweep** — there are **four overlapping
pipelines** producing **different numbers via different methods for
the same atoms**. The fragmentation, plus a **stale published table
backed by a nonexistent witness**, is the main finding. The
"brane-tower corrected" m_p that this audit was asked to wire
everywhere turns out to be **either not-derived (d₃ unidentified) or
CODATA-anchored (validation row)** — so wiring it as a derived
correction would propagate fits.

## 1. Coverage — "what happened to Ca?"

| Pipeline (witness) | Atoms | Method | Status |
|---|---|---|---|
| `low-isotope-mass-table` | p,n,D,T,³He | canonical Σ y_λ·χ^λ (laurent_q) | A≤3 by design (wrapper line 76) |
| `canonical-mass-table-extended` | …+⁴He; 5–7Li **null** | laurent_q; B_pred cross-ref'd from `mass-table-ppb` | \|tr_M\| computes for ⁴He+ but **B_pred=null A≥5** |
| `mass-table-ppb` | 16 entries Z1–20 incl. ⁴⁰Ca | Kashaev Vol-law (A≤3) + α-cluster (A≥4) | live, but +5–20% error |
| `mass-table-comprehensive` | 65 isotopes p→⁵⁸Fe | absolute mass Z·m_p+N·m_n−B | binding A≥5 **not computed** |
| **PUBLISHED `mass-table-z1-20.md`** | Z1–20 incl. Ca | "3-invariant Wedderburn" | **STALE — backing witness `atom-mass-complete-wedderburn.witness.json` does not exist** |

**Why the canonical sweep stops at ³He/⁴He:** not compute cost
(⁷Li laurent_q ≈ 1.1 hr, feasible). The wall is the **binding-energy
map**: A≥5 has **no derived atom→knot rule** (5Li/6Li/7Li marked
`"gap"`). \|tr_M\| computes for ⁴He+, B_pred stays null.

**Ca specifically:** only `mass-table-ppb` predicts it, via the
α-cluster rule (n_α=10) at **+19.5%** — error degrades monotonically
with A (⁸Be +10%, ¹²C +5.4%, ²⁰Ne +8.3%, ⁴⁰Ca +19.5%).

## 2. Per-atom error + method (best live witness)

| Atom | Pred | Exp | Err | Method |
|---|---|---|---|---|
| p | 965.38 | 938.272 | **+2.89%** | Family-A Geom_full(𝓑₃) |
| n | 966.71 | 939.565 | **+2.89%** | Family-A |
| D | 2.249 (B) | 2.2246 | +1.09% | canonical-trace / census 6₂ |
| T | 8.469 (B) | 8.482 | −0.16% | canonical-trace / census 8₁₁ |
| ³He | 7.489 (B) | 7.718 | −2.97% | canonical-trace / census L6a4 |
| ⁴He | 29.96 (B) | 28.30 | +5.87% | A·8G "magic" rule |
| ⁸Be | 62.3 (B) | 56.5 | +10.3% | α-cluster |
| ¹²C | 97.2 (B) | 92.2 | +5.4% | α-cluster |
| ⁴⁰Ca | 408.8 (B) | 342.1 | **+19.5%** | α-cluster n_α=10 |
| 5/6/7Li, 9Be, 11B, 14N, 19F | null | — | — | **GAP (no rule)** |

## 3. Fitted / empirical / justified-but-not-derived

| Atom(s) | Class | Evidence |
|---|---|---|
| p, n (Geom_full +2.89%) | **(a) Derived** — honest gap | Family-A λ_A=5/2+¾h² proved |
| **m_p/m_n/m_μ in 100x dashboard** | **(c) EMPIRICAL** — `role:"validation"`, pred=codata identically, ratio-anchored to CODATA m_e | `per_observable_100x_status.py:94` |
| D, T, ³He | **(d)→(b)** census-assigned knots = "AME-driven fitting" | `mass_table_ppb.py:18-21`, `origin:"hyp: census-assigned (EXPLORATORY)"` |
| ⁴He | **(d)** "magic rule, ν_SDP extrapolated" | `mass_table_ppb.py:110` |
| ⁸Be…Ca (α-cluster) | **(d)** n_pairs=C(n,2) asserted; +5–20% over-pred = KLR-positivity violations | `mass_sweep_wiring_status.py:29-33` |
| **Q_β** | **(a) DERIVED** (Habiro-exact, CAL-3) — the ONE genuine sub-100× | `q-beta-operator-valued-N3` |
| Published Z1–20 | **UNVERIFIABLE** — backing witness absent; falsely claims "zero fitted parameters" | `mass-table-z1-20.md` |
| `branch_phase_fit_to_mass_tower.py` | **(b) FITTED (self-declared)** | line 123 "Suggestive partial fit, not a derivation" |

## 4. The brane-tower / m_p "0.39 ppQ" reality

**Correction (owner, 2026-05-29): the tower coefficients c_k / d_k ARE
derived — they are Habiro/Taylor expansion coefficients of the exact
rational mass function, not fitted.** Confirmed:
- Q_β: `qbeta_habiro_tower_1ppq.py:8` — c_k are "integer or algebraic
  expressions from the Habiro series"; c₂=−1, c₃=−2=J (line 68). This
  is the **production** Q_β path and the one genuine sub-100×
  derivation (5.7 ppb).
- m_p: `habiro_exact_mass_endomorphism.py:43` — "Habiro coefficients …
  are exact polynomials".

So "d₃ needs categorical identification" (the exploratory probe) means
its categorical **name** (which knot invariant) is open — **not** that
its value is fitted. My earlier "not derived" framing was wrong on this
point.

**However**, the dashboard's sub-ppQ m_p is still **not** the Habiro
tower — it is a *validation* row anchored to CODATA m_e (pred=codata).
The production-derived m_p paths give:
- Habiro-exact mass endomorphism: m_p **+1.84%**, m_n **−55%** (the
  neutron tower in that script is badly off; Δm_np nonsense). NOT
  production for the nucleons.
- Substrate identity `m_p = dim V₍₂,₁₎·(m_μ·F_Bor − |S₃|·m_e)`: **0.24
  ppm** — derived structure (2, |S₃|=6), the ONE open piece being
  F_Bor's status as "the natural categorical observable" (line 67).
- Family-A Geom_full single-level: +2.89%.

**Net for wiring:** the c_k/d_k Habiro method is derived and is
already production for **Q_β**. For the **nucleons**, the cleanly-
derived path is the substrate identity (0.24 ppm) modulo the F_Bor
derivation; the Habiro endomorphism is not yet wireable (m_n −55%);
the 0.39 ppQ is CODATA-anchored. So the legitimate wiring is the
substrate identity (label F_Bor open), not a silent tower factor.

## 4b. Root cause of the nucleon +2.89% — a missing DERIVED factor

The nucleon gap is a **uniform scale** (p and n agree to 0 ppm; both
= 1.028891), so it is a scaling issue, not per-knot. Decomposing
m_p/m_e into known component pieces (Route 2):

| Piece | Value | Behavior |
|---|---|---|
| Vol(B₃) = 8G | 7.3277 | Catalan, derived |
| Vol(B₃)/ℏ² | 746.42 | geometric scale |
| lw_A = 5/2 + 3h²/4 | 2.5328 | Family-A, PROVED |
| spectral_corr = arccos(2−3h⁴−h⁶)/(8ℏ²) | 0.97112 | arccos of exact Hoefsmit χ^(2,1)(B₃) |

- leading (Vol/ℏ²·lw_A): m_p/m_e = 1890.5 → **+2.96%** (= the sweep's +2.89%)
- × spectral_corr: m_p/m_e = 1835.9 → **−130 ppm**

So the +2.89% is **one missing multiplicative factor** — the spectral
correction 0.97112 (1/0.97112 = 1.0297 ≈ the uniform 1.0289). It is
**derived** (arccos of the exact Borromean character χ^(2,1)(B₃) =
2−3h⁴−h⁶, Hoefsmit), not fitted, not a coordinate error. The sweep's
`Geom_full(𝓑₃)` computes the leading `Vol/ℏ²·lw_A` and **omits** this
factor. Wiring it closes nucleons +2.89% → 130 ppm (the residual is
the arccos Taylor truncation, h⁴-order). This is a legitimate,
derivable wiring — distinct from the α-cluster (+5–20%, binding
overcounting) and the non-production Habiro-endomorphism m_n (−55%).

## 5. Recommendations (priority order)

1. **Fix/retract the stale published Z1–20 table (discipline risk,
   top priority).** `mass-table-z1-20.md` advertises mean-0.074%
   "zero-fitted" numbers backed by a witness that does not exist.
   Either regenerate from a real script or replace with live
   `mass-table-ppb`/`comprehensive` numbers (+3.8% / +5–20%) and drop
   the "zero fitted parameters" claim.
2. **Close the A∈{5,6,7} atom→knot gap with a DERIVED rule (SDP),
   not census.** This is the single blocker stopping the canonical
   Σ y_λ·χ^λ pipeline from extending. Replace census knots
   6₂/8₁₁/L6a4 with SDP-selected braid words (the gated "R5-full SDP
   solver"). Do not add a 7th fit (CLAUDE.md Δ_λ gate).
3. **Consolidate the four pipelines to one canonical consumer.**
   Make `canonical-trace` authoritative; mark the others
   downstream/deprecated. Stop `canonical_mass_table_extended` from
   cross-referencing census `mass-table-ppb` for B_pred while its
   docstring claims "canonical".
4. **State the honest headline:** categorical m_p/m_n = +2.89%;
   D +1.1%, T −0.16% (census-fitted knots); Q_β the only genuine
   sub-100× prediction. The "6/7 beat 100×" framing rests on
   CODATA-anchored validation rows, not predictions.

## Note on wiring (the original request)

The request was to "wire the brane-tower knot-convolution corrected
values everywhere." Per §4, the correction is not a clean derivation,
so the disciplined action is **not** to apply it silently. The
legitimate wiring is the **substrate identity** (derived structure)
for p/n — clearly labeled, reaching 0.24 ppm — with the residual
brane-tower ratio flagged conditional/conjectural, not presented as
closing the gap.
