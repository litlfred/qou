import { table } from "../../schema/builders";
export default table({
  label: "tbl:sigma-shell-from-beta-chain-derivation-table-data",
  title: "Data table from conj:sigma-shell-from-beta-chain-derivation",
  uses: ["conj:sigma-shell-from-beta-chain-derivation"],
  tags: ["extracted-table"],
  computation: { engine: "mpmath", script: "computations/sigma_shell_from_beta_chain.py", witness: "computations/sigma-shell-from-beta-chain.witness.json", status: "verified" },
});
