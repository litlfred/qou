import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:spin-from-so3-fiber",
  title:
    "Spin $\\mathrm{SU}(2)_S$ from full $\\mathrm{SO}(3)$ fiber action on color-sheet rotations",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.SpinFromSo3Fiber",
    validation: "not_checked",
  },
  uses: [
    "conj:inter-nucleon-channel-color-tube",
    "thm:jones-markov-trace",
  ],
  cites: [
    "klein1888",
    "kashiwara1991",
    "khovanov-lauda2009",
    "wigner1937",
  ],
  tags: [
    "spin",
    "duality-d10",
    "so3-fiber",
    "color-tube",
    "spherical-harmonic-h4",
    "bring-surface",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-06-01",
      body:
        "**Stated $h^4$-source mechanism falsified (core conjecture unaffected).** A character-table derivation (audit `2026-06-01-s5-so3-su2-u1-fiber-action.md`) refutes two sub-claims of this conjecture's *argument*, though not its core (spin $=\\mathrm{SO}(3)$ lift): (1) the premise that the discrete $S_3$ subgroup \"sees only $\\ell \\le 1$\" is **false** — under $S_3 \\subset \\mathrm{SO}(3)$ the standard/$(2,1)$ irrep already appears at **both** $\\ell=1$ (mult 1) and $\\ell=2$ (mult 2), so $S_3$ is not $\\ell$-truncated and the \"only full $\\mathrm{SO}(3)$ reaches $\\ell=2$\" reasoning does not hold; (2) the icosahedral story lives on $A_5 \\subset S_5$ (**5 strands**) whereas $h^4=-3/4$ lives on the $H_3$ Borromean trace (**3 strands**, the $(2,1)$ irrep) — different representation rings with no canonical map, so the $\\ell=2 \\Rightarrow h^4$ link is not derivable as written. A genuine positive survives: spin-$\\mathbb{Z}_2 \\ne$ sign-$\\mathbb{Z}_2$ (binary icosahedral $2I$ is perfect, $|2I|=120=|S_5|$, $2I \\not\\cong S_5$), so spin is a ribbon/framing phenomenon. The missing object is a functor from the $S_5$/$\\mathrm{SO}(3)$ level $\\ell$ to a Wedderburn coefficient of the 3-strand $H_3$ trace.",
      see: "docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md",
    },
  ],
});
