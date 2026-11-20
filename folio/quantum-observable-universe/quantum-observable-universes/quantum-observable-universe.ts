import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-observable-universe",
  title: "Quantum Observable Universe",
  tags: ["quantum", "observable", "category-theory"],
  lean: { ref: "qou:QOU.QuantumObservableUniverse",
    validation: "not_checked",
  },
  // def:rigid-monoidal-category + def:snake-identity added 2026-08-14:
  // rigidity moved down from def:quantum-universe (which is now braided
  // only) and is condition 1 here, so this block now depends directly on
  // the rigid structure and on the snake identities it cites.
  uses: [
    "def:quantum-universe",
    "def:rigid-monoidal-category",
    "def:snake-identity",
    "unital-groebner-bases:def:admissible-system",
  ],
  examples: ["ex:qou-su2", "ex:c-quantum-observable-universe", "ex:c-quantum-universe", "rem:yekutieli-stokes"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-observable-universe-0.svg", blockIndex: 0, hash: "6d717475f32e" },
    { mime: "image/svg+xml", url: "rendered/quantum-observable-universe-1.svg", blockIndex: 1, hash: "198957633587" },
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the two table rows are `exteriorSquareDim_ne_zero_iff` and `exteriorSquareDim_eq_one_iff`.",
    },
    { kind: "note", date: "2026-10-11", body: "Relocated from the block prose by the paper-voice commentary audit: earlier statements of this definition wrote ε as a non-degenerate epimorphism; the two dimension rows are proved in `lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean`." },
    {
      kind: "refined-framing",
      date: "2026-08-22",
      body:
        "Condition 5 now reads as an isomorphism rather than a bare " +
        "'non-degenerate epimorphism'. This is bean qou-n1dj item 2, an " +
        "editorial choice Lean could not settle: the two readings are not " +
        "equivalent, and only the iso forces the fibre dimension N = 2 that " +
        "the D-forcing chain consumes (epi gives only N >= 2, which admits " +
        "the colour fibre N = 3). It is the reading under which condition 5 " +
        "does its stated job, because det(g) is the action on the TOP " +
        "exterior power and Lambda^2 is top exactly when N = 2. Both rows of " +
        "the table are proved in VolumeConstraintForcesFibreTwo.lean.",
    },
    {
      kind: "status",
      date: "2026-08-22",
      body:
        "The formalised condition 5 was vacuous and is no longer (bean " +
        "qou-n1dj item 3). It was two free fields, `exteriorSquare : C` and " +
        "`volumeForm : exteriorSquare -> 1`, with nothing tying " +
        "`exteriorSquare` to Lambda^2(fundamentalObj); since QuantumUniverse " +
        "supplies Preadditive C, `volumeForm := 0` inhabited it for ANY " +
        "exteriorSquare. Now: `exteriorSquareProj : V (x) V -> exteriorSquare` " +
        "with `exteriorSquare_epi`, plus `volumeIso : exteriorSquare = 1`. " +
        "`iso_unit_hom_ne_zero` proves a zero volume form forces End(1_C) " +
        "trivial, hence (via unitEndEquiv) the base ring trivial. " +
        "Deliberately NO braiding-eigenvalue condition on the projection: on " +
        "the q-exterior square the braiding acts by -q^{-1}, not -1, so " +
        "demanding antisymmetry would silently impose q = 1.",
    },
    {
      kind: "caveat",
      date: "2026-08-22",
      body:
        "What this does NOT do. It does not bridge the categorical statement " +
        "to the numeric one: getting from `volumeIso` to " +
        "`exteriorSquareDim N = 1` needs the fibre functor to be monoidal and " +
        "to send exteriorSquare to Lambda^2(tau V), and neither is available " +
        "in QuantumUniverse today, so markovWeights_eq_jones_of_volume_" +
        "constraint still takes `hvol` as a hypothesis on a natural number. " +
        "It also raises the bar for ever exhibiting a QOU, and this tree has " +
        "no instance of QuantumObservableUniverse anywhere — see " +
        "WitnessObstruction.lean, which rules out module categories. " +
        "Downstream, RankOneGaugeData's `volume_nondeg` becomes derivable, " +
        "so that structure now adds nothing to QuantumObservableUniverse.",
    },
  ],
});
