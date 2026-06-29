import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:arc-space",
  label: "rem:adelic-tate-motivic-dual",
  title:
    "Motivic dual of the adelic zeta factorisation via the arc space and motivic measure",
  uses: [
    "def:arc-space",
    "rem:adelic-tate-squeeze",
    "rem:bsd-surreal-bound",
  ],
  tags: [
    "adeles",
    "motivic-integration",
    "arc-space",
    "tate-thesis",
    "surreal",
  ],
  cites: [
    "kontsevich1995",
    "denef-loeser2001",
  ],
});
