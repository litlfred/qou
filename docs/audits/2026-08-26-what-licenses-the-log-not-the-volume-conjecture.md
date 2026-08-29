# What licenses `ln|tr_M|` as a binding energy — and what does not

**Bean:** `qou-mkm8` (steps 1–3). **Branch:** `claude/isotope-mass-binding-dashboard-kdvhz6`.
**Verdict:** the log-forms `B_sym` / `B_qCLT_fac` are **`POSITED`**, not `DERIVED*`.
The KVC-conditional tag they carried is wrong in both directions, and I put it
there myself.

## The question

`B_sym = α·ln(tr_free/tr_atom)` is the production binding form. What licenses
taking a **logarithm** of a Markov trace and calling the result an **energy in
MeV**?

## Three neighbouring objects, three different licences

Tracing `B_sym`'s dependency cone in the **code** rather than the prose tag
separates three things the tag had merged.

### (1) The log's extensivity — DERIVED, no conjecture

`computations/mass_binding_dashboard.py::_bond_type_L`. The sole generator
joining nucleon *k*'s last strand to nucleon *k+1*'s first satisfies
`σ² = hσ + 1`, so it generates a **two-dimensional** subalgebra `span{1, σ₂}`
and every interface element is `aσ₂ + b·1`. With the Markov property
`tr_M(W·σ₂) = z·tr_M(W)`,

```
tr_atom = tr_free · ∏_bonds (a·z + d_XY),      L_XY = −ln(z + d_XY)
```

A **product** over bonds has an **additive** logarithm. That is the entire
reason a log appears, it is elementary, and it needs no volume conjecture. It
establishes that the log is **extensive**. It establishes nothing about MeV.

The closed form agrees with the exact transfer trace to `4.489e-32` at all three
bond types, and `chain_resid ≈ 1e-13` against `tr_m_atom_zn` in the dashboard —
so `B_sym` genuinely *is* the log-ratio, not a different object computed cheaply.

### (2) `E₀ × (trace DIFFERENCE)` — a Conjecture, and a different functional form

[`knot-factor-frobenius-pairing.md`](../../content/quantum-observable-universe/mass-theory/knot-factor-frobenius-pairing.md)
is the only block that attaches `E₀` to a trace:

> **Conjecture.** `B_bulk(Z,N) = E₀·( |tr_M(W_free)| − |tr_M(W_atom)| )`
> … "A single archimedean calibration constant `E₀`, fixed by neutron beta
> decay, maps the pure Markov **defect** to the physical MeV scale."

That is the **difference**, which is the dashboard's `B_can0` column — and the
code comment there already said so: *"absolute trace difference (≡
binding_canonical), **NOT** the log `B_sym`."* It is also a **`conjecture`**
block, not a proposition.

### (3) `ln|tr_M| = Vol` — KVC-conditional, and it does not reach this object

[`vol-through-tau.md`](../../content/quantum-observable-universe/mass-theory/vol-through-tau.md)
is the block the dashboard cited. It fails for `atom_braid_word_3A` twice:

- **Quantifier.** It reads *"for every **braid** β ∈ B_n, with image ρ(β) ∈
  H_n(R,q) and closure K_β"*. The atom word's letters are `c·σ_g + d·1` —
  general Hecke elements, not braid generators. `ρ : B_n → H_n(R,q)` is neither
  injective nor surjective, and the statement is only meaningful on its image.
- **Even reading past the quantifier, the value is zero.** `c64833a979`:
  **0 of 40** branch closures of the atom element are hyperbolic (proton 0/4,
  neutron 0/4, deuteron 0/32), both controls green — the figure-eight positive
  control reads `2.029883212819307`. So `Vol = 0`, while
  `B_sym(²H) = 3.8897 MeV`.

## So what is `B_sym`?

It has **(1)'s extensivity** and **(2)'s prefactor**, and **no block asserts the
combination.** `α = m_e/(q₀(q₀−1)) ≈ 4.18598 MeV` carries the CAL-1 unit
correctly (this is the dimensional check that killed the Reeb override — see
`_bond_type_L`), so the *units* are right. What is missing is any derivation
that this particular dimensionless log, rather than the difference, is the thing
`E₀` multiplies.

`POSITED` is the honest tier: **the functional form is asserted.**

## Self-correction — I introduced the tag I am now removing

The `DERIVED*` KVC citation entered in **`933053614f`**, *"RETRACT 'posited':
B = −alpha*ln|tr_M| IS derived (KVC-conditional)"* — my own commit, 2026-08-25
**18:59:59**. It replaced a dead `standard-part-functor.md` reference, and it
announced that an earlier "posited" finding of mine had been wrong.

**`1c83073b3c`**, 2026-08-25 **19:46:19** — **47 minutes later**, same session —
corrected `vol-through-tau`'s quantifier from *"for every braid β ∈ H_n(R,q)"* to
*"for every **braid** β ∈ B_n"*, and added a note saying in as many words that
the production pipeline's object is **not** covered and *"the corresponding Vol
is in fact 0."*

I wrote both. I did not go back and check that the second invalidated the first.
So the retraction is itself retracted, and the original "posited" finding was
closer to right than the thing that replaced it.

Two general lessons, both already in AGENTS.md and both violated here:

- **Grep the claim SHAPE, not the topic.** `933053614f`'s commit message
  correctly diagnoses *why* the first grep missed the derivation ("the
  derivation is spelled in terms of `Vol`, not `B_sym`") — and then failed to
  ask the arity question one step further along: does the proposition's
  quantifier cover the object being computed? It did not.
- **A retraction is a claim too.** It gets the same corpus-grep discipline as
  the finding it retracts. This one did not get it.

## What this does NOT change

- **No number moves.** This is a provenance tier, not a computation. The
  dashboard's `B_sym` column is byte-identical.
- **The binding defect stands.** The five-front closure (`qou-39bx`, `qou-hh9q`,
  `qou-52x7`, `qou-o37w`, `qou-09e0`) is untouched: `B_AME/B_allpairs` is
  non-monotone in A (²H 0.785, ⁴He 1.647, ⁷Li 0.639), so no scale correction
  repairs it, whatever licenses the log.
- **KVC is not refuted and is not needed here.** Scope **(a)**: the volume
  conjecture is simply not on this object's dependency path. Whether it holds is
  irrelevant to `B_sym`, which is exactly the point — a live open conjecture was
  being carried as a caveat on a quantity that never touches it.

## Still open (bean `qou-mkm8`, step 4)

Nothing here derives the log-form. The two candidate closures are:

1. **Show the difference-form and the log-form agree** in the regime used — i.e.
   derive `α·ln(tr_free/tr_atom)` from `E₀(|tr_free| − |tr_atom|)` plus a stated
   condition. They differ at second order: with `s = 1 − tr_atom/tr_free`,
   `B_can0 = α·tr_free·s` and `B_sym = α(s + s²/2 + …)`, so they agree only for
   small `s` **and** `tr_free ≈ 1`. Neither holds here (`B_lin` vs `B_sym` in the
   dashboard is exactly this gap).
2. **Find or write a block that licenses the log directly** — an extensivity
   argument that produces the MeV scale, rather than importing it from the
   difference-form conjecture.

Do **not** close this by re-citing `vol-through-tau`.
