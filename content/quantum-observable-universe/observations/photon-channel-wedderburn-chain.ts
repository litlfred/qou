import { remark } from "../../schema/builders";

export default remark({
  label: "rem:photon-channel-wedderburn-chain",
  title: "From 4 photon channels to 3 Wedderburn invariants",
  interprets: "prop:wedderburn-mass-formula",
  uses: ["prop:wedderburn-mass-formula"],
});
