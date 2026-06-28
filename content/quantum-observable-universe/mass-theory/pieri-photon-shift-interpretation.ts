import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:pieri-photon-shift",
  label: "rem:pieri-photon-shift-interpretation",
  title: "The Pieri box-shift as a non-commutative Fourier single-step shift",
  uses: ["prop:pieri-photon-shift", "prop:wedderburn-as-noncomm-fourier"],
});
