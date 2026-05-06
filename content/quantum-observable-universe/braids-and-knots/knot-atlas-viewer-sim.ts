import { simulator } from "../../../folio-assistant/schemas/builders";

/**
 * Recursive Knot-Atlas Viewer — interactive simulator paired with
 * `prop:recursive-atom-knot-atlas`.
 *
 * STRICT NO-HARDCODED-VALUES contract: every numeric / knot-identity
 * shown by the simulator HTML is read at runtime from
 * `knot-atlas-viewer-data.witness.json`, which itself sources from
 * `q_parameter.py`, `mass-table-ppb.witness.json`,
 * `methodology-deprecation.witness.json`,
 * `gb-filtration-jet-order.witness.json`, and the `def:confined-particle`
 * registry.
 *
 * The viewer supports two modes (`basis`, `confined`) with per-mode
 * coordinate-chart, scaling, and centre selectors; per-knot deep-links
 * are query-string driven so atlas tokens can link directly without
 * exploding the named-views list.
 */
export default simulator({
  label: "sim:knot-atlas-viewer",
  title: "Recursive Knot-Atlas Viewer",
  html: "folio-assistant/simulators/knot_atlas_viewer.html",
  computation: {
    engine: "python",
    script: "folio-assistant/computations/knot_atlas_viewer_data.py",
    witness: "folio-assistant/computations/knot-atlas-viewer-data.witness.json",
    status: "verified",
  },
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
    "def:confinement-level",
    "rem:knot-particle-dictionary",
  ],
  tags: [
    "simulator",
    "knot-atlas",
    "interactive",
    "wasm-ready",
    "recursive-atlas",
  ],
  defaultView: {
    name: "default-atlas-overview",
    title: "Default — basis-knot atlas overview",
    params: {
      mode: "basis",
      chart: "briggs-klein-A2",
      backend: "wasm",
    },
  },
  views: [
    {
      name: "basis-knot",
      title: "Basis-knot mode (gallery)",
      params: { mode: "basis", chart: "briggs-klein-A2" },
    },
    {
      name: "confined-baryon",
      title: "Confined baryon mode (proton/neutron)",
      params: {
        mode: "confined",
        chart: "briggs-klein-A2",
        scaling: "S2",
        centre: "C6",
        knot: "proton",
      },
    },
    {
      name: "hyperbolic-register",
      title: "Hyperbolic B3 (volume-puff) chart",
      params: { mode: "basis", chart: "hyperbolic-B3" },
    },
    {
      name: "polar-projection",
      title: "Polar 2D braid-closure projection",
      params: { mode: "basis", chart: "polar-knot-projection" },
    },
    {
      name: "confinement-sweep",
      title: "Confinement-sweep ($q$ slider)",
      params: {
        mode: "confined",
        chart: "briggs-klein-A2",
        scaling: "S2",
        centre: "C6",
      },
    },
  ],
});
