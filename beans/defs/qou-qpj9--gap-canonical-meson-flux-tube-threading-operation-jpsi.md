---
# qou-qpj9
title: 'GAP: define canonical meson flux-tube threading braid (J/ψ underived)'
status: in-progress
pr: 8196
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-qcd
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-10-10T07:16:06Z
parent: qou-8lxd
---

## The wall

J/ψ = c̄c targeted as a hyperbolic bound-state braid volume
(`computations/jpsi_boundstate_mass_probe.py`,
`docs/audits/2026-08-02-jpsi-boundstate-mass.md`, branch
`claude/jpsi-boundstate-mass-2026-08-02`).

**In-range but underived.** With the scale fixed only on the proton
(Borromean → 938 MeV, 128.044 MeV/Vol), J/ψ needs Vol ≈ 24.19 and η_c
needs Vol ≈ 23.30 — both reachable by simple hyperbolic braids (positive:
distinguishes J/ψ from the neutrino's scope-(b) volume exclusion). But **no
derived c̄c braid**:

1. The proton's own family `(σ₁σ₂⁻¹)^k` misses J/ψ at every integer winding
   (k=6→2770, k=7→3336; J/ψ=3097 falls between).
2. The volume spectrum is dense near target (~4% of 196 simple braids land in
   the 230-MeV band).
3. J/ψ and η_c — the same c̄c system split by only 3.7% hyperfine — are best-fit
   by DIFFERENT-topology braids (4-str `(σ₁σ₂⁻¹σ₃)⁴`→3085 vs 5-str
   `(σ₁σ₂⁻¹σ₃σ₄⁻¹)³`→2964). Per-state fitting signature.

## The precise open item

**"Thread c̄c through the gluon T(2,9) color tube" is topologically
under-defined.** Satellite/companion, cable, connected-sum (non-hyperbolic),
and strand-insertion each give a different volume; the framework specifies no
canonical operation. A prediction requires a **single canonical parameter-free
topological operation** that fixes strand count + insertion sites + winding from
the c̄c + gluon quantum numbers *without reference to 3097 MeV*, then check once
against J/ψ AND η_c jointly (same base braid, hyperfine as perturbation).

## Suggested next honest step

Derive the meson flux-tube operation from the proton's 3-tube Borromean vertex
by the Y-junction → single-tube reduction (baryon → meson). If that reduction
fixes a unique braid a priori, it is a genuine derivation; check it once.
Anything that picks the braid to land on 3097 is a fit and worthless.


## 2026-08-24 — this bean's "suggested next honest step" is ALREADY DONE, and one of its obstructions is phantom

**Read this before working the bean.** The step recorded above — *"Derive the meson
flux-tube operation from the proton's 3-tube Borromean vertex by the Y-junction →
single-tube reduction"* — was **attempted and closed** on 2026-08-02
(`docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md`, PR #4614,
sorry-free `MesonFluxTubeReduction.lean`). It is a **scope-(b) structural
exclusion**: the literal reduction takes strands 3 → 2, `B₂ ≅ ℤ` is abelian, so
every 2-strand closure is `T(2,k)` with `Vol = 0`. Do not redo it.

### Correction to that audit (PR #5659, this branch)

It records **two** independent obstructions. **One is not real.**

It claims the corpus assigns charm two incompatible windings — `T(2,5)` and
`T(2,7)` — and flags the conflict for canonical-watcher. Both tables say
**T(2,5)**. The reported `(2,7)`/`7₁` is the value on the **preceding line**:
line 8 is the **tau lepton** `| 𝔎_τ | septafoil | 7₁ | τ⁻ | τ⁺ |`. The audit read
line 9's label with line 8's knot.

Verified: `git log -L 9,9` shows the line was **created** as `(2,5)`
(`e54ffbca0a`); `git log -S` finds no commit that ever wrote a charm `7₁` row;
corpus-wide, charm maps to 7 nowhere.

**The correction makes the surviving obstruction HARDER.** With charm fixed at
n = 5 there is no n = 7 alternative, so `D {5,3}` is an **exact** multiset
collision with `K {3,5}`.

### The "missing" T₃ grading is in the corpus, as σ

Table 2 read whole:

    gen 1   u = T(2,3)      d = T(2,3)^σ
    gen 2   c = T(2,5)      s = T(2,5)^σ
    gen 3   (top deprec.)   b = T(2,7)^σ

**σ present iff down-type — 5/5 quark rows.** `T_{m,n}^σ = T_{m,-n}`. So charm
and strange are a knot and its mirror, not the same object. The degeneracy is
`windingContent` **discarding σ** in its projection to `Multiset ℕ` — a lossy
projection, not an absent structure.

**Caveat, do not over-read:** σ is overloaded (it also marks
particle/antiparticle — electron vs positron). Whether table 2's σ *is* T₃ or is
notation reuse aligning 5/5 is the open question. A pattern is not a derivation.

### What is actually still open here

The braid is still not canonically fixed and `m_D` / `m_J/ψ` are still un-checked
(deliberately — checking now would be the per-state fit). The refined target is
narrower than this bean states: **lift `windingContent` to carry σ**, rather than
import a `T₃` from the weak `T(3,5)` sector. That work is owned by `qou-mesont3` /
`qou-20sx` / `qou-2udt`; intent posted there.

## 2026-08-25 — the tool this bean needs is IN THE LIBRARY, and the heavy end is bounded

Probe: computations/meson/meson_braid_syllable_bound_probe.py
Witness: meson-braid-syllable-bound.witness.json (3 assertions, pass)
Audit addendum: docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md

That audit's Literature section says the library carries 'NOTHING on the
classification or volumes of closed 3-braids, which is exactly the tool
Obstruction A needs', and flags its own entries as 'search-result summaries,
NOT READ PAPERS ... constants must be checked before use'.

The library DOES carry it: library/arxiv-1406.7337v4/ = Giambrone,
'Semi-Adequate Closed Braids and Volume' — THE SAME ARXIV ID that section
links as an unfetchable external result. Read from the ingested copy:

  Thm 1.2  v8*(s-1) <= vol(S^3\K) < 4*v8*s   [A-adequate closed 3-braid]
  Thm 3.1  s = t_-(D) = #{negative syllables}, read off the ORIGINAL word
  Lem 2.1(1)  every negative exponent r_i <= -3
  Cor 1.1  volume also bounded by the colored Jones stable penultimate coeff

  v8 = 4*Catalan = 3.66386237671 (ideal OCTAHEDRON). 2*v8 = 7.32772475342 =
  the corpus's own Vol(Borromean) = 8G. NB the first draft wrote 8*Catalan
  and the tie-to-corpus assertion caught it — the Lambda-vs-Cl_2 trap class.

CONSEQUENCE 1 — 'positivity is the culprit' becomes STRUCTURAL.
Sublemma 2.1's proof: 'Condition (2a),(2b),(2c) of Lemma 2.1 imply that BETA
CANNOT BE POSITIVE. Because positive syllables of beta are cyclically
neighbored by negative syllables' — and that neighbouring IS Stoimenow's
classification of A-adequate closed 3-braid diagrams (Prop 2.1). A fully
positive 3-braid is structurally excluded from the family, s = 0. The corpus
braid M = (s0 s1)^2 s1 s0 is entirely positive => s = 0. s is the dial.
SCOPED: a positive braid is OUTSIDE the family, so Thm 1.2 EXCLUDES it rather
than predicting its measured Vol=0. Agreement, not identity.

CONSEQUENCE 2 — the heavy end IS bounded (that audit said it was not).
Inverting Thm 1.2, with >=3 negative crossings per syllable from Lem 2.1(1):

  meson   Vol*rho   s window   >= neg crossings
  pi+-      2.681   [1, 1]      3      <- SINGLE VALUE
  K+-       9.484   [1, 3]      3
  eta      10.525   [1, 3]      3
  D0       35.827   [3, 10]     9
  eta_c    57.326   [4, 16]    12
  J/psi    59.497   [5, 17]    15

The pion window is a single value: any A-adequate closed-3-braid pion
candidate has EXACTLY ONE negative syllable, >= 3 negative crossings —
against a current corpus braid with zero and 6 positive crossings.

SCOPE: (a) NECESSARY conditions on a candidate space. No braid derived,
proposed or mass-checked. Obstruction A untouched and OPEN. A candidate
outside Giambrone's family is uncovered by these numbers, not excluded.

NEXT, and the better lead: Cor 1.1 bounds volume by the colored Jones stable
penultimate coefficient — and this framework computes colored Jones AS MARKOV
TRACES (J_L(q) = tr_M(rho(beta_L))). A bridge from machinery the corpus
already has to a volume bound, with no braid word in between. Not attempted.

## SELF-CORRECTION, same day — the family excludes the corpus's own carriers

My addendum scoped its windows as 'CONDITIONAL on the target braid lying in
Giambrone's family' — correct, and written before the numbers — but did not
say HOW RESTRICTIVE that family is. It is very.

Lemma 2.1(1) requires EVERY negative exponent r_i <= -3. The corpus builds
braids from single crossings:

  figure-eight (s1 s2^-1)^2   MUON,   Vol 2.0299   neg exps -1,-1      OUT
  Borromean    (s1 s2^-1)^3   PROTON, Vol 7.3277   neg exps -1,-1,-1   OUT
  meson M = (s0 s1)^2 s1 s0                        none (positive)     OUT
  trefoil s1^3                                     none (positive)     OUT

So the family contains NEITHER of the framework's two load-bearing hyperbolic
carriers. The syllable windows stay valid for their family, but that family
holds none of the corpus's anchor manifolds, so 'the heavy end IS bounded'
oversells it. Correct reading: 'IF a candidate lies in this family, THEN...'

CAVEAT ON THE CAVEAT (softens it): Lemma 2.1 constrains a DIAGRAM, not a link
type. A different word for the same link might satisfy it. Not settled here,
and not settleable by inspecting the canonical words. So: 'the corpus's
CANONICAL WORDS are outside', not 'these links are outside'.

WHAT IT IS GENUINELY EVIDENCE FOR, and this is worth more than the windows:
a structural mismatch between the framework's braid vocabulary (single
crossings, +-1 exponents) and the hypotheses of the closed-3-braid volume
literature (>= 3 same-sign crossings per syllable). That tells you which
theorems can apply before more of that literature gets imported.

