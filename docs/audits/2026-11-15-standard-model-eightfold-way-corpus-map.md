# Standard Model and eightfold way — corpus map

Bean `qou-qs5m` (epic `qou-qs0e`). Date 2026-11-15. PR #7823.

**Purpose.** A classified map of every corpus connection to the Standard Model gauge group,
hypercharge, weak isospin, generations, anomaly cancellation, flavour SU(3), SU(6), quantum
Schur–Weyl duality, CKM, confinement and colour antisymmetry. The other quark-state beans build on
it.

**Classes** (exactly one per row):
- **proved** — a sorry-free Lean proof of the claim;
- **conditional** — Lean conditional on a named class, with no instance;
- **conjecture** — a `conj:` block or an open bean;
- **prose** — narrative only;
- **fitted** — something selected against data.

"Proved (arith)" marks a sorry-free theorem whose content is arithmetic or definitional rather than
representation theory.

**Existing hubs — cite these, do not rebuild them.**
- `docs/sm-eightfold-derivation-cheat-sheet.md` (918 lines, refreshed 2026-09-03);
- `docs/audits/2026-08-08-sm-eightfold-epistemic-accounting.md`;
- `docs/coordination/sm-26-parameter-chip-away.md`.

This map is the delta measured today, plus the drift that has appeared since 2026-09-03.

**Method.**
- **Six-path grep**, run by a delegated `corpus-grepper` agent, over: `docs/audits`, `folio/`
  (excluding `.lake`), `computations/`, `docs/coordination`, `library/INDEX.md` plus `sections/` plus
  `ocr/`, and `beans/defs`. The exact patterns are in §13.
- **Path 0 (`corpus_search`) was NOT run**: the paper-assistant MCP server failed to connect. Every
  absence claim below therefore rests on the greps alone, without a graph check.
- **"Proved" is a grep result, not a compile.** It means sorry-free by a word-bounded grep with no
  `: True` field. These files were **not compiled** for this map; the exception is
  `ColourChannelSpinStatistics.lean`, verified in this PR.
- **Spot-checks** (each verified by reading the file):
  - the `g_A` lines in `AxialCoupling.lean:20,215-217` and `hadron-half-life-verification.md:22`;
  - the stale "not formalised" in the cheat sheet at `:546`;
  - the GMO sentence at `eightfold-open-problems.md:319-321`.

## 1. SM gauge group SU(3)×SU(2)×U(1)

| item | location | claim | class | note |
|---|---|---|---|---|
| `conj:sm-gauge-truncation` | `appendix-standard-model/sm-gauge-truncation.lean:44` | the SM group embeds in the archimedean truncation | conjecture | **inhabited too cheaply**: `StandardModelTruncation G` holds for `G := SU(3)×SU(2)×U(1)` itself |
| `conj:gauge-hecke-realization` | `gauge-hecke-realization.lean:52` | End X ↪ H_n(q) | conjecture | no instance |
| `def:gauge-action-groupoid` | `gauge-action-groupoid.lean:48` | gauge equivalence is an equivalence relation | proved | definitional |
| quaternionic electroweak | `QOU/QuaternionicElectroweak.lean:50-97` | SU(2)_L and SU(2)_R commute; U(1)_Y sits in the i-plane | proved | textbook facts; derives no gauge group |
| sin²θ_W | `sm-params-gauge-couplings.md:28-32` | one value at ~60 % miss; another at 0.127 % | conjecture / **fitted** | the 0.127 % is the best of 74 enumerated candidates and its witness calls it inconclusive; it sits on a three-row block, which convention D kills |

## 2. Hypercharge Q = T₃ + Y/2

| item | location | claim | class | note |
|---|---|---|---|---|
| `conj:sm-hypercharge-invariant` | `sm-hypercharge-invariant.lean:71` | gauge-invariant I₃ and Y exist with GMN, and Y is not a writhe function | conjecture | a proved corollary forces an equal-writhe pair |
| writhe as Y | `eightfold-way/flavor-charge-assignments.md` | p and n share Y but differ in writhe | proved negative | the writhe → Y map is falsified |
| GMN on six quarks | `ParticleInteractions/WeakIsospinT3Grading.lean:234-313` | GMN closes | proved, **narrow** | `hyperchargeLeft` is the constant 1/3 put in by hand, so the six cases collapse to two arithmetic rows |
| `CanonicalWeakIsospinFromBowtie` | same file `:369` | GMN closes with a derived Y | conditional | no instance; this is the open step |
| strand-twist battery | `StandardModel/TwistBatteryVacuity.lean:86` | the battery reduces to T = 3Q | proved negative | zero selectivity |
| battery reduction | `StandardModel/HyperchargeBatteryReduction.lean:92-187` | Y_R fixed by Q; Y_L = B−L | proved | standard SM identities, self-declared as such |
| μ̄₁₂₃, the second invariant | `StandardModel/SecondCrossingInvariant.lean:99,183` | μ̄ separates the two U(1)s | proved separation + conditional | normalisation open |
| SU(5) level | `su5-hypercharge-n3-gate.md` | Wenzl level r = 5 would fix z | prose | says explicitly it does not derive SU(5) |

