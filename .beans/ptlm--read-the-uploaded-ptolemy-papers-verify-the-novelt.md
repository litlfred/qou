---
# ptlm
title: 'Read the uploaded Ptolemy papers: verify the novelty assessment, and price the Ptolemy route past the Gröbner ceiling'
status: in-progress
type: task
priority: high
tags:
    - literature
    - hyperbolic-volume
    - gluing-equations
    - ptolemy
parent: m015
created_at: 2026-08-10T01:35:00Z
updated_at: 2026-08-10T01:35:00Z
---

Two primary sources were uploaded to the repo at
[`765457e`](https://github.com/litlfred/qou/commit/765457e64bf8b1e862decd2e91171c8a7df1e605):

- `library/arxiv-1207.6711v1/1207.6711v1.pdf` — Garoufalidis–Goerner–Zickert, *Gluing equations for
  PGL(n,ℂ)-representations of 3-manifolds*
- `library/arxiv-1507.03238v3/1507.03238v3.pdf` — *Triangulation independent Ptolemy varieties*

⚠ **They are on `main`, not on the Route 75 branch** — fetch before reading.

## Why this matters — two open questions Route 75 left on a search snippet

**1. The novelty assessment rests on a search result, not on the papers.** Route 75's
docstring and bean `m015` both state flatly that none of the mathematics is new, citing
these two papers plus Thurston, Neumann–Zagier, Neumann–Reid and `snap`. That assessment
is almost certainly right, but it was made from a search summary. **Read the sources and
either confirm it or correct it.** Getting this wrong in the conservative direction costs
nothing; getting it wrong in the other direction would be a false novelty claim in the
corpus.

Specifically, confirm the sentence Route 75's gate G7 leans on — that Gröbner
computations are *"usually impractical for the gluing equations even when the cusp
equations are added"* — is actually in 1207.6711 and says what G7 claims it says.

**2. The Ptolemy variety may be the way past the measured ceiling.** The same snippet
says Gröbner bases **are** feasible for *Ptolemy* varieties "even for many simplices",
while being impractical for gluing equations — and that a **monomial map** recovers the
shapes from Ptolemy coordinates. If that holds, it directly attacks what Route 75
measured:

| Route 75's ceiling | what Ptolemy might give |
|---|---|
| Gröbner derivation dies at 4 tetrahedra (gate G7) | Gröbner reportedly fine "for many simplices" |
| identification (LLL) fails for 11a1/11a2/12a1 (17–20 tets) | exact solutions with **no LLL at all**, hence no height/precision gate and no identification step |

That would make the whole pipeline float-free end to end, at every size — not just up to
3 tetrahedra. It would also retire gate G2's LLL-artifact trap by removing LLL.

## What to produce

1. A verdict on the novelty assessment: confirmed, or corrected in `m015` + the probe
   docstring.
2. A priced plan for the Ptolemy route, with the monomial map written down explicitly,
   and a decision on whether SnapPy's bundled `ptolemy` module can run **without** Sage
   or Magma in this environment — that is the practical blocker, since `find_field`
   already needs Sage (which is why Route 75 re-implements identification by hand).
3. If it runs: extend Route 75, or open a Route 76.

## Related

- `m015` — the gluing-data lane; Route 75's measured ceiling is recorded there.
- `glnl` — Lean-proving the equations; unaffected by which method produced the shapes.
