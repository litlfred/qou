# α\* has no Lean backing — the "if Lean-proved then re-centre" gate is NOT satisfied

**Bean:** `qou-2zjp`.
**Question asked (owner):** *"if qou-2zjp is lean proved then go."*
**Answer: NOT PROVED.** The bracket was left where it is; nothing was regenerated.

## What α\* is

`computations/alpha/alpha_high_precision.py` bisects `err_n_mp(α)` — the relative
error of the predicted neutron mass — for the **blend parameter** α\* appearing in

```
V̂_std^(α) = α · ½[χ_std(chain) + χ_std(S(chain))]  +  (1 − α) · √|det T_chain|
```

i.e. the mixing between the Frobenius-antipode-symmetrised std-channel character
and the antipode-invariant determinant. The committed witness
(`computations/alpha/alpha-high-precision.witness.json`) records
`alpha_star = 0.3058074307438076264762191`; the current root is
`0.35088642931861095442` (+14.741 %, anchor-independent — see `qou-2zjp` for the
convention-C→D attribution).

Re-centring the bracket onto the D-frame root would **replace a published value**.
The owner gated that on Lean backing. This document is the search.

## The search — all five corpus-grep paths

| Path | Query | Result |
|---|---|---|
| `content/**/lean/` | `alpha_star`, `alphaStar`, `alpha_blend`, `blend`, `err_n`, `bisect`, `IntermediateValue`, `StrictMono`/`StrictAnti` | no declaration about α\* |
| `docs/audits/` | `alpha_star`, `α*` | hits are prose; **all say α\* is NOT closed-form** |
| `content/` (whole tree) | `alpha-blend`, `blend parameter/coefficient` | 2 content blocks, one `theorem` — see below |
| `computations/` | `alpha_star`, `ALPHA_STAR` | 9 scripts, all numerical; none cites a Lean decl |
| `docs/coordination/` | `α*`, `alpha_star` | 2 hits, **both a different α** (see §Symbol collision) |
| `library/INDEX.md` | `blend`, `antipode` | 1 unrelated Hopf-algebra paper; an external paper cannot supply a declaration in this corpus anyway |

LSP (`lean_local_search`) over the built QOU library confirms it at declaration
level: **no `alphaStar` and no `blend` declaration exists.** The only `Alpha*`
matches are `QOU.BraidKnot.AlphaShiftTorus.*`, an unrelated ℕ-valued torus-knot
shift index.

## The one theorem that looked like a hit, and why it is not

`thm:frobenius-antipode-unifies-chirality-and-tower` is a `theorem` block carrying
`lean: { ref: "qou:QOU.BraidKnot.frobenius_antipode_unifies" }`, tagged
`alpha-blend`, and its interpreting remark
(`rem:frobenius-antipode-neutron-tower-closure`) says in prose that the blend
"yields a sub-ppm match at the precise optimal mixing value". That is the closest
the corpus comes.

The declaration is real and genuinely sorry-free — `lean_verify` reports axioms
`[propext]`, no warnings. **But read its type:**

```lean
theorem frobenius_antipode_unifies {G : Type*} [Group G] (σ : ℕ → G) :
    (∀ i, frobeniusAntipode (σ i) = (σ i)⁻¹) ∧
    (∀ a b : G, frobeniusAntipode (a * b)
        = frobeniusAntipode b * frobeniusAntipode a)
```

with `frobeniusAntipode := fun g => g⁻¹`. It proves that the group-inverse map on
any group sends generators to their inverses and is an anti-homomorphism —
`rfl` and `mul_inv_rev`. **The symbol α does not occur anywhere in the file.**

This is the AGENTS.md §"Grep the claim SHAPE, not only the topic" failure mode
exactly: the *topic* (Frobenius antipode / neutron tower / α-blend) has Lean; the
*proposition* is a generic group fact. It establishes none of the four things
that would license re-centring — existence of a root of `err_n`, uniqueness of
that root, monotonicity of `err_n`, or the value of α\*.

Two further near-misses, both failing the same way:

