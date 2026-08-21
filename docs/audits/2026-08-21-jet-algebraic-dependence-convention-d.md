# Bean `qou-j4mn` archaeology: the tr_M jet algebraic-dependence finding is
# convention-C-frame; under canonical convention D the minimal degree is 3, not 7

**Date:** 2026-08-21 · **Bean:** `qou-j4mn` (type `bug`, filed 2026-08-09, **empty body**)
**Branch:** `claude/jet-algebraic-dependence-2026-08-21` · **PR:** #5402

## The claim under audit

The bean has no body. Its entire content is the title:

> FINDING: tr_M jets are ALGEBRAICALLY DEPENDENT (min degree 7, nullspace dim 3,
> stability-verified) — forced since all three are in Q(sqrt q), trdeg 1. So
> `JetTransportImpliesIndependence` cannot be a transfer of independence;
> `JetOrderIndependence` is only a LINEAR rank certificate.

Three separable assertions: a **structural** one (dependence is forced by
trdeg 1), a **numerical** one (min degree 7, nullspace dim 3), and a
**consequence** about two Lean declarations.

## Verdict

| Assertion | Verdict |
|---|---|
| Dependence is **forced** by trdeg 1 | **HOLDS** — and is convention-independent |
| The three traces lie in `Q(sqrt q)` | **Convention-C-frame.** Under canonical D they lie in the *smaller* field `Q(q)` |
| Minimal relation degree **7**, nullspace dim **3** | **Does not reproduce.** Under canonical D the minimal degree is **3** |
| `JetOrderIndependence` is only a linear rank certificate | **HOLDS** — verified from the declaration, not inherited |
| `JetTransportImpliesIndependence` "cannot be a transfer of independence" | **Right conclusion, wrong reason** — see §4 |

## §1 Provenance

`53263a8e79` ("probe qou-5b23: tr_M jets are algebraically DEPENDENT, min degree 7")
produced [`computations/jet-algebraic-independence.witness.json`](../../computations/jet-algebraic-independence.witness.json),
which records `minimal_relation_degree: 7`, `nullspace_dim: 3` at `d = 7`, and
`nullspace_dim: 0` at `d = 5, 6` — each `stable: true` under a wide-margin re-run.
The bean was filed the same day.

The producer has changed **only** in `elapsed_sec` formatting since
(`79d21b2fda`, a float64-ratchet fix). The mathematics is byte-identical. So the
witness is not stale with respect to *its own producer*.

