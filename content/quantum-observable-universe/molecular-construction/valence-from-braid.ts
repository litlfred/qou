import { remark } from "../../schema/builders";

/**
 * Valence electron count and bonding capacity derived from
 * the atomic braid LP dual.
 */
export default remark({
  label: "rem:valence-from-braid",
  title: "Valence and bonding capacity from the atomic braid",
  interprets: "def:electron-shell-braid-capacity",
  uses: ["prop:shell-filling-rule"],
  tags: ["valence", "bonding-capacity", "octet-rule"],
});
