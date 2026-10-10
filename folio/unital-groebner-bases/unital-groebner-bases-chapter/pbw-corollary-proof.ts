import { proof } from "../../schema/builders";

export default proof({
  label: "prf:pbw",
  uses: ["cor:pbw", "thm:buchberger"],
});
