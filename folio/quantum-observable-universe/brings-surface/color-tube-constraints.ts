import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:color-tube-coordinates",
  label: "rem:color-tube-constraints",
  title: "Constraint equations in color tube coordinates",
  uses: [
    "rem:aggregate-color-quantities",
    "prop:x5-bring-weight-identification",
    "rem:u1-phase-tube",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-0.svg", blockIndex: 0, hash: "560d3f6cd3c0" },
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-1.svg", blockIndex: 1, hash: "9e3dff9fca6d" },
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-2.svg", blockIndex: 2, hash: "8f4af1d0c75c" },
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-3.svg", blockIndex: 3, hash: "5d19e432fe21" },
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The three shift laws and this transport are machine-checked (`QOU.Mass.ColorTubeSpectralBridge`: `psum1_shift`, `psum2_shift`, `psum3_shift`, `tube_psum1_of_bring`, `tube_psum2_of_bring`, `tube_psum3_of_bring`), as is the corresponding shift for the color tube cubic. Each identity is machine-checked in `QOU.Mass.ColorTubeSpectralBridge` (`shifted_quadric_eq_H2`, `shifted_cubic_eq_H3`, `spacetime_recovery_eq`, packaged as `constraints_spectral_form`)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The three color coordinates $r, g, b$ and the shift $z$ collapse to observables on the single $\\mathrm{U}(1)$ phase tube of [rem:u1-phase-tube](#rem:u1-phase-tube)." },
  ],
});
