import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-lagrangian-dm-cubic",
  title:
    "Donagi--Markman cubic condition as an independent geometric origin for the binding kernel $C_1$",
  lean: {
    ref: "qou:QOU.Brings.CategoricalLagrangianDMCubic.QCubicEqBindingKernel",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-20",
      body:
        "**OPEN research route — scaffold only, keystone NOT closed.** This block states, honestly, the structural chain by which the Donagi--Markman cubic condition would give the binding kernel $C_1$ an *independent* geometric origin, **de-tautologizing** QDM-3. The QDM-3 identity `symbol D_q = recurrenceKernelLead κ` (`QOU.Machinery.QProlongation.symbol_eq_recurrence_kernel`) is an honest **tautological re-encoding** — $D_q$ is *defined from* the $C_1$ recurrence, so the symbol match holds by construction; it is NOT a geometric origin. The genuine open wall is the identity $c = C_1$ (`QCubicEqBindingKernel`, no instance). Deriving it (NOT fitting it) closes the route; it is not proved here.",
    },
    {
      kind: "caveat",
      date: "2026-07-20",
      body:
        "**4-form → 2-form correction (load-bearing).** The Bring cone is a real-4-dimensional manifold, so the tetraplectic 4-form degenerates to a mere volume form ($m=1$) and carries **no** Lagrangian-fibration data. The structure that actually supports a Donagi--Markman ACIHS / Lagrangian fibration is the hyperkähler **holomorphic-symplectic 2-form** $\\Omega_{\\mathbb{C}}$ (signalled by the 3-Sasakian link + the Reeb twist $[M_i,M_j]=2M_k$, proved sorry-free in `QOU.Tetraplectic.BringCone`). Do NOT claim the SW base is a Frobenius manifold (`braden-marshakov2006wdvv` caveat); the genuine fact used is 'cubic = 3-jet of the prepotential'.",
    },
    {
      kind: "note",
      date: "2026-07-20",
      body:
        "Lean scaffold `QOU.Brings.CategoricalLagrangianDMCubic` (generic `[CommRing R]`, §7c): two **primary** conjecture classes (`QDonagiMarkmanCubicCondition`, `BringHolomorphicSymplectic`, content-bearing, no instance), one **conditional theorem** proved sorry-free modulo them (`categorical_lagrangian_dm_cubic`, §3b-cond), and the **dependent target** class `QCubicEqBindingKernel` (the open $c = C_1$ identity, no instance). Verified `lean`-direct (exit 0). Scaffolds the route; does not close the keystone.",
    },
  ],
  uses: [
    "def:categorical-lagrangian",
    "conj:qdifference-kernel-prolongation-symbol",
  ],
  cites: [
    "donagi-markman1996cubics",
    "donagi1997swintegrable",
    "grassi-gu-marino2019qsw",
    "braden-marshakov2006wdvv",
  ],
  tags: [
    "tier:keystone",
    "bring-surface",
    "donagi-markman",
    "cubic-condition",
    "holomorphic-symplectic",
    "binding-kernel-c1",
    "de-tautologization",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
