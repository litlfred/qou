import { remark } from "../../schema/builders";

export default remark({
  label: "rem:spacetime-length-distance-layers",
  title:
    "Three stratified layers of aether grain, metric moduli, and empirical unit bridges",
  interprets: "prop:reeb-coefficient-is-hbar-q",
  lean: {
    ref: "qou:QOU.InformationTheory.UnifiedClockScaleLayers.hbarQ_mul_planckTick",
    validation: "not_checked",
  },
  uses: [
    "prop:reeb-coefficient-is-hbar-q",
    "rem:planck-length-share-vs-total",
    "rem:connes-distance-not-reeb-step-count",
    "rem:discrete-planck-step",
    "def:gravitational-constant",
    "prop:gram-degeneracy-blocks-connes",
  ],
  cites: [
    "kantorovich1942",
    "rubinstein1957",
    "connes1989",
    "rieffel1999",
    "rieffel2004",
    "dandrea-martinetti2010",
  ],
  tags: [
    "planck-length",
    "hbar-q",
    "reeb-flow",
    "connes-distance",
    "base-ring-wall",
    "calibration-discipline",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "Consolidates the seven scale, clock, distance, and volume notions across QOU into three " +
        "stratified layers paired with an explicit §7c base-ring classification (Options 1 + 4). " +
        "Layer I generic-field identities (`hbarQ_mul_planckTick`, `jackson_uv_geom_sum`, " +
        "`jackson_uv_sum_lt_planckTick`, `atomic_clock_scales_with_planckTick`) are proved in " +
        "`QOU.InformationTheory.UnifiedClockScaleLayers`, linking `PlanckStepAtomicity` and " +
        "`SubstrateClockUniqueness` (`QOU.AlgebraicSubstrate.PlanckStepAtomicity`). Layer IIa " +
        "Rieffel–Kantorovich Lip-seminorm faithfulness and finite shortest-path duality are proved in " +
        "`QOU.InformationTheory.FiniteRieffelQuantumMetric` (bean qou-5uj7); Layer IIb's exclusion of " +
        "`r ∝ Vol^{1/3}` is proved in `QOU.MassTheory.RadialVolRhoMirrorTest`. Retires the colliding " +
        "glyphs `\\ell_P^{\\mathrm{step}}` and `\\ell_q` in favour of `\\hbar_q = 1 - q^{-1}` (bean qou-adwi).",
    },
  ],
});
