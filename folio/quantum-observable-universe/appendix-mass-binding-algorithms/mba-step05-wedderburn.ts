import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:wedderburn-decomposition",
  title: "Semisimple Wedderburn decomposition and GPMT modified-trace renormalization on $H_n(q)$",
  uses: [
    "prop:wedderburn-trace-identity",
    "prop:wenzl-bridge-applicability-qou",
    "prop:wedderburn-as-noncomm-fourier",
    "prop:convention-d-kills-antisymmetriser",
  ],
  tags: [
    "mba",
    "step-5",
    "wedderburn",
    "wenzl",
    "gpmt",
    "canonical-chain",
  ],
});
