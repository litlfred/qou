import { example } from "../../schema/builders";

export default example({
  interprets: "thm:descartes",
  label: "ex:terminal-morphism-brings",
  title:
    "Constructive terminal morphism to Bring's QOU",
  tags: [
    "brings-surface",
    "terminal-object",
    "constructive",
    "descartes-universe",
  ],
  uses: [
    "thm:descartes",
    "ex:tannaka-krein-su2",
    "prop:vacuum-state",
  ],
});
