---
# qou-d7h1
title: 'GAP: Eightfold Way flavor SU(3) from QOU components — distinguish from colour SU(3), then derive octet/decuplet organization'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-02T17:29:24Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

Near term: inventory the existing I3/Q/Y, strange-quark, and three-strand colour ingredients; prove the corpus already has the right state labels for u,d,s-level organization.

Medium term: build a flavor-SU(3) candidate action on the hadron state space and test baryon-octet / meson-octet / decuplet decomposition without conflating it with the colour module.

Long term: connect the flavor action, if it exists, to the Bring/icosahedral side (A5 / S5 / W-plane geometry) as a derivation route rather than a one-number analogy.
2026-08-02 concrete inventory.

- `sm-gauge-truncation.md` already separates the three roles cleanly: `Q` is derived, `I_3` is matched by the writhe ladder on the nucleon doublet, and `Y` remains open because proton and neutron share `Y=+1` while their writhes differ.
- `strand-twist-datum.md` gives the best current candidate for the missing second invariant: twist is independent of writhe, and the candidate hypercharge is `Y_t = 2(Q_twist - I_3)`, but only as a battery candidate.
- `strangelet-crossing-energy-proof.md` and `strangelet-intro.md` already carry usable flavor labels: `d = T_{2,3}^σ`, `s = T_{2,5}^σ`, and baryonic `(u,d,s)` units use the `{+,-,-}` charge partition.
- Colour SU(3) is partially closed elsewhere: `sm-colour-stabilizer-action` plus `OctonionColourActionBaseModule.lean` already realize the abstract colour-action class on `O = C ⊕ C^3`; the open piece there is the action on QOU's own Hecke three-strand state space.

- There is already a q=1 SU(3) symmetry anchor in the corpus: completed bean `1ict` resolved that Elliott SU(3) sits at the q=1 corner of the existing Schur-Weyl / Wedderburn shell picture, via mutual centralizers on `(ℂ^3)^{⊗ n}`. So the flavor route is not starting from zero representation theory.
- There is also already a baryon-label precursor table: `predicted-spectra/linking-relations-table-table3-data.md` lists `p,n,\Lambda,\Sigma^\pm,\Xi^0,\Xi^-,\Omega^-` as Borromean `(u,d,s)` triples. But this is NOT yet an Eightfold-Way derivation: it mixes octet and decuplet content (`\Omega^-` is decuplet) and omits the full weight-multiplet organization (e.g. `\Sigma^0`, meson octet, decuplet structure).

- Gap list after corpus grep: no relevant `meson octet`, `baryon octet`, `decuplet`, or `weight diagram` layer is present in the content tree, and the existing baryon-label table does not yet include a `\Sigma^0` row. So the corpus currently has state labels and one q=1 SU(3) anchor, but not the Eightfold-Way multiplet geometry itself.

## Owner re-ask (2026-08-02): "missing 8-fold way. categorical?"

Yes — the tracked route IS categorical, and it is this bean. The
Eightfold Way should fall out of the **q=1 corner of the existing
Schur–Weyl / Wedderburn shell picture** (Elliott SU(3), bean `1ict`):
mutual centralizers on $(\mathbb{C}^3)^{\otimes n}$ give the flavor
SU(3) multiplets categorically, with the octet/decuplet split being the
Wedderburn block decomposition of $(u,d,s)$ Borromean triples. The one
missing categorical piece is the **weight-multiplet geometry** (octet vs
decuplet organisation, the $\Sigma^0$ row, meson octet) — NOT the SU(3)
representation theory, which is already anchored at q=1. Owner's
"icosahedral embedding on Bring's surface" hint is the geometric handle:
the $A_5\cong$ icosahedral / Bring-Jacobian $E^4$ structure is where the
flavor weight lattice should sit. Session: `qou-ywj9`.

## Colour-level measurement + the code-vs-Lean question (PR #5241, 2026-08-16)

Commissioned to re-open what PR #5234 closed on one measurement. Full writeup:
docs/audits/2026-08-16-colour-level-and-tln-compute.md (TASK 1).

