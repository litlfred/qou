import { remark } from "../../schema/builders";

// Was rem:joint-galois-braid-figure-8-verified-sketch. The block it argued for is now the conjecture
// conj:joint-galois-braid-figure-8-verified (owner, #8526, 2026-11-21; bean qou-tm3c), so the
// argument is recorded as an interpretive sketch, not a proof (AGENTS.md §3b).
export default remark({
  label: "rem:joint-galois-braid-figure-8-verified-sketch",
  title: "Argument sketch for the figure-8 joint Galois-braid conjecture",
  interprets: "conj:joint-galois-braid-figure-8-verified",
  uses: ["conj:joint-galois-braid-figure-8-verified"],
});
