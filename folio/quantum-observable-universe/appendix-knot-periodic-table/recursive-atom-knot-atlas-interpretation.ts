import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-interpretation",
  title:
    "Provenance of the recursive atom-knot atlas entries",
  interprets: "prop:recursive-atom-knot-atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
  ],
  cites: [
    "wenzl1988",
    "codata2022",
    "pdg2024",
    "ame2020tables",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-4b6g: retired dead provenance claims referencing `computations/recursive_atom_knot_atlas_render.py` and `computations/witness_staleness_tracker.py` (both moved to `computations/_deprecated/`) and dropped the unenforced 'every entry never drifts / no entry maintained by hand' overclaim. Live producers are `computations/master_atlas_jacobian_80dps.py` (Master Tables A.1-A.5 and `master-atlas-80dps.witness.json`), `computations/atlas_render_canonical_table.py`, `computations/atlas_render_stability_summary.py`, and `computations/atlas_render_per_z.py` (`<!-- AUTO:... -->` regions of `recursive-atom-knot-atlas-registry.md`), whereas `computations/per_atom_hyperbolic_volume_witness.py` carries a hardcoded 6-entry `ATLAS` dictionary (`p`, `n` principled Borromean closure; `D = 6_2`, `T = 8_11`, `3He = L6a4` quarantined `manual-historical-volume-match`; `4He` retired `magic-A-formula`). Converted broken `(#cite:...)` links to `\\cite{...}` + `cites[]`.",
    },
  ],
  tags: [
    "archimedean-bridge",
    "atlas",
    "build-pipeline",
    "appendix",
  ],
});
