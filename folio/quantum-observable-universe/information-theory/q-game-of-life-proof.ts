import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-game-of-life",
  title: "Proof of q game of life",
  uses: ["prop:q-game-of-life"],
  cites: [
    "squier1984",
    "bennett1973",
    "toffoli1980",
    "fredkin1982",
    "shi2002",
    "aharonov2003",
  ],
});
