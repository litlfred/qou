import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-operator-energy-consumers",
  title: "Consumers: gluon-channel selection by energy minimisation",
  interprets: "def:knot-operator-energy",
  uses: [
    "def:knot-operator-energy",
    "def:categorical-proton",
    "def:categorical-neutron",
  ],
  tags: [
    "knot-operator",
    "gluon-channel",
    "proton",
    "neutron",
    "energy-minimisation",
  ],
});
