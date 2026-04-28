import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-instanton",
  label: "ex:instanton",
  title: "Instanton connection",
  tags: ["instanton", "archimedean"],
  lean: { ref: "qou:QOU.InstantonConnection",
    validation: "leanok",
  },
  uses: ["ex:c-quantum-universe", "def:categorical-instanton"],
});
