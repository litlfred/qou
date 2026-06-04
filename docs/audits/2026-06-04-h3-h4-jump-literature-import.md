# Literature import — the H₃ → H₄ "partition jump" in the mass/binding weight

**Date:** 2026-06-04
**Trigger:** PR #1762 ("1ppQ roadmap + Geom_full bridge derivation gap") Option E —
focused literature-import research to find an established mathematical result
that would **derive** or strongly **analogize** the H₃ → H₄ jump in production.
**Scope:** research/audit only. No production code, content blocks, or witnesses
were modified. This document is the sole deliverable.

> **Tool note.** The `mcp__paper-search-mcp__*` tools (search_arxiv,
> read_arxiv_paper, search_google_scholar) were **permission-denied** in this
> session, and direct `arxiv.org` PDF fetches returned **HTTP 403**. All
> citations below were therefore verified via **WebSearch** against the arXiv
> abstract pages, publisher pages (Annals of Mathematics, J. reine angew. Math.),
> and nLab. Every citation here resolves to a real source; none is fabricated.
> Where a full-text read would have sharpened a verdict, that is flagged inline.

---

## §1. The gap (one paragraph)

The canonical mass formula is `m(K) = m_e · Geom_full(K, q₀)`. In production,
every atom's `Geom_full` is evaluated through `geom_full_borromean(q)`, whose
linking weight is the **Family-A** factor `5/2 + (3/4)·h²` (`h = q − q⁻¹`). The
leading constant **5/2** is the *number of partitions of 4* — the Wedderburn-block
count of the **H₄** Iwahori–Hecke algebra: `(4), (3,1), (2,2), (2,1,1),
(1,1,1,1)`. But the proton braid 𝓑₃ is a **3-strand** braid, living in **H₃**,
whose Wedderburn decomposition is over the **3** partitions of 3 (`(3), (2,1),
(1,1,1)`). Production therefore evaluates a 3-strand object's mass/binding weight
as a structure indexed by **partitions of 4, not 3** — an unexplained "H₃ → H₄
jump" (`H_4_dim_count = 5`). This jump is load-bearing: it maps to 3 of the 5
missing L2 100× observables (m_n, Δ_pn, m_K/m_π) per PR #1762 §2. The question:
**is there an established theorem that forces, derives, or naturally analogizes a
+1 shift in the strand/partition index of a braid evaluated under the Markov
trace?**

---

## §2. Candidate 1 — Markov stabilization / Markov's theorem  *(MOST PROMISING)*

**The relevant theorem.** Markov's theorem states that two braids `β ∈ B_n` and
`β' ∈ B_m` have **isotopic closures** (`β̂ ≅ β̂'`) iff they are related by a
finite sequence of (i) conjugation within a braid group and (ii) **stabilization**:
the move `β ∈ B_n ↦ β·σ_n^{±1} ∈ B_{n+1}` (and its inverse, destabilization).
A link invariant built from a braid representation must therefore be invariant
under stabilization — this is exactly the **Markov-trace property**. In the
Iwahori–Hecke setting (Jones 1987, following Ocneanu), the trace `tr` on the
**tower** `H_1 ⊂ H_2 ⊂ ⋯ ⊂ H_n ⊂ H_{n+1} ⊂ ⋯` is defined **inductively** with
a *conditional-expectation / Markov property* relating `tr` on `H_{n+1}` to `tr`
on `H_n`: `tr(x·σ_n) = z·tr(x)` for `x ∈ H_n`. The Markov-trace weights are
indexed by **partitions** (Young diagrams), and the inductive step from `H_n`
to `H_{n+1}` is, on the Bratteli/branching diagram, exactly **"add one box"** to
a Young diagram — i.e. the restriction–induction pair carries `λ ⊢ n` to
`μ ⊢ n+1` with `μ` obtained by adding a single box.

