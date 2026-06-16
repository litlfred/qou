# Discipline assessment — Option E v9 ³H/³He mirror-difference "closure"

**Date**: 2026-05-31
**Author**: discipline-gate audit (production-vs-exploratory + canonical-derivation)
**Subject**: PR #1570 (`claude/option-e-richer-delta-rules-2026-05-30`, merged) — the
claim that

$$
B_T - B_{^3\mathrm{He}} \;=\; m_\pi \cdot \hbar_q \cdot \frac{1+q}{2}
   \cdot \sum_\lambda y_\lambda \cdot
   \frac{\chi^\lambda(\mathcal{B}_T) + \chi^{\lambda^\mathsf{T}}(\mathcal{B}_{^3\mathrm{He}})}{2}
   \approx 0.7629\ \mathrm{MeV}
$$

closes the A=3 isospin mirror difference to **0.11 %** (target 0.7637 MeV).

> **Verdict (one line): NUMEROLOGY / post-hoc fit.** The `(1+q)/2` factor is
> NOT substrate-derived — it was computed as the exact ratio needed to hit
> the target and then name-matched against a 9-candidate substrate menu, and
> it **fails to generalize** to the absolute binding energies (154 % error).
> Do NOT promote to a proposition claiming closure.

---

## 1. What was actually computed (evidence)

Scripts on `main` (all under `computations/`):

- [`option_e_v7_involution_aware.py`](../../computations/option_e_v7_involution_aware.py)
  — 5 scales × 7 involution sums = **35 candidates** for the mirror pair,
  plus the same grid against D, T, ³He absolute energies.
- [`option_e_v8_hecke_involution_isospin_mirror.py`](../../computations/option_e_v8_hecke_involution_isospin_mirror.py)
  — 6 scales × 5 inputs = **30 candidates** for the mirror pair.
- [`option_e_v9_all_symmetries.py`](../../computations/option_e_v9_all_symmetries.py)
  — docstring: "Tests 9 scales × 9 input combinations = **81 candidates**",
  PLUS a separate **9-candidate** "multiplicative correction" search.

### The decisive code (v9, lines 190–211)

```python
base_v8 = M_PI_MEV * H_Q * base_sym                 # the 6.15%-off baseline
correction_target = diff_target / base_v8          # <-- SOLVE for the needed factor
...
cands = [ ("1 + h_q²", ...), ("(1 + q)/2", (1 + Q_0) / 2), ... ]   # 9 substrate guesses
for name, val in cands:
    err = (val - correction_target) / correction_target * 100      # which guess is nearest?
```

`correction_target` is **defined as** `target / baseline` — i.e. exactly the
number required to make the formula hit the experimental value. The script
then asks which of 9 hand-picked substrate expressions lands nearest to that
required number. `(1+q)/2 = 1.05485` happens to sit 0.113 % from the required
1.05605 (re-verified at 40-digit decimal: needed factor
`1.0560497209845428`, `(1+q)/2 = 1.05485451245`, gap `−0.1132 %`; final value
`0.7628736`, final err `−0.1132 %` — matches the committed witness exactly).
This is the canonical post-hoc-fit signature (skill
`production-vs-exploratory-discipline.md` Antipattern 1 / Antipattern 2):
solve for the residual, then find a substrate label near it.

### The "all symmetries" search itself FAILED

The 81-candidate grid in v9's witness
([`option-e-v9-all-symmetries.witness.json`](../../computations/option-e-v9-all-symmetries.witness.json))
has **`best_err_pct` = 2.52 %** (`m_π·ℏ_q·(1+ℏ_q) · (v8 alt y M_asym)`).
None of the 81 structural combinations reached the cheat-sheet's 2 %; the
0.11 % number comes ONLY from the appended divide-and-name-match step, not
from any symmetry combination.

---

## 2. Per-factor tiered classification

Tiered as in the Q_β `c_k` framing (`proved` / `near-match` / `fitted`):

| Factor | Value at q₀ | Classification | Rationale |
|---|---|---|---|
| `m_π` (139.57039 MeV) | 139.57 | **imported scale** | PDG charged-pion mass. It is a genuine isospin-breaking scale in QCD and the CAL-3 anchor in QOU — but here it is used as a *dimensional multiplier to set the MeV scale of a dimensionless character sum*, not derived to be the correct coefficient of this difference. Plausible, not derived. |
| `ℏ_q` (0.09886) | 0.09886 | **near-match** | q-Planck constant `1 − 1/q₀`; canonical substrate quantity. But there is no derivation that the mirror difference must carry exactly one power of ℏ_q; the power was selected because `m_π·ℏ_q` lands in the right ballpark (v8: 6.15 %). |
| `Σ y_λ · (χ^λ(T)+χ^{λᵀ}(³He))/2` | 0.05241 | **near-match (infrastructure-real, selection-fitted)** | The Wenzl weights `y_λ` and atom-side characters `χ^λ` ARE canonical infrastructure (Rust/Hoefsmit pipeline). The *cross-isotope bar-symmetric combination* (partition transpose = chirality, Z↔N = isospin mirror) is a defensible structural object. But choosing `M_sym` over `M_asym`, atom over free, `y` over `y²`/`dim`/`phase` was a **selection across the 9 inputs** v9 sweeps — the input was also chosen by best-fit. |
| `(1+q)/2` (1.05485) | 1.05485 | **FITTED** | Introduced at the last step purely to close 6.15 %→0.11 %. Defined operationally as the nearest substrate label to `target/baseline`. No categorical derivation; not traceable to any of the 13 canonical drivers; not in v9's own structural sweep; fails to generalize (§3). **This is the CAL-4 antipattern.** |

