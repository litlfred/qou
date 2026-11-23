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

## Theorem (Lean): pure γγ words pass reading 3 for 1 ≤ q ≤ 1 + (1/12)/m

`QOU.QuarkState.GammaGammaFourStrandPureBound.pure_gg_reading3`
(`folio/quantum-observable-universe/lean/QOU/QuarkState/GammaGammaFourStrandPureBound.lean`), sorry-free;
`#print axioms` gives propext, Classical.choice, Quot.sound only. For every pure γγ word w of length m ≥ 1,
every q with 1 ≤ q ≤ 1 + (1/12)/m, and every one of the eight level shapes, the convention-D level character is ≥ 0.

Method. The Hoefsmit seminormal matrices of the (3,1) and (2,2) blocks are written out over ℝ (the H₄ quadratic and
braid relations are proved in the same file). At q = 1 a pure word is the identity, so the 24-element S₄ closure
table gives the q = 1 products exactly. A generic perturbation lemma (`QOU.MathlibExt.ListProdPerturbation`, ℓ∞
operator norm) bounds the distance from the identity by M((1 + Mδ)^m − 1) with M = 11/6 (largest table row sum) and
δ = (11/10)(q − 1) (certified per-entry rational bounds on q ∈ [1, 11/10]). Bernoulli then gives ≤ 1 when
m·M·δ·(M + 1) ≤ 1, which c = 1/12 ensures, so every diagonal entry is ≥ 0 and each level character, a positive
combination of diagonal entries, is ≥ 0.

Scope (a). c = 1/12 is proved; the measured threshold is m(q* − 1) ≥ 1.187 (Amendment 3), so the constant is not
sharp. The bound reaches q₀ ≈ 1.10998 only for m = 1, so it says nothing about long words at q₀. Generators:
`lean_gen/` (exact sympy).

## Amendment 4: pure ⟺ pass at q₀ for long words (pre-registered)

`gg_four_strand_pure_long_q0_probe.py`, the amendment-3 seminormal representation at q₀ (proton pin,
convention D, mpmath 40 dps; H₄ relations hold to 9.8e-41). Its m ≤ 6 counts reproduce the table above exactly.
Witness: `gg-four-strand-pure-long-q0.witness.json`.

**Pure ⟺ pass fails at q₀ in both directions once words are long.**

R1, every word of length 7 and 8:

| m | pure & pass | pure & fail | not pure & pass | not pure & fail |
|---|---|---|---|---|
| 7 | 1792 | 0 | 0 | 14592 |
| 8 | 3584 | 0 | **208** | 61744 |

All pure words still pass at m ≤ 8 (smallest pure level character 0.50999). The non-pure direction breaks
again: 208 non-pure words pass at m = 8 (6 at m = 6, 0 at m = 7).

R2, powers u^k of every pure u with 3 ≤ |u| ≤ 6 (560 words), k = 1..10: **18 of the 560 have a failing
power**, all with |u| = 6. The earliest failure is k = 4, i.e. length 24 (u = V0.B0.V0.V0.B0.B0, smallest level
character −7.69 at some k ≤ 10). In the irreps (3,1) and (2,2) these u have eigenvalues either a reciprocal
pair 1/λ, λ with λ up to 1.89, or a unimodular complex pair (e.g. 0.98786 ± 0.15536i). Powers then grow one
eigen-direction and shrink another, and since the level characters are partial traces over the branching
subspaces, not full traces, they can turn negative. This is an explanation of the failures, not a proof.

R3, seeded samples of 2000 words each:

| m | pure: fail / 2000 | non-pure: pass / 2000 |
|---|---|---|
| 10 | 0 | 9 |
| 12 | 0 | 20 |
| 16 | 0 | 30 |
| 20 | 0 | 54 |
| 24 | 1 | 58 |
| 30 | 6 | 80 |

What this settles: at q₀, "pure ⟺ pass" is false. Failing pure words exist (shortest found: length 24), and
the non-pure passers grow with m. It does not settle the shortest failing pure length: 9 ≤ m ≤ 23 was only
sampled (10, 12, 16, 20) or reached through powers, so a shorter failing pure word may exist. The Lean bound
`pure_gg_reading3` is not contradicted: its interval 1 ≤ q ≤ 1 + (1/12)/m excludes q₀ for every m ≥ 1 except
m = 1. Scope (a).

## Amendment 5: shortest failing pure word at q₀ (pre-registered)

`gg_four_strand_shortest_failing_pure_probe.py`; witness `gg-four-strand-shortest-failing-pure.witness.json`.
Same representation and convention as amendment 4 (q₀ proton, convention D, 40 dps).

S1, every pure word of length 9, 10, 11 (22528, 102400, 315392 words): **all pass.** The smallest level
character over pure words falls slowly with length (0.3484, 0.3298, 0.3200). With amendment 4 this makes
**every pure word of length ≤ 11 pass at q₀.**

S2, squares (and cubes for |u| = 7) of every pure u with 7 ≤ |u| ≤ 11:

| \|u\| | length of u² | pure u tested | u² fails |
|---|---|---|---|
| 7 | 14 (u³: 21) | 1792 | 0 (u³: 0) |
| 8 | 16 | 3584 | 0 |
| 9 | 18 | 22528 | **3** |
| 10 | 20 | 102400 | 10 |
| 11 | 22 | 315392 | 34 |

**Shortest failing pure word found: length 18**, e.g. (B0.B0.V0.V0.B0.B0.V0.V0.B0)², smallest level character
−0.1487. Not settled: lengths 12 to 17, where only powers were tested, so a failing pure word of length 12–17
that is not a power may exist. Scope (a).

## Amendment 6 — the length 12–17 gap (run 2026-11-16)

Pre-registered in `preregistration.md` §Amendment 6 before the run. Same frame as amendments 3–5: Hoefsmit seminormal H₄(q), convention-D level weights, proton pin q₀, 40 dps (relations error 9.76e-41).

| readout | words tested | failures | min level character |
|---|---:|---:|---|
| G1, m = 12, exhaustive | 1,351,680 pure words | 0 | 0.02316 |
| G2, m = 13, 20,000 seeded | 20,000 | 0 | 0.2146 |
| G2, m = 14 | 20,000 | 0 | 0.1580 |
| G2, m = 15 | 20,000 | 0 | 0.1566 |
| G2, m = 16 | 20,000 | 0 | 0.1735 |
| G2, m = 17 | 20,000 | 0 | 0.0695 |

**What this settles.** Every pure word of length ≤ 12 passes reading 3 at q₀ (exhaustive, extends amendment 5's ≤ 11). No failure was found at lengths 13–17.

**What it does not settle.** Lengths 13–17 were sampled, not enumerated, so "no pure word of length 13–17 fails" is not shown. The shortest known failing pure word is still length 18, `(B0.B0.V0.V0.B0.B0.V0.V0.B0)²`. The minimum at m = 12 (0.0232) is much closer to 0 than the sampled minima, consistent with failures being rare structured words (squares and powers) that uniform sampling does not hit.

Witness: `gg-four-strand-pure-gap-12-17.witness.json`.
