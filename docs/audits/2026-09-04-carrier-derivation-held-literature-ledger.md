# Held literature for the three carrier-derivation routes — measured across both library tiers

**Date:** 2026-09-04 · **Bean:** `qou-768r` (taken over; see §Takeover) · **Arc:** carrier derivation
**Tier:** ledger — no new mathematics; a measured answer to *"what do we already hold?"*

Owner selected all three carrier-derivation routes and asked for links to the literature.
This is the measured answer. Every count below was produced this session by grepping
`library/*/sections/` **and** `library/*/ocr/`; nothing is quoted from the earlier survey
in `qou-768r`, which searched `sections/` only.

## The framing correction this ledger rests on

The phrase *"the carrier assignment is a fit"* has been used across this arc to mean two
different things, and only one of them is true.

- **The census lookup is a fit.** `jsj_verification.py` scans `snappy.LinkExteriors`
  keeping volumes near `B_AME/(ρ·m_e)`, producing `²H ↔ 6₂`, `³H ↔ 8₁₁`,
  `³He ↔ L6a4`. Admitted in production source and measured 797-fold degenerate in
  [`2026-08-25-knot-id-is-an-admitted-fit.md`](2026-08-25-knot-id-is-an-admitted-fit.md).
  Retired by owner ruling 2026-08-29 (Option A).
- **The carrier itself is derived.** It is the closure of the canonical atom braid word —
  a connected sum of `(2,k)` torus links `#_g T(2, e_g)`, verified against SnapPy
  `deconnect_sum` on **32/32** branches of the ²H word with zero mismatches
  ([`2026-08-25-atom-word-closures-are-not-hyperbolic.md`](2026-08-25-atom-word-closures-are-not-hyperbolic.md)).

Re-measured this session by re-running
[`computations/probes/atom_closure_milnor_indeterminacy_probe.py`](../../computations/probes/atom_closure_milnor_indeterminacy_probe.py)
(**70/70 checks pass**) rather than citing the bean:

| quantity | value | branch-dependence |
|---|---|---|
| components `μ` | **A + 1** exactly | **independent** — a superposition letter and its `σ` branch induce the same permutation |
| linking graph | **the path `P_μ`** (`path? True` on ²H, ³H, ³He, ⁴He, ⁶Li, ⁸Be, ¹²C) | independent |
| nonzero linking pairs | `μ − 1 = A`, the consecutive pairs `(i, i+1)` | independent |
| `Σ|lk|` | **2A** in the all-`σ⁻¹` branch | **dependent** (`−1`/`−2` mix in the all-`σ` branch) |
| `Δ = gcd(lk)` set | `[2]` for A ≤ 3; `[0, 2]` from A = 4 | dependent through `lk` |

So the open question is not *which link* but *which invariant of that link* carries binding.

## Route 1 — SLq(2) `(N, w, r) → irrep`

**Primary, held:** [`library/arxiv-0806.3105v3`](../../library/arxiv-0806.3105v3/) —
Finkelstein, *Knots and preons*. 5 sections, no OCR tier.
The dictionary sends a quantum knot to `D^{N/2}_{w/2,(r+1)/2}` with `(N, w, r)` =
(crossings, writhe, rotation) — verified in the held text at
[`sec-001-the-knot-representation.md:245`](../../library/arxiv-0806.3105v3/sections/sec-001-the-knot-representation.md)
(*"knot (N, w, r) and, like the Jones (Laurent) polynomial, label the knot"*) and
`sec-000-introduction.md:26`. **No volume, no census, nothing fitted.**

Registered as `finkelstein2008` (`content/schema/references.ts:10757`) and **still cited by
no content block** — re-verified this session, unchanged from the 2026-08-31 survey.

**🛑 CORRECTED — this said "Ten SLq(2) / braid-matter documents held" (pattern `SLq(2)|preon`).
Only **2** contain `SLq(2)` at all, and the other 8 are the `preon` milieu; two of those 8 are
`duplicate_of` copies, so it is **8 distinct works**, not 10 documents. See §Links below. The
list that follows is retained as the raw hit set:**

