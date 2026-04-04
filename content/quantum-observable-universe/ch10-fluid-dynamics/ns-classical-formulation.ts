import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:ns-obstruction",
  label: "rem:ns-classical-formulation",
  title: "The classical regularity question for the Navier--Stokes equation",
  uses: [
    "def:ns-obstruction",
    "def:q-navier-stokes",
  ],
  tags: ["navier-stokes", "regularity", "classical", "formulation"],
});
