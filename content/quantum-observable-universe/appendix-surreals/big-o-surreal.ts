import { remark } from "../../schema/builders";

export default remark({
  label: "rem:big-o-surreal",
  title:
    "Big-O / little-o / $\\Theta$ / $\\sim$ are leading-exponent assertions",
  tags: [
    "surreal-numbers",
    "big-o",
    "little-o",
    "asymptotic",
    "notation",
    "valuation",
    "leading-exponent",
    "register",
  ],
  interprets: "rem:conway-normal-form",
  uses: [
    "rem:conway-normal-form",
    "def:birthday-grading",
  ],
  cites: ["conway1976", "gonshor1986", "ehrlich2012"],
});
