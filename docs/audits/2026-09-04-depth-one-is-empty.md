# The +2 map exists; depth 1 is empty. And options of attack.

**2026-09-04, owner question:** *"does quadratic curvature term from frobenius
pairing provide mapping into order ≤ +2 from current level? we should see these
maps and operators are related to filtration."*

**Short answer: the +2 mechanism exists and I told you the opposite last turn.
It cannot fire from the interface layer, but not for the reason I gave — the
obstruction is that the depth-1 stratum is empty, and there is a structural
reason it might have to be.**

---

## 1. RETRACTION — `*_q` is depth-ADDITIVE, not depth-preserving

I wrote: *"the one composition law the grid records, `*_q`, **preserves** `n` —
depth-raising is exactly what the corpus does not have."*

**False.** `def:hq-bi-filtration`'s own compatibility table states:

| operation | effect on `(n, K)` |
|---|---|
| **convolution `*_q` (q-shuffle)** | `ℋ_q^(n₁,K₁) *_q ℋ_q^(n₂,K₂) ⊆ ⊕ ℋ_q^(n₁+n₂,K')` |
| coproduct `Δ_q` | `Δ_q(ℋ_q^(n,K)) ⊆ ⊕_{n₁+n₂=n} ℋ_q^(n₁,K₁) ⊗ ℋ_q^(n₂,K₂)` |
| bar involution | `ℋ_q^(n,K) → ℋ_q^(n,K*)` — depth-preserving, mirrors `K` |
| Markov trace `tr_M` | `ℋ_q^(n,K) → 𝒫_n/𝒫_{n−1}` — depth-preserving |
| braid action | depth-preserving |

That is a **filtered-algebra law**: the shuffle is depth-*additive*. Exactly one
of the five operations moves depth, and it is the product. I read the *grid
table's* summary cell ("preserves `n`") instead of the *definition's*
containment, and reported the cell. Sixth instance this session of the same
failure — read the definition, not the summary.

**So the owner's reading is right: a quadratic term maps `n → 2n`, i.e. `≤ +2`
from a depth-1 level.** The mechanism is in the corpus and is stated in the
defining block.

## 2. But it cannot fire from the interface, and here is the real obstruction

`⋈_K` and the whole convolution layer sit at **depth 0**, and `0 + 0 = 0`. A
quadratic in depth-0 objects is still depth 0. To reach depth 2 by squaring you
need a **depth-1** input.

**Measured: the depth-1 stratum is never instantiated anywhere in the corpus.**

* `def:hq-bi-filtration`'s own "low-`(n,K)` examples" grid has columns
  `ℋ_q^(0,K)`, `ℋ_q^(2,K)`, `ℋ_q^(3,K)` — **it skips `n = 1`.**
* `grep` for `\mathcal{H}_q^{(1` across every `.md` and `.lean` in
  `content/`: **zero hits.**

So the additive law has nothing to add. **The missing object is a depth-1
stratum, not a depth-raising law** — which is a much more specific gap than the
one I described yesterday.

### And there may be a reason it is empty

The same block's third downstream conjecture,
`rem:k-theory-period-rosetta`, matches **depth `n` to the Beilinson regulator on
`K_{2n−1}^ind(ℚ̄)`**. Under that dictionary:

| depth | `K`-group | content |
|---|---|---|
| 1 | `K_1^ind` | **indecomposable part vanishes** |
| 2 | `K_3^ind` | `Li_2` / Bloch–Wigner / **volume** |
| 3 | `K_5^ind` | `Li_3` / Chern–Simons |

`K_1(F) = F^×` is entirely *decomposable*, so its indecomposable part is trivial.
If the rosetta is right, **depth 1 is empty by construction, not by neglect** —
and the `n=1` column is missing from the grid because there is nothing to put in
it. **This is a hypothesis about the corpus's own dictionary, not a theorem**;
proving or refuting it is option (F) below.

Note the grid's depth-2 entries are already real: figure-eight `4₁` at
`ℋ_q^(2,K)` is `2·Cl₂(π/3)` — `Vol(4₁)`, marked **confirmed**.

## 3. The curvature 2-cocycle is real — on a THIRD filtration

