import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:electron-categorical-action-unity",
  title:
    "The emitted electron's categorical action equals $1$ in $m_e$ units (closes ELECTRON-1)",
  uses: [
    "prop:three-calibration-discipline",
    "def:categorical-action",
    "def:mass-identity",
    "rem:building-block-knots",
    "prop:bw-coefficient-shadow-price",
  ],
  tags: [
    "electron",
    "trefoil",
    "calibration",
    "beta-decay",
    "categorical-action",
    "frobenius-positivity",
    "audit-closure",
  ],
});
