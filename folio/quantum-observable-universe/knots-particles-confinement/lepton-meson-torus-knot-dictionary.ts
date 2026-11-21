import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lepton-meson-torus-knot-dictionary",
  lean: { ref: "qou:QOU.ParticleInteractions.lepton_meson_crossing_match" },
  title:
    "Torus-knot dictionary: leptons at $H_2$ vs mesons at $H_3$",
  uses: ["def:categorical-meson"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Quark indices re-read as **lepton-partner generation labels** " +
        "(owner ruling 2026-11-21, option 1, on top of the 2026-11-20 " +
        "ruling that a quark is an unknot strand of $\\mathcal{B}_3$ and " +
        "$T(2,n)$ is its lepton partner). The $3, 5, 7$ attached to quarks " +
        "are the crossing counts of their partners, not crossings carried by " +
        "the quark strands; the sign of the quark's crossing letter is its own " +
        "orientation. The meson column is therefore a **sum of labels** " +
        "($\\pi = 3+3$, $K = 3+5$), not a crossing count of a braid word " +
        "made of the two quarks. Every Lean statement is unchanged " +
        "(`lepton_meson_crossing_match`, `meson_crossing_is_sum` are integer " +
        "arithmetic). Whether the Hecke reduction of the meson word " +
        "$\\mathfrak{M}_+$ (6 crossings) still matches the pion's label sum " +
        "by more than coincidence is no longer implied by the table.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-02",
      body:
        "The parenthetical **(odd primes)** in the opening line is now " +
        "**derived at the normal-form level**, no longer merely " +
        "asserted. Setup: `torus-embeddable-complete-proof` proves the " +
        "genus bound $g(T(2,n)) = (n-1)/2 \\le 4$, admitting " +
        "$n \\in \\{3,5,7,9\\}$ — four knots — while this table assigns " +
        "three generations, so the question reduces to the single lemma " +
        "**what excludes $T(2,9)$?** Derivation: the $\\sigma$-coefficient " +
        "$b_n$ of the Gröbner–Shirshov normal form of $T(2,n)$ (the " +
        "Morgan–Voyce continuant of `prop:lepton-continuant-recurrence`) " +
        "satisfies the Fibonacci-polynomial divisibility " +
        "$b_a \\mid b_n \\iff a \\mid n$. Among $\\{3,5,7,9\\}$, only " +
        "$9 = 3\\cdot3$ is composite, and $b_9 = b_3\\,(h^6+6h^4+9h^2+1)$ " +
        "— the precise form of *$\\sigma^9 = (\\sigma^3)^3$ is a harmonic " +
        "of generation 1*; the prime windings $3,5,7$ leave unit " +
        "remainders and are mutually non-divisible. So the generation " +
        "windings are exactly the odd windings whose continuant " +
        "coefficient does not factor through a smaller one — the odd " +
        "primes. Sorry-free Lean twin " +
        "`QOU/Archimedean/lepton_continuant_generation_exclusion.lean` " +
        "(`t29_harmonic_of_first_generation`, `not_b3_dvd_b5/b7`) + " +
        "derivation witness " +
        "`generation-t29-continuant-divisibility.witness.json` (bean " +
        "qou-x4qm). **Scope-(a), not scope-(b):** this derives the " +
        "harmonic/factorisation distinction on the normal-form " +
        "coefficient; it does **not** prove $T(2,9)$ is unphysical " +
        "($T(2,9)$ is a genuine prime knot of genus 4). The remaining " +
        "bridge — normal-form-independence $\\Rightarrow$ physical " +
        "generation, plus the still-open $\\mathrm{net}\\to$ mass map " +
        "(the sibling probe `generation-count-t29-truncation` records " +
        "that validation as FAILED, unpatched) — stays open.",
    },
    {
      kind: "status",
      date: "2026-08-01",
      body:
        "Quark-flavour column realigned to match the charm/bottom " +
        "assignment in `knot-particle-dictionary-table4-data` " +
        "($\\mathfrak{c} \\leftarrow T_{2,5}$ at generation 2, " +
        "$\\mathfrak{b} \\leftarrow T_{2,7}^{\\sigma}$ at generation 3). " +
        "The prior text listed $s$ at **both** generation 2 and " +
        "generation 3 (as *heavy-strange*) and omitted $c$, $b$, $t$ " +
        "entirely — stale relative to the realignment. The meson column " +
        "is left unchanged and is **not** asserted to be consistent " +
        "with the corrected quark column: $\\phi = s\\bar{s}$ carries " +
        "generation-2 flavour content while sitting in the " +
        "generation-3 row, which is a separate open question.",
    },
  ],
  cites: [
    "jones1987",
    "kashaev1997",
  ],
  tags: [
    "lepton",
    "meson",
    "torus-knot",
    "hecke-algebra",
    "dictionary",
  ],
});