**#5234's measurement CONFIRMED, independently.** Symbolically over Q(q),
z_2 = q^3/(q^2+1) exactly, so convention D IS level r=2. All 11 production
colour/strong paths resolve to that one z (closed_form_tau_M.markov_z,
hecke_symbolic.z_markov, pyhecke/gram.py:175 + :437, hecke-engine gram.rs:125,
color_weight.rs; the rest inherit). The color_tube_*.py family (8 files) uses
no z at all -- they build the 9-element colour-pair weight tensor W.
z_C solves z_r = z_C at r = 2.5995 (no integer). **z_3 appears NOWHERE outside
one probe** (ocneanu_param_from_fibre_dimension.py, nothing imports it) and one
audit comparison table.
Grep warning [CORRECTED 2026-09-05, bean qou-yk03 -- SEE BELOW, the original
named the wrong quantity]: the literal 0.44930482320583087 in many witnesses
is h_q, NOT z_3 (0.449304809090...) -- they differ at the 8th decimal.

CORRECTION. That literal is z_3 AT THE MUON ANCHOR, not h_q. Measured at
65 dps (probes/z3_muon_pin_vs_hq_misidentification_probe.py, 2/2):

    z_3 @ muon    0.4493048233034703126034   rel 2.17e-10  <- the literal
    z_3 @ proton  0.4493048090902078605552   rel 3.14e-8
    h_q = q-1/q   0.2090602987956393154308   rel 0.535     <- 53 % away

h_q is not a near miss; it is off by a FACTOR OF TWO, so 'they differ at the
8th decimal' is not a small slip inside a true statement -- the quantities are
not comparable. The 2.17e-10 on the muon row is the literal's own 17-digit
truncation.

The real content is MORE SERIOUS IN KIND and SMALLER IN EXTENT. These are not
two lookalike quantities; they are ONE quantity, z_3 = q^3/[3]_q, at the two
substrate anchors. The 3.14e-8 gap is the mu-p tension through z_3. That is a
LAYER STRADDLE, which AGENTS.md calls a defect regardless of size -- and the
warning as written tells an agent a muon-pinned value needs NO anchor check,
inverting the 2026-08-07 proton-by-default directive.

EXTENT: ZERO live producers. Five files carry the literal -- three under
computations/_deprecated/, and the other two are this bean and
docs/audits/2026-08-16-colour-level-and-tln-compute.md, i.e. the two sites
carrying the misidentification itself. The correct proton value appears in 21
files. A documentation correction, not a drain; nothing computed is wrong.

**bring_color_weighted implies NO level.** It is a per-bond scalar over the
A-1 nearest-neighbour bonds: p-p -> z, n-n -> z-h, p-n -> z-h(1/2-delta/4).
It CONSUMES z and never defines, derives or constrains it; no representation,
no fibre object, no row cap anywhere in it. So its canonicity under owner
ruling R3 says nothing about the level.

**The code-vs-Lean tension: THERE IS NONE — they are about different
objects.** Two things the cited line does not show on its own:
  1. FibreDimensionForcesTL.lean:69-71 is a PROSE REMARK inside a module
     docstring, under a heading literally titled "What this does NOT
     establish". Nothing below it formalizes the claim. The formalized content
     is entirely about the mass channel (ocneanu_param_eq_of_fibre_qdim,
     twoDimFibre_pins_h3_weights). So it is not "the Lean says colour needs
     three rows" — a comment says it.
  2. Production has no colour fibre at all (see bring_color_weighted above).
So the Lean remark correctly describes a not-yet-constructed object, and the
code correctly implements a different, weaker thing. Neither "code is wrong"
nor "Lean is aspirational" is right.

