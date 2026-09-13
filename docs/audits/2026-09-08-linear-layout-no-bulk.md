# 2026-09-08 — Avenue 2 closed over the encoding: every expressible edge set is a linear layout, and a linear layout has no bulk

Bean `qou-brng`. Branch `claude/brng-avenue2-bulk-edge-set-2026-09-08`. Follows
[`2026-09-05-coordination-bulk-criterion.md`](2026-09-05-coordination-bulk-criterion.md), whose
§7 named this as its third option (*"attack the scope-(b): is every edge set the braid word can express affine?"*) and whose §5(i) narrowing this tranche removes. That §7 also worried the question might have to be posed at the braid-word layer "where it is harder"; it is posed there, and it is not harder — the layout is fixed by generator indices alone.

## 1. The question

Owner, 2026-09-08: *"Both derived edge sets on main are affine and an affine count can never be
a surface term, so ask what edge set has a bulk at all. That is decidable by a proved invariant
rather than a fit, and a negative closes Avenue 2 outright."*

The 2026-09-05 tranche proved the criterion — `HasBulk(A_surf) ⇔ A_surf → ∞ ∧ A_surf/A → 0` — and
showed both derived edge sets (production chain `A−1`, deltahedron `3A−6`) are affine, hence
`p = 1`, hence never a surface term. It stopped at a scope-(a): *"no **affine** edge set has a
bulk"*. What it could not say was whether the encoding could express a non-affine edge set at all.

## 2. The invariant: linear layout

The canonical word builder [`atom_braid_word_3A`](../../computations/mass_at_3A_proper.py) lays
block `k` of the ordering on strands `3k, 3k+1, 3k+2` and emits every inter-nucleon letter at
generator `3k+2` — between block `k` and block `k+1` of the ordering, and nowhere else. So the
nucleon pairs that share a letter are exactly the pairs **consecutive in the ordering**, whatever
the ordering, whatever the multiplicities `m_pp, m_pn, m_nn`, whatever the p/n convention. The
coordination graph is a subgraph of the path on the ordering. Call such a graph a **linear
layout**: every edge joins `k` and `k+1`.

This is not a property of the numbers in the word. It is a property of which generator index each
letter carries, and the letter values are never read to establish it — the invariant is
anchor-independent, convention-independent, and does not change under the 2026-09-05 intra-order
change (`qou-hu1f`), which moved only letters *inside* a block.

## 3. Lean — `QOU/Mass/LinearLayoutNoBulk.lean` (sorry-free)

Over `Fin n` with Mathlib's `SimpleGraph`. `lean -DautoImplicit=false -s 65536` exit 0 against the
restored cache; `#print axioms` on `linearLayout_family_not_hasBulk`,
`not_linearLayout_of_degree_ge_three`, `card_edgeFinset_eq`: `propext, Classical.choice,
Quot.sound` only; `card_edgeFinset_le` uses no axioms.

| declaration | statement |
|---|---|
| `LinearLayout G` | `∀ i j, G.Adj i j → i+1 = j ∨ j+1 = i` |
| `Chained G` | `∀ u w, Relation.ReflTransGen G.Adj u w` (connectedness, spelled as a chain of adjacencies — the cache holds no `Walk`/`Connected` olean; the notions coincide) |
| `degree_le_two` | linear layout ⇒ every degree `≤ 2` |
| `card_edgeFinset_le` | linear layout ⇒ `|E| ≤ n` |
| `not_linearLayout_of_degree_ge_three`, `not_linearLayout_of_card_edge_gt` | a vertex of degree `≥ 3`, or `|E| > n`, refutes linear layout |
| `chain_le_of_missing_edge` | with `{k,k+1}` absent, no chain from `≤ k` reaches `> k` |
| `chained_linearLayout_adj_succ`, `adj_iff` | connected linear layout ⇒ every consecutive edge present: it **is** the path |
| `degree_eq` | connected ⇒ `deg v = [0<v] + [v+1<n]` |
| `card_edgeFinset_eq` | connected ⇒ `|E| = n − 1` (affine, `p = 1`) |
| `surface_eq_two` | connected, `n ≥ 2` ⇒ `#{v : deg v ≤ 1} = 2` |
| `linearLayout_family_not_hasBulk` | a family of connected linear layouts, one per `A`, has `¬ HasBulk (A ↦ surface (G ⌊A⌋₊))` |

The last theorem is the one that answers the owner's question. The others are what make it
consequential: the three edge sets that *could* carry a bulk are all excluded by `|E| ≤ n`.

