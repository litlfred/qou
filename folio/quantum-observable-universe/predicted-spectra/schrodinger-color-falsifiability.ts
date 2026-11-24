import { remark } from "../../schema/builders";

export default remark({
  label: "rem:schrodinger-color-falsifiability",
  title:
    "Schrödinger's color metric, diminishing returns, and a falsifiable $q_0$ prediction",
  interprets: "rem:q-chromaticity",
  tags: [
    "color",
    "chromaticity",
    "color-perception",
    "schrodinger",
    "weber-fechner",
    "falsifiability",
    "non-riemannian",
    "skein",
    "substrate-parameter",
  ],
  uses: ["rem:q-chromaticity"],
  cites: ["bujack2022", "schrodinger1920color"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "80-dps evaluation at the canonical proton-pinned substrate parameter " +
        "`q_at(80)` (`q_parameter.Q`) in " +
        "`computations/probes/schrodinger_color_bujack_q0_probe.py` " +
        "(`computations/probes/schrodinger-color-bujack-q0.witness.json`, " +
        "bean qou-fls0): `q_0 = 1.1099785827513808...`, `eta = " +
        "(q_0 - q_0^{-1})/2 = 0.10453015...`, `d* = 1/eta = 9.5666179...` " +
        "(correcting a prior `ln(q_0)` conflation `0.1043` / `9.59`).",
    },
  ],
});
