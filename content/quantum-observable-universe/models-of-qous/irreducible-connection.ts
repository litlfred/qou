import { example } from "../../schema/builders";

export default example({
  interprets: "lem:categorical-irreducible",
  label: "ex:irreducible-connection",
  title: "Irreducibility of the connection",
  tags: ["irreducibility", "archimedean"],
  lean: { ref: "qou:QOU.irreducible_connection",
    validation: "leanok",
  },
  uses: ["lem:categorical-irreducible", "ex:c-quantum-observable-universe"],
});
