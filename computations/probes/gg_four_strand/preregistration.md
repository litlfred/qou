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