It is stale with respect to its **import cone** — AGENTS.md's documented hazard
("a producer's own source can be byte-stable while the module it *calls*
changed"). Both cone modules — `computations/knot_braid_database.py` and
`qou-mass/src/qou_mass/_internal/markov_trace_recursive.py` — changed in
`162d66eb7d`, *after* the witness was written.

## §2 What actually changed: the Markov parameter convention

`markov_trace_recursive.py:66` now reads

```python
z_sym = q**3 / (q**2 + 1)
```

which is **convention D**, made canonical by the owner ruling of 2026-08-15
("convention D is convention. excise convention C"). The witness predates that
migration and was computed under **convention C**, `z = sqrt(q)/(q+1)`.

This single fact explains the entire discrepancy, including the detail that
makes the bean title self-consistent on its own terms:

* Under **C**, `z` carries a literal `sqrt(q)`, so the traces genuinely lie in
  `Q(sqrt q)` — exactly as the bean says — and the minimal relation degree
  was measured as 7.
* Under **D**, no square root appears. The traces lie in `Q(q)`:

  | knot | `tr_M` (convention D, exact) |
  |---|---|
  | `4_1` | `(q^8 - q^6 + q^4 - q^2 + 1) / (q^2 (q^2+1)^2)` |
  | `5_2` | `(q^10 - q^8 + 2q^6 - q^4 + 2q^2 - 1) / (q^3 (q^2+1)^2)` |
  | `B_3` | `-(q^12 - 3q^10 + 2q^8 - 4q^6 + 2q^4 - 3q^2 + 1) / (q^4 (q^2+1)^2)` |

  The `(q^2+1)^2` denominators are the convention-D signature AGENTS.md names
  (one `(q^2+1)` per Markov peel; two peels for a 3-strand braid).

Per AGENTS.md's standing treatment of C-frame results, the degree-7 figures are
**correct for C and need scoping, not correction**. They are not a defect in the
2026-08-09 work.

## §3 Independent verification (three methods, no shared machinery)

[`computations/jet_algebraic_dependence_verification.py`](../../computations/jet_algebraic_dependence_verification.py).
Exact arithmetic throughout — sympy over `Q` and `Fraction`. No float anywhere;
the problem is algebraic, so exact is both available and required.

**Method 1 — field membership.** All three traces satisfy `free_symbols == {q}`:
they lie in `Q(q)`, `trdeg_Q = 1`.

**Method 2 — resultant elimination.** Eliminating `q` from
`num_K(q) - v*den_K(q)` pairwise gives non-zero resultants for all three pairs;
every pair is algebraically dependent. The `(4_1, B_3)` resultant has a
**degree-3** factor of multiplicity 4 that annihilates the pair.

**Method 3 — exact complete minimal-degree search** on the rational functions
themselves (no jets, no truncation, no stability question). Nullspace dim 0 at
total degree 1 and 2; dim **1** at degree **3**, giving

```
16 x^3 - 5 x^2 z - 19 x^2 + 11 x z - 2 x - 5 z^2 + 4 = 0,    x = tr_M(4_1), z = tr_M(B_3)
```

Methods 2 and 3 produce this **identical** polynomial by disjoint routes. It also
vanishes exactly at `q = 7/3, 2, -5/4, 11/7` under pure-`Fraction` arithmetic.

**Cross-check against the probe's own jets.** The relation annihilates the
*probe's own* `jet_series` output to order 40, all coefficients exactly zero — so
the probe's jets are correct and only its recorded verdict is C-frame. Re-running
the committed producer today gives nullspace dim **1 / 4 / 12** at `d = 3 / 4 / 5`
— against the witness's `0` at `d = 5`. The dims 1 and 4 are exactly the count of
multiples of a single degree-3 relation by monomials of degree `<= 0` and `<= 1`,
which is the consistency check that confirms degree 3 is minimal rather than
merely present.

## §4 The consequence — the actual bug

### `JetOrderIndependence` — the bean is right, and the name is the problem

```lean
class JetOrderIndependence where
  jacobianRank : ℕ → ℕ
  full_rank : ∀ N, 3 ≤ N → jacobianRank N = 3
```

This is a statement about the **rank of a matrix**. Rank is a linear-algebra
quantity; the class asserts nothing algebraic. The bean's "only a LINEAR rank
certificate" is **correct**, verified from the declaration rather than inherited.

Note this is *not* a contradiction with the dependence finding. Linear
independence of jet coefficient vectors and algebraic dependence of the
underlying functions are logically independent properties, and here **both hold
simultaneously**: rank 3 at the base order (elimination determinant `1/16`), and
a degree-3 algebraic relation. Nothing needs to be retracted — but the name
`JetOrderIndependence` invites exactly the conflation AGENTS.md §"Grep the claim
SHAPE" warns about, since the file's own prose glosses it as "the three series
are jet-order independent".

Also relevant to arity: `full_rank` is a **level-indexed family** (`∀ N`), not a
single proposition, and it is currently **uninstantiated** — the global instance
was removed because it fed `ofPivots` a fabricated constant
`jetPivots = fun _ => (1/4, 2, 1/8)` at *every* order (bean `qou-1n7g`). The
genuine sorry-free content is the base-order certificate alone.

### `JetTransportImpliesIndependence` — right conclusion, wrong reason

```lean
class JetTransportImpliesIndependence (E : TransportErrorData)
    [JetOrderIndependence] [SurrealParallelTransportBound E] : Prop where
  nonempty_independence : Nonempty HyperbolicVolumeIndependence
```

The bean says this "cannot be a transfer of independence" **because** the jets
are dependent. That reasoning does not go through, and the shape audit shows why:
**the class never mentions the tr_M jets at all.** Its conclusion is about
`vol_4_1, vol_5_2, vol_B3` — three *real numbers* — and its hypotheses are two
class binders. The jet dependence found here is a fibre-level statement about
`tr_M`, and (per the original probe's own scope warning) the `q -> 1` jet of
`tr_M` is not an expansion of `Vol(K)`. So the finding does not reach this class
by the route the bean claims.

The declaration is nonetheless defective, for a **different and more basic**
reason: it is a §3b-cond **item-5 violation — a self-assuming projection.** The
class's single field *is* the downstream conclusion, and the consumer

```lean
noncomputable def hyperbolicVolumeIndependence_of_reduction ... := R.nonempty_independence.some
```

is a bare projection that uses neither `[JetOrderIndependence]` nor
`[SurrealParallelTransportBound E]`. Both binders are decorative. AGENTS.md
§3b-cond item 5 is explicit: a class that "carries the block's own conclusion as
a field, with a 'theorem' that merely projects it" is vacuous, and satisfies the
propagation audit while failing `proof-statement-integrity`.

So the bean reaches a **correct verdict on this declaration through an argument
that does not support it**. The defect is real; the stated reason is not the one.

## §5 Scope classification (AGENTS.md)

The forcing argument is a **scope-(b) structural exclusion**, and the cited
invariant is the **transcendence degree**: `Q(q)` (equally `Q(sqrt q)`) has
`trdeg_Q = 1`, and any two elements of a trdeg-1 extension are algebraically
dependent over `Q`. Since the Taylor expansion map into `Q((g))` is a field
embedding, the relation transfers to the jets. No numerical probe is required
and none can overturn it; a probe can only measure the *degree*.

This is the one place where the convention change is genuinely irrelevant:
`trdeg_Q Q(sqrt q) = trdeg_Q Q(q) = 1`. **The bean's structural finding is
robust; only its measured degree was convention-dependent.**

## §6 Follow-ups

1. The committed witness `jet-algebraic-independence.witness.json` is
   convention-C-frame and should be **scoped** (labelled C), not deleted — its
   numbers are correct for C.
2. `JetTransportImpliesIndependence` needs restructuring per §3b-cond item 5 so
   the class carries genuine sub-hypotheses and the consumer *derives* rather
   than projects. Filed separately.
3. `JetOrderIndependence` remains uninstantiated and correctly so
   (`qou-1n7g`, `qou-xc8t`).
