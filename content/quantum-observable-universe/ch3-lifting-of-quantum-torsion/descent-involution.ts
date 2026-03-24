import { definition } from "../../schema/builders";

export default definition({
  label: "def:descent-involution",
  lean: { decl: "QOU.DescentInvolution" },
  title: "Descent involution",
  tags: ["descent", "involution", "idempotent"],
  uses: [
    "prop:jet-prolongation",
    "lem:descent",
  ],
});
