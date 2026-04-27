import { simulator } from "../../../folio-assistant/schemas/builders";

export default simulator({
  label: "sim:knot-atom-diagrams",
  title: "Knot Diagrams of Light Atoms ($Z \\leq 4$)",
  html: "folio-assistant/simulators/knot_atom_diagrams.html",
  uses: ["rem:knot-atom-diagrams"],
  tags: [
    "knot-diagram",
    "trefoil",
    "hopf-link",
    "electron-shell",
    "sub-link",
    "atom",
    "interactive",
    "borromean",
  ],
  defaultView: {
    name: "default",
    title: "Light atom knot diagrams (H, He, Li, Be)",
    params: {
      display: "all",
    },
  },
});
