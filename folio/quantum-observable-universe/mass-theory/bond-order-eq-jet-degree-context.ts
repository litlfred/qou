import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bond-order-eq-jet-degree-context",
  title: "Obligation-(C) identification, cluster exhaustiveness, and physical framing",
  interprets: "lem:bond-order-eq-jet-degree",
  tags: ["jet-filtration", "grobner-shirshov", "body-order", "binding"],
  uses: ["lem:bond-order-eq-jet-degree"],
});