## 3. Weak isospin, left-handed doublets, chirality

| item | location | claim | class | note |
|---|---|---|---|---|
| T₃ = sign(κ)/2 | `WeakIsospinT3Grading.lean` (26 theorems) | the T₃ grading is orthogonal to generation | proved (on a finite toy `Quark` type) | one of the cheat sheet's three corpus-wide derived items |
| I₃ on the nucleon doublet | `flavor-charge-assignments.md`, `coulomb-charge.lean:47` | Q = w/2 | derived | a two-point sign-and-ratio match |
| chirality files | `StandardModel/Chirality*.lean`, `TypeBFoldingChiralityObstruction`, `Gen1QuarkRays` | constructions and obstructions on eight labels | proved (finite) | the chirality flip matches only projectively |
| SU(2) acts on L only | — | — | **absent** | stated nowhere in Lean or prose |
| N = 2 Schur–Weyl | `SchurWeyl/JimboActionKernel.lean`, `JimboKernelGeneric.lean` | ker(Jimbo) = trace radical; H/rad ≅ TL; Jimbo trace = convention D | proved | the level-2 factor exists; nothing ties it to L-chirality |

## 4. Generations

| item | location | claim | class | note |
|---|---|---|---|---|
| leptons T(2,3), T(2,5), T(2,7) | `observations/symmetry-preserving-leptons.md:2-29` | "genus saturation at T(2,9) excludes a fourth" | prose | conflicts with the next two rows |
| continuant divisibility | `Archimedean/lepton_continuant_generation_exclusion.lean:166` | b₃ ∣ b₉, which removes 9 | proved (arith) | three is reached by removing one element of a four-set |
| genus bound | `TorusKnotGenusFourUnique.lean` | genus ≤ 4 gives {3, 5, 7, 9} | proved | gives **four** |
| `generation_completeness` | `brings-surface/generation-completeness.lean` | — | proved but **vacuous** | see `2026-08-30-generation-completeness-is-vacuous.md` |
| four countings | `2026-10-10-generation-count-two-independent-countings.md` | 4 / 3 / 2 / 3 | conjecture, owner decision | beans `qou-x4qm`, `qou-xtcl` (todo) |

## 5. Anomaly cancellation — **absent**

There is no gauge-anomaly cancellation anywhere on the six paths. The hits are homonyms or labels:
- "anomaly-free B−L" is a bare label at `HyperchargeBatteryReduction.lean:123`;
- "anomaly freedom" means vanishing Chern classes in `qou-axioms-physical-reading.md:11` and
  `vertex-algebra-relations.md:265`.

Three library documents hit; they are citation candidates only.

"Anomaly cancellation forces N_c = 3" appears only in beans `qou-qs4c` and `qou-qs5m`. As
`2026-11-15-quark-factor-relations-and-colour-channel.md` §3 notes, the anomaly fixes the
**charges given N_c**, not N_c from nothing.

## 6. Flavour SU(3): octet, decuplet, Gell-Mann–Okubo

| item | location | claim | class | note |
|---|---|---|---|---|
| A₂ from three strands | `WeylInvarianceQDeformation.cartanMatrix_A2` | the Cartan matrix of A₂ | proved | true by construction |
| q-weight lattice | `WeylInvarianceQDeformation.lean:147` | the Cartan entries stay fixed | proved | no L2 leverage |
| 3 ⊗ 3̄ = 8 ⊕ 1 | `meson-octet-decomposition.lean:34,42` | N² = (N²−1) + 1 | proved (arith) | conditional on N = 3 |
| decuplet/octet/singlet row cap | `Eightfold/RowCapObstruction.lean:101-178` | C(N,3) = 0 ⟺ N < 3 | proved (arith) | the representation theory is only in `def` names |
| octet weight degeneracy | `OctetWeightDegeneracy.lean:138` | m_Λ = m_Σ⁰ under weight-only mass | proved negative, scope (b) | |
| GMO, first order | `GellMannOkuboIdentity.lean:128` | an identity | proved negative | GMO withdrawn as a target |
| GMO, second order | `GellMannOkuboSecondOrder.lean:120` | two equations, three unknowns | proved | under-determined — **contradicts** `eightfold-open-problems.md:319-321` (see §12) |
| decuplet spacing, Coleman–Glashow | `DecupletEqualSpacing.lean:167`, `ColemanGlashowIdentity.lean:119` | identities of the ansatz | proved negative | |
| nonet mixing | `NonetMixingUnconstrained.lean:115` | the mixing angle is unconstrained | proved | gated on N = 3 |
| flavour vs colour | `FlavourColourDiscriminator.lean:96` | no object-level gate separates them | proved (definitional) | `rw` on two hand-entered records |
| N = 3 routes | cheat sheet §4-A plus five Lean files | seven routes excluded | proved negatives, scope (b) | survivor: owner decision `qou-j3w6` (todo) |
| level-3 channel | `2026-10-10-level3-su3-channel-test.md` | near-match 2.69e-4 | scope-(a) negative | ~1100× worse than level 2; y_(1³) = q⁶/(Φ₃Φ₆)³ = 1/27 at q = 1 |
| level-3 colour-factor ratio | `computations/probes/level_three_colour_channel_probe.py` | the signs are right; \|L_a/L_s\| = 1 vs QCD's 2 | measured miss | the factor of 2 comes from \|det T\| = 1 |

