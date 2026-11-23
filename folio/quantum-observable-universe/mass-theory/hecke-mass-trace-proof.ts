import { remark } from "../../schema/builders";

// Was prf:hecke-mass-trace. The block it argued for is now the conjecture
// conj:hecke-mass-trace (owner ruling 2026-11-20, bean qou-tm3c), so the
// argument is recorded as an interpretive sketch, not a proof (AGENTS.md §3b).
export default remark({
  label: "rem:hecke-mass-trace-sketch",
  title: "Argument sketch for the Hecke mass trace conjecture",
  interprets: "conj:hecke-mass-trace",
  uses: ["conj:hecke-mass-trace"],
});
