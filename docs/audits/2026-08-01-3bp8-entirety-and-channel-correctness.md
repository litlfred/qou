# qou-3bp8: the winding GF is entire, and the A_ω channel is σ₁σ₂ — a channel-correctness audit

**Date:** 2026-08-01 · **Axis:** ϑ_K gap (`qou-qnnq`, route 2b `qou-3bp8`) · **Tier:** structural (Lean) + measurement (scope-(a)).
**Nothing fitted; nothing wired; the T5 `A_ω` field is untouched.**

Probes: [`qbeta_3bp8_annihilator_continuation_probe.py`](../../computations/probes/qbeta_3bp8_annihilator_continuation_probe.py)
(W1) · [`qbeta_3bp8_w2_direct_sheet_probe.py`](../../computations/probes/qbeta_3bp8_w2_direct_sheet_probe.py)
(W2) · [`qbeta_3bp8_sigma12_substrate_probe.py`](../../computations/probes/qbeta_3bp8_sigma12_substrate_probe.py)
(channel audit).
Lean: [`WindingGFTransform.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/WindingGFTransform.lean) (sorry-free).

## 1. The winding generating function is entire on ℂ* (Lean-proved)

The route opened as a **continuation** problem: #4433 reported the winding sum
`F(w) = Σ_e I₄₁(0,e)(q̃)·wᵉ` had radius of convergence 1, putting the corpus
sheet outside it. That reading was **pre-asymptotic** — its window stopped at
e ≤ 28, on the plateau. The leading q̃-power of `I(0,e)` grows quadratically
(`lead(e) = T(⌈e/2⌉) ≈ e²/8`), forcing super-exponential decay past the hump:

| e | 28 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|
| I(0,e)(q̃_sub) | −8.3·10⁻² | 2.0·10⁻⁵ | −2.1·10⁻¹⁶ | −3.5·10⁻³² | 1.9·10⁻⁵³ |

Machine-checked consequences (`WindingGFTransform.lean`):

- `summable_sq_dominated_nat` — `A·ρ^{n²}·Rⁿ` is summable for **any** `R`.
- `summable_winding_of_sq_dominated` — a two-sided family with
  `|c_e| ≤ A·ρ^{(natAbs e)²}` is absolutely summable against `wᵉ` at **every**
  `w ≠ 0`: the winding GF is **entire on ℂ\***.
- `gf_three_term` — the DGG eq (C.7) annihilator (carried as the
  content-bearing conditional class `FourOneIndexAnnihilated`; its 10-term
  expanded form cross-checked to 1e−71 against the composed operator)
  transforms into an exact three-term functional equation for the `F_m`.
- `gf_three_term_of_sq_dominated` — capstone: with square-dominated rows the
  relation holds among the `tsum`s at every `w ≠ 0`, `HasSum` hypotheses
  discharged by entirety.

**So the continuation ladder is unnecessary**: the corpus sheet is reached by
direct summation. The W1 probe's A1 leg independently re-certifies the
annihilator at the substrate (residual 6.6·10⁻¹⁵, dropping ×8.5·10¹² when the
internal order rises 1600 → 2400 — truncation-limited, not structural).

## 2. Channel-correctness: A_ω lives in σ₁σ₂, the x-refinement in σ₁σ₁

**This is the load-bearing correction of this audit.** The T4/T5 chain's
`A_ω = 3` is the **(1,2)** entry of the q→0 Stokes matrix (GGM 2012.00062
eq 60: `S⁺(0) = [[1,3],[0,1]]`). The winding x-refinement proven for 4₁
(Conjecture 4 / eq 21; GGM 2007.10190 eq 5/80) is a statement about the
**(1,1)** entry, whose w = 1 substrate value is 0.42764420 — *not* 3.

Therefore the qou-awpk and W2 winding results — the ϑ-dependence, the bar-odd
part, the sign flip, the Im-ratio −6.03 — are properties of **σ₁σ₁**, and
comparing them to `S(proton)/S(muon) = −4.0751` is a **cross-channel**
comparison. It demonstrates a *mechanism*; it does not measure `A_ω`.
The x-refinement of σ₁σ₂ is **not proven in the literature for 4₁** — that is
the honest gap between the winding programme and the corpus channel.

(W2's numbers stand as recorded: at the `q₀²e^{2iϑ}` sheet the σ₁σ₁ effective
coefficient acquires a genuine bar-odd part with a sign flip between the two
anchors, Im-ratio −6.03; at the `q₀e^{iϑ}` sheet no flip, +2.31. The
individual sign assignment is *inverted* relative to observation — absorbable
only by one global convention sign. Magnitudes 1.08 and 8.23 differ by 7.6×,
whereas the constant-A_ω picture needs them equal. All consistent with these
being a different matrix entry. Not wired.)

## 3. The σ₁σ₂ substrate measurement, and a ϑ-reality discriminator

Evaluating the OCR-free certified sandwich at the substrate (q̃-order 1600,
honest ladder guard, printed heads re-gated):

| entry | substrate value | agree-digits |
|---|---|---|
| S⁺₁₁ (σ₁σ₁) | 0.427644201317458 | 13 |
| **S⁺₁₂ (σ₁σ₂ ← A_ω)** | **1.585163662915485** | 13 |
| S⁺₂₁ | −0.302231058963111 | 12 |
| S⁺₂₂ | 1.218102118355424 | 12 |

The printed **ratio series** `S⁺₁₂/S⁺₁₁ = 3 + 9q̃ + 75q̃² + 642q̃³ + …` has
coefficients growing ~8.7×/order (radius ≈ 0.115) — it **diverges** at
q̃ ≈ 0.9009 and must not be summed. The meaningful object is the quotient of
the two convergent entry values:

$$
\left.\frac{S^+_{12}}{S^+_{11}}\right|_{\tilde q_{\mathrm{sub}}} = 3.70673484647288 \;=\; 1.2356 \times 3 .
$$

**The ϑ-reality requirement discriminates the two readings.** Substituting
each candidate into the T5 channel `S_K = A·κ·(ln²q₀ − ϑ²)` and solving for ϑ
at both anchors (κ = √3/4, ln q₀ = 0.104341 is the boost/spin divide):

| A | ϑ(muon) | ϑ(proton) | both real? | diagonal crossed? |
|---|---|---|---|---|
| 3 (T4 constant) | 0.0586 | 0.2031 | yes | yes |
| **3.7067 (substrate value-ratio)** | **0.0697** | **0.1883** | **yes** | **yes** |
| 1.5852 (substrate raw entry) | — (ϑ² < 0) | 0.2615 | **no** | — |

So the T4 structure survives the normalized reading and **breaks** on the
raw-entry reading.

**Sharpened by formalization (`ThetaRealityBound.lean`, sorry-free) — and the
first reading of this table was too generous.** Proving the two checks reveals
exactly what they constrain:

- **The diagonal crossing is worth nothing as evidence.** `S > 0 ⇒ ϑ² < ln²q₀`
  and `S < 0 ⇒ ϑ² > ln²q₀` hold for **every** `A, κ > 0` (`diagonal_crossed`).
  The crossing is *equivalent to the measured sign flip of S* and is
  independent of `A`. The T4 crux probe reported "diagonal crossed ✓" as a
  check; it is an identity. It supports no value of `A` whatsoever.
- **Reality is a one-sided lower bound.** `ϑ² ≥ 0 ⟺ A ≥ S/(κ·ln²q₀)`
  (`thetaSq_nonneg_iff`), binding only at the `S > 0` (muon) anchor — the
  `S < 0` anchor is automatically real for any positive `A`
  (`thetaSq_pos_of_neg`). Numerically `A_c = S_μ/(κ·ln²q₀) ≈ 2.054`, and the
  bound is monotone upward (`thetaSq_nonneg_mono`).

So the honest content of the table is `A ≥ 2.054`: it **excludes the raw entry
1.5852** and **admits both 3 and 3.7067 equally**. It does *not* select the
normalized reading over the integer — the audit's first phrasing ("selects a
reading") overclaimed. The independent reason to prefer the normalized form is
conventional, not numerical: GGM themselves print `S⁺₁₂/S⁺₁₁ − 3` (eq 62), so
`S₁₁`-normalization is the literature's own presentation of "the 3".

**Consequence for the T4 ϑ values.** They are convention-dependent at the
10–20% level (muon 0.0586 → 0.0697, +19%; proton 0.2031 → 0.1883, −7%). Any
downstream use of ϑ — including W2's own sheet evaluations — inherits that
uncertainty. Recorded, not resolved.

## Verdict

- **Proved (Lean, sorry-free):** entirety of square-dominated winding
  families; the annihilator ⇒ three-term GF functional equation; its validity
  at every `w ≠ 0`; unit-sheet bar-evenness.
- **Corrected (scope-(a)):** #4433's radius-1 / outside-the-annulus reading
  (pre-asymptotic); and the framing of the qou-awpk winding results as
  bearing on `A_ω` — they are σ₁σ₁, cross-channel.
- **Measured (scope-(a), on the correct channel):** the σ₁σ₂ Stokes entry has
  deformed at the substrate to 1.5852 raw / 3.7067 normalized; the normalized
  reading preserves the T4 ϑ-reality structure and the raw one destroys it.
- **Resolved (§4):** `A_ω = 3` is an exact, q-independent structure
  constant (`S₁₂ + S₂₁ = 3·S₁₁`, certified through q⁴⁰⁰, Lean-formalized);
  the corpus value is vindicated and the "deformation" question was
  ill-posed. Bean `qou-bbsy` re-scoped, not run as specified.
- **Open:** the x-refinement of σ₁σ₂ for 4₁ (not in the literature);
  deriving the integer 3 from the categorical drivers. `A_ω` stays as it is in
  production — a measurement is not a derivation.


## 4. W3 — `A_ω = 3` is an exact structure constant, and the corpus value is vindicated

Bean `qou-bbsy` asked for a self-consistent ϑ fixed point using the
winding-refined `A_eff(ϑ)`. **That was re-scoped rather than run**: `A_eff`
is σ₁σ₁ and `A_ω` is σ₁σ₂ (§2), so the fixed point as specified would have
hard-wired the very cross-channel error this audit diagnosed.

What the certified Stokes matrix actually satisfies — **exact integer
q-series identities**, coefficient-by-coefficient through q⁴⁰⁰
([`qbeta_3bp8_w3_stokes_symmetry_constant.py`](../../computations/probes/qbeta_3bp8_w3_stokes_symmetry_constant.py)):

$$
S^+_{12}(q) + S^+_{21}(q) = 3\,S^+_{11}(q), \qquad \det S^+(q) = 1 .
$$

The first is GGM's symmetry (eq 65). **It says the integer 3 is the
structure constant of an identity holding at every order in q — not the
value of any entry.** So there are three readings of "the 3", coinciding at
`q → 0` (where `S⁺(0) = [[1,3],[0,1]]`) and separating at the substrate:

| reading | at q̃_sub | q-dependent? |
|---|---|---|
| R1 raw entry `S⁺₁₂` | 1.5852 | yes |
| R2 value-ratio `S⁺₁₂/S⁺₁₁` | 3.7067 | yes |
| **R3 symmetry constant `(S⁺₁₂+S⁺₂₁)/S⁺₁₁`** | **exactly 3** | **no** |

Two independent discriminators select R3:

1. **The ϑ-reality bound excludes R1** (`A ≥ A_c ≈ 2.054`, §3).
2. **Truncation-invariance.** At a *pre-asymptotic* q-order 400, R1 and R2
   are meaningless (the honest guard reports 0 agree-digits; R1 reads
   −50836) while **R3 is already exactly 3**. A structure constant is
   truncation-invariant; an entry value is not.

Formalized sorry-free in
[`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean),
over an arbitrary field and index type: `symmetryConstant_const`
(the symmetry *forces* q-independence — it is not a numerical accident),
`readings_coincide_at_base` (why the `q → 0` data cannot distinguish them),
and the two separation criteria.

**Consequence.** The corpus's `A_ω = 3` is **vindicated**: read as the
Stokes symmetry constant it is exact, integral, and needs no substrate
correction — and the question this route opened with, "does `A_ω` deform at
the substrate?", was **ill-posed**. It also explains the T4 crux probe's
0.6% two-anchor consistency at `A = 3`: that is what an exact constant
looks like.

**Still open (unchanged):** deriving the integer 3 from the 13 categorical
drivers, and the σ₁σ₂ x-refinement for 4₁. The identification of `A_ω` with
the symmetry constant is a *reading selection* (reality exclusion +
q-independence), **not** a derivation of 3.

## Cross-references

- Beans: `qou-3bp8` (route), `qou-ovph` (domain re-scope), `qou-bbsy` (W3 fixed point).
- Corrected audit: [`2026-07-31-awpk-perwinding-stokes-41.md`](2026-07-31-awpk-perwinding-stokes-41.md) §Correction.
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
- AGENTS.md §"Before declaring refuted"; §"Axiomatization is NOT a Proof".
