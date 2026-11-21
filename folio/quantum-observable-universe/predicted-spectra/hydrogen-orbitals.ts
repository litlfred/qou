import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hydrogen-shell-writhe",
  label: "rem:hydrogen-orbitals",
  title:
    "Hydrogen orbitals: the spinning trefoil around the Borromean anchor",
  tags: [
    "hydrogen",
    "orbital",
    "shell",
    "subshell",
    "trefoil",
    "writhe",
    "borromean",
    "electron-cloud",
  ],
  uses: [
    "ex:hydrogen-knot-structure",
    "conj:hydrogen-shell-writhe",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): , and it is proved as `mode_cutoff_iff` in the Lean sibling of that conjecture, with no symmetry group entering the argument." },
    { kind: "caveat", date: "2026-11-21", body: "This block reads the electron as the trefoil $T_{2,3}$. On 2026-11-21 the owner ruled, for now, that the electron is the braid word $\\sigma_0\\sigma_1\\sigma_0$, whose closure is the Hopf link; the trefoil ($\\sigma_0^3$ on $B_2$) is kept as the backup reading. Under the primary ruling, photon absorption is the strand-adding curl $\\sigma_0\\sigma_1\\sigma_0 \\to \\sigma_0\\sigma_1\\sigma_0\\sigma_2 \\to \\cdots$, a Markov stabilisation. The closure stays the Hopf link, the excited word is Gröbner–Shirshov reduced, and the level shows as word length and as one factor of $z_D$ in the Markov trace. The writhe $+2$ picture below is the backup reading only. Its diagram-level statement (two R-I moves preserve the knot type) is correct; read as braid powers $\\sigma^{2n+1}$ on two strands it would give $T_{2,2n+1}$ instead. See docs/audits/2026-11-21-photon-excitation-gs-reduction.md §4a and bean qou-xc7g." },
  ],
});
