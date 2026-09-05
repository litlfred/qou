# The +2 map exists; depth 1 is un-instantiated (not empty). And options of attack.

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
If the rosetta is right, depth 1 would be empty by construction.

> ### 🛑 REFUTED the same hour, by the rosetta's own table
>
> **Depth 1 is not indexed by `K_1^ind`.** `rem:k-theory-period-rosetta`'s
> dictionary row reads **`1 | log_q | K_1(F) via Bloch logs | Dirichlet
> regulator`** — plain `K_1(F) = F^×`, *not* the indecomposable part. The `ind`
> qualifier means "modulo the image of products of lower K-groups", and at
> `n = 1` there are no lower K-groups to quotient by, so it is vacuous there.
> My inference applied the general `K_{2n−1}^ind` formula past the point where
> its qualifier means anything.
>
> Worse for the hypothesis: the rosetta's **status** column marks depth 1
> **"theorem"** — Dirichlet regulator plus Baker–Wüstholz on `log`-linear
> independence — making it the *most* established row in the table, better
> supported than depth 2 ("theorem (essentially)") and far better than depth 3
> ("mostly conjectural").
>
> **So depth 1 is populated in principle and empty only in practice.** The
> grouplike is `log_q`, the K-group is `F^×`, the field of definition for a
> Bring-embeddable knot is `ℚ(z_K)` — all supplied. What has never been built
> is the **knot-indexed** stratum `ℋ_q^(1,K)`.
>
> This *upgrades* option (B) rather than pruning it: the ingredient exists and
> is theorem-grade; the missing step is attaching it to a cell. And the target
> function shows the mechanism explicitly — Bloch–Wigner is
> `D(z) = Im Li₂(z) + arg(1−z)·log|z|`, whose **second term is literally a
> product of two depth-1 objects landing in depth 2**, i.e. the shuffle-square
> the owner asked about. It is formalised in the corpus as
> `QOU.Knot.KummerRadial.kummer`.

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

**(C) ~~Curvature-rank instead of depth.~~ 🛑 DEAD — the filtration itself is
excluded.** I proposed attacking on filtration 3, where the quadratic object
lives. Corpus-grep found that path already walked and closed:
[`2026-08-16-three-gb-filtrations-one-name.md`](2026-08-16-three-gb-filtrations-one-name.md)
finds **three inequivalent objects all written `J^•`** — a rewrite-count
(*"not obviously well defined"*), the image of the `ℓ`-th power of the rewrite
ideal (**provably `⊥` for every `ℓ ≥ 1`**), and the Coxeter-length span (fails
the dimension count at `n ≤ 3`). Its 2026-08-26 supersession
([`no-shift-rescues-the-word-partition-bridge`](2026-08-26-no-shift-rescues-the-word-partition-bridge.md),
bean `qou-wjbd`) excludes the third **for every `n ≥ 2`, with no re-indexing
repairing it**, concluding *"all three readings of `J^•` are excluded"* and
*"the citation does no work"*.

So the curvature 2-cocycle `F` has no established filtration to be a cocycle
**on**. Reviving this route means first repairing `J^•`, which two audits say
cannot be done by re-indexing.

**And this hits `conj:two-filtration-bridge` too** — the corpus's own statement
of the owner's question ("*the maps and operators are related to filtration*"),
conjecturing that iterated-integral depth and partition GB-depth are bridged by
the central idempotents `e_λ`, with
`d_II(λ) = 2` (self-conjugate) / `3` (chiral pair) / `min(depth_GB(λ), 2⌈n/2⌉)`.
That block **flags its own defect in its statement**: the cited stratification
*"stratifies by the curvature rank of **words** and supplies no
partition-indexed filtration, so this conjecture **presupposes** the very
word-to-partition step that is unestablished."* It cannot be used as-is.

Note also `d_II(λ)` is **never 1** except at the trivial cell `λ = (1)` — an
independent corroboration, from the bridge's own formula, that depth 1 is thin
on the knot axis.

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

**(B), and it is now a BUILD rather than a proof.** The refutation above
changed its character: depth 1 is not structurally empty, it is theorem-grade
and merely un-instantiated on the knot axis. So (B) is *construct `ℋ_q^(1,K)`*
— a `log_q`-level object indexed by the cell `λ_K`, over `ℚ(z_K)` — after which
the shuffle squares it into `ℋ_q^(2,K)` = volume, which is exactly the owner's
`≤ +2`. Bloch–Wigner's own `arg(1−z)·log|z|` term is the worked instance of
that square.

**(A) remains the cheap parallel** and needs no new object. **(E) is the real
prize** and is now the *only* untouched high-ceiling route, since (C) is dead
and (D) is a template rather than an answer.

**(F) is worth doing regardless** and costs an hour.
