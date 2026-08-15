import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's content *is* an ordering " +
        "claim: `q_viscosity_pos {q : ℝ} (hq : 1 < q) : 0 < (1 - q⁻¹) / 2`. " +
        "The proof runs `inv_pos`, `nlinarith`, `linarith` — it derives " +
        "`q⁻¹ < 1` from `1 < q` and concludes strict positivity of the " +
        "kinematic viscosity `ν_q`. Strip the ordering and nothing remains: " +
        "\"for `q > 1` the dissipation is genuine, and vanishes at `q = 1` " +
        "(Euler limit)\" is the whole statement. `ν_q` is moreover a physical " +
        "viscosity. Per the §7c table (\"Ordering `0 < q` → `ℝ`\") this is the " +
        "archimedean side of the wall by construction.",
    },
  ],
  label: "def:q-navier-stokes",
  title: "$q$-deformed Navier--Stokes equation",
  lean: {
    ref: "qou:QOU.FluidDynamics.QNavierStokes",
    validation: "not_checked",
  },
  uses: [
    // The quantum Euler equation this definition adds dissipation to; the
    // opening sentence introduces the block as exactly that extension.
    "rem:madelung-fluid",
  ],
  tags: ["navier-stokes", "q-deformation", "dissipation", "fluid-dynamics"],
});
