import { remark } from "../../schema/builders";

export default remark({
  label: "rem:nucleon-pair-isospin-channel-remark",
  title: "Colour-flavour exchange antisymmetry behind the selection map",
  interprets: "def:nucleon-pair-isospin-channel",
  uses: [
    "def:nucleon-pair-isospin-channel",
    "prop:isospin-singlet-binds-more",
  ],
});
