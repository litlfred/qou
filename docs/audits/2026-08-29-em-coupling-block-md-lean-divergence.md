# The `em-coupling-chern-simons` block's `.md` and `.lean` state different formulas

Bean `qou-aemx`. This supersedes the "cross-sector dilemma" framing of
[`2026-08-28-alpha-em-lean-vs-compute-divergence.md`](2026-08-28-alpha-em-lean-vs-compute-divergence.md)
§10 — see §4 below.

## 1. The divergence

One content block, two incompatible statements of its own claim.

**`.md`** — the paper's live claim:

```
1/α_EM = q·[9]_q·[10]_q · (1 + δ_CS/(1 − δ_CS·κ)),      κ = det G^cl_CS / det G^q_CS ≈ 1.7216
```

**`.lean`** — its formalisation:

```
alphaEmInvCorrected q = 45·[3]_q · (1 + δ + κ·δ²),      κ = gluonOctetKappa = 8q ≈ 8.8798
```

Different prefactor, different κ, different tower shape. Numerically
**470.2 ppb apart**: `.md` → 137.035935093976, `.lean` → 137.035999531717.

**The `.md` is the live one.** Its formula and κ reproduce
`meson_em_sinh_closed_form._alpha_em_inv_derived` **exactly** —
137.035935093976, byte-for-byte, which is what the L2 dashboard consumes.

**And the `.md` says so about the `.lean`'s form, in its own words:**

> The order-`δ_CS²` form `1 + δ_CS + δ_CS²κ`, **which this proposition
> previously displayed**, is its second-order truncation and costs 11.06 ppb.

So the `.lean` formalises the **superseded** version of its own block. This is
a `proof-statement-integrity` defect: the Lean does not state the `.md`'s claim.

## 2. This dissolves the "cross-sector dilemma"

§10 of the previous audit asked why a **nucleon** (Borromean, hyperbolic)
volume should set a coefficient in an **electromagnetic** coupling, and called
it a dilemma against the corpus's own volume↔mass sector rule.

**The live formula has no such problem.** The `.md` is explicit:

> The correction arises from the descent decomposition of the coupling
> endomorphism on the force-carrier configuration. The torus knots `T_{2,9}`
> and `T_{3,5}` are **non-hyperbolic**. Their τ-image geometric invariant is
> the **Chern–Simons functional, not the hyperbolic volume**.

Torus knots, zero volume, CS invariant — **exactly what the sector rule
prescribes for a force carrier.** No nucleon volume appears anywhere in the
live formula.

The dilemma was real only for the `.lean`'s stale `κ = 8q`. **Withdrawn as a
statement about the framework**; it survives only as one more symptom of the
stale sibling.

## 3. What survives from the previous two tranches

- **`Vol(𝓑₃)/G = 8` exactly** — still true, still non-generic (2 of 9 knots,
  both octahedral). It is a true identity about a **superseded** coefficient.
- **`8q` is forced within its ansatz family** (new, §5) — likewise about the
  superseded coefficient.
- **The two prefactors are different functions** crossing 0.016 % from `q₀` —
  unaffected; it is now explained as *stale vs current* rather than as two
  live rivals.

## 4. Correcting my own §10

§10 concluded the sector question was *"the whole remaining content of the
claim"* and needed an owner ruling. **That was wrong**, and wrong for a
diagnosable reason: I analysed the `.lean` without checking it against its own
`.md`. The block's narrative had already moved on, and says so in the sentence
quoted above.

The lesson is the corpus-grep discipline applied one level in: **a block's
`.lean` is not a primary source for the block's claim — the `.md` is.**
AGENTS.md says the `.md` is "the narrative/authoritative human-readable face of
a content block"; I treated the Lean as authoritative for two tranches.

## 5. What IS derivable — κ forcing within the ansatz family

Measured on the **`.lean`'s** (superseded) form, so its standing is historical.
Window of κ giving |err| < 100 ppb is `[8.4744, 9.2648]`.

| ansatz | result |
|---|---|
| `κ = c·q`, `c` integer | `c ∈ [7.635, 8.347]` → **`c = 8` unique** |
| `κ = 8·q^n`, `n` integer | n=0 → −220 ppb, **n=1 → +2.59 ppb**, n=2 → +250 ppb → **`n = 1` unique** |
| `κ = c·q^n`, both integer | **three** land: (7,2) −62 ppb, **(8,1) +2.59 ppb**, (9,0) +33 ppb |

So fixing either exponent or coefficient forces the other; freeing both leaves
three, with (8,1) best by ~13×. Stronger than "in range", weaker than "forced".

## 6. The live block's own open item is unchanged, and it is honest

The `.md` already states its gap plainly: κ is *"conjectured"*, *"This
identification is unproved"*, *"not computed end-to-end"*, *"A direct fit to
CODATA gives κ ≈ 1.8878"*, and *"This suggests the formula misses a
higher-order term or the entire ansatz uses the wrong decomposition."*

That matches this arc's independent measurement — the Gram κ = 1.7216 misses,
and the value needed is ≈ 1.9153 on the resummed form. **The live block is not
over-claiming.** The defect is confined to its Lean sibling.
