import { prose } from "../../schema/builders";

export default prose({
  label: "sec:millennium-bounds-via-surreals-intro",
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-06-08",
      body:
        "Re-scope: the Millennium-problem entries in this section are " +
        "**narrowing** statements — each reduces its problem to a *named " +
        "external residue* (Goncharov's motivic conjecture, Beilinson, the " +
        "Volume Conjecture, …), not an unconditional proof. The surreal " +
        "grading is the bookkeeping *language* for that narrowing; surreal " +
        "*necessity* was assessed negative (the mass / Gröbner–Shirshov tower " +
        "collapses at $E_1$ by Whitehead/semisimplicity, and the genuinely " +
        "perpetual volume obstruction $\\kappa_n \\neq 0$ (on Bring's surface " +
        "only for $n \\nmid 6$; re-scoped 2026-11-15, PR #7747) is " +
        "Mostow-convergent), so no statement here depends on surreals. " +
        "Consolidated narrowing map: " +
        "`docs/coordination/2026-06-08-transcendental-surreal-narrowing-ledger.md`.",
      see: "conj:gb-depth-period-correspondence",
    },
  ],
});
