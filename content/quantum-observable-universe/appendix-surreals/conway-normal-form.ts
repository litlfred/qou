import { remark } from "../../schema/builders";

export default remark({
  label: "rem:conway-normal-form",
  title:
    "Conway normal form unifies Big-O / little-o / Θ / $\\sim$",
  tags: [
    "surreal-numbers",
    "conway-normal-form",
    "big-o",
    "little-o",
    "asymptotic",
    "leading-exponent",
    "notation",
    "cross-reference",
  ],
  interprets: "def:birthday-grading",
  uses: ["def:surreal-blowup-calculus"],
  cites: ["conway1976", "gonshor1986", "ehrlich2012"],
});