## 7. SU(6) spin–flavour (56, μ_p/μ_n = −3/2)

**No corpus derivation existed before this PR.**
- μ_p/μ_n appears only as a target in `the_twist_is_absent_where_it_is_needed_probe.py:32,128`, as a
  scope-(a) negative.
- This PR adds `ColourChannelSpinStatistics.signMult_anti`: δ(spin, flavour) given colour (1³). That
  is the 56 = (10, 3/2) ⊕ (8, ½) structure. It is **conditional** on four S₃ factors, Fermi
  statistics and the Δ⁺⁺. μ_p/μ_n = −3/2 then needs μ_q ∝ Q_q as an extra imported input.

**`g_A` is FITTED, and published as RESOLVED.**
- `Archimedean/AxialCoupling.lean:20,83` defines g_A = (5/3)·|tr_std|/|tr_sym|.
- The 5/3 is the imported naive-quark-model (SU(6)) value.
- The colour average is one of three options listed at `:215-217` beside their PDG deviations: h₀₁
  alone −23 %, h₀₂ alone +46 %, the symmetric average +0.1 %. The +0.1 % one is the one used.
- That is selection against the target. Yet `observations/hadron-half-life-verification.md:22`
  reads "**RESOLVED. g_A(q) ≈ 1.277**".
- The cheat sheet's "no fitted content found" does not cover this file.

**Wigner SU(4) is cheaply inhabited.** `WignerSU4FromSpinIsospin.lean:100` carries three fields
typed `: True`, plus `occupancy_from_binding: c = B_AME/E_gate`, which inverts data. Conditional, no
instance.

## 8. Schur–Weyl and quantum Schur–Weyl

| item | location | claim | class | note |
|---|---|---|---|---|
| `prop:schur-weyl-eightfold` | `eightfold-way/schur-weyl-eightfold.md` | Jimbo duality, cited | prose + row-cap consequence | **stale**: the cheat sheet `:546` says "duality itself not formalised" |
| Jimbo kernel at N = 2 | `SchurWeyl/JimboActionKernel.lean:535,604,784`, `JimboKernelGeneric.lean` | the trace is Markov with z = q³/(q²+1); ker = trace radical; H/rad ≅ TL; image dimension is Catalan | proved | **N = 2 = TL = convention D is unconditional**; commutant surjectivity not claimed |
| three-row vanishing | `OcneanuWeight.lean:142`, `WenzlWeightLevelR.lean:131` | y_(1³) = 0 at z_D; w_μ = 0 ⟺ ℓ(μ) > r | proved | general level r |
| N ≥ 3 Jimbo action | — | — | **absent** | coordinator gap G1 |
| Wenzl's theorem | `QBeta/WenzlWeightVanishing.lean` | class `IsOcneanuWeightSystem` | conditional | axiomatised |

## 9. CKM

`sm-params-ckm.md` lists all four parameters as **open and unposed**: there is no flavour basis.
Class: prose. There is no Lean beyond two disclaimers. Beans `qou-pj82` (CKM) and `qou-y0mq`
(PMNS) are open.

## 10. Confinement — homonym

In this corpus "confinement" mostly names the **confinement SDP/LP**, i.e. operator selection under
Frobenius positivity.

QCD confinement appears only as an analogy:
- `mass-theory/confinement-categorical.md`, whose Lean is conditional on
  `SemisimpleFrobeniusHeckeLike`;
- there is no colour-singlet confinement theorem.

## 11. Colour antisymmetry

