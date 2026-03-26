import { remark } from "../../schema/builders";

export default remark({
  label: "rem:valley-table",
  title:
    "Representative stable isotopes: Coulomb ratio and Diophantine error",
  tags: [
    "valley-of-stability",
    "diophantine",
    "codata",
    "neutron-proton-ratio",
  ],
  uses: [
    "prop:integer-stability",
    "rem:diophantine-valley",
    "prop:beta-stability",
    "def:stable-nucleus",
  ],
});
