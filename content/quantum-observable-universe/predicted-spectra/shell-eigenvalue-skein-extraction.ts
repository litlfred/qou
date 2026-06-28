import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:shell-structure-eigenvalues",
  label: "rem:shell-eigenvalue-skein-extraction",
  title:
    "Determining shells from an arbitrary Skein polynomial: the transfer-matrix diagonalization algorithm",
  uses: ["prop:shell-structure-eigenvalues"],
  tags: [
    "shell",
    "skein",
    "transfer-matrix",
    "extraction-algorithm",
  ],
});
