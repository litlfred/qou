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

## Brick 2 (DONE, this PR) — crossing-minimality by enumerate-then-assert

`theorem QOU.Knots.TL.borromean_crossing_minimal` in
[`KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean),
proved by **`native_decide`** (axioms `Lean.ofReduceBool` + `Lean.trustCompiler`).
It enumerates **every** 3-braid word of length `< 6` over `{σ₁^±, σ₂^±}` and asserts:

1. the Borromean `(σ₁σ₂⁻¹)³` is pure, Brunnian, nontrivial and has word-length 6;
2. no word of length `< 6` is simultaneously Brunnian and nontrivial.

Two decidable invariants combine, both already in the library:

- **Brunnian** = every 2-sublink trivial = each deleted-strand 2-braid has
  `B₂ ≅ ℤ` exponent sum `0` (`b2class`, re-implemented from #2455 in the
  `{σ₁,σ₂}` indexing this file uses).
- **Nontrivial** = the **writhe-normalised** Kauffman bracket — the Jones
  invariant `(-A³)^(-w)·⟨·⟩`, a genuine ambient-isotopy invariant — differs from
  the 3-unlink's `δ³`. Normalisation was *essential*: the unnormalised bracket
  (brick 1) shifts by `(-A³)^±1` under R1, so a *trivial* braid of nonzero writhe
  would spuriously read "nontrivial"; only the Borromean (writhe 0) was safe
  unnormalised. Jones-nontrivial ⇒ genuinely nontrivial (the converse can fail,
  which only makes the lower bound safer — it never over-counts).

**Per-length breakdown** (`#eval`, reproducing the Python oracle's table and
proving the theorem is non-vacuous):

| len | pure | pure+Brunnian | nontrivial-Brunnian |
|----:|-----:|--------------:|--------------------:|
| 0 | 1 | 1 | 0 |
| 2 | 8 | 4 | 0 |
| 4 | 96 | 28 | 0 |
| 6 | 1408 | 248 | **4** (the Borromean family) |

The **28 Brunnian-but-trivial** words at length 4 are the load-bearing check: there
*are* Brunnian braids below 6 crossings, but the Jones invariant certifies every
one of them trivial, so none counts. At length 6 exactly **4** words are
nontrivial-Brunnian — `(σ₁σ₂⁻¹)³` and its sign/mirror variants, all
Borromean-signature — matching the oracle. The `native_decide` verdict (minimal
`= 6`) **agrees with** the Python enumeration
(`b3_brunnian_minimality_enumeration.py`); the agreement is the audit.

- **Performance:** ~1365 words below length 6 (+ the length-6 witness check), each
  a Laurent-polynomial bracket — far beyond kernel `decide` (brick 1's *single*
  bracket took ~45 s), so `native_decide` (compiled) is required. It trusts the
  Lean compiler (the same trust class as the Python oracle), documented in the
  theorem docstring and the axiom audit. Whole-file `lean`-direct check: ~36 s.

## Honest scope

- Brick 1 is a **genuine, axiom-free** machine proof that the Borromean rings are
  a nontrivial link — the previously-missing invariant.
- Full crossing-minimality (brick 2) is **`native_decide`-backed** (axioms
  `Lean.ofReduceBool` + `Lean.trustCompiler`), not kernel-`decide` — the finite
  computation is too large for the kernel. This is exactly the author's
  enumerate-then-assert pattern; the verdict cross-checks the Python oracle.
- Scope is **3-braid closures** (the framework's 3-quark setting) and **braid-word
  crossing number**, not full link-theoretic uniqueness over all links; and
  nontriviality is the Jones invariant — a *sufficient* (not complete) certificate,
  which only strengthens the lower bound. The literature uniqueness (Borromean =
  the unique 6-crossing Brunnian link, Rolfsen) is unchanged.
- None of this touches binding *magnitude* (still research-grade). It completes
  the *selection-principle* formalisation: confinement = crossing-minimal
  nontrivial Brunnian, now with both the triviality (B₂) and nontriviality
  (Kauffman/TL₃) invariants in Lean.

## Cross-links
- `content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_operator_selection.lean` — the Brunnian signature + sublink-triviality (`decide`, axiom-free).
- `computations/probes/b3_brunnian_minimality_enumeration.py` — the Python enumeration oracle.
- `docs/audits/2026-06-17-b3-dense-sdp-lever-closed.md` — why the selection is topological, not operator-space.
