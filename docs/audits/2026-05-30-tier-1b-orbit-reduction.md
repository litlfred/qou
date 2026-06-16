# Tier 1.B — nucleon-orbit reduction: implemented + roadmap corrected

**Date:** 2026-05-30
**Trigger:** Owner — implement Tier 1.B (now unblocked by the proven
orbit-trace identity, #1483).
**Builds on:** [`2026-05-30-orbit-trace-identity-proof.md`](2026-05-30-orbit-trace-identity-proof.md)
(the identity) and §1.B of
[`2026-05-20-compute-optimization-roadmap.md`](2026-05-20-compute-optimization-roadmap.md)
(the original — and partly mistaken — plan).
**Deliverables:**
[`atom_orbit_reduction.py`](../../computations/atom_orbit_reduction.py)
(API) +
[`orbit_reduction_crosscheck.py`](../../computations/orbit_reduction_crosscheck.py)
→ `tier-1b-orbit-reduction-crosscheck.witness.json`.

## TL;DR — what Tier 1.B actually is

The roadmap framed Tier 1.B as the *single largest open speedup* — "36× ⁶Li,
576× ⁸Be, the gateway to organic chemistry" — via

> `tr_M(β_{Z,N}) = |orbit| · tr_M(rep)`,  `|orbit| = Z!·N!`.

Both halves of that are wrong, and the corrected picture is the deliverable:

1. **The formula has no `|orbit|` multiplier.** The proven identity is
   `tr_M(β_{Z,N}) = tr_M(rep)`. `orbit_size = Z!·N!` is **audit metadata**,
   never a trace factor. A literal implementation of the roadmap formula
   would have made `m(⁴He)` **4× too large** and `m(⁸Be)` **576× too large**.
2. **The 36×/576× reduce-speedup is illusory as framed.** It assumed the
   current reduce walks `|orbit|` permuted words and the orbit-quotient
   walks one. It does not — `atom_braid_word_3A` already emits the single
   canonical `p…pn…n` word. There is no `|orbit|`-fold enumeration to
   collapse.
3. **The real benefit is correctness + a proof that production is already
   optimal.** The canonical `p…pn…n` ordering is *interface-minimal*, and
   production already uses it. The identity proves that choice is both
   valid (trace is representative-independent) and cheapest.

## Evidence (measured this session)

### The identity and the metadata

| atom | (Z,N) | `orbit_size` (metadata) | interfaces | canonical `n_pn` |
|------|-------|------------------------:|------------|:----------------:|
| ⁴He | (2,2) | 4 | {pp:1, pn:1, nn:1} | 1 |
| ⁵Li | (3,2) | 12 | {pp:2, pn:1, nn:1} | 1 |
| ⁶Li | (3,3) | 36 | {pp:2, pn:1, nn:2} | 1 |
| ⁸Be | (4,4) | 576 | {pp:3, pn:1, nn:3} | 1 |

The canonical word from `atom_braid_orbit_representative(Z,N)` is
**byte-identical** to the production `atom_braid_word_3A(Z,N)` (verified for
every case above) — the production compute path is unchanged.

### Ordering-dependence — full-S_A is *not* a symmetry

A same-species permutation `σ ∈ S_Z × S_N` leaves the word unchanged
(Lemma 1), so there is nothing non-trivial to check at the *trace* level for
the orbit action — the word is literally the same. The only non-trivial
arrangements are **cross-species** reshufflings (full `S_A`), and those give
genuinely **different** braids and **different** traces:

| ordering (Z=N=2) | interfaces | `tr_M` @50dps | reduce wall |
|------------------|-----------|---------------|------------:|
| `ppnn` (canonical) | {pp:1, **pn:1**, nn:1} | `0.05534833516376856681` | **12.8 s** |
| `pnpn` (interleaved) | {**pn:3**} | `0.05952107403930675795` | 29.1 s |

So `tr_M` depends on the species *ordering*, not just the multiset — full-S_A
is not a symmetry. Only the same-species `S_Z × S_N` (which fixes the word)
is, which is exactly why `tr_M(β)=tr_M(rep)` and there is no orbit averaging
or multiplier.

### Interface-minimality → the canonical ordering is the cheapest

The canonical `p…pn…n` has **exactly one** `pn` crossing (the single
proton→neutron boundary); every other ordering of the same multiset has more
(`pnpn`→`pn:3`, `pnnp`→`pn:2`). The mixed `pn` crossing `(1, -h/2)` is the
expensive one in the LaurentQ reduce: the interface-minimal `ppnn` reduces in
**12.8 s** vs `pnpn`'s **29.1 s** (~2.3× at A=4; the gap widens with A as more
interleavings become possible). Production already uses the canonical
ordering, so it is **already at this optimum** — there is no further speedup
to extract here, only the guarantee that the choice is correct and minimal.

## Cross-check (`orbit_reduction_crosscheck.py`)

- **Structural (A≤8, no trace):** canonical ordering, `orbit_size` metadata,
  interface-minimality (`n_pn == 1 == global min`), byte-identical production
  word — for (1,1),(2,1),(2,2),(3,2),(3,3),(4,3),(4,4).
- **N1 — `|orbit|`-factor guard (³He = (Z=2,N=1), orbit_size = 2!·1! = 2):**
  `tr_M_via_orbit_representative(2,1) == tr_M_atomic_fast(2,1)`. A stray
  `Z!·N!` factor would make these differ by exactly 2×; they agree to
  < 1e-40. This is the regression guard against anyone re-introducing the
  roadmap's multiplier.
- **N2 — ⁴He value smoke:** `tr_M_via_orbit_representative(2,2)` reproduces
  the post-re-pin canonical `0.0553483351…` @50dps.

## Consequence for "organic chemistry" tractability

The roadmap pinned tractable ¹²C on the orbit-quotient. Since that quotient
does not reduce the work (production already walks one canonical word), the
path to heavier atoms is **not** Tier 1.B. It is:

- **Tier 1.A** — the Rust LaurentQ reduce (already landed, #1440 audit), which
  attacks the actual bottleneck (`reduce_laurent`, ~80% of ⁶Li wall); and
- a possible **intermediate-state memoisation** inside the reduce of the
  single canonical word (orbit-equivalent *reduction-tree* states, per the
  identity proof's roadmap-correction note) — **unverified**; it requires
  permuting strand-blocks on reduced words, which hits a representation
  artefact in the Markov-peel recursion (noted in the identity proof's
  follow-ups). Scoped as research, not a 3-5 day engineering item.

**Net:** Tier 1.B is *implemented* as a correct, metadata-carrying API with a
`|orbit|`-factor regression guard, and the roadmap's headline speedup is
retired as illusory. The genuine win is a high-value negative result — the
project is saved from (a) a catastrophic `Z!·N!` mass error and (b) spending
"3-5 days" chasing a phantom optimization.

## Follow-ups

- Lean formalisation of Lemma 1 (word-construction invariance) + the
  interface-minimality of the canonical ordering, tracked with the
  identity-proof Lean follow-up.
- If A ≥ 7 atoms become a wall, investigate the intermediate-state
  memoisation (research-grade; needs the strand-block conjugation realised
  without the Markov-peel representation artefact).