| doc | note |
|---|---|
| [`arxiv-0806.3105v3`](../../library/arxiv-0806.3105v3/) | Finkelstein — **the dictionary** |
| [`arxiv-hep-ph-0503213v2`](../../library/arxiv-hep-ph-0503213v2/) | Bilson-Thompson, *A topological model of composite preons* — the sibling construction the corpus **already adopts at the lepton level** ([`breit-wheeler-vertex-literature.md`](../../content/quantum-observable-universe/mass-theory/breit-wheeler-vertex-literature.md)) |
| [`arxiv-1910.09966v1`](../../library/arxiv-1910.09966v1/) | *Braids, 3-manifolds, elementary particles* |
| `0603022v2`, `arxiv-1901.01312v1`, `arxiv-2106.01332v4`, `arxiv-2306.13098v2`, `arxiv-2507.13873v1`, `s10052-023-11923-y-a`, `symmetry-11-01298` | the remaining seven |

**What the framework already settled, and it is a hard constraint.** `r = 3A` is the strand
count (no fetch needed: for a coherently-oriented closed braid on `n` strands the rotation
number is `n`, and Finkelstein's own trefoil `r = ±2` confirms it). The label's integrality
condition `j − m' = (N − r − 1)/2 ∈ ℤ` reduces through Seifert on a closed braid to **`μ`
odd**, i.e. **A even** — `QOU/Mass/SLq2LabelParity.lean`, sorry-free. So the dictionary as
stated admits ²H, ⁴He, ⁶Li, ⁸Be, ¹²C, ¹⁶O and gives **no label at all** to ³H, ³He, ⁵Li,
⁷Be, ⁷Li on **every** branch — and the excluded half contains the A = 3 mirror pair this
arc's convention systematic lives on.

**Therefore the open question is a link generalisation (`μ > 1`), not an extension in `N`** —
the parity condition *is* the knot condition. Nothing held answers that; this is the one
route with a genuine acquisition gap.

## Route 2 — Freedman–He asymptotic crossing number

**Primary, held:** [`library/arxiv-0808.1533v1`](../../library/arxiv-0808.1533v1/) —
Komendarczyk. The link bound is stated at
[`sections/sec-001-energy-bound.md:203-216`](../../library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md);
verified verbatim this session at line 211 (`ac(Lk, L)|Flux(Xk)|`).

```
E_{3/2}(X) ≥ (π/16)^{1/4} · ( Σ_{k=1}^{n} ac(L_k, L)|Flux(X_k)| ) · min_{1≤k≤n} |Flux(X_k)|
```

**Two readings that must not drift**, both re-verified against the source rather than
carried from a bean:

1. The index is `ac(L_k, L)` — **one component against the whole link**, summed over the
   `n` **components**, not the `n(n−1)/2` pairs. No `ac(L_i, L_j)` occurs anywhere.
2. The constant is `(π/16)^{1/4}` — **pure, with no volume factor**. The `Vol^{-1/3}` that
   `qou-0hdx` called "the Freedman–He template" is Khesin Thm 3.6, the **single knotted
   torus** bound, misapplied. That is why `qou-0hdx` is scrapped.

**🛑 The "computable handle" paragraph that stood here was WRONG, in the direction that
mattered, and is corrected below the rule. Do not restore it.** It read:

> *"The same paragraph bounds `ac(L_k, L)` below by 'a smallest genus among surfaces in
> `ℝ³ ∖ {L₁ ∪ … ∪ L̂_k ∪ … ∪ L_n}` with a single boundary component' — verified at line 217.
> That is a **real complement constraint**, so `ac` is a positive quantity, not an infimum
> that collapses to zero. **Why the derived carrier makes this easier than Borromean.** The
> earlier bound `1 ≤ ac(L_k, L) ≤ 3.285` was obtained for L6a4 via `μ̄₁₂₃ = 1 ≠ 0`. On the
> derived carrier, consecutive components have `lk = ±2 ≠ 0`, so `genus ≥ 1` follows
> directly from linking rather than through a Milnor invariant."*

---

**What the source actually says**, read this session at
[`sec-001-energy-bound.md:216-217`](../../library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md):

> *"the asymptotic crossing numbers `ac(Lk, L)` **for borromean links** can be estimated
> below by a smallest genus among surfaces in `ℝ³ ∖ {L₁ ∪ … ∪ L̂_k ∪ … ∪ L_n}` with a single
> boundary component"*

**The qualifier is load-bearing, and the corpus drops it.** `qou-a9li` and `qou-b5yi`, both
`completed` 2026-09-02, quote the genus clause without *"for borromean links"*; the
paragraph above took its wording from them rather than from the source, and then drew the
**opposite** conclusion from the one the qualifier supports.

**Why it must be there.** A compact oriented surface `S ⊆ ℝ³ ∖ L_j` with `∂S = L_k` forces
`lk(L_k, L_j) = 0`, since `[L_k] = [∂S] = 0` in `H₁(ℝ³ ∖ L_j) ≅ ℤ` and that class *is* the
linking number. So where some `lk ≠ 0` the surfaces being minimised over **do not exist**:
off the Brunnian class the estimate is **ill-posed** — an infimum over ∅ — rather than
merely weaker. Nonzero linking does not make the handle easier; it removes it.

**Measured on the derived carrier** —
[`fh_genus_handle_requires_brunnian_probe.py`](../../computations/probes/fh_genus_handle_requires_brunnian_probe.py),
4/4, both crossing-resolution branches: **0 of 30** components have all their pairwise
linking numbers vanishing. Not one, on any isotope, in either branch.

**The inversion this produces.** The genus handle applies exactly on the Brunnian class,
which in this arc means **L6a4** — the A = 3 *census* assignment, i.e. the admitted
AME-driven fit that owner ruling 2026-08-29 retired. The only carrier route 2's computable
handle works on is the one that was retired as a fit; on the derived carrier it does not
apply at all.

Formalised in
[`QOU/Mass/FreedmanHeGenusHandleNeedsVanishingLinking.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/FreedmanHeGenusHandleNeedsVanishingLinking.lean)
(lean-direct exit 0, sorry-free; two declarations depend on no axioms at all). The
homological step is **deliberately not** formalised — Seifert surfaces and `H₁` of a link
complement are not cheaply available in this Mathlib, and asserting them as a class would be
the axiomatisation-is-not-a-proof pattern.

**Scope — (b) on the HANDLE**, invariant cited (complement homology). Eq. (43) is untouched
and remains a true lower bound, and `ac(L_k, L)` itself is untouched: nothing here says it
is small or zero, only that this particular route to a number for it is unavailable here. A
different lower bound on `ac`, not routed through a complement genus, is not excluded and is
not examined.

**Note on `v1` vs `v3`.** `arxiv-0808.1533v1` carries **no `INDEX.md` row** and is marked
`duplicate_of`; `arxiv-0808.1533v3` (*On the third order helicity of magnetic fields on
invariant domains in S³*) is the indexed copy and the registered one
(`references.ts:9421`, `alternates: ["arxiv-0808.1533v1"]`). **This is correct behaviour,
not index staleness** — the arithmetic checks out: 576 directories − 552 rows = 24, against
23 `duplicate_of` directories, and the single unaccounted directory is `ant-v14-n7-s`,
unrelated to any of these routes. Cite the `v1` sections for eq. (43); its text is the one
that has been verified line-by-line.

**🛑 CORRECTED — "twelve documents" is a hit count on `asymptotic crossing|Freedman`, and
"Freedman" matches any bibliography containing a person of that name. Only **4** contain
`asymptotic crossing`, and two of those are one work: **3 works**. See §Links below. Raw hit
set retained:** twelve documents match, including
[`procrsoclondona92`](../../library/procrsoclondona92/) — Moffatt & Ricca, *Helicity and
the Calugareanu invariant*, whose real text is **19 OCR pages against a 1-section stub**,
so a `sections/`-only grep does not find it.

## Route 3 — Milnor invariants / higher helicity

**🛑 CORRECTED — "nine documents" is a hit count on a five-way disjunction. Only **6** contain
`Milnor invariant` or `triple linking`, and one of those is a `duplicate_of` copy: **5 works**
in the core tier, plus 2 adjacent. See §Links below. Raw hit set retained:**

| doc | title |
|---|---|
| [`deturck-…-2008-triple-lin`](../../library/deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin/) | *Triple linking numbers, ambiguous Hopf invariants and integral formulas* — registered (`references.ts:9363`) |
| [`arxiv-1101.3374v1`](../../library/arxiv-1101.3374v1/) | *Pontryagin invariants and integral formulas for Milnor's triple linking number* |
| [`0110001v3`](../../library/0110001v3/) | *A geometric interpretation of Milnor's triple linking numbers* |
| [`arxiv-physics-0203048v1`](../../library/arxiv-physics-0203048v1/) | *Towards a third-order topological invariant for magnetic fields* |
| [`helicity03mmj`](../../library/helicity03mmj/) | *Geometry of higher helicities* |
| [`arxiv-0808.1533v1`](../../library/arxiv-0808.1533v1/) / [`v3`](../../library/arxiv-0808.1533v3/) | Komendarczyk (also route 2) |
| [`arxiv-0901.1612v1`](../../library/arxiv-0901.1612v1/), [`arxiv-math-0605314v1`](../../library/arxiv-math-0605314v1/) | remaining two |

**What is held is the geometry, not the computation.** Every one of these gives an
*integral formula* or a *geometric interpretation* for `μ̄₁₂₃`. **None supplies the Magnus
expansion of a longitude in the free group**, which is what computing `μ̄` on a concrete
link presentation needs. The repo's ~20 `magnus_*` probes are Burau/Hecke Magnus — a
different object. So route 3's remaining work is **code, not acquisition**.

**Where it is available.** `μ̄(ijk)` is a genuine integer only where `Δ = 0`, which on a
path requires mutually non-adjacent components, hence `μ ≥ 5`, hence **A ≥ 4** — confirmed
in this session's probe run (`Δ` set `[2]` at A ≤ 3, `[0, 2]` from ⁴He). The deuteron and
the A = 3 mirror pair are outside its reach entirely.

**The count is the constraint.** All non-adjacent triples number `C(μ−2,3) = C(A−1,3) ~ A³`,
which C4 excludes arithmetically and `QOU.Mass.CoordinationSaturation` refutes structurally.
The minimal-span family `{i, i+2, i+4}` has **A − 3** members with per-component multiplicity
capped at **3** independent of A — linear, bounded degree, and named by a topological
minimality criterion with no reference to AME.

## Not held

- **Freedman–He 1991 itself.** Absent from `library/`. Komendarczyk's statement of the bound
  is held and unambiguous on both points above, so this gap does not touch either correction.
- **The nuclear Skyrme model.** The two Skyrme papers held are Skyrme–**Faddeev** (33× "Hopf
  charge", **0×** "baryon number"); `Houghton`: 0 files. Owner deferred this route.
- **A multi-component SLq(2) labelling.** The route-1 acquisition gap.

## Takeover of `qou-768r`

`qou-768r` was `in-progress` with `updated_at` 2026-08-31T04:11:30Z — four days, well past
the 3 h staleness threshold, and its backing work is on `main`. Taken over per the standing
stalled-claim policy; the bean is re-claimed with a note rather than duplicated.

## Scope

**Ledger only.** No invariant is computed here, no magnitude is claimed, and nothing is
wired. The one substantive claim is the framing correction at the top — that the carrier is
derived while the census lookup was the fit — and it rests on two merged audits plus this
session's own 70/70 re-run, not on a bean.

## Corrections made to this document after it was first committed

Recorded rather than silently edited, because both errors were mine and both are
instructive.

1. **The route-2 "computable handle" paragraph was backwards** (corrected above, with the
   superseded text quoted so a reader who saw the first version can tell what changed). I
   took the genus clause from two beans that had dropped its *"for borromean links"*
   qualifier, in a session whose own PR body warns against treating a bean as a primary
   source. Reading the sentence itself took one command.

2. **The verification claim on the sibling PR #6515 was too weak, and this document
   inherited the method.** That PR body said *"the new files appear nowhere in the gate
   log"*, established by grepping the log for the filename. The q0-anchor refill ratchet
   reports a **count, not filenames**, and the only line naming the file was a
   `skipped: (new file — no HEAD copy to compare)` notice — which reads like a clean bill
   and is not one. Measured properly, by A/B-ing `precision-gates.sh --changed` with the
   files removed:

   | tree | `NEW (not in baseline)` |
   |---|--:|
   | without the new files | 40 |
   | with them, no `q0Anchor` declared | **41** |
   | with both probes declaring `independent` | **39** |

   So the files *were* implicated, and the fix at the producer drains one pre-existing
   entry as well. Both probes genuinely read no `q₀` — this one works in integer linking
   numbers and a text search, `r5full` entirely in `ℚ[q]` — so `independent` with a reason
   is the honest declaration; a stamped `q0Value` would be flagged `Q0_FLIP`. No baseline
   was touched.

   **The generalisable rule:** to check whether your files affect a ratchet, remove them and
   diff the counts. Grepping a gate log for your own filename cannot detect a gate that
   counts.

---

# Links — and a correction to this document's own counts

Added 2026-09-04 on owner request ("LINKS for lit pls"). Building the link list
exposed **two errors in the counts above**, both mine, both from the same cause:
I reported **keyword hits on files** and called them **held sources on a topic**.

## Correction 1 — files vs works

AGENTS.md §corpus-grep path 5 says *"One line per **work**, not per file… Do not read
two hits on one work as two sources."* I did exactly that. Four of the hits are
`duplicate_of` copies of another hit, verified from their section front-matter:

| copy | is a duplicate of |
|---|---|
| `arxiv-0808.1533v1` | `arxiv-0808.1533v3` |
| `arxiv-0901.1612v1` | `deturck-…-2008-triple-lin` |
| `symmetry-11-01298` | `arxiv-1910.09966v1` |
| `s10052-023-11923-y-a` | `arxiv-2306.13098v2` |

## Correction 2 — the grep patterns were far too wide, and route 2 is the worst

Route 2's pattern was `asymptotic crossing|Freedman`. **"Freedman" matches any
bibliography containing a person of that name.** Splitting the disjunction:

| route | as reported above | actually contains the core term | of those, distinct works |
|---|--:|--:|--:|
| 1 — SLq(2) | 10 | **2** contain `SLq(2)` | **2** |
| 2 — Freedman–He | 12 | **4** contain `asymptotic crossing` | **3** |
| 3 — Milnor | 9 | **6** contain `Milnor invariant`/`triple linking` | **5** |

So route 2's "12 held documents" is **three works**, and eight of the twelve were
bibliographies mentioning someone called Freedman. **Do not quote 10 / 12 / 9.**

This does not change any route's verdict — every result above rests on sources in
the *core* tier, and the route-2 correction concerns how much surrounding
literature exists, not what the primary source says. It changes what "held" is
worth as a claim.

## Route 1 — SLq(2) `(N, w, r) → irrep`

**Core (2 works — the only held documents that mention `SLq(2)` at all):**

| work | link | held copy |
|---|---|---|
| Finkelstein, *Knots and preons* (2008) — **the dictionary**, `D^{N/2}_{w/2,(r+1)/2}` | [arXiv:0806.3105](https://arxiv.org/abs/0806.3105) | [`library/arxiv-0806.3105v3/`](../../library/arxiv-0806.3105v3/) · [`sec-001`](../../library/arxiv-0806.3105v3/sections/sec-001-the-knot-representation.md) |
| Belaey, *Probing the singularity at the holographic screen via q-holography* (2025) | [arXiv:2507.13873](https://arxiv.org/abs/2507.13873) | [`library/arxiv-2507.13873v1/`](../../library/arxiv-2507.13873v1/) |

**Braided-matter milieu (6 works — `preon` but no `SLq(2)`):** Bilson-Thompson,
*A topological model of composite preons* — [arXiv:hep-ph/0503213](https://arxiv.org/abs/hep-ph/0503213)
(the construction the corpus already adopts at the lepton level);
Bilson-Thompson–Markopoulou–Smolin, *Quantum gravity and the standard model* —
[doi:10.1088/0264-9381/24/16/002](https://doi.org/10.1088/0264-9381/24/16/002);
Gresnigt, *Braided fermions from Hurwitz algebras* — [arXiv:1901.01312](https://arxiv.org/abs/1901.01312);
Gresnigt, *Three generations of colored fermions with S₃ family symmetry* —
[arXiv:2306.13098](https://arxiv.org/abs/2306.13098) / [doi:10.1140/epjc/s10052-023-11923-y](https://doi.org/10.1140/epjc/s10052-023-11923-y);
*Braids, 3-manifolds, elementary particles* — [arXiv:1910.09966](https://arxiv.org/abs/1910.09966) /
[doi:10.3390/sym11101298](https://doi.org/10.3390/sym11101298);
*Braided matter interactions in quantum gravity via 1-handle attachment* —
[arXiv:2106.01332](https://arxiv.org/abs/2106.01332) (**not registered** in `references.ts`).

## Route 2 — Freedman–He asymptotic crossing number

**Core (3 works — every held document containing `asymptotic crossing`):**

| work | link | held copy |
|---|---|---|
| Komendarczyk, *On the third order helicity of magnetic fields on invariant domains in S³* — **eq. (43), the link bound** | [arXiv:0808.1533](https://arxiv.org/abs/0808.1533) | [`v1/sec-001-energy-bound.md`](../../library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md) (line 211; the Borromean qualifier at 216) · [`v3`](../../library/arxiv-0808.1533v3/) is the indexed copy |
| Khesin, *Geometry of higher helicities*, Moscow Math. J. **3** (2003) 989–1011 | **no DOI/URL registered** | [`library/helicity03mmj/`](../../library/helicity03mmj/) |
| Moffatt & Ricca, *Helicity and the Calugareanu invariant* (1992) | **no DOI/URL registered** | [`library/procrsoclondona92/`](../../library/procrsoclondona92/) — **96 % of its text is in `ocr/`**, 19 pages against a 1-section stub |

Freedman–He (1991) itself is **not held**. It does not touch either eq.-43
correction, since Komendarczyk's statement of the bound is held and unambiguous.

## Route 3 — Milnor invariants / higher helicity

**Core (5 works — every held document containing `Milnor invariant` or `triple linking`):**

| work | link | held copy |
|---|---|---|
| DeTurck–Gluck–Komendarczyk–Melvin–Shonkwiler–Vela-Vick, *Triple linking numbers, ambiguous Hopf invariants and integral formulas* | [arXiv:0901.1612](https://arxiv.org/abs/0901.1612) | [`deturck-…-triple-lin/`](../../library/deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin/) |
| — same group, *Pontryagin invariants and integral formulas for Milnor's triple linking number* | [arXiv:1101.3374](https://arxiv.org/abs/1101.3374) | [`library/arxiv-1101.3374v1/`](../../library/arxiv-1101.3374v1/) |
| Mellor & Melvin, *A geometric interpretation of Milnor's triple linking numbers*, Alg. Geom. Topol. **3** (2003) 557–568 | **no DOI/URL registered** | [`library/0110001v3/`](../../library/0110001v3/) |
| Komendarczyk (as route 2) | [arXiv:0808.1533](https://arxiv.org/abs/0808.1533) | — |
| Khesin (as route 2) | **no DOI/URL registered** | — |

**Adjacent (2 works — matched only on `Massey product` / `higher-order helicity`):**
Hornig & Mayer, *Towards a third-order topological invariant for magnetic fields* —
[arXiv:physics/0203048](https://arxiv.org/abs/physics/0203048);
*A unified Witten–Reshetikhin–Turaev invariant for integral homology spheres* —
[arXiv:math/0605314](https://arxiv.org/abs/math/0605314).

Also relevant and found only via the `ocr/` tier: Evans & Berger,
*A Hierarchy of Linking Integrals* — **no DOI/URL registered**,
[`library/1992evansberger/`](../../library/1992evansberger/).

**None of the five core route-3 works supplies the Magnus expansion of a longitude
in the free group** — they give integral formulas and geometric interpretations. That
was route 3's gap, and it is now moot: the min-span triples vanish by their own
defining condition.

## Four held sources have no resolvable external link

`khesin2003`, `moffatt-ricca-helicity`, `mellor-melvin2003` and `evans-berger1992`
carry **neither `DOI` nor `URL`** in `references.ts`, and no arXiv or DOI stamp
appears anywhere in their held text (checked across both the `sections/` and `ocr/`
tiers). Two of them — Khesin and Moffatt–Ricca — are **core route-2 sources**. Their
citations are complete enough to identify the work (journal, volume, pages, year for
three of the four) but a reader cannot click through, and this ledger will not invent
an identifier it did not measure. Worth a bibliography pass; not done here.
