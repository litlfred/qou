import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:wigner-2-coefficient",
  label: "rem:wigner-2-coefficient-interpretation",
  title: "$h/2$ is the isospin midpoint of the Hecke spectrum",
  uses: ["prop:wigner-2-coefficient"],
});
