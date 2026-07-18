import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hecke-baer-star-generic",
  label: "rem:hecke-baer-star-generic-corollary",
  title:
    "Central primitive idempotents as a complete system of bar-aware projections",
  tags: ["hecke-algebra", "baer-star", "central-idempotent", "bar-involution"],
  uses: ["prop:hecke-baer-star-generic", "prop:explicit-central-idempotent"],
});
