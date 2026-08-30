import { proof } from "../../schema/builders";

export default proof({
  label: "prf:piece-a-specht-character-trace",
  title: "Proof of the $C_2$ traces on $S^\\mu$ and on the regular representation",
  uses: ["lem:piece-a-specht-character-trace"],
  cites: ["serre1977", "sagan2001"],
});
