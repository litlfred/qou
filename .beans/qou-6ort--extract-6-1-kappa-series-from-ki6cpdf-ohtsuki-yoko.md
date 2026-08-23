---
# qou-6ort
title: Extract 6_1 kappa-series from ki6c.pdf (Ohtsuki-Yokota 6-crossing) — Ohtsuki-tower third-knot leg
status: completed
type: task
priority: normal
created_at: 2026-08-15T11:35:54Z
updated_at: 2026-08-21T15:39:08Z
---


## 2026-08-15 extraction pass (pypdf; library/ki6c/ki6c.pdf = Ohtsuki-Yokota,
## "Kashaev invariant of the knots with 6 crossings", 72pp)

WHAT THE PAPER SUPPLIES for 6_1 (mirror 6bar_1 convention; 6_1 values
are complex conjugates):
- Leading exponent: sigma(6bar_1) = 0.5035603... - i*1.08078...
  (Re = Vol(6_1)/2pi checked: 3.16396.../2pi = 0.5035603 OK)
- omega(6bar_1) = -0.52139... + i*0.071732...  (eq on p.15; omega^2
  relates to twisted Reidemeister torsion per their [22])
- EXACT saddle data (p.18-19): gluing equations (1-x)^2 = -x^3 y^2 z,
  1-y = x^2 y^2 z, 1-z = -xyz; z' quartic 2z'^4 - z'^3 - 2z'^2 + z' + 1
  = 0; numeric saddle x0 = 0.895123+i*1.55249, y0 = 0.17385+i*1.06907,
  z0 = 0.322042+i*0.15778 (t0,s0,u0 also given)
- Exact Hessian H0 (their eq 42) in x0,y0,z0.

WHAT IT DOES NOT SUPPLY: the kappa_i(6_1) numeric values — unlike the
5_2 paper (which tabulated kappa_1..kappa_4), here the higher
coefficients exist by Theorem 1.1 + Prop 2.6 but are not printed.

COMPUTE PATH (follow-on probe, session-scale): implement Prop 2.6's
formal Gaussian expansion on their explicit potential V-hat (2Li2(x) +
Li2(y) + Li2(z) + quadratic, p.19 eq 40) at the given saddle: Newton
from their numeric seed at 60 dps, then the order-hbar correction gives
kappa_1(6_1) — the Ohtsuki-tower third-knot rung. Cross-validate
machinery first on 5_2 against the published kappa_1(5_2).

## 2026-08-19 rescope — the machinery EXISTS; this is reuse, not build-from-scratch

Two corpus-greps changed the cost estimate and killed one phantom hazard.

**1. No κ symbol collision (a hazard I nearly recorded, then disproved).**
I suspected the corpus κ_n (`OhtsukiKappaVsCkSign.kappa1 = 11√3π/108`, cited
to [andersen-hansen2006]) might be the Andersen-Hansen *b*-tower — a different
object from Ohtsuki's ℏ-series κᵢ in ki6c, which would need a conversion step.
It is NOT: `docs/audits/2026-07-12-ohtsuki-higher-rungs-exact.md` line 22 states
the corpus tower is `log(1 + Σ κ_n^Oht ℏⁿ)` with **ℏ = 2πi/N**, and line 10 has
`κ₁ = [1/N] log J_N(4₁)`. Same object. So a 6₁ κ-series IS directly a
third-knot rung of the corpus tower — qou-6ort is correctly aimed.

**2. The extraction producer exists and is a template.**
`docs/audits/scripts/qbeta_ohtsuki_higher_rungs.py` computed 4₁'s κ₁..κ₄ to
36/30/25/19 digits at dps 220 by: direct `log_kashaev_4_1(N)` evaluation over
many N → `poly_fit_1_over_N` → `pslq_rational_multiple` against the real
cyclotomic subfield. The 6₁ job is the same pipeline with two substitutions:
  (a) the ⟨6₁⟩_N state sum (ki6c §3 gives the 3-variable potential
      V(t,s,u); the Kashaev sum is finite and directly evaluable) in place of
      the 1-variable 4₁ sum;
  (b) a DIFFERENT PSLQ recognition basis — 4₁'s parity pattern (odd n → ℚ·√3·πⁿ,
      even n → ℚ·πⁿ) is trace-field-specific to ℚ(√-3) and will NOT transfer;
      6₁'s field is the quartic 2z'⁴ − z'³ − 2z'² + z' + 1 (ki6c p.18).

