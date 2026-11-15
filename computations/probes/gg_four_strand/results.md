# gg_four_strand — results (bean qou-a1hh; hypothesis only; nothing wired)

Pre-registration ba70b76ef7a, plus an amendment written before any readout: on 4 strands
only s ∈ {0, 1} is a vertex site, so there are 4 vertex types V0, B0, V1, B1, and lengths
run to m = 6 (5460 words). Convention D, proton q₀, base module at 40 dps.
Reading 3 alone = every character at levels 1..4 ≥ −1e-30.

## Check: T0 (restriction to sites {0} agrees with the 3-strand values): PASS

## R1 pass counts
| m | pass / words |
|---|---|
| 1 | 0 / 4 |
| 2 | 0 / 16 |
| 3 | 16 / 64 |
| 4 | 32 / 256 |
| 5 | 0 / 1024 |
| 6 | 518 / 4096 |

## R2: pass is NOT a function of length alone (E1 holds)
It is almost entirely a function of the **site pattern** (which site each vertex sits
on), and almost blind to orientation (V vs B):

- m = 3: patterns 000 and 111 pass for all 8 orientations each. One-site words only.
- m = 4: patterns 0101 and 1010 pass for all 16 orientations each.
- m = 6: patterns 000000, 111111 and the six cyclic rotations of 000111
  (000111, 001110, 011100, 111000, 110001, 100011) pass for all 64 orientations.
  Six other patterns (alternating-type) pass for exactly one orientation each:
  B0.V1.B0.V1.B1.V0, B0.V1.B1.V0.B0.V1, V1.B0.V1.B1.V0.B0, V1.B1.V0.B0.V1.B0,
  B1.V0.B0.V1.B0.V1 (χ_(3,1) = 0.42048999549) and B1.V0.B1.V0.B1.V0 (χ_(3,1) = 0.374693274178).

## Reading (scope a)
- Since the trace is cyclic, "rotations of 000111" is one class: three vertices on site 0
  followed by three on site 1. Site 0 spans strands 0–2, site 1 spans strands 1–3.
- Orientation (V/B, the chirality pair bit) does not decide passing except in the six
  single-orientation words. Site placement does.
- The site bit is a new binary label beyond V/B. Whether it is related to the σ₃-eigenline
  flavour of the n ≥ 4 doublet thread is not tested here.

## Amendment 2: J₄-projected reading 3 on the m = 6 flavour-changing words

Scope note (added after the run, 2026-11-15): "flavour" in this section means the J₄ label of
the n ≥ 4 doublet, which is the H₃ isotypic sector (Ja = (3), Jb = (2,1)): three-strand isospin
3/2 vs 1/2. It is not n ↔ p; Hecke elements commute with U_q and cannot change T³ (PR #7975,
beans qou-wkcd / qou-0whz). The numbers below are unchanged.

Pre-registered at 669d96f2adb. Probe `gg_four_strand_j4_projected_probe.py`, witness
`gg-four-strand-j4-projected.witness.json`. Explicit (3,1) rep of H₄(q) from draft PR #7957, mpmath at
proton q₀ (40 dps). T_rep (Ja + Jb = PL, J₄ commutes with σ₁, σ₂) and T1 (tr w = base χ_(3,1)(w), all
454 words, to 1e-30) both pass.

Candidates: the 454 m = 6 words that passed reading 3 and contain a site-1 vertex (518 passing minus the
64 words of pattern 000000).

| group | words | projected pass (d_a, d_b, d_R ≥ 0) |
|---|---|---|
| pattern 111111 | 64 | 64 |
| rotations of 000111 | 384 | 384 |
| the six mixed-site words | 6 | **0** |

All six mixed-site words fail in the same place: the Jb diagonal d_b = tr(Jb w Jb) is negative (−0.20 to
−0.40), while d_a and d_R stay positive. Their full χ_(3,1) is positive only because d_R outweighs d_b.

Flavour flip tr(Ja w Jb w Ja) is nonzero on 452 of 454 words; it is ≈ 0 on V1.B0.V0.B0.B1.V1 and
B1.V0.B0.V0.V1.B1 (both rotations of 000111). Its sign is not definite (114 negative), and no criterion
was registered on it.