The PR-body table asserting "**Every factor is structurally meaningful** … no
fitting" is **not supported by the code**. The code's own variable name is
`correction_target = diff_target / base_v8` and its own block header is
"v8 base + multiplicative correction".

---

## 3. Generalization test (Option 3) — DECISIVE

Probe: [`probe_isospin_mirror_v9_generalization.py`](../../computations/probe_isospin_mirror_v9_generalization.py)
→ witness `probe-isospin-mirror-v9-generalization.witness.json`.

If `(1+q)/2` is a genuine substrate factor it must help the **absolute**
binding energies, not only the difference where it was back-solved. Applying
the same `m_π·ℏ_q·(1+q)/2 · Σ y_λ χ^λ(atom)` structure to D, T, ³He:

| quantity | err |
|---|---:|
| mirror **difference** with `(1+q)/2` (PR #1570) | **0.11 %** |
| absolute B max err WITH `(1+q)/2` | **154.0 %** |
| absolute B max err WITHOUT the factor | 140.8 % |

The factor not only fails to help the absolute energies — it makes them
*worse* (140.8 % → 154.0 %). **This is the textbook overfitting tell**: the
0.11 % was specific to the one number `(1+q)/2` was tuned against. (The probe
asserts the refutation, so `allPassed = true` on the expected-negative
outcome per discipline §Step 6.)

---

## 4. Overfitting / multiple-comparisons estimate

Distinct candidates evaluated against the **same** 0.7637 MeV mirror target:

| stage | candidates vs mirror target |
|---|---:|
| v1–v6 (per saga table) | ≥ 6 rule families, many variants (≳ 20) |
| v7 | 35 (5 scales × 7 inputs) |
| v8 | 30 (6 scales × 5 inputs) |
| v9 grid | 81 (9 scales × 9 inputs) |
| v9 correction search | 9 |
| **v7–v9 subtotal** | **155** |
| **incl. v1–v6 (conservative)** | **≳ 175** |

With ~175 tries against a single target, a sub-percent best match is
**expected, not surprising**. The 9 correction candidates alone span
0.55 → 1.81; sampling that many dimensionless substrate expressions, landing
one within ~0.1 % of an arbitrary target carries essentially **no evidential
weight** for a structural identity. (Cf. the `5/2 − h²·G` 5.6 ppm match
falsified across 5 routes — single-point closeness ≠ identity.)

The **q-locality gate** was not run on `(1+q)/2`, but it is moot: the factor
was back-solved from the target, not proposed as a q-form to be tested. The
fit lives in the **selection**, not the q-dependence — and §3 already refutes
it directly.

---

## 5. Comparison to the cheat-sheet line-113 claim

Cheat-sheet line 113 ("Bind" row) states the A=3 mirror pair closes "to 2 %
**with no fit**" via the q-Reeb phase θ_λ. **That claim was itself retracted**
in the same row: "per-λ 'closure' retracted as a C_knot fit; gate is the
A≥3 per-rep structure, NOT the scale (PR #1417)."

So v9 did **not** reproduce a standing "2 % no-fit" result — it re-opened an
already-retracted fit and pushed it from 2 % to 0.11 % by adding *another*
fitted factor. The PR title "cheat-sheet 2 % beaten" misreads a retracted
claim as a live benchmark.

What IS canonical and survives (per line 113, PR #1417):
- `μ₀ = m_e / (3(q−q⁻¹)/2) ≈ 1.63 MeV` — **derived**.
- `μ₀·ℏ_q·J_q²(j=n/2)` reproduces `B_D` to −9 % with **0 free params**
  (deuteron only) — a genuine zero-parameter near-match.
- The structural gate for A≥3 is the **per-rep deficit structure**, not any
  single scale factor.

---

## 6. Recommendation

1. **Do NOT author `prop:isospin-mirror-canonical-closure`.** The 0.11 % is a
   post-hoc fit, not a closure. A proposition would be a Δ_λ-gate violation in
   spirit (the standing "no 7th fit ansatz" rule) and a CAL-4 violation
   (off-menu fitted coefficient promoted as framework prediction).

2. **Author instead** an honest exploratory `remark`
   (`rem:isospin-mirror-v9-empirical-near-match`) that records the empirical
   near-match as exploratory, states the tiered classification, `interprets`
   the existing derived A≥3 structural gate (not a new claim), and carries
   status/caveat in `authorNotes`, not prose.

3. **Re-label the v9 script** docstring as `EXPLORATORY shape-probe` per
   discipline §Step 7 (it currently reads as a result-bearing "breakthrough").
   Follow-up; out of scope for this branch unless owner asks.

---

## 7. Bottom line per the brief's questions

- **Is `(1+q)/2` derived or fitted?** → **Fitted.** Operationally defined as
  `target/baseline`, then name-matched to a 9-item menu; does not generalize.
- **How many symmetry combinations were tried?** → **≳ 175** against the single
  mirror target across v1–v9 (155 in v7–v9 alone).
- **Expected best-fit error by chance with that many tries?** → sub-percent
  matches are expected; a lone 0.11 % hit out of ~175 tries is **not evidence**
  of a structural identity.
- **Did Option-3 (absolute energies) generalize?** → **No** — 154 % max error,
  worse than without the factor. Confirms the 0.11 % was difference-specific.
- **Is m_π the canonical isospin scale here?** → m_π is a real isospin-breaking
  scale and the CAL-3 anchor, but here it is **imported as a dimensional
  multiplier**, not derived to be the correct coefficient of this difference.
