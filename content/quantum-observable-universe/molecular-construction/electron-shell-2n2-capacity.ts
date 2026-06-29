import { conjecture } from "../../schema/builders";

/**
 * The open 2n² shell-capacity claim (electron-shells-Hopf conjecture): the 2×2
 * photon-electron transfer matrix gives only a 2-fold degeneracy, so the
 * 2n² = 2·Σ(2ℓ+1) count would require an SO(4)-type accidental degeneracy.
 * Previously embedded as "open problem 1" inside def:electron-shell-braid-capacity.
 */
export default conjecture({
  label: "conj:electron-shell-2n2-capacity",
  title: "Shell capacity $2n^2$ from an $\\mathrm{SO}(4)$ accidental degeneracy",
  uses: ["def:electron-shell-braid-capacity"],
  tags: [
    "shell-capacity",
    "2n2",
    "SO4",
    "accidental-degeneracy",
    "open-problem",
  ],
});
