---
# qou-hprp
title: '23 conjecture carriers assert nothing — the `holds : Prop` shape'
status: in-progress
type: task
priority: medium
created_at: 2026-08-29T18:10:00Z
updated_at: 2026-09-03T08:35:25Z
---

Found sweeping the q-geometric-langlands Lean siblings after the four
`False`-proving axioms (`qou-hwax`, `qou-qexf`).

```lean
class QuantumLanglandsDual where
  holds : Prop
```

`⟨True⟩` inhabits this. So a downstream `[QuantumLanglandsDual]`-conditional
theorem proves nothing modulo the conjecture, and the carrier records only that
*someone intends a proposition to go here*. It is the `true-class-field` variant
of `proof-claims-unencoded` — one step less obvious than an empty carrier, and it
passes every existing check.

## Measured, and the first number was wrong

| measure | files |
|---|---|
| naive grep `holds : Prop` | 38 |
| **live, comments stripped** | **23** |
| prose-only false positives | 15 |

A 39 % false-positive rate for the naive grep. The false positives are
docstrings describing a stub that was *already replaced* — including
`modular-s-transform-q-q-tilde.lean`, whose docstring records that it
"replac[ed] the former `holds : Prop` stub". A grep that reads comments as code
would have sent an agent to fix the one file in the chapter that is already
correct.

By chapter: mass-theory 7, `lean/` 6, nuclear-interactions 4,
stochastic-mechanics 2, q-geometric-langlands 2, appendix-surreals 1,
appendix-surreals-archimedean 1.

Detector: [`scripts/lean-overclaim-audit.py`](../scripts/lean-overclaim-audit.py)
reports 39 such *declarations* under `contentless-carrier`, plus 9
`empty-carrier`. That is the trustworthy family in that script; read its
docstring for what is not.

## The model to copy is in the same chapter

`ModularSTransformQQTilde` shows the right shape — a conjectural continuation
`F : ℂ → ℂ`, a `nondegenerate` field so the duality is not vacuous, and the
`s_automorphy` law carrying the actual claim. Three carriers in one chapter, two
dispositions, and the good one already documents its own migration.

## Why this is NOT a mechanical drain

**Do not sweep these.** Filling in a carrier means deciding what the conjecture
claims, which is a mathematical judgment about the author's intent, not a
repair. The specific trap, worked through on `QuantumLanglandsDual`: its `.md`
claims `H_n(q) ↔ H_n(q^{-1})` via Cartan folding. An encoding restricted to the
*parameter* — an involution `q ↦ q⁻¹` on `ℝ`, nontrivial for `q > 1` — is
content-bearing, satisfiable, and **provable**, so supplying it with an instance
would report an open conjecture as closed. That is strictly worse than the stub
it replaced.

A faithful encoding has to reach the algebra. `QOU.Hecke.HeckeAlgebra R n q A`
exists (`QOU/StaircaseCornerHook.lean` uses it as an instance binder), so the
statement is expressible — an algebra equivalence `A ≃+* B` between `H_n(q)` and
`H_n(q⁻¹)` compatible with folding — but that is a per-conjecture piece of work
needing the author's reading of each claim, and it carries a build cost the
content-block siblings do not currently pay.

---

## TRIAGE 2026-08-29 — and the ordering above is WRONG

That closing line said *"take the ones whose `.md` states a single crisp identity
or inequality first."* Having read all 23 `.md` claims, **that is backwards.** The
crisp ones are crisp *because* they are classical or numerical, and those are
precisely the two categories that need a different disposition rather than a
content-bearing conjecture class. Filling one in would be wrong work, not easy
work.

The 23 are **not one population.** Four kinds:

**(a) The claim is a CLASSICAL theorem, mislabelled as a framework conjecture.**
`conj:poincare-lefschetz-borromean` states `H^k(M, ∂) ≅ H_{3−k}(M)` — Poincaré–
Lefschetz duality, a theorem of algebraic topology — and `H₁ ≅ ℤ³` for the
3-cusped Borromean complement, which is standard. Nothing here is conjectural.
The right disposition is a **cited hypothesis class** in the `IsWeilZeta` pattern
(`qou-hwax`), carrying the classical result as a named, referenced hypothesis —
not a conjecture stub, and not an axiom. `conj:borromean-bloch-group-element` is
partly this too: Bloch-group/regulator theory is classical, the `h⁴` shadow is
the framework's.

