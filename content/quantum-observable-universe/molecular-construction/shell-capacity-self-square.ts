import { proposition } from "../../schema/builders";

/**
 * Shell capacity 2n² as the q=1 self-square of the angular q-dimension.
 * The DERIVED leg of the electron-shell program: an elementary, sorry-free
 * Lean identity (sum of the first n odd numbers), doubled by spin.
 */
export default proposition({
  label: "prop:shell-capacity-self-square",
  title: "Shell capacity $2n^2$ as the self-square of the angular $q$-dimension",
  lean: {
    ref: "qou:QOU.Molecular.shell_capacity_self_square",
    validation: "not_checked",
  },
  uses: ["def:electron-shell-braid-capacity"],
  tags: [
    "shell-capacity",
    "self-square",
    "q-clebsch-gordan",
    "bar-even",
    "no-second-su2",
  ],
});
