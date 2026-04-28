import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-reeb",
  label: "ex:q-lie-bracket",
  title: "$q$-Deformed Lie bracket",
  tags: ["lie-bracket", "archimedean"],
  lean: { ref: "qou:QOU.qLieBracket",
    validation: "leanok",
  },
  uses: ["def:categorical-q-lie-bracket"],
});
