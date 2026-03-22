import { prose } from "../../schema/builders";

export default prose({
  label: "sec:brane-fluid",
  todos: [
    {
      id: "todo-viscosity-q-laplacian",
      summary: "Investigate viscosity gradient encoding via q-Laplacian",
      comment:
        "Investigate whether the viscosity gradient can be encoded by " +
        "the q-Laplacian Delta_q.",
      status: "open",
      priority: "medium",
      origin: "extracted",
      targetLabel: "sec:brane-fluid",
      createdAt: "2026-03-22T00:00:00Z",
    },
    {
      id: "todo-navier-stokes-q",
      summary: "Formulate Navier-Stokes analogue in q-deformed gauge-field setting",
      comment:
        "Formulate a Navier-Stokes analogue in the q-deformed gauge-field setting.",
      status: "open",
      priority: "high",
      origin: "extracted",
      targetLabel: "sec:brane-fluid",
      createdAt: "2026-03-22T00:00:00Z",
    },
  ],
});
