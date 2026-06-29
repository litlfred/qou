import { definition } from "../../schema/builders";

export default definition({
  label: "def:information-bandwidth",
  title: "Information bandwidth per Planck time",
  tags: [
    "information-bandwidth",
    "information-theory",
    "bremermann",
    "speed-of-light",
    "operational-entropy",
  ],
  lean: { ref: "qou:QOU.Information.informationBandwidth",
    validation: "not_checked",
  },
  uses: [
    "def:information-speed-of-light",
    "def:operational-entropy",
  ],
});
