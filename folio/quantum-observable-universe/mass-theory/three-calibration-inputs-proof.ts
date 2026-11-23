import { remark } from "../../schema/builders";

// Was prf:three-calibration-inputs. The block it argued for is now the
// conjecture conj:three-calibration-inputs (owner choice 2026-11-20, bean
// qou-tm3c), so the argument is recorded as a sketch (AGENTS.md §3b).
export default remark({
  label: "rem:three-calibration-inputs-sketch",
  title: "Why three calibration inputs (sketch)",
  interprets: "conj:three-calibration-inputs",
  uses: ["conj:three-calibration-inputs"],
});
