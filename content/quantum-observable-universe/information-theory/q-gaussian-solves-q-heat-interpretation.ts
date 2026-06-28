import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-gaussian-solves-q-heat",
  label: "rem:q-gaussian-solves-q-heat-interpretation",
  title: "Time-rescaling interpretation of the Reeb-invariant $q$-Gaussian",
  uses: ["prop:q-gaussian-solves-q-heat"],
});
