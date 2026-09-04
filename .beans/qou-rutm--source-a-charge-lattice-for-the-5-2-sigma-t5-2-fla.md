---
# qou-rutm
title: 'Source a charge lattice for the 5_2 sigma: T[5_2] flavour lattice from 3d-3d (D1-b arrow test)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T07:37:09Z
updated_at: 2026-09-04T07:37:47Z
---


## 2026-09-04 opened — three routes closed on the first pass; the gap is now named

Opened on owner instruction ("sourcing a 5₂ charge lattice is worth opening")
after `qou-q9ih` reduced the D1-b arrow question to one labelled hypothesis with
one test:

> **H:** the D1-b quiver has `V = 3` (the three σ) and 3 arrows (the three
> unordered pairs `{12,13,23}`), the two rays being the two orientations.
> **Test:** compute the Dirac pairing `⟨γᵢ,γⱼ⟩` on the 5₂ charge lattice; if it
> is not supported on exactly `{12,13,23}`, H is dead.

`computations/qbeta/d1b_52_charge_lattice_sourcing_probe.py` (6/6, exact
integers) went to source that lattice. **It does not find one**, by three
independent routes — and none of them is a failed numerical search.

**R1 — the paper that produced the datum defines no lattice.** Measured over the
sectioned text of GGM `arXiv:2012.00062v3`: `"charge lattice"` **0**,
`"Dirac pairing"` **0**, `"symplectic"` **2** — both in §7 and both naming
Neumann–Zagier. The σ are labels for asymptotic series; GGM equips them with no
lattice and no pairing. So **H's test has no referent in its own source.**

**R2 — Neumann–Zagier, the paper's own candidate, is Lagrangian exactly where it
would have to matter.** Antisymmetrizing the rect gluing datum,
`J = A·Bᵀ − B·Aᵀ`:

* the **edge block is exactly the zero matrix** — `A·Bᵀ` is symmetric, which *is*
  the NZ symplectic theorem;
* the **entire** nonzero content is the **rank-2 cusp block** `(μ,λ)` carrying
  `±2`, i.e. the 1-cusped relation `A_μ·B_λᵀ − A_λ·B_μᵀ = 2`.

Measured for **both** 4₁ (N=2) and 5₂ (N=3), so it is structural, not an
accident of tetrahedron count. eq (98) is **rank 3**; the NZ antisymmetric
content is **rank 2, always**. So NZ cannot carry an eq-(98)-shaped pairing at
any index set — **scope-(b)**, invariants cited being the NZ symmetry theorem
and the cusp relation. What antisymmetric content NZ *does* have lives on the
**boundary torus**, which is about the cusp, not about saddles.

**R3 — KRSS is the wrong symmetry class.** `arXiv:1707.02991v1` ("BPS states,
knots and quivers") is the one held source assigning a quiver to a knot, and its
quivers are **symmetric** by its own definition — *"the number of arrows from i
to j equals the number of arrows from j to i"*. eq (98) is **antisymmetric**, so
it is not a KRSS quiver matrix before any question of values.

> **Do not merge R3 with the standing refutation.** `qou-q9ih` says *"do NOT
> resurrect the refuted KRSS open-sector route (det(K)=5)"*. That is a
> refutation of a particular **open-sector** construction. R3 is a structural
> remark about the **symmetry class**, applies to the closed sector, and is
> recorded separately so neither is read as evidence for the other.

**What remains, named precisely.** A map

    {σ₁, σ₂, σ₃}  (saddles / asymptotic series, GGM)  ⟶  Γ

where `Γ` carries an antisymmetric integral pairing. It would come from the
**3d-3d correspondence** — the flavour/charge lattice of `T[5₂]` — which is
**not held in `library/`** and is not computable from anything in this repo.

**Consequence, and it is sharper than "blocked".** Until that map exists, **H is
UNSTATED, not merely unconfirmed**: the phrase "the Dirac pairing on the
charges" does not yet denote anything. The honest next step is acquiring a 3d-3d
source (a DGG-lineage paper giving `T[M]`'s flavour lattice for a census knot),
not another probe against what is already held.

## 2026-09-04 CORRECTION — I named one route and called it *the* route

The first pass ended: *"a lattice for the σ would have to come from the 3d-3d
correspondence … not held in `library/`, not computable from anything in this
repo"*, and concluded the next step was **acquiring a paper**. **Both halves
were too strong**, and the trigger was a sibling landing —
[`2026-09-03-colour-cubic-is-a-rank-three-spectral-curve.md`](docs/audits/2026-09-03-colour-cubic-is-a-rank-three-spectral-curve.md),
which merged to `main` while this branch was open.

**Route 2, never named.** For a spectral curve `Σ`, the charge lattice is
`H₁(Σ,ℤ)` with its **intersection form** — a canonical antisymmetric integral
pairing. That is the standard Seiberg–Witten / Hitchin construction and it does
**not** route through `T[5₂]`'s flavour lattice at all. Naming the 3d-3d route as
the only one was an assertion, not a measurement.

**And the repo is not empty of the machinery** (measured):

* **A-polynomial producers, 3** — `aj_figure_eight_operator_construct_verify.py`,
  `aj_trefoil_operator_construct_verify.py`, `borromean_apoly_renormalize.py`.
* **A rank-3 spectral curve worked in-corpus** — the colour cubic
  (`ColorSpectralCubicGeometry`, `bring_cubic_monodromy_probe`). **Wrong curve
  for 5₂, right method.**
* **Intersection-form machinery, 10 files** — including the literal
  `intersection form J = V − Vᵀ`, the Seifert-form antisymmetrization, live in
  the `nastokes_*` probes.

**🛑 My own control caught my own sub-claim.** C7's assertion originally required
**zero** intersection-form files and **FAILED at 10**. So the correction is
*stronger* than its own first draft: the repo has **both** halves of route 2, not
just one. Worth recording because it is the fourth time this session that a
check I wrote to test something else caught a claim I had smuggled past myself.

**What is genuinely absent, and it is narrow:** nothing computes 5₂'s
A-polynomial specifically, and the live intersection forms are on **Seifert
surfaces** rather than on a **spectral curve** — a different lattice, the same
construction.

**So the next step is in-repo work, not an ingest**: extend the existing
A-polynomial machinery to 5₂, then compute `H₁` and its intersection form. That
is a substantially better rung than "acquire a paper", and it is work I can do.

**NOT claimed:** that route 2 succeeds. Whether `H₁(Σ)` is the right lattice for
the σ is exactly as open as route 1 was. Only the *availability* claim is
corrected.
