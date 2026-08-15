# Gauge-gap synthesis: the proved q-lift kernel and the GGM/Stokes carrier are distinct q-difference modules — four independent routes converge

**Date:** 2026-07-20
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20` (PR #4139)
**Beans:** `qou-znbg` (synthesis), consolidating `qou-jwbq` (Door-i), `qou-gh6m` (Door-ii)
**Status:** AUDIT — synthesis of four completed adversarial routes. The core
result (C1 ≢ GGM as q-difference modules) is a **scope-(b) structural
distinction with the invariant named** (Newton-polygon slopes, RSZ Thm
2.2.1/2.2.4). No new open item is declared; the prolongation-symbol
identification remains the standing conjecture, now sharply re-scoped.

## 0. The question

The keystone `conj:qdifference-kernel-prolongation-symbol` asks that the
binding q-difference kernel be identified with the Seiberg–Witten
prolongation symbol / GGM Stokes datum. After the confluent-limit narrowing
([`…confluent-narrowing.md`](2026-07-20-qdifference-kernel-confluent-narrowing.md))
proved the raw-OGF form impossible and the q-lift was proved on the
q-factorial carrier (Lean `QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists`),
the concrete carrier is

- **C1** (proved q-lift): `[m+2]_q · b_{m+2} = b_{m+1} + b_m`
- **C2** (GGM eq-49 / Stokes carrier): `y_{m+1} − (2 − q^m) y_m + y_{m−1} = 0`

Both are order-2 q-difference operators with the same classical (q→1)
shadow. **The gauge gap: are they the same module?** Four routes attacked
this independently.

## 1. The four routes — all convergent

| Route | Method (independent) | Result | File |
|---|---|---|---|
| **A** | RSZ Newton polygon (from library/arxiv-0903.0853v3/0903.0853v3.pdf, Thm 2.2.1/2.2.4) | slopes at ∞: **C1 {½,½}** vs **C2 {−1,+1}** — disjoint; fuchsian exponents at 0 and det-classes also differ | [`routeA`](2026-07-20-qlift-routeA-rsz-invariants.md) |
| **B** | numeric 2×2 connection matrix, growth-class fit | `‖A_m‖ ~ q^{m²/4}` (theta) at q>1; exponent **¼ = C1's −¼ ⊕ C2's +½**, matching A exactly | [`routeB`](../../computations/probes/qlift_routeB_connection_matrix_probe.py) |
| **C** | homogenize 4₁ colored-Jones to order-3 `L3`, right-factor test | **neither** C1 nor C2 embeds ungauged; the order-2 right factor of `L3` is the AJ homogeneous part `L_hom`, not either candidate | [`routeC`](../../computations/probes/qlift_routeC_homogenized_factor_probe.py) |
| **D** | formal q-Borel/q-Laplace (all 4 RSZ conventions), diagonal invariant | every formal weight is diagonal; complete invariant **`I^{C1}_m = −[m]_q` ≠ `I^{C2}_m = 1/((2−q^m)(2−q^{m−1}))`** | [`routeD`](2026-07-20-qlift-routeD-qborel-transform.md) |

**Consistency of the four.** A gives the classifying invariant (slopes); B
independently *measures* the slope gap as the theta-exponent of the
connection matrix (¼ is exactly the arithmetic of A's polygon); D
re-derives the diagonal-gauge exclusion from the complete diagonal invariant
and shows no *formal* Borel weight rescues it; C places both candidates
*outside* the actual colored-Jones module. No route dissents. This is a
textbook multi-modal convergence: four blind angles, one conclusion.

## 2. The result (scope-(b), invariant named)

**C1 and C2 are inequivalent as q-difference modules over `K(x)` (x = q^m),
under every meromorphic gauge — diagonal, GL₂, or Möbius — and under every
*formal* q-Borel/q-Laplace transform.** The excluding invariant is the
Newton-polygon slope datum at ∞ (Ramis–Sauloy–Zhang local classification,
Thm 2.2.1 + 2.2.4): `{½,½} ≠ {−1,+1}`. Slopes are a complete invariant of
the graded module and are preserved by all of the above transform classes;
therefore no such transform maps one to the other. This is not "a bad
numerical fit" — it is a proved obstruction with a cited theorem.

## 3. Door-ii — the reframe (owner-flagged "serious weight"): the q-lift
kernel is the binding series' own resurgent object, not the colored-Jones
module

The half-integer slope `½` is not incidental. It is **exactly the proved
Gevrey-1/2 signature of the binding series** (`QOU.Mass.BindingGevreyHalf`:
`n! ≤ 4ⁿ I(n)² ≤ 8ⁿ n!`; the involution EGF `e^{x+x²/2}` is entire, its
level-1 Borel transform trivial, the content living at level ½). Route A's
slope `½` and Route B's `q^{m²/4}` theta-growth are the *same* ½ resurfacing
on the q-side. Route C then shows the decisive structural fact: the q-lift
kernel does **not** sit inside the 4₁ colored-Jones q-holonomic module (its
order-2 factor is the AJ part `L_hom` = the GGM side). 

Read together, these say: **C1 is a genuinely different resurgent object
from the colored-Jones/Stokes carrier — it is the binding series' *own*
half-slope module.** Two coherent readings survive, and the corpus should
hold both without prematurely collapsing them:

- **(R1) C1 *is* the prolongation-symbol carrier**, and the GGM/Stokes datum
  is a *different* face of the SW connection (the integral-slope, colored-
  Jones face). The conjecture's "identify with GGM" clause would then be the
  part that is *wrong*, not merely unproved — the prolongation symbol is the
  Gevrey-½ binding module C1, and the two faces meet only under an analytic
  (transcendental) summation, not an algebraic gauge (Door-i).
- **(R2) C1 and GGM are two legs of one order-≥3 object** (the true
  colored-Jones module `L3`), neither being the whole; the prolongation
  symbol is a factor of `L3`, and C1 is a *shadow* of it, not it. Route C's
  "neither embeds ungauged" is evidence for this: both are approximations to
  `L_hom`, exact only after the right (non-diagonal) intertwiner.

Distinguishing R1 from R2 is exactly Door-i's job (§4). Neither is asserted
here; both are recorded so the next agent does not over-collapse to one.

## 4. Door-i RESOLVED — (c) OBSTRUCTED: no q-difference-module transform bridges them

Door-i is closed ([`doorI audit`](2026-07-20-qlift-doorI-analytic-summation.md),
bean `qou-jwbq`), and the verdict is **(c) obstruction — even analytic
summation and ramified pullback fail.** The decisive invariant is
**isoclinicity**:

- RSZ ch. 5 analytic q-Borel–Laplace summation stays *inside one formal
  class*: it realizes a module with fixed `gr M`, indexed by q-Stokes data
  (Thm 5.5.7: Stokes matrices are unipotent on `gr`; §2.3: formal class =
  `gr M`). **Summation never changes the slope multiset.**
- C1 at ∞ is **pure isoclinic** `{½,½}` (irreducible `E(2,1,·)`); GGM is
  **anisoclinic** `{−1,+1}`. Different `gr` ⇒ no summation functor bridges
  them.
- Ramified pullback `x → x^{1/ℓ}` scales slopes *uniformly* (Thm 2.2.1(iv)):
  `{½,½} → {ℓ/2, ℓ/2}` — an **equal pair for every ℓ**, which can never
  equal the distinct pair `{−1,+1}`. (ℓ=2 lands C1 on pure isoclinic slope
  1, still one slope.) **Isoclinicity survives summation, Borel shear, and
  ramification** — it is the permanent obstruction.

So **no q-difference-module transform of any kind — meromorphic gauge
(Route A), formal q-Borel weight (Route D), analytic q-summation, or
ramified pullback (Door-i) — maps C1 to GGM.** The only carve-outs left are
non-module maps (arbitrary sequence-level identifications, inhomogeneous
correspondences), which lie *outside* q-difference-module theory entirely
and carry none of the structural meaning the conjecture intends.

**This promotes R1 (§3) to the favored reading** and refutes, at the module
level, the conjecture's literal "identify with the GGM Stokes datum" clause:
the binding q-lift kernel C1 is a genuinely distinct object — its own
pure-isoclinic Gevrey-½ module — not a transform of the colored-Jones /
Stokes carrier. Re-scoping the conjecture accordingly is an owner-level
framing decision (see §5).

## 5. Effect on the conjecture

`conj:qdifference-kernel-prolongation-symbol` stays a conjecture, but its
content is now sharply constrained. **Five routes** (A slopes, B theta-growth,
C module-embedding, D formal q-Borel, Door-i analytic summation + ramified
pullback) exclude *every* q-difference-module identification of C1 with GGM,
the last by a permanent invariant (isoclinicity). The honest options for the
block, an **owner-level framing decision**:

- **(F1) Re-scope to R1** — rewrite the conjecture as "the prolongation
  symbol is the binding module C1 (`qlift_normalized_kernel_exists`)", and
  demote the GGM/Stokes identification to a *separate, distinct-face*
  relationship (or drop it). This is the reading the five routes favor.
- **(F2) Keep both, mark the GGM clause module-refuted** — retain the
  conjecture but annotate that the C1↔GGM identification is excluded as
  q-difference modules, leaving only non-module correspondences as the
  (weak, structure-free) surviving possibility.
- **(F3) Split** — one conjecture for "C1 is the prolongation carrier"
  (well-posed, R1), one for "C1 and GGM are two faces of one order-≥3 SW
  object" (R2, Route C's `L3` embedding target).

The `authorNotes` records the five-route verdict; the choice among F1–F3 is
deferred to the owner (it rewrites the conjecture's core claim).

## 6. Discipline

- **Corpus-grep:** the identification's entire trail is this branch's
  2026-07-20 files (confirmed by the gauge-gap corpus sweep); no prior
  attempt, so no closed item is re-opened. The four route docs + Lean are
  the evidence base.
- **Anti-laundering / anti-fit:** every route is parameter-free; the
  invariant mismatch is exact rational arithmetic (D) plus a cited
  classification theorem (A). No AME data anywhere. The scope-(b) claim
  cites its invariant per the refuted-discipline rule; R1/R2 are held open,
  not asserted.
- **Reversal-safety:** the reframe does **not** claim the conjecture false —
  only that its *algebraic-gauge* reading is excluded and its *GGM-identity*
  clause is now one of two live readings. Door-i's verdict updates this.