**Eightfold line: the numerological inference is DEAD; a structural test is
not.** "Level 3 is SU(3) and colour is SU(3)" stays unsound — the Wenzl tower
contains every SU(r). z_3's absence from production removes even the weak
circumstantial version.
BUT: ocneanu_param_eq_of_fibre_qdim is proved GENERAL IN N, not just N=2:
dim_q V = [N]_q  =>  z.[N]_q = q^N. So a genuine 3-dimensional colour fibre
would FORCE z = q^3/[3]_q = z_3, with no freedom and no fitting. The live test
is therefore:
  [ ] Construct a functor with a 3-dim fibre that actually realizes colour
      antisymmetry (the three-row block). This is the whole difficulty and
      nothing in the corpus does it.
  [ ] Its Markov parameter is then z_3 BY THE ALREADY-PROVED THEOREM.
  [ ] Check whether that functor reproduces colour phenomenology.
NUMEROLOGY FLAG ON THIS ENTRY: the above is a statement of what evidence WOULD
look like, not evidence. If it is later cited as support for the eightfold
line without step 1 being done, that citation is the error.
Scope (a): unsupported as stated, usual argument invalid; NOT structurally
excluded, and I have no invariant that would exclude it.


## INVENTORY DONE 2026-08-25 — the 2026-08-02 gap list is COMPREHENSIVELY STALE

This bean's near-term step was: inventory the I3/Q/Y, strange-quark and
three-strand ingredients and establish what the corpus already has. Done. The
headline is that the gap list below it no longer describes the tree.

The 2026-08-02 entry states: "no relevant meson octet, baryon octet, decuplet,
or weight diagram layer is present in the content tree, and the existing
baryon-label table does not yet include a Sigma-0 row."

MEASURED 2026-08-25, all four are present. The eightfold-way chapter carries 16
blocks:

  meson octet     prop:meson-octet-decomposition   (+ rem:meson-mass-splitting,
                                                    rem:vector-meson-nonet)
  baryon octet    prop:baryon-octet-decomposition
  decuplet        prop:borromean-decuplet, rem:decuplet-equal-spacing
  weight geometry prop:a2-from-three-strands (the A2 root system),
                  rem:q-deformation-weight-lattice,
                  rem:flavor-charge-assignments
  U-spin          rem:u-spin-coleman-glashow
  colour side     prop:color-su3-from-g2
  Schur-Weyl      prop:schur-weyl-eightfold

Sigma-0 IS present, in baryon-octet-decomposition (.md/.ts/.qa.json) and in
QOU/Eightfold/OctetWeightDegeneracy.lean. It is still absent from
predicted-spectra/linking-relations-table-table3-data.md, which is the table
the old entry was actually looking at - so that one clause is narrowly true
and the general claim built on it is not.

Do not re-derive the multiplet layer. It exists.

## THE ACTUAL BLOCKER FOR THIS BEAN'S OWN QUESTION: A NOTATION COLLISION

