import { simulator } from "../../../folio-assistant/schemas/builders";

export default simulator({
  label: "sim:knot-periodic-table",
  title: "Knot-Centric Periodic Table with Beta Decay",
  html: "simulators/knot_periodic_table.html",
  uses: [
    "prop:shell-structure-eigenvalues",
    "prop:knot-particle-correspondence",
  ],
  tags: [
    "periodic-table",
    "knot-centric",
    "nuclear-shell",
    "borromean",
    "transfer-matrix",
    "skein-polynomial",
    "beta-decay",
    "knot-diagram",
    "interactive",
  ],
  defaultView: {
    name: "default",
    title: "Knot-centric layout with nuclear sub-shell filling",
    params: {
      layout: "knot-centric",
      color: "block",
      columns: "nuclear",
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
