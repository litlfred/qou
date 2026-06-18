# Lean link-invariant library — toward crossing-minimality of the Borromean confinement operator

**Branch:** `claude/lean-tl3-kauffman-bracket-2026-06-17`
**Picks up:** the last residual of the Brunnian confinement selection (#2455).
After the Brunnian *signature* and *sublink-triviality* were proved in Lean
(`confinement_operator_selection.lean`, `decide`, axiom-free), the one open
piece was **crossing-minimality** — that the Borromean is *the* minimal
nontrivial Brunnian 3-link. That needs recognising **3-link nontriviality**, and
since `B₃` is non-abelian the `B₂ ≅ ℤ` exponent-sum test does not reach it: a
genuine link invariant is required. Author directive: *"worst case, enumerate in
Python to get the answer and assert it in Lean — `B₃` is small enough."* This
library realises that.

## Brick 1 (this PR) — a computable link invariant, Borromean nontriviality proved

[`content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean):

- **`LP`** — integer Laurent polynomials `ℤ[A, A⁻¹]` with normalised
  representation and `DecidableEq` (so polynomial equality is `decide`-able).
- **`TL`** — the Temperley–Lieb algebra `TL₃`, only **5-dimensional**
  (`Catalan 3 = 5`); full multiplication table from `eᵢ² = δeᵢ`, `e₁e₂e₁ = e₁`,
  `e₂e₁e₂ = e₂`.
- **`bracket`** — the Kauffman bracket of a 3-braid closure (`σᵢ ↦ A·1 + A⁻¹·eᵢ`,
  Markov-trace loop counts), an `LP`.
- **`borromean_link_nontrivial`** — proved **by `decide`, axiom-free**: the
  bracket of `(σ₀σ₁⁻¹)³`'s closure (a degree-28 Laurent polynomial) differs from
  the 3-unlink's (`δ³`). Both closures have writhe 0, so the unnormalised bracket
  already separates them. **The Borromean rings are a nontrivial link, machine-
  verified.**

This is the invariant the `B₂`-exponent-sum test could not provide. (`decide`
takes ~45 s on the single degree-28 reduction — acceptable for one theorem;
brick 2's enumeration will need `native_decide`, see below.)

## Brick 2 (next) — crossing-minimality by enumerate-then-assert

The plan the author described, now concrete and tractable because `TL₃` is tiny:

1. **Python oracle** (`computations/probes/b3_brunnian_minimality_enumeration.py`,
   already merged): enumerates pure 3-braids of word length `≤ 6` and confirms no
   nontrivial Brunnian below 6 crossings, Borromean at 6.
2. **Lean assertion:** enumerate the same finite set in Lean; for each, the
   Brunnian test is the `B₂` exponent-sum (decidable, brick from #2455) and the
   *nontriviality* test is `bracket ≠ (unlink bracket)` (brick 1). `decide` the
   minimality statement over the finite set.
   - **Performance:** ~4096 length-6 words × a degree-≈28 bracket each is far too
     slow for kernel `decide` (45 s × thousands). Brick 2 will use
     **`native_decide`** (compiled evaluation) — this adds the
     `Lean.ofReduceBool` axiom, which must be **documented** in the theorem's
     docstring and the axiom audit. This is the honest cost of the
     "assert in Lean" route for a computation of this size; it trusts the Lean
     compiler (the same trust as the Python oracle), not a hand-waved step.
   - Cross-check: the `native_decide` verdict must match the Python enumeration
     (both are the trusted-compiler oracle; agreement is the audit).

## Honest scope

- Brick 1 is a **genuine, axiom-free** machine proof that the Borromean rings are
  a nontrivial link — the previously-missing invariant.
- Full crossing-minimality (brick 2) will be **`native_decide`-backed** (one
  documented axiom), not kernel-`decide` — the finite computation is too large
  for the kernel. This is exactly the author's enumerate-then-assert pattern.
- None of this touches binding *magnitude* (still research-grade). It completes
  the *selection-principle* formalisation: confinement = crossing-minimal
  nontrivial Brunnian, now with both the triviality (B₂) and nontriviality
  (Kauffman/TL₃) invariants in Lean.

## Cross-links
- `content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_operator_selection.lean` — the Brunnian signature + sublink-triviality (`decide`, axiom-free).
- `computations/probes/b3_brunnian_minimality_enumeration.py` — the Python enumeration oracle.
- `docs/audits/2026-06-17-b3-dense-sdp-lever-closed.md` — why the selection is topological, not operator-space.
