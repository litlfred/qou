# Pre-registration — nucleon split from the four-strand lepton reading

Beans `qou-myts` (nucleon split, route list), related `qou-99qc`. Last parameter-free route named
for `m_n − m_p`: the neutron and proton words carry a lepton strand (β-decay picture
`n → p e ν̄`, crossed to `n ν → p e`), and the split comes from the lepton's crossings. Written
before any MeV value of this route is computed. Disclosure: the symbolic sector traces of §4 were
computed in sympy (over `ℚ(q)`, no number substituted) while writing this file, to state the
closed forms and the two structural facts used in §3. The proton anchor `q₀ = 1.10997858…` and
`E₀ = 4.18598136329 MeV` were read from the sibling audits. No ratio at `q₀`, no MeV value and no
comparison with CODATA had been computed for any variant below.

## Object (corpus, not chosen here)

`QOU.MassTheory.NeutronFourStrand` (choice C-lep, #8636 Part B): a fourth strand on the same `V`
is the lepton doublet, `ν = u`, `e⁻ = d`. The `T³ = 0` block of `V^{⊗4}` is
`N ⊕ P`, `N = n⊗ν = span(uddu, dudu, dduu)`, `P = p⊗e = span(uudd, udud, duud)`, with `σ₁, σ₂`
block-diagonal (the three-strand Jimbo blocks) and `σ₃` (third quark × lepton) mapping `N ↔ P`.
Sector traces `tr_N`, `tr_P` are the traces of the diagonal blocks, i.e. the trace with the lepton
strand coloured `ν` (resp. `e`). Nucleon word `V³ = (σ₁σ₂⁻¹)³` on strands 1–3.

## Formula (fixed in advance)

Gibbs map of route 1 (`NucleonSplitGibbsCoulomb`), no Coulomb term:

  `m_n − m_p = E₀ · log(τ_p / τ_n)`,  `E₀ = k_BT_q` (route T, `qbeta_e0.order_zero`);

tower `E₀` (`qbeta_e0.canonical`) as a labelled second column. A variant whose ratio is `≤ 0` at
`q₀` is reported as "log undefined", not dropped.

## Choices the construction forces, and the rule that fixes each (before numbers)

**C1. Which spaces are compared, and the trace weight / normalisation.**

* S1-closed: both nucleons in the same four-strand block (`τ_n` on `N`, `τ_p` on `P`), the lepton
  strand closed, weight `K^{⊗4}` (= 1 on both sectors), normalisation `[2]_q⁴` on both. Ratio
  `tr_P(β)/tr_N(β)`.
* S1-open: same block, lepton strand left open (weight `K^{⊗3} ⊗ 1`: `q` on `P`, `q⁻¹` on `N`).
  Ratio `q² tr_P(β)/tr_N(β)`.
* S2a: decay picture, neutron = four-strand `p⊗e` sector `P` (weight `K^{⊗4}`, `[2]_q⁴`), proton
  = three-strand `p` (`K^{⊗3}`, `[2]_q³`). Ratio `q[2]_q tr_A(V³)/tr_P(β)`.
* S2b: as S2a with `[2]_q³` for the four-strand neutron too. Ratio `q tr_A(V³)/tr_P(β)`.

Rule (null test): **a lepton strand that crosses nothing must give zero split**, because the
route claims the split comes from the extra crossing(s). For the spectator `β = V³ ⊗ 1`:
S1-closed gives ratio 1 (proved on main, `trN_V3_eq_trP_V3`); S1-open gives `q²` (the
three-strand cell, not from a crossing); S2a gives `q[2]_q = q² + 1` (the closed lepton loop's
quantum dimension, from comparing spaces of different strand number); S2b gives `q`. Only
S1-closed passes. It is also the corpus definition of a coloured trace (`K`-weighted trace of
`P_c ρ(b)` with `K` on every strand, `BorromeanRingColouredTrace`) extended to four strands, and
`K^{⊗4}` is what makes the trace Markov on the closed lepton component. **Selected: S1-closed.**
S1-open, S2a, S2b are reported, unselected.

**C2. Where the lepton strand crosses (the word `β = V³·X`).** Candidates, all parameter-free:

* `X = 1` (spectator, the null test);
* `X = w`-type single crossings `σ₃^{±1}`, and the #8636 word `w = σ₁σ₃⁻¹` (reference);
* `X = A_{k4}^{±1}`, the pure-braid generator in which the lepton loops once around quark strand
  `k` (`A_{34} = σ₃²`, `A_{24} = σ₃σ₂²σ₃⁻¹`, `A_{14} = σ₃σ₂σ₁²σ₂⁻¹σ₃⁻¹`);
* `X = L^{±1}`, `L = σ₃σ₂σ₁²σ₂σ₃ = A_{14}A_{24}A_{34}`: the lepton loops once around the whole
  nucleon (linking number 1 with each quark component).

Rule, in order:

1. *Lepton closes on itself.* The sector label (lepton coloured `ν` or `e`) is a label of the
   lepton component only if the word returns strand 4 to position 4, i.e. `X` is pure on the
   lepton. This excludes `σ₃^{±1}` and `w = σ₁σ₃⁻¹` (lepton merges with a quark component). `w`
   is printed as a reference row because it is the #8636 word.
2. *No quark position chosen.* The lepton couples to the nucleon, not to one quark. `L = Δ₄²Δ₃⁻²` (full
   twist of the four strands over the full twist of the three quarks) commutes with all of `B₃`;
   the `A_{k4}` single out quark `k` and do not. Structural facts (to be proved in Lean): `L` commutes with `σ₁, σ₂` on the block, so
   `V³L = LV³` (no ordering choice), and `tr_N(g V³ g⁻¹ L) = tr_N(V³ L)`, likewise `tr_P`, for
   every `g` in the image of `B₃` — the headline is invariant under conjugating the nucleon word
   inside `B₃`, which removes the per-colouring conjugation caveat of #9544 for the nucleon part.
   `A_{k4}` pick a quark (`k`) and depend on ordering; reported, unselected.
3. *Chirality.* `L` vs `L⁻¹` is a mirror choice. Sympy shows (Lean to confirm) that the S1-closed
   ratio for `L⁻¹` is exactly the reciprocal of the one for `L`: the **magnitude** of the split
   is chirality-free, only its **sign** depends on the choice. Pre-registered: `L` (positive
   crossings, the chirality of the Jimbo `σ = Ř` and of the corpus electron word `σ₀σ₁σ₀`). If
   `L` gives `m_n < m_p` that is reported as the result, not fixed by switching to `L⁻¹`.

**Pre-registered headline: S1-closed, `β = V³·L`, ratio `tr_P(V³L)/tr_N(V³L)`.**

## Selection rule

Nothing is selected by closeness to CODATA. Every variant in the grid
`{S1-closed, S1-open, S2a, S2b} × {1, σ₃, σ₃⁻¹, w, A_{34}^{±}, A_{24}^{±}, A_{14}^{±}, L^{±}}`
(S2 only for the words pure on the lepton plus the spectator) is printed with its gap; the gap
decides nothing. S1-open is S1-closed plus exactly `2E₀ log q`.

## What would count

* Headline within 0.1 % of CODATA 1.29333 MeV: reported as a candidate with every choice above
  listed. Prior: < 5 %.
* Otherwise scope-limited negative for this route.

## Method

Lean `QOU/Nuclear/NucleonSplitFourStrand.lean` (generic `[Field R]`, built on
`NeutronFourStrand`): `L` as an explicit block matrix, `L` commutes with `σ₁, σ₂`, `B₃`-conjugation
invariance of the sector traces, exact `tr_N`, `tr_P` of `V³L`, `V³L⁻¹`, `V³A_{k4}^{±}`, the
reciprocity `ratio(L⁻¹) = ratio(L)⁻¹`. Probe `computations/probes/nucleon_split_four_strand_probe.py`:
exact `Fraction` rebuild of the 6×6 block from the Jimbo Ř on the full 16-dimensional `V^{⊗4}`,
check of every Lean closed form, then 80 dps at the proton and muon `q₀`. CODATA only in the gap
column.
