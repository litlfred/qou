# Pre-registration: the gluon segment of the nucleon word by the γγ rule

Written and committed **before** any diagnostic was computed. Bean parent
`qou-99qc`; related `qou-ales`, `qou-z08b`, `qou-1qsw`. Task (owner-approved,
relayed 2026-11-15): "work Gluon: 1 (derive the gluon by the γγ rule), then 2 if
that doesn't give a unique word".

## 0. The object

The scored nucleon element `nuc11_interleaved` is, per nucleon, the 11-letter
H₃(q) word

    CORE · TAIL · GLUON,   CORE = (σ₀σ₁⁻¹)³,  GLUON = σ₀σ₀,
    TAIL_p = σ₀ · (σ₀ − h/2) · (σ₁ − h/2),  TAIL_n = (σ₀ − h/2)² · (σ₁ − h),

with σ⁻¹ = σ − h, h = q − q⁻¹ (letters as in
`computations/qbeta/qbeta_bar_parity_split_gap_probe.py`). Only the GLUON segment
is replaced in this probe. The CORE and the TAILs are held fixed exactly as
above. The quark tail is itself census-derived and owner-ruled to be derived
later (`qou-ales`, 2026-10-12, option 4); it is out of scope here.

## 1. Corpus-grep (six paths), what the corpus fixes and what it does not

Searched: `docs/audits`, `folio/` (whole tree), `computations/`,
`docs/coordination`, `library/INDEX.md` + `library/*/sections` + `library/*/ocr`
(no braid-word gluon rule; 0 INDEX hits, 60 section hits all particle-physics
prose, 0 OCR hits), and `beans/defs` (65 files mention "gluon"; read in full:
`qou-ales`, `qou-99qc`, `qou-z08b`, `qou-iagg`, and the relevant parts of
`qou-1qsw`).

**What the corpus fixes.**

- F1. **The γγ rule** (`qou-ales`, owner 2026-09-08; Lean
  `QOU/Mass/GammaGammaWordSelection.lean`): a γγ word is a concatenation of
  pair-production vertices `vertex i = σᵢσᵢ₊₁⁻¹`
  (`inductive GammaGammaWord`). On three strands (generators 0, 1) the only
  vertex is `vertex 0 = σ₀σ₁⁻¹ =: V`.
- F2. **The corpus gluon unit IS that vertex.**
  `QOU/StandardModel/ChiralFermionBraidWords.lean` and
  `WritheLevelParity.lean`: `gluonUnit = σ₀σ₁⁻¹`, `borromean = gluonUnit³`;
  `GammaGammaWordSelection.toCorpus_vertex_zero`: `vertex 0` is the corpus
  `gluonUnit` (sorry-free). So the CORE is three gluon units.
- F3. **σ₀² is not a γγ word.** `GammaGammaSelectedDeltaVanishes.gluonPair_not_gammaGamma`
  (no axioms). γγ words have writhe 0 and even length (`writhe_vertex`,
  `gammaGamma_length_even`); σ₀² has writhe +2.
