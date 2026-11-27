# The down quark as a strand object, and what γγ production says about u and d

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-down-quark-strand-2026-11-27`
**Beans:** `qou-myts`, `qou-99qc` (selection rule: `qou-ales`)
**Lean:** `QOU/Nuclear/NucleonDownQuarkStrand.lean` (lean-direct `-DautoImplicit=false -s 65536`, exit 0;
axioms propext, Classical.choice, Quot.sound; the three core lemmas use none; no `sorryAx`)
**Probe:** `computations/probes/nucleon_down_quark_strand/` (pre-registration committed first; exact
sympy over ℚ(q), then 80 dps at the proton q₀; witness `nucleon-down-quark-strand.witness.json`)

## 1. Questions

Owner, 2026-11-27: *"what does γγ production say for u and d quarks. track full tower"*. Second,
fork F1 of `2026-11-27-nucleon-down-strand-self-energy.md`: is the down strand a different strand
object from the up strand (up = unknot strand, owner ruling 2026-11-20), so that a flavour self
energy `θ_d ≠ θ_u` exists?

γγ words are products of the pair-production vertex `σᵢσᵢ₊₁⁻¹` (photon
`1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`; `QOU/MassTheory/GammaGammaWordSelection.lean`).

## 2. What γγ production says for u and for d (full tower)

| | up strand | down strand |
|---|---|---|
| what γγ forces on the strand | nothing | nothing |
| a single quark letter `σᵢ^{±1}` γγ-produced? | no (odd length) | no (odd length) |
| value of the u/d scalar (`σ ↦ a`, `σ⁻¹ ↦ a⁻¹`) on any γγ word, any `n` | 1 | 1 |
| strand framing in the γγ core `V³` | self-writhe 0, signed count 0 | same |

Proved, every `H_n`:

* `wordChar_gammaGamma`: any character `σᵢ ↦ a`, `σᵢ⁻¹ ↦ a⁻¹` is `1` on every γγ word. With
  `a = q` and `a = −q⁻¹` these are the two one-dimensional blocks `λ = (n)` and `λ = (1ⁿ)` of every
  `H_n`; with `a = q` it is also the through-strand coefficient of the Jones decomposition, which
  `gg_quark_letters_tl` identified as the flavour datum (u ↦ `q`, d ↦ `q⁻¹`). So the one scalar
  that separates an up letter from a down letter cancels on every γγ word.
* `quark_letter_not_gammaGamma`: a lone up or down letter is never γγ-produced
  (`gammaGamma_length_even`).
* `gammaGamma_writhe_ne_nucleon`: γγ words have net orientation 0; reading u as `+1` and d as `−1`,
  `uud` has `+1` and `udd` has `−1`. No γγ word carries either nucleon's flavour content.
* `core_pure`, `core_linking_zero`, `core_strand_writhe_zero`: in the γγ core `V³ = (σ₀σ₁⁻¹)³`
  all three strands return home, all pairwise linking numbers are 0, and every strand's signed
  crossing count is 0. No strand of the core is marked as u or d.

Measured, exact, all γγ words up to the vertex counts shown:

| n | max vertices | γγ words | pure braids | strand signed-count patterns of the pure ones |
|---|---|---|---|---|
| 3 | 6 | 6 | 2 (`V³`, `V⁶`) | (0,0,0) |
| 4 | 4 | 30 | 4 | (0,0,0,0), (2,2,−2,−2) |
| 5 | 4 | 120 | 7 | (0,0,0,0,0), (2,2,−2,−2,0) |
| 6 | 3 | 84 | 4 | (0,…,0) |

From `n = 4` γγ can split strands into opposite-orientation classes, but only as **linked pairs**
(e.g. vertices `[0,1,0,1]`: strands 0,1 linked `+1`, strands 2,3 linked `−1`), always balanced
(the counts sum to `2·writhe = 0`). That is a pair-production pattern (a `+` pair and a `−` pair),
not a three-quark flavour assignment. On three strands γγ produces only the balanced core.

**What is not reachable by γγ:** the quark letters (odd length), the flavour sign map (which strand
is u, which is d: `gg_quark_letters_parity` R5), and any net orientation `±1`. The reach on the
11-letter nucleon word stays 6 of 11 letters (`GammaGammaSelectedDeltaVanishes`). Confinement SDP
reading 3 does not add it: on the γγ placement 001 all 27 parity choices pass (`gg_quark_tail`).

**Answer to the owner's question:** γγ production says the same thing about u and d, namely
nothing that tells them apart. It forces equality of every u/d scalar on what it produces, at
every level of the tower, and it cannot produce the letters that carry flavour.

## 3. Is the down strand a distinct object? (fork F1)

Corpus: `def:down-quark` makes the down quark **the same unknot** as the up quark
(`down_quark_is_unknot`) with the **opposite crossing orientation** (`quark_crossing_asymmetry`).
No different colouring, twist or framing is defined. `H_n(q)` has one strand type. γγ (§2) gives
every strand of the core framing 0. **So the corpus does not force a distinct down-strand object.**
Scope (b) for γγ+reading 3 (invariants: vertex length, writhe 0, the character identity); this is a
statement about the selection rule, not that a distinct object is impossible.

Enumerated candidates for a hand-placed (non-γγ) flavour sign, none selected:

| id | one-strand factor u / d | where in the corpus | split `E·log(f_u/f_d)` |
|---|---|---|---|
| C0 | 1 / 1 | `def:down-quark` read as same object, same framing | 0 |
| CT | `q` / `q⁻¹` (through-strand parity) | `gg_quark_letters_tl`; the K-weight of `NucleonSplitFullTower` | `2E·log q` |
| CM | `z_D` / `z̄_D` (Markov stabilisation curl) | Markov property, convention D | `4E·log q` |

Exact (Lean `curl_ratio`, `zbarD_eq`, `zD_bar`; probe B): `z̄_D = z_D − (q − q⁻¹) = 1/(q(q²+1))`,
`z_D = q⁴·z̄_D`, and `q ↦ q⁻¹` swaps them, so u ↔ d is the bar involution here too. The corpus
`K`-weighted partial trace gives `ptr_K(Ř) = z_D` and `ptr_K(Ř⁻¹) = z̄_D` on one pair, exactly
(probe B), so CM is the value the existing trace assigns to a curl of each sign. A γγ vertex read as
two curls carries one of each, `z_D·z̄_D = q²/(q²+1)²`, which is bar-even (`vertex_curls_bar_even`):
flavour-blind again. CT is the existing Gibbs cell, not a new term.

## 4. Numbers (proton q₀ = 1.10997858275138…; CODATA only in the last column)

| candidate | E₀ order zero | E₀ tower | ratio to CODATA 1.29333 MeV (order zero / tower) |
|---|---|---|---|
| C0 | 0 | 0 | 0 / 0 |
| CT `2E log q` | 0.873537 MeV | 0.882197 MeV | 0.675 / 0.682 |
| CM `4E log q` | 1.747073 MeV | 1.764395 MeV | 1.351 / 1.364 |

`curl_split_eq_twice_through`: CM is exactly twice CT. The data sit between the two; that is a
comparison, not a selection, and it does not favour either candidate.

## 5. Verdict

* γγ (with SDP reading 3) forces nothing for u or d separately and assigns them equal values on
  everything it produces, on every `H_n`. Scope (b) for that rule.
* The corpus does not force a distinct down strand. Survivors if flavour is placed by hand: C0, CT,
  CM. None is forced; nothing is selected.
* No new derived flavour self energy results. The split stays the existing CT cell (0.874 MeV) until
  a rule outside γγ places the flavour sign and picks CT or CM.

## 6. Forks (owner calls, not decided here)

* **G1** Is CM (a quark letter acting as a stabilisation curl on its own strand) a legitimate reading
  of `def:down-quark`'s "negative crossing orientation", or only CT (through-parity)? CM doubles the
  cell; CT is the status quo.
* **G2** The γγ rule cannot reach flavour. Either flavour letters are admitted from another rule
  (which one), or the γγ definition is widened (e.g. admit `V̄ = σ₀⁻¹σ₁`, `gg_two_orientations`).
* **F1** (from the sibling audit) resolves to "not forced by the corpus".

## 7. Reproduce

    python3 -u computations/probes/nucleon_down_quark_strand/nucleon_down_quark_strand_probe.py
    lean -DautoImplicit=false -s 65536 folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonDownQuarkStrand.lean
