import { prose } from "../../schema/builders";

export default prose({
  label: "sec:varying-euler",
  meta: { position: "opening" },
  todos: [
    {
      id: "todo-varying-euler",
      summary: "Fill in varying Euler characteristic discussion",
      comment:
        "Discuss how varying the Euler characteristic leads to lower and higher " +
        "versions of the Bring surface. Include: relationship between Euler " +
        "characteristic and genus; classification of surfaces for chi = -2, -4, " +
        "-6, -8, ...; how the braid group changes with genus.",
      status: "open",
      priority: "medium",
      origin: "extracted",
      targetLabel: "sec:varying-euler",
      createdAt: "2026-03-22T00:00:00Z",
    },
  ],
});
