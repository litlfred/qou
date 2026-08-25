import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:geodesic-vortices",
  title: "Geodesic vortices: variational characterisation and stability",
  uses: [
    "rem:geometric-drag",
    // Supplies the quantum pressure Q_q in the energy functional's integrand,
    // and the acoustic metric whose geodesics the block characterises.
    "rem:madelung-fluid",
  ],
  tags: ["vortex", "geodesic", "variational", "stability", "morse-index"],
});
