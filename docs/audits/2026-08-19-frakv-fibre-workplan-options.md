# The fibre route for `𝔙`: what is actually available, and six options

**Date:** 2026-08-19
**Branch:** `claude/frakv-fibre-workplan-2026-08-19`
**Predecessor:** [`2026-08-18-convention-d-two-row-cap-and-ck-magnifier.md`](2026-08-18-convention-d-two-row-cap-and-ck-magnifier.md) §3e–§3f
**Conjecture:** `conj:binding-qbeta-complex-volume` — `𝔙 = E₀·tr_M((Π_free−1)∘𝓜)`, `Re 𝔙 = 𝔈_bind`, `Im 𝔙 = 𝔔_β`

The `qou-cds1` arc ended at a wall: the imaginary channel is **degenerate at the
observable level**, because `Im(q₀) = 0` gives real weights, real characters, a
real trace, and hence `Im 𝔙 ≡ 0`. Any live `𝔙` therefore lives on the **fibre**,
pre-`τ`. This document maps what the corpus already holds on that fibre, and what
the honest options are.

Two findings from the triage change the shape of the problem, and neither was in
the predecessor audit.

---

## 0. Finding 1 — the two ζ₄ artifacts do not touch

The corpus holds two sorry-free ζ₄ objects, and **nothing imports one from the
other**:

| file | what it is | ground |
|---|---|---|
| [`QOU/Mass/ComplexVolumeZeta4Partner.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/ComplexVolumeZeta4Partner.lean) | an **analytic model** `vModel z = cosh z + i·sinh z`, its ζ₄ orbit, the vanishing of the trivial and sign isotypes, and `IsZeta4Faithful` as a falsifier | `ℂ` |
| [`QOU/QBeta/FaddeevPhiFibreBranch.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FaddeevPhiFibreBranch.lean) | an **algebraic** root-of-unity object: `CyclicFaddeevPhi ζ N D`, discharged unconditionally at every primitive `N`-th root of unity by the finite q-Pochhammer `(x;ζ)_N` | generic field `K` |

`ζ₄ = i` is a primitive 4th root of unity, so `CyclicFaddeevPhi ζ 4` is an
*instance* of the second file's machinery sitting exactly where the first file's
ζ₄-rotation acts. `grep -rl CyclicFaddeevPhi` over the whole `QOU` tree returns
**its own file and nothing else**.

This matters because the descent map in
[`frakV_descent_zeta4_partner_probe.py`](../../computations/substrate/frakV_descent_zeta4_partner_probe.py)
records `single_fibre_V` as OPEN with *"Missing: both fibre kernels AND their
assembly into one trace object"*. One of the two missing kernels may already be
built — as an algebraic object on the cyclic branch — and simply not connected to
the analytic model that the descent argument is phrased in. **Connecting them is
not a derivation; it is a bridge, and it is cheap to attempt and cheap to
falsify.**

Honest caveat, stated by the fibre-branch file itself: the correspondence between
the cyclic object and the exact ℂ-`FaddeevPhi` class is a genuine **degeneration**
of the functional equation, not an instance relation — *"there is therefore no
honest sorry-free bridge that makes the cyclic dilog an instance of the exact
ℂ-`FaddeevPhi` class."* So the bridge to build is to `vModel`'s **ζ₄ action**, not
to `FaddeevPhi`.

## 1. Finding 2 — the bar-pairing blocker is tooling, not mathematics

[`complex_volume_witness.py`](../../computations/complex_volume_witness.py)
already **attempts** the bar-norm `‖tr_M‖² = tr_M(q₀)·tr_M(q₀⁻¹)` — the
principled bar-even mass modulus — and guards it:

> *"The canonical color-weighted atom word BAKES `q₀` into its crossing values, so
> it cannot re-lift at `q⁻¹` (a q-parameterised word builder is required — see
> `tr_m_atom_via_transfer` docstring). Guarded: the bar-norm is the principled
> mass-modulus but is not yet computable for this convention."*

and, in the same comment, records the fact this whole route turns on:

> *"They coincide on the unit circle (where conjugation = bar-involution) and
> **DIFFER at the real anchor** `q₀` (`q̄₀ = q₀ ≠ q₀⁻¹`)."*

So: every bar-parity statement about a trace-derived quantity currently rests on
a quantity the corpus **cannot evaluate**, for a reason that is a *word-builder
implementation detail*. `tr_M(q₀⁻¹)` is not hard mathematics; it is a
q-parameterised braid word. This is the single highest-leverage unblock in the
space, because bar-parity is the constraint every route in §3 needs.

