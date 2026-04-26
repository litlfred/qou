import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-q-bit",
  title: "The $q$-bit: unit of $q$-deformed information",
  tags: ["glossary", "information-theory", "q-bit", "operational-entropy", "hecke-algebra"],
  uses: [
    "def:operational-entropy",
    "prop:skein-generation",
    "def:reeb-bundle",
  ],
  defines: ["q-bit"],
});
