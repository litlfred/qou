import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gs-quotient-ideals-i8-i9-remark",
  title: "Why the quotient ideals $I_8$ and $I_9$ reduce the normal form",
  interprets: "def:gs-quotient-ideals-I8-I9",
  tags: ["groebner-shirshov", "quotient-ideal"],
  uses: [
    "def:gs-quotient-ideals-I8-I9",
    "prop:shell-closure-normal-form",
  ],
});
