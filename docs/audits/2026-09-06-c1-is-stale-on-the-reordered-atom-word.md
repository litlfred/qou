# `qou-pdg9`'s six `c₁` values are the pre-2026-09-05 atom word — and the floor share is 85 %, not 22 %

**Date:** 2026-09-06
**Beans:** `qou-pdg9` (completed — should be reopened), `qou-zrx2`, `qou-hu1f` (the ruling that moved
the word)
**Probe:** [`c1_is_stale_on_the_reordered_atom_word_probe.py`](../../computations/probes/c1_is_stale_on_the_reordered_atom_word_probe.py)
**Scope:** (a) scope-limited. Exact `Fraction`/integer arithmetic for `[★]`; the cross-check is
`mpf` at 60 dps end to end. No witness, nothing wired, no Lean edited.

## The finding

Bean `qou-pdg9` is marked **completed**. It derived `c₁`, the ℏ_q¹ coefficient of
`tr_M(W_free) − tr_M(W_atom)`, two independent ways, recorded six exact dyadic rationals, and
carried them into `QOU/MassTheory/PairwiseChainLeadingOrder.lean` as `def`s with a closed form. It
completed **2026-09-03**.

**The atom word changed on 2026-09-05.** Owner ruling `qou-hu1f` moved each nucleon's confinement
core from grouped `σ₀³σ₁⁻³` to the alternating `(σ₀σ₁⁻¹)³` its own source comment always named,
because `σ₀` and `σ₁` do not commute and only the alternating word is `β_Bor`. That reordering moved
absolute traces by `3.785×` (²H) to `14.325×` (⁴He).

All six recorded values are the **grouped** word's:

| case | `c₁` recorded (grouped) | `c₁` canonical (borromean) | ratio |
|---|---|---|---|
| pp | 19/8 | **1/8** | 19 |
| pn | 37/16 | **1/16** | 37 |
| nn | 9/4 | **0** | ∞ |
| T | 163/64 | **1/64** | 163 |
| ³He | 85/32 | **1/8** | 85/4 |
| ⁴He | 259/128 | **7/128** | 37 |

Six of six moved.

## Two independent routes

**1. `[★]`, `qou-pdg9`'s own Part-B formula**, reimplemented:

```
d tr_M/dε|₀  =  2^(−n) · Σ_ℓ w_ℓ · 2^(c(word with letter ℓ deleted))
```

with `w_ℓ = 1 + d′_ℓ(0) ∈ {+1, −1, 0, 0}` for `σ` / `σ⁻¹` / averaged / colour-weighted. **Its
self-test is that it reproduces all six recorded rationals exactly under `grouped`** — six
independent dyadic values, which a wrong implementation does not hit by accident. That is what makes
the canonical column a statement about the word rather than about the code.

**2. The live trace machinery**, `tr_m_atom_via_transfer.tr_m_atom_zn`, with no reference to `[★]`.
Deuteron, `(Δtr − c₀)/ℏ_q` along `q = exp(η)`:

```
η = 1e-3 → 0.0632870    1e-4 → 0.0625782    1e-5 → 0.0625078    1e-6 → 0.06250078
```

Converging on `1/16 = 0.0625` with `O(η)` error — not on `37/16 = 2.3125`, which is **37× away**.

## Why nothing flagged it

The sibling result in the same arc **did** survive. `c₀(A) = 2^(−A) − 2^(1−2A)` is a pure cycle
count, and cycle counts are blind to letter order — measured invariant under `intra_order` **and**
under `pn_convention`
([the parity probe](../../computations/probes/classical_floor_is_interface_parity_probe.py)). So the
floor, `ClassicalTraceFloor.lean`, and every ℏ_q⁰ statement are untouched by the reordering.

`c₁` is the **first** order that can see letter order at all, and it sits one bean over, already
marked completed. **A reordering that provably cannot move the leading term is not evidence about
the next one** — that inference is what let this through, and it is the reusable lesson here.

## The floor share is 85 %, not 22.46 %

