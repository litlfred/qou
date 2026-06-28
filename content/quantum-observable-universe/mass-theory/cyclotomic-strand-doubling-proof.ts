import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cyclotomic-strand-doubling",
  title: "Proof of cyclotomic strand doubling",
  uses: ["lemma:cyclotomic-strand-doubling"],
});
