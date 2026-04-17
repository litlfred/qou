import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-heat-equation-exists",
  title: "Proof of well-posedness of the $q$-heat equation",
  uses: ["prop:q-heat-equation-exists"],
});
