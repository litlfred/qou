# External dialog assessment: Écalle alien calculus ↔ Yekutieli non-abelian Stokes — what is right, what is standard, what has no object

**Date:** 2026-09-05 · **Branch:** `claude/binding-gap-categorical-research-cem5tp` (PR #6865)
**Beans:** `qou-2akx` (session), `qou-onte` (parent research doc)
**Scope:** scope-(a) assessment of an owner-pasted AI dialog, under the critical-distance
license. **No derivation, no number, nothing wired.** Corpus-grep paths 1–6 run by hand
(path 0 unavailable); the corpus turns out to hold a full alien-calculus arc from July 2026 that
the dialog does not know about, and that arc decides most of the questions.

---

## 0. The claim, flatly

1. **The dialog's one-dimensional half is correct and standard.** Alien derivations `Δ_ω` generate
   a free (hence non-commutative) Lie algebra; Stokes automorphisms `𝔖 = exp(Δ)` compose
   non-commutatively; the total monodromy across several Stokes rays is a path-ordered product.
   None of that needs Yekutieli: a path-ordered product of group elements is ordinary 1-dimensional
   holonomy (Dyson / Schlesinger), which is Yekutieli's *chapter 3*, not his theorem.
2. **The dialog's two-dimensional half has no object behind it.** "Alien data jumping across 2-D
   Stokes walls, integrated over a surface by non-abelian surface holonomy for a categorical gauge
   group" requires a **Lie crossed module** `(G, H, Ψ, Φ)` with `H` the group in which surface
   holonomy lives. Alien calculus supplies one pronilpotent Lie algebra (a `G`); nobody — not the
   dialog, not the corpus, not the resurgence literature I know — has named an `H` of "alien
   2-derivations" with a feedback map `Φ : H → G`. Without it Yekutieli's 2-dim MI is not
   applicable; the sentence is vocabulary, not mathematics. Kontsevich–Soibelman wall-crossing is
   a product of *1-dimensional* automorphisms around a point in a 2-dimensional parameter space;
   the wall is a codimension-1 locus, not a surface one integrates over.
3. **The corpus already asked "do we need non-abelian Stokes for the resurgence?" and answered
   it** on 2026-07-07: *no for the compute, yes as the fibre origin* — the two "Stokes" are
   different objects (the categorical connection that builds `𝐂 → H_n(q)`, versus the Borel-plane
   jumps that connect saddles), linked only through the flat connections that are the saddles
   ([`2026-07-07-fmap-resurgence-action-and-pion-knot.md`](2026-07-07-fmap-resurgence-action-and-pion-knot.md)).
   The dialog conflates them, exactly the "triple-overloading hazard" the utilization audit named
   ([`2026-07-12-borel-alien-calculus-utilization-audit.md` §3](2026-07-12-borel-alien-calculus-utilization-audit.md)).
4. **The answer to the dialog's question is: yes, and the corpus has measured which space.** The
   binding kernel's asymptotics are **Gevrey-1/2, Lean-proved** (`QOU.Mass.BindingGevreyHalf`), so
   the standard (Gevrey-1) Borel plane is the *wrong* plane — the dialog's "alien derivatives at
   singularities in the Borel plane" is refuted at scope (a) for this kernel
   ([`2026-07-12-alien-calculus-review-binding-gevrey-half.md`](2026-07-12-alien-calculus-review-binding-gevrey-half.md)).
   The level-1/2 singularity sits at `ξ = 1/√2` at `q = 1`, and **at `q₀` the class changes to
   q-Gevrey**: the correct plane is the **q-Borel plane** (Ramis–Sauloy–Zhang theta kernel, held,
   tested as route D on 2026-07-20) and the arithmetic home is the **Habiro ring / cyclotomic
   completion** — non-archimedean in the cyclotomic-adic sense, which is the fibre-vs-observable
   banner's "all orders in `q`". The archimedean Stokes/wall-crossing structure is post-`τ` and is
   the wall the framework deliberately does not cross before the final evaluation (KS audit §16.1).
5. **One connection in the dialog's vicinity is real, non-obvious, and now checkable — and the
   dialog did not make it.** Écalle's alien Lie algebra, graded by the singularity `ω`, is
   **pronilpotent**; Stokes automorphisms are its exponentials; gauge equivalence of the resulting
   transseries data is a Maurer–Cartan / Deligne-groupoid question. That is exactly the subject of
   Yekutieli's *MC Elements in Pronilpotent DG Lie Algebras* ([arXiv:1103.1035](https://arxiv.org/abs/1103.1035),
   ingested today as `library/arxiv-1103.1035v4`): a DG Lie quasi-isomorphism induces an
   equivalence of reduced Deligne groupoids in the unbounded pronilpotent case. So the honest
   bridge between the two authors is **Yekutieli-2012 (MC elements), not Yekutieli-2015 (surface
   integration)** — the 1-groupoid of Stokes data, not a 2-holonomy. Judgement, not finding.