| item | location | claim | class | note |
|---|---|---|---|---|
| μ̄₁₂₃ in the sign rep | `2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md:86-89` | A established; B (colour channel = (1³)) not | prose / cited | |
| Brunnian isotype | `StandardModel/BrunnianIsotypeExclusion.lean` | Λ³ is the only non-empty channel | proved | |
| colour channel forced | `SchurWeyl/ColourChannelSpinStatistics.lean` (**this PR**) | colour (1³), given four S₃ factors + Fermi + Δ⁺⁺ | **conditional** (premises are physical, not Lean) | lean-direct exit 0; standard axioms only |
| colour on the regular H₃ | `StandardModel/ColourHeckeRegularHost.lean` | a Hecke-compatible colour action cannot live on the regular carrier | proved negative | |
| `ColourStabilizerAction` | `StandardModel/ColourStabilizerAction.lean:42` | an injective su(3) → End V | conjecture | **inhabited too cheaply**: holds whenever dim V ≥ 3, which the file acknowledges |

## 12. Gaps and inconsistencies, ranked

1. **`g_A` is published as RESOLVED while fitted** (§7). Recommended fix: re-scope
   `hadron-half-life-verification.md:22` to "selected from three colour averages", which is
   exemption 2 (the corpus's own Lean lists the selection). **Not applied in this PR** — it is a
   content change and is left to the owner.
2. **The generation count is unresolved**: 4 / 3 / 2 / 3, with prose claiming 2 + 1 (§4). Owner
   beans `qou-x4qm`, `qou-xtcl`.
3. **The quantum Schur–Weyl status is stale** in the cheat sheet `:546` and in
   `schur-weyl-eightfold.md`. The N = 2 half is proved (§8). This is a corpus-derived doc-currency
   fix.
4. **Several conjecture carriers are inhabited too cheaply**: `StandardModelTruncation`,
   `ColourStabilizerAction`, `WignerSU4FromSpinIsospin`. And arithmetic theorems are cited as
   representation theory: `RowCapObstruction`, `meson_octet_at_three`, `FlavourColourDiscriminator`.
5. **Three things are absent or stale**:
   - anomaly cancellation (§5) and SU(6) (§7, now partly supplied by this PR);
   - "SU(2) acts on L only" (§3);
   - the GMO "genuine prediction" sentence at `eightfold-open-problems.md:319-321`, which contradicts
     `GellMannOkuboSecondOrder.lean:120` (second order under-determined).

### Decision for the owner: which drift fixes to make

**The decision.** Items 1 and 3 change reader-facing content. Under §🟥 ASK THE OWNER they need a
yes unless they fall under the exemptions.

**Option 1: fix only item 3** (the Schur–Weyl currency).
- *Means:* edit two sentences to cite `JimboActionKernel`.
- *Costs:* two files.
- *Risks:* low.
- *Commits to:* nothing.
- *Exemption:* it is corpus-derived (exemption 2), so it may proceed without asking. It is
  nevertheless held for this decision because it touches content in a math PR.

**Option 2: fix items 1 and 3.**
- *Means:* additionally re-scope "RESOLVED" for g_A to "selected among three colour averages
  (+0.1 %)".
- *Costs:* one more content block, and its `.qa.json`.
- *Risks:* the observation list loses a "resolved" entry.
- *Commits to:* treating g_A as fitted under the anti-fit directive.

**Option 3: no change.** The map records the drift and nothing else moves.

**Recommendation (judgement).** Option 2. A fitted value marked "RESOLVED" is precisely what the
NO-FITTING directive forbids, and the evidence is in the file's own docstring.

**Default.** Option 3: no change, and the drift stays documented here.

## 13. Commands

```sh
grep -rliE '<pat>' docs/audits folio --exclude-dir=.lake computations docs/coordination beans/defs
grep -ciE '<pat>' library/INDEX.md ; grep -rliE '<pat>' library/*/sections library/*/ocr
# patterns: anomaly cancel|anomaly-free|gauge anomal ; SU\(6\)|spin-flavou?r ; mu_p ?/ ?mu_n|μ_p/μ_n ;
#   three generations|generation count ; CKM|Cabibbo ; hypercharge ; weak isospin|left-handed doublet ;
#   Gell-?Mann.?Okubo ; Schur.?Weyl ; colou?r antisymm|colou?r singlet ; confinement ; SU\(3\)_c
grep -rlIE --include=*.lean 'Hypercharge|Anomal|Generation|CKM|SU\(6\)|GellMann|Okubo|SchurWeyl|Confin|Colour|Color|Decuplet|Octet' folio/quantum-observable-universe/lean/QOU
grep -cE '(^|[^-[:alnum:]`])sorry([^-[:alnum:]`]|$)' <file> ; grep -cE ':\s*True\b' <file>
```
