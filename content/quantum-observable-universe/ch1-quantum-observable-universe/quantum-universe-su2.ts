import { example } from "../../schema/builders";

export default example({
  label: "ex:quantum-universe-su2",
  title: "$\\mathrm{SU}(2)$ as a quantum universe",
  tags: ["su2", "quantum"],
  uses: ["def:quantum-universe", "def:frobenius-pairing", "ex:rigid-monoidal-vect"],
});
