import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-ns-properties",
  title: "Properties of the $q$-Navier--Stokes system",
  uses: ["def:q-navier-stokes", "thm:q-ns-wellposedness"],
});
