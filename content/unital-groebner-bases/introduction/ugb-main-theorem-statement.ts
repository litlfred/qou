import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ugb-main",
  title: "Freeness of quotient by unital Gröbner basis",
  tags: ["groebner-basis", "freeness", "main-result"],
  uses: [
    "def:admissible-system",
    "def:unital-groebner-basis",
  ],
});
