import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hydrogen-capacity",
  title:
    "Hydrogen capacity from chain topology and unsaturation degree",
  tags: [
    "hydrogen",
    "capacity",
    "saturation",
    "alkane",
    "alkene",
    "alkyne",
    "iupac",
    "taxonomy",
  ],
  lean: { ref: "qou:QOU.Organic.hydrogenCapacity",
    validation: "not_checked",
  },
  uses: ["rem:organic-chain-taxonomy"],
  cites: [],
});