RETAINED: Consequence 1 (positivity => outside the A-adequate family) is
unaffected — it is a statement about positive words and M is positive. The
v8 = 4*Catalan fix and its tie to the corpus Borromean volume stand.

2026-08-25T21:0xZ — LINK LEVEL, the question the retraction named.

Searched the conjugacy class (Markov-I orbit; the closure and hence Vol(K)
depend only on it) for a representative meeting Ito Thm 2's [beta]_D >= 3.

CONTROL: 4_1 figure-eight is genuinely hyperbolic (Vol 2.0299, the muon
carrier) and IS a knot, so Thm 2 applies by hypothesis if the floor condition
is reachable at all. Result: floor 0 as written, 0 across all 118097
freely-reduced conjugators of length <= 10 in B_3. Positive control
(Delta^6 s1 s2^-1) reaches 3; raising control (Ito's own pair, searched from
the low side) goes 0 -> 1. So the null is about the class, not the search.

READING: the earlier negative was aimed at the wrong target. Ito's threshold
sits at 18 crossings and small hyperbolic knots live below it -- a statement
about the THEOREM'S DOMAIN, which is measurable, unlike the retracted claim
about the framework's capacity.

ALSO corrects a lead that landed on main as b437d3bb7e: 'small floor is the
regime where closures tend to be torus or composite'. Ito Prop 4 and Remark 4
(Menasco-Nakamura) give composite => small floor; that lead uses the converse,
and 4_1 refutes it. Their primary conclusion is untouched (monotonicity), and
Prop 4 read forwards supports it. Pointer added to their doc.

