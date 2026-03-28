import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-reeb",
  label: "ex:q-lie-bracket",
  title: "$q$-Deformed Lie bracket",
  tags: ["lie-bracket", "archimedean"],
  lean: {
    decl: "QOU.qLieBracket",
    validation: "leanok",
  },
  uses: ["def:categorical-q-lie-bracket"],
});
