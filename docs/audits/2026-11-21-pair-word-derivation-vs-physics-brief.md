# The β⁻ pair-creation word: what is derived, what matches physics, what each ruling changes

Bean `qou-99qc`. Decision brief for the owner (Carl), 2026-11-21, on PR #8696
(`docs/audits/2026-11-21-beta-pair-creation-word-proposal.md`). **Nothing here is ruled.** No
candidate is chosen or ranked by `Q_β`, by any residual, or by CODATA.

You asked: *"You need to provide more context and implications downstream before ruling. What is
derivation? What is aligned to physical?"* You lean toward **(b)** require chirality, then study
`V₂V₀V₁V₂` on five strands, and **(d)** rule first whether mirror vertices belong to the γγ
grammar. This brief answers your three questions for each option.

## The decision, in two sentences

Two premises need you, because no proved corpus result fixes them:

* **(d)** Is the γγ production grammar closed under the mirror? In other words, is `V̄ᵢ = σᵢ⁻¹σᵢ₊₁`
  a pair-production vertex alongside `Vᵢ = σᵢσᵢ₊₁⁻¹`?
* **(b)** Must the word that creates the e⁻ν̄ pair be one-directional, i.e. have a zero
  `p⊗e⁻ → n⊗ν` block?

(d) should come first. It changes which words exist for every γγ selection in the corpus, the
nucleon included. (b) only changes which β⁻ words survive.

## Terms used throughout

* **Vertex `Vᵢ = σᵢσᵢ₊₁⁻¹`.** One positive crossing next to one negative crossing. It is the
  photon's fourth term, `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (owner-ruled photon form; the old
  `σ₀σ₁` fourth term is wrong).
* **Mirror vertex `V̄ᵢ = σᵢ⁻¹σᵢ₊₁`.** The same vertex with both crossings flipped.
* **γγ word.** A word in the Lean predicate `GammaGammaWord`
  (`QOU/Mass/GammaGammaWordSelection.lean`). It admits products of `Vᵢ` only, so its first letter
  is always positive.
* **Reading 3.** The confinement positivity test the owner selected on 2026-09-12 and applied to
  the whole word on 2026-09-13: every Markov-weighted Wedderburn character is `≥ 0`. Under
  convention D only the two-row shapes count.
* **CC block.** The charged-current matrix block `n⊗ν → p⊗e⁻`, taken on the Jimbo representation
  under premise L.
