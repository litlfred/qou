# The eightfold live surface has collapsed to one question — and T3g's stand-down is void

**Date:** 2026-08-07
**Epic:** `qou-8lxd` (eightfold way / SM derived from QOU); this session's child epic `qou-8p1x`
**Trigger:** four scope-(b) exclusions landed today, one of which retires the route that two other beans deferred to.

---

## 1. The currency problem, stated first

`docs/audits/2026-08-04-tannakian-gerbe-flavor-assessment.md` (T3g, bean
`qou-y7vg`) closes with:

> The S₄ bridge / Fano route (T3h) is more concrete and testable.
> Mark as **documented** and lower priority.
> **The Fano/S₄ route subsumes the structural content of this bean.**

**That rationale is now void.** Today's `s4_marked_pair_obstruction.py` excluded
the S₄/Fano bridge as a **scope-(b) structural exclusion**: the pinch supplies
an S₄-stable pair of marked points, and S₄ has *no orbit of size ≤ 2* on ℙ²
(both the 3-dim rep of S₄ and its restriction to A₄ are absolutely irreducible),
so no smooth plane quartic carries such a pair. And
`s4_genus3_pencil_infinite_family.py` showed the S₄ datum admits an infinite
pencil of genus-3 curves, so it has essentially no selecting power.

T3g deferred to a route that no longer exists. It is not "subsumed" — it is now
the **surviving** direction, and should be re-prioritised accordingly.

This is the same failure mode caught earlier today in the eightfold chapter
prose (which described the S₄ bridge as failing against "at least one other
genus-3 curve" after the pencil result had superseded that): an assessment
written before a downstream result, left pointing at a conclusion that has since
moved.

## 2. What today's exclusions did to the board

| Route | Status after today |
|---|---|
| S₄ / Fano bridge to Klein (T3h) | **excluded**, scope-(b) — marked-pair obstruction |
| "4-form degenerates" → Spin(7) → G₂ → SU(3) | **excluded**, scope-(b) — no open GL(8)-orbit on Λ⁴(ℝ⁸); Cayley locus is codim 27 |
| Re-tune the Ocneanu parameter to N = 3 | **excluded**, scope-(b) — the N=2 and N=3 traces are not proportional |
| Some summand of `V^⊗n` as the triplet | **excluded**, scope-(b) — every SU(2) rep is self-dual, so none passes the Sym² gate |
| Tetraplectic / quaternionic | supplies **SU(2)**, already spent on electroweak; vacuous at `m = 1` |
| Octonionic G₂ (status quo) | works, but **unearned** — empty `uses[]`, no `def:octonion-algebra` in the corpus (`qou-8fl1`) |
| **Non-neutral Tannakian gerbe (T3g)** | **the surviving direction** — see §3 |

## 3. Two beans are the same question

`qou-8p1i` (T3b, "multi-fibre groupoid") asks for *inequivalent fibre objects*.
`qou-y7vg` (T3g) asks whether QOU's braided category admits *inequivalent fibre
functors*, i.e. a non-neutral Tannakian gerbe.

Today's Sym²-gate result forces them together. Since **no summand of any tensor
power of the 2-dimensional fibre can pass the gate** — all SU(2)
representations are self-dual — T3b's "inequivalent fibre objects" *cannot* mean
"different summands of `V^⊗n`". It must mean genuinely non-isomorphic fibres.
That is exactly T3g's question.

Likewise the Ocneanu result: an N = 3 flavour channel cannot be the same trace
re-tuned, and since the Ocneanu parameter is the fibre's quantum dimension
(`Σ_λ f^λ s_λ(1,q,…,q^{N−1}) = [N]_q^n`), it must be the categorical trace on a
genuinely 3-dimensional object. Same requirement again.

**Three independent threads all terminate on the same requirement.** The
eightfold programme's live surface is one question:

> **Does QOU's braided category admit inequivalent fibre functors?**
> Equivalently: is `H¹(base, Aut^⊗)` non-trivial, and can the resulting gerbe's
> band be SU(3)?

## 4. What T3g already established, and what it did not

Worth preserving, because it is real and it constrains the answer:

* **The naive route is dead** (T3g §4). Permuting 3 fibres gives S₃, whose
  natural 3-dimensional representation is a *permutation* representation. Every
  permutation representation is self-dual — the permuted basis is orthonormal
  for an invariant symmetric form, so Frobenius–Schur is `+1` and `Sym²`
  contains a singlet. It fails the same gate, for the same reason the SU(2)
  adjoint does. S₃ = W(A₂) supplies the *Weyl group* of the weight lattice, not
  the fundamental representation.
* **The obvious twisting does not match** (T3g §5). A non-neutral gerbe with
  band SU(3) would want a fibre functor over a degree-3 extension, with the
  Galois group acting by outer automorphisms. But `Out(SU(3)) = ℤ/2` (complex
  conjugation, `3 ↔ 3̄`), not `ℤ/3`. A degree-3 extension alone does not
  naturally produce the required twist.

What T3g did **not** establish is that no gerbe works. §5 rules out one specific
construction — degree-3 extension twisted by outer automorphisms — and §7 then
stood the bean down on *priority* grounds (deferring to S₄/Fano), not on
mathematical ones. With the priority rationale void, the mathematical question
is untouched and open.

## 5. Recommended next step

Re-prioritise `qou-y7vg` and merge its scope with `qou-8p1i`. The concrete first
question, and it is sharper than "construct a gerbe":

> **Is `Out(SU(3)) = ℤ/2` an obstruction to *every* gerbe route, or only to the
> degree-3-extension one?**

The `ℤ/2` is suggestive rather than merely inconvenient: it is exactly the
`3 ↔ 3̄` conjugation, and the framework already carries a `ℤ/2` of its own — the
bar involution `q ↦ q⁻¹`, whose bar-even/bar-odd decomposition runs through the
`Q_β` and `c_k` work and whose Type-B folded fixed points are the
bar-invariant normal forms (`AGENTS.md` §7b).

**Stated as a question, not a claim.** "Both are ℤ/2" is precisely the kind of
coincidence the anti-laundering discipline exists to catch — the same trap
flagged for the characteristic-2 idea in `qou-8p1j`. What would settle it is a
map, derived from the substrate, under which the bar involution acts as the
outer automorphism of the band. Absent that, record it as an open lead and do
not wire it.

A refutation would be equally valuable: showing the bar involution *cannot* be
the band's outer automorphism would close the last live route, at which point
the honest corpus position is that colour and flavour SU(3) are **imported**
symmetries, and the chapter should say so plainly rather than leave several
dead routes reading as live.
