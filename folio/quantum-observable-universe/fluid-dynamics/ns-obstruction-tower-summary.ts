import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-obstruction-tower-summary",
  title: "The NS obstruction as a local-cohomology residue",
  interprets: "prop:ns-obstruction-tower",
  uses: ["conj:levi-degeneracy"],
  tags: ["navier-stokes", "obstruction", "local-cohomology", "levi-form"],
});
