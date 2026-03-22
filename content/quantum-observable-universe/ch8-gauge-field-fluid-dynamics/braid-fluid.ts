import { prose } from "../../schema/builders";

export default prose({
  label: "sec:braid-fluid",
  todos: [
    {
      id: "todo-braid-vortex",
      summary: "Connect braid-group operators to vortex braiding in fluid dynamics",
      comment:
        "Work out the connection between braid-group operators (Chapter 4) " +
        "and vortex braiding in the fluid dynamics.",
      status: "open",
      priority: "medium",
      origin: "extracted",
      targetLabel: "sec:braid-fluid",
      createdAt: "2026-03-22T00:00:00Z",
    },
  ],
});
