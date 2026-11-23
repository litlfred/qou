import { remark } from "../../schema/builders";

/**
 * The 5-layer iterated confinement tower (L_0..L_4), 80-dps adiabatic gap
 * ratios eta_k = ||V_{k+1}|| / Delta_k, neutron-star outer-crust flip, and
 * comparison with continuum EFT and polygraphic coherence.
 */
export default remark({
  label: "rem:five-layer-confinement-tower-rg",
  title:
    "The five-layer iterated confinement tower as zero-counterterm algebraic renormalization",
  interprets: "thm:adiabatic-confinement-gap-stability",
  lean: {
    ref: "qou:QOU.MathlibInfra.ConfinementLayerTower.neutron_star_electron_capture_threshold",
    validation: "not_checked",
  },
  uses: [
    "def:iterated-confinement-layer",
    "thm:adiabatic-confinement-gap-stability",
    "rem:shell-filling-electronegativity-ilp",
  ],
  cites: [
    "wilson1971",
    "weinberg1990",
    "aubert-emc1983",
    "vidal2007",
    "squier1987",
    "lafont2003",
    "guiraud-malbos2012",
    "guiraud-malbos2018",
  ],
  computation: {
    engine: "python",
    script:
      "computations/probes/confinement_layer_tower_chem/confinement_layer_tower_chem_probe.py",
    witness: [
      "computations/probes/confinement_layer_tower_chem/confinement-layer-tower-chem.witness.json",
    ],
    status: "experimental",
  },
  tags: [
    "confinement-tower",
    "renormalization-group",
    "adiabatic-ratio",
    "EMC-effect",
    "neutron-star",
    "polygraphs",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "Evaluated at 80 decimal digits in `confinement_layer_tower_chem_probe.py` " +
        "(`confinement-layer-tower-chem.witness.json`, `q0Anchor = \"proton\"`); " +
        "`neutron_star_electron_capture_threshold` is proved in `QOU.MathlibInfra.ConfinementLayerTower`.",
    },
  ],
});
