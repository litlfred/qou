import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:su2-emergence",
  // Was `qou:QOU.RankOneGaugeData` — no declaration of that name exists
  // anywhere in the Lean tree, and the canonical resolver returns unresolved.
  // Before folio-assistant PR #121 it fell back to the import-only library
  // root `QOU.lean`, where every checker audited a list of import lines and
  // passed vacuously, which is why the dangling ref survived.
  // `QOU.SU2Emergence` (`lean/QOU/QuantumObservableUniverse/VolumeForm.lean`)
  // carries this theorem's own `\label{thm:su2-emergence}`, which is the
  // evidence — the ref's own name was not.
  //
  // Repointing makes the declaration auditable; it does not make it strong.
  // See the authorNote below and `qou-n1dj`.
  // REPOINTED 2026-08-26 (bean `qou-v1h5`). Was `qou:QOU.SU2Emergence`, the
  // contentless `structure` the authorNote below dissects. It now points at a
  // theorem that DERIVES both conclusions: the rank from the volume constraint
  // (`exteriorSquareDim_eq_one_iff`, itself sorry-free) and the subgroup from
  // the two element-wise constraints. Sorry-free, `#print axioms` clean
  // (propext / Classical.choice / Quot.sound only), verified `lean`-direct
  // against its real import cone.
  lean: { ref: "qou:QOU.su2_emergence_rank_forced", validation: "not_checked" },
  title: "Emergence of the gauge group",
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean pointers moved out of the prose (voice drain, epic `qou-d4kh`). [`SU2EmergenceRankForced.lean`](../lean/QOU/QuantumObservableUniverse/SU2EmergenceRankForced.lean) carries the statement above as `QOU.su2_emergence_rank_forced`, together with the rank-free subgroup half `QOU.mem_specialUnitary_of_unitary_of_det_one` and the non-vacuity check `QOU.su2_emergence_rank_hypothesis_is_load_bearing`. The rank is sourced from `QOU.BraidsAndKnots.exteriorSquareDim_eq_one_iff`; the subgroup half composes `QOU.su2_emergence_combined`.",
    },
    { kind: "note", date: "2026-10-11", body: "Relocated from the block prose by the paper-voice commentary audit: stating the two conclusions as one conjunction is deliberate — an earlier formulation derived \"which subgroup\" and reported it as though it had also derived \"which rank\". `QOU.su2_emergence_rank_forced` is sorry-free." },
    {
      kind: "note",
      date: "2026-08-16",
      body:
        "**What the Lean declaration does and does not say (bean `qou-n1dj`).** " +
        "`QOU.SU2Emergence` has three fields: an abstract `gaugeGroupType`, an " +
        "action `ext_sq_action` on `Λ²V`, and `det_one : ∀ g, ext_sq_action g = " +
        "𝟙 exteriorSquare`. It states that a group acts trivially on the " +
        "exterior square. It does not mention SU(2), and it does not mention " +
        "the rank of the fundamental object — `exteriorSquare` is an " +
        "unconstrained parameter. The two supporting lemmas " +
        "(`SU2EmergenceVolumeDeterminant`, `SU2EmergenceDaggerUnitarity`) are " +
        "single-field classes restating their own conclusions, with docstrings " +
        "recording that the witness is pending a categorical-determinant " +
        "formalisation in Mathlib. " +
        "This matters downstream because the mass channel's trace-convention " +
        "argument cites this theorem for `dim V = 2`. The prose proof takes " +
        "that rank as an input to both sub-lemmas (each concludes `G ⊆ " +
        "SL(2, ℂ)` / `G ⊆ U(2)` with the 2 already present), and the Lean " +
        "carries no rank content, so the citation does not supply it. " +
        "`QOU.BraidsAndKnots.VolumeConstraintForcesFibreTwo` re-sources that " +
        "hypothesis from the categorical volume constraint of " +
        "`def:quantum-observable-universe` instead.",
    },
    {
      kind: "status",
      date: "2026-08-26",
      body:
        "**Repaired (bean `qou-v1h5`).** The note above stands as the record " +
        "of what was wrong; this records what was done about it. The block " +
        "now states a theorem with its hypotheses explicit, and `lean.ref` " +
        "points at `QOU.su2_emergence_rank_forced` " +
        "(`SU2EmergenceRankForced.lean`), which derives BOTH conclusions " +
        "rather than assuming either: `N = 2` from the volume constraint via " +
        "`exteriorSquareDim_eq_one_iff`, and `G ⊆ SU(N)` from unitarity plus " +
        "`det = 1`. The second half is stated at general `n` " +
        "(`mem_specialUnitary_of_unitary_of_det_one`) precisely to make " +
        "visible that it carries no rank content — which is the conflation " +
        "the prose proof made. Non-vacuity is " +
        "`su2_emergence_rank_hypothesis_is_load_bearing`: at `N = 3` the " +
        "volume hypothesis fails while the subgroup half still applies, so " +
        "the rank conjunct is doing work. All sorry-free and axiom-clean. " +
        "**Still assumed, and now said in the statement rather than left " +
        "implicit:** that `Aut^⊗(τ)` IS such a matrix set. This narrows the " +
        "gap from 'rank and subgroup both assumed' to 'the realisation is " +
        "assumed'; it does not close it.",
    },
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**The display sibling carried a third vacuous statement, now a " +
        "theorem.** `su2-emergence.lean` held `axiom su2_emergence` for " +
        "`∃ sd : SpinDecomposition …, sd.fundamentalObj = " +
        "data.qou.fundamentalObj`. That is vacuously true: " +
        "`SpinDecomposition` has three free fields and two equations " +
        "satisfiable by taking `simpleObj` constant, so the whole statement " +
        "closes by `rfl`. Unlike a false axiom nothing unsound followed " +
        "from it -- and unlike a false axiom it could stand indefinitely, " +
        "cited as Tannaka-Krein reconstruction, since looking for a " +
        "counterexample finds none. The old docstring described the " +
        "consequence as *simple objects indexed by half-integer spin " +
        "labels with dim = 2j + 1*; `SpinDecomposition` carries no " +
        "simplicity condition, no injectivity of `simpleObj` and no " +
        "dimension field, so none of that was in the statement. The block " +
        "itself already points at `QOU.su2_emergence_rank_forced` and is " +
        "unaffected.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
  uses: ["def:quantum-observable-universe"],
  proofs: ["prf:su2-emergence"],
  examples: ["ex:su2-emergence"],
  tags: ["emergence", "gauge-group", "su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/su2-emergence-0.svg", blockIndex: 0, hash: "ff77986f66d2" },
    { mime: "image/svg+xml", url: "rendered/su2-emergence-1.svg", blockIndex: 1, hash: "e6bb15a051f3" },
  ],

});