**Validation gate before trusting any 6₁ rung**: ki6c prints ς(6̄₁) =
0.5035603... − i·1.08078... and ω(6̄₁) = −0.52139... + i·0.071732... to ~6
digits. The fit's leading terms must reproduce BOTH before any κ is read;
mirror/conjugation convention (the paper works with 6̄₁) must be pinned
explicitly, not assumed.

**Cost**: session-scale for the pipeline port + 4₁ re-validation; the 6₁ state
sum at the N needed for 4+ rungs is the compute risk (long-compute logging
discipline applies). NOT a from-scratch saddle-point/Feynman-diagram build,
which is what the previous note implied.

## 2026-08-19 — the ki6c saddle leg has been consumed; the κ-series has not

PR #5293 used this bean's ki6c extraction as one of three independent routes to
`r(6₁) = 4`, and proved the ki6c gluing quartic generates the SAME field as
DG §6's `x⁴−2x³+x²+3x+1` (exact witness in `ℤ[α]`). So the *saddle/field* leg of
the ki6c extraction is now spent and owned by `qou-gz37`.

**What remains here is distinct and still open: the κ-series itself.** `r` is a
rank (the R1 shadow); the κᵢ are the coefficients of Ohtsuki's ℏ-expansion of
⟨6₁⟩_N. Different objects. The rescope above (reuse
`qbeta_ohtsuki_higher_rungs.py`; new PSLQ basis; ς/ω validation gate) is
unaffected by #5293 and is now DOUBLY motivated: it is the perturbative input a
Borel/Stokes extraction needs, i.e. a step toward #5293's open item 1 (an
independent resurgence DT count for 6₁, which would turn `r = 4` into a test of
the DT correspondence). **Precision, so this is not over-sold: a κ-series is
NOT a DT count.** Stated that way on #5293 too.

## 2026-08-19 ATTEMPT — controls pass, gate fails, and the failure is the result

Built the pipeline (`computations/qbeta/qbeta_ohtsuki_sixone_kappa_series.py`).
It does **not** report a κ-series. What it establishes is a precise,
reproducible discrepancy that neither the transcription nor the evaluation can
be blamed for.

**Transcription of ki6c eq.(29) verified three ways:**
1. form 3 recovered from the *separately extracted* form 2 under the paper's
   own stated substitution `j→j+1, k→k+1`, factor by factor;
2. `⟨6₁⟩_2 = −9` exactly, and `det(6₁) = 9`;
3. **moduli, by an independent route**: `|(q)_j(q)_{N−j−1}| = N` exactly, so the
   exponential variation is only `1/(q)_i²·1/(q)_{j−i}·1/(q)_{k−j}`, whose max
   is `4Λ(π/6)/π = 0.6461318944`. ki6c p.20 independently computes
   `max Re V̂ = 0.646131`. **Seven-digit agreement.**

*Correction to my own method*: the form-3-vs-form-4 check I built first is NOT
independent — form 4 was derived here by applying the stated substitution, so it
validates algebra, not transcription. It is retained and labelled as such.

**Evaluation verified two ways**: an O(N²) two-convolution factorisation of the
`i≤j≤k` chain matches the literal triple sum to 1e-120, and `log|⟨6₁⟩_N|` is
bit-identical across dps 60 → 600.

**The discrepancy.** `(log|⟨6₁⟩_N| − (3/2)log N)/N` converges cleanly to
**≈ 0.5715** (0.5604 / 0.5663 / 0.5692 / 0.5705 / 0.5710 / 0.5713 at
N = 100…1400) where Theorem 1.1 + the volume conjecture — a *proved* result for
6₁ — require `Vol(6₁)/2π = 0.50356`. 13.5 % off in an exponential rate,
converged and precision-independent. The same pipeline on 4₁ converges correctly
to `Vol(4₁)/2π`, so the conventions (q = e^{2πi/N}, the N^{3/2} normalisation)
are right.

