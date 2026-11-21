# Pre-registration: which inter-nucleon bond words does the γγ rule + reading 3 admit?

Written and pushed **before** the probe in this directory computes anything. Bean `qou-k54t`
(the A≥3 binding chain redo), `qou-brng`, `qou-ales` (γγ selection rule), `qou-99qc`.
Branch `claude/gg-internucleon-bond-2026-11-21`.

**Disclosure (not blind on one word).** While measuring run time, before this file was written,
I ran one word through the checker: nucleon `V³` with bond `V³` on generators `(3k+2, 3k+3)`
(the a3plus arm R word) for D, T and ⁴He. It passed reading 3 at every level for all three
(⁴He took 24 s). Nothing else was computed. That word is in the space below and its row will be
recomputed and reported like every other.

## 0. What the corpus already fixes (read, not assumed)

- **Nucleon.** `V = σ_a σ_{a+1}⁻¹`; nucleon k is `V³` on generators `(3k, 3k+1)` (0-indexed),
  proton = neutron as words (PR #7741, `../h2_gg_atom/results.md`; owner ruling 2026-11-20, D1 = A).
  `V` is the fourth (chiral-vertex) term of the ruled photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`.
- **γγ grammar.** `QOU/Mass/GammaGammaWordSelection.lean`: a γγ word is a concatenation of
  `vertex i = σᵢ σᵢ₊₁⁻¹`, no inverses (even length, writhe 0).
- **Owner decision A (2026-11-15).** The γγ rule also covers the nuclear bond letters;
  the single-crossing interface letters of `atom_braid_word_3A` are superseded
  (`docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`).
- **Prior bond results, none on the atom word:**
  - `qou-ales` steps 3/6/7: the bond **alone** `G^m = (σ₂σ₃⁻¹)^m` on H₆, reading 3 at the top
    level only, is feasible iff `3 | m` (m ≤ 10); selected `G³`. Lean `GammaGammaSelectionTen`.
  - `qou-ales` step 11: the junction generator is not adjacent to another junction generator, so
    every interface vertex borrows one nucleon generator. Four candidates: `σ₂σ₃⁻¹`, `σ₂σ₁⁻¹`,
    `σ₃σ₂⁻¹`, `σ₁σ₂⁻¹`; "nothing in the arc derives that choice".
  - `docs/audits/2026-09-14-…-artin-band-fork.md` R6: 120 band vertices on H₆, all feasible iff
    `k ∈ {3,6,9}` (bond alone, top level).
  - PR #7741: atom–atom (H₂) bond `V³` passes reading 3 at every level, at both sites.
  - PR #8722 (`../a3plus_gg_candidate/`): nucleon `V³`, bond `V³` at arms L/R; did **not** test
    reading 3 on the atom word.
  - `qou-99qc` NOTE 2026-11-16: on three strands over `{V, V⁻¹, L₊, L₋}`, a word passes reading 3
    iff it is a pure braid.

So the open question is whether reading 3 on the **whole nucleus word, at every level**, picks the
bond, and what it admits.

## 1. Atoms and word layout

Generators 0-indexed. Nucleon k = `V³` on `(3k, 3k+1)`. Junction j (between nucleon j and j+1) has
junction generator `g = 3j+2`; a bond at junction j is a word in generators `g−1, g, g+1` only.
Word order (same as PR #8722): `N₀ B₀ N₁ B₁ … N_{A−1}`.

| atom | strands | junctions |
|---|---|---|
| D | 6 | 1 |
| T, ³He | 9 | 2 (identical words, since p = n; reported once, labelled for both) |
| ⁴He | 12 | 3 |

## 2. Bond-word space (finite; nothing outside it is evaluated)

Written for junction generator g; shifted by 3j at junction j.

- **Arm A (primary: the Lean γγ grammar at the junction).** Every non-empty concatenation of the
  two vertices that touch the junction, `v_{g−1} = σ_{g−1}σ_g⁻¹` and `v_g = σ_gσ_{g+1}⁻¹`, of
  vertex-length 1…6. 2+4+8+16+32+64 = **126 words**. These are exactly the γγ words supported on
  the junction's three generators that use the junction generator.
- **Arm B (comparison: single-vertex powers, inverses included).** The four step-11 vertices
  `{v_{g−1}, v_g, v_{g−1}⁻¹, v_g⁻¹}` to the power k = 1…9. **36 words** (the positive powers
  k ≤ 6 are also in arm A and are reported once per arm). Inverse vertices are not γγ words under
  the Lean grammar; they are reported, not selectable.
- **Arm C (comparison: pure braids straddling the junction).** Freely reduced words in
  `σ_{g−1}^{±1}, σ_g^{±1}, σ_{g+1}^{±1}` of length 2, 4 and 6 whose permutation is the identity
  and which contain `σ_g^{±1}`. Tests whether "pass ⟺ pure" from the three-strand gluon thread
  holds across a junction. Not selectable (not γγ words).
- **Reference row:** no bond (free nucleons).

## 3. Runs

1. **D:** every word of arms A, B, C.
2. **T/³He, uniform:** the same bond word at both junctions, for every word of A, B, C that passed
   at D. **T/³He, mixed:** every ordered pair (B₀, B₁) of D-survivors in arm A, if there are at
   most 20 of them; otherwise uniform only, stated.
3. **⁴He, uniform:** the same bond at all three junctions, for every word (any arm) that passed
   the T/³He uniform run. ⁴He is 24 s per word, so it is limited to T survivors; mixed bonds at
   ⁴He are not run.

## 4. Test (the corpus checker, unchanged)

Reading 3 at every level, exactly as `../h2_gg_atom/h2_gg_atom_probe.py` (`level_chars`, lo = 1)
on top of `../h2_one_rule/h2_one_rule_probe.py`: close strands from the top with the
convention-D Markov trace and require `χ_μ(E_{n→m} W) ≥ 0` for every two-row `μ ⊢ m`, every
`m = 1…n` (under convention D the two-row shapes are exactly those with `y_μ > 0`). Seminormal
basis, mpmath 40 dps (the base's precision), proton q₀ via the committed `y-lambda-at-q0`
witness. A value `< −1e-25` fails. Any level character with `|χ| < 1e-15` is flagged
"numerical zero" and listed; it is not silently counted either way in the outcome.

Calibration before reading results:
- K1: the nucleon `V³` alone on H₃ reproduces `χ_(2,1) = 1.9941858…` and passes every level.
- K2: the top level equals `mjw.chi` for one D word (character check, as `h2_one_rule` K2).
- K3: `Σ_μ y_μ χ_μ(E_{n→m}W)` is independent of m (trace preservation) for one T word.

## 5. Reported

Per atom and word: pass/fail, failing levels, the negative characters, the crossing count, and
the trace ratio `tr(atom)/tr(free)` (reported, never used to select; ruling B of 2026-11-15).
Per arm and atom: the admissible set and its minimum-crossing-count members.

## 6. Outcome rules (fixed now)

Applied to **arm A** (the only selectable arm), per atom, with cost = crossing count and ties not
broken (the `qou-ales` FrobeniusSelected rule):

- **FIXES the bond:** at every atom the arm-A admissible set is non-empty and has exactly one
  minimum-cost word, and it is the same word (up to the junction shift) at D, T/³He and ⁴He.
- **ADMITS A FAMILY:** the admissible set is non-empty at every atom but the minimum is tied, or
  differs between atoms. The tied words are reported; no residual, trace ratio or AME number is
  used to pick among them.
- **ADMITS NONE:** at some atom no arm-A word passes.

Arms B and C are reported beside it and cannot change the outcome.

## 7. Not allowed

Changing the space, the order, the level range, the tolerance or the outcome rules after seeing
results; using AME binding energies, the trace ratio or any downstream number to choose a word,
site or power. No number here is compared to experiment. Scope (a) throughout: this space, this
word order, convention D, proton pin.