---

## 1. Verdict per claim

| dialog claim | status | corpus evidence |
|---|---|---|
| `Δ_ω` do not commute; `𝔖_ω = exp(Δ_ω)`; monodromy is path-dependent | **correct, standard** | Écalle; the corpus's `def:ecalle-borel-resummation`, `rem:st-is-median-resummation`; G4 "Habiro kernel `R(q,ξ)` as a Stokes automorphism" (utilization audit) |
| "calculating the global Stokes phenomenon across a web of singularities requires precisely the multiplicative integration Yekutieli formalized" | **over-claimed** — it requires 1-dim path-ordered exponentials (Schlesinger), which predate Yekutieli by a century; Yekutieli's contribution is the *2-dim* MI and the 3-dim Stokes theorem | Yekutieli 2015 Thm 0.4.2 states its own `G = H = GL_m` special case *is* Schlesinger |
| "alien data jumps across 2-D Stokes walls … integrated over a surface … categorical gauge group" | **no object**: needs a crossed module `(G,H,Ψ,Φ)`; no `H` is named anywhere | 0 hits for "alien" + "crossed module" in the same file across `content/ docs/ computations/ .beans/` (measured) |
| "KS wall-crossing formulas need alien data integrated over a surface" | **wrong shape**: the KS product is a product of 1-dim automorphisms ordered by phase around a point; a wall is codimension 1 | [`2026-06-04-kontsevich-soibelman…`](2026-06-04-kontsevich-soibelman-0811.2435-qou-comparison.md) §0-Q8, §16.1 |
| implicit: the binding kernel's divergence is Gevrey-1 (factorial), so standard Borel applies | **refuted (scope-a, Lean-backed)**: Gevrey-1/2; level-1/2 singularity at `1/√2`; q-Gevrey at `q₀` | `QOU.Mass.BindingGevreyHalf`; `lever1_borel_half_singularity_probe.py` |
| "does your framework require integrating over a non-archimedean or q-deformed space?" | **yes — q-Borel (RSZ theta kernel) at the level the growth dictates, and the Habiro ring as the cyclotomic-adic home; the archimedean Stokes structure is post-`τ`** | route D (`2026-07-20-qlift-routeD-qborel-transform.md`); `conj:surreal-limit-transfer` (median resummation = standard part, class with no instance) |

## 2. What the corpus holds that the dialog should be read against

- **Stokes constant as a count.** `A_ω(4₁) = 3` is proved as an integer-matrix fact from the
  certified Garoufalidis–Gu–Mariño series and *identified* with a BPS/DT count only conditionally
  on `conj:stokes-dt-bps-bridge` (a §3b class; bean `qou-ypge` still owes it the Bridgeland
  citation, `[bridgeland2016]`). The dialog's "BPS wall-crossing" is this bridge, and it is a
  conjecture here, not machinery.
- **The f-map is the resurgence connection** (PR #3474): its Stokes datum is a *complex* instanton
  action oscillating near `|A| ≈ 0.5–0.6`, consistent with `Vol ± iCS`, preliminary at 6 orders.
  Nothing in the dialog changes that measurement.
- **Median resummation = standard part** (`conj:surreal-limit-transfer`, content-bearing class,
  no instance, no sorry). This is the corpus's formalised statement of "how alien data reaches an
  archimedean number", and it is a surreal/standard-part statement, not a surface integral.

## 3. What this changes for the research doc

Nothing in §§5–7 of
[`2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md`](2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md).
Two additions worth recording there later, not now: (i) route D's "kite tethering" check (§4.4)
has a resurgence twin — a Stokes automorphism along one ray is tethered to the base point of the
Borel plane in the same way; (ii) the pronilpotent-MC reading in §0.5 above is a fourth place
where Yekutieli's *groupoid* half meets the framework, and it is the one place where his
*deformation* papers (now all held) rather than the surface-integration book are the right text.

## 4. Verification limits

Path 0 unavailable; all corpus absences lexical. The claim "no `H` of alien 2-derivations exists
in the literature" is my knowledge, not a measurement — the corpus-grep establishes only that
none is *held*. If the owner knows of one, §0.2 is the sentence to overturn.