**Diagnosis.** Moduli confirmed ⇒ the residual freedom is **phases**, and the
cancellation from 0.6460 down to 0.5036 is exactly a phase effect. ki6c's form 1
carries index-dependent factors `q^{1/2+i}`, `q^{−1/2−i}`, `q^{−1/2+k}`,
`q^{−1/2−k+1}` which cancel to `q^0` only if read exactly as printed, and the
OCR of form 1 is badly mangled. Most likely a dropped or misread
index-dependent q-power in the simplification to form 3.

**NOT tuned.** No formula variant was searched for one that hits 0.50356 — that
would be fitting a transcription to its target and is exactly the move the
anti-fit discipline forbids.

**Next step** (not a parameter hunt): a clean source for eq.(29) — the published
version rather than this OCR — or Ohtsuki's 5₂ paper, whose analogous sum would
validate the whole pipeline end-to-end against a knot with published κ values.
The O(N²) evaluator, the fit, the branch unwrapping and the gate are all built
and reusable the moment the sum is right.

## 2026-08-19 SECOND PASS — the convention mismatch is PROVED

First pass *inferred* "the phases are wrong". Now established, by a
font-metadata PDF extraction (`visitor_text`, which exposes superscripts the
flat text layer silently drops — that is how the `q^{-1}` prefactor of eq.(29)
got confirmed too):

**ki6c eq. (4) is `(q)_n (q)_{N-n-1} = N`, exactly** — read character by
character, nothing rendered outside the band. The STANDARD Pochhammer
`P_n = ∏(1-q^j)` **violates it**: `P_n·P_{N-1-n}` has modulus exactly N but a
nontrivial phase for every n ≥ 1 (N=7, n=1 → −4.364−5.473i, not 7), since
`P_n·P_{N-1-n} = N·(−1)^{N−1−n}·q^{(N−1−n)(N−n)/2}`.

**⇒ the paper's `(q)_n` is NOT the standard q-Pochhammer.** No longer a guess
about a dropped character; forced by an identity the paper states and the
standard object fails. With `(q)_n = P_n·c_n`, `|c_n| = 1`, eq.(4) gives ONE
constraint `c_n c_{N−1−n} = (−1)^{N−1−n} q^{−(N−1−n)(N−n)/2}`, which does not
determine `c_n`. **The convention must be READ, not solved for.**

Two principled evaluations, both reported, bracketing the target:
  standard Pochhammer throughout ................ 0.5715
  eq.(4) used for the two reflected pairs ....... 0.398
  required (Thm 1.1 + proved VC) ................ 0.50356
Opposite sides, consistent with the true `c_n` being an intermediate phase.
Both keep |⟨6₁⟩_2| = 9 = det(6₁), so that check cannot separate them. Only two
variants were run; more would be fitting a transcription to its answer.

**New measured precision hazard**: the eq.(4) variant needs dps ≥ 200 — at
dps 60 it silently returns 0.475 at N=1000 where the converged value is 0.3980
(identical at dps 200 and 400). The original variant is dps-stable from 60.
Dropping the reflected-pair phases makes the cancellation far worse, so a
precision setting adequate for one variant is NOT adequate for the other.

**NEXT STEP (a read, not a hunt)**: ki6c §2.1 defines `(q)_n` via a
quantum-dilogarithm/integral presentation `exp(φ(…) − φ(…))`; its OCR is
mangled and the font-metadata pass did not recover it either. A clean §2.1
determines `c_n` and closes this. Everything else — O(N²) evaluator, fit,
branch unwrapping, gate — is built and correct.

## 2026-08-19 THIRD PASS — THE DEFECT IS FOUND: a dropped OVERLINE

Ohtsuki's 5₂ paper is **in the library** (`library/104171-qt-83/`, = ki6c's
ref [20]) and its PDF is far more legible. It settles the convention:

    eq.(3):   (q)_n · (q̄)_{N−n−1}  =  N        ← BARRED second factor
    p.10:     (q)_n = exp(φ(1/2N) − φ((2n+1)/2N))
              (q̄)_n = exp(φ(1 − (2n+1)/2N) − φ(1 − 1/2N))
    p.7:      R_ijkl = N q^{−1} (q)_{[i−j]} (q̄)_{[j−l]} (q)_{[l−k−1]} (q̄)_{[k−i]}

