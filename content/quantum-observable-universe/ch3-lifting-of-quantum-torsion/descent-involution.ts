import { definition } from "../../schema/builders";

export default definition({
  label: "def:descent-involution",
  lean: { decl: "QOU.DescentInvolution" },
  status: "not_started",
  title: "Descent involution",
  tags: ["descent", "involution", "idempotent"],
  uses: [
    "prop:jet-prolongation",
    "lem:descent",
  ],
});
