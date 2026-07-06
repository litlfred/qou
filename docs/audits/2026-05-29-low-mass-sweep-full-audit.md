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
| p | 965.38 | 938.272 | **+2.89%** | Family-A VolDensity(𝓑₃) |
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
| p, n (VolDensity +2.89%) | **(a) Derived** — honest gap | Family-A λ_A=5/2+¾h² proved |
| **m_p/m_n/m_μ in 100x dashboard** | **(c) EMPIRICAL** — `role:"validation"`, pred=codata identically, ratio-anchored to CODATA m_e | `per_observable_100x_status.py:94` |
| D, T, ³He | **(d)→(b)** census-assigned knots = "AME-driven fitting" | `mass_table_ppb.py:18-21`, `origin:"hyp: census-assigned (EXPLORATORY)"` |
| ⁴He | **(d)** "magic rule, ν_SDP extrapolated" | `mass_table_ppb.py:110` |
| ⁸Be…Ca (α-cluster) | **(d)** n_pairs=C(n,2) asserted; +5–20% over-pred = KLR-positivity violations | `mass_sweep_wiring_status.py:29-33` |
| **Q_β** | **(a) DERIVED** at the substrate-identity / Habiro-exact residual; its *ppb-closing* c_k rungs were CODATA-fits, **removed by #1416** | `q-beta-operator-valued-N3` |
| Published Z1–20 | **UNVERIFIABLE** — backing witness absent; falsely claims "zero fitted parameters" | `mass-table-z1-20.md` |
| `branch_phase_fit_to_mass_tower.py` | **(b) FITTED (self-declared)** | line 123 "Suggestive partial fit, not a derivation" |

## 4. The brane-tower / m_p "0.39 ppQ" reality

**Reconciled (2026-05-29, with merged #1416).** Two distinct objects
were being conflated, and #1416 (merged) cut the line:

- **Habiro-exact value (DERIVED).** The c_k/d_k *as Habiro/Taylor
  coefficients of the exact rational mass function* are derived
  (`habiro_exact_mass_endomorphism.py`); they reproduce the
  formula→Habiro value, which for m_p is **+1.84%** vs CODATA.
- **ppb-closing rungs (FITTED — removed by #1416).** The *additional*
  tower rungs that tuned the Habiro-exact value down to ppb (the
  `(1+46u⁴)…`, the "m_p 0.39 ppQ", the Q_β c_k closure) closed the
  formula→**experiment** gap — i.e. CODATA-fits, not derivations.
  #1416 removed them; the honest dashboard is now **2/7** (m_e + m_p),
  not 6/7. My original "not derived" audit framing was right; the
  intervening "c_k/d_k are derived → 0.39 ppQ" reading conflated the
  derived Habiro-exact value with the fitted ppb closure.

**Where this leaves the nucleon m_p (derived options):**
- Habiro-exact endomorphism: m_p **+1.84%** (m_n −55%, non-production).
- Substrate identity `dim V₍₂,₁₎·(m_μ·F_Bor − |S₃|·m_e)`: **0.24 ppm**,
  derived structure (2, |S₃|=6), F_Bor "natural observable" open.
- **Spectral correction (this PR): m_p = Vol(B₃)/ℏ²·lw_A·arccos(χ/2)/(8ℏ²)
  → 130 ppm** — a separate derived path with **no tuned coefficient**
  (Vol=8G, lw_A proved, χ from Hoefsmit), so it **survives the #1416
  de-fit**. This is the legitimate derived m_p closure, distinct from
  the removed fitted brane-tower.

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
2−3h⁴−h⁶, Hoefsmit), not fitted, not a coordinate error.

**The character input is itself derived, not asserted.** Building the
Hoefsmit (2,1) matrices σ₁ = diag(q, −q⁻¹), σ₂ from the Hecke
quadratic + braid relation, the Borromean braid B₃ = (σ₁⁻¹σ₂)³ has
bare (2,1) trace
`tr_{(2,1)}[(σ₁⁻¹σ₂)³] = −q⁶+3q⁴−3q²+4−3q⁻²+3q⁻⁴−q⁻⁶ = 2−3h⁴−h⁶`
— verified symbolically (sympy-exact) and numerically at q₀ (residual
< 1e-30, witness assertion `borromean_char_derived_from_hoefsmit`).
Lean: `borromeanChar_laurent` proves the Laurent form. So the entire
m_p → 130 ppm chain (Vol=8G, lw_A proved, χ derived) is
first-principles.

**Neutron (the other +2.89% nucleon) — per-knot lw, open.** Each knot
has its **own** linking weight (not the proton's + a correction). The
effective (spectrally-corrected) weights are per-knot: λ_p ≈ 2.4596,
**λ_n ≈ 2.4633** (`lambda_scale_substrate_probe.py`). The neutron's is
`λ_n = 5/2 − h²·G + ΔS(n)·ℏ²/Vol(B₃)`, where ΔS(n) is the neutron's
Skein correction from its udd braid. The shared 𝓑₃ spectral factor
applies to both; the n-p splitting is entirely in ΔS(n).
Numerically the required ΔS(n) ≈ 2.46 is **not** a clean derived
integer (and the leading-weight difference lw_A_n − lw_A_p = 2.0007·h⁴
is a fit-to-CODATA, not derived — the Family-A h⁴ term is proved to
vanish). So the genuine n-p splitting = derive ΔS(n) from the
neutron's braid Skein count — open, analogous to the m_K/m_π EM
correction. **Not wired** (would be a fit).

**q₀-robust (vs #1422's re-pin).** Evaluated at both the muon-pinned
q₀ (−130.35 ppm) and #1422's m_p-pinned q₀ = 1.10997858275 (−130.16
ppm), the spectral decomposition shifts only 0.19 ppm under the
−11.5 ppb re-pin. So the 130 ppm is intrinsic to the decomposition,
not a pin artifact — and it is a **separate derived** m_p path,
distinct from #1422's m_p-as-anchor (which is 0 by construction). The sweep's
`VolDensity(𝓑₃)` computes the leading `Vol/ℏ²·lw_A` and **omits** this
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
   solver"). Do not add a 7th fit (AGENTS.md Δ_λ gate).
3. **Consolidate the four pipelines to one canonical consumer.**
   Make `canonical-trace` authoritative; mark the others
   downstream/deprecated. Stop `canonical_mass_table_extended` from
   cross-referencing census `mass-table-ppb` for B_pred while its
   docstring claims "canonical".
4. **State the honest headline (post-#1416):** the dashboard is now
   **2/7** (m_e + m_p), not 6/7 — #1416 removed the CODATA-fitted
   ppb-closing towers (m_p `(1+46u⁴)`, Q_β c_k). Categorical m_p/m_n
   raw = +2.89%; Habiro-exact m_p = +1.84%; the derived **spectral
   correction closes m_p to 130 ppm** (this PR, no tuned coefficient).
   D +1.1%, T −0.16% use census-fitted knots.

## Note on wiring (the original request)

The request was to "wire the brane-tower knot-convolution corrected
values everywhere." Per §4, the correction is not a clean derivation,
so the disciplined action is **not** to apply it silently. The
legitimate wiring is the **substrate identity** (derived structure)
for p/n — clearly labeled, reaching 0.24 ppm — with the residual
brane-tower ratio flagged conditional/conjectural, not presented as
closing the gap.
