import { simulator } from "../../schema/builders";

export default simulator({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Fermion-rule ruling (owner card, 2026-11-21 14:31Z, option 'Scope the rule, mark it open'): prop:fermion-boson-knot-link is a statement about the T(2,n) family only. The electron is sigma_0 sigma_1 sigma_0 in B_3 (closure: the Hopf link); its statistics are not classified by that proposition and are open. Issue #8822. Electron relabelled; the HTML simulator simulators/knot_periodic_table.html still draws the trefoil, and the prose now says so." },
  ],
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
