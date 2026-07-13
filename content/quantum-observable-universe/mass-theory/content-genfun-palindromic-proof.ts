import { proof } from "../../schema/builders";

export default proof({
  label: "prf:content-genfun-palindromic",
  title:
    "Proof that $C_n(q)$ is palindromic and bar-even via the conjugation anti-involution",
  uses: [
    "prop:content-genfun-palindromic",
  ],
});
