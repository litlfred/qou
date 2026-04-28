import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:geodesic-vortices",
  title: "Geodesic vortices: variational characterisation and stability",
  uses: [
    "rem:geometric-drag",
    "prop:discrete-vortex-spectrum",
  ],
  tags: ["vortex", "geodesic", "variational", "stability", "morse-index"],
});
