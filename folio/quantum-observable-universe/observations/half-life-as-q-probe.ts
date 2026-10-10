import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hadron-q-self-correction",
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
  uses: ["rem:c-substrate-via-levi"],
});
