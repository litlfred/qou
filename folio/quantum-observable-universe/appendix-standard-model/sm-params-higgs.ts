import { prose } from "../../schema/builders";

export default prose({
  label: "prose:sm-params-higgs",
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Bean qou-ewsb (Q-Gap-9): synced prose with QOU/StandardModel/ElectroweakSweedlerScaleAndRGThresholds.lean, remediated QOU/BraidKnot/HiggsCategoricalMassFormula.lean (replacing the 52-digit rational literal for catalanG with QOU.Archimedean.Catalan_constant = Cl_2(pi/2) + certified rational bracket), and wired the pre-registered 80-dps probe computations/probes/sm8w_ewsb_vew_mh_mz_rg/sm8w_ewsb_vew_mh_mz_rg_probe.py.",
    },
  ],
  title: "Higgs sector (2)",
  tags: ["appendix", "standard-model", "parameters", "higgs", "electroweak"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/sm8w_ewsb_vew_mh_mz_rg/sm8w_ewsb_vew_mh_mz_rg_probe.py",
    witness: [
      "computations/probes/sm8w_ewsb_vew_mh_mz_rg/sm8w_ewsb_vew_mh_mz_rg_probe.witness.json",
    ],
    status: "verified",
  },
});
