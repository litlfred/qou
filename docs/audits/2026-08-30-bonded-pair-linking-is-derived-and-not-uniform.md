# What fixes the linking number of a bonded pair — derived, and it is not uniform

**Date:** 2026-08-30 · **Bean:** `qou-k12x` (parent `qou-y2l3`) ·
**Probe:** [`bonded_pair_linking_from_canonical_braid_probe.py`](../../computations/probes/bonded_pair_linking_from_canonical_braid_probe.py)
**Answers:** `qou-zbgu` · **Bears on:** `qou-klgu` (merged), `qou-izah`, `qou-ooqh`

## The question

[`2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md`](2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md)
claimed a scope-(b) exclusion needing **every bonded pair to have `lk = 1`**;
`binding_mn_milnor_linking.py:188` models the **triton** — all three of whose
pairs are bonded — as `BORROMEAN` with pairwise `lk = [0,0,0]`. Bean `qou-zbgu`
recorded the contradiction and left the question: *what fixes the linking
number of a bonded pair?*

## The answer

**The canonical braid word does, and it fixes it non-uniformly.**
`mass_at_3A_proper.atom_braid_word_3A(Z, N)` is the corpus's source of truth for
the atomic braid, and the owner's Option-A ruling (2026-08-29) makes its closure
the nucleus's knot. Reading the inter-nucleon interfaces out of it — the
crossings `include_inter=True` adds and `include_inter=False` drops:

| iso | A | interfaces | at generators |
|---|---:|---|---|
| D | 2 | `averaged_weighted` (no sign) | 2 |
| T | 3 | `averaged_weighted`, `sigma_inv` (−1) | 2, 5 |
| ³He | 3 | `sigma` (+1), `averaged_weighted` | 2, 5 |
| ⁴He | 4 | `sigma` (+1), `averaged_weighted`, `sigma_inv` (−1) | 2, 5, 8 |

The four interface elements, as Hecke elements `σ_g + d·1`:

| ctype | `d` | in the braid group? |
|---|---|---|
| `sigma` | `0` | yes — `σ_g`, sign +1 |
| `sigma_inv` | `−h` | yes — `σ_g⁻¹` (from `σ² = hσ + 1`), sign −1 |
| `averaged` | `−h/2` | **no** |
| `averaged_weighted` | `−h(½ − δ/4)` | **no** |

## Three consequences

**(1) `bonded ⇒ lk = 1` is FALSE, derived.** ⁴He's three interfaces carry
`+1`, no sign, and `−1`. This strengthens `qou-zbgu`'s retraction of `qou-klgu`
from *"premise not established"* to **"premise false"**.

**(2) `bonded ⇒ lk = 0` is also false.** Two of ⁴He's three interfaces are
genuine signed braid generators, so the triton's uniform `lk = 0` is not the
canonical word either. **Neither branch of the `qou-zbgu` dichotomy is what the
corpus's own canonical object contains.**

**(3) The p–n interface has no classical linking number at all.** It is
`σ_g − h(½ − δ/4)·1`, strictly between `σ` (`d = 0`) and `σ⁻¹` (`d = −h`), hence
**not in the braid group**. A linking number is an invariant of a *link*; this is
a linear combination of an over- and an under-crossing. Promoting it to a
classical link requires **choosing** a representative.

That choice — not a wrong value — is the unforced step `qou-zbgu` was looking
for. Every `μ̄` count in the `M_n` tower silently classicalises a Hecke element.

## 🛑 CORRECTION 2026-08-30 — the "fourth thing" below is NOT new, and the
## corpus had already RESOLVED it

I presented the `A−1` vs `C(A,2)` disagreement as something found on the way and
"larger". **The corpus states it explicitly and settled it.**
[`theta_mn_linearchain_vs_allpairs.py`](../../computations/theta_mn_linearchain_vs_allpairs.py)
is about exactly this question, derives the interface positions
`{3k−1 : k = 1..A−1}` from the recipe JSON, and closes:

> "RESOLUTION: the mba-9b color-averaging note's `binom(A,2)` is superseded by
> the linear-chain `A−1` count. (A distinct all-pairs mean-field model would
> need its own derivation; the canonical braid does not realise it.)"

with the body-order aggregate `Σ(A−n+1)(n−1) = binom(A+1,3)` **Lean-proved**
(`prop:linear-chain-bond-count`). Re-run today, it passes.

**It is also ahead of me on the interfaces.** That file already records the
**channel** mapping — `pp→σ`, `pn→averaged`, `nn→σ⁻¹` — which I did not have: I
found the three types but did not identify which pair type each belongs to. My
independent counts confirm it exactly (⁴He = `σ`, `averaged`, `σ⁻¹` at gens 2,
5, 8 ⇒ pp, pn, nn; T ⇒ pn, nn; ³He ⇒ pp, pn; D ⇒ pn). So my "the mirror pair
differs in its interfaces" note is just the known pp/nn asymmetry, not a new
observation.

**What survives as new in this audit**, and it is narrower than I claimed:

1. the algebraic decomposition `σ − d·1 = a·σ + b·σ⁻¹` with `a + b = 1`, and
   that `averaged` is **exactly** ½:½ — the classicalisation argument;
2. the consequence for the Milnor premise, i.e. the retraction of `qou-klgu`;
3. the derived representative and its 0.069 % margin.

**And the residual question is a DRAIN question, not a discovery.** If the
resolution is the chain, why do **57 witness-emitting files** still compute a
`C(A,2)`/clique bond set? That is stale consumers of a superseded convention,
which is actionable and mechanical — not the unknowing inconsistency I implied.

## A fourth thing, found on the way — SEE THE CORRECTION ABOVE BEFORE READING

**The canonical braid is a chain of `A−1` interfaces** (D 1, T 2, ⁴He 3, at
generator indices 2, 5, 8 — exactly the boundaries between consecutive 3-strand
nucleon blocks). The max-contact contact-graph model used throughout the `M_n(K)`
programme asserts `C(A,2)` bonded pairs (D 1, T 3, ⁴He 6).

| iso | A | braid interfaces (`A−1`) | contact graph `C(A,2)` |
|---|---:|---:|---:|
| D | 2 | 1 | 1 |
| T | 3 | 2 | 3 |
| ⁴He | 4 | 3 | 6 |

**They agree only at A = 2.** So the clique-counting programme and the canonical
braid word disagree about *which pairs are bonded*, before any linking number is
assigned. Every clique count in `gap2_borromean_triple_count.py` and in my own
`gap2_irreducible_triple_bracket_probe.py` is taken against the contact graph,
not against the canonical braid.

## Also worth recording — the mirror pair differs in its interfaces

T is `(averaged_weighted, sigma_inv)` and ³He is `(sigma, averaged_weighted)`.
The isospin mirror shows up directly in the interface signature, not only in a
Coulomb correction. Not pursued here; noted because a mirror-splitting argument
built on identical interfaces would be wrong.

## Scope

scope-(a) on the interface reading — it reports what the canonical word contains
and what follows for the two uniform link models. Claim (3) is structural and
cites the algebra (the element is not in the braid group), but **excludes
nothing**: a derivation that *fixes* a classical representative would define a
linking number, and nothing here says one cannot exist.

**That is the next question, and it is sharper than the one this answers:** is
there a derivation that fixes the classical representative of the averaged
interface — or is the `M_n` tower's whole link-invariant framing applied to an
object that does not admit one?

## Reproduce

```bash
python3 -u computations/probes/bonded_pair_linking_from_canonical_braid_probe.py
```
