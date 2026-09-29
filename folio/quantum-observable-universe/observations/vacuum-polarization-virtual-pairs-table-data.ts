import { table } from "../../schema/builders";

export default table({
  label: "tbl:vacuum-polarization-virtual-pairs-table-data",
  title: "QFT concepts and their QOU brane-tower realisations",
  caption:
    "Six standard quantum-field-theory concepts (on-shell particle, " +
    "virtual particle, propagator, vacuum polarisation, loop correction, " +
    "off-shell lifetime) paired with their QOU realisations in the " +
    "recursive brane-tower picture.",
  uses: ["rem:vacuum-polarization-virtual-pairs"],
  tags: [
    "virtual-particles",
    "vacuum-polarisation",
    "qft-dictionary",
    "summary-table",
  ],
});
