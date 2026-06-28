import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:shell-structure-eigenvalues",
  label: "rem:shell-eigenvalue-subshells",
  title:
    "Sub-shell structure from multi-electron tensor products: orbital capacities $2(2\\ell+1)$",
  uses: ["prop:shell-structure-eigenvalues"],
  tags: [
    "shell",
    "sub-shell",
    "tensor-product",
    "orbital-capacity",
  ],
});
