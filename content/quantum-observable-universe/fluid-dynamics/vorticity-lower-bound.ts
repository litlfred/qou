import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vorticity-lower-bound",
  title:
    "Vorticity lower bound for anti-parallel filament collision as $q \\to 1$",
  uses: [
    "thm:q-bkm",
    "conj:q-aubin-lions",
  ],
  tags: [
    "vorticity",
    "lower-bound",
    "biot-savart",
    "anti-parallel",
    "blowup",
    "last-gap",
  ],
});
