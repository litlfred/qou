import { remark } from "../../schema/builders";

export default remark({
  label: "rem:surreal-rate-calculus-setup",
  title:
    "Surreal rate calculus — infinitesimal setup and classical-limit rate table",
  interprets: "prop:surreal-rate-calculus",
  uses: [
    "prop:surreal-rate-calculus",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "thm:quantum-gap-collapse",
  ],
  tags: [
    "surreal",
    "reeb-infinitesimal",
    "rate-table",
    "classical-limit",
    "appendix",
  ],
});
