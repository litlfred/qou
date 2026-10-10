import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ew-triplet-charge-spin-from-involution",
  title: "Bar-parity of the even-twist carriers and the forced quantum numbers",
  uses: ["thm:ew-triplet-charge-spin-from-involution", "def:spin-involution", "prop:self-dual-higgs-real-volume"],
});
