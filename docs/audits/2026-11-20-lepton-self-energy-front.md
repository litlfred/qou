# Lepton self-energy front: the muon carrier read as the 4₁ Kashaev saddle

**Date:** 2026-11-20 · **Bean:** `qou-6gf9` · **PR:** #8573 ·
**Owner instruction (2026-11-20):** open the lepton self-energy front, Lean-first;
CAL-2 stays unchanged for now.

**Lean:** [`QOU/BraidKnot/MuonKashaevReading.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidKnot/MuonKashaevReading.lean)
(sorry-free; `lean -DautoImplicit=false -s 65536` exit 0 against the restored
Mathlib olean tree; `#print axioms` on every capstone = `[propext,
Classical.choice, Quot.sound]`). Mathlib-only imports, so no QOU import cone.
**Probe:** [`computations/probes/mu_kashaev_reading_probe.py`](../../computations/probes/mu_kashaev_reading_probe.py)
→ `mu-kashaev-reading.witness.json` (mpmath 70 dps, no float64, 4/4 assertions).

## Verdict

**The "Kashaev limit" reading of CAL-2 does not supply the μ–p correction, and
it fails on SIGN, not merely on size.** Read literally, `m_μ/m_e = Vol(4₁)/ℏ_q²`
is the leading term of the 4₁ Kashaev log-series at `N = 2π/ℏ_q² ≈ 640.02`. The
series then fixes every correction with no free coefficient. Every derived term
except one constant is **positive**, their sum is **+4.555 × 10⁷ ppb** on `m_μ`,
and the measured residual needs the carrier to go **down** by 211 ppb.

Scope **(b)** for the class *"`m_μ/m_e` is a finite truncation of the 4₁
Kashaev log-series at the forced `N`, with non-negative Ohtsuki rungs"*. Named
invariant: the sign of the one-loop term, `log 3 < 6·log 2`, proved in Lean
(`two_thirds_lt_one_loop_4_1`). The measured sign of the residual enters the
capstone as the hypothesis `hr`; it is a measurement, not a theorem.

**No derived term of the needed size and sign was found. GAP stays open.**

## 1. What the muon object is in the corpus

| item | where | status |
|---|---|---|
| the relation `m_μ/m_e = Vol(4₁)/ℏ_q²` | `knots-particles-confinement/figure-8-muon-mass-cross-check.md`; CAL-2 in AGENTS.md | **calibration identity**, not derived. The block says so: the 50-dps residual is "equality by construction … not a falsifiability test". |
| "Kashaev limit" wording | `mass-theory/lepton-mass-tower-canonical.md`, `braids-and-knots/figure-eight-muon-anchor-reading.md` | asserted in prose; no derivation of the `ℏ_q²` power from the Kashaev series exists anywhere I searched. |
| knot identity | `figure-8-muon-mass-cross-check.md` | the block itself says the 4₁ is the "Higgs knot" whose volume the muon **proxy** evaluates, and the muon's identity knot is `T(2,5)`. See `2026-05-24-muon-knot-id-conflict.md`. So "the muon IS 4₁" is not a corpus fact; "the CAL-2 proxy uses `Vol(4₁)`" is. |
| 4₁ Kashaev series data | `2026-07-12-ohtsuki-higher-rungs-exact.md`, `2026-07-12-kappa5-exact-identification.md`; Lean `AlgebraicSubstrate/OhtsukiKappaDependence.lean` (κ₁, κ₂) | κ₁…κ₅ exact by PSLQ (19–40 digits), **not** Lean-proved. |
| one-loop / torsion | held source **`[murakami-h2011]`** (H. Murakami, *The colored Jones polynomial, the Chern–Simons invariant, and the Reidemeister torsion*, `library/arxiv-1102.3530v1`), Thm 1.2 quoting Andersen–Hansen | `J_N(4₁; e^{2πi/N}) ∼ 3^{-1/4} N^{3/2} exp(N·Vol/2π)`; torsion `2/√−3`; CS invariant `i·Vol`, i.e. `CS(4₁) = 0`. |

Prior work on this exact front (bean `qou-6gf9` body; `2026-08-08-mu-p-residual-carrier-order-and-bar-parity-prune.md`):
the monomial order window `k ∈ {6,7}` in `ℏ_q`, the bar-even `w`-tower
exclusion, the two-term sum narrowing, and the Σ(2,3,5) Ohtsuki least-term
closure. That audit pruned *"a 1-loop volume-conjecture term at order `ℏ_q`"*.
It did **not** examine the reading in which the Kashaev parameter is `ℏ_q²`,
where the one-loop term is a **logarithm**, not a monomial — so the order
window does not cover it. That is the gap this audit fills.

## 2. Lean (formalize-first, landed before the probe)

`MuonKashaevReading.lean`:

| declaration | content | base ring |
|---|---|---|
| `leading_match_forces_hbar_sq` | `V/ℏ_K = V/ℏ_q²`, `V ≠ 0` ⇒ `ℏ_K = ℏ_q²`. The reading is not free: `ℏ_K = ℏ_q` would give leading term `≈ 20.5`. | generic `[Field K]` |
| `leading_term_eq` | `(2π/ℏ_K)·V/(2π) = V/ℏ_K` | ℝ |
| `kashaevTrunc` | `N·V/2π + (3/2)log N + c₀ + Σ_{n=1}^m κ_n/N^n` (def) | ℝ (log) |
| `kashaevTrunc_sub_leading_ge` | `N ≥ 1`, rungs ≥ 0 ⇒ truncation − leading ≥ `(3/2)log N + c₀` | ℝ |
| `one_loop_4_1_gt`, `two_thirds_lt_one_loop_4_1` | `c₀ = −(1/4)log 3`, `N ≥ 2` ⇒ one-loop `> log 2 > 2/3` | ℝ |
| `kappa_4_1`, `kappa_4_1_nonneg` | κ₁…κ₅ closed forms are ≥ 0 | ℝ |
| `kashaev_reading_gap` | truncation `> V/ℏ_q² + 2/3` at `N = 2π/ℏ_q²` | ℝ |
| `kashaev_reading_excluded`, `…_4_1` | if `r < V/ℏ_q²` then `r ≠` any such truncation | ℝ |

The asymptotic expansion itself is **not** asserted as a theorem. The theorems
are about the truncations, which is all the exclusion needs; the expansion is
cited (`[murakami-h2011]`) and its numerical validity at this `N` is checked in §3.

## 3. Measured (proton pin, 70 dps, NO adjustment)

Datum: `ℏ_q = 0.0990817160442585…`, carrier `206.76832637067389`, CODATA 2022
`206.7682827 ± 0.0000046` ⇒ residual **+211.206 ppb (9.4936 σ on the ratio)**;
the carrier would need to move by **−4.3671 × 10⁻⁵** absolute.

`N_eff = 2π/ℏ_q² = 640.018943965708` (not an integer — see §5).

| derived term at `N_eff` | absolute shift of the ratio | ppb on `m_μ` | cumulative ppb |
|---|---|---|---|
| `(3/2)·log N` | +9.692246664 | +46 874 909.9 | +46 874 909.9 |
| `−(1/4)·log 3` (torsion/prefactor) | −0.274653072 | −1 328 313.1 | +45 546 596.8 |
| `κ₁/N` | +8.65938 × 10⁻⁴ | +4 187.96 | +45 550 784.8 |
| `κ₂/N²` | +1.78476 × 10⁻⁶ | +8.6317 | +45 550 793.4 |
| `κ₃/N³` | +1.0125 × 10⁻⁸ | +0.04897 | +45 550 793.4 |
| `κ₄/N⁴` | +7.80 × 10⁻¹¹ | +3.77 × 10⁻⁴ | — |
| `κ₅/N⁵` | +7.9 × 10⁻¹³ | +3.8 × 10⁻⁶ | — |

**Validation that this is the right expansion at this `N`.** The Kashaev sum
was computed exactly at the two integers bracketing `N_eff`:

| N | exact `log ⟨4₁⟩_N` | exact − series(κ₁…κ₅) | exact − leading |
|---|---|---|---|
| 640 | 216.1806231711227710 | +1.0000 × 10⁻¹⁴ | +9.418417 |
| 641 | 216.5060296826234837 | +0.9906 × 10⁻¹⁴ | +9.420758 |

The remaining gap is the κ₆/N⁶ scale (`676.9/640⁶ ≈ 9.85 × 10⁻¹⁵`), and it too is
positive. So at this `N` the series is not a formal object: it reproduces the
exact Kashaev invariant to 10⁻¹⁴, and the exact invariant sits **9.42 above**
its leading term.

**Effect on the muon `q₀` pin** (reported only; CAL-2 not changed). Bare CAL-2
muon pin is `+11.614 ppb` above the proton pin (the known μ–p tension). Replacing
CAL-2 by the truncation would move the muon pin by **+2.58 × 10⁶ ppb (+0.26 %)**
— it destroys the calibration rather than refining it.

**Multiplicative reading (NOT derived, for completeness).** No corpus artifact
supplies a reading in which the Ohtsuki series multiplies the mass. Under such a
reading with `ℏ_K = ℏ_q²` the rungs give relative `+8.66 × 10⁵`, `+1785`,
`+10.1`, `+0.078` ppb — again all positive. (Numerically these equal the
absolute shifts above, because `κ̃_n ℏ_K^n = κ_n/N^n`.) The first is already
excluded by the monomial order window (`k = 2` in `ℏ_q`).

## 4. Diagnostic comparison (last, and only as a diagnostic)

Needed: **−211.2 ppb**. Derived, in order: +4.69 × 10⁷, −1.33 × 10⁶, +4188,
+8.63, +0.049 ppb. No single term and no partial sum has the needed sign and
size. The one negative term is a constant `−(1/4)log 3`, 6 300× too large, and it
never appears without the positive `(3/2)log N`.

Two near-coincidences are recorded so nobody mistakes them for evidence: the
`κ₂/N²` term (+8.63 ppb) and the multiplicative `κ̃₃` term (+10.1 ppb) are of the
same order as the experimental σ on the ratio (22 ppb); both have the wrong sign and neither is selected by
anything. Per the 2026-08-08 entropy bound the datum carries ~1 significant
digit, so matching would carry no weight even if the sign were right.

## 5. What this does and does NOT exclude

Excluded (scope (b), class above): CAL-2 as the leading term of the 4₁ Kashaev
log-series at `N = 2π/ℏ_q²`, corrected by any finite truncation with
non-negative rungs. The 4₁ rungs κ₁…κ₅ are proved non-negative from their closed
forms; κ₆ is measured positive.

**Not excluded**, each a different object:

1. **The off-root-of-unity deformation.** `[murakami-h2011]` Thm 1.3 evaluates
   `J_N(4₁; e^{ξ/N})` at `ξ = 2πi + u`, `u` real, and the asymptotic is governed
   by the deformed Chern–Simons function `S(u)` and torsion `T(u)`. The substrate
   `q₀` is real, not a root of unity, so this is arguably the *better* home for a
   real deformation parameter. Nothing here evaluates it, and nothing in the
   corpus fixes `u` without a choice. Gap bean filed.
2. **A reading of CAL-2 that is not the Kashaev exponent.** The corpus never
   derives the `ℏ_q²` power. If the relation has a different origin, this audit
   says nothing about that origin's corrections.
3. **Non-integer `N`.** `N_eff = 640.019` is not an integer, and the Kashaev
   invariant is defined only at integer `N`. The series is a smooth function of
   `N` and the exclusion uses only the series, so this does not weaken §2; it does
   mean "the muon is the Kashaev invariant at level N" is not literally available.
4. **The tail beyond κ₆.** The theorem carries `κ_n ≥ 0` beyond `n = 5` as a
   hypothesis. At `N ≈ 640` the tail is below 10⁻¹⁴ absolute, so it cannot reach
   −4.4 × 10⁻⁵ in any case; the sign hypothesis is only needed for the clean
   statement.

## 6. Corpus-grep record

- Step 0 (`corpus_search` MCP) was **not available** in this session; paths 1–6 run by grep.
- Paths 1–4: `docs/audits` (Kashaev/Ohtsuki/κ₁/muon/mu-p), `folio/` (content + Lean),
  `computations/`, coordination ledgers via the cited audits. The `N = 2π/ℏ_q²`
  identification appears nowhere; the 2026-08-08 Ohtsuki prune used `ℏ_q`.
- Path 5: `library/*/sections` **and** `library/*/ocr` grepped for the
  Andersen–Hansen prefactor; found in `arxiv-1102.3530v1` (`[murakami-h2011]`,
  already registered in `folio/references/`).
- Path 6: `beans/defs` grepped for Kashaev × muon and for `N_eff`; the only
  `N_eff` hits (`qou-rm47`, `qou-n1dj`) are an unrelated Markov-parameter quantity.

## 7. Anti-recurrence

- Do not re-propose "the muon carrier is the leading Kashaev saddle and the μ–p
  residual is its first correction". At the forced `N` the first correction is
  `+9.42`, positive, and the exact invariant confirms it.
- Do not quote the `κ₂/N²` (+8.6 ppb) or multiplicative `κ̃₃` (+10.1 ppb) sizes as
  near-matches: wrong sign, unselected, inside a 1-digit datum.
- Do not change CAL-2 on the strength of this audit.
