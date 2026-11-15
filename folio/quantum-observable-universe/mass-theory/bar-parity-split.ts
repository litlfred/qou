import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bar-parity-split",
  title:
    "The binding trace and the $\\mathfrak{Q}_\\beta$ residue are the bar-even and bar-odd parts of one fibre element",
  uses: [
    "lem:bar-involution-parity-decomposition",
    "prop:sl2-prolongation-recurrence",
    "def:bar-involution",
    "conj:binding-qbeta-complex-volume",
  ],
  tags: ["bar-parity", "beta-decay", "binding-energy", "fibre-level"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-15",
      body: "**Demoted from `prop:bar-parity-split` to a conjecture (owner, 2026-11-15, option (a)).** Three reasons. (1) The Lean it cited, `QOU.Mass.evenPart_add_oddPart`, proves that ANY element of ANY module splits into a σ-fixed and a σ-anti part under a linear involution. That is true of everything, so it does not prove that the binding trace and the Q_β residue are the two parts of one element. It is kept, unchanged, as `lem:bar-involution-parity-decomposition`. (2) No Q_β functional on record is bar-odd: the retired Form A, the retired z = 1 trace $(q^2-1)(q^2-2q-1)/(2q^2)$ and the ruled z_D trace $(q^2-1)(q^4+1)P_{12}(q)/(4q^7(q^2+1)^2)$ all fail $f(q^{-1}) = -f(q)$; the ruled trace's bar-even part is $-h^2[2]_q(q^2+q^{-2})/8 \\neq 0$. They share only an overall factor $h = q - q^{-1}$ (docs/audits/2026-11-15-one-sided-weak-vertex.md §4, bean qou-hlx8). (3) As a proposition it violated AGENTS.md §3b, because `uses[]` contains `conj:binding-qbeta-complex-volume`.",
    },
    {
      kind: "caveat",
      date: "2026-11-15",
      body: "**What the conjecture needs in order to have content.** If $F$ is allowed to be any element of the same space as the two readouts, with identity readouts, then such an $F$ exists exactly when the binding trace is bar-even and the Q_β residue is bar-odd (take $F$ = their sum; conversely the odd part of anything is σ-anti, `oddPart_anti`). So the conjecture is non-trivial only with an $F$ and readout maps specified in advance, and with identity readouts it fails for every Q_β functional on record. Investigation of routes to close it: bean qou-qs0e children.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "**Honest negative, scope (b) for the ruled element only (bean qou-hlx8; audit docs/audits/2026-11-15-bar-parity-split-gap-routes.md).** (1) Letter level, kept as true: the n − p letter difference is $\\pm h/2$ per differing letter, and $h = q - q^{-1}$ is bar-odd. (2) Trace level: the Markov trace at $z_D = q^3/(q^2+1)$ intertwines bar with $q \\mapsto q^{-1}$, because $z(q) - z(q^{-1}) = h$ holds for $z_D$ (Lean `QOU.Mass.BarParitySplitGap.zD_bar_shift`, one letter; all words by Ocneanu uniqueness, checked exactly on both words). Exactly $f = h\\,g$ (Lean `ruledTrace_eq_h_mul_context`), so the readout $f$ is bar-odd iff the context trace $g$ is bar-even. For the ruled word `nuc11_interleaved` it is not: $g_{\\mathrm{odd}} = -h[2]_q(q^2+q^{-2})/8 \\neq 0$ (Lean `ruledContext_not_bar_even`, `ruledTrace_not_bar_odd`). The invariant cited is that inequality; the exclusion is for THIS element, not for every element. (3) Localisation (probe `qbeta_bar_parity_split_gap_probe.py` R5, exact subset interpolation, word unchanged): the quark tail contributes exactly 0, alone and in every cross term; $g_{\\mathrm{odd}}$ is the core term plus the gluon-pair term plus their cross term; the core's own trace is bar-even, and the context trace without the gluon pair is bar-even. So the obstruction needs the gluon pair. This is a diagnostic: no word was changed or chosen.",
    },
  ],
});
