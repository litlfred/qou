import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-markov-trace",
  title: "Markov trace (Convention D)",
  tags: ["glossary", "markov-trace", "hecke-algebra", "convention-d"],
  uses: ["thm:jones-markov-trace", "prop:convention-d-kills-antisymmetriser"],
});