`qou-zrx2` sizes its own complaint with `Δtr(D) = 0.556544660404`, a **grouped** value. Recomputed
at the canonical `q₀` on the canonical word:

| atom | `Δtr` | `c₀` | floor share | `qou-zrx2` said |
|---|---|---|---|---|
| D | 0.14704667798041 | 1/8 | **85.007 %** | 22.46 % |

The floor did not move; its denominator did. On the canonical word the deuteron binding observable
is ~85 % a **`q`-independent topological term**. That does not weaken `qou-zrx2`'s complaint — it is
the same complaint, roughly four times larger. ⁴He is not recomputed here (`H_12` trace, slow);
`--with-he4` includes it.

## What is stale

- `QOU/MassTheory/PairwiseChainLeadingOrder.lean` — the six `c₁` `def`s.
- `QOU/MassTheory/LeadingOrderTraceCoefficient.lean` — the Part-B derivation, stated for the old
  word.
- The closed form `c₁(Z,N) = (21Z + 16N)·(2^(−A−1) − 2^(−2A)) − 4·(I_pp − I_nn)·2^(−2A)`.
- `qou-zrx2`'s floor shares (22.46 % D, 4.88 % ⁴He).
- `qou-pdg9`'s status. It should be **reopened**.

**Not stale:** `c₀`, `ClassicalTraceFloor.lean`, the floor closed form, the interface-parity
generalisation, and every ℏ_q⁰ conclusion.

### Be precise about what "stale Lean" means here — two different things

The Lean was **not** invalidated in one uniform way, and saying so loosely would be the same
scope conflation this corpus keeps having to correct.

- **Mis-scoped, still true.** `LeadingOrderTraceCoefficient.lean:156-161` proves
  `c1Closed_pp : c1Closed 2 0 = 19 / 8` and five siblings. These are `norm_num` facts *about the
  definition `c1Closed`* and remain true — nothing about them is refuted. What is wrong is the
  **identification** of `c1Closed` with the ℏ_q¹ coefficient of the canonical atom word. Same for
  the `def c1_pp : ℚ := 19 / 8` family in `PairwiseChainLeadingOrder.lean:77-83`: a `def` asserts
  nothing, so it cannot be false; its docstring's claim about what it denotes is what moved.
- **A wrong datum.** `LeadingOrderTraceCoefficient.lean:222-224` hardcodes `letters_pnAtom`, the
  per-letter `(w, c(σ⁽ˡ⁾))` data of the pn atom word, and proves
  `star_pnAtom : starSum 6 letters_pnAtom = 37 / 16`. That table **is** the grouped word's letter
  data. The theorem is still true of the table; the table is no longer the canonical word's.

So the repair is a re-derivation of the inputs plus a re-statement of what the definitions denote —
not a retraction of any proof. No Lean is edited in this branch.

## This is the third instance of the same root cause, found independently

A sibling landed `63a50799b8` on `main` at 04:35Z, while this branch was being written, with the
same shape from a different direction: the free-word **extremality** conjecture (#6714) is a local
maximum under `grouped` (0 of 196 one-swap neighbours beat the canonical) and **refuted** under
`borromean` (110 of 196 beat it, 56 %). Its conclusion — *"extremality is NOT a property of
canonicality; it belongs to the grouped assembly and does not transfer to the word the owner ruled
correct"* — is this document's conclusion for a different quantity.

So the 2026-09-05 reordering has now invalidated three prior results (`c₁`, the floor **share**, and
extremality) and left one standing (`c₀`, invariant because it is a cycle count). Two agents found
two of them within an hour of each other without coordinating. **That is a rate, not a coincidence:
treat any pre-2026-09-05 quantity computed from the atom word as suspect until its
`intra_order`-invariance is checked, and check it by computing both orderings rather than by
reasoning about whether it "should" depend on letter order.**

## What this does not claim

Not that `qou-pdg9`'s derivation is wrong — the method is sound and this probe is built on it; the
*inputs* changed under it. And no new closed form in `A` is proposed: the six canonical values are
recorded exactly and left as data. Guessing a closed form from six points is how this arc has been
burned before, and finding the real one is the reopened bean's work.