Two DIFFERENT functions, alternating through the R-matrix. Verified
numerically: `(q)_n · conj((q)_{N−1−n}) = N` **exactly, to 1e-40, all n, all N**.

**So my `(q)_n` was right all along.** The defect is that ki6c eq.(29) contains
`(q̄)` factors and **the OCR silently dropped every overline** — LaTeX sets
`\overline{q}` as a *rule*, not a glyph, so it is invisible to `extract_text`,
to layout mode, AND to the font-metadata `visitor_text` pass (which does recover
superscripts and minus signs). Three extraction methods, none can see a bar.

**This explains the exact signature measured in pass 1**: bars leave every
modulus untouched (`|(q̄)_n| = |(q)_n|`) — which is why the transcription
reproduced ki6c's `max Re V̂ = 0.646131` AND its location `t₀=s₀=u₀=1/6` — while
changing every phase, which is precisely where the 0.6460 → 0.5036 cancellation
lives. Pass 1 said "moduli right, phases wrong"; this is the mechanism.

Also note ki6c eq.(4) as I read it (`(q)_n(q)_{N−n−1} = N`) is the SAME identity
with the bar dropped — my pass-2 conclusion "the paper's (q)_n is not the
standard Pochhammer" was **wrong, and is retracted**: it is standard; the
*second* factor was barred.

**Readings tested (3) — and stopped deliberately.** Unbarred → 0.5715;
eq.(4)-substituted → 0.398; eq.(4) + `(q)_i(q̄)_i = |(q)_i|²` (supported by Ṽ's
`φ(t) − φ(1−t)` pairing) → ~0.449 and still rising at N=700. None reaches
0.50356. Continuing to permute bars until one matches would be fitting a
transcription to its target; stopped.