`observations/confinement-curvature-rank.md` carries exactly the object the
question names, and it is not on the depth axis:

> The GB filtration `J⁰ ⊃ J¹ ⊃ ⋯` stratifies `A = H_n(R,q)` by **curvature-rank
> `k = depth(λ) − 1`**. […] `k ≥ 1`: extracting an element requires energy
> proportional to the **curvature 2-cocycle `F`** (the combined Hecke and
> Yang–Baxter obstruction). This is categorically the **string tension**.

So there is a genuine quadratic (2-cocycle) obstruction moving along a
filtration, and the unified mass formula already **sums over its layers**,
`𝔪 = Σ_{k=0}^{n−1} α_k 𝔪^(k)`. The owner's *"maps and operators are related to
filtration"* is precisely what the corpus asserts.

**But `depth(λ)` here is PARTITION depth, a third meaning.** Three filtrations
are now in play and conflating them is the standing hazard:

| # | filtration | index | what moves it |
|---|---|---|---|
| 1 | transcendence / iterated-integral | `n` — `G^(n)` adjoins `Li_n^q` | `*_q`, additively |
| 2 | knot / Hecke cell | `K`, refined by `λ_K ⊢ n_K` | braid action, cell merging |
| 3 | GB / curvature-rank | `k = depth(λ) − 1` | the 2-cocycle `F` |

The Frobenius co-Casimir sits at `k ≥ 4` ("universal residue, no specific
knot"); the chirality layer at `k = 3`. **Whether `F` moves axis 1 at all is not
established anywhere** — it is stated as an obstruction on axis 3.

---

## 4. Options of attack

Ordered by cost, with what each needs and what it would settle.

**(A) Act, don't map: use the `2 = 2 + 0` split.** `Δ_q` decomposes depth 2 as
`n₁ + n₂`; the `2 + 0` component pairs the **existing** depth-2 volume stratum
with the **existing** depth-0 interface. That is a *module* structure — the
convolution layer acting on the volume stratum — and it needs no new object at
all. Cheapest live route, and it does not require depth 1.
*Settles:* whether `⋈_K` acts on `ℋ_q^(2,K)` compatibly with `tr_M`.

**(B) Prove depth 1 is empty (or find it).** Take the `K`-theory rosetta
seriously and test it: if depth `n` ↔ `K_{2n−1}^ind`, then `K_1^ind = 0` forces
`ℋ_q^(1,K) = 0`. A proof converts today's gap into a **theorem** and prunes
every route that hoped to square a depth-1 object. A refutation is better still:
it hands you the missing input and (A)'s harder sibling `1 + 1 = 2` opens.
*Settles:* whether the +2-by-squaring route exists at all.

**(C) Curvature-rank instead of depth.** Attack on filtration 3, where the
quadratic object actually lives. The mass formula already sums over `k`, so the
consumers exist. *Needs:* establishing what `F` does to `⋈_K` specifically.
*Risk:* it may never touch the volume, which lives on axis 1.

**(D) Hadamard / creative telescoping** for connected sum — the only surviving
route after `ConnectedSumAnnihilator.lean` excluded the naive ideal map. Order
`≤ n₁·n₂`, operator-level, **does not cross depth**. Worth doing as the
template, not as the answer.

**(E) PGL(3) / Fock–Goncharov.** The corpus's own identified route past the
SL(2) ceiling (`qou-52fu`), with **35 held library directories and zero content
blocks** (`qou-960k`). Highest ceiling, largest lift, and the only option that
targets *flavour* rather than volume.

**(F) Do nothing on the bridge; drain the three-filtration collision.** Name the
three depths distinctly in the notation register. Cheap, and it is the direct
countermeasure to the error class that has produced six corrections today.

### Recommendation (my judgement, not a finding)

**(B) then (A).** (B) is a single structural question whose answer prunes or
opens everything else, and it is exactly the formalize-first move the repo
mandates — establish the invariant before running any search. (A) is the only
route that works with objects the corpus already has. (E) is the real prize but
should not start until (B) says whether the cheap bridge exists.

**(F) is worth doing regardless** and costs an hour.
