import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:x5-bring-weight-identification",
  label: "rem:x5-bring-weight-geometric-content",
  title: "Geometric content of the weight-$(-1)$ identification",
  uses: [
    "prop:x5-bring-weight-identification",
    "rem:u1-phase-tube",
    "rem:x5-bring-prym-jacobian",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The same categorical weight-$(-1)$ coordinate parametrises the single $\\mathrm{U}(1)$ phase tube of [rem:u1-phase-tube](#rem:u1-phase-tube) and the first Fourier mode of Bring's geometry. See [rem:x5-bring-prym-jacobian](#rem:x5-bring-prym-jacobian) for the parallel structure at the level of Jacobians." },
  ],
});