## 4. Probe — `computations/probes/linear_layout_no_bulk_probe.py`, **4/4**

Witness `computations/probes/linear-layout-no-bulk.witness.json` (`q0Anchor: independent`;
integer combinatorics only, no float, no `q₀` read).

1. **Position-based (bond-model) graph, every word the builder can produce for `A = 2..8`, every
   distinct ordering — 246 words, 42 of them the default sorted word.** Every one is exactly the
   path on the ordering: edge set `{(k,k+1)}`, `|E| = A−1`, max degree `≤ 2`, surface `2`,
   connected, interfaces `A−1`. This is the measured premise of the Lean's hypotheses
   (`LinearLayout ∧ Chained`).
2. **Strand-tracked graph.** Every letter `c·σ_g + d·1` has a `σ_g` component, so the strand
   permutation is branch-independent; tracking origin blocks through the word and recording an
   edge between the origin blocks of the two strands each letter acts on gives — measured, on all
   42 default words — **the same path**. The intra core `(σ₀σ₁⁻¹)³` permutes trivially and each
   interface is a single transposition, so no strand migrates far enough to meet a third block.
   (This was the one way the invariant could have failed; it does not.)
3. **What the bound `|E| ≤ A` excludes.** Max-contact / convex deltahedron `3A−6` exceeds `A` for
   every `A ≥ 4`; the complete graph `C(A,2)` — the count pyhecke's `build_atom_nf_exact` is —
   exceeds `A` for every `A ≥ 4`; the sub-affine true packing `6n − 0.926 n^{2/3}`
   (`MaxContactHasBulk`, the corpus's only bulk-carrying edge set) exceeds `n` for every `n ≥ 1`
   (checked via the weaker integer bound `6n − ⌈n^{2/3}⌉ > n`). None is expressible. At
   `A = 2, 3` the first two coincide with the path and are affine anyway.
4. **Surface count** of the expressible connected graph is `2` at every `A` measured.

## 5. Verdict — scope-(b) over the encoding

**No edge set that `atom_braid_word_3A` can express has a bulk.** A connected assembly is the
path: surface `2`, bond count `A−1`, `p = 1`, no bulk. A disconnected one is a disjoint union of
paths whose surface is twice its component count; a "bulk" there would be fragmentation into
unboundedly many chains, which the closure of a single braid word is not, and which the bond
model's connected-sum multiplicativity would factor away in any case.

The invariant that decides it is **linear layout**, a proved structural property of the encoding,
and the exclusion of every bulk-carrying candidate is by the proved bound `|E| ≤ n` — not by a
fit, not by a comparison with data. This is scope-(b) in the sense of AGENTS.md §"Before
declaring refuted": the invariant is cited and Lean-proved. Its scope is the **encoding**.

### What it does not say

- It does **not** say that no edge set anywhere has a bulk. The sub-affine true packing does
  (`MaxContactHasBulk.subAffine_hasBulk`). It says the encoding cannot express it.
- It does **not** derive a different layout. A bulk needs a strand layout in which one block
  touches three or more others — an interleaving of blocks across strand positions that the
  corpus derives nowhere. Choosing such a layout because it reproduces the surface term would be
  selection against the target (AGENTS.md §NO FITTING, "selection against the target"), and is
  not proposed.
- It does **not** touch the Route-C / `InteriorMarkov` question (`qou-gr3t`), which is about the
  *value* the bond product takes on this path, not about the graph.

### Consequence for `qou-brng`

Avenue 2 — *"find the edge set that supplies the surface term"* — is **closed over the encoding**.
The three-pronged narrowing of 2026-08-29/30 (complete graph by saturation, linear chain by
arrangement-dependence, body-order depth ≥ 3) is joined by a fourth that covers every edge set
the current encoding can produce at once. What remains of the extensive-term frontier is not an
edge-set question inside this encoding; it is either (i) a **different encoding** with a derived
non-linear layout, or (ii) an extensive term that is not a coordination count at all. Neither is
proposed here; both are open, and the bean records them as such.

## 6. Verification

- Lean: `lean -DautoImplicit=false -s 65536 QOU/Mass/LinearLayoutNoBulk.lean` — exit 0, no
  warnings after `omit`; axioms as in §3.
- Probe: `python3 computations/probes/linear_layout_no_bulk_probe.py` — 4/4, 0.04 s.
- `scripts/precision-gates.sh --changed`: see the PR body.
