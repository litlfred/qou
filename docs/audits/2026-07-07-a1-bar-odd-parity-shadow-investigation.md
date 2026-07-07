# Investigation: is the kernel coefficient `a₁ = −c₃` exactly bar-odd? (the T3-2 tension on the merits)

**Date:** 2026-07-07 · **Branch:** `claude/z-c-k-f-map-keystone-ub5yix` (PR #3449)
· **Trigger:** owner declined to rule by fiat on the T3-2 tension ("not sure /
actually investigate"); this audit traces the "a₁ bar-odd" claim to its sources
and determines what the corpus actually establishes.
· **Discipline:** no tier change, no wiring; one docstring clarification to a
conditional Lean lemma (no mathematical content changed).

## 1. The tension (proved, reading-agnostic)

`ZBarParity.lean` §5 (`fixed_eval_two_mul_kills_bar_odd`,
`shadow_carried_by_even_part`, sorry-free): any bar-compatible evaluation —
in particular the q=1 evaluation, which the bar involution fixes —
annihilates exactly-bar-odd elements. So the conjunction

- (A) `a₁ = −c₃` is **exactly** bar-odd (pointwise), and
- (B) `a₁` is q=1-regular with nonzero shadow (`c₃ → −2 = J_Hopf(1)`, the
  preflight gate §4(c))

is **jointly impossible**. At most one of (A), (B) can survive.

## 2. Tracing (A) to its sources — what is actually established

| source | what it actually proves/records | exactly-odd? |
|---|---|---|
| [`QBetaReebSinhParity.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaReebSinhParity.lean) (PR #1887) | `cosh(kη)` bar-even, `sinh(kη)` bar-odd, and the **bar-antisymmetric PART** of `a·cosh + b·sinh` is `b·sinh` — component-level parity algebra. The docstring calls c₃ "the first bar-antisymmetric coefficient", citing PR #1866. | **No** — a statement about *parts*, not about c₃ pointwise |
| PR #1866 ("even slice empty") | the even slice `cos(√2·u)` reproduces c₂ = −1 but gives **c₃ = 0**; a nonzero c₃ requires odd content (`Φ₂ ≠ 0` in the #1887 phase reframe `c₃ = −Φ₁Φ₂`) | **No** — this is *rung*/phase parity ("c₃ needs an odd ingredient"), not pointwise bar-antisymmetry of c₃ |
| [`QBetaCKRecursionKernelConstraints.ck_a1_bar_odd_of_c3_odd`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean) | **conditional**: *IF* `∀η, c₃(−η) = −c₃(η)` *THEN* `a₁` is odd. The exactly-odd antecedent is a hypothesis, imported from the #1887 swing narrative — proved nowhere | **No** — hypothesis-carrying |
| [2026-06-13 heat f-map audit](2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md) §1 | the heat-route `a₁ = κ_{(2,1)}(q)·S` with `κ_{(2,1)}` **exactly bar-odd** (sympy-exact; Lean-certified on this branch) | **Yes — but for a different object** (see §3) |
| Cross-anchor swing (`dc₃/dη ≈ 4.26×10⁶`) | the *extracted* c₃ differs 2.4% between anchors ~1e-8 apart in q₀ — but PR #1821 proved this slope **impossible for any smooth real f**, which is precisely why c₃ was refuted as a real-q element and moved to the fibre level | **No** — pointwise real η-parity statements about c₃(η) are ill-posed by the corpus's own #1821 verdict |

**Finding 1.** No source establishes (A). The exactly-odd premise entered as
a conditional hypothesis and was propagated by shorthand ("a₁ bar-odd") into
constraint lists — including this branch's own K2 gates.

**Finding 2 — symbol overloading (the registry §2 disease, new instance).**
There are **two distinct `a₁` objects**:

| object | parity | q=1 value | magnitude at q₀ |
|---|---|---|---|
| **heat-route `a₁`** = `κ_{(2,1)}·S` (2026-06-13 audit) | exactly bar-odd ✓ | `0` (κ has the `(q−1)³` factor) — **consistent** with odd | ~1e-3 (Stage B, 1ppQ ledger cont. 19: "\|a₁\| ~ 1e-3 vs √2·Φ₂ ≈ 2.069" — the per-mode refutation) |
| **kernel `a₁`** = `−c₃ = √2·Φ₂` (conditional lemma `ck_a1_eq_neg_c3_depth_two`) | **not established** | shadow `2 ≠ 0` (gate §4(c)) | ≈ 2.07 |

Stage B already recorded the 2000× magnitude mismatch when it refuted the
per-mode identification; the *parity* attribute of the first object was
nonetheless transferred to the second without the (never-constructed)
normalization bridge. The T3-2 tension is this transfer made visible.

## 3. What the fibre level says (consistency check)

At the fibre level (Habiro ring; the AGENTS.md "Im(q) at fibre vs observable
level" wall), "bar-odd" means the (−1)-eigenspace of the algebraic bar
involution — and the §5 fixed-point lemma applies verbatim (it is stated over
generic rings): an exactly-odd fibre element has zero q=1 (ε₁) evaluation.
So even fibre-level exact oddness of c₃'s element would force abandoning the
§4(c) shadow gate as stated. The gates cannot keep both; the corpus's own
usage (every candidate since 2026-06-04 was screened by `c₃ → −2` at q=1)
has *de facto* treated (B) as binding, not (A).

## 4. Verdict (evidence-based, not a fiat ruling)

1. **(B) stands; (A) falls to the odd-PART reading.** The established
   content is: *c₃ requires a nonzero odd ingredient* (`Φ₂ ≠ 0`, #1866/#1887)
   and *the anchor-swing component of the extracted c₃ is the odd channel's
   signature*. The corpus nowhere proves c₃ (or kernel `a₁`) exactly
   bar-odd, and its own §4(c) gate presupposes the opposite.
2. **Parity gates should therefore test the odd part; shadow gates the even
   part** (`shadow_carried_by_even_part`). Concretely, for I-B step B2: the
   induced kernel's `a₁`-slot must have **nonzero bar-odd part** (not: be
   exactly odd), and its bar-even part carries the `→ 2` shadow.
3. **[SUPERSEDED on the mechanism — see the
   [P-C15 correction audit](2026-07-07-pc15-a1-transcription-error-correction.md):
   the "non-monomial covariance" was a transcription-error artifact; the slots are
   exactly bar-even, T1's D(q) is exactly bar-odd (SURVIVOR), and verdict items 1–2
   are strengthened.]** Original text: **The K2 kill of c4qz/T1 survives re-examination** — those gates tested
   "bar-odd up to monomial twist", and the raw/pair-symmetrized slots failed
   even the weaker requirement of *clean parity decomposition with monomial
   twists*; under the odd-part reading the operative question becomes whether
   the slot's odd part is well-defined and nonzero, which the non-monomial
   covariance still obstructs at the pointwise level. I-B remains the route.
4. **Docstring clarification applied** (this PR) to
   `ck_a1_bar_odd_of_c3_odd` (conditional lemma, no math change): its antecedent is a
   modelling hypothesis, not established; see this audit.

**Owner sign-off requested** on verdict items 1–2 becoming the standing
reading (they only re-scope prose/gates; no Lean statement changes, since
the Lean was conditional all along).

## 5. Cross-references

- Fixed-point lemmas: [`ZBarParity.lean` §5](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean)
- Tension discovery: T3 witness [`qbeta-t3-carrier-q1-order-preflight.witness.json`](../../computations/qbeta/qbeta-t3-carrier-q1-order-preflight.witness.json)
- Ledger: [`z-ck-fmap-keystone.md` §4-ter](../coordination/z-ck-fmap-keystone.md)
- Smooth-real refutation making pointwise η-parity ill-posed: PR #1821
- Registry symbol-overloading precedent: [`ck-dk-canonical-registry.md` §2](../coordination/ck-dk-canonical-registry.md)
