# Pre-registration: H₂ with a γγ-built nucleon block (owner decision C, "try γγ first")

Written and committed **before** any number in this directory was computed. Beans `qou-a1hh`
(H₂ tower), `qou-ales` (γγ rule), `qou-99qc` (scored element). Owner, 2026-11-15, on the card
"Where does the atom's 3-letter quark block come from?": **try γγ first** — build the quark block
from γγ vertices, test reading 3 at every level, then re-run H₂ on that atom. Same day the owner
ruled A (one γγ rule also covers nuclear bonds) and B (trace drop is reported, not a selection
clause). Previous result: `../h2_one_rule/results.md` — with the production atom, the bare H₂ word
fails reading 3 at levels 3–4 in all four cells, so the bond was undecided (outcome ii).

## 0. What the corpus fixes

- γγ words are concatenations of `vertex i = σᵢσᵢ₊₁⁻¹`, with no inverses
  (`QOU/Mass/GammaGammaWordSelection.lean`, `inductive GammaGammaWord`). They have even length and
  writhe 0.
- On three strands the only vertex is V = σ₀σ₁⁻¹. The CORE is V³.
- The production proton block (`mjw.tokens(1,0)`) is `V³ · TAIL_p · σ₀σ₀` (11 letters). TAIL_p
  (3 letters, odd) and the gluon σ₀σ₀ (writhe +2) are not γγ words.

## 1. Structural statement, made before computing

If the whole nucleon block on its three strands is a γγ word, it is **Vᵐ** for some m ≥ 0. So:

- the quark block, the gluon and the core merge into one power of V, and the split m = 3 + j + k
  (core, quarks, gluon) is invisible to any diagnostic;
- **the proton and the neutron become the same word**. A three-strand γγ nucleon carries no
  flavour. Telling them apart needs a non-γγ letter or more strands (pair production on four or
  more strands, closed down). That is out of scope here and is the named next step if the owner
  wants flavour.

This is a consequence of the corpus grammar, not a measurement.

## 2. Enumeration space (nothing outside it is evaluated)

- Nucleon block **Vᵐ, m ∈ {3, 4, 5, 6, 7}** on the nucleon's three strands. m = 3 is the core
  alone. m = 7 matches the production budget 11 letters rounded to the even length 14 (core 6 +
  quark block up to 4 + gluon 2–4); m = 4, 5, 6 lie between.
- The electron is held fixed exactly as in `h2_one_rule`: both corpus choices, T_w0 = σ₀σ₁σ₀ and
  the trefoil σ₀³σ₁. **The electron is not a γγ word** (odd length). Decision C is about the quark
  block only; the electron is flagged, not changed.
- H₂ cells exactly as `h2_one_rule` (owner option 1): 12 strands, atom = nucleon (strands 0–2) +
  electron (3–5), atom 2 in order pe or ep, no p–e letter, no junction letter. Bond letters
  K ∈ {none, V, V², V³} at bond site s ∈ {4, 5}.
- Also the bare nucleon Vᵐ on H₃ alone (levels 1–3).

Counts: 5 values of m × (2 electrons × 2 orders × 7 bond choices) = 140 H₂ rows, plus 5 H₃ rows.

## 3. Test (unchanged from `h2_one_rule`)

Reading 3 at every level: close strands from the top with the Markov trace at convention D,
z_D = q³/(q²+1), proton pin; require χ_μ(E_{n→m} W) ≥ 0 on every two-row μ ⊢ m with y_μ > 0, for
every m = 1…n. mpmath at 70 dps, seminormal basis. Code reused from `h2_one_rule_probe.py`
unchanged except the nucleon block. Reported per row: failing levels, the negative characters,
and the trace ratio tr(xK)/tr(x) (reported, not used to select, ruling B).

## 4. Calibration (must pass before results are read)

- K0: with the nucleon block set back to the production block, the 28 rows of
  `h2-one-rule.witness.json` are reproduced to 1e-40.
- K1–K4 from `h2_one_rule` (y formula, top level = χ, closing preserves the trace, Markov property).
- K5: χ_(3)(Vᵐ) = 1 on H₃ for every m (V has trivial-rep value q·(−q⁻¹)·(−1)... checked
  numerically against `mjw.chi`).

## 5. Outcomes

- **(i) a γγ bond exists:** for some m, the bare H₂ word passes every level and some bond
  K ≠ none also passes every level. Reported with every such (m, K, site, electron, order).
- **(ii) still blocked, now by the electron:** for every m the bare H₂ word fails some level.
  Since the nucleon block is then pure γγ, the remaining non-γγ ingredient is the electron, and
  the next owner question is whether the one rule covers the electron too.
- **(iii) no γγ bond:** for some m the bare word passes, but no K ≠ none passes for that m.
- Mixed results across m are reported per m. No m is chosen by the result; there is no ranking.
