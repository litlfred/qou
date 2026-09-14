# The 1D sector, and why the missing extensive term and the missing dimension are one gap

**Date:** 2026-09-14 · **Beans:** `qou-ifto` (milestone), `qou-5scj`, `qou-dz1h`, `qou-9ven` ·
**Issue:** #7367 · **PR:** #7372

## Summary

The session opened from the premise *"QOU has 2D and 3D mechanics; add 1D."* Measured, the
premise is backwards, and correcting it is the useful part. The corpus's best-developed,
Lean-proved, dimension-explicit mechanics **is** one-dimensional; 2D and 3D are what is missing.
Three findings follow, and the third joins two arcs that have not been put side by side.

## 1. The corpus is already 1D, from two directions

**The layout.** `lean/QOU/Mass/SurfaceExponentIsDimension.lean` carries the section heading
*"The production word is one-dimensional, and this is exact"* and fixes the exponent `p = 1`,
"the `d = 1` case". `lean/QOU/Mass/LinearLayoutNoBulk.lean` (sorry-free) proves the coordination
graph of every word the nuclear encoding can produce is a linear layout: `degree_le_two`,
`not_linearLayout_of_degree_ge_three`, `card_edgeFinset_le`. `StrandLayoutForcesChain.lean` adds
that *"the chain is forced by the layout, not selected among bond sets."*

**The algebra** — not previously stated in the corpus. Convention D is the SU(2)/Temperley–Lieb
trace (`computations/y_lambda_su_n.py` docstring; `FibreDimensionForcesTL.lean` proves
`z·[N]_q = q^N`, giving `z_D = q³/(q²+1)` at `N = 2`). Measured at `mp.dps = 60` in
[`computations/onedim/tl_is_the_xxz_chain_probe.py`](../../computations/onedim/tl_is_the_xxz_chain_probe.py)
(17/17), that algebra **is** the open `U_q(sl₂)`-symmetric XXZ chain:

```
-2 * sum_i e_i  =  H_XXZ - Delta*(n-1)*I - ((q - 1/q)/2)*(sz_1 - sz_n),   Delta = (q + 1/q)/2
```

verified `n = 2,3,4,5`, at both documented pins. `Δ = 1.005448433353561` (proton) /
`1.005448434567581` (muon) — 1.2 ppb apart, so the verdict is pin-independent. `Δ > 1` is the
massive, Ising-like regime, where Bethe strings are stable bound states. **Derived, not fitted:**
`Δ = cosh(log q) > 1` for every real `q ≠ 1`, so it is forced by the substrate being a genuine
deformation, with no calibration input and no free parameter
(`QOU.OneDim.one_lt_anisotropy`, sorry-free).

**What is genuinely absent is 2D and 3D.** 2D is explicitly disclaimed at
`braids-and-knots/categorical-braiding-intro.md` (*"This algebraic structure precedes any
geometric realisation"*); 3D is ambient-only (`markov-trace-ambient-s3.md`: *"constructed
categorically as the target of the Alexander–Markov correspondence, rather than posited
geometrically upstream"*); and `d` is never a Lean binder anywhere — `q-navier-stokes.lean`
carries `dim : Nat := 3` as a default field no theorem varies. The descent ladder has written
rungs at `dim M_k = 1` and `= 0` and none at 2 or 3.

## 2. The `b₃` sign requirement constrains a family, not one-dimensional binding

`UrsellPartitionFunctionB3.lean` fixes the cluster partition function as a **product over pairs**,
`Z_S = ∏_{e ⊆ S} f_e`, and proves `b₃ = −φᵀ₃`; on the A=3 chain `φᵀ₃ = g₀₁·g₁₂`, so `b₃ > 0`
requires exactly one bond above 1 — the sign-mixed condition of `qou-q8vl`.

[`computations/onedim/string_vs_bond_product_probe.py`](../../computations/onedim/string_vs_bond_product_probe.py)
(7/7, exact rational arithmetic) reproduces that — both-repulsive `−1/8`, both-attractive `−3/8`,
sign-mixed `+1/4` — and then measures what it does not settle. The exactly soluble 1D case reaches
a positive three-body term at a **single uniform coupling with no sign mixing at all**: the
`n`-string binds `n(n²−1)/12`, so at `n = 3` the excess over the pairwise chain is `+2ε`.

The invariant: **the log of a product over bonds is a sum over bonds**, so on a chain the log
assembly is affine in `n` for every bond assignment whatever (constant first difference, checked
at six bond values), while the string law is genuinely cubic (constant non-zero third difference).
The ratio string/pairwise-chain is exactly `n(n+1)/6` — unbounded, so no bond value rescales it.

Two routes to `b₃ > 0` therefore exist: **(a)** stay inside the family and find `f_e > 1` — the
corpus's current search, blocked at both derived bond families (production letters `d ≤ 0`;
isospin projectors `μ₊ + μ₋ = 1`); **(b)** leave the family — unexplored. This does not establish
that (b) applies to nucleons. It establishes that **(a)'s blockage is not evidence against (b)**.