It also corroborates, from the compute side, what `qou-qcz1` proved on the Lean
side (τ sends fibre parameter-conjugation, i.e. bar on `|q| = 1`, to Hodge
conjugation): **the fibre where the imaginary channel is real content is
`|q| = 1`, and the archimedean evaluation at real `q₀` is precisely the step that
kills it.**

## 2. What the arc established as binding constraints

Any option below must survive all four:

1. **Observable level is degenerate.** `Im(q₀) = 0` ⇒ `Im 𝔙 ≡ 0` after `τ`. A
   route that produces its imaginary part only at the anchor produces zero.
2. **Convention-D weights are bar-even.** `y₍₃₎ = (q⁴+1)/(q²+1)²`,
   `y₍₂,₁₎ = q²/(q²+1)²` — no bar-odd material comes from the D weights, so the
   odd channel must come from the *word* or the *fibre parameter*, not the
   Wedderburn weights.
3. **ζ₄-faithfulness is a proved falsifier.** `IsZeta4Faithful` (sorry-free): a
   candidate single-`𝔙` assembly with a nonzero ζ₄ orbit sum, or a nonzero
   trivial/sign isotype component, is **refuted** — not merely unsupported.
4. **Fitting `Φ₂` is forbidden**, and the `c_k` ladder's non-circular content is
   exhausted (`greedy_later_rungs_vanish`, sorry-free). No option may route
   through extracting another rung.

## 3. The options

Ordered by value per unit effort, not by ambition.

### F — repair the witness's machine-readable surface (cheapest; independent of every derivation)

`complex-volume-unification.witness.json` carries `assertions: []` with
`allPassed` set. The producer's **docstring is honest** — it says in terms that
the single-`𝔙` descent *"is the open conjecture, not proved here"* — but the
machine surface a consumer reads says a check ran and passed, when none ran.
`Im` is *assigned* from `q_beta_substrate`, not derived from a trace.

Fix: emit assertions that state what is actually checked (the `Re` cross-check
against AME, the `Im` cross-check against CODATA) and a `verdict` that names the
descent as unproved. Blocked by nothing. Does not advance the physics and must
not be described as if it does.

### D — q-parameterise the atom word builder (unblocks everything else)

Make `tr_m_atom_via_transfer` build its word over a symbolic/parameterised `q` so
`tr_M(q₀⁻¹)` is computable, then un-guard the bar-norm in
`complex_volume_witness.py`. Consequence: every bar-parity claim about a
trace-derived quantity becomes *checkable* rather than asserted. This is
compute-engineering with a mathematical payoff, and it is the prerequisite for
B, C and E to be more than prose.

Risk: the color-weighted convention may bake `q₀` in at more than one site; the
cost is unmeasured until someone reads the builder.

### A — bridge `CyclicFaddeevPhi` (N = 4) to the ζ₄ model

Per §0. Build the missing edge between the algebraic cyclic object and the
analytic ζ₄ rotation, on the `|q| = 1` branch where bar = conjugation. Falsifiable
immediately by constraint 3: if the resulting assembly has a nonzero ζ₄ orbit
sum, it is refuted and the option closes.

Most developed of the derivation options, and the only one whose two halves are
both already sorry-free.

### C — Neumann–Zagier / A-polynomial

The conjecture is explicitly the QOU analogue of `𝕍 = Vol + i·CS`, and in NZ the
imaginary partner is genuinely Chern–Simons, with the A-polynomial as the object
carrying both. Literature-grounded, and the library holds the sources. Large;
does not become concrete until D lands, because without `tr_M(q₀⁻¹)` there is
nothing to test a CS identification against.

### E — re-scope the corpus sites that state `Q_β`'s bar-oddness as established

Four sites assert it as fact. Per §1 the supporting quantity is not currently
computable, so the honest status is *fibre-level and conditional*. This is the
"open" / "refuted" scoping discipline applied to a claim that is neither — it is
**asserted**. Cheap, and it prevents a later agent building on it.

### B — Habiro ring / cyclotomic completion — **not recommended now**

The natural home for a root-of-unity `𝔙`, but the `c_k` Habiro element is exactly
what the corpus records as GATED, and constraint 4 forbids the route that would
pin it. Revisit only after A or D changes the inputs.

## 4. What this document did not do

- It ran **no new compute** and proved nothing. Every claim above is read from
  committed Lean, a committed witness, or a producer's own guard comment.
- It did **not** verify that `CyclicFaddeevPhi` at `N = 4` can in fact carry the
  ζ₄ action — that is the content of option A and may fail.
- It did **not** measure how many sites bake `q₀` into the word builder, so
  option D's cost is stated as unknown rather than estimated.
