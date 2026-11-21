import { remark } from "../../schema/builders";

// Was rem:hook-weight-derivation-sketch. The block it argued for is now the conjecture
// conj:hook-weight-derivation (owner, #8526, 2026-11-21; bean qou-tm3c), so the
// argument is recorded as an interpretive sketch, not a proof (AGENTS.md §3b).
export default remark({
  label: "rem:hook-weight-derivation-sketch",
  title: "Argument sketch for the hook-weight conjecture",
  interprets: "conj:hook-weight-derivation",
  uses: ["conj:hook-weight-derivation"],
});
