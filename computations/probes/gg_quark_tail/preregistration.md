# Pre-registration: which quark tails does γγ + reading 3 admit?

Written and committed **before** any diagnostic was computed. Beans `qou-ales` (option 4,
"derive it, do not pick it", owner 2026-10-12) and `qou-99qc`; follows `qou-ggls` (PR #7876).
Owner request 2026-11-15: "work the tail".

## 0. What is already known (not re-derived here)

- `gg_quark_letters_parity` (#7781): no rule built from the γγ vertex V, the core V³ or their
  Jones-pair closures fixes the flavour sign map or the letter placement at n = 3. The γγ
  construction names no flavour.
- Stream 11 (branch `claude/corner-doublet-vs-flavour-2026-11-15`): the n = 4 corner doublet is
  not flavour (σ₃⁻¹ acts as σ₃ − h·I, a central shift).
- The owner's selection rule (`qou-ales`, 2026-09-08) is γγ production **plus** the confinement
  test at q₀. The test is reading 3, applied at every tower level (owner 2026-10-11, option 3);
  on three-strand families this coincides with H₃ (#7702 × #7733 fold-in).

So this probe asks the question the construction leaves to the test: which tails does reading 3
admit, given a γγ core and gluon?

## 1. Space (finite, fixed in advance)

- Letter alphabet A, six letters, the γγ-produced crossings on each generator g ∈ {0, 1}:
  σ_g (through parity q), σ_g⁻¹ = σ_g − h (parity q⁻¹), and the bar-fixed average
  ½(σ_g + σ_g⁻¹) = σ_g − h/2 (parity [2]/2). These are exactly the letters R1, R2 and R4 of #7781
  produce, and the letters of every #7718 template.
- Tails T = ℓ₁ℓ₂ℓ₃ with ℓᵢ ∈ A: 6³ = 216 tails.
- Elements W(T, G) = CORE · T · G, CORE = V³, V = σ₀σ₁⁻¹, with two gluon segments:
  G = V (the γγ survivor, k = 1, `qou-ggls`) and G = σ₀² (the current element's gluon).
  432 words in all. Nothing outside this space is evaluated.

## 2. Test and readouts

- Reading 3 at H₃, convention D, proton pin q₀: χ_(3)(W) ≥ 0 and χ_(2,1)(W) ≥ 0
  (y_(1³) = 0, so χ_(1³) carries no weight). Same formulas as `gg_gluon_segment_probe.py`.
- For each word also report the real roots of χ_(2,1) in (1, ∞) (exact, sympy real_roots), so the
  verdict's dependence on q is visible.
- Counted and reported: survivors per gluon; whether the census tails TAIL_p, TAIL_n survive;
  how survivors split under the generator flip φ (σ₀ ↔ σ₁) and the letter-wise bar involution.
- Not used to choose anything: Q_β, trace differences, comparison with data. No survivor is
  labelled proton or neutron: reading 3 does not read flavour, so that assignment stays open.

## 3. Calibration (must pass before results are reported)

- C1. The census tails with G = σ₀² reproduce χ_(2,1) = −0.2805933509 (p) / −0.3719563247 (n).
- C2. The census tails with G = V reproduce +0.2170281485 (p) / +0.4294149854 (n) (`qou-ggls`).
- C3. χ_(2,1) from the explicit seminormal 2×2 representation equals the trace formula on 20
  randomly chosen words of the space (fixed seed 0).

## 4. Outcomes, stated in advance

- (i) Exactly one tail survives (up to a symmetry stated in the results): reading 3 fixes the tail
  shape; flavour assignment remains open.
- (ii) Several survive: the test does not fix the tail; report the family.
- (iii) None survives: the γγ core + gluon admit no tail in this alphabet.

Scope (a): this alphabet, H₃, the proton pin.