**Citations (verified).**
- V. F. R. Jones, *Hecke algebra representations of braid groups and link
  polynomials*, **Annals of Mathematics 126 (1987), no. 2, 335–388**.
  [annals.math.princeton.edu/1987/126-2/p05](https://annals.math.princeton.edu/1987/126-2/p05).
  (The Ocneanu trace on the H_n tower; the two-variable HOMFLY invariant via the
  inductive Markov property.)
- R. C. Orellana, *Weights of Markov Traces on Hecke algebras*,
  **arXiv:math/9806163** (1998), J. Algebra.
  [arxiv.org/abs/math/9806163](https://arxiv.org/abs/math/9806163). (Markov-trace
  weights are values at the **minimal idempotents**, indexed by **pairs of Young
  diagrams / partitions**; the tower `{H_n(u)}` and the branching structure.)
- M. Geck & S. Lambropoulou, *Markov traces and knot invariants related to
  Iwahori–Hecke algebras of type B*, **J. reine angew. Math. 482 (1997),
  191–213**.
  [degruyterbrill.com/…/crll.1997.482.191](https://www.degruyterbrill.com/document/doi/10.1515/crll.1997.482.191/html).
  (Inductive construction of normalized/non-normalized Markov traces on
  `{H_n}_{n=1}^∞`; the H_n → H_{n+1} branching is explicit.)

**Verdict: SUPPORTS (as an analogy), but does NOT force the production jump.**

- *Why it supports.* The H_n → H_{n+1} promotion is a **real, canonical move** in
  exactly the algebra the framework uses, and the trace the framework uses
  (`tr_M = Σ_λ y_λ χ^λ`, Wenzl) is precisely the Markov trace whose inductive
  definition lives on the box-adding branching graph. If the proton's mass weight
  is naturally an object on the **stabilized** braid `𝓑₃·σ₃^{±1} ∈ B₄`, then it
  is genuinely a sum over `λ ⊢ 4` — the "5/2 = #partitions(4)" would be the
  Wedderburn-block count *after one stabilization*. This is the single literature
  result in which a strand-count `+1` appears as a forced, canonical, invariant
  preserving operation.
- *Why it does not close the gap.* Stabilization is an **equivalence move**, not a
  promotion that changes the invariant. The whole point of the Markov property is
  that the (suitably normalized) trace is **invariant** under `β ↦ β·σ_n^{±1}`:
  the closure `β̂` is unchanged, so the *physical observable* (a link/knot
  invariant) cannot depend on whether you read the proton as a 3-strand or a
  stabilized 4-strand braid. Hence Markov's theorem **permits** evaluating 𝓑₃ in
  H₄ (via stabilization) but gives **no reason to prefer** the partitions-of-4
  count over partitions-of-3 — and, taken at face value, says the two must give
  the **same** trace value (modulo the normalization factor `z`). So the theorem
  *legitimizes* the H₃ → H₄ move as well-defined but does **not derive** that the
  weight "should" be a 5-term `λ ⊢ 4` sum rather than a 3-term `λ ⊢ 3` sum. PR
  #1762 §2.3 already flagged the Hilbert-space resolution-of-identity (H2) variant
  of this as "prima facie wrong"; this audit agrees on the precise reason: a
  destabilizable strand is invisible to the invariant.

**Net for the framework.** This is the **right place to look** for a derivation,
but the correct form of the claim is *not* "stabilization promotes H₃ → H₄."
The promising sub-direction is the **branching/box-adding** structure underneath
the Markov property: the candidate that "5/2" counts the partitions of 4 reachable
by **adding one box to the partitions of 3** (the `H₃ ↗ H₄` induction-functor
image), which would tie the +1 to the **induction product `Ind_{H₃}^{H₄}`** — a
canonical, non-equivalence operation. That is a *categorical* refinement of the
naive stabilization story and the single most worthwhile lead to chase next.

---

## §3. Candidate 2 — Volume conjecture (Kashaev; H. Murakami – J. Murakami)

**The relevant theorem/conjecture.** The volume conjecture asserts
`(2π/v₃)·lim_{N→∞} log|J_N(K; e^{2πi/N})|/N = ‖K‖` (Gromov norm; `= Vol(S³∖K)/v₃`
for hyperbolic K), where `J_N` is the **N-colored** Jones polynomial and the limit
is the `q → 1` root-of-unity asymptotic. Kashaev conjectured it via his quantum-
dilogarithm invariant; H. Murakami & J. Murakami identified Kashaev's invariant
with the colored Jones polynomial and stated the general conjecture; H. Murakami
verified the figure-eight case.

**Citations (verified).**
- H. Murakami, *The asymptotic behavior of the colored Jones function of a knot
  and its volume*, **arXiv:math/0004036** (2000).
  [arxiv.org/abs/math/0004036](https://arxiv.org/abs/math/0004036). (Figure-eight
  colored-Jones asymptotic confirming Kashaev's conjecture.)
- H. Murakami & J. Murakami, *The colored Jones polynomials and the simplicial
  volume of a knot*, **arXiv:math/9905075**, Acta Math. 186 (2001), 85–104.
  [arxiv.org/pdf/math/9905075](https://arxiv.org/pdf/math/9905075).
- R. M. Kashaev, *The hyperbolic volume of knots from quantum dilogarithm*,
  Lett. Math. Phys. 39 (1997) — the origin conjecture (referenced throughout the
  above; not independently fetched here, flagged).

**Verdict: SILENT on the strand/partition jump.**

- The volume-conjecture limit parameter is the **color N** (the dimension of the
  `U_q(sl₂)` irrep cabling each strand) and the **root-of-unity order**, *not* the
  number of strands of the braid or the partition index `n`. The asymptotic shifts
  `N → ∞`; there is no `n → n+1` strand promotion anywhere in the statement.
- The framework *does* already use the Kashaev `tr_M ~ exp(Vol)` relation as the
  scaffold for the binding linearization (cheat-sheet §3 "Bind" row, §9.2), so the
  volume conjecture is structurally relevant to the framework — but it offers
  **no mechanism** for the partitions-of-4-vs-3 count. It speaks to *Geom_leading
  = Vol(K)/ℏ_q²* (the leading factor), not to the *linking-weight* factor where
  the H₄ count sits. Honest negative: do not expect the volume conjecture to
  explain the +1.

---

## §4. Candidate 3 — Habiro ring / cyclotomic completion of WRT invariants

**The relevant result.** Habiro's cyclotomic completion `ℤ[q]^` (the "Habiro ring")
is the natural home of the **unified WRT invariant** `J_K(q)` of an integral
homology sphere / knot complement: a single element that **simultaneously
specializes** at every root of unity *and* admits a Taylor expansion at `q = 1`.
The 2024 **Habiro ring of a number field** (Garoufalidis–Scholze–Wheeler–Zagier)
upgrades this to modules **graded by `K₃(F)`**, identifying the perturbative
Chern–Simons / Bloch-group data with this arithmetic grading.

**Citations (verified).**
- S. Garoufalidis, P. Scholze, C. Wheeler, D. Zagier, *The Habiro ring of a number
  field*, **arXiv:2412.04241** (Dec 2024).
  [arxiv.org/abs/2412.04241](https://arxiv.org/abs/2412.04241);
  [nLab: Habiro ring](https://ncatlab.org/nlab/show/Habiro+ring).
- S. Garoufalidis & D. Zagier, *Knots, perturbative series and quantum
  modularity*, **arXiv:2111.06645** (2021).
  [arxiv.org/abs/2111.06645](https://arxiv.org/abs/2111.06645). (Source of the
  per-knot perturbative series `Φ_K(h)` the framework would compare Family-A
  against; flagged as the "single highest-leverage experiment" in PR #1762 §6.8.)

**Verdict: SILENT on the strand/partition jump — but the strongest *adjacent*
hook for the per-knot λ(K) derivation (a different gap).**

- The Habiro ring provides the right **analytic object** to carry a per-knot weight
  `λ(K)` that is simultaneously valid at the framework's two regimes (real
  `q₀ ≈ 1.110` and the RT root-of-unity regime), and the `K₃`-grading is rigid
  (no free parameters → Δ_λ-compliant). This is genuinely valuable, and PR #1762's
  background agent already surfaced it as "the strongest hook."
- **However, it says nothing about strand count.** The Habiro element is attached
  to a *fixed* knot/link; there is no `n → n+1` braid-index shift in its
  construction. It would explain *what* `Geom_full(K)` is as a function of `q`
  (the per-knot wire-up gap, cheat-sheet §5 item #1), but **not** *why a 3-strand
  braid's weight is indexed by partitions of 4*. These are orthogonal gaps. Citing
  Habiro for the H₃→H₄ jump specifically would be a category error; cite it for the
  per-knot `Geom_full(K, q₀)` refinement instead.

---

## §5. Candidate 4 — Khovanov–Rozansky sl_N → sl_{N+1} stabilization

**The relevant result.** Triply-graded (HOMFLY-PT) Khovanov–Rozansky homology
categorifies the HOMFLY polynomial; for each `N > 0` there is a **spectral
sequence from the reduced triply-graded homology to reduced sl(N) homology**,
which **stabilizes (becomes trivial) for large N** — the "large-N stabilization"
of Dunfield–Gukov–Rasmussen / Rasmussen.

**Citations (verified).**
- N. M. Dunfield, S. Gukov, J. Rasmussen, *The superpolynomial for knot
  homologies*, **arXiv:math/0505662** (2005).
  [arxiv.org/pdf/math/0505662](https://arxiv.org/pdf/math/0505662).
- J. Rasmussen, *Some differentials on Khovanov–Rozansky homology*,
  **arXiv:math/0607544** (2006).
  [arxiv.org/pdf/math/0607544](https://arxiv.org/pdf/math/0607544). (The `d_N`
  differentials / spectral sequences `HHH → sl(N)`.)
- N. Chandler, E. Gorsky, et al., *Structures in HOMFLY-PT homology*,
  **arXiv:2209.13058** (2022).
  [arxiv.org/abs/2209.13058](https://arxiv.org/abs/2209.13058).

**Verdict: REFUTES (the analogy points the wrong way).**

- The "+1" in Khovanov–Rozansky stabilization is a shift in the **rank `N` of the
  gauge Lie algebra `sl_N`** (the color/representation category), **not** in the
  number of strands or in the partition index `n` of the symmetric group / Hecke
  algebra. `sl_N → sl_{N+1}` changes *which* `R`-matrix / quantum group acts; it
  does not promote `H₃ → H₄`. The framework's H₄ count is a `λ ⊢ 4` Hecke-block
  count (an `S_4` / `H_n` datum), which is the **transverse** axis to the `sl_N`
  rank. So KhR stabilization is not even an analogy for the production jump — it is
  a shift along a different axis, and importing it would actively mislead.
- (Tangential positive: large-N stabilization is the categorified shadow of the
  HOMFLY two-variable structure the Markov trace already lives in, so it reinforces
  that the **Hecke/Markov** axis — Candidate 1 — is the right one, by contrast.)

---

## §6. Most promising lead + recommendation

**Most promising: Candidate 1 (Markov stabilization), but reframed as the
induction functor `Ind_{H₃}^{H₄}` / box-adding branching — NOT bare
stabilization.**

Rationale:

1. It is the **only** candidate in which a strand/partition `+1` appears as a
   canonical, invariant-respecting operation **in the exact algebra the framework
   uses** (the Hecke tower with the Ocneanu/Markov trace `tr_M = Σ_λ y_λ χ^λ`).
   Candidates 2–4 shift a *different* index (color N, root-of-unity order, gauge
   rank) and are SILENT/REFUTES on strand count.
2. The "5/2 = #partitions(4)" production constant is literally a Wedderburn-block
   count of **H₄**, and the H₃ → H₄ branching graph **is** the box-adding induction
   diagram (Jones 1987; Orellana 1998; Geck–Lambropoulou 1997). The numbers line
   up: `λ ⊢ 3` has 3 blocks, and adding one box reaches the `λ ⊢ 4` blocks whose
   count is 5.
3. **The honest caveat that must travel with this lead:** Markov's theorem makes
   stabilization an **equivalence** (the trace is *invariant* under
   `β ↦ β·σ_n^{±1}`), so bare stabilization cannot *derive* a preference for the
   H₄ count — a destabilizable strand is invisible to the link invariant. The
   derivation, if it exists, must come from the **induction product**
   `Ind_{H₃}^{H₄}(𝓑₃)` being the *physically correct* object (e.g. because the
   proton's interface/closure genuinely lives one strand up), not from
   stabilization-as-equivalence. This is PR #1762's H1/H3 territory (brane-tower
   truncation), and it is where the categorical work should concentrate.

**Concrete next experiment** (cheap, derivation-discipline-safe): compute the
**induction-restriction multiplicities** `λ ⊢ 3 ↗ μ ⊢ 4` on the H₃ ⊂ H₄ Bratteli
diagram and check whether the Family-A leading constant `5/2` and the `3/4·h²`
correction emerge as the **Markov-weighted box-adding sum** over the 5 partitions
of 4 reachable from the 3 partitions of 3. If yes, the H₄ count is *derived* as
`Ind_{H₃}^{H₄}`, not assumed; if no, the jump remains conjectural and the
production `geom_full_borromean` constant stays a fitted/structural placeholder.
This sits **above** Candidate 1's bare-stabilization reading and **below** the full
Δ_λ Kashiwara-crystal closure (PR #1762 Option D).

---

## §7. Honest-negative summary table

| Candidate | Index that shifts | Verdict on H₃→H₄ | Use it for |
|---|---|---|---|
| 1. Markov stabilization / induction | **strand n → n+1 (partition box)** | **SUPPORTS (analogy); does not force** | the H₃→H₄ jump — chase `Ind_{H₃}^{H₄}`, not bare stabilization |
| 2. Volume conjecture | color N, root-of-unity order | **SILENT** | `Geom_leading = Vol(K)/ℏ_q²`, binding linearization |
| 3. Habiro ring | none (fixed knot) | **SILENT** | per-knot `Geom_full(K, q₀)` wire-up (a different gap) |
| 4. KhR sl_N stabilization | **gauge rank N**, not strand | **REFUTES (wrong axis)** | nothing here; do not import for the jump |

**Bottom line.** No established theorem *forces* a 3-strand braid's weight to be
evaluated over partitions of 4. The only candidate that even **analogizes** a
strand-count `+1` is Markov stabilization — and Markov's theorem makes that move an
*equivalence*, so it legitimizes but cannot derive the jump. The live derivation
path is the **box-adding induction functor `Ind_{H₃}^{H₄}`** underneath the Markov
trace (Candidate 1, reframed), with the Habiro ring (Candidate 3) reserved for the
orthogonal per-knot `λ(K)` gap. Candidates 2 and 4 should not be cited for this
specific jump.