Scope-(b), invariant = bond-product factorisation.

## 3. The convergence: the candidate extensive term needs a 3-cell, and the chain has none

`CrossedModuleSurfaceHolonomy.lean` (bean `qou-20bk`, route D's first prune) proves that the
kernel of the crossed-module feedback is central, hence that no 2-dimensional Yekutieli object
carries a non-abelian many-body term beyond word ordering. It then names the one candidate that
survives, in its own words:

> "the only 3-body-shaped object in the book is the abelian volume term `∫γ` over a **3-cell** —
> which is additive over 3-cells (extensive), exactly the *super-pairwise additive extensive
> object* the Δ_λ audit asks for, **if** `γ ≠ 0` for the framework's connection."

and records that `γ ≠ 0` "cannot be evaluated: the framework's Step-2 curvature is stipulated,
not a form."

A 3-cell needs three mutually incident sites.
[`QOU.OneDim.no_triangle`](../../content/quantum-observable-universe/lean/QOU/OneDim/NoThreeCellOnTheChain.lean)
shows a linear layout has none: adjacency forces consecutive indices, and three indices cannot be
pairwise consecutive.

**So the corpus's one identified candidate for the missing extensive term is structurally
unavailable on the corpus's own production geometry** — not blocked by the unevaluated `γ ≠ 0`,
but by there being no 3-cell to integrate it over.

This is a second, independent obstruction, and it is the cheaper one to act on. `γ ≠ 0` is a
question about a stipulated curvature; this is a question about the layout — and
`LinearLayoutNoBulk` already closes its own docstring with *"a bulk needs a non-linear layout, and
the corpus derives no such layout."* **A bulk is a 3-cell.** The missing extensive term and the
missing dimension are the same gap, reached from two directions that had not been connected.

Scope-(b), invariant = the linear layout; it inherits exactly `LinearLayoutNoBulk`'s scope and
widens it by nothing. It says nothing about what layout the physics wants, nothing about whether
`γ ≠ 0`, and it is **not** an argument that the extensive term does not exist — it locates where
it cannot be found.

## What this does not claim

- Nothing here identifies the sites of the chain with any physical object.
- The TL↔XXZ matrix assembly is verified numerically, not formalised; the Lean covers the scalar
  identities it rests on. Both the Lean docstring and `rem:tl-is-the-xxz-chain` say so.
- The XXZ `n`-string band energy is deliberately **not quoted**; measuring it by momentum-resolved
  exact diagonalisation is bean `qou-6b9y`, not done here.
- No comparison to the ultracold-cesium measurement is made. [arXiv:2505.10550](https://arxiv.org/abs/2505.10550)
  is what prompted the question; it is not evidence for anything above.

## Three corrections made in the course of this work

**A `q₀` derivation.** The proton pin was first computed by applying the *muon* relation
`m_μ/m_e = Vol(4₁)/ℏ_q²` to the proton ratio, giving `1.0344`. The proton pin has its own
defining identity (`m_p/m_e = 2(Vol/ℏ_q²)·F_Bor − 12`). Both pins are now computed from their own
identity via `q_at` / `q_muon_at`; the proton value round-trips `m_p/m_e` to all quoted digits and
the muon value reproduces the anchor witness digit-for-digit.

**Three Lean statements were false, not merely unproved.** `twoMul_eq`, `twoInv_eq` and
`tlLoop_add_heckeH` were stated over a bare `Field R`, where `2` need not be invertible. Mathlib's
`0⁻¹ = 0` convention makes the failure silent: in characteristic 2 every `x/2` collapses to `0`.
`lean -DautoImplicit=false -s 65536` caught it at exit 1, and the negations are witnessed over
`GaloisField 2 2` and — for `tlLoop_add_heckeH` — already in `ZMod 2` at `q = 1`. Fixed by adding
`(h2 : (2:R) ≠ 0)`, the honest signature for a statement about halving. Re-verified exit 0, all
`sorryAx` gone.

**A third statement was vacuous and is deleted.** The same file first carried
`threeCell_weight_vanishes : ∀ w, … → w a b c = 0`, on the reasoning that the `∀ w` showed no
choice of curvature could evade the obstruction. That defence is wrong. Its hypotheses are exactly
the ones `no_triangle` proves unsatisfiable, so every instance is vacuously true — and the mutant
test is decisive rather than a matter of taste: the *identical* hypotheses also prove
`w a b c = r` for arbitrary `r`, and prove `0 = 1`. Both mutants compile, and Lean's own
`unused variable 'w'` warning fires on them, because `w` never enters the proof. So the conclusion
`= 0` was not distinguished by the theorem; the `∀ w` sat outside the vacuity rather than
protecting against it. The intuition is real and is carried in full by `no_triangle` alone: there
is no 3-cell **at all**, independently of any weight. Deleting it costs the file's thesis nothing.

This one was caught by asking for it adversarially. It is the shape AGENTS.md §3b-cond names — a
carrier whose "theorem" merely projects an assumption — and it would very likely have reached a
reviewer otherwise.

Worth recording: `one_lt_anisotropy`, the declaration flagged in advance as most likely to fail,
was green with clean axioms throughout. The failure was entirely in the section expected to be
safe, and **a bare `lean` would not have caught it** — the `-DautoImplicit=false` flag was
confirmed live with a two-sided control before the verdict was trusted.

## Open, in priority order

1. **`qou-9ven`** — write the `dim M_k = 2` and `= 3` descent rungs, and make `d` a real binder.
   The shape suggested by §3 is that `d` enters through `∂Σ`: at `d = 3` the surface has knotted
   boundary (the live mass theory); at `d = 2` it is closed, so the surface holonomy is purely
   central; at `d = 1` it degenerates to `M_k` (written); at `d = 0` there is no surface (written).
   **This is a proposal, not a derivation** — it is what the existing rungs plus the Stokes
   reduction suggest, and it has not been checked.
2. **`qou-dz1h`** — whether route (b) of §2 applies to nucleons.
3. **`qou-6b9y`** — the XXZ `n`-string band by momentum-resolved ED.
4. **`qou-st2v`** — disambiguate "one-dimensional". **Measured**, not estimated, by
   [`computations/audits/one_dimensional_sense_audit.py`](../../computations/audits/one_dimensional_sense_audit.py):
   **773 hits** across `content/`, `lean`, `computations/` and `docs/`.

   | sense | hits | share |
   |---|---|---|
   | representation / Wedderburn block | 408 | 52.8 % |
   | **no marker disambiguates it** | 286 | 37.0 % |
   | **spatial** | **36** | **4.7 %** |
   | ambiguous (spatial *and* rep markers) | 27 | 3.5 % |
   | seminormal channel | 16 | 2.1 % |

   **It is four senses, not three** — the fourth is plain linear-algebraic dimension
   (*"`HH² ≅ k` is one-dimensional"*, *"the outer derivation space is one-dimensional"*), which is
   neither spatial, nor a Wedderburn block, nor a seminormal channel. The audit now buckets it
   explicitly (`LINALG`).

   **🛑 And the alarming reading of that table is WRONG — it was mine, and I repeated it three
   times before catching it.** I wrote that "a reader meeting the phrase should assume it is not
   spatial", on the strength of the 37 % bucket then labelled `UNCLASSIFIED`. That label meant
   *the classifier's regex had no marker*, **not** *a reader cannot tell*. Three separate samples
   of it turned out to be plainly clear linear-algebraic and representation uses
   (`Λ²ℂ² ≅ ℂ (one-dimensional)`, `binom(dim V, 2) = 1`, `the pretzel state integral is
   one-dimensional`). The bucket is renamed `NO-MARKER` so the next reader is not misled the same
   way.

   **The number that actually matters is the qualified/bare split**, and it says the corpus is
   fine: **526 of 773 uses carry a disambiguating noun directly after the phrase** — `block`,
   `channel`, `representation`, `irrep`, `Wedderburn` — and are ambiguous to nobody. Of the 254
   bare uses, most are still clear from their own sentence, and the genuinely **spatial** bare
   uses number about **four**.

   So there was no pervasive ambiguity to sweep, and sweeping 773 sites would have been churn.
   What was missing was an **authoring rule**, now recorded in
   [`notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md):
   write the spatial sense as `dim M_k = d` or qualify it in words, because it is the rarest sense
   and a bare use in *new* prose will be read as one of the other three. The other senses need no
   change — the noun already carries them.
