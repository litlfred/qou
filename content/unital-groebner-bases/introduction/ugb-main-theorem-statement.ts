import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ugb-main",
  title: "Freeness of quotient by unital Gröbner--Shirshov basis",
  lean: { ref: "ugb:UGB.Introduction.main_theorem_statement", validation: "not_checked" },
  tags: ["groebner-basis", "freeness", "main-result"],
  uses: [
    "def:admissible-system",
    "def:unital-groebner-basis",
  ],
});
