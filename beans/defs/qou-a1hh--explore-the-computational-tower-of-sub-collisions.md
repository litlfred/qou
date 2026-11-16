---
# qou-a1hh
title: Explore the computational tower of sub-collisions (multi-strand convolution, C+O to CO)
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:48:36Z
updated_at: 2026-11-15T17:26:00Z
---

Owner 2026-10-12: explore two types of towers. Parent context: qou-jfx8 (segment collision datum, PR #7741). Prior-work grep in progress.


## 2026-10-12 — formalized (SegmentCollisionDatum.lean Parts E, F, lean-direct exit 0)
Part F chain3_trace: under the disjoint-block law, solved pieces joined by single-crossing letters compose by traces: tr(a ℓ₁ b ℓ₂ c) = μ₁μ₂ tr a tr b tr c. Part E: a window state depends only on the strands above the nearest bond it does not reach. Scale (exact integers): under convention D the trace factors through the two-row (TL) blocks, Σ dim² = Catalan(n): T/3He n=9 4862; ⁴He 2.08e5; C (n=36) 1.20e19; O (n=48) 1.31e26; CO (n=84) 2.71e47, max block 2.2e23. Direct evaluation of CO is impossible; composition by traces is O(#bonds) once pieces are solved. Open: what a depth-k window costs at a multi-strand (molecular) junction.


## 2026-10-12 — prior art
The chain law I derived (chain3_trace, conditional on DisjointBlockMultiplicative) was already MEASURED: docs/audits/2026-09-16-sdp-analysis-entangled-deviation-and-light-cone-recursion.md — tr(atom)/tr(free) = ∏(z_D + d_kind) to 1e-50 on D, T, ³He, ⁴He. chain3_trace is its derivation from the disjoint-block law (itself conditional on TowerSpan). Related: qou-tower ('There is no tower': GS reduction in H₃ leaves the same 6-dim state for every nucleus), molecular-construction/ (parabolic H_λ ↪ H_N; co-molecular-braid; co_lp_dual_binding.lean), universal-ilp-algorithm, ComputationalHorizon.lean, qou-sv7h (O(dim³) cost). No cost-per-level law exists in the corpus.


## 2026-10-12 — molecular junction window (PR #7769, stacked on #7741; probe 33/33, Lean junction corollaries exit 0)
CO vs N₂ (both 28 nucleons): for windows NOT containing the junction generator, they first separate at depth k* = 19 on the carbon side (agree over 6 nucleons; gap 1.85e-50 one short, 0.921 at k*, at the bond at carbon's p|n interface) and k* = 22 on the oxygen side. Lean (junction_window_above/below, junction_cannot_separate_above): a window off the junction generator sees one atom only, whatever the junction letter. Caveats: the depth is set by the builder's sorted p…p n…n ordering (a convention, D1 note), and the corpus has NO molecular junction letter (molecular-braid.md names a 'molecular crossing table' never specified; A+Z strands with electrons vs 3A nucleus words), so junction-containing windows were not measured and none was invented.

## 2026-10-13 — bond-order gap (U5 of #7773) is an encoding artifact; owner points to the dual-space operator
Owner: "there is a knot-convoluted tensor product that acts on braids, part of dual space" (answer to: which #_β?).
- Why U5 failed: #7773 read L_b (covalent-bond-shared-trefoil) as adjacent Artin letters linking extra trefoil BLOCKS laid contiguously on one line; only one block fits between the nuclei. Scope (a): a statement about that encoding, not about bonds. Correction comment posted on #7773.
- Corpus match for the owner's operator: prop:ilp-covalent-bond (molecular-construction/ilp-covalent-bond.md): the bond is a KNOT OPERATOR K acting by x ↦ NF(x·K), chosen in the LP's DUAL space ("the dual space of the LP is the knot operator space"); K = T_{2,3}^{-1}, min crossing s.t. G·NF(x·K) ≥ 0, tr(x·K) ≤ tr(x). Acting by multiplication on existing strands, k operators need NO new strands, so the contiguity obstruction does not arise.
- Corpus CONFLICT found: covalent-bond-shared-trefoil says "Hopf linking" of shared trefoils; ilp-covalent-bond says knots not links and "the Hopf link gives repulsive or weak binding". #7773 followed the former under the 2026-10-12 ruling "corpus L_b".
- Not fixed by the corpus: which strands of A⊗B the operator K acts on; and whether order k is K^k on one site or k sites. Existing producer molecular-trefoil-scan.py uses a 2-generator crossing-list "vertex volume" model in float64 with α_em/E_mol, not a Hecke product. Its D0(H₂) 0.1% figure is not re-derived here.

## 2026-10-13 — H₂ corpus LP for ⊗_K, both electron words, γγ-restricted (probe 5/5, KnotConvolutedTensor.lean exit 0)
Owner: "try both" (electron = corpus T_w0 σ0σ1σ0, which closes to a Hopf link; vs true trefoil σ0³σ1) and γγ-restricted K (σ_sσ_{s+1}⁻¹ = unknot, its square = 4₁). 8 configurations each (atom2 pe/ep, intra-atom p–e letter on/off, junction crossing-table letter on/off).
- p–e letter ON: reading 3 fails on the H₂ state itself in all 8 (both electrons) → no K feasible. Measured, scope (a).
- p–e OFF, junction letter OFF: γγ LP selects the vertex σσ⁻¹ (unknot) for both electrons, both orientations.
- p–e OFF, junction letter ON: T_w0 electron: full LP selects σ0⁻³σ1^± (true inverse trefoil) for e|p, unknot words for e|e; γγ selects nothing for e|p and the vertex for e|e. Trefoil electron: NO K feasible at all (full and γγ) in either orientation.
- γγ never selects 4₁ (min crossing picks the length-2 vertex whenever any γγ word is feasible).
- Corpus naming: σ0σ1σ0 "trefoil" closes to a Hopf link; σ0σ1 "Hopf link" closes to the unknot. Algebra unaffected; names shifted. Not edited (owner call).

## 2026-10-13 — 🛑 RETRACTION: both H₂ ⊗_K runs (e1ef182f22, 94552dacf2) computed tr(Mᵀ K), not tr(M K)
- Bug: knot_convoluted_tensor_h2_probe.py::tr_prod indexed M[j][i]; K[i] is column i ({j: K_ji}), so it returned tr(MᵀK). The probe's cross-check used M = identity, which cannot see a transpose.
- Invalidated: EVERY x·K figure — ratios, reading 3 on x·K, trace-decrease, hence every "LP selects" / "γγ selects" / "none feasible" row in the 2026-10-13 entry above and in the PR #7741 comments 6147812696 / 6147079940-follow-ups and chat.
- NOT affected: reading 3 on the H₂ state x itself (chi_x is read off the prefix diagonal) — "p–e letter on ⇒ x fails reading 3" stands; the knot-vs-link closure checks; the Lean file.
- Fix: M[i][j], plus a cross-check with a NON-identity prefix against chi of the concatenated word (old formula misses by 1.92, new by 4.6e-41). Re-run in progress.
- Found by a locality test (owner pick "try 1"): with the correct product, the ratio of σ0⁻³σ1^± at the e|p junction is identical on 6-, 9- and 12-strand windows (0.52575295871417605185 / 0.45095163122811970554 at 40 dps), and disagreed with the witness's 0.8865 / 0.8117.

## 2026-10-13 — corrected H₂ ⊗_K run (6/6 checks, tr(MK) fixed); owner pick "try 1" = drop p–e letter, keep junction letter
Option-1 cells (pe_letter=0, cmol=1), 40 dps, measured:
- Corpus orientation p|e|p|e (the interleaved ordering h2-lp-dual-binding selects) + corpus electron T_w0: full LP selects K = σ1^{±1}σ0⁻³ at site 4 (min crossing 4). Both close to the INVERSE TREFOIL — the knot prop:ilp-covalent-bond names. Ratios tr(xK)/tr(x): 0.88645508185181440444 (σ1σ0⁻³), 0.81165375436575805813 (σ1⁻¹σ0⁻³). The LP's min-crossing objective does not break that tie.
- Same cell, γγ-restricted (σσ⁻¹ unknot, its square 4₁): NOTHING feasible — all four raise the trace (1.31–1.60).
- Conjugate braid reps of the same knot are NOT interchangeable: σ0⁻³σ1 at site 4 gives 0.52575 but fails reading 3 on (6,6); σ1σ0⁻³ gives 0.88646 and passes. The bond value depends on the braid word, not only the knot.
- e|e orientation: LP selects length-2 words (unknot closures), 6-way tie, ratios 0.6588 / 0.7723 / 0.8865; γγ nothing.
- True-trefoil electron σ0³σ1: nothing feasible in either orientation.
- Locality (this config): ratio identical on 6-, 9-, 12-strand windows → CO can be done on a junction window, conditional on chain multiplicativity (not proved).
Still open (owner): tie-break between the two inverse-trefoil braids; γγ ruling vs ilp-covalent-bond conflict on H₂.

## 2026-11-15: correction, takeover, and the H₂ run under the one rule
Takeover: thread "Map SM and eightfold way, probe option C" (session_01Qmmkt9BEcDtGHY9hqeKYab). The last commit on this branch before the takeover was b3e86396f5a.
- Owner ruling 2026-11-15: "molecular bonds should be same... all one rule." So γγ + SDP (qou-ales) governs bonds. The bond exemption was an agent recommendation (2026-10-13), never a ruling.
- Correction: "γγ selects nothing on H₂" (above) was over-stated. In the option-1 cell the γγ words fail only on the trace-drop clause, and that cell's junction letter is a single crossing, so it is not γγ. In the cell with no junction letter, V passed at n = 12. Re-audit doc: https://claude.ai/artifact/YEvvHTsb8EY6Suwp4hXX2d
- One-rule cell (no p–e letter, no junction letter), with reading 3 at EVERY level by top closing. Pre-registered 4ff6d8d594d; results 3a88b14ab5c (4/4 checks). Outcome (ii): the bare x fails at level 3 in all 4 cells, because of the production proton block's (2,1) character (−0.08436 for T_w0, −0.04773 for the trefoil electron). So the bond is UNDECIDED until the atom is γγ-derived (re-audit decision C).
- Observation: V³ never adds a failing level beyond the atom's. V and V² do (levels 7–12). At n = 12 only, V had looked feasible.
Status: open. It waits on re-audit decisions A, B and C.

## 2026-11-15: owner rulings A and B
- A: the one γγ rule also covers nuclear bond letters (g+d_k). The binding thread is notified.
- B: trace drop is a RESULT, not a selection clause. Bonds are selected by γγ + reading 3 (every level). tr(xK) < tr(x) is reported. prop:ilp-covalent-bond still lists it as a clause; the rewording will be put to the owner before any edit.
- C (origin of the 3-letter quark block) is still open.

## 2026-11-15 — decision C ("try γγ first"): H₂ with a γγ nucleon (PR #7741, `h2_gg_atom/`)

Pre-registered (97dacc709d3), then computed (4901ed2c59b). Nucleon block Vᵐ, m = 3…7. On H₃ only V³ and V⁶ pass reading 3 at every level; p and n are the same word (no flavour on three strands). With the T_w0 electron the bare H₂ word passes every level and the bonds that pass are exactly V³ at s = 4 and 5 (trace ratio 0.9974/0.9985, ep at s=5 ratio 1). With the trefoil electron the bare word fails at level 6, block (3,3), so the electron is now the only non-γγ ingredient blocking. Open owner question: does the one rule cover the electron? Scope (a).

## 2026-11-15 — γγ electron (owner: "Yes, test a γγ electron"), PR #7741 `h2_gg_electron/`

Pre-registered e1e22ebfb1d. Nucleon V³/V⁶, electron V^k, k = 0…7, 224 rows. Bare H₂ passes iff k ∈ {0, 3, 6}; then the passing bonds are exactly V³ at s = 4, 5 (ratio ≈ 0.9984). Under the one rule on three strands nucleon, electron and bond all come from {V³, V⁶} and the bond is V³; nucleon and electron are not distinguished by the grammar. Open: which power is the electron (owner). Scope (a).

## 2026-11-15 — level-6 trefoil failure derived (owner request)

Closed form, PR #7741 `h2_gg_atom/level6_trefoil_derivation.py` (7/7). χ_(3,3)(p⊗e) = χ_(3)(p)χ_(3)(e) + χ_(2,1)(p)χ_(2,1)(e); χ_(2,1)(σ₀³σ₁) = −1 exactly, χ_(2,1)(σ₀σ₁σ₀) = 0, χ_(2,1)(V³) ≈ 1.99419 > q⁴ ≈ 1.51795 ⇒ negative; matches witness to 1e-18. Negative for 1 ≤ q < 1.18313. The T_w0 "pass" holds only because its (2,1) character vanishes (Hopf link). Bare word only.

## 2026-11-15 — electron generator: (b) weak vertex, then (a) torus knots (owner: "b, then a as fall back")

- (b) `computations/probes/h2_weak_vertex_electron/`: W = (σ+σ⁻¹)/(q[2]) and W′ = q²W, so it is
  mirror-symmetric. The passing set is unchanged from plain γγ: the electron must be V³ or V⁶, and the
  passing H₂ cells are bare and V³@4,5. Outcome (i), with no new information.
- (a) `computations/probes/h2_torus_electron/`: e = σ₀^m σ₁^t, with m odd in [−9, 9] and t = ±1. The atom
  passes level 6 only for m ∈ {7, 9} with t = +1, a q₀-dependent threshold predicted before the run. Those
  H₂ cells pass every level (bare and several bonds), and every mirror fails, so the rule is chiral on this
  family. The electron fails reading 3 on its own three strands. **OPEN (owner):** must an electron pass
  on its own? If yes, no torus electron survives. The passing set is a tail m ≥ 7, not a choice.

## 2026-11-15 — order test (h2_order_test, PR #7741)

Outcome (i), order-dependent. The torus T(2,7) electron passes H₂ only with the proton on the bottom strands;
with the electron on the bottom it fails levels 2–4 (it fails alone). The V³ electron passes in every order
(P = V³, V⁶). Higher levels also test upper particles. Still OPEN (owner): must each particle pass alone?
Owner leans to option 1 ("i think A").

## 2026-11-15 — OWNER RULING: each particle must pass alone

Owner chose option 1 on "Must each particle pass reading 3 on its own strands?": yes. Consequence: torus electrons
(fail alone) are excluded; the electron is in {V⁰, V³, V⁶} within the 3-strand γγ grammar, and H₂ bonds by exactly V³
(h2_gg_electron). Verdict is order-independent in every cell of h2_order_test. Which power is the electron stays OPEN.

## 2026-11-15 — symmetry and mirror-electron probes (PR #7741, af40380ef81)

gg_symmetry: inverse/mirror/swap of Vᵏ keep the full level-3 characters and the pass-alone set (k = 3, 6, 9 in 1..9),
but change the level-2 restriction (V³: χ_(1,1) 1.0112 vs V̄³ 0.9830). Pre-registered check S0 failed at level 2.
h2_mirror_electron: electron V̄³, V̄⁶, V⁹, V̄⁹ with nucleon V³/V⁶ → passing bonds exactly {bare, V³@4, V³@5}.
So H₂ cannot select the electron. Still OPEN (owner card pending): which observable decides the electron.


## 2026-11-15 owner ruling (thread 'Map SM and eightfold way', decision card): D-H2 restated at the pair level
D-H2 = no stays for single letters (flip_ne_swap). Added: on γγ pairs the swap ι: σ ↦ −σ⁻¹ sends V = σᵢσᵢ₊₁⁻¹ to V̄ = σᵢ⁻¹σᵢ₊₁ (signs cancel on even words), so the pair orientation bit V/V̄ IS the chirality mirror. Flavour must come from elsewhere (n ≥ 4 lead, qou-wkcd). Lean lemma ι(V)=V̄ not yet written. Evidence: PR #7741 gg_two_orientations (03b13f15561), gg_decay (6ff2aaaa8bf).

## 2026-11-15 — 4-strand γγ grammar (branch claude/gg-four-strand-2026-11-15, 1d8f88a737c)
Reading 3 on H₄, vertices V/V̄ at sites 0,1, m=1..6. Pass counts 0/4, 0/16, 16/64, 32/256, 0/1024, 518/4096. Passing is fixed by the SITE PATTERN (000,111; 0101,1010; rotations of 000111) and is nearly blind to V/V̄ orientation; six mixed-site m=6 words are the exception. Site pattern is a new binary label beyond the pair bit; its relation to the σ₃-eigenline flavour (qou-wkcd) is untested. Scope (a).

## 2026-11-15 — J₄-projected reading 3 (8f8c472b110, PR #7950)
454 m=6 passing words with a site-1 vertex, (3,1) rep from PR #7957. 448 pass in every J₄ sector (all 111111 and 000111-rotation words). The six mixed-site words fail: tr(Jb w Jb) ∈ [−0.40, −0.20]. Two rotation words (V1.B0.V0.B0.B1.V1, B1.V0.B0.V0.V1.B1) give d_a = 1 and flip = 0 (identity on Ja). Scope (a).

## 2026-11-15 — reading 3 tracks pure braids (c8b20019919, PR #7950; post hoc)
At m ≤ 6 on 4 strands: every pure γγ word passes reading 3 (560/560); the only non-pure passes are the six mixed-site words, which fail the J₄ projection. So J₄-projected reading 3 ⟺ pure braid. At q = 1 it is S₄ character theory under convention D. Open: a uniform bound in q−1 (pure words of length m pass for q ≤ 1 + c/m) and whether it holds for m > 6. Lean (7fd7a7ec2de): site-0 vertices fix Ja; two strand-4 words commute with J₄.

## 2026-11-15 — PR #7950 merged (rebase, main d0f681f5be9)
- Amendment 3 (q-threshold on pure γγ words, 4 strands): m(q* − 1) ≥ 1.187 on m ≤ 12 (m = 9, 12 sampled); first failure always level-2 χ_(1,1).
- Lean `QOU.QuarkState.GammaGammaFourStrandPureBound.pure_gg_reading3`: every pure γγ word of length m passes reading 3 for 1 ≤ q ≤ 1 + (1/12)/m. Sorry-free; axioms propext/choice/Quot.sound. Generic lemma `QOU.MathlibExt.ListProdPerturbation.prod_perturb`.
- Still open: a sharp constant (measured ≥ 1.187 vs proved 1/12), whether long pure words fail at q₀ (the bound reaches q₀ only for m = 1), and pure ⟺ pass for m > 6.

## 2026-11-15 — amendment 4: pure ⟺ pass FAILS at q₀ for long words (c0e1d67e816, branch claude/gg-pure-long-words-q0-2026-11-15)
At q₀ (proton, conv D, 40 dps). Exhaustive m = 7, 8: every pure word passes (min level char 0.50999), but 208 non-pure words pass at m = 8. Powers u^k of the 560 pure u (|u| = 3..6, k ≤ 10): 18 have a failing power, earliest at length 24 (u = V0.B0.V0.V0.B0.B0, k = 4). Seeded samples: pure fails 1/2000 at m = 24, 6/2000 at m = 30; non-pure passers 9 → 80 from m = 10 to 30. So pure ⟺ pass is false at q₀ in both directions. Still open: the shortest failing pure length (9..23 only sampled), and the sharp constant. Scope (a).

## 2026-11-15 — amendment 5: shortest failing pure word at q₀ (dbdcdebf265, branch claude/gg-shortest-failing-pure-2026-11-15)
Every pure word of length ≤ 11 passes reading 3 at q₀ (exhaustive; min level char 0.3200 at m = 11). Squares of pure words of length 9, 10, 11 fail 3, 10, 34 times, so the shortest failing pure word found has length 18, e.g. (B0.B0.V0.V0.B0.B0.V0.V0.B0)². Open: lengths 12–17 (only powers tested). Scope (a).

## 2026-11-16 amendment 6 (PR #8122, issue #8121)
Exhaustive m=12: 1,351,680 pure words, 0 fail (min level char 0.0232). Seeded 20,000 per m=13..17: 0 fail. Every pure word of length <= 12 passes reading 3 at q0; shortest known failing pure word stays length 18. 13-17 sampled, not enumerated.

## 2026-11-16 electron observables (PR #8126, issue #8125)
V^0/V^3/V^6 are the unlink / Borromean (vol 7.3277) / L12a1882 (vol 21.6316). All 3-component, zero linking, amphichiral: none is chiral. On (2,1) V is a rotation, 2cos(theta) = -1-h^2. Which power is the electron is an owner ruling (card posted).


## 2026-11-16 twist recheck + trefoil (PR #8128)
L± added: pass ⟺ pure (5460 words). H₂ with chiral electrons σ₁², V⁻¹L₋, L₊V⁻¹, L₋V⁻¹: bare passes, bond V³@4,5 always; σ₁² also V²@4. Trefoil fails reading 3 alone and bound; negative trace is exact in q (2-strand char product (−1)^k; (2,1) trace −1), so readings 1/2 and any q fail too; only z=q truncation escapes. Electron power ruling held by owner pending this.

## 2026-11-16 08:30Z — full-photon stage 3, bound-electron shift (PR #8128)
- Stage 3: full-photon γγ words (B₃, L± included), length ≤ 7. Knots 0/720 pass, pure 372/372 pass, 2-component 1214/3280 pass by placement. The site reading is not conjugation-invariant. The conjugation-invariant reading 3 gives pass ⟺ pure exactly.
- Owner, 08:16Z: "bound electrons q power shifted". Measured: the handed electrons σ₁², L₊V⁻¹ (χ₃ = q₀²) and V⁻¹L₋, L₋V⁻¹ (q₀⁻²) against free V³ (χ₃ = 1); χ₍₂,₁₎ = 2.04371 for all four.
- Owner, 08:20Z: no virtual photons in qou. Card, 08:21Z: option A, the q^{±2} shift. Read as one prior entangled γγ pair (L term × V⁻¹) across p|e. Stage 4 pre-registered (3f6f5a66d4b), running.
- STANDBY backups (owner, 08:22Z): (i) put the q² on the bond letter, with the electron staying V³; (ii) unseen emitters at the exceptional divisor = the conjugation-invariant reading.

**2026-11-16 (PR #8128, 04e78f0 / 8519534).** Connected-part principle formalised: `connected`, `connected_eq_zero_of_split` (sorry-free) in observations/virtual-subword.lean. Borromean three-party Jones cumulant exact: log(1 − (t−1)⁴(t²+t+1)/(t²(t+1)²)) ≈ −¾(log t)⁴, pairs 0. Stage 4: entangled pair admissible but reading 3 does not discriminate it from a self-twist or no pair (scope a). Stage 5 (6-node ring) pre-registered, not run. Open: t↔q dictionary; whether φ is b₃.
