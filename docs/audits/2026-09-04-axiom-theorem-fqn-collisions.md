# Two fully-qualified names are declared as both an `axiom` and a `theorem`

**Measured 2026-09-04 on `origin/main`** (3529 `.lean` files; 177 axioms, 22,402
theorems). Namespace resolution tracks `namespace`/`end` nesting, so these are
genuine FQN matches, not bare-name coincidences — of which there are 8 more,
and which mean nothing.

| FQN | axiom | theorem |
|---|---|---|
| `QOU.categorical_jet_prolongation` | `lifting-and-descent/categorical-jet-prolongation.lean` | `lean/QOU/QuantumObservableUniverse/Instanton.lean` |
| `QOU.transfer_matrix_level_independence` | `mass-theory/categorical-transfer-matrix.lean` | `mass-theory/transfer-matrix-level-independence.lean` |

## I expected the `delta_max_uniform_bound` shape. Neither is.

The obvious hypothesis was: *an axiom asserts what the corpus proves elsewhere,
so delete the axiom* — the shape that made `seminormalDim_pos` and the
`delta-max-uniform-bound` stub removable. **Both hits fail that hypothesis, and
in the same way: the two declarations state different mathematics.**

**`categorical_jet_prolongation`.** The sibling axiom is an *existence* claim,

```lean
axiom categorical_jet_prolongation (C) [Category C] [MonoidalCategory C]
    (fh : FrobeniusHopfData C) : ∃ (jet : JetPreservesQU C), jet.original = fh
```

while the library theorem is a *commutation identity*,
`cj.jetEval ≫ jp.connection = jp.prolonged_connection ≫ cj.jetEval`, proved by
projecting a structure field (`jp.commutes`). The library does **not** prove the
sibling's existence claim, so **the axiom must stay.**

**`transfer_matrix_level_independence`.** Two content-block siblings:
`(T₁ T₂ : CategoricalTransferMatrix q) → T₁.base = T₂.base → T₁.vertex_volume =
T₂.vertex_volume` on one side, and `∀ H p, p = foldl (·*·) 1 → p =
H.compositePolynomial` on the other. Vertex volumes against polynomial
products — unrelated propositions under one name.

## Consequence, and why it is currently benign

Under AGENTS.md §0a a `lean.ref` resolves to the block's **own sibling** first,
so each of the two `lean.ref`s that exist lands on the right file today:
`prop:transfer-matrix-level-independence` reaches the polynomial-product
version, and `prop:categorical-jet-prolongation` reaches the existence axiom.
No block currently reaches the wrong proposition.

What the collision costs is that the vertex-volume axiom in
`categorical-transfer-matrix.lean` is **orphaned under a name that means
something else** — nothing refs it, and anything that later refs
`QOU.transfer_matrix_level_independence` by name gets the other proposition.
The fix is a rename, not a deletion; neither is urgent.

## A detector caveat, on my own instrument

The "theorem" side of the `transfer_matrix` row is
`theorem transfer_matrix_level_independence … := transfer_matrix_level_independence_axiom …`
— a projection of a **local axiom in the same file**. Syntactically a theorem;
epistemically an axiom with an extra hop. So the label "declared as both an
axiom and a theorem" over-promises: read it as *"declared twice, under one
name"*, and check what the theorem's proof term actually is before concluding
anything is proved.

## Precedent worth knowing about

`transfer-matrix-level-independence.lean` carries a note recording that a
previous `transfer_matrix_path_independence_axiom` used `True` as its
isotopy-equivalence hypothesis, making it equivalent to `∀ tm1 tm2 : R_q, tm1 =
tm2` — **inconsistent**, since `R_q = LaurentPolynomial ℤ` has more than one
element — and was **removed 2026-05-17**.

So the corpus has already found and fixed an inconsistent axiom of exactly the
class recorded in `qou-4paj` (the two false nucleon-mass axioms). That is a
useful precedent for the disposition question there: the corpus's own answer,
last time, was to remove it and say why in place.