**(b) The `.md` declares conditionality that the type does not carry.**
`conj:spin-from-so3-fiber` ("conditional on the S₅ ↔ SO(3) fibre action"),
`conj:wigner-su4-from-spin-isospin` ("conditional on spin and isospin"),
`conj:lusztig-canonical-basis-q-eq-1` ("conditional on
[`conj:kazhdan-lusztig-classical-limit`]"), `conj:kashaev-density-equals-sdp-multiplicity`
("under the Kashaev volume conjecture"). This is the named criterion
`proof-dependent-conjecture-not-conditional` — which could not see any of them;
see `qou-vgat`.

**(c) An IDENTIFICATION of a framework notion with a mathematical object,
blocked on the framework notion having no formal carrier.**
`conj:p-from-braid-mirror` (parity *is* the braid mirror),
`conj:quantum-langlands-dual`, `conj:mirror-3d-3d-correspondence`,
`conj:hecke-anyonic-substrate`, `conj:type-b-folding-cpt`. Same blocker shape as
`qou-qspc`: the mathematical half is often provable, the identification is the
claim, and there is nothing to identify *with*. `p-from-braid-mirror` is the
sharpest illustration — "P is an involution negating writhe" is a provable fact
about braid words; that P *is parity* is not statable without a formalised
parity operation.

**(d) A NUMERICAL near-match.** `conj:isospin-from-canonical-bowtie` gives
`Δm/M_N = ℏ_q²·h·[2]_q·(1+ℏ_q³)/3` at **305 ppm** against CODATA. Encoding it as
an equation would be **false**; encoding it with a tolerance is a modelling
decision under the anti-fit discipline, not a transcription.

**Separately, one is not a conjecture at all.**
`prop:crystal-basis-resolves-mass-tower-open-problems` is a **`proposition`**
whose carrier is `holds : Prop`. A provable-kind block asserting nothing is worse
than a conjecture doing so — the label claims it is established. Worth handling
before any of the conjectures.

**Revised order.** (1) the `prop:` above, since its kind over-claims; (2) the
category-(a) classical ones, which need a citation rather than a derivation and
are the only genuinely cheap group; (3) category (b), where the fix is adding a
binder the prose already asserts; (4) leave (c) and (d) — they need the author.


--------

## 2026-09-03 — item (1) of the revised order was ALREADY DONE, and the count moved

**Correcting this bean against the tree.** The revised order above puts
`prop:crystal-basis-resolves-mass-tower-open-problems` first, "since its kind
over-claims". That was written 2026-08-29. It was fixed on **2026-08-31** — the
file now carries `ReducesTo`, a seven-parameter `CrystalBasisCorrespondence` with
three reduction fields, and a derived `crystal_basis_reduction`, plus a
"What is NOT claimed here" section. It does not appear in the detector's
`contentless-carrier` list. The bean's own top-priority item was stale by two
days; re-run the detector before working from this list.

**Live detector figures, `scripts/lean-overclaim-audit.py` on main + this branch:**

| | at triage | now |
|---|---:|---:|
| candidates | — | 128 |
| `overclaim-structure` | — | 78 |
| `contentless-carrier` | 39 | **37** |
| `empty-carrier` | 9 | 9 |
| `overclaim-independent-binders` | — | 3 |

Both steps measured separately: 39 → **38** after the Poincaré–Lefschetz fix,
38 → **37** after the Bloch-group one. (This entry briefly carried a 37 that was
a *prediction* — the Bloch file was still being `lean`-checked when it was
written. Corrected to a measurement, then re-measured to the same value.)

**Two category-(a) carriers done — the classical ones, as the triage predicted.**

1. **`conj:poincare-lefschetz-borromean`.** Poincaré–Lefschetz duality and
   `H₁(S³∖𝓑₃) ≅ ℤ³` enter as **cited hypotheses** (the `IsWeilZeta` pattern), not
   as conjectures — encoding settled topology as "conjectural" would misreport it.
   The framework's own claim is the third field, that the top-degree pairing is
   `Vol(𝓑₃)`. Derived: `rankHrel_two_eq_three` (the block's own "in particular
   `H²(∂𝓑₃) ≅ H₁ ≅ ℤ³`" — none of the fields, and it needs two of them),
   `plPairing_eq_eight_catalan`, `plPairing_pos`.

2. **`conj:borromean-bloch-group-element`.** Stronger: the block's headline
   `r₂[𝓑₃] = 8G` is **derived, not assumed**. One classical field
   (`r₂([i]) = Cl₂(π/2) = G`); Thurston's two-octahedron decomposition lives in the
   *definition* `borromeanClass := 8 • [i]`; then `regulator_borromean` gets `8G`
   out of **additivity of the regulator**, so the `8` comes from the group
   structure rather than from a hypothesis. Also derived: the class is non-zero in
   `B` (the block's "non-trivial element of `K₃(ℂ)`"), and the `h⁴` shadow
   `r₂[𝓑₃]·(−3/4) = −6G`.

**Both show non-vacuity from BOTH sides**, which the triage did not ask for and
which is what actually distinguishes a content-bearing field from a decorative
one: a witness satisfying the fields, *and* a theorem that a specific datum does
**not** satisfy them (`b₁ = 2` fails one; a vanishing regulator fails the other).
Both witnesses are `theorem`s, never `instance`s — as instances the next reader is
invited to add one to a datum not constructed to satisfy the fields
(`trivialSkeinGenerationContext`, `qou-skgn`).

**What each file does NOT formalise is written in the file**, not left implied:
no manifold-with-cusps machinery (the PL block's own "still open" item 3), no
Bloch group / five-term relation / `K₃` construction, `blochI` not forced to be
`[i]` so the ζ₄-vs-ζ₆ care in the block is carried only by the *value*, and the
`h⁴ = −3/4` coefficient taken as a hypothesis rather than re-derived.

Verification: `lean`-direct exit 0 on both; `#print axioms` clean on all ten new
declarations. Sidecars refreshed.

**Remaining category (a) is now empty.** Next is category (b) — four carriers
whose `.md` declares a conditionality the type does not carry — and note the fix
there is **not** just adding a binder: adding `[KazhdanLusztigClassicalLimit]` to a
`holds : Prop` carrier leaves the field just as contentless. Both halves are
needed.
