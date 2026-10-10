import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:toffoli-transfer-matrix",
  label: "rem:toffoli-transfer-matrix-interpretation",
  title: "Explicit q-AND amplitudes at the substrate value $q_0$",
  uses: [
    "prop:toffoli-transfer-matrix",
    "prop:local-substrate-q",
  ],
});
