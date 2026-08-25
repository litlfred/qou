# Is KVC for 8₁₁ attackable with existing infrastructure?

**Date:** 2026-08-25 · **PR:** [#5765](https://github.com/litlfred/qou/pull/5765) · **Bean:** `qou-b5h9`

Owner question, after the KVC discharge survey found 8₁₁ the one genuinely open case
among the knots QOU takes volumes of.

## Answer: PARTLY — numerically yes, today. Provably no.

And the real numerical blocker is **not** compute, precision or memory. It is that the
**diagram convention is not pinned**, and scanning conventions against the volume is
measurably numerology.

## 1. Colored Jones DOES exist in the repo — three ways

The Markov trace on `H_n(q)` gives only N = 2, but that is not the only engine here.

| route | file | general? | root of unity? | verdict for 8₁₁ |
|---|---|---|---|---|
| **[Kas95] §3 planar state sum + tensor network** | `computations/kashaev_link_statesum.py` | **yes**, any PD code | **yes** | **works today** |
| `U_q(sl₂)` N-dim irrep braid rep | `whitehead_fast.py::closure_norm` | yes | yes | dense `N^m`; m=5 ⇒ N ≤ 5 |
| weight-block decomposition | `whitehead_weightblock_numeric.py` | reaches N ≈ 30–40 | yes | **hardwired to 3 strands**; 8₁₁ needs 5 |
| TL cabling (Rust) | `tl_cable{,_mpfr}.rs`, `wenzl_lr.rs` | N = 3..6 cables | **no — real q only** | unusable |

`kashaev_rmatrix.py` records *why* the state sum is the right object: the Kashaev
invariant is provably **not** an enhanced Markov trace (no diagonal-μ solution,
σ_min ≈ 2.45), so the `H_n(q)`/Hoefsmit/Gram machinery cannot reach it. The §3 state sum
carries face (angle) indices a braid trace does not have.

**Run on 8₁₁.** Baseline: `fig8_state_sum` reproduces the closed form exactly (N = 3,5,7
→ 13.00000 / 50.47214 / 151.27903). SnapPy's 8₁₁ PD traces to a valid planar diagram
(8 crossings, 16 edges, 10 faces, V−E+F = 2 ✓) and the evaluator returns values at every
prime N tested.

## 2. What SnapPy actually gives — measured, not assumed

SnapPy 3.3.2 standalone is **Sage-gated on every polynomial method**.

- **Works:** `volume` = 8.2863168178 ✓, `complex_volume`, `PD_code`, `braid_word`
  (5 strands, 14 letters), `bridge_upper_bound` = **2**, `seifert_matrix`, `writhe` = −4
- **`SageNotAvailable`:** `jones_polynomial`, `alexander_polynomial`, `determinant`,
  `signature`, `goeritz_matrix`, `invariant_trace_field_gens`

**SnapPy gives no colored Jones at any N** — not even ordinary Jones without Sage. It is
a volume oracle and a diagram source.

Derived from `seifert_matrix` via sympy: **det(8₁₁) = 27**, and with bridge number 2 this
makes **8₁₁ the 2-bridge knot b(27,10)**, continued fraction [2,1,2,3] — the same class as
Whitehead b(8,3), so `plat_to_pd` and the library's 2-bridge colored-Jones formula apply.

## 3. Size: cost is N⁶ and 8 crossings is nearly free

Measured via `np.einsum_path` greedy; exponent from N = 41 → 81:

| knot | crossings | opt FLOP @ N=81 | largest intermediate | exponent |
|---|---|---|---|---|
| 4₁ | 4 | 1.13e12 | 0.69 GB | **6.00** |
| Whitehead plat | 5 | 1.70e12 | 0.69 GB | **6.00** |
| **8₁₁** | 8 | 3.39e12 | 0.69 GB | **6.00** |

Treewidth is bounded for these 2-bridge diagrams, so **8₁₁ costs ~1.8× Whitehead at equal
N, not exponentially more** — crossing count enters linearly, not in the exponent.

Wall-clock (prime N): N=23 → 4.1 s, N=31 → 14.4 s, N=37 → 31.6 s. Extrapolating:
**N ≈ 61 ≈ 10 min, N ≈ 79 ≈ 50 min.**

**Precision is not the bottleneck.** complex64 vs complex128 diverge by only 1e-7…4e-6 up
to N = 21 — 1–2 digits lost to cancellation against complex128's ~14 of headroom. The
50–65 dps mpmath infrastructure is **not needed** for this object.

**Bug caught mid-run:** `_solve_mod` inverts via `pow(a, N-2, N)` (Fermat), valid **only
for prime N**. Composite N (9, 15, 21, 25, 27, 33, 35, 39) are silently wrong. All figures
above are primes-only.

## 4. THE BLOCKER — the convention is not pinned, and scanning it is numerology

`deficit_face_of` returns **None** (non-unique) for both the SnapPy PD *and* the plat from
CF [2,1,2,3]. The state sum is invariant only for a genuine two-strand-tangle presentation
with a pinned (strand-pair, outer-face, deficit-face) convention — the Whitehead docstring
records that a braid closure gave 144 distinct values at N = 7, *"no invariant."*

**Measured for 8₁₁: 1200 (strand-pair, outer-face) choices give 1184 distinct values at
N = 7**, growth spanning **[5.205, 15.623]**. With an arbitrary choice, growth sits flat at
~10.2–10.6 across every prime N from 11 to 37 — **not** 8.286.

**The numerology trap, quantified.** Of those 1200 conventions, against Vol = 8.2863:

| within | count | fraction |
|---|---|---|
| 10 % | 34 | 2.8 % |
| 5 % | 19 | 1.6 % |
| 2 % | 1 | 0.1 % |

**Scanning conventions against the volume will produce a "hit" by chance.** The convention
must be pinned by an **independent reference** — exactly as the Whitehead work insisted
(*"No number was asserted from a scan against the noisy volume — the reference is what
pins it"*).

## 5. A proof is NOT attackable — the obstruction is documented one crossing lower

From `library/ki6c/` (Ohtsuki–Yokota, 72 pp): Poisson summation → saddle point on a
potential `V̂(t,s,u)`. The hard step, in their words, is constructing a **concrete
homotopy** of the integration domain in ℂ³ so the new domain contains the critical point
while its boundary stays in `{Re(V̂ − ς) < 0}`. *"This part of the proof is quite
non-trivial."*

**It is not a recipe, and they state it fails:** *"we can not make such a homotopy for the
7₂ knot as shown in [21]."* **A known obstruction at seven crossings.**

Two references, neither settling 8₁₁:
- **[24] Takata, "…Kashaev invariant of SOME hyperbolic knots with 8 crossings"** — cited
  as *preprint / in preparation* in both library copies. **Whether 8₁₁ is among the "some"
  is UNVERIFIED** — not in the library, list not confirmable.
- **Ohtsuki–Takata, Geom. Topol. 19 (2015) 853–952** on two-bridge knots — covers 8₁₁'s
  *class* but proves the ω/torsion identification (the **second** coefficient), not VC.

**More decisive: the corpus's own proof technology has not closed the easier case.** QOU
proves VC by **squeeze**, which needs a manifestly **positive** sum:
- **4₁ succeeds** — `⟨4₁⟩_N = Σ_k ∏(2 − 2cos(2πj/N))` is manifestly positive
  (`tendsto_log_kashaev_vol`, the one machine-proved case).
- **Whitehead does not** — its outer sum carries phases. **3,556 Lean lines across 8 files,
  two independent programmes, both still open on exactly that gap** (`VdVWhiteheadLemma4`,
  no instance).
- **8₁₁ has no positive-sum form at all**, and `kashaev_link_statesum.py` already records
  that cutting the TN at any single edge does **not** produce one.

So the repo cannot close a case that has a *published* proof and a positive sum. 8₁₁ has
neither, plus a method that fails at 7₂. **A proof needs new ideas — a paper, not a recipe
application.**

*Scope (a):* not a claim that 8₁₁ KVC is unprovable or the saddle route excluded — only
that no route in this corpus reaches it as configured.

## 6. Does QOU need it? Weakly — and a volume justification would be circular

**The ³H → 8₁₁ assignment is not derived.** Same `conj:canonical-knot-id-sdp` as the 6₂
deuteron assignment, whose own text says *"historical volume matching originally proposed
these assignments"* — and which
[`2026-08-25-knot-id-is-an-admitted-fit.md`](2026-08-25-knot-id-is-an-admitted-fit.md)
shows was AME-driven census fitting. **So justifying it by volume is circular: the knot was
selected because its volume matched.**

Applying the documented `ρ_F ∈ {m_e, 2m_e}` rule (`ρ = {1,2,2}`):

| nucleus | knot | ρ_F | prediction | B_AME | error |
|---|---|---|---|---|---|
| ²H | 6₂ | m_e | 2.2488 | 2.2246 | **+1.090 %** |
| ³H | **8₁₁** | 2m_e | 8.4686 | 8.4818 | **−0.156 %** |
| ³He | L6a4 | 2m_e | 7.4889 | 7.7181 | **−2.969 %** |

> **Note against a misreading I nearly published.** Bare `m_e·Vol` gives ratios 0.4992 and
> 0.4852 at A = 3 — an apparent unexplained factor of 2. **It is not an anomaly:** it is
> the `ρ_F` rule, which the source calls a *"truly derived piece … identified as
> `ρ_F = ν_SDP`"* — though that identification is itself per
> `conj:kashaev-density-equals-sdp-multiplicity`, i.e. conditional on another open
> conjecture.

Eleven live consumers import `binding_link_volumes`, but they consume Vol(8₁₁) as a
*number*, independently certified by SnapPy. KVC would be load-bearing only if the
framework needs `Vol = τ_arch(Vol_q)` **at 8₁₁** — and per
[`2026-08-25-atom-word-closures-are-not-hyperbolic.md`](2026-08-25-atom-word-closures-are-not-hyperbolic.md)
that route yields 0 there regardless.

**Proving KVC for 8₁₁ is premature** while the assignment it would support rests on an
open conjecture seeded by volume matching.

## Recommendation (judgement, not a finding)

**Do not attack the proof.** Do the numerics only with the convention pinned properly:

1. **Generalize `norm_weightblock` from 3 strands to arbitrary `m`.** Small, well-defined,
   and the *only* thing between us and an independent reference. It also unlocks colored
   Jones for every 5-strand knot in the atlas.
2. **Pin the 8₁₁ state-sum convention against that reference** at N = 3,5,7,9,11 — **never
   against the volume**. The 19-in-1200 measurement is why.
3. **Only then** run the tower to N ≈ 61–79 (10–50 min) and Richardson-extrapolate. Expect
   ~1 % — a **two-significant-figure numerical check, not a proof.**
