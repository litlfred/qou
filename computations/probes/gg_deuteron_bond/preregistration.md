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
