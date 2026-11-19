import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:n-equals-1-vacuous-magic",
  label: "rem:n-equals-1-vacuous-magic-context",
  title: "Base case, empirical magic numbers, and archimedean scope of vacuous primality",
  tags: ["primality", "magic-numbers", "recursion-base-case"],
  uses: ["prop:n-equals-1-vacuous-magic"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
