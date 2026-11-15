# gg_four_strand — pre-registration (bean qou-a1hh; hypothesis only; nothing wired)

Owner, 2026-11-15: "what next" → default option 1 (4-strand γγ grammar), to give the
n ≥ 4 doublet thread (bean qou-wkcd) a candidate list rather than hand-picked words.
Owner rulings in force: two orientations allowed as a hypothesis; V/V̄ is the chirality
pair bit (ι(V) = V̄, Lean `QOU.QuarkState.Helicity.iota_vertex`, PR #7941).

## Objects
- Vertex types on 4 strands: V_s = σ_sσ_{s+1}⁻¹ and B_s = σ_s⁻¹σ_{s+1}, s ∈ {0, 1, 2}.
- Words: all sequences of m vertices, m = 1..4 (6 + 36 + 216 + 1296 = 1554 words).
- Reading 3 alone: every level-m character χ_μ(E_{4→m} w), m = 1..4, two-row μ, is
  ≥ −1e-30 (convention D, proton q₀, base module at 40 dps).

## Readouts (all reported, none used to select)
R1 pass counts per length m; R2 whether pass depends only on m (as on 3 strands);
R3 passing words that use all three sites; R4 the (3,1) character of each passing word.

## Check (run void if it fails)
T0: for words on sites {0,1} only, characters at levels 1..3 equal the 3-strand values
from gg_two_orientations (restriction must agree).

## Expectation (may fail)
E1: pass is no longer a function of length alone, because level 4 sees how vertices on
different sites interleave.

## Amendment before any readout (crash on first run)
On 4 strands the generators are σ₀, σ₁, σ₂, so a vertex σ_sσ_{s+1}^{±} has s ∈ {0, 1} only
(4 vertex types, not 6). The first run crashed on s = 2 before any readout was computed.
Lengths are extended to m = 1..6 (4 + 16 + 64 + 256 + 1024 + 4096 = 5460 words) so that
m = 3 and m = 6 are both covered. R3 becomes "passing words using both sites". Everything
else is unchanged.

## Amendment 2 (2026-11-15, before any run): J₄-projected reading 3 on the m = 6 flavour-changing candidates

Requested by the n ≥ 4 doublet thread (draft PR #7957). Its explicit 3-dim (3,1) representation of H₄(q)
(`n4_left_doublet_flavour_probe.py`) supplies the projectors PL (left line of σ₁), PR (right line), and
Ja, Jb (J₄ = σ₃σ₂σ₁²σ₂σ₃ eigenlines inside PL; Ja + Jb = PL).

Candidates: every m = 6 word that passed reading 3 in the first run AND contains a site-1 vertex
(flavour-changing under J₄, per that thread). Words with no site-1 vertex are excluded by that criterion.

Readouts at q₀ (proton, base module's 40 dps), for each candidate w in the (3,1) rep:
- d_a = tr(Ja w Ja), d_b = tr(Jb w Jb), d_R = tr(PR w PR)  (d_a + d_b + d_R = χ_(3,1)(w));
- flip = tr(Ja w Jb w Ja).

Consistency check T1 (must pass before readouts are trusted): tr(w) in the explicit rep equals the base
module's χ_(3,1)(w) to 1e-30 on every candidate.

Pass criterion ("projected reading 3"): d_a ≥ −TOL and d_b ≥ −TOL and d_R ≥ −TOL. Reported per word, with
counts. No word is selected by its numbers; all candidates are listed. Scope (a).

## Amendment 3 (2026-11-15, before any run): q-threshold of reading 3 on pure γγ words

Requested by the owner ("thm then merge") to support a theorem of the form: every pure γγ word
(underlying permutation in S₄ is the identity) of length m passes reading 3 on 1 ≤ q ≤ 1 + c/m.

Object: for each pure word w of length m, q*(w) = inf{ q > 1 : some level character χ_(k,μ)(w) < 0 }
(levels k = 1..4, two-row μ, convention-D weights y_μ), computed in an independent exact Hoefsmit
seminormal representation at variable q (mpmath, 40 dps; grid step 1e-3 on [1, 2], then bisection to 1e-12).

Consistency check T2 (must pass before readouts are trusted): at q = q₀ the independent implementation
reproduces passes_alone and min_char of gg-four-strand.witness.json on all 5460 words (min_char to 1e-6).

Readouts: q*_min(m) = min over pure words of length m, for m = 3..6 (all pure words) and m = 9, 12
(seeded uniform random sample of 2000 pure words each, seed 0; sample, not exhaustive). Report m·(q*_min(m) − 1).
Also report which character fails first at the minimiser.

Hypothesis H (may fail): m·(q*_min(m) − 1) is bounded below by a positive constant c. If it is not,
the 1 + c/m form is wrong and the theorem will be stated in whatever form the data does support, or not at all.
Nothing selected or fitted; c is a readout, and the Lean statement will use a rational below it, not at it.
Scope (a).
