import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:positive-definite-dagger",
  label: "rem:dagger-notation",
  title: "Notation: $\\dagger$, $\\ast$, and the physicist's adjoint",
  uses: ["prop:positive-definite-dagger"],
  tags: ["notation", "pedagogy"],
});
