import { proof } from "../../schema/builders";

export default proof({
  label: "prf:descartes-elliptic-curve",
  title: "Proof of descartes elliptic curve",
  uses: ["prop:descartes-elliptic-curve"],
});
