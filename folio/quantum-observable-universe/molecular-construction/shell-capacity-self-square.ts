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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The $q=1$ integer identities above are proved in Lean (sum of the first $n$ odd numbers, by induction). The full $q$-deformed self-square, cleared of the denominator $(q - q^{-1})$, is the polynomial identity `qCG_self_square`, proved for every $n$ in the sibling of" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The full $q$-deformed self-square, cleared of the denominator $(q - q^{-1})$, is a polynomial identity proved for every $n$; see [The shell state space is the self-square of the angular object](#conj:shell-space-is-self-square)." },
  ],
});
