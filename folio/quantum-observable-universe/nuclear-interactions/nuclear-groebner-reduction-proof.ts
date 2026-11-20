import { proof } from "../../schema/builders";

export default proof({
  label: "prf:nuclear-groebner-reduction",
  title: "Proof of nuclear groebner reduction",
  uses: ["prop:nuclear-groebner-reduction", "def:hecke-normal-form"],
  cites: ["bokut2001", "bergman1978"],
});