This bean asks to DISTINGUISH flavour SU(3) from colour SU(3). Measured, the
chapter does not distinguish them NOTATIONALLY at all:

  31 occurrences of SU(3) in eightfold-way/*.md
   0 of them subscripted
   corpus-wide there are only 4 subscripted forms (_{c}, _c, _R, _L), none in
     this chapter

So one symbol serves two different groups - colour SU(3) from
G_2 = Aut(octonions), and flavour SU(3) organising the multiplets - with the
distinction carried entirely in surrounding prose. Under AGENTS.md section
7aa that is a register collision of exactly the kind the notation-collisions
block forbids (compare its H_q ruling: "H_q alone = FORBIDDEN (collision)").

NOT FIXED HERE, deliberately. It is 31 sites across 12 math-bearing .md blocks,
each needing the render-QA battery and a sidecar refresh, and it is a change to
the paper's notation register - which AGENTS.md routes through the notation
content block, not through a chapter edit. Proposed: SU(3)_C and SU(3)_F, added
to notation-register.md + notation-collisions.md first, then swept. That is an
owner-visible convention decision, not a mechanical fix.

## WHAT THE COMPLEX-TYPE RESULT CONTRIBUTES TO THIS BEAN

Sym2GateComplexType.lean (this session) proves the mechanism the chapter had
only asserted, and it bears directly on the flavour/colour split.

color-su3-from-g2.md already says, correctly, that "the 3 and 3-bar are complex
conjugate (not self-dual)" and that "non-self-duality is what the Sym^2 gate
consumes". That was prose. It is now a theorem: the parity exclusion
(dimOfMult_ne_three_of_gate) runs through self-duality, and a complex-type
irrep whose conjugate is ABSENT passes the gate at any dimension, odd included
- witnessed at dimension exactly 3.

Consequence for this bean: a 3-dimensional FLAVOUR object is not barred by the
corpus's own parity invariant, and the property it must have is now named and
proved - complex type, conjugate absent. That is a genuine constraint on any
flavour-SU(3) candidate action this bean goes on to build, and it is sharper
than "must be multi-fibre".

Wired into eightfold-open-problems.md, where the exclusion is stated, so the
scope travels with the claim rather than sitting only in the Lean.

## STATUS

Near-term (inventory): DONE, and it overturned the recorded gap list.
Blocker surfaced: the SU(3)_C / SU(3)_F notation collision - needs an owner
convention decision before the medium-term "flavor-SU(3) candidate action
without conflating it with the colour module" can even be stated unambiguously.
Medium and long term: unchanged, open.


## RESEARCH 2026-08-26 — colour neutrality formalized as a Z/3 grading (PR #5810)

Attacked the COLOUR side of this bean's question, formalize-first, because the
constraint turned out to be structural rather than numerical.

CORPUS-GREP, and it is a good example of why topic-grep is not enough.
"triality" hits 22 files. A topic-grep stops there and concludes the corpus has
it. It does not: every one of those is either the zeta_3 ROTATION of the
three-strand Hecke datum (threeStrand_cubes_to_one) or the 3d-index triality of
the tetrahedron probes. Grepping the claim SHAPE -- "singlet iff", "contains a
singlet", a mod-3 condition on a tensor product -- returns ZERO across content/,
docs/, computations/, the ledgers and library/INDEX.md.

PROVED (QOU/Eightfold/TrialitySelectionRule.lean, 14 decls, sorry-free,
lean-direct exit 0 first attempt, no sorryAx):

  triality a b = a - b in Z/3;  Neutral a b iff it vanishes
  neutral_iff_mod            a % 3 = b % 3
  triality_add, neutral_add  a genuine grading: additive, closed
  hadron table               meson (1,1), baryon (3,0), antibaryon (0,3)
                             neutral; single quark (1,0), DIQUARK (2,0),
                             four-quark (4,0) NOT; observed tetraquark (2,2)
                             and pentaquark (4,1) neutral
  neutral_decomposition      every neutral combination IS m mesons + n baryons
    + converse               + n' antibaryons

The decomposition pair is the content: mesons and baryons are not merely
examples of colour-neutral states, they EXHAUST them -- the neutral monoid is
generated by (1,1), (3,0), (0,3), so there is no third kind of colour-neutral
composite to look for. diquark_not_neutral is confinement in this language: no
colour singlet in a two-quark object, for grading reasons alone, at any q, with
no dynamical input.

THE MODEL IS THE EQUIVALENCE and is labelled so: "vanishing triality iff a
singlet occurs" is standard SU(3) rep theory, cited [fulton-harris1991] s13,
NOT derived (Mathlib has no SU(3) type). Same register as
Sym2GateMultiplicity.sym2SingletCount. Everything below the definition is
derived.

A CONFLATION I DELIBERATELY DID NOT MAKE, recorded because it is inviting.
The Sym^2 gate files count singlets in Sym^2(W); this counts singlets in W.
Those are different questions. A baryon HAS a singlet in W -- the totally
ANTISYMMETRIC epsilon tensor, i.e. Lambda^3 -- about which the Sym^2 machinery
says nothing at all. I checked before writing whether the gate criterion and
the triality criterion could be unified and they cannot; two singlet-counting
statements about different objects sharing a word is exactly the arity slip
AGENTS.md "Grep the claim SHAPE" describes. The file states the separation
explicitly so a later reader does not merge them.

An earlier line of attack that DID NOT WORK, so it is not re-tried: I tried to
derive "flavour SU(3) cannot equal colour SU(3)" from the gate, on the argument
that identifying them puts a quark in 3 (x) 3 of one group, which contains 3bar
alongside 3 and so fails conjugate_pair_fails_gate. It does not: 3 (x) 3 =
6 + 3bar contains 3bar but NOT 3, so no conjugate pair is present and the object
passes. The argument is wrong and the identification is not excluded this way.

BEARING ON THIS BEAN, as a constraint and explicitly NOT an answer: triality is
a property of each SU(3) copy separately, so a quark carrying both a colour and
a flavour index has TWO independent gradings with independent neutrality
conditions, which collapse to one under an identification of the groups. That
is a structural difference the corpus can test rather than assert.
eightfold-open-problems.md line 32 stays open.

## NOTATION MEASUREMENT — my earlier "31 ambiguous sites" was WRONG

Reported to the owner as a blocker; re-measured properly, it is smaller and
partly a non-problem. Of 31 SU(3) occurrences in eightfold-way/*.md:

   17  already disambiguated -- 9 by the adjacent word ("flavour SU(3)",
       "colour SU(3)"), 8 by unambiguous mathematics (SU(3) subset G_2 can only
       be colour; "gluon octet")
    4  DELIBERATELY GENERIC -- "true of any SU(3)", "a theorem of SU(3)
       representation theory". These are about the abstract Lie group.
       Subscripting them would ASSERT a physical identification the sentence
       avoids: a sweep would introduce four errors, not fix four.
   10  genuinely bare, and several of those are unambiguous to a physicist by
       standard usage ("SU(3) breaking" is always flavour, "SU(3) gauge" always
       colour)

THE CORPUS ALREADY HAS A CONVENTION AND IT IS NOT THE ONE I PROPOSED.
observations/color-superconductivity-borromean.md writes
SU(3)_c x SU(3)_L x SU(3)_R -> SU(3)_{c+L+R} -- standard colour-flavour-locking
notation, LOWERCASE _c for colour, _L/_R chiral, the eightfold-way group being
the diagonal/vector subgroup. My proposed SU(3)_C / SU(3)_F contradicts it on
case and under-specifies on the flavour side. The notation register itself says
NOTHING about SU(3), so this would be an addition, not an overturning.

WHY IT IS AN OWNER DECISION rather than a cleanup: eightfold-open-problems.md
line 32 lists "flavour vs colour SU(3)" as OPEN. Leaving every occurrence bare
quietly suggests one group; subscripting every occurrence quietly asserts two.
Both beg the open question, in opposite directions. Recommendation put to the
owner: adopt SU(3)_c and SU(3)_F, register both, apply ONLY to the ~10 bare
sites where a definite copy is meant, leave the 4 generic ones bare, and add a
register note that the subscripts name the two ROLES rather than claiming the
groups are distinct as objects.


## SELF-CORRECTION, same session — the "testable structural difference" is NOT one

I recorded above, and wrote into TrialitySelectionRule.lean and PR #5810, that
triality gives a way to test the flavour-vs-colour identification: distinct
groups mean a quark carries one fundamental index of each, identified groups
mean two indices of one group, so the grading collapses and that is "a
structural difference the corpus can test rather than assert".

THAT IS WRONG, and it is now a proved negative rather than a corrected sentence.

If the groups are identified the quark's triality is 2, not 1, so neutrality
reads 2(a - b) = 0 instead of (a - b) = 0. But 2 is a UNIT in Z/3, so
multiplying the grading by it permutes the non-zero classes and fixes zero. The
two conditions are the same condition. Checked on the whole hadron table --
meson, baryon, diquark, four-quark, tetraquark, pentaquark -- and the verdict is
identical in every case.

Added to the file, sorry-free, lean-direct exit 0:

  trialityWeighted k a b                 = k * triality a b, k = indices per quark
  trialityWeighted_eq_zero_iff           weighting by a unit changes nothing
  identification_invisible_to_selection_rule
                                         the negative, general in (a,b)
  identification_agrees_on_hadrons       the table, as a corollary

WHY THIS IS WORTH HAVING rather than just deleting the wrong sentence: the
triality route is the FIRST thing anyone reaches for on this question, and it
is dead on arrival. The invariant itself is real and the confinement content
stands; what is now established is that the invariant is BLIND to the
identification. A discriminator has to look somewhere the Z/3 grading does not
reach.

So the open question is not narrowed by this work. The file closes one route to
it, which is a smaller and more honest claim than the one I made an hour ago.


## PROGRESS 2026-08-26 — Route B's T_1-vs-G_2 comparison is now a COROLLARY (PR #5810)

This bean records the chapter's argument that the octonionic SU(3) and the
icosahedral colour triple cannot both come from one construction, "since the
Sym^2 gate excludes the icosahedral colour triple T_1 while the G_2 route
passes it". That is a case analysis over two examples. The actual mechanism is
Frobenius-Schur type -- T_1 is a rotation rep of A_5 subset SO(3) and so REAL,
the Gunaydin-Gursey triple in Im(O) = R + C^3 is COMPLEX -- and neither of the
two existing gate files could state it: Sym2GateMultiplicity models FS = +-1
only, Sym2GateComplexType models FS = 0 only.

QOU/Eightfold/Sym2GateFSTrichotomy.lean unifies them over the full trichotomy
(12 decls, sorry-free, lean-direct exit 0, axioms [propext, Quot.sound] only --
not even Classical.choice):

  gate_forces_complex_of_dim_three   ANY dim-3 object passing the gate contains
                                     a complex-type irrep
  real_triple_fails_gate             the T_1 half, one line, no icosahedron
  even_dimOf_of_selfDual             recovers Sym2GateMultiplicity's conclusion
                                     in the unified language

So real and quaternionic constructions are excluded AS A CLASS, not as two
examples: passing forces real multiplicities to zero, quaternionic dimensions
are even, the total is even, and 3 is odd. Complex type is not one way among
several to reach dimension 3 through this gate -- it is the ONLY way.

Two standard inputs are carried as EXPLICIT HYPOTHESES rather than assumed:
QuaternionicEvenDim (an H-module has even dimension; Sym2GateMultiplicity got
this free from dim = 2j+1, there is no such formula here) and the self-duality
classification. That is deliberate -- the theorem then names exactly what it
needs, and no fact about octonions or icosahedra is among them.

GAP (i) IS UNCHANGED AND I WANT THAT ON THE RECORD. This does NOT prove the
Gunaydin-Gursey triple IS complex type; that remains the cited literature
decomposition, exactly as this bean says. The file establishes what complex type
BUYS and what real type COSTS. The input is still an input, and Route B still
needs it formalised or explicitly cited at the point of use.

WHAT IT CHANGES FOR THE ROUTE: the target is now sharper. Route B does not need
to argue about icosahedra at all -- it needs exactly one thing, that its triple
is complex type. Everything else follows. Conversely any future candidate that
is real or quaternionic is dead on arrival at dimension 3, without further
analysis.


---

## 🛑 THE BLOCKER IS ALREADY RULED — this bean is stale, not blocked (2026-09-05)

STATUS above says the `SU(3)_C / SU(3)_F` notation collision "needs an owner
convention decision before the medium-term work can even be stated
unambiguously". **That decision exists.**

`folio/quantum-observable-universe/notation/notation-collisions.md` carries a
full ruling, landed **2026-09-03** in `afec87d506` (bean `qou-gght`) with a
28-site sweep of the eightfold chapter:

> **`SU(3)` alone** = permitted only for a representation-theoretic statement true
> of any `SU(3)`. The two groups the paper uses are always subscripted:
> **`SU(3)_c`** (colour — the stabiliser in `G_2 = Aut(O)`, colour tubes, gluon
> octet) and **`SU(3)_f`** (flavour — meson/baryon octets, decuplet, quark
> flavour). Roman lowercase subscripts. **The reason is that eightfold-open-problems
> item 4 asks whether the two are the same, different, or groupoid-dual; a shared
> glyph presupposes an answer.** Legacy spellings are recorded as legacy and are
> **not** swept by this ruling.

That reasoning is exactly what this bean wanted. The ruling postdates this bean's
last update (2026-08-26) by **eight days** — nobody missed it; it arrived from a
different bean and this one was never updated.

**So the medium-term item — "state the flavour-SU(3) candidate action without
conflating it with the colour module" — is UNBLOCKED and agent-actionable.**

### Compliance, measured 2026-09-05

    canonical SU(3)_c                          16
    canonical SU(3)_f                          19
    legacy _c / _L / _R (declared, NOT swept)   6
    bare SU(3), no subscript                   45  across 22 files

The 45 bare are mostly the ruling's own carve-out: **20 sit in
`appendix-standard-model/`**, where they are the standard SM gauge triple
`SU(3) x SU(2) x U(1)` — universally written bare and true of any `SU(3)`.

### One genuinely NEW question, small and not this bean's

`observations/q-deformed-nuclear-models-comparison.md` uses **Elliott's `SU(3)`**
(3 sites, `\cite{elliott1958}`) — the harmonic-oscillator shell-model symmetry.
That is a **third** group: neither colour nor flavour. The register names only two.

It is currently disambiguated by the adjacent word "Elliott", which is the same
mechanism the register already accepts for `\zeta(s)` vs `\zeta_n`. **Proposed (not
applied — a register change is a convention claim):** add one line to
`notation-collisions.md` recording Elliott's `SU(3)` as a third, context-
disambiguated use, so a future sweep does not "correct" those 3 sites into `_c`
or `_f`.

### A measurement error of mine, recorded

I first reported **0** bare occurrences. That grep passed both `-E` and `-P`,
which GNU grep rejects as conflicting matchers — non-zero exit, no output, and
`wc -l` dutifully printed 0 with stderr suppressed. The true count is 45. A
suppressed-stderr pipeline reports a failed search as a clean result.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update — 2026-11-16 (`litlfred/qou#8155`, `f3af82fd1d99fc5eb05c0bd46bbd812b46330432`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/FlavourCartanOctetDecuplet.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Explicitly separates colour $\mathrm{SU}(3)_c$ (locked in the 1-dimensional totally antisymmetric baryon singlet $\Lambda^3(\mathbf{3}_c) = \mathbf{1}_c$, `weylDimAlt3 3 = 1`, carrying $I_3 = S = C = 0$) from flavour $\mathrm{SU}(3)_f$ (carrying $(2I_3, Y_f = B + S + C)$ across `baryonOctet`, `baryonDecuplet`, and `mesonOctet`).
  - Proves `su6_spin_flavour_56_and_condition5_split`: because $\Lambda^3(\mathbf{3}_c) = \mathbf{1}_c$ is totally antisymmetric, Fermi statistics forces the $L = 0$ spin-flavour wave function in $W_{\mathrm{flavour}} \otimes V_{\mathrm{spin}} \cong \mathbb{C}^3 \otimes \mathbb{C}^2 \cong \mathbb{C}^6$ to lie in $\mathrm{Sym}^3(\mathbb{C}^6)$ of dimension $\binom{8}{3} = 56$. Pairing identical $S_3$ Young diagrams $(3) \otimes (3)$, $(2,1) \otimes (2,1)$, and $(1^3) \otimes (1^3)$ gives $10 \times 4 + 8 \times 2 + 1 \times 0 = 40 + 16 + 0 = 56$ — deriving the ground-state baryon octet ($J = 1/2$) and decuplet ($J = 3/2$) while excluding an $L = 0$ flavour singlet because $\dim \Lambda^3(\mathbb{C}^2_{\mathrm{spin}}) = \binom{2}{3} = 0$.
- **Witness (`computations/probes/flavour-cartan-octet-decuplet-degeneration.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8155, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-25: "content(qou-d7h1): wire the proved gate scope into the chapter; inventory overturns the recorded gap list"). The work may be partly or fully done. Read the bean before you close it.
