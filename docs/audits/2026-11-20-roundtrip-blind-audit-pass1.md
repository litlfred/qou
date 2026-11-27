# Blind round-trip audit, pass 1 (epic qou-ncxf: RT-1 qou-zqno, RT-2 qou-wnm3, RT-3 qou-da6d)

Date 2026-11-20. Workstream W11 (coordinator epic `qou-c20n`, thread PR #8526). Branch `claude/roundtrip-blind-audit-2026-11-20`, PR #8528. Corpus `main` at `917b69399`.

## 1. Summary

Ten provable blocks were sampled deterministically and run through three blind round trips. **Two of the ten pass cleanly**: B10 is trivially correct but weakly formalised, and B07 reproduces a finding already on record. **Eight carry a semantic mismatch between the `.md` statement, its narrative proof, and its Lean.** The mismatches fall into three classes, which recur across blocks:

| class | blocks | what it means |
|---|---|---|
| **A. Lean conclusion supplied by an assumption** (a class field, a hypothesis, or instance data) | B02, B04, B06, B08 | The Lean typechecks, but proves nothing beyond what it assumes. |
| **B. Lean strictly weaker than the `.md` claim** | B01, B03, B05, B06, B09, B10 | The Lean is genuine and correct, but formalises only a tail, a special case, or a numerical check of the stated claim. |
| **C. Narrative proof does not prove its statement** | B01, B02, B03, B04, B08, B09 (and B07, already known) | The narrative is weaker than the statement, internally inconsistent, or restates the claim. |

**The sharpest case is B08 `thm:topological-mass`.** It is kind `theorem`. Its Lean is a self-assuming projection of `MassDecompositionCategoricalContext`. Its own proof block proves only `≤` and says equality "is open" (`topological-mass-proof.md` lines 30–46). Three artifacts, three different claims.

**No corpus-derived fix was applied.** None of the discrepancies is a case where the corpus already decides the answer and the code merely disagrees with it. Each needs a re-derivation, a rescoping, or a kind change, and all three are owner decisions under the 2026-09-07 ask-first rule. Each finding became a bean (§5). One owner question is asked on #8526.

## 2. Method

### 2.1 The tool the epic names does not exist

The epic body names `folio/pipeline/roundtrip-blind-packets.ts`. **It is absent on `main` `917b69399`**, and no branch or PR carries it. This pass therefore uses a new read-only script, `scripts/roundtrip-blind-sample.py` (in this PR).

### 2.2 Population and sampling rule

**Population: 435 blocks.** These are the provable blocks (`theorem` / `proposition` / `lemma` / `corollary`) in `folio/quantum-observable-universe/` that satisfy all of:

1. they have a `qou:` `lean.ref`;
2. their statement `.md` exists;
3. some `prf:*` block lists them in `uses[]` and has a non-empty `.md`.

The epic's figures of 741 provable blocks and 437 proof blocks count blocks that lack a proof block or a Lean ref.

**Sampling rule:** sort the population by `sha256(label)` and take the first eligible entries. A block is skipped if its declaration cannot be located, its proof contains `sorry`, or its statement concludes `: True`. This took the first 15 by hash: **10 sampled** and 5 skipped. Four of the 5 skips are real findings (§4); the fifth was a parser miss.

### 2.3 Blind packets

For each sampled block:

- Lean comments and docstrings are stripped.
- The target declaration is renamed `thm`, so its name cannot reveal the claim.
- Non-proof declarations from the same file are supplied as context, capped at 6000 characters.
- Blocks carry the IDs B01–B10, never their labels.

### 2.4 Legs

Each blind leg was a sub-agent instructed to make exactly one tool call: reading its own packet file and nothing else.

| RT | leg A | leg B | adjudication |
|---|---|---|---|
| RT-1 | stripped Lean statement → English | leg A's English (flags removed) → Lean statement | W11 (this session), comparing original Lean, round-tripped Lean, and `.md` statement |
| RT-2 | `.md` statement + narrative proof → Lean skeleton + mechanism | Lean statement + proof → English narrative + "where the content lives" | W11 |
| RT-3 | narrative proof only → inferred statement | statement only → proof obligations | W11 |

### 2.5 Limitations (stated so the result is not over-read)

1. **Blindness is enforced by instruction, not by sandbox.** Each agent reported exactly one tool use, which is consistent with the instruction, but the agents could have read other files.
2. **The adjudicator was not blind and was not a separate agent.** The epic specifies an adjudicator agent per RT. W11 adjudicated directly, and checked each recorded claim against the files. The specific checks: the B02 scope note at `unstable-atom-decay-channel-proof.md:1`, the B01 `h/2 = 1/2` claim at `c5-…-proof.md:42`, the B08 open-equality text, the B05 and B09 arithmetic, and b² = 7/8 at q = 1+√2.
3. **Narrative proofs can contain spoilers.** RT-3 leg A flagged spoilers in B01, B06 and B07 (the proof quotes its statement or names its Lean theorem). The B01, B06 and B07 RT-3 verdicts are therefore partly non-blind.
4. **No Lean was built.** The question here is semantic equivalence, not compilation. The sampler excludes `sorry`-bearing proofs, but does not verify that the files compile.
5. **n = 10 of 435.** This pass measures whether the method is useful and what the defect classes are. It is not a corpus rate. Eight of ten mismatched is a sample of ten; do not quote it as 80 % of the corpus.

### 2.6 Calibration

Both checks below confirm the method finds real defects rather than inventing them:

- **B07 `prop:sl2-prolongation-recurrence`.** The blind legs independently reproduced bean `qou-vkm6` (`completed`, 2026-08-29): the Lean proves only the Cayley–Hamilton implication, and the statement's own scope section says the recurrence fails from n = 5.
- **B04 `lem:mobius-energy-frobenius-kernel`.** Its projection shape matches the earlier `qou-kkja`.

## 3. Per-block verdicts

Paths are relative to `folio/quantum-observable-universe/`. Each block has a statement `.md`, a proof `-proof.md` beside it, and the Lean file listed.

| # | block | Lean | RT-1 (Lean ↔ Lean ↔ `.md` stmt) | RT-2 (narrative ↔ Lean proof) | RT-3 (stmt ↔ narrative) | bean |
|---|---|---|---|---|---|---|
| B01 | `prop:c5-involution-leibniz-decomposition` (`stochastic-mechanics/`) | `stochastic-mechanics/c5-involution-leibniz-decomposition.lean` | Round trip faithful. ℝ-specialised without need (§7c). Weaker than `.md`: c5 is a *definition*, and its identity with ladder rung 5 is not derived. | Same mechanism (rational-function algebra). | Narrative errors: `h/2 = 1/2` (line 42; at the silver ratio h = 2); "TWO averaged crossings" (line 35) though the second factor is σ₁⁻¹; c_k table asserted. | `qou-xxa9` |
| B02 | `prop:unstable-atom-decay-channel` (`knots-particles-confinement/`) | sibling `.lean` | **Class A.** Uniqueness is hypothesis `hsel`; the second conjunct is the IVT for an arbitrary `E`; no existence claim. | Divergent: the `.md` claims existence + uniqueness of λ*. | Narrative self-contradictory: `x = 0` is feasible (its own scope note); "LP relaxation = convex hull of integer solutions" (line 6) is false in general; generic uniqueness is called open. | `qou-ni0g` |
| B03 | `lem:su2-emergence-dagger-unitarity` (`quantum-observable-universes/`) | `lean/QOU/su2_emergence_dagger_unitarity.lean` | Faithful and genuine (2×2 inner-product-preserving ⇒ unitary). **Class B**: only the linear-algebra tail of the G ⊆ U(2) claim. | Narrative's categorical step absent from Lean. | Narrative missing: Hermitian/sesquilinear structure, positive-definiteness, `S(f)` on morphisms, dim τ(V) = 2. | `qou-1iit` |
| B04 | `lem:mobius-energy-frobenius-kernel` (`climax-volume-mass/`) | `lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean` | **Class A**: composes two class fields; the only instance in the file is degenerate. | Lean has no content of its own. | The narrative restates the limit; derives no 1/r² from a distance-independent Killing form. | `qou-n3xv` (and `qou-15oa` was completed on this) |
| B05 | `prop:golden-quartet-galois` (`predicted-spectra/`) | sibling `.lean` | Faithful. **Class B**: roots + φψ = 1 only. | Galois orbits, ι exchange, regular action and disc = 400 absent from Lean. | Narrative omits irreducibility and the τ∘ι = ι∘τ check. Its conclusions are true. | `qou-k9tf` |
| B06 | `prop:alpha-em-shift-multiplicative-chain` (`predicted-spectra/`) | sibling `.lean` | **Class A/B**: `chainIndices = bareIndices` from instance data; α_EM absent. RT-1 leg B: unprovable from the English without the class↔α_shift link. | Narrative is a substitution of two upstream propositions. | `.md` "=" vs the reported 0.213 gap to CODATA: "=" is true only of the model quantity. | `qou-tdhw` |
| B07 | `prop:sl2-prolongation-recurrence` (`mass-theory/`) | sibling `.lean` | Faithful generic implication. | Lean proves the implication only. | Statement vs its own scope section (`.md:30`, "fails from n = 5"). | already `qou-vkm6` (no new bean) |
| B08 | `thm:topological-mass` (`mass-endomorphism/`) | `lean/QOU/Torsion/mass_decomposition_categorical.lean` | **Class A**: self-assuming projection. | Lean has no content of its own. | Proof gives only `≤`; equality open; norms vs squared norms; Φ_q used as a norm. | `qou-27ys` + ask |
| B09 | `prop:crossed-module-euler-characteristic` (`mass-theory/`) | `lean/QOU/BraidKnot/CrossedModuleEulerCharacteristic.lean` | Faithful finite check (`decide`). **Class B**: −12 = dim V·χ(Σ₄) is numerical only. | Same. | Φ₀ direction reversed in statement; intermediate matrix asserted; Bring-bridge table unproved. | `qou-zxuy` |
| B10 | `lem:staircase-corner-hook` (`mass-theory/`) | `lean/QOU/StaircaseCornerHook.lean` | Faithful but **Class B**: pure ℕ arithmetic, no partition. | Same. | Proves the claim under ρ_k = (k,…,1), which the `.md` does not state. | `qou-pwo1` |

## 4. Side finding from the sampler: lean.refs that do not name a proof

Of the 15 lowest-hash candidates, 4 have a `lean.ref` that does not name a proof of the block (bean `qou-5d0x`):

| block | the ref names |
|---|---|
| `prop:centered-hecke-variance-positive` | a **module** (the proof is `centeredVariance_pos`) |
| `thm:jones-markov-trace` | a **structure** |
| `prop:curvature-rank-gb-stratification` | a Prop proof declared as **`def`**. It is also a class-field projection: the `def-disguised` shape of AGENTS.md §1a. |
| `prop:box-braid-irreducibility` | the **`Prop` definition**, not its proof |

A fifth skip (`prop:quantum-observable-universe-exists`) was a parser miss on the dotted theorem name `QuantumObservableUniverse.exists_instance`. It is not a corpus defect.

## 5. Beans

All new beans are children of `qou-ncxf`:

| bean | finding | priority |
|---|---|---|
| `qou-27ys` | B08 | high |
| `qou-ni0g` | B02 | high |
| `qou-1iit` | B03 | |
| `qou-n3xv` | B04 | |
| `qou-tdhw` | B06 | |
| `qou-zxuy` | B09 | |
| `qou-xxa9` | B01 | |
| `qou-5d0x` | ref audit (§4) | |
| `qou-k9tf` | B05 | low |
| `qou-pwo1` | B10 | low |

**None of these, and none of the RT beans, may be closed while the claims they track stay open.** The epic and RT-1/2/3 stay `in-progress`: this is one pass of ten out of 435.

## 6. Scope overlaps (said on #8526)

| bean | block | owning workstream |
|---|---|---|
| `qou-27ys` | B08 | W1 (mass chapter Lean) |
| `qou-tdhw` | B06 | W3 (α_EM / photon) |
| `qou-n3xv`, `qou-ni0g`, `qou-5d0x` | B04, B02, `curvature-rank` | W8 (de-vacuify) / W10 (class-field debt) |

W11 edited no Lean and no content block.

## 7. Next passes (recommendation, judgement not finding)

1. **Run the sampler over all 435 refs for the §4 class.** It is mechanical, needs no agents, and gives a real rate for the ref defect.
2. **Pass 2: the next 20 by hash.** Use a separate adjudicator agent, so the adjudication is also blind to W11's priors.
3. **Make the sampler handle dotted declaration names.**
