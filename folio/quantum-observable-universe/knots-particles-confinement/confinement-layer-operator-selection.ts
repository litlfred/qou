import { remark } from "../../schema/builders";

export default remark({
  label: "rem:confinement-layer-operator-selection",
  renamedFrom: ["def:universal-ilp-algorithm"],
  title:
    "Confinement-layer reduced-cost selection and involution-twisted $\\ast$-positivity",
  interprets: "def:derived-atom",
  uses: [
    "def:derived-atom",
    "prop:confinement-universality",
  ],
  cites: [
    "farkas1902",
    "kantorovich1939",
    "dantzig-wolfe1960",
  ],
  lean: {
    ref: "qou:ToricConicOpt.ConfinementLayerTower.ConfinementLayer",
    validation: "not_checked",
  },
  tags: [
    "operator-selection",
    "confinement",
    "gluon",
    "reduced-cost",
    "star-positivity",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Replaces broken `def:universal-ilp-algorithm` (`universal-ilp.py` `NameError: apply_atom_nf`, hardcoded two-crossing gluon) under `qou-mba8`. Generic-ordered-ring `ConfinementLayer` and reduced-cost decomposition live in `QOU.MathlibInfra.ConfinementLayerTower` (`ConfinementLayer`, `reducedCost`, `reduced_cost_decomposition`); step-4 gluon stabilization remains open across the four candidate stabilization arms.",
    },
  ],
});
