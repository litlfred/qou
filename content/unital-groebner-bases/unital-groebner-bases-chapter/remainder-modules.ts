import { definition } from "../../schema/builders";

export default definition({
  label: "def:remainder-modules",
  title: "Remainder modules $O(I)$ and $\\widetilde{O}(I)$",
  tags: ["groebner-basis", "module"],
  lean: {
    decl: "QOU.UnitalGroebner.RemainderModule",
    validation: "not_checked",
  },
  uses: ["def:admissible-system", "def:leading-terms"],
});
