# Pre-registration: the deuteron with a γγ-selected p-n bond

Written and committed **before** any number in this directory was computed. Bean `qou-xj4p`
(the deuteron log-law overshoot), `qou-ales` (γγ rule), `qou-brng`.

## Why

The log binding law `B = E₀·log(tr_free/tr_atom)` is canonical (owner 2026-11-25; Lean
`QOU.Nuclear.LogFormUniqueness`). Its deuteron value, +27.36 % vs AME, was computed on the
single-crossing interface letter `σ₂ + d_pn·1` of `atom_braid_word_3A`. The owner ruled on
2026-11-15 that the γγ selection rule covers bond letters, so that input is superseded and the
+27.36 % is a record, not a prediction. No γγ-selected p-n bond has been computed. This probe
computes one, in the cell the corpus already defines for H₂ (`../h2_gg_atom/`).

## What the corpus fixes

- γγ words are concatenations of `V(i) = σᵢσᵢ₊₁⁻¹`, no inverses (`QOU/Mass/GammaGammaWordSelection.lean`).
- A three-strand γγ nucleon is `Vᵐ`; only m = 3 and m = 6 pass reading 3 (`../h2_gg_atom/results.md`).
  Proton and neutron are then the same word, so this cell cannot tell a deuteron from a diproton
  or dineutron. That is a stated limitation, not a finding.
- Reading 3 at convention D, `z_D = q³/(q²+1)`, proton pin: `χ_μ(E_{n→m} W) ≥ 0` on every two-row
  μ ⊢ m with `y_μ > 0`, for every level m.

## Enumeration (nothing outside it is evaluated)

- 6 strands. Free word `x = Vᵐ (gens 0,1) · Vᵐ (gens 3,4)`, m ∈ {3, 6}.
- Bond `K ∈ {V(s)ᵏ : s ∈ {1, 2}, k ∈ {1, 2, 3}}`. s = 1 and s = 2 are the two γγ vertices that
  contain the junction generator σ₂; s = 0 and s = 3 lie inside one nucleon and are not bonds.
  Atom word `x·K`.
- Code: `../h2_one_rule/h2_one_rule_probe.py` helpers (`diag_of`, `V`, `y`, seminormal basis),
  N = 6, levels 1..6, mpmath 40 dps as in that base.

## What is reported, and the rules

- Per row: reading 3 pass/fail per level, the negative characters, the ratio
  `r = tr(xK)/tr(x)`, and `B = −E₀·ln r` with `E₀ = m_e/(q₀(q₀−1))` (order-zero, owner 2026-11-20).
- **Ruling B (2026-11-15): the trace drop is reported, never used to select.** A bond is selected
  only by passing reading 3 at every level, together with the bare `x` passing.
- **No fitting, no selection against AME.** If several bonds pass, all are reported; none is
  chosen by its binding. If none passes, that is outcome (ii) and is the result.
- Outcomes: (i) a γγ bond passes; its `B` is the γγ deuteron value in this cell. (ii) none passes.

## Calibration (must pass before results are read)

- K1: the bare nucleon `Vᵐ` on 3 strands reproduces `h2-gg-atom.witness.json`'s H₃ verdicts
  (m = 3, 6 pass).
- K2: for the production interface letter `σ₂ + d_pn·1` on the production free word, the ratio
  equals `z_D + d_pn` (the Markov property) to 1e-30.

## Addendum 1 (owner 2026-11-25: "need all strands"), committed before any of its numbers

The first run covered three-strand γγ nucleons and bonds `V(s)ᵏ` at two sites. This addendum
removes both limits. Same test (reading 3 at every level, convention D, proton pin), same
reporting rules (ruling B: trace ratio and `B = −E₀ ln r` reported, never used to select; no
selection against AME), same code base.

### Phase A: every γγ bond word on all six strands

- Free word `x = Vᵐ ⊗ Vᵐ`, m ∈ {3, 6}.
- Bond `K` = every γγ word on six strands, i.e. every concatenation of vertices `V(0)…V(4)`,
  of length 1 to L = 6 vertices (5 + 25 + … + 15625 = 19530 words), that contains at least one
  junction-crossing vertex (`V(1)` or `V(2)`). Words with no junction vertex are not bonds.
