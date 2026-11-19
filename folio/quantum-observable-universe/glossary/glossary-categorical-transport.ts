import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-categorical-transport",
  title: "Categorical transport equation",
  tags: ["glossary", "transport", "jet-bundle", "q-deformation"],
  uses: ["def:categorical-instanton", "def:categorical-q-ext-deriv", "def:categorical-jet"],
  defines: ["categorical-transport"],
});