**THE CLEAN PATH, now concrete**: transcribe the **5₂** sum from
`library/104171-qt-83` where the bars ARE legible (they render as an 'N' glyph
in that PDF's encoding: `.Nq/`), and validate end-to-end against its published
`ς = 0.4501096100… + i·0.4813049796…` (Re = Vol(5₂)/2π ✓) and
`ω = 0.0901905774… − i·0.6499757866…`. That is a real test with a published
answer. Only then apply the same bar pattern to 6₁.

**CORPUS-WIDE HAZARD worth propagating**: flat PDF text extraction silently
drops overlines/bars. The library holds 332 PDFs that agents grep. Any
transcription of a formula containing `q̄`, `z̄`, `Ā`, a complex conjugate or a
closure will come out WRONG-BUT-PLAUSIBLE — moduli intact, phases destroyed —
and will pass determinant-style sanity checks. Worth a line in the corpus-grep
discipline.

## 2026-08-21 SOLVED — κ-series measured, validated end-to-end

The bars are restored and the κ-series is out. Route: Ohtsuki's 5₂ paper
(`library/104171-qt-83`) prints eq.(7) with the bars LEGIBLE:

    ⟨5₂⟩_N = Σ_{0≤j≤i<N} N³q / [ (q)_i (q)_{N−i−1} · (q)_j(q̄)_j · (q̄)_{i−j} ]

That yields a bar RULE — doubled index → (q)(q̄) = |·|²; difference index →
barred; reflected pair (q)_m(q)_{N−m−1} → both unbarred — and, applied to
ki6c eq.(29), gives 6₁'s rate converging to 0.50356 where every earlier
reading missed.

**Validated end-to-end on 5₂ against PUBLISHED values before 6₁ was touched:**
    fitted ς(5₂) = 0.45010961002522 + 0.48130497966592i   |Δ| = 7.06e-11
    fitted ω(5₂) = 0.090190577405664 − 0.64997578664241i  |Δ| = 4.28e-11

**6₁ gate PASSES:**
    ς(6₁) = 0.5035603876377462 + 1.080780076864617i   vs ki6c |Δ| = 1.17e-7
    ω(6₁) = −0.5213883634451721 − 0.07173228265342455i vs ki6c |Δ| = 1.66e-6
Re(ς) = 0.5035603876 = Vol(6₁)/2π independently ✓. |⟨5₂⟩_2| = 7, |⟨6₁⟩_2| = 9 ✓.

**Mirror frame resolved BY MEASUREMENT, not assumption** (the ambiguity flagged
at the outset): the branch guide is run in both conjugations and the
self-consistent one kept — 7.7e-8 vs 30.85. My sum computes the UNBARRED ⟨6₁⟩,
whose ς, ω are the conjugates of the paper's 6̄₁ values.

**κ_i(6₁), ℏ = 2πi/N, in the 6̄₁ frame:**
    κ₁ = −0.857036577786166099 + 0.0996113097156072094i
    κ₂ =  0.358255042584737923 − 0.0945323841291178526i
    κ₃ = −0.0950597684808133093 + 0.0432714333144021833i
    κ₄ =  0.0183530121695171879 − 0.0131501497029207267i
    κ₅ = −0.00271366861525603234 + 0.00466421458693848123i

**SCOPE — these are NOT DT counts.** They are the perturbative coefficients of
the asymptotic expansion; the DT/Stokes constants need a Borel resummation this
probe does not do. This is the *input* to `qou-btvl`'s open item, not the item.
No PSLQ recognition attempted yet: unlike 4₁ (ℚ(√−3), parity-split basis), 6₁'s
trace field is the quartic and the right basis is not obvious — a separate step.

NEXT: (a) more rungs / higher N for PSLQ-grade precision; (b) the Borel/Stokes
step that turns these into DT constants and tests R1's {5} vs the {5,10} guess.

## Note from a passing agent (2026-08-21) — the witness declares `independent` with no reason

Not claiming this bean; flagging one field so it gets fixed at the
producer rather than by someone patching the witness behind you.

`qbeta-ohtsuki-sixone-kappa-series.witness.json` (landed `ae1d692cc6`)
carries `q0Anchor: "independent"` with no `q0AnchorReason`, so
`q0_anchor_consistency_audit` scores it `Q0_INDEPENDENT_NO_REASON`. The
audit requires the reason because otherwise a reader has to re-derive the
producer's import cone to check the claim.

The fix is one line, `qbeta_ohtsuki_sixone_kappa_series.py:406`:

```python
    wb.save({"q0Anchor": "independent"})
    # ->
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": "…why no substrate pin is read…",
    })
```

Deliberately **no** `q0Value` — the audit reads a value alongside
`independent` as a contradiction, since it would mean something did
supply a pin.

The token itself looks right from here (a kappa-series extracted from
ki6c, symbolic in q, no substrate anchor) — it is the justification
that is missing, not the classification. I did not patch the witness,
because your next producer run would overwrite it.

Context: PR #5312 drained this class 2 -> 0 earlier today; this one
landed after. Count is back to 1.

### Second defect in the same producer — an import-time `mpf` literal

Surfaced by `scripts/precision-gates.sh` during an unrelated merge-prep
run. `mpf_import_time_dps_audit` reports:

```
NEW files (not baselined) : 1
  literal=1   computations/qbeta/qbeta_ohtsuki_sixone_kappa_series.py
  L166: mpf('3.163963228883143983991757529167384812325703962')  [literal]
```

The string spelling is right — `mpf('...')` is the correct way to keep a
constant out of float64 — but the **evaluation point** is wrong. This is
at module scope, so it runs at IMPORT time, before `set_compute_dps()`.
mpmath parses it at whatever `mp.dps` is then (default 15), so those 46
digits are truncated on the way in. The literal *looks* precise and the
value is not.

Fix: move the construction inside the function that uses it (after the
dps is set), or wrap it so it is built lazily. Do not add the file to
`raw-float64-baseline.json` — AGENTS.md is explicit that baselines drain
and never grow.

Counts, for whoever fixes it:

```
files_with_findings  14 -> 15
literal_findings      0 -> 1
new_not_baselined     0 -> 1
```

Not fixed here for the same reason as the anchor field above: this is
your in-progress bean and your next producer run owns both.
