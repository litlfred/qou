import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:symmetric-point-channel-collapse",
  proofs: ["prf:symmetric-point-channel-collapse"],
  lean: { ref: "qou:QOU.symmetric_point_channel_collapse",
    validation: "not_checked",
  },
  title: "Channel collapse at the symmetric point",
  tags: ["symmetric-point", "hecke", "degeneration"],
  uses: [],
});
