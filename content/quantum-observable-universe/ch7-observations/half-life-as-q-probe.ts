import { remark } from "../../schema/builders";

export default remark({
  label: "rem:half-life-as-q-probe",
  title:
    "Beta-decay half-lives as precision probes of local $q$-variation",
  tags: [
    "half-life",
    "substrate-parameter",
    "experimental",
    "neutron-star",
    "heavy-ion",
    "magnetic-field",
    "sensitivity",
  ],
  uses: [
    "prop:hadron-half-life",
    "rem:hadron-half-life-regimes",
    "prop:hadron-q-self-correction",
    "def:substrate-parameter",
    "prop:local-substrate-q",
    "rem:c-substrate-via-levi",
  ],
});