* **Chiral** (the word as #8696 uses it). The reverse block `p⊗e⁻ → n⊗ν` is zero. This is a
  statement about the **direction** of the process. It is **not** handedness; see (b).
* **Premise L** (#8673, open, undecided). The lepton strand carries the colours `ν = u` and
  `e⁻ = d`. Every CC statement uses it.
* **Tiers.** *Proved* means a sorry-free Lean result or an exact `ℚ(q)` identity. *Ruled* means an
  owner ruling. *Definition* means a choice of notation with no content. *New choice* means a
  premise that nothing in the corpus forces.

## What the corpus has already fixed (the shared base)

| item | tier | where |
|---|---|---|
| words are selected by γγ production plus the confinement SDP; no census | ruled 2026-09-08 | bean `qou-ales` |
| reading 3, on the whole word | ruled 2026-09-12 / 09-13 | `qou-ales`, AGENTS.md §Precision goals |
| convention D, `z = q³/(q²+1)` | ruled 2026-08-15 | AGENTS.md §q₀ anchor convention |
| photon form `γ(φ)` with fourth term `σ₀σ₁⁻¹` | ruled | photon ruling, applied in #8696 |
| left line for `q > 1` | ruled 2026-11-15 | `LeftLineDefinition.lean` |
| one-crossing weak vertex `W − σ = −(q−q⁻¹)·P_L` | proved at one crossing; a **conjecture** for the weak knot `T(3,5)`, whose right-line share is −9.33 % | `docs/audits/2026-11-15-weak-vertex-left-projector.md`, `WeakVertexLeftProjector.lean` (merged) |
| charged current `n⊗ν → p⊗e⁻ = (q²−1)·T⁺` for the passage `σ₀σ₁σ₂`; zero in reverse | proved, on an **open** PR | #8638 (open) |
| nucleon element `β_Bor = V³`, the unique cost-minimal γγ word passing reading 3 | proved for the V-only grammar | #8564 (merged), `GammaGammaSdpQBetaBase.frobeniusSelected_ten_unique` |
| scored `Q_β` = the T³ flavour split `ε_flavour(V³)` | ruled 2026-11-20 (D1 = A) | #8586, `per_observable_100x_status.py` |
| up quark = unknot strand of `B₃`; the trefoil is its lepton partner | ruled | #8677 (merged) |
| quark lengths 3/5/7 are lepton-partner generation labels | ruled | #8698 (merged) |
| right-handed fields are matter⊗Higgs composites on the right line (`e_R` = lepton⊗Φ̃) | ruled today, PR not merged | #8694 (open) |

Two items in this table rest on **open** PRs, #8638 and #8694. Read every "derived" below that
cites them as "derived on an unmerged branch".

---

## (d) Are mirror vertices `V̄ᵢ` γγ vertices?

### What is derived, what is a definition, what would be new

* **Definition, not a finding.** `GammaGammaWord` admits `Vᵢ` and not `V̄ᵢ` only because the
  inductive type is written that way (`vertex i = [(i,+), (i+1,−)]`). No theorem excludes `V̄`.
* **Proved: the proved invariants do not distinguish them** (#8696, `PairCreationExclusions.lean`).
  - `V̄ᵢ` has writhe 0 and alternating character 1, the same as `Vᵢ` (`writhe_mirrorW`,
    `altChar_mirrorW`).
  - The bar involution `q ↦ q⁻¹` maps `Vᵢ ↦ V̄ᵢ` (`barW_vertex`), so the ruled grammar is not
    bar-closed (`gammaGamma_not_bar_closed`).
  - At the element level the mirror vertex is already a photon: `1 + c·V̄₀ = γ(hc, −hc, c)`
    (`one_add_mirror_eq_photon`). The element-level reading of γγ is therefore vacuous, because
    photons generate all of `⟨σ₀, σ₁⟩` (`photon_adjoin_eq`).
* **Measured earlier, not proved.** The swap `ι: σ ↦ −σ⁻¹` sends `V` to `V̄` on even words, so the
  `V`/`V̄` bit is the chirality mirror (bean `qou-a1hh`, 2026-11-15; the Lean lemma `ι(V) = V̄` is
  not yet written).
* **Would be new.** Ruling either way is a new choice. *Out* keeps the current definition and
  adds a stated reason for it. *In* changes the definition.

### What is aligned with physics

* **Pair production in the SM is parity- and C-symmetric.** γγ → f f̄ is a QED process. QED
  conserves P, C and T separately, so the antiparticle and the mirror process are produced with
  equal amplitude. If `V̄` is the corpus's P or CP image of `V`, a grammar that produces `V³` but
  not `V̄³` builds parity violation into the electromagnetic production step. Nature puts parity
  violation only in the weak sector.
* **But the corpus has not ruled which map is P, C or CP.** Four involutions are in play and they
  are distinct:
  - bar, `q ↦ q⁻¹`, which sends `V ↦ V̄`;
  - `ι: σ ↦ −σ⁻¹`, which sends `V ↦ V̄`;
  - the group inverse, which sends `V ↦ V⁻¹ = σ₁σ₀⁻¹`, a different word;
  - charge conjugation C as the colour-flavour swap (`CFromColorFlavorSwap.lean`, proton ↦
    antiproton), which does not act on words at all.

  The corpus has retracted a conflation of two of these before (bean `qou-ales`, step 8). So
  "excluding `V̄` breaks CPT" is **true only if** bar or `ι` is ruled to be the parity/CP map. That
  is not established. AGENTS.md §7b reads the bar involution as the matter/antimatter pairing in
  the Type-B folding *conjecture*, and `TypeBFoldingChiralityObstruction.lean` proves that this
  folding reading conflicts with a global chirality grading. So that reading is itself contested.
* **CPT proper.** CPT maps β⁻ of the neutron to β⁺ of the antineutron. It does not require the
  *production* grammar to be mirror-closed. It requires that the CPT image of every admitted
  process be admitted. With `V̄` excluded, the CPT image of the nucleon word is admitted only if
  CPT does not send `V³` to `V̄³`. That is unsettled for the same reason as above.

### Downstream implications — measured

**The nucleon selection stops being unique.** On three strands, all eight three-vertex words in
`{V, V̄}` pass reading 3 (`computations/probes/gg_two_orientations`, bean `qou-a1hh`). Level 3 sees
two classes: the pure pair `VVV, V̄V̄V̄` with `χ_(2,1) = 1.99419`, and six mixed words with
`χ_(2,1) = 2.13303`. All eight have the minimal length 6. So `frobeniusSelected_ten_unique` (#8564)
stays true but answers a question about the old grammar. Under the widened grammar, cost
minimality gives an **8-way tie**, and `β_Bor = V³` is no longer singled out by the ruled
selection rule.

**Measured today: what that does to the scored `Q_β` row.** The scored row is `|ε_flavour(V³)|`,
ruled #8586. Probe `computations/probes/pair_word_brief/mirror_vertex_nucleon_probe.py`, exact in
`ℚ(q)`, values at the proton `q₀`, 70 dps. It reproduces the scored closed form for `V³` exactly
(an assertion) and gives:

| word(s) | `ε_flavour` exact | at proton `q₀` |
|---|---|---|
| `VVV`, `V̄V̄V̄` | `(q²−1)(q¹²−3q¹⁰+3q⁸−5q⁶+3q⁴−3q²+1)/(q⁴(q²+1)³)` | −0.0769805346013642 |
| the six mixed words | `−(q²−1)(q⁸−q⁶+3q⁴−q²+1)/(q²(q²+1)³)` | −0.0805501901000802 |

* The mirror pair gives the **same** `ε` as `V³` exactly. If (d) admits `V̄` and the tie is
  resolved to the pure class, **the scored row does not move**.
* If a mixed word were selected, `|ε|` would move by a factor of **1.04637**. That changes the
  scored `Q_β` by +4.64 % in magnitude, with `E₀` unchanged.
* This number must **not** be used to choose between the classes. That would be selection against
  the target.

**Four strands, for the β⁻ word** (#8696 §3.2, finite enumeration). With mirrors, `V₁³` ties with
7 other words at length 6, so cost minimality selects nothing.

**Five strands** (#8696 §3.2). With mirrors, four length-4 words beat `V₁³`: `V₀V̄₁`, `V₁V̄₂`,
`V̄₁V₀` and `V̄₂V₁`. Whether any of them is chiral was not reported. That is the next measurement
if (d) goes *in*.

**Mesons: no change.** No γγ meson selection exists on `main`. Searched: every
`QOU/Mass/GammaGamma*.lean` file, every `computations/qbeta/qbeta_gamma_gamma_*` and
`computations/probes/gg_*` file, and every `docs/audits/*gamma-gamma*` audit, for
"meson/pion/kaon". There are 0 hits. The meson word in `rem:meson-to-proton-via-borromean` is a
construction (`σ₀·L₊·σ₀⁻¹`), not a γγ selection. This is an absence on that surface. A meson
selection in a different vocabulary could still exist.

**Who reads the grammar.** On `main`, `GammaGammaWord` or a γγ selection is referenced by
**18 `.lean` files** and about **30 `computations/` scripts**:

* the `GammaGamma*` Lean files under `QOU/Mass`, `QOU/QBeta`, `QOU/OneDim` and `QOU/Archimedean`;
* `per_observable_100x_status.py` (the scored row);
* the `qbeta_gamma_gamma_*` probes and the `gg_*` probes;
* `ilp-covalent-bond`;
* the γγ-selection step 1–11 audits and `2026-11-21-magic-shells-gamma-gamma-model.md`.

Bean `qou-ales` is cited in 156 files. Under (d) *out* none of these changes. Under (d) *in*,
every result that enumerates `GammaGammaWord` and claims uniqueness has to be re-run with mirrors:

* #8564's nucleon base;
* the steps 3/4/8/11 selections, including the diproton reading;
* #8636 (n and p give the same element);
* the magic-shells model.

Results that are invariant under `V ↦ V⁻¹` at the character level are a partial exception. Bean
`qou-ales` records that reading-3 feasibility on `H₃` and `H₆` is invariant under that swap. That
swap is the group inverse, not `V̄`, so the exception does **not** carry over automatically.

### The options

**(d)-out — keep the grammar V-only and record a reason.**
* *What it means:* production vertices have one orientation; the mirror process is not a
  production event.
* *What it costs:* one ruling, and a sentence in `qou-ales` stating the reason. Nothing is re-run.
* *What it risks:* if bar or `ι` is later ruled to be the parity/CP map, the grammar is
  P-asymmetric in the electromagnetic sector, which is a physics mismatch that a referee will see.
  The nucleon and the scored row are unaffected.
* *What it commits to:* `β_Bor = V³` stays uniquely selected. The β⁻ word search stays as #8696
  ran it.

**(d)-in — admit `V̄ᵢ`.**
* *What it means:* the grammar is closed under the mirror (and under bar).
* *What it costs:*
  - one redefinition of `GammaGammaWord`, and a sweep of its Lean consumers, since
    `writhe_eq_zero` and `altChar_eq_one` still hold;
  - a re-run of about 10 selections;
  - a tie-break principle for the nucleon, because cost minimality alone gives 8.
* *What it risks:* the scored row is safe if the tie resolves to the pure pair. It moves by
  +4.64 % if a mixed word is chosen. Any tie-break chosen by its numbers is fitting.
* *What it commits to:* a **second ruling** (the tie-break), with the γγ rule no longer selecting
  the nucleon alone.

**(d)-in, modulo the mirror — admit `V̄`, but count `w` and its mirror image as one word.**
* *What it means:* the grammar is mirror-closed, and selection happens on mirror classes.
* *Measured:* the pure pair `{V³, V̄³}` is one class with identical `ε`. The six mixed words
  form **three** mirror classes (`VVV̄↔V̄V̄V`, `VV̄V↔V̄VV̄`, `VV̄V̄↔V̄VV`), so 4 classes tie
  at length 6. This option alone does not restore uniqueness either.

**Default (nothing ruled):** (d)-out in effect. The definition stands, nothing is re-run, and the
scored row is unchanged.

---

## (b) Must the pair-creation word be chiral (one-directional)?

### What is derived, and what would be new

* **Derived, at one crossing.**
  - The weak vertex is `−h·P_L` (merged).
  - The passage `σ₀σ₁σ₂` gives `(q²−1)·T⁺` with a zero reverse block (proved on **open** #8638).
  - The single crossing `σ₂ = R₀ + h·E⊗F` carries the W, and `E⊗F` is one-directional by
    construction (#8638 Part A).
* **Derived:** `[2]·P_L(σ₂) = q⁻¹·γ(0, q, 0)`, so the left projector is a photon element
  (`leftProjector_eq_photon`, #8696).
* **New choice:** requiring directionality of the **selected word**. No theorem says the β⁻ word
  must be one-directional. The corpus derives one-directional *vertices*. Promoting that to a word
  filter is a premise.
* **Proved negative for the current V-only candidates.** On four strands no γγ word of length
  ≤ 8 is chiral and passes CC and reading 3 (#8696; finite enumeration, scope (a)).

### What is aligned with physics, and the one distinction that matters most

**"Chiral" in #8696 is not V−A. Please keep the two apart when ruling.**

* **V−A** is about handedness. The charged current couples only left-handed fermions and
  right-handed antifermions. In the SM `ν̄_e` from β⁻ is right-handed. In the corpus, handedness
  is the left line and `P_L` (ruled and proved at one crossing), with `e_R` the matter⊗Higgs right
  line (#8694).
* **Directionality** is whether the operator has a `p⊗e⁻ → n⊗ν` block. In the SM the weak
  interaction Hamiltonian is Hermitian:
  `H_W ∝ (ūγ^μ(1−γ₅)d)(ēγ_μ(1−γ₅)ν) + h.c.` The "+ h.c." is the reverse process, i.e. electron
  capture or inverse β (`p e⁻ → n ν`), and it is physical. So:
  - If the pair word is read as **the β⁻ amplitude** (the J⁺ half of `H_W`), one-directionality
    is physics-aligned. A's non-zero reverse block then means A carries both halves and is not
    the β⁻ amplitude.
  - If the word is read as **the interaction operator** `H_W`, both blocks are expected, and a
    one-directional word is the wrong object. A's two blocks would then be a feature, provided
    they are adjoints of each other.

  That adjointness for A is **not measured**. It is the cheap check that would separate the
  readings.
* **The Fermi 4-fermion structure.** The Fermi vertex is one quark line times one lepton line at
  a point. In braid terms that is a single crossing between the active quark strand and the lepton
  strand, and `σ₂`'s `h·E⊗F` term is exactly `T⁺_quark ⊗ T⁻_lepton`. So candidate **C (`σ₂`) is
  the closest structural match to Fermi**. A touches two quark strands. B (the passage) touches
  all three. `V₂V₀V₁V₂` touches three quark strands, as measured below. In the SM the other two
  quarks are spectators at tree level.
* **Lepton number.**
  - On four strands, premise L puts ν in and e⁻ out on one strand. That is crossing symmetry, and
    lepton number is conserved along the strand.
  - On five strands the pair is a `U_q` singlet cup [L5]. A cup is one strand turning back in
    time, which is the Feynman–Stückelberg picture of a created pair (`L = +1 − 1 = 0`). Both
    settings book lepton number consistently. Five strands makes ν̄ a distinct outgoing line,
    closer to how the decay is observed.
* **Neutrino handedness.** No corpus object gives the ν̄ strand a helicity. `P_L` acts on a
  crossing, and `ν_R` exists in the corpus only as lepton⊗Φ (#8694). This was searched within the
  six-path grep of #8694 and not found. It is an absence on that surface.

### What `V₂V₀V₁V₂` commits to (measured today)

Same probe as above, combinatorial and exact.

* **It is a 4-letter braid, not an 8-letter one.** `V₀V₁ = σ₀σ₁⁻¹σ₁σ₂⁻¹` cancels internally, so
  `V₂V₀V₁V₂ = σ₂σ₃⁻¹σ₀σ₃⁻¹ = σ₀σ₂σ₃⁻²` as a braid. Its "length 8" is the γγ letter count. #8696's
  cost minimality ranks words by that count, which overstates the crossings of any γγ word with
  adjacent `VᵢVᵢ₊₁`. Whether cost should count grammar letters or reduced crossings is itself
  unruled. It affects every enumeration on four or more strands; on three strands it cannot
  arise.
* **Closure with `β_Bor` on strands 0–2** (either order) has three components:
  - `{0, 1}`: two nucleon strands **merged** by the `σ₀`. The nucleon's Borromean closure is
    broken.
  - `{2, 3}`: quark strand 2 and the lepton, `T(2,1)` (an unknot).
  - `{4}`: the ν̄ strand.

  Linking numbers: `lk({2,3}, {4}) = −1` and `lk({0,1}, {2,3}) = 0`. **So ν̄ closes as its own
  component but is Hopf-linked to the e⁻ component.** #8696 said "ν̄ closes alone", which is true
  of the components; the linking is new information here.
* **Strand roles.** Strands 0–2 are the nucleon, 3 is e⁻ (`d` colour under L), and 4 is ν̄. Two
  premises remain open: L (#8673) and the singlet cup [L5]. Uniqueness is checked only to length
  8, and without mirrors.
* **Knot reading (#8677).** The lepton is still an unknot here, not a trefoil. #8696 shows this
  holds for every candidate tested, so it is a property of the setting, not of this word.

### The options

**(b)-yes — require a zero reverse block.**
* *What it means:* the selected word is the β⁻ amplitude, the J⁺ half. The reverse process gets
  its own word.
* *What it costs:* one ruling, then one probe on `V₂V₀V₁V₂`:
  - its cross terms;
  - its `q → 1` order;
  - longer words, to test uniqueness;
  - with mirrors, if (d)-in.

  About an hour of compute; no Lean blocker.
* *What it risks:*
  - it rests on [L5] and L, both open;
  - the only survivor merges two nucleon strands, which conflicts with the SM spectator picture;
  - if (d) goes in, five-strand length-4 mirror words may also be chiral, and uniqueness is
    unknown.
* *What it commits to:*
  - A, B and C are all out (B by writhe and reading 3, C by nucleon-blindness in the one-term
    trace, A by direction);
  - ν̄ becomes a separate strand;
  - the reverse process (electron capture) needs its own word, presumably the reverse or adjoint.

**(b)-no — allow two-directional words.**
* *What it means:* the word is read as the interaction operator. A (`V₁³`) stays admissible.
* *What it costs:* nothing now. To be meaningful it needs the adjointness check on A's two blocks.
* *What it risks:*
  - A is not unique on five strands (`V₂³` ties);
  - with mirrors it ties 8-way;
  - A conflicts with the derived one-directional vertices (#8638).
* *What it commits to:* chirality is not a selection principle for words.

**Default:** nothing ruled. The pair stays the disjoint union `e⁻ ⊔ ν̄`, the factorisation no-gos
stand, and no scorecard reads any of this.

---

## (a) `V₁³` and (c) `σ₂`, briefly

**(a) `V₁³`.**
* *Derived:* it is a γγ word, the unique minimal word in G ∧ CC ∧ R3 on four strands (V-only).
  `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`, so it is literally two ruled photons.
* *Physics:* not directional; touches two quark strands; the lepton closes to an unknot.
* *Downstream:* nothing moves, because no energy has been computed on it. It is excluded by
  (b)-yes. It ties under (d)-in and on five strands.

**(c) `σ₂`.**
* *Derived:* it carries the W (`R₀ + h·E⊗F`) and is directional.
* *Physics:* closest to the Fermi point vertex (one quark line × one lepton line).
* *Proved defect:* in the one-term trace it is nucleon-blind, `C₁ = 0` for every nucleon element
  (`crossTerm_lastLetter_eq_zero`, from the Markov property). It is not γγ (writhe 1). In the
  labelled lepton-charge two-term comparison its cross term is non-zero (+1.45·10⁻⁴), but that
  form is not covariant. The covariant two-term form gives 0 for every candidate (proved, #8696).
* *Downstream:* it is the natural object for the Q_β energy routes still in flight:
  - route L (#8693, additive log-trace);
  - pairwise EM (#8704);
  - two-term covariance (#8707);
  - the Yukawa split (#8694).

  Each of those must say which word it uses. None is affected by (b) or (d) unless it selects its
  word through `GammaGammaWord`.

---

## Recommendation (my judgement, not a finding)

**Rule (d) first, and before ruling, ask for one small measurement: which involution the corpus
calls parity.** Whether excluding `V̄` is a physics defect depends entirely on that.

On the evidence I would take **(d)-out for now, with the reason stated as "production vertices
carry the left-line orientation"**, for three reasons:

* it is the only option that keeps the nucleon selection unique without a second ruling;
* the scored row is identical under the pure mirror pair anyway (measured), so nothing physical is
  lost by deferring;
* (d)-in creates a tie-break that is hard to make without fitting.

Revisit once a P/CP map is ruled.

On **(b)** I would not rule "chiral" until the adjointness of A's two blocks is checked (cheap).
The physics question is whether the word is the amplitude or the Hamiltonian, and #8696's
"chiral" answers the first while V−A is about something else.

## What is NOT established

* Which corpus involution is P, C or CP. Without that, "(d)-out breaks CPT" is neither shown nor
  refuted.
* Whether A's `n→p` and `p→n` blocks are adjoints of each other (not computed).
* Chirality and reading 3 of the five-strand length-4 mirror words (not computed).
* Whether cost should count grammar letters or reduced crossings.
* No energy and no `Q_β` is computed for any β⁻ candidate.

The `ε` values above are exact in `ℚ(q)`. They are evaluated at the proton `q₀` for display only
and selected nothing.