- `QOU.WedderburnMass.s_symmetric_ansatz_misses_chirality`
  (`mass-theory/frobenius-s-classification.lean:86`) is *about* a blend
  `α·V_a + (1−α)·V_b` — but in a two-element toy type `SEigenvalue`, and it
  proves the blend **cannot** capture chirality. It is a negative about the
  ansatz, not a characterisation of α\*.
- `braids-and-knots/frobenius-antipode-lean-stub.lean` carries
  `axiom markov_trace_antipode_invariant` and an `antipodeSymmetrize` whose body
  is admittedly a placeholder (it returns `antipodeS n q x`, not `(x + S x)/2`).
  Per §"Axiomatization is NOT a Proof", an axiom is not a proof; and this file
  too contains no α.

## Symbol collision — three different α's

Worth recording, since two of the six corpus hits for "α\*" are not this α at all:

| Symbol | Meaning | Where |
|---|---|---|
| α\* ≈ 0.3058 | **this one** — Frobenius/det blend parameter | `alpha_high_precision.py` |
| α\* = 0.89 | an SDP feasibility fraction for ²H ↔ 6₂ | `docs/coordination/2026-05-24-post-1089-followups-ledger.md:57` |
| α, α_EM | fine-structure constant; and `alpha_bind := m_e·8·catalan_G` | `2026-05-30-alpha-em-4pi-thread.md`, `WedderburnMassFormula.lean:83` |

Per the registry rule that attributes do not transfer across overloaded symbols,
none of these says anything about the others.

## The corpus does not merely lack a proof — it argues the opposite

This is the part that should stop a future agent from re-opening the gate hoping
to find the proof somewhere:

- `docs/alpha-blend-derivation.md` §5: PSLQ at 25-digit tolerance over
  `{1, G, π, 1/π, q₀, h_q}` with `maxcoeff = 10⁶` returns **no integer relation**,
  and explicitly **falsifies** `α* = G/3` (the 0.16 % agreement was a
  three-digit coincidence). Its conclusion: the 2-term blend "is **not a
  fundamental decomposition** of the std-channel value. A single phenomenological
  mixing parameter is the wrong ansatz."
- `docs/canonicalization-review.md` §3 lists `α* ≈ 0.305807` as **row 1 of the
  seven empirical/fitted constants**, root cause "2-term blend drops chirality",
  and §3.1 states: *"There is no closed form for α\* in the 2-term frame because
  the quantity it patches is structurally outside that frame."* The intended fix
  is to **eliminate α\* entirely** by moving to the 3-term Wedderburn formula.
- `docs/agent-briefs/lambda_scale.md:552` classes it as "numerical root-find",
  target state "closed form in q₀ from antipode + det" — i.e. open.

So α\* is currently a **fitted mixing parameter with a documented plan to be
removed**, not a derived quantity awaiting a bracket refresh.

## Consequence

The gate is not satisfied, so **no re-centring, no regeneration, no witness
change**. `alpha_high_precision.py` stays exactly as it is: it exits 1 and names
where the root actually is on stderr (landed on `main` as `b95cc706d9`, PR
\#5695). That is the honest state — a producer that refuses rather than one that
publishes a convention-D number under a convention-C witness.

Note the scope, per §"Before declaring refuted": this is a **scope-(a)** finding
— *no Lean declaration characterising α\* exists in this corpus today*. It is not
a claim that no such characterisation could exist. What would satisfy the gate is
a declaration whose **statement** mentions the blend parameter: existence and
uniqueness of a zero of `err_n` on an interval (an IVT + strict-monotonicity
argument would do it), or a closed form for α\*. Nothing weaker — a lemma about a
generic monotone function, an axiom, a conditional-class instance, or another
theorem about the antipode's algebra would not.

**A caution for whoever does re-centre it later.** Even with the gate satisfied,
re-centring only fixes the *bracket*. It does not make α\* derived — the
regenerated witness would still record a fitted mixing parameter, now in the
D frame, and would need to say so. The deeper item is `qou-cds1`-shaped: α\* is a
convention-C quantity that needs re-derivation under D, and per the two documents
above the D-frame re-derivation may well conclude that the parameter should not
exist at all.
