import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:nuclear-groebner-reduction",
  label: "rem:nuclear-groebner-reduction-computational",
  title: "Computational tractability of the nuclear normal form",
  uses: ["prop:nuclear-groebner-reduction"],
});
