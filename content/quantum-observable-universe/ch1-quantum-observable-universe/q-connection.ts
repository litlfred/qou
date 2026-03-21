import { example } from "../../schema/builders";

export default example({
  label: "ex:q-connection",
  title: "$q$-Deformed connection",
  lean: { decl: "QOU.qConnection", validation: "not_checked" },
  uses: ["ex:instanton", "def:categorical-q-connection"],
  tags: ["connection", "archimedean"],
});