- F4. **The corpus already carries a derivation of σ₀², but it is not the γγ
  rule.** Owner ruling 2026-08-30 (`qou-1qsw`; Lean
  `QOU/QBeta/GluonVertexPsdParity.lean`, `vertex_psd_iff_even`): among powers
  σ₀ᵏ of the H₂ generator, literal PSD on H₂ holds iff k is even, and σ₀² is the
  minimal non-zero one. That rule ranges over σ₀ᵏ only (a one-generator H₂
  alphabet), does not force k > 0 ("whether the vertex is present at all stays
  open"), and is a reading-1 rule on H₂. So "σ₀² was picked from the census" is
  imprecise: it was picked by the H₂ parity rule over an alphabet the corpus
  chose. This probe does not touch that ruling; it applies the γγ rule instead,
  as asked.
- F5. **The crossing budget 11 = 6 + 3 + 2** (`qou-1qsw`,
  `sdp_gamma_gamma_to_qqbar.py` four-component decomposition, H₂ gluon
  component of 2 letters). The 2 comes from F4.
- F6. **Minimal non-zero reading-3 γγ word on H₃ is V³** (`qou-ales` step 3,
  #7192/#7207, `GammaGammaSelectorH3`/`frobeniusSelected_borromean`): that is
  how the CORE was selected.
- F7. **The retired 9-crossing convention**: `build_nucleon_nf`'s old docstring
  "B₃ IS the gluon structure" (no separate gluon). Retired by the owner
  2026-08-30 (`qou-1qsw`). Recorded only as a corpus-named member, not as a live
  rule.

**What the corpus does not fix.** No corpus artifact states that the gluon
segment must be a γγ word, nor how many γγ vertices it carries. The γγ rule
fixes the **letter content of a unit** (F1 + F2: V, unique on three strands),
not the **number of units** in a separate gluon segment. There is no
"gluon = γγ exchange" rule and no Jones-pair closure rule for the gluon on
record (`gg_ntower` closures explicitly exclude gluons).

## 2. Derivation rule and its output (step 1)

Rule G (γγ rule applied to the gluon slot): the gluon segment is a γγ word on
the nucleon's three strands. By F1 the segment is `Vᵏ`, k ≥ 0. Output: the
**family** {Vᵏ : k ≥ 0}. Not unique.

Corpus side-rules that would each pick one member (listed, none adopted here):

| side rule | source | member |
|---|---|---|
| keep the 2-letter slot of the budget 11 | F5 | k = 1 (`V = σ₀σ₁⁻¹`) |
| the gluon is its own SDP component, selected like the core (minimal non-zero reading-3 γγ word on H₃) | F5 + F6 | k = 3 (`V³`) |
| no separate gluon (retired) | F7 | k = 0 |

These disagree, so step 1 does not give a unique word and step 2 runs.

**Structural note, stated before computing.** All three diagnostics below are
class functions (the Markov trace, the irreducible characters) or are built from
them, and the bar involution is applied letter by letter. `CORE·TAIL·Vᵏ =
V³·TAIL·Vᵏ` is conjugate to `V^{3+k}·TAIL` (and its letter-wise bar to the bar
of that). So every diagnostic depends on k only through m = 3 + k, and the
placement of the segment before or after the tail is not a degree of freedom.
This is checked numerically (check P1 below), not assumed.

## 3. Step 2 enumeration space (pre-registered in its own commit, before computing)

Elements `E_k = CORE · TAIL_x · Vᵏ`, x ∈ {p, n}, with **k ∈ {0, 1, 2, 3}**.
Bound: k ≤ 3 is the largest member any corpus side-rule names (F6 gives k = 3);
k = 2 is included because it lies between named members. Four elements per
nucleon; nothing outside this space is evaluated. The γγ condition holds for
every member by construction (the gluon segment is a γγ word). The reading-3
condition (whole word, both nucleons) is then evaluated and the survivors are
counted. All four are reported with all diagnostics, in k order. No ranking.

## 4. Calibration checks (must pass before any diagnostic is reported)

- C1. `computations/qbeta/qbeta_bar_parity_split_gap_probe.py` reruns 24/24.
- C2. With this probe's own code on `nuc11_interleaved` (GLUON = σ₀σ₀):
  f = tr^{z_D}(n) − tr^{z_D}(p) equals the recorded closed form
  `(q²−1)(q⁴+1)P12/(4q⁷(q²+1)²)`; f = h·g; g_odd = −h[2]_q(q²+q⁻²)/8 exactly.
- C3. At the proton pin: Δ trace = −0.1541948850472397056592555 (recorded
  `tr_conv_D`); Q_β = |Δ trace|·E₀ with `E₀ = qbeta_e0.canonical()` equals the
  dashboard scored cell 0.65185631006 MeV.
- C4. Reading-3 machinery: y_(3) + 2y_(2,1) = 1, y_(2,1) ≈ 0.2473, y_(1³) = 0
  at z_D; χ_(2,1)(1) = 2; χ_(3)(Vᵏ) = 1; χ_(2,1)(V³) ≈ +1.9942 (core admitted).
  On `nuc11_interleaved`: χ_(3) = 1.38249446339 (p) / 1.1221068216 (n);
  χ_(2,1) = −0.2805933509 (p) / −0.3719563247 (n); reading-1 block determinants
  (2,1): −1.02197249381 (both); (1³): −0.739223570776 (p) / −0.910762214553 (n).
- C5. Independent route: an explicit 2×2 seminormal (2,1) representation of
  H₃(q) built from σ₀ = diag(q, −q⁻¹) and a σ₁ solved from the braid and Hecke
  relations; its trace equals the trace-formula χ_(2,1) exactly (symbolic) on
  every word evaluated.
- P1. The structural note: diagnostics of `CORE·TAIL·Vᵏ` equal those of
  `V^{3+k}·TAIL` exactly.

## 5. Diagnostics per element (consequences only)

- (a) Bar parity of g. f = tr^{z_D}(n) − tr^{z_D}(p) = h·g with g the context
  trace from the n − p letter telescoping (same construction as the R2 route of
  the bar-parity-split probe). Report g_odd = (g − ḡ)/2 exactly and whether it
  is 0.
- (b) Reading 3 on the whole word, both nucleons: χ_(3) ≥ 0 and χ_(2,1) ≥ 0
  (y_(1³) = 0, so the alternating block does not bind). Report χ_(2,1) exact
  rational function and its value at the proton pin, plus χ_(3). Also report the
  reading-1 (2,1) and (1³) determinants for comparison only (reading 1 is
  parked).
- (c) Q_β at z_D: |tr^{z_D}(n − p)|·E₀, E₀ = `qbeta_e0.canonical()` (the
  tower-summed E₀ = 4.22748335562903 MeV), and its percentage against CODATA
  `Q_BETA_MEV`. Reported as a number only.

## 6. Hard rules

- Never filter, rank or choose by bar parity, Q_β or any residual. The only
  filter in step 2 is the ruled reading-3 condition, and every member is
  reported whether it passes or not.
- The gluon segment is not dropped and not mirrored (σ₀⁻² or V⁻¹) — no corpus
  rule requires either. k = 0 is a member only because F7 names it.
- No dashboard re-score; `per_observable_100x_status.py` and its witness are not
  touched (`qou-iagg`).
- Exact arithmetic over ℚ(q) (sympy) for every verdict; the proton pin is
  substituted as an exact rational of `Q_50_DIGIT_STR`; mpmath at 60 dps for
  display. No float64.
