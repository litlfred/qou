import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:madelung-fluid",
  label: "rem:hamilton-jacobi-phase",
  title: "Hamilton--Jacobi equation for the phase and classical trajectories",
  uses: ["rem:geodesic-vortices"],
  tags: ["hamilton-jacobi", "phase", "classical-limit", "eikonal", "WKB"],
});
