# Q_β c_k closure — untested avenues × literature survey

**Date:** 2026-07-11
**Status:** SURVEY — no derivation, no wiring, no probe run. This doc maps
avenues **not yet tested** (checked against the refuted-class map C1–C14 and
the kernel-constraint registry KC1–KC20) and what the external literature
offers for each. Every proposed avenue below carries a formalize-first
invariant + kill criterion per [AGENTS.md](../../AGENTS.md) §"Formalize-first probe discipline".
No c_k value is proposed anywhere in this doc (flip-flop guard).

**Authoritative companions (read first):**
[`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
(method-level, C1–C14),
[`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
(rung tiers + KC constraints),
[`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) (master ledger).

---

## 1. Corpus-internal candidates proposed but never executed

From the PR #1585 five-candidate queue (2026-05-31) and later session flags,
these remain **proposed-never-run** as of 2026-07-11:

| # | candidate | status | note |
|---|---|---|---|
| U1 | **Exponentiated per-block** decomposition (`F = exp(Σ per-block)` instead of product) | untested | #1585 queue item 2; never picked up |
| U2 | **Modular bootstrap** | untested, **blocked on missing infra** | #1585 queue item 4; the 2026-07-06 accuracy audit found the corpus "Φ_q" is the compact q-dilog — the **Faddeev Φ_b / modular double is entirely absent**, so every prior Φ-probe on the decay face used the wrong object |
| U3 | **Galois descent on the Habiro ring** | untested | #1585 queue item 5 / #1713 Phase B menu; see §2 item 1 and §3.F — GSWZ 2024 now supplies the actual descent structure (Frobenius gluing) |
| U4 | **Exotic-signed Lusztig** (Whittaker / Yun–Zhu / twisted `T_i`) | narrowed (N1–N3, PR #1930) but formally open | research-grade; specifying the convention IS the task |
| U5 | **KC15 odd-channel candidate `D(q)`** (bar-odd 4₁-operator pair difference) | gate-passed, not driven to a value | with P-C15 (4₁ qZeilberger kernel, Casoratian bar-self-reciprocal) the only surviving fibre-kernel objects |
| U6 | **Exact chiral operator realizing `q^{2n(λ)}` at `q = i`** | open (#3509) | the Δ_λ/Q_β shared ζ₄ fibre locus |
| U7 | **Closed tower-summed trace difference** (convergence-leg, `conj:qbeta-trace-counit-convergence`) | open | would upgrade the counit-vs-trace 0.99% bound |

## 2. Literature survey — what exists (verified arXiv IDs)

Backends note: paper-search MCP was proxy-blocked; results are WebSearch-driven
with per-item arXiv verification.

1. **Habiro ring structure.** Habiro's injectivity theorem — an element of
   `Ẑ[q]` is uniquely determined by its Taylor expansion at q=1, with
   **integer** coefficients in the `(q−1)` / cyclotomic basis
   (arXiv:math/0209324, Publ. RIMS 2004). Unified WRT: arXiv:math/0605314
   (Invent. Math. 2008); rational homology spheres: Beliakova–Bühler–Le
   arXiv:0801.3893. **New (Dec 2024): Garoufalidis–Scholze–Wheeler–Zagier,
   "The Habiro ring of a number field" (arXiv:2412.04241)** — elements are
   collections of series at each root of unity glued by a Frobenius
   endomorphism, with admissibility controlled by a **Bloch-group element**
   (hyperbolic-geometry datum). Follow-ups: arXiv:2505.19885,
   arXiv:2510.04782.
2. **Ohtsuki series.** LMO (arXiv:q-alg/9512002) universal; integrality
   (Lawrence 1999; Habiro 2008). Injectivity needs the full series — no
   theorem recovers the element from finitely many coefficients, but
   integrality + growth class cut the space to a lattice.
3. **Quantum modularity + resurgence.** Garoufalidis–Zagier
   arXiv:2111.06645 (SIGMA 2024) + arXiv:2304.09377: the 4₁ perturbative
   series sits in a matrix of q-series with quantum-modular gluing
   `q ↦ q̃ = e^{−4π²/ln q}`. Resurgence: Gukov–Mariño–Putrov
   arXiv:1605.07615; **Andersen–Mistegård arXiv:1811.05376** (Ẑ is a
   resummation of the Ohtsuki series for Seifert HS, Borel singularities at
   complex-CS values); Costin–Garoufalidis arXiv:math/0609619;
   Garoufalidis–Gu–Mariño arXiv:2007.10190. Directly on target:
   **Crew–Fantini–Goswami–Osburn–Wheeler, "Resurgence, Habiro elements and
   strange identities" (arXiv:2304.07001)** and Goswami–Osburn
   arXiv:2204.02628 (asymptotics + sign patterns of Habiro-element
   coefficients).
4. **Cyclotomic expansions.** Habiro's `J_K = Σ C_n(K)·(q^{1+N};q)_n(q^{1−N};q)_n`
   with `C_n ∈ Z[q^±]`; **Masbaum arXiv:math/0306345 gives closed-form `C_n`
   for all twist knots**; double-twist arXiv:2110.03616, arXiv:2308.16749;
   Willetts arXiv:2003.09854 (unified ADO/colored-Jones in a Habiro-type
   ring). Surgery formulas extend to links (Hopf, Borromean).
5. **Experimental identification.** No black-box "q-series from truncated
   coefficients" tool exists. The working method is Garoufalidis–Zagier:
   Richardson/Zagier extrapolation + **PSLQ against a small basis dictated by
   the arithmetic** (trace field, its units, Bloch–Wigner values, powers of
   π) — arXiv:2304.09377. PSLQ canon: Bailey–Broadhurst arXiv:math/9905048.
6. **Kreimer knots↔Feynman program (outside-view precedent).**
   Broadhurst–Kreimer hep-ph/9504352, hep-th/9609128; Kreimer, *Knots and
   Feynman Diagrams* (CUP 2000). **Verdict: abandoned** — broke at 10
   crossings / 7 loops; the durable descendants (Connes–Kreimer Hopf algebra,
   Brown's motivic periods) replaced knots. Its failure mode — low-order
   number-matches that die at higher order — is exactly the c_3 ≈ −2
   near-match risk this ledger already polices.
7. **q-holonomic methods.** Colored Jones is q-holonomic
   (Garoufalidis–Le arXiv:math/0309214); AJ conjecture arXiv:math/0306230;
   modular q-holonomic modules arXiv:2203.17029. Software for
   guessing/testing q-recurrences from finite data: **qGeneratingFunctions**
   (Kauers–Koutschan, Ramanujan J. 2009), **qFunctions** (Ablinger–Uncu,
   JSC 2021), RISC qZeil/qMultiSum, Sage `ore_algebra`. With only ~6 rungs,
   guessing is under-determined (supports bisize ~(2,1) only); **testing** a
   known operator is well-posed.
8. **State integrals at real q.** Andersen–Kashaev arXiv:1109.6295;
   Garoufalidis–Kashaev state-integral evaluations; **"Summability for state
   integrals of hyperbolic knots" (arXiv:2410.20973)**: state integrals built
   from Faddeev's Φ_b are genuine analytic functions **off** |q|=1 whose
   expansions reproduce the perturbative series. Also Bettin–Drappeau
   arXiv:1905.02045 (exact modularity for q-Pochhammer / Zagier's modularity
   conjecture for knots ≤ 7 crossings incl. 4₁); Gukov–Manolescu F_K
   arXiv:1904.06057; GPPV arXiv:1701.06567.

## 3. New avenues (distinct angles, none in a refuted class)

Ranked by decisiveness-per-cost. Each has a pre-stated kill criterion.

### A. Arithmetic angle — Habiro-integrality kill-test (cheap, decisive)

Re-expand the empirical ladder data in the `(q−1)` / cyclotomic basis
`(q;q)_n` and test whether the induced coefficients are **integers** (Habiro
injectivity + integrality, §2.1). The corpus has never run this test.
*Invariant:* any genuine Habiro element has integer cyclotomic coefficients.
*Kill:* non-integrality at any order at 10⁻⁵⁰ **refutes the "F(q) is a
Habiro-ring element" hypothesis outright** — which would redirect the whole
axis to the analytic object of angle B. Either outcome narrows the search.
*Refuted-class check:* not a c_k derivation; a hypothesis-class test. Not in
C1–C14.

### B. Analytic angle — state integral / Faddeev modular double at real q₀

The structural tension the literature exposes: a raw Ohtsuki series is
**Gevrey-1 factorially divergent**, but the ladder is **convergent with a
simple pole at u_substrate** (KC8; `c_{k+1}/c_k → 1/u = 117.41`, geometric
growth — established at k = 8..10). So **F(q) cannot be a raw Ohtsuki series
of a hyperbolic manifold**; the analytically honest object at a real anchor
q₀ ≈ 1.11 (off the unit circle, outside the Habiro ring's natural domain) is
a **state integral / Borel-median resummation** (arXiv:2410.20973,
arXiv:1811.05376) or a convergent false-theta-type series inside the disk via
the bar involution `q₀ ↔ 1/q₀` (the move the keystone already uses for
`Ψ(1/q₀)`). This *also* dissolves U2's blocker into a concrete first step:
**build the Faddeev Φ_b / modular double** (the 2026-07-06 audit's missing
object) and compare the ladder to the 4₁/Borromean state-integral expansion
at q₀. *Kill:* state-integral expansion at q₀ fails c_2 = −1 exactly, or
fails the proton+muon anchor-stability gate (registry §8).
*Refuted-class check:* not C1 (not a real-q closed form for a c_k; a
fibre-level analytic construction evaluated at the anchor); not C14 (not a
root-of-unity forced-knot Ohtsuki lookup).

### C. Forced-candidate angle — the Borromean cyclotomic/unified-WRT expansion

C14 tested the two forced knots (4₁, Hopf) — **it never tested the Borromean
rings**, which are the framework's own nucleon braid 𝓑₃ and therefore a
zero-free-choice forced candidate under C14's own discipline. Habiro's
surgery formalism + tabulated cyclotomic coefficients (§2.4; Masbaum-style
closed forms) make the Borromean unified-WRT/cyclotomic expansion at q=1 a
**symbolic, finite computation** — a lookup, not a scan (no fitting).
*Kill:* fails to reproduce c_2 AND the c_3 shadow parameter-free → add a C15
row, stop. *Refuted-class check:* extends C14 to the one forced candidate it
missed; explicitly allowed by C14's "does not refute every root-of-unity
object" reading.

### D. Basis-constrained PSLQ (passes the repo's own entropy bound)

The refuted PSLQ attempt used an unstructured 12-constant basis (killed by
the entropy bound `precision > n·log₁₀(2·height)`). GSWZ (§2.1) + the
Garoufalidis–Zagier method (§2.5) dictate a **small arithmetic basis** for
each coefficient: the trace field of 4₁ is ℚ(√−3), so the basis is ~4–6
elements ({1, √3, Vol(4₁)/π, D(ζ₆)-values, π²}), well inside the 50-dps
entropy budget. This is per-coefficient recognition against a
theory-predicted lattice — the discipline-compliant version of the killed
attempt. *Kill:* no relation found within the entropy budget → coefficient
stays empirical; no fit is proposed.

### E. q-holonomic TEST (not guess) — drive P-C15/U5 to a verdict

The 4₁ order-2 qZeilberger operator already gate-passed as kernel candidate
(P-C15); the literature (§2.7) supplies the mature tooling
(qGeneratingFunctions / qFunctions / ore_algebra) to **test** whether the c_k
satisfy the known 4₁ (or Hopf) inhomogeneous q-recurrence, and to run the
deferred anchor Casoratian sweep. With 6 rungs this is well-posed as a test;
operator *guessing* stays deferred until ≥ 15 rungs exist (which the Δtr_M
even-in-ℏ series + f-map would have to supply first). *Kill:* recurrence
residual ≠ 0 at compute precision at both anchors.

### F. Descent/gluing angle — Galois descent with GSWZ Frobenius structure (U3)

The never-run #1585 candidate now has actual literature infrastructure: GSWZ
elements are exactly "series at each root of unity + Frobenius gluing +
Bloch-group admissibility". Formalize-first shape: state the gluing
constraint the c_k data must satisfy as a Lean-side conditional class before
any numeric sweep. *Kill:* the gluing constraint is symbolically incompatible
with the KC6 parity-shadow data (bar-odd a₁ with nonzero q=1 shadow).

### G. Internal quick wins (no literature needed)

U1 (exponentiated per-block — one probe script), U6 (chiral operator at
q = i), U7 (tower-summed trace difference). Each is a bounded probe with the
standard §8 anchor gate.

## 4. Outside-view caution

The Kreimer program (§2.6) is the historical precedent for exactly this
enterprise — matching physical perturbative numbers to knot invariants — and
it died of accumulated low-order near-matches. Its lesson is already encoded
in the registry's anchor-stability gate; angles A–C above are structural
(hypothesis-class tests), not value matches, which is the right side of that
history.

## 6. Execution-wave results (2026-07-11, owner-selected: all of A–G)

The owner selected all avenues (priority 1, 3, 5, 6, 4, 2 = §3.A, C, E, G, D,
B). Results land here per probe as they complete.

### PROBE 4 — basis-constrained PSLQ (§3.D): ENTROPY-BLOCKED (formalize-first kill)

**Stage 1 (entropy audit) killed Stage 2; PSLQ was NOT run.**

- Extraction chain: `c_3 = (Q_CODATA/Q_N2 − 1)/u³` amplifies relative σ(Q_β)
  by `1/u³ ≈ 1.62e6` (c_4: `1/u⁴ ≈ 1.90e8`). Chain reproduced exactly vs
  `qbeta-ck-cache` (delta 1.6e-30).
- Effective per-anchor digits of empirical c_3: actual σ(Q_β) = 0.78 ppm ⇒
  **0.2 digits** (both anchors); optimistic 7.8-ppb reading ⇒ **2.21 digits**
  (proton), **1.25** (muon — the q₀-pin channel 22 ppb × dc₃/dq ≈ 4.66e6
  dominates); corroborated by the 0.0105 inter-producer spread (~2.3 stable
  digits).
- **c_4: ZERO digits — and identically 0 by construction under exact c_3
  extraction; the quoted −0.972 is a rounding artifact of c_3** (confirms the
  registry rung-4 artifact tier mechanically).
- PSLQ entropy bound (PR #1805): minimal n=4, H≤100 needs 9.2 digits (12.2
  with margin); the full {1, √3, π², Vol(4₁), ζ(3)} basis at H≤10 needs 7.8.
  Best-case supply 2.21 ⇒ **deficit ≥ 7 digits**; max supportable basis = 1
  term. Passing even the minimal budget needs σ(Q_β) ≈ 8e-16 relative (~1
  ppq) or a canonical non-extracted c_3 producer — i.e. the open keystone
  F(q) itself.

**Conclusion:** coefficients remain empirical under the arithmetic basis. No
relation claimed, no value proposed, nothing wired (§8 guard intact). Scope:
**(a)-type** — blocks *PSLQ recognition of the extracted values*; does not
exclude any basis element from a future F(q) construction.
Witness: `computations/probes/qbeta-ck-basis-constrained-pslq.witness.json`.

### PROBE 6a — U1 exponentiated per-block seeding (§3.G): NEGATIVE (extends C13)

**Probe:** `computations/probes/qbeta_exponentiated_per_block_probe.py`
(witness `qbeta-exponentiated-per-block.witness.json`). Seed
`F = exp(N·Σ_λ g_λ(u_L))`, λ ∈ {(3),(2,1),(1,1,1)} (paper closed forms, PR
#1764; leading ε-coeffs −2/−1/−2), even-in-ℏ projection onto `u_L = b·ℏ_q²`
(C13 change of variable), UNIFORM weights, scale fixed only by the proved
`c_2 = −1`.

**Result:** `c_3 = −265/(94·b) ≈ −3.2494` at BOTH anchors — anchor-constant
(swing 3.9e-10 vs empirical 2.88%), 57.0% (proton −2.0693) / 61.7% (muon
−2.0097) off. `c_4 = ½ − 292/(47b²) ≈ −7.75`. Kill criterion hit (C13
failure mode) ⇒ **NEGATIVE**.

**Structural findings (why U1 could never differ at c_3):**
1. Uniform weights collapse `exp(Σ_λ g_λ)` to `exp(g_total)` — the
   per-block structure is invisible without a (forbidden, fitted) per-block
   weight rule.
2. With the seed starting at `u_L²` (no c_1 rung), exponentiated and linear
   seedings share `c_3` identically (verified symbolically); exponentiation
   first acts at `c_4` (+½·c_2²).
3. The per-block (y_λ-surrogate) sum is NOT ∝ the atomic Δtr_M
   (q-dependent ratio, 4 only at q=1) — different seed data, and it lands
   farther from empirical (−3.25) than C13's atomic seed (−1.50).

**Scope (a), not (b):** refutes the exponentiated-uniform per-block Δtr_M
seeding *alone*; does not exclude per-block data inside a non-linear or
derived-non-uniform closure. C13 row extends to: linear, bar-even, AND
exponentiated-uniform Δtr_M-seeded f all refuted.

## Appendix A — P6c executed: Galois-descent / GSWZ Frobenius-gluing scoping (U3)

**Status:** SCOPING ONLY (owner-selected 2026-07-11; no numerics, no Lean, no
c_k value). Dependency-gated on P1 (§3.A) — see kill criterion below.

Per GSWZ, "The Habiro ring of a number field" (arXiv:2412.04241): elements of
the Habiro-ring module attached to a number field K are collections of formal
power series, one at each root of unity, glued by a **Frobenius endomorphism**
after division by a gluing series determined by an element of the **Bloch
group** B(K). Applied to the Q_β element F(q):

1. **The field is forced, not chosen.** The framework's CAL-2 anchor is
   Vol(4₁) = 2Λ(π/3); the 4₁ trace field is ℚ(√−3) and its Bloch-group
   element is the class of the 4₁ shape parameter [ζ₆] ∈ B(ℚ(√−3)). If F
   lives in the GSWZ module for ℚ(√−3), its expansions at *all* roots of
   unity are determined by (i) the single q=1 series — i.e. the c_k data —
   and (ii) that forced Bloch-group element. Zero free choices, so this
   passes the C14 anti-fitting discipline.
2. **Compatibility with the KC registry (checked on paper):**
   - **KC6** (a₁ = −c₃ has a nonzero bar-odd part with nonzero q=1 shadow):
     the Bloch–Wigner function is odd (D(z̄) = −D(z)) while the Rogers
     L-side is even — the bar-odd/bar-even split of the c_k data mirrors
     the imaginary(volume)/real(CS) split of the dilogarithm at the
     Bloch-group element. Consistent, and independently suggestive.
   - **KC20** (bar-odd carrier is not a root-of-unity object; cyclotomic
     content exactly q²−1): consistent — Frobenius gluing constrains
     expansions *at* roots of unity; it does not force the carrier to *be*
     a root-of-unity evaluation.
3. **Formalize-first target** (before any numeric sweep): a §3b-cond
   conditional class `QBetaGSWZDescentClass` carrying (a) the q=1 series
   with c₂ = −1, (b) the Frobenius-congruence family on the integer
   coefficient sequence (exact congruence shape to be transcribed from
   arXiv:2412.04241 §-level statements before formalizing — not from this
   summary), no instance (open). The descent datum is then a *checkable
   arithmetic constraint* on the same integer coefficients P1 tests.
4. **Kill criterion / gate:** GSWZ descent **presupposes** Habiro
   integrality of the q=1 series. If P1 (§3.A) returns NEGATIVE on all
   natural normalizations, this route dies with it — record and stop. If
   P1 passes, the first executable descent test is the small-prime
   (p = 2, 3) Frobenius congruence on the integer coefficients.

## 5. Cross-references

- Refuted-class map: [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
- Registry (tiers + KC1–KC20): [`../coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
- Master ledger: [`../coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Keystone (merged F(q) axis): [`../coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- Missing modular double: [`2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`](2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md)
- Growth/pole data (KC8): PR #1727, #2445, #2611
