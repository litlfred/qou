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

**Ten SLq(2) / braid-matter documents held**, measured on `SLq(2)|preon` across both tiers:

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
[`sections/sec-001-energy-bound.md:203-216`](../../library/arxiv-0808.1533v1/sections/sec-001-energy-bound.md);
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

**The computable handle.** The same paragraph bounds `ac(L_k, L)` below by *"a smallest
genus among surfaces in `ℝ³ ∖ {L₁ ∪ … ∪ L̂_k ∪ … ∪ L_n}` with a single boundary component"*
— verified at line 217. That is a **real complement constraint** (settled in `qou-a9li` /
`qou-b5yi`), so `ac` is a positive quantity, not an infimum that collapses to zero.

**Why the derived carrier makes this easier than Borromean.** The earlier bound
`1 ≤ ac(L_k, L) ≤ 3.285` was obtained for L6a4 via `μ̄₁₂₃ = 1 ≠ 0`. On the derived carrier,
consecutive components have `lk = ±2 ≠ 0` (measured above), so `genus ≥ 1` follows directly
from linking rather than through a Milnor invariant.

**Note on `v1` vs `v3`.** `arxiv-0808.1533v1` carries **no `INDEX.md` row** and is marked
`duplicate_of`; `arxiv-0808.1533v3` (*On the third order helicity of magnetic fields on
invariant domains in S³*) is the indexed copy and the registered one
(`references.ts:9421`, `alternates: ["arxiv-0808.1533v1"]`). **This is correct behaviour,
not index staleness** — the arithmetic checks out: 576 directories − 552 rows = 24, against
23 `duplicate_of` directories, and the single unaccounted directory is `ant-v14-n7-s`,
unrelated to any of these routes. Cite the `v1` sections for eq. (43); its text is the one
that has been verified line-by-line.

**Twelve documents** match `asymptotic crossing|Freedman` across both tiers, including
[`procrsoclondona92`](../../library/procrsoclondona92/) — Moffatt & Ricca, *Helicity and
the Calugareanu invariant*, whose real text is **19 OCR pages against a 1-section stub**,
so a `sections/`-only grep does not find it.

## Route 3 — Milnor invariants / higher helicity

**Nine documents** match `Milnor invariant|triple linking|mu-bar|higher-order helicity|Massey product`:

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
