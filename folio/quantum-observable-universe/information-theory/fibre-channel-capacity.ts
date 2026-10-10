import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:one-dim-qou-channel",
  label: "rem:fibre-channel-capacity",
  title: "Information capacity of a fibre as Markov-trace entropy",
  tags: [
    "optical-fibre",
    "channel-capacity",
    "markov-trace",
    "operational-entropy",
    "information-theory",
  ],
  uses: ["def:one-dim-qou-channel"],
});
