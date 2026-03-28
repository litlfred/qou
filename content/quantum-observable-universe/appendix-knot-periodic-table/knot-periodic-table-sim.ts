import { simulator } from "../../../folio-assistant/schemas/builders";

export default simulator({
  label: "sim:knot-periodic-table",
  title: "Knot-Centric Periodic Table",
  html: "folio-assistant/simulators/knot_periodic_table.html",
  uses: [
    "prop:nuclear-shell-intruder",
    "prop:shell-structure-eigenvalues",
  ],
  tags: [
    "periodic-table",
    "knot-centric",
    "nuclear-shell",
    "electron-shell",
    "borromean",
    "transfer-matrix",
    "skein-polynomial",
    "interactive",
  ],
  defaultView: {
    name: "default",
    title: "Knot-centric layout with electron block coloring",
    params: {
      layout: "knot-centric",
      color: "block",
      filter: "all",
      q: 1.11,
    },
  },
  views: [
    {
      name: "magic-numbers",
      title: "Magic numbers highlighted",
      params: {
        layout: "standard",
        color: "shell",
        filter: "magic",
        q: 1.11,
      },
    },
    {
      name: "binding-energy",
      title: "Binding energy gradient",
      params: {
        layout: "standard",
        color: "ba",
        filter: "all",
        q: 1.11,
      },
    },
    {
      name: "alpha-clusters",
      title: "Alpha sub-link count",
      params: {
        layout: "standard",
        color: "kalpha",
        filter: "all",
        q: 1.11,
      },
    },
    {
      name: "transfer-matrix",
      title: "Transfer matrix complexity (Skein polynomial degree)",
      params: {
        layout: "standard",
        color: "skein-deg",
        filter: "all",
        q: 1.11,
      },
    },
    {
      name: "shell-eigenvalues",
      title: "Shell eigenvalue $\\lambda_+^n$ at outermost shell",
      params: {
        layout: "knot-centric",
        color: "lambda",
        filter: "all",
        q: 1.11,
      },
    },
  ],
});
