import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-q-connection",
  label: "ex:q-connection",
  title: "$q$-Deformed connection",
  lean: { ref: "qou:QOU.qConnection", validation: "not_checked" },
  uses: ["ex:instanton", "def:categorical-q-connection"],
  tags: ["connection", "archimedean"],
});
