**Conjecture (D22 Type-B folding closure, per CLAUDE.md §7b).**
*The $\mathfrak{sl}_n$ Cartan datum on the canonical atomic-braid
Hecke algebra $H_n(q)$ folds into a Type-B Cartan datum
$\mathrm{B}_{n/2}$ under the involution $\iota: \alpha_i \leftrightarrow
\alpha_{n-i}$.  The resulting Kashiwara crystal is a **symmetric
crystal** whose GS normal forms are **bar-involution invariant by
construction** (i.e., the bar Z/2 action is realised as a Cartan-
fold symmetry).  Stable matter = fixed points of the folded crystal;
antimatter = the $\iota$-orbit complement.  Under this folding, the
composite CPT operator
([`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density))
decomposes naturally as a tensor of:*

- *C from color-sheet flavor conjugation
  ([`conj:c-from-color-flavor-swap`](#conj:c-from-color-flavor-swap), D6)*
- *P from Type-B Cartan folding* (this conjecture)
- *T from Markov-trace cyclicity
  ([`conj:t-from-trace-cyclicity`](#conj:t-from-trace-cyclicity), D8)*

## The CLAUDE.md §7b authoring shortcut

Per [`CLAUDE.md`](../../../CLAUDE.md) §7b (symmetric-crystal techniques):

> **Type B folding for chirality / CPT.** To enforce matter–antimatter
> pairing structurally in the reduction engine, do not write custom
> Z/2 rules. Fold the $\mathfrak{sl}_n$ Cartan datum into a Type B
> datum; the resulting Kashiwara graph is a *symmetric crystal*, and
> its GS normal forms are bar-involution ($q \mapsto q^{-1}$)
> invariant by construction. Stable matter = fixed points of the
> folded crystal.

This conjecture **formalises** that authoring shortcut as a content
block — the structural mechanism that:

1. Generates the bar-involution invariance "for free" (no manual
   Z/2 axioms needed),
2. Identifies stable matter with crystal fixed points,
3. Decomposes CPT into D6 + D22 + D8 (with D22 standing in for
   the role D7 normally plays).

## Relationship to D6/D7/D8

The CPT decomposition I authored in PRs [#1162](https://github.com/litlfred/qou/pull/1162)
([D6](c-from-color-flavor-swap.md)) +
[#1168](https://github.com/litlfred/qou/pull/1168)
([D7](p-from-braid-mirror.md), [D8](t-from-trace-cyclicity.md))
gives one decomposition:

$$\mathrm{bar} = P \cdot C \cdot T.$$

Type-B folding provides an **alternative categorical realisation**
where the role of "P (braid mirror)" is replaced by "the Cartan-fold
Z/2", and the bar-invariance emerges from the Type-B symmetric-crystal
structure rather than from explicit $\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ braid manipulation.

The two decompositions are not redundant — they are **two views**
of the same CPT composite:

| View | Realises bar via |
|------|------------------|
| D6/D7/D8 (combinatorial) | explicit $\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ + q $\leftrightarrow$ $q^{-1}$ on Hecke generators |
| **D22 Type-B folding** (categorical-symmetric-crystal) | structural fold automorphism $\iota: \alpha_i \leftrightarrow \alpha_{n-i}$ |

The D22 view is **more compact** (no need to track three separate Z/2
actions) but **requires more category theory** (Kashiwara crystal +
folding). CLAUDE.md §7b recommends D22 as the authoring shortcut for
new content; D6/D7/D8 are the explicit decomposition for blocks that
need separate access to each component.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: per-atom; the Type-B folded crystal has
  the same Coxeter length as the unfolded $\mathfrak{sl}_n$ crystal,
  with stable-matter corresponding to length-preserving fixed points.
- **Jet order**: $h^0$ (the folding is a structural symmetry, not a
  q-deformation effect).
- **Bar-symmetry status**: bar-symmetric **by construction** —
  Type-B folding IS the realisation of bar-invariance as a crystal-
  level structure.

## Lean axiomatisation (sketch)

```lean
class TypeBFoldingCPT (M : Type*) [BrCategory M] [Crystal M] where
  /-- The Type-B Cartan folding automorphism. -/
  iota_cartan_fold : Crystal → Crystal
  /-- Folding is an involution. -/
  iota_involution : ∀ c, iota_cartan_fold (iota_cartan_fold c) = c
  /-- GS normal forms of the folded crystal are bar-invariant. -/
  folded_gs_nf_bar_invariant :
    ∀ (β : Braid n), bar_involution (gs_nf_folded β) = gs_nf_folded β
  /-- Stable matter = crystal fixed points. -/
  stable_matter_def : MatterState → Prop
    := fun s => iota_cartan_fold s.crystal = s.crystal
  /-- CPT = D6 ⊗ D22 ⊗ D8 alternative decomposition. -/
  cpt_via_type_b :
    cpt_composite = c_color_swap ⊗ iota_cartan_fold ⊗ t_trace_reverse
```

## Open R&D

1. **Verify Type-B folding produces bar-invariant GS normal forms**
   numerically on the canonical atomic-braid catalogue
   ([`isotope_record_schema.py`](../../computations/isotope_record_schema.py)).
2. **Identify stable-matter crystal fixed points** for ${}^{2}\mathrm{H}$, ${}^{4}\mathrm{He}$
   (Wigner SU(4) supermultiplet — see [D11](wigner-su4-from-spin-isospin.md))
   and verify the prediction that these atoms correspond to folded-
   crystal singlets.
3. **D22 to closed** requires the Lean class `TypeBFoldingCPT` inhabited
   via the explicit $\iota$ map, plus the folded-GS-NF bar-invariance
   proof.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D22
  + §2 Cluster A alternative
- [`CLAUDE.md`](../../../CLAUDE.md) §7b authoring shortcut
- D6/D7/D8 explicit CPT decomposition:
  [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md),
  [`conj:p-from-braid-mirror`](p-from-braid-mirror.md),
  [`conj:t-from-trace-cyclicity`](t-from-trace-cyclicity.md)
- Composite CPT:
  [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
- Wigner SU(4) fixed-point story: [`conj:wigner-su4-from-spin-isospin`](wigner-su4-from-spin-isospin.md) (D11)
- [Brundan-Kleshchev 2009; Kashiwara 1991; Lecouvey 2007 for Type-B crystals]
