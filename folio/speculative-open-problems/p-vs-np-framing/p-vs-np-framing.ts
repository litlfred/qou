import { chapter, section } from "../../schema/builders";

export default chapter({
  title: "P versus NP Framing",
  label: "chap:p-vs-np-framing",
  sections: [
    section({
      title: "Skein resolution horizons, counting hardness, and observation cost models",
      label: "sec:p-vs-np-framing",
      blocks: [
        "p-vs-np-framing-intro",
        "p-vs-np-boundary",
        "p-vs-np-boundary-table1-data",
        "p-vs-np-boundary-table2-data",
        "p-vs-np-boundary-interpretation",
        "p-vs-np-event-horizon",
        "p-vs-np-event-horizon-table1-data",
        "p-vs-np-event-horizon-table2-data",
        "qou-p-neq-np",
        "p-vs-np-conjecture",
        "p-vs-np-surreal-bound",
        "p-vs-np-open-problems",
      ],
    }),
  ],
});
