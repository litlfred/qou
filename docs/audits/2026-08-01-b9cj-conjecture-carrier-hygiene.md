# §3b Conjecture-Class Lean Carrier Hygiene — bean epic `b9cj` (2026-08-01)

**Scope.** The 23 open §3b conjecture-class Lean carriers tracked under
bean epic [`b9cj`](https://github.com/hmans/beans). Per AGENTS.md §3b /
§1a / §3b-tax these are **honest conjecture placeholders**: the class
axiomatises the conjecture; an absent (or `sorry`) instance is the
open state, *not* missing proof. This pass is **hygiene, not proving**:

- We do **not** fabricate an instance to "close" any carrier (that is
  an audit-dodge / anti-laundering violation).
- Famous-open encodings (RH, BSD, Collatz, Diophantine-birthday, P≠NP)
  are **aspirational** — verified honestly-marked, never proved.
- The only genuine work is **§3b-tax content-bearing hygiene**: a
  conjecture *class* must **assert** something. A carrier that is an
  empty marker, a `: True` field, or a `residual : ℝ` / `residual = 0`
  placeholder with an uninterpreted scalar asserts nothing meaningful —
  any trivial instance would discharge it. Those are strengthened so the
  fields carry the conjecture's actual claim *in the shape of the claim*
  (the ReebEpsilon / ConditionalClasses Round-11 pattern).

**Anti-fabrication (STRICT):** no instances were created for any carrier;
no `: True`, `native_decide`, or tautology was introduced. Strengthened
carriers stay **instance-less** (matching the de-abstracted exemplars
`QCollatz`, `BringTrilogDepth3Witness`, `jet_filtered_knot_factor`).

## Findings summary

| Verdict | Count | Meaning |
|---|---|---|
| **genuine** | 14 | already content-bearing — fields carry a parameter-quantified claim in the shape of the conjecture; verified, no change |
| **fixed** | 3 | strengthened a degenerate placeholder to content-bearing (2), or removed a fabricated laundering instance (1) |
| **needs-owner** | 6 | degenerate `residual = 0` placeholder whose faithful content requires the owner to state the real claim, or which touches the Habiro-dilog / polylog frontier owned by other agents (deferred, not modified) |

The machine audit (`lean-vacuity-axiom-audit.ts`, 4 conjecture-discipline
criteria) flagged **none** of the 23 as `proof-no-empty-prop-carrier` /
`proof-claims-unencoded` / `true-class-field` — each already carries a
Prop field that is not literally `: True`. The degenerate `residual = 0`
pattern passes the machine checks (it *has* a Prop field) but fails the
deeper §3b-tax "shape of the claim" standard; that is the human judgement
this pass supplies.

## Per-carrier table

| Carrier | File:line | Verdict | Reason |
|---|---|---|---|
| BorelZagierQouVolumes | `Archimedean/BorelZagierQouVolumes.lean:44` | genuine | `qLinearIndependent` field = Q-linear independence of the 3 volumes (shape of claim) |
| BringTrilogDepth3Witness | `BraidKnot/BringTrilogDepth3Witness.lean:55` | genuine | fully de-abstracted (Clausen components + K=5 distribution relation + non-degeneracies); instance-less; derived sorry-free lemmas |
| ClassicalRiemannHypothesis | `BraidKnot/ClassicalRiemannHypothesis.lean:36` | genuine | `rh` field over Mathlib `riemannZeta` (faithful RH statement); already matured from a `residual` placeholder |
| He4DemandClosure | `Interactions/NuclearOperatorRegimes.lean:139` | genuine | `all_nonneg : ∀ c ∈ coeffs, 0 ≤ c` + legitimate derived instances; not a sorry carrier |
| QCollatz | `AppendixSurreals/QCollatz.lean:65` | genuine | exemplary: full Skein-Collatz map content + `reaches_cycle` conjecture field; instance-less; extensive derived sorry-free cycle-exclusion lemmas |
| QouPNeqNp | `Information/QouPNeqNp.lean:78` | genuine | `faithful : residual ≠ 0 → PNeqNPInQOU` over opaque target; non-degenerate; sorry confined to the open implication (history: fixed a prior backwards `residual=0` fabrication) |
| SingleVolumeIrrationality | `Archimedean/SingleVolumeIrrationality.lean:27` | genuine | 3 volume fields + `Irrational` fields (shape of claim) |
| TorusKnotMass | `BraidKnot/TorusKnotMass.lean:56` | genuine | mass-factor fields + `factors_distinct` + `WZ_mass_ratio_in_unit` + derived lemmas |
| TwoFiltrationBridge | `BraidKnot/TwoFiltrationBridge.lean:50` | genuine | `bridge` depth-lift dichotomy over real Mathlib `YoungDiagram` + concrete `gbDepth` |
| jet_filtered_knot_factor | `BraidKnot/jet_filtered_knot_factor.lean:52` | genuine | `factor_is_jones` field over real `QPlancherel` weights; instance-less; sorry-free positivity lemma |
| q_gl_classical_limit | `QGeometricLanglands/q_gl_classical_limit.lean:29` | genuine | `hecke_limit` (real q=1 eigenvalue collapse) + `recovers_classical` |
| q_gl_fiber_functor | `QGeometricLanglands/q_gl_fiber_functor.lean:25` | genuine | `uniqueness` rigidity field |
| q_gl_kummer_filtration | `QGeometricLanglands/q_gl_kummer_filtration.lean:27` | genuine | `level1_all` + `lifts_iff_divides` (n ∣ χ(A)) fields |
| q_oper_hecke | `QGeometricLanglands/q_oper_hecke.lean:27` | genuine | `oper_irreducible` field |
| **ConfinementNfStructureForcing** | `BraidKnot/ConfinementNfStructureForcing.lean:27` | **fixed** | was `residual = 0`; strengthened to the .md's two-part claim — NF-support localisation (`λ⋆ ∈ A`, `|A| < n!`) + duality-bounded shift (`shift_NF = α_shift + Δ`, `\|Δ\| ≤ gap`) + 2 derived sorry-free lemmas; instance-less |
| **QBirchSwinnertonDyer** | `AppendixSurreals/QBirchSwinnertonDyer.lean:27` | **fixed** | was `residual = 0`; strengthened to Weak q-BSD (`ord_{s=1} L = r_q`) + rank-0 Full-BSD collapse; derived sorry-free `ord_zero_iff_rank_zero`; instance-less (aspirational famous-open — honestly stated, NOT proved) |
| **jet_convergence_classical_limit** | `BraidKnot/jet_convergence_classical_limit.lean:44` | **fixed** | class was already content-bearing (`converges : Filter.Tendsto …`) but carried a **fabricated trivial instance** `⟨fun _ => 0, 0, tendsto_const_nhds⟩` — an audit-dodge; removed it (instance-less, matching sibling `jet_filtered_knot_factor`) |
| BringFigureEightDepth2Witness | `BraidKnot/BringFigureEightDepth2Witness.lean:27` | needs-owner | degenerate `residual = 0`; content IS available (.md: `Vol(4_1) = std(2 Im Li_2^q(e^{iπ/3})) = 2 Cl_2(π/3)`), but the claim is dilog (`Li_2^q`) — **deferred to avoid the Habiro-dilog frontier owned by other agents** |
| archimedean_agreement | `BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean:27` | needs-owner | degenerate `residual = 0`; lives under `HabiroResidueSumEquivalence/` — **Habiro frontier, deferred (owned by other agents)** |
| QouInfraDischargesGoncharovZeta5 | `AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean:27` | needs-owner | degenerate `residual = 0`; meta-claim ("QOU infra discharges Goncharov's depth-3 conjecture at ζ_5") in the polylog/depth-3 frontier — deferred; faithful encoding needs Goncharov's conjecture stated first |
| SpectralNormalForm | `AppendixSurreals/SpectralNormalForm.lean:27` | needs-owner | degenerate `residual = 0`; claim = "eigenvalues of every spectral operator are rational in ε (∈ valuation ring 𝒪)" — no faithful encoding without valuation-ring machinery; owner to state |
| LocalInfinitesimalField | `AppendixSurreals/LocalInfinitesimalField.lean:27` | needs-owner | degenerate `residual = 0`; claim = "ε is a sheaf of infinitesimals across a scheme X" — sheaf-theoretic, not faithfully encodable without inventing structure |
| DiophantineBirthday | `AppendixSurreals/DiophantineBirthday.lean:27` | needs-owner | degenerate `residual = 0`; the docstring quotes the **proved** Liouville/Roth bounds, but the actual conjecture (algebraic-vs-transcendental *birthday-trajectory* separation) is not stated as a formula — owner to state the real claim; do not encode Liouville-as-conjecture |

## Discipline notes

- The 6 needs-owner carriers were **left untouched** (`.lean` unchanged):
  strengthening any of them would require either inventing the
  conjecture's real claim (SpectralNormalForm, LocalInfinitesimalField,
  DiophantineBirthday) or editing files in the Habiro-dilog / polylog
  frontier that two other agents own (BringFigureEightDepth2Witness,
  archimedean_agreement, QouInfraDischargesGoncharovZeta5). Honest
  "needs the owner" beats a guessed encoding.
- All three fixed carriers keep the honest open state: content-bearing
  class, **no instance**. Each carries at least one derived sorry-free
  consequence proving the class content is non-vacuous.
- Durable record: this doc + the review ledger
  `docs/audits/lean-vacuity-review-ledger.json`.