**Reading.** Scope (a): within this grammar, every site-pattern word survives the J₄ projection, and the
six orientation-sensitive exceptions do not. So at m = 6, "passes reading 3 in every flavour sector"
coincides with "passes by site pattern". Nothing is selected or adopted.

## Exploration (post hoc, not pre-registered): reading 3 at m ≤ 6 tracks the pure-braid condition

`gg_four_strand_pure_braid_check.py`. A γγ vertex V_s or V̄_s maps to the same permutation, the 3-cycle
s_{s+1}s_{s+2}, so a word's permutation forgets orientation. Against the reading-3 results above:

| m | pure & pass | pure & fail | not pure & pass | not pure & fail |
|---|---|---|---|---|
| 1, 2, 5 | 0 | 0 | 0 | all |
| 3 | 16 | 0 | 0 | 48 |
| 4 | 32 | 0 | 0 | 224 |
| 6 | 512 | 0 | **6** | 3578 |

Every pure γγ word with m ≤ 6 passes. The only non-pure passing words are the six mixed-site words, and
those are exactly the ones that fail the J₄-projected reading (Amendment 2). So at m ≤ 6:
**J₄-projected reading 3 holds ⟺ the word is a pure braid.**

Why this is expected near q = 1 (standard character theory, not yet formalised): at q = 1, H₄ becomes the
group algebra of S₄ and a γγ word becomes its permutation π, an even permutation. Under convention D only the
shapes (4), (3,1), (2,2) carry weight. χ_(2,2) = −1 on 3-cycles and χ_(3,1) = −1 on double transpositions,
so at q = 1 reading 3 passes iff π = id, where every χ_λ = dim λ > 0. Lower levels see π restricted, with the
same conclusion. So the 448 inequalities at q₀ ≈ 1.11 are perturbations of strict inequalities
χ_λ = dim λ > 0 at q = 1. The projected diagonals d_a, d_b, d_R all sit near 1 = tr(projector), as they
should. The six exceptions are non-pure words that the deformation pushes over the line. The same argument
explains the 3-strand result (V^m pure iff 3 | m) and the orientation blindness.

Open: a uniform bound that makes this a theorem ("pure γγ words of length m pass for 1 ≤ q ≤ 1 + c/m"),
and whether pure ⟺ pass persists for m > 6.

## Amendment 3: q-threshold of reading 3 on pure γγ words (pre-registered)

`gg_four_strand_pure_threshold_probe.py`, independent Hoefsmit seminormal representation of H₄(q) at
variable q (mpmath 40 dps). H₄ relations hold to 1e-40 at q₀, and T2 passes: it reproduces passes_alone and
min_char of the first run on all 5460 words. q*(w) = first q > 1 where some level character goes negative
(grid 1e-3 on [1, 2], then bisection).

| m | pure words | mode | q*_min | m·(q*_min − 1) | first failing character | minimiser |
|---|---|---|---|---|---|---|
| 3 | 16 | all | 1.39567 | 1.187 | level 2, (1,1) | B0.B0.B0 |
| 4 | 32 | all | 1.52956 | 2.118 | level 2, (1,1) | V0.B1.V0.B1 |
| 5 | 0 | all | — | — | — | — |
| 6 | 512 | all | 1.21061 | 1.264 | level 2, (1,1) | B0.B0.V0.V0.B0.B0 |
| 9 | 2000 | sample, seed 0 | 1.18815 | 1.693 | level 2, (1,1) | B0.B0.B1.B1.V1.V1.B1.B1.B0 |
| 12 | 2000 | sample, seed 0 | 1.14589 | 1.751 | level 2, (1,1) | B0.B0.V0.V0.B0.B0.B1.V1.B1.V0.V0.B0 |

Reading (scope a):
- Hypothesis H survives on this data: m·(q*_min − 1) ≥ 1.187 on every length tested, with the minimum at m = 3.
  m = 9 and 12 are samples, so their minima are upper bounds on the true minima.
- The first failure is always the level-2 sign character χ_(1,1), never level 4.
- A bound of the form 1 + c/m with c ≈ 1.19 reaches q₀ ≈ 1.10998 only for m ≤ 10. So such a theorem
  cannot by itself say that every pure word passes at q₀; whether long pure words fail at q₀ is open
  (at m = 12 the sampled minimum, 1.146, is still above q₀).
