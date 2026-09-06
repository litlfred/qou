# The canonical word's extremality is GROUPED-specific — it dies under the ruled-correct word

**Settles** the conjecture #6714 left open at `p ≈ 0.024`: *does the canonical
ordering maximise `f₁/f₀` among orderings of its own letters?* Answered by the
directed test that document named, for **both** intra orderings.
Beans `qou-brng` / `qou-pdg9` / `qou-hu1f`.

## Measured — exhaustive over the 1-swap neighbourhood

    intra_order   canonical   neighbours   range        above   verdict
    grouped         37/2         196       8 .. 37/2      0     LOCAL MAXIMUM
    borromean        1/2         196      −1 .. 17      110     NOT a local max

`pn` free word, `n = 6`, 22 letters, `P = 3`, exact `Fraction`. Every distinct
transposition of two letters; swapping identical letters is a no-op and skipped.
385 s and 393 s respectively.

## The finding

**Under `grouped` the conjecture survives; under `borromean` it is refuted, and
not marginally — 110 of 196 neighbours (56 %) beat the canonical word.**

So the extremality is **not a property of canonicality**. It is a property of
the *grouped assembly*, and it does not transfer to the word the owner ruled
correct (`qou-hu1f`).

## It is a maximum, but NOT a strict one

Under `grouped`, `max(neighbours) = 37/2 = canonical`. Since the canonical value
is not itself in the neighbour list, **at least one 1-swap neighbour ties it**.
The honest statement is *a* maximum, not *the* maximum, and not strict.

## What this joins

Three independent properties are now measured grouped-specific:

1. **Per-generator/per-letter factorisation** — grouped factorises to `~3e-59`;
   interleaved fails by `2.8×`–`13.3×`
   (`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe`).
2. **The six `c₁` values** and their `c1_from_letters` derivation (bean
   `qou-j1e5`).
3. **This extremality.**

The reading — offered as interpretation, not measurement — is that contiguity is
what all three depend on: the grouped word puts each generator's letters
together, and factorisation, per-letter additivity and extremality are all
consequences of that. The Borromean word interleaves and has none of them.

**This does not argue the ruling is wrong.** It says the grouped word's
tidiness was a consequence of contiguity rather than evidence of correctness —
which is the opposite of how a nice property is usually read.

## Scope, and what is NOT established

- **One nucleus** (`pn`, `n = 6`), one precision (`P = 3`).
- **Local, not global.** 196 neighbours out of `22!/(11!·7!·4!) = 232,792,560`
  orderings. A 1-swap-exhaustive result says nothing about 2-swap or further.
  No number of random draws would establish a global maximum either — which is
  why #6714's `p ≈ 0.024` was correctly labelled suggestive.
- **Not a claim about the physics.** This is the expansion of a computational
  object. Scope-(a).
- The `borromean` refutation is decisive *for that ordering*; the `grouped`
  local-max is a positive result at the weakest useful strength.

## Method note — the trap this walked into first

The first attempt called `atom_canonical_crossings` **unpinned**, so it measured
the Borromean word (canonical `1/2`) while testing a grouped-word conjecture,
and reported seven "beating" swaps that meant nothing. Both orderings are now
pinned explicitly. This is the same unpinned-default failure the whole arc has
been about, in a script written after documenting it — the default is load
bearing and inheriting it silently is the recurring defect, not a one-off.
