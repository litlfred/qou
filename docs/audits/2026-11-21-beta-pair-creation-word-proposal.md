# Which word creates the e⁻ν̄ pair in β⁻ decay — proposal for owner ruling

Bean `qou-99qc`. Owner (Carl), 2026-11-21: propose, for his ruling, the word that creates the
lepton pair. **Nothing here is ruled.** No candidate was chosen by its `Q_β` or by any residual;
CODATA is not read.

Pre-registration: `computations/probes/beta_pair_creation_word/PREREGISTRATION.md` (commit
`ee04d3c394`, before any number). Probe + witness: same directory (8/8 assertions, proton `q₀`,
70 dps, exact in `ℚ(q)`). Lean: `QOU/QBeta/PairCreationWordGammaGamma.lean` (sorry-free).

## The decision

The corpus writes the β⁻ lepton pair only as a **disjoint union** `e⁻ ⊔ ν̄` (`beta-decay-skein`,
`antineutrino-knot`, `two-photon-pair-production`, `breit-wheeler`), so any word that links the
pair to the nucleon is a choice (P2, #8680). This note lists the words that corpus principles admit
and says which principle, if any, singles one out. Choosing among them needs you, because the
principles disagree: the γγ rule and reading 3 pick one word, and the derived W exchange picks a
different one.

## Setting (stated, not derived)

* Four strands. Strands 0–2 are the nucleon, the γγ + reading-3 core `β_Bor = (σ₀σ₁⁻¹)³`, which is
  the same element for n and p (#8636). Strand 3 is one lepton strand.
* The process word is `W = X · β_Bor`: the nucleon braid acts first, then the candidate `X`.
* **Premise L** (#8673, which you left undecided): the lepton strand carries `ν = u`, `e⁻ = d`, and
  the outgoing ν̄ is the incoming ν by crossing. Every charged-current statement below uses it.
* Trace: Ocneanu–Markov, convention D. At `q₀` the Markov weights are `y_(4) = 0.3193`,
  `y_(3,1) = 0.1861` and `y_(2,2) = 0.0612`; every shape with three or more rows has weight 0. So
  reading 3 constrains exactly `χ_(4), χ_(3,1), χ_(2,2)`. Checked: `tr_D = Σ y_λ χ_λ` on all 24
  basis elements of `H₄`.
* **Reading 3 at every level reduces to `H₄`.** Every two-row shape of `H₅` restricts to two-row
  shapes of `H₄` (branching), so non-negative `H₄` characters stay non-negative higher up.

## 1. The principles as filters (exact; counts from the witness)

| principle | what it admits | forces one word? |
|---|---|---|
| **Q** charge / `T³` / `Y` conservation | every word (Hecke elements commute with `U_q`) | no, it constrains states, not words |
| **G** γγ grammar (`GammaGammaWord`, vertices `Vᵢ = σᵢσᵢ₊₁⁻¹`) | 30 words of length ≤ 8 on four strands | no |
| **CC** non-zero n⊗ν → p⊗e⁻ block `[L]` | 572 of 937 letter words of length ≤ 4 | with crossing-count minimality: **`σ₂` alone** (length 1), unique |
| **wrap** (lepton crosses ≥ 2 nucleon strands) | 368 of 937 | no |
| **R3** reading 3 on the whole word | 179 of 937 | no |
| G ∧ CC | 23 of 30 | minimal is `V₁` (length 2), unique, but it **fails R3** |
| **G ∧ CC ∧ R3** | 3 of 30: `V₁³`, `V₀V₁V₀V₁`, `V₁V₀V₁V₀` | with minimality: **`V₁³ = (σ₁σ₂⁻¹)³`**, unique |
| Ḡ (mirror vertices `V̄ᵢ = σᵢ⁻¹σᵢ₊₁` allowed) ∧ CC ∧ R3 | 8 of 84 words of length ≤ 6 | no, 8 words tie at length 6 |
| CC ∧ wrap ∧ cross term ≠ 0 ∧ R3, no γγ | 10 letter words of length ≤ 4 | no, 6 tie at length 3 (`σ₁²σ₂`, `σ₁σ₂σ₁`, `σ₂σ₁σ₂`, `σ₁⁻¹σ₂σ₁⁻¹`, `σ₁⁻²σ₂`, `σ₂⁻¹σ₁σ₂⁻¹`) |

Lean-proved exclusions, scope (b), invariant **writhe** (every γγ word has writhe 0,
`writhe_eq_zero`). None of the following can be a γγ word:
* the derived passage `σ₀σ₁σ₂` (writhe 3);
* the electron trefoil `σ₀³` (writhe 3);
* the weak knot `T(3,5)` (writhe 10);
* the single crossing `σ₂` (writhe 1).

So the γγ rule and the corpus's odd-writhe weak objects never meet in one word.

Two of the pre-registered priors failed:
* **PR3** ("CC implies wrap") is false. A single lepton crossing already carries the W
  (`σ₂ = R₀ + h·E⊗F`, #8638 Part A), so 265 CC words cross only one nucleon strand.
* **PR4** ("no unique word") is false within the ruled grammar G, and true once mirror vertices are
  allowed.

## 2. The surviving candidates

The cross term is `C(X) = tr_D(βX) − tr_D(β)·tr_D(X)`. The order of a quantity is the power of
`(q − 1)` it carries as `q → 1`.

| candidate | γγ? | CC block | wraps | `C(X)` | R3 at `q₀` |
|---|---|---|---|---|---|
| **(a) `V₁³ = (σ₁σ₂⁻¹)³`** | yes | ≠ 0, order 2, **both chiralities** | strands 1, 2 (net signed crossings 0, 0: Borromean) | `−(q²−1)⁶(q⁴+1)²(q⁴+q²+1)/(q⁸(q²+1)⁴)`, order 6 | ✓ `χ = (1, 2.984, 2.000)` |
| (b) passage `σ₀σ₁σ₂` (#8638) | no | `= (q²−1)·T⁺`, order 1, **chiral** | 0, 1, 2 | `q(q²−1)²(q⁴+1)(q⁴+q²+1)(q⁴−2q²−1)/(q²+1)⁵`, order 2 | ✗ `χ_(3,1) = −1.218` |
| (c) single crossing `σ₂` | no | ≠ 0, order 1, chiral | strand 2 only | **0** (connected sum, nucleon-blind) | ✓ |
| (d) `T(3,5)` on strands 1–3 | no | ≠ 0, order 1 | 1, 2 | order 3 | ✗ `χ_(2,2) = −1.133` |
| (e) left-handed vertex passages `ι₀ι₁ι₂`, `Ŵ₀Ŵ₁Ŵ₂` (`−h·P_L`) | elements, not words | ≠ 0 (orders 4, 1) | — | orders 5, 2 | ✗ (see the caveat below) |
| (f) mirror family, 8 words of length 6 | Ḡ only | ≠ 0 | 1, 2 | orders 4–6 | ✓ |

Caveat on (e): `ι = −h·P_L` carries an overall minus sign, so `ι₀ι₁ι₂` fails reading 3 on sign
alone. Reading 3 is not invariant under the scale of an element, so this failure says nothing about
the vertex. The same applies to any signed element.

Normal form of `V₁³ · β_Bor`: 17 basis elements `T_w`, listed exactly in the witness. Its
identity coefficient is `−(q⁴−q²+1)(q⁸−3q⁶+3q⁴−3q²+1)/q⁶`. The p⊗e⁻ column of its CC block on the
input `udd ⊗ u` is proved in Lean (`cc_column_udd`):

* `(q²−1)⁴(q⁴−q²+2)/q⁴`,
* `(q²−1)²(q³−q−1)(q³−q+1)(q⁶−2q⁴+3q²−1)/q⁹`,
* `(q²−1)²(q⁴−q²+1)(q⁶−2q⁴+3q²−1)/q⁸`.

It vanishes at `q = 1` and is non-zero at `q = 2`. An independent sympy run straight from the Lean
matrices reproduces the same three entries.

What `V₁³` is: the **Borromean core again**, on strands 1–3 (two nucleon strands and the lepton).
By the photon ruling, `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`, so `V₁³` is literally a product of two ruled
photons straddling the nucleon and the lepton. That is a γγ pair-production event in the corpus's
own grammar. Its closure is a pure braid, so **the lepton strand closes to an unknot**. Under your
#8677 ruling the unknot strand is the up-quark type and the electron is the trefoil, so in the knot
reading `V₁³` does not produce a trefoil electron. In the strand-colour reading (premise L) the
electron is the `d` colour on that strand, and there is no conflict.

## 3. Can any candidate be excluded? (parts 2–3, owner request 2026-11-21)

You asked: *"Keep these as options and explore the implications of each. Can we rule out some of
them?"* Pre-registered before any number (`PREREGISTRATION-exclusions.md` `f816f993c8`,
`PREREGISTRATION-part3.md` `3e36b55843`). Probe `beta_pair_exclusions_probe.py`, witness
`beta-pair-exclusions.witness.json` (12/12, exact in `ℚ(q)`, signs at the proton `q₀`, 70 dps).
Lean `QOU/QBeta/PairCreationExclusions.lean` (sorry-free, no `sorryAx`).

### 3.1 The two traces

* **One-term** `tr_D`: the Ocneanu trace, convention D, checked equal to the quantum trace
  `Tr(K^{⊗4}ρ)/[2]⁴` on 24 + 6 elements. Cross term `C₁(X) = tr_D(X·β) − tr_D(β)·tr_D(X)`.
* **Two-term**: the scored form `two_term_covariant_all_pairs_qtrace` is defined on three strands
  only. Its four-strand extension is a choice, stated in part 3: insertion `Σ_{i<j} QᵢQⱼ`, weight
  `K^{⊗4}`, subtract the insertion's average on each weight space, `F_c = tr_D + c·conn` with `c` not
  chosen (the QED scale is a selection, #8524). Cross term `F_c(Xβ) − F_c(β)F_c(X) = C₁ + c·C₂ + c²·C₂₂`.
  Two readings:
  - **T2cov** (the scored form, covariant): quark charges on all four strands.
  - **T2lep** (labelled comparison, **not covariant**): lepton charge `(0, −1)` on position 3 [L].
* **Proved, for every number of strands:** with quark charges on every strand, `Σ_{i<j} QᵢQⱼ` of a
  basis state depends only on its number of `d`s (`twoTerm_allPairs_formula`,
  `twoTerm_allPairs_scalar`). So the covariant insertion is a scalar on every weight space, and its
  connected trace is 0 for **every** element (`trace_scalar_insertion_connected`). The scored
  two-term form therefore gives `C₂ = C₂₂ = 0` for every candidate: it cannot rule anything in or out.
  This answers "is it non-zero once the lepton strand is wrapped": **no, not covariantly.**
* Under T2lep the insertion stops being a scalar (`lepton_allPairs_not_scalar`), and the connected
  term is already non-zero on `β` alone, before any wrapping:
  `conn(β) = −(q²−1)⁵(q⁴+q²+1)/(6q⁴(q²+1)³)`.
* The ring-coloured Borromean trace (PR #8706, branch
  `claude/borromean-ring-coloured-trace-np-2026-11-21`) is **open, not merged**, so it is not
  evaluated for A. Correction to part 3 §5, which said the branch was not on the remote: my
  `git ls-remote` pattern was wrong; the PR exists. One consequence can be read off without computing:
  in #8706's W-free strict colouring each closure component keeps its flavour, and A's process word is
  pure with zero signed crossings between the lepton and every quark strand (L `linkCountA`), so under
  that colouring A carries no `n → p` amplitude at all. Not computed; to be added if #8706 lands.

### 3.2 The table

Tiers: **L** proved-lean · **S** symbolic-exact (exact in `ℚ(q)`; a number only for a sign at `q₀`) ·
**Cn** conditional on a named premise · **E** empirical (a finite enumeration, or a sign at `q₀` only).

| | A `V₁³` | B passage `σ₀σ₁σ₂` | C `σ₂` | D mirror family (7 words of length 6, if `V̄` admitted) |
|---|---|---|---|---|
| chirality (reverse block `p⊗e⁻ → n⊗ν` zero?) | **not chiral** — both blocks ≠ 0 (S). Still not chiral with `P_L(σ₂)` on either side (S) | chiral, `(q²−1)·T⁺` (L, #8638) | chiral (S) | none chiral (S) |
| lepton closure component | pure braid: lepton closes alone, **unknot** (L `trackA`) | one 4-strand component with all three quark strands (L `trackB`); not identified | lepton + quark strand 2, `T(2,1)` = unknot (L `trackC`, `linkCountC`) | each: lepton alone, unknot (S) |
| nucleon sensitivity | yes, `C₁` order 6 (S) | yes, order 2 (S) | **none**: `C₁ = 0` for every `x ∈ H₃` and every `y = α + β·σ₂` (L `crossTerm_lastLetter_eq_zero`) | yes, orders 4–6 (S) |
| reading 3, whole word | pass at `q₀`: `χ = (1, 2.984, 2.000)` (E) | **fail at every `q > 0`, every non-zero scale, every conjugate**: `χ₍₄₎ = q³`, `χ₍₃,₁₎ = −(q⁶−q⁴+1)/q`, `χ₍₂,₂₎ = 0` (S), sign step (L `passage_readingThree_mixed`) | pass at `q₀` (E) | all pass at `q₀` (E) |
| γγ, word level (`GammaGammaWord`) | yes (L) | no, writhe 3 (L) | no, writhe 1 (L) | no by definition; writhe 0 and alternating character 1, so **no invariant separates them from `V`** (L) |
| γγ, element level ("products of photons") | vacuous: photons generate all of `⟨σ₀, σ₁⟩` (L `photon_adjoin_eq`) | same | same | `1 + c·V̄₀ = γ(hc, −hc, c)` (L) |
| one-term cross term `C₁` at `q₀` | `−(q²−1)⁶(q⁴+1)²(q⁴+q²+1)/(q⁸(q²+1)⁴)` = −6.49·10⁻⁵ (S) | −1.98·10⁻² (S) | 0 (L) | orders 4–6 (S) |
| two-term `C₂`, T2cov (scored) | 0 (L) | 0 (L) | 0 (L) | 0 (L) |
| two-term `C₂`, T2lep (labelled, non-covariant) | ≠ 0, order 5, −5.08·10⁻⁵ (S; pure word, so also the strand-tracked value) | ≠ 0, order 3 (S; position-labelled only) | **≠ 0**, order 4, +1.45·10⁻⁴ (S) | ≠ 0, order 5 (S) |
| five strands (separate ν̄ strand, pair = `U_q` singlet cup [L5]) | **not unique**: `V₁³` and `V₂³` tie at length 6 in G ∧ CC₅ ∧ R3 (E, all 120 G words of length ≤ 8) | — | — | with mirrors, four length-4 words beat `V₁³` (`V₀V̄₁, V₁V̄₂, V̄₁V₀, V̄₂V₁`) (E) |

Further element results (S, all at four strands):
* `A·passage` (`V₁³σ₀σ₁σ₂`) is **chiral**, but writhe 3 (not γγ, L `A_passage_not_gammaGamma`) and
  fails reading 3 (`χ₍₃,₁₎ = −1.321`). `passage·A` is not chiral: the order matters.
* `[2]·P_L(σ₂) = q⁻¹·γ(0, q, 0)` (L `leftProjector_eq_photon`): `A·P_L` is a scalar times three
  photons, admissible only at the vacuous element level.
* The one-sided weak vertex `σ₂ − h·P_L(σ₂)` is chiral and nucleon-blind (one-term), and fails
  reading 3 at `q₀` (`χ₍₂,₂₎ = −0.025`). `P_L(σ₂)` alone passes.
* **On four strands no γγ word of length ≤ 8 is chiral and passes CC and reading 3**: the three
  survivors `V₁³`, `V₀V₁V₀V₁`, `V₁V₀V₁V₀` are all non-chiral (S). **On five strands exactly one is:
  `V₂V₀V₁V₂`** (length 8; lepton component = lepton + quark strand 2, `T(2,1)`; ν̄ closes alone) (E).

### 3.3 What is excluded, and in which scope

* **B — excluded, scope (b), on two independent invariants:** writhe (not a γγ word, L) and reading 3
  on the whole word, which fails at every `q > 0` under every scale and conjugation (L sign step on S
  characters). It survives only if **both** rules are amended: reading 3 restricted to bound-state
  words (not transition words), and weak words exempted from γγ. Neither the bar image `P̄`, nor
  `P_L`-projected passages, nor products with A pass reading 3, so no cheaper amendment exists among
  the elements tested (scope (a) for that last clause: a finite list).
* **C — excluded as an energy-carrying word, scope (b) in the one-term trace only** (invariant: the
  Markov property; covers `σ₂`, `P_L(σ₂)` and the one-sided weak vertex). **Not** excluded in the
  T2lep comparison, where its `C₂` is non-zero. Also not γγ (writhe 1, L).
* **A — not excluded by any proved invariant in the strand-colour reading (premise L).**
  - In the **knot reading** (electron = trefoil, #8677) A is excluded, scope (b) **conditional** on
    that reading: its process word is pure, so the lepton closes alone to an unknot (L).
  - But in that reading **every** four-strand candidate fails the same way: a trefoil needs a
    component on two or more strands, and the lepton can only get one by merging with a quark
    strand. So the knot reading excludes the four-strand setting, not A specifically.
  - A is not chiral, and `P_L` on either side does not fix that. If you rule that the pair-creation
    word must be chiral, A is excluded, scope (b) conditional on that premise.
  - Its uniqueness fails on five strands (`V₂³` ties), scope (a): a finite enumeration under [L5].
* **D — cannot be settled by an invariant.** The mirror vertex is a photon element
  (`γ(hc, −hc, c)`), the bar involution maps `V ↦ V̄`, and writhe and the alternating character do
  not separate them. Only the definition of `GammaGammaWord` excludes `V̄`. That is a ruling, not a
  finding.

## 4. Decision for you

**What is decided:** which premise to fix next. Three premises do all the work: (1) must the
pair-creation word be chiral? (2) is the γγ grammar bar-closed (D)? (3) does reading 3 apply to
transition words or only to bound states? Each needs you, because no corpus invariant fixes it
(§3.3).

### Option 1 — rule A (`V₁³`), non-chiral, four strands
* **What it means:** the pair is a second Borromean core on two quark strands and the lepton.
  Both `n→p` and `p→n` blocks are non-zero.
* **What it costs:** a ruling in `qou-99qc`; a `Q_β` functional on it is one more probe.
* **What it risks:** it contradicts the derived left-handed vertex (#8638,
  `prop:weak-vertex-left-projector`); it is not unique once ν̄ gets its own strand (`V₂³` ties);
  the lepton is an unknot, against #8677's trefoil electron.
* **What it commits to:** chirality is not required of the pair-creation word; premise L
  (strand-colour) over the knot reading.

### Option 2 — require chirality, then look at five strands
* **What it means:** the pair-creation word must have a zero reverse block. On four strands no γγ
  word passing CC and reading 3 is chiral (length ≤ 8). On five strands the only one found is
  `V₂V₀V₁V₂`.
* **What it costs:** one ruling, then one probe to characterise `V₂V₀V₁V₂` (cross terms, `q → 1`
  orders, longer words to test uniqueness). About an hour of compute; no Lean blocker.
* **What it risks:** the five-strand setting rests on the singlet-cup pair state [L5], a stated
  choice; `V₂V₀V₁V₂`'s uniqueness is only checked to length 8.
* **What it commits to:** excludes A, B (γγ) and C (nucleon-blind) together; makes ν̄ a separate
  strand.

### Option 3 — rule B with an amendment
* **What it means:** the derived chiral passage `σ₀σ₁σ₂`, with reading 3 restricted to bound-state
  words and weak words exempt from γγ.
* **What it costs:** two amendments to `qou-ales`.
* **What it risks:** a per-sector dispatch (weak words selected by a different rule), which
  AGENTS.md lists as a fitting pattern.
* **What it commits to:** the weak sector sits outside both selection rules.

### Option 4 — rule D first (is the grammar bar-closed?)
* **What it means:** decide whether `V̄ᵢ = σᵢ⁻¹σᵢ₊₁` are γγ vertices.
* **What it costs:** one ruling. If yes, `#8636`'s nucleon selection must be re-run with mirrors.
* **What it risks:** with mirrors, four-strand A ties with 7 words and five-strand words of length 4
  become cheapest, so cost-minimality stops selecting anything.
* **What it commits to:** the meaning of `GammaGammaWord` for every later selection.

### Default (nothing ruled)
Nothing changes: the pair stays the disjoint union `e⁻ ⊔ ν̄`, the factorisation no-gos stand, and
the probes and Lean stay as records. No scorecard reads any of this.

### Recommendation (my judgement, not a finding)
**Option 2's question first.** Chirality is the one premise that separates A from everything else,
and the corpus already derives a left-handed vertex (#8638), so I would require it. That leaves one
five-strand candidate to characterise before any ruling on a word.

## 5. What is NOT established

* Minimality is over the stated families: every G word up to length 8, every letter word up to
  length 4, and block products of two. The minimality of `V₁³` within G is complete, because every
  shorter G word was enumerated. Five or more strands (a separate ν̄ strand, vertex `V₂`) were
  **not** enumerated.
* Reading 3 is evaluated at `q₀` in mpmath at 70 dps, not proved in Lean.
* No energy functional and no `Q_β` is computed for any candidate.

* Parts 2–3: the four-strand extension of the two-term form is a stated choice (§3.1). The
  T2lep reading is not covariant. The five-strand pair state (singlet cup, `e⁻ = ν̄ = d`) is the
  stated choice [L5]. Five-strand enumerations stop at length 8 (G) and 6 (with mirrors).
* The topological step "a one-strand closure and `T(2,±1)` are unknots" is standard and not
  formalised; the Lean proves the strand permutations and signed crossing counts.