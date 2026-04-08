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
    "prop:brings-is-qou",
    "ex:brings-surface-concrete",
    "ex:substrate-parameter-brings",
    "ex:tannaka-krein-su2",
    "prop:vacuum-state",
  ],
});
