import { example } from "../../schema/builders";

export default example({
  label: "ex:chi-minus-six-derivation",
  title: "$\\chi(A) = -6$: complete derivation chain",
  interprets: "def:archimedean-condition",
  uses: [
    "def:archimedean-condition",
    "def:motivic-substrate",
    "prop:euler-char-stability",
    "rem:kummer-tower",
    "thm:motivic-perpetual-obstruction",
  ],
  tags: ["descartes", "chi", "derivation", "example", "motivic-galois"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**Step 5's parenthetical is factually wrong, and the correction is in a held source.** It reads *\"from the S_3 subset S_5 orbits on the 6 Weierstrass points of Bring's surface\"*. Bring's curve has **60** Weierstrass points, not 6, and `Aut(B) = S_5` acts on them **transitively** -- Braden & Disney-Hogg, Prop. 3.3, held at `library/s40879-023-00706-0/sections/sec-006-31-weierstrass-points.md`, quoting Edge. So there is no set of six for an `S_3` to act on, and the stabiliser is not an `S_3`: the same proof says each point is *\"preserved by the transposition (ij) only\"*, giving orbits of size 120/2 = 60. A 6 **does** occur one line further on -- `60 = 6 x 10`, six points fixed by each of the ten transpositions -- and Riemann-Hurwitz on that degree-2 quotient gives genus 1, hence `chi = 2*0 - 6 = -6`. That is one substitution from coherent: the carrier is an **involution**, not an `S_3`, and 6 is a **per-involution** count, not a total. **It is still a read-off from Bring's surface**, so it does not change this block's own verdict that the chain locates the value rather than deriving it. **Not enacted**: what Step 5 should say instead is a reading of the chain and is the author's call. The proposed one-line replacement is *\"...from the six Weierstrass points fixed by each transposition in S_5 (60 = 6 x 10), whose degree-2 quotient has genus 1\"*, adding `[braden-disney-hogg-2022]` to `cites`. Beans `qou-qhcr`, `qou-xz89` (which already flagged the 60-vs-6 mismatch, but for the wrong reason -- it cited the hyperelliptic bound `2g+2 = 10`, and Bring is not hyperelliptic).",
    },
  ],
});
