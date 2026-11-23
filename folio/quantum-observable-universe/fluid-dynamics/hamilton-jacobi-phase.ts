import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:madelung-fluid",
  label: "rem:hamilton-jacobi-phase",
  title: "Hamilton--Jacobi equation for the phase and classical trajectories",
  uses: ["rem:geodesic-vortices"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This grounds the Hamilton--Jacobi picture in the [discrete vortex spectrum](#prop:discrete-vortex-spectrum) and completes the correspondence between wave mechanics, fluid dynamics, and knot particles." },
  ],
  tags: ["hamilton-jacobi", "phase", "classical-limit", "eikonal", "WKB"],
});