- Reported: the number that pass reading 3 at every level; for each passing word its ratio and
  `B`; the full distribution of ratios over the passing set. If the run time exceeds 2 h, L is
  lowered and the change stated.

### Phase B: flavoured nucleons on four strands, all eight strands kept

- A nucleon is a γγ word on its own four strands (vertices `V(0), V(1), V(2)`), length 1 to 6
  vertices, that passes reading 3 at every level on four strands. Proton and neutron can now be
  different words. **Which word is the proton and which the neutron is not determined by the
  corpus**, so every ordered pair (w₁, w₂) of passing nucleon words is evaluated; none is chosen.
- Deuteron on 8 strands: `x = w₁ (gens 0–2) · w₂ (gens 4–6)`, bond `K = V(3)ᵏ`, k ∈ {1, 2, 3}
  (the junction vertex that enters the newer nucleon, per the 2026-11-22 ruling) and `V(2)ᵏ`.
  Every strand stays in the trace; nothing is closed down before the full trace.
- Reported: passing nucleon words; for every pair, whether the bare `x` and each `x·K` pass, the
  ratio and `B`. Summary: the set of `B` over passing atoms. No pair is labelled "the deuteron".

## Addendum 2 (owner card 2, answer "A + B + D"), committed before any of its numbers

Applies to the twelve four-strand nucleon words that pass reading 3 in Phase B (L = 6). Nothing in
this addendum selects a word by its binding. Exact arithmetic: sympy, Laurent polynomials /
rational functions in q, no floats; numerical residuals at the proton pin q₀ with mpmath.

### (A) normal-form net against net(p), net(n)

- Corpus definition (`neutron-qvalue-symbolic.md` §Retired Form A; `qbeta_delta_candidate_census_probe.py::net`):
  `net(x)` = the sum of the coordinates of x in the normal-form basis {T_w} of H₃(q), with
  σ² = hσ + 1, σ⁻¹ = σ − h, h = q − q⁻¹. Targets: `net(p) = 1 − h/2`, `net(n) = 1 − 3h/2 + h²/2`.
- A four-strand word lives in H₄. "Closing to three strands" is not fixed by the corpus, so three
  readings are computed and all are reported:
  - **A1**: coordinate sum of the normal form in H₄ (no closure).
  - **A2**: Ocneanu conditional expectation E₄→₃ at z = 1 (T_u T₂ T_v ↦ z·T_u T_v, u, v ∈ ⟨s₀, s₁⟩),
    then the H₃ coordinate sum. z = 1 is the parameter at which the corpus calls `net` a trace.
  - **A3**: the same with z = z_D = q³/(q²+1).
- Reported per word and per reading: the exact net, the exact differences from net(p) and net(n),
  and their values at q₀. An **exact match** is a zero difference as a rational function of q. A
  **near match** is reported with its residual; no threshold makes it a match. If (A) yields a
  unique word equal to net(p) and a unique word equal to net(n), under one reading, that pair's
  Phase B binding (both bonds) is reported as the identified value with its scope. Otherwise none is.

### (B) bar-involution pairs

- bar is the ring automorphism σᵢ ↦ σᵢ⁻¹, q ↦ q⁻¹. bar(V(i)) = σᵢ⁻¹σᵢ₊₁ is not a γγ vertex, so
  bar of a γγ word is not a γγ word as a letter string; the test is equality of elements.
- For every ordered pair (w₁, w₂) of passing nucleon words: is the H₄ normal form of w₂ equal to
  bar(w₁) (normal form of the letter-inverted word, coefficients mapped q ↦ q⁻¹)? Also reported,
  as a weaker relation: equality of the z_D Markov traces of w₂ and bar(w₁), and of the nets under
  A1–A3.

### (D) every pair

- All 144 ordered pairs, both bonds, with bare-x pass, ratio and B, are written out in
  `phaseB-pairs.md` from the witness. No pair is labelled the deuteron.
