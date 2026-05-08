import { remark } from "../../schema/builders";

export default remark({
  label: "rem:photon-channel-wedderburn-chain",
  title: "From 4 photon channels to 3 Wedderburn invariants",
  interprets: "thm:wedderburn-mass-formula",
  uses: ["thm:wedderburn-mass-formula"],
});