SCOPE (a): a search. Class supremum not computed; no Malyutin bound invoked
(not in library/, so path 5 cannot support citing it); B_3 rests on Ito's one
stated example that stabilisation lowers the floor; Borromean row is a LINK,
excluded by Thm 2's hypothesis.

Obstruction A unchanged. PR #5782 (rebased; the library ingest is gone from it
-- main landed a better ingest of the same 7 docs).

2026-08-25T22:12Z — PR #5782 MERGED to main (1f68a7c7e8).

Landed across seven addenda on
docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md:

  A3  link-level search: 4_1, genuinely hyperbolic, floor 0 across 118097
      conjugates in B_3.
  A4  Obstruction A splits. (1) the atom object is NOT A LINK -- H_n(q)
      outside im(rho), 2A+1 averaged letters, measured at 2H/3He/4He; no
      topological quantity applies, about KIND. (2) the knot-dictionary
      carriers ARE links and sit below Ito's reach, about SCALE.
  A5  the conjugacy bound was IN THE CORPUS all along (Ito Prop 2(2), from
      [MN]/[Ma]): search -> PROOF, scope (a) -> (b). My path-5 grep hit only
      INDEX.md, which is one line per document and cannot see a result cited
      INSIDE a held paper.
  A6  'Same Markov class' in per_atom_hyperbolic_volume_witness.py cannot
      hold -- a non-braid has no Markov class. Corrected; no number moved.
  A7  p/n's 'principled-derivation' IS sound (registry T_w sigma-braid word
      via hp_volume_of_link_closure) -- my suspicion failed. But the atlas
      provenance block's 'no entry is maintained by hand' is UNENFORCED:
      both credited producers are deprecated. -> bean qou-4b6g.

Probes: _dehornoy.py, meson_braid_dehornoy_floor_probe (3),
meson_braid_conjugacy_floor_search_probe (4),
meson_braid_floor_conjugacy_bound_probe (4),
atom_word_braid_letter_census_probe (3). All assertions pass.

STILL OPEN and unchanged by any of it: Obstruction A itself. T(2,n) torus
closures have Vol = 0. Nothing above touches that.

## Progress (2026-11-16, PR #8196)
- [x] Formalized `minNegativeCrossings`, `syllableVolumeWindowMultipliers`, `negative_crossing_lower_bound`, and `pion_and_charmonium_syllable_bounds` in `folio/quantum-observable-universe/lean/QOU/Eightfold/LeptonReadoutHiggsScaleMesonSyllableAndIcosahedralOrbit.lean` + 50-dps mpmath witness (`qou_qpj9_negative_syllable_volume_window`) in PR #8196 (`38b68fa660bb34e2ffb7a2e1a09e5c4f5308e2cf`).
