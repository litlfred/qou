import { remark } from "../../schema/builders";

/**
 * Companion remark to thm:toric-diophantine-stoichiometry: Smith/Hermite normal
 * forms, the strict inclusion C(A_CHO) < UGB(I_{A_CHO}) < G(A_CHO) (20 < 32 < 33),
 * Sturmfels-Thomas zero-T Gröbner reduction on P_b cap Z^7, and finite-T Birch
 * detailed-balance mass-action equilibria on Spec C[N A_chem].
 */
export default remark({
  label: "rem:toric-chemical-groebner-geometry",
  title:
    "Gröbner test sets, Sturmfels–Thomas enthalpy normal forms, and Birch mass-action toric equilibria",
  interprets: "thm:toric-diophantine-stoichiometry",
  lean: {
    ref: "qou:QOU.MathlibInfra.ConfinementLayerTower.toric_hom_vanishes_on_binomial_of_kernel",
    validation: "not_checked",
  },
  uses: [
    "def:h2-molecular-braid",
    "def:co-molecular-braid",
    "def:co2-molecular-braid",
    "def:ch4-molecular-braid",
    "def:h2o-molecular-braid",
    "def:iterated-confinement-layer",
    "thm:toric-diophantine-stoichiometry",
  ],
  cites: [
    "deloera-hemmecke-koeppe2013",
    "hemmecke-koeppe-weismantel2014",
    "sturmfels-thomas1997",
    "birch1963",
    "horn-jackson1972",
    "feinberg1972",
    "gatermann-huber2002",
    "craciun-dickenstein-shiu-sturmfels2009",
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
    "stoichiometry",
    "groebner-basis",
    "graver-basis",
    "toric-geometry",
    "mass-action",
    "birch-theorem",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "Exact SNF/HNF, Pottier Graver basis (`|G| = 33` unoriented), Universal Gröbner Basis " +
        "(`|UGB| = 32`), elementary circuits (`|C| = 20`), zero-`T` Sturmfels–Thomas normal-form " +
        "reduction on `b = (2, 8, 4)`, and 80-dps finite-`T` Birch mass-action equilibrium (`8.5e-80` " +
        "residual) are certified in `confinement-layer-tower-chem.witness.json` (bean qou-5lct).",
    },
  ],
});
