import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:geodesic-vortices",
  title: "Geodesic vortices: variational characterisation and stability",
  uses: [
    "rem:madelung-fluid",
    "def:state-bundle",
    "def:mass-identity",
    "rem:geometric-drag",
    "def:adjoint-weight-decomposition",
    "prop:discrete-vortex-spectrum",
  ],
  tags: ["vortex", "geodesic", "variational", "stability", "morse-index"],
});
