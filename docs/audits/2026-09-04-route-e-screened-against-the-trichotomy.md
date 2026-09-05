# Route E (PGL(3) higher Teichmüller), screened against the Sym² trichotomy

**Date:** 2026-09-04
**Beans:** `qou-960k` (route E), `qou-52fu` (T3e, completed 2026-08-04),
`qou-8pl3` (N = 3 routes), epic `qou-2q85`
**Lean:** `QOU/Eightfold/AmbientInvolutionDoesNotDecideType.lean`
(sorry-free, `lean`-direct exit 0 in 3.5 s, axioms `[propext, Quot.sound]`)

## 0. What this is

Route E — a `PGL(3,ℂ)` decoration of the knot complement, `ρ₃ : π₁(M) →
PGL(3,ℂ)`, as the geometric source of a rank-2 structure — was the last live
route on epic `qou-2q85` and the only one aimed at *flavour* `SU(3)_f`.

It already had an assessment:
[`docs/audits/2026-08-04-pgl3-higher-teichmuller-assessment.md`](2026-08-04-pgl3-higher-teichmuller-assessment.md).
This one does not replace it. It runs route E through a screen that did not
exist when that audit was written, and reports what the screen returns.

**The corpus-grep found that audit before this one was written.** That is worth
saying because the alternative was a duplicate assessment: the fourth time this
session that reading the corpus's own prior work replaced a fresh derivation.

## 1. The screen route E has to pass

`Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three` (sorry-free, 2026-08-26)
proves that a three-dimensional object passing the `Sym²` gate **must contain a
complex-type irrep** (`FS = 0`, `X ≇ X̄`). Real and quaternionic constructions
are excluded *as a class* — real multiplicities are forced to zero, quaternionic
dimensions are even, the total is even, and `3` is odd.

So a route to the flavour triple owes exactly one thing, and it is checkable:
**a three-dimensional object of complex Frobenius–Schur type.**

## 2. What the 2026-08-04 assessment claimed, and why it does not survive

§2c of that audit gives route E's reason for clearing the bar:

> The resulting 3-dim fundamental would be non-self-dual (`PGL(3)` is rank 2
> with non-trivial outer automorphism).

**The premise is about the ambient group; the conclusion is about one
representation.** `PGL(3)` carries its outer automorphism whatever `ρ₃` does,
and a representation's Frobenius–Schur type is a property of the
representation. Concretely: `SO(3) ⊂ PGL(3,ℝ)` has a three-dimensional standard
representation of **real** type, and `real_triple_fails_gate` kills it in one
line — while `PGL(3)` still has the outer automorphism.

`AmbientInvolutionDoesNotDecideType.fsType_not_determined_by_dual` makes this a
theorem in the corpus's own model of the gate: over **one fixed** duality datum
(a fixed-point-free involution on the index set — the model's stand-in for the
outer automorphism) there are two three-dimensional candidates, one passing the
gate and one failing it. The ambient involution does not decide gate passage.

This is the arity/scope conflation `AGENTS.md` §"Grep the claim SHAPE" names,
applied to a *positive* claim rather than a negative one.

## 3. What that does and does not do to route E

**It is not a refutation, and it is not evidence against the route.** Scope-(a)
throughout. What it removes is a *reason for confidence*, and what it leaves in
its place is an obligation that can be discharged by computation:

> exhibit `ρ₃ : π₁(S³∖K) → PGL(3,ℂ)` with `ρ₃ ≇ ρ̄₃` — an image not conjugate
> into a real form — for the knots the particle dictionary actually uses.

`selfDual_candidate_not_three` is that screen in the form a route can be held
to: a candidate whose occurring irreps are all self-dual cannot be
three-dimensional and pass, whatever the ambient group's outer automorphism
does.

**One consequence is immediate and prunes half the route.** The classical
higher-Teichmüller object — a `PGL(3,ℝ)` Hitchin representation of a surface
group — lands in the self-dual sector and is excluded. The surviving branch is
the `PGL(3,ℂ)` gluing-equation one. Which is, as it happens, the branch the
corpus actually holds sources for (§4).

## 4. What is on disk — and a correction to `qou-960k`

`qou-960k` records "35 library dirs on quantum Teichmüller, ZERO content blocks"
and reads it as *35 held sources for the rank-2 route*. Re-measured
2026-09-04, that reading is wrong in a way worth fixing:

| measured | count | what it is |
|---|---|---|
| `library/` dirs matching "quantum Teichmüller" | 35 | the **rank-1** (`PGL(2,ℂ)`) quantisation the corpus already uses — Baseilhac–Benedetti, state integrals, Faddeev dilogarithm |
| `library/*/sections/` dirs matching Fock–Goncharov (case-insensitive, hyphen or space) | **4** | `arxiv-1204.4824v2`, `arxiv-1207.6711v1`, `arxiv-2304.12545v1`, `hyperbolicandneumann` |
| of those, on-point for `PGL(n,ℂ)` | **1** | `arxiv-1207.6711v1` = Garoufalidis–Goerner–Zickert, *Gluing equations for `PGL(n,ℂ)`-representations of 3-manifolds* — 109 occurrences of `PGL(n, C)`; the other three mention it once each |

So the held body is for the rank-1 machinery, and the rank-2 route has **one**
substantive held source, not thirty-five. The count in `qou-960k` was not wrong;
the inference from it was.

**A false positive to not repeat.** A `summary.json`-level grep for "Fock"
returns `arxiv-1106.2975v1` (*The Polyanalytic Ginibre Ensembles* — Fock
*space*) and `arxiv-1611.09182v1` (*Standard model physics from an algebra?*).
Neither is Fock–Goncharov. The `sections/`-level grep for the full name is the
one to run.

**Not measured:** `library/*/ocr/` (25 dirs carry one, and a `sections/` grep is
blind to them) and the PDFs. `corpus_search` (path 0) unavailable for a fifth
session.

## 5. Where this leaves epic `qou-2q85`

Routes A, B, C and D are closed or non-crossing (`qou-ox7v`, `qou-jopk`,
`qou-wjbd`). Route E is **still live** and is now the only one, with its stated
rationale replaced by a checkable obligation rather than removed. The next
honest step on it is a computation, not a derivation: `PGL(3,ℂ)` representations
of the trefoil, figure-eight and Borromean complements, with the Frobenius–Schur
type of each read off. The 2026-08-04 audit's §3 recommendation — *"becomes
actionable if/when someone computes `PGL(3)` representations for the trefoil,
figure-eight, and Borromean links"* — is unchanged by any of this, and is now
the *only* thing route E is waiting on.

Two obstructions that audit records still stand and are not addressed here: not
every knot complement admits a `PGL(3,ℂ)` structure, and the trefoil complement
is Seifert-fibred rather than hyperbolic.
