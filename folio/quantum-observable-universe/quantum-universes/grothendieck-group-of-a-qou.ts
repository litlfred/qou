import { definition } from "../../schema/builders";

export default definition({
  label: "def:grothendieck-group-of-a-qou",
  title: "The Grothendieck group of a quantum universe",
  lean: { ref: "qou:QOU.GrothendieckChern.K0", validation: "not_checked" },
  uses: ["def:quantum-universe", "rem:simple-objects-V", "def:rigid-monoidal-category"],
  defines: ["grothendieck-group"],
  foreshadows: ["def:chern-character", "ex:su2-characters-and-quantum-dimension"],
  cites: ["bghl-2017", "kassel1995"],
  tags: ["grothendieck-group", "k-theory", "wedderburn", "quantum-dimension"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): **The example to keep in mind.** For $\\mathbf{C} = \\mathrm{Rep}(\\mathrm{SU}(2))$, with simple objects $V_n$ of dimension $n + 1$, the Clebsch–Gordan rule $V_1 \\otimes V_n = V_{n-1} \\oplus V_{n+1}$ makes $K_0(\\mathbf{C}) = \\mathbb{Z}[x]$ with $x = [V_1]$: each $[V_n]$ is the polynomial in $x$ determined by $x\\,[V_n] = [V_{n-1}] + [V_{n+1}]$, and the rank of $[V_n]$ is $1$ while $\\dim_q [V_n] = [n+1]_q$. The quantum group $\\mathrm{Rep}(\\mathrm{SU}_q(2))$ at generic $q$ has the same simple objects, the same Clebsch–Gordan rule, and hence the same Grothendieck ring; what changes with $q$ is not the group $K_0$ but the homomorphism $\\dim_q$ out of it. That is the sense in which the quantum dimension, and not the Grothendieck class, is the $q$-dependent object \\cite{bghl-2017}." },
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Introduced by the 2026-09-15 explicit-layer selection (owner option B). The Lean carrier `QOU.GrothendieckChern.K0` in `lean/QOU/GrothendieckChern.lean` presents `K_0` on the block set of axiom 4 as `U.blocks →₀ ℤ`, with the rank and the additively extended quantum dimension, sorry-free. The factorisation `dim_q = ev ∘ ch` (bean `qou-mjt3`, item 3) is proved there as `dimQK0_eq_evDimQ_chernCharacter` and is the content of `def:chern-character`.",
    },
  ],
});
