
## Assessment 2026-08-08 — NOT closed, and here is exactly why

Attempted after closing `spechtIso_imp_dom_both` (qou-6gwx). The cross-shape
machinery does **not** reach this, and I want the reason on record so the next
session does not re-derive the dead end.

### What was delivered instead

`SpechtClassification.dom_of_nonzero_hom` — Sagan Thm 2.4.4 in its general
**hom** form, sorry-free and axiom-clean:

    Hom_{k[S_n]}(S^μ, M^ν) ∋ θ ≠ 0  ⟹  μ ⊵ ν

The previously proved `dom_of_intertwiner` (iso form) is now a corollary: it is
the case `θ = (S^ν ↪ M^ν) ∘ e`. Extracting a surviving polytabloid from `θ ≠ 0`
is a span-induction over `SpechtSubmodule = span (range polytabloid)`.

This is the strongest form of the dominance bound and is what any route to
exhaustion will consume. It is not, by itself, enough.

### The dead end, precisely

`W` simple ⇒ a quotient of the regular module ⇒ (Maschke, char 0) a submodule
of it ⇒ `W ↪ M^{(1ⁿ)}`. Pick `ν` extremal in dominance with `W ↪ M^ν` and apply
`specht_submodule_dichotomy`:

* `S^ν ≤ W` ⇒ `W = S^ν` by simplicity. **Done.**
* `W ≤ (S^ν)ᗮ` ⇒ stuck.

Excluding the second branch needs to know **where the composition factors of
`(S^ν)ᗮ` live** — Young's rule. `dom_of_nonzero_hom` bounds such a factor by
dominance but does not assert one exists, so extremality has nothing to
contradict. Adding a hypothesis to dodge this is assuming the theorem.

### The two honest routes

**(a) Counting** — recommended. `#simples = dim_k Z(k[S_n]) = #conj classes =
#partitions`, then pigeonhole against the `#partitions` pairwise
non-isomorphic Specht modules (`specht_pairwise_noniso`, proved). Three Mathlib
gaps, all checked absent at the pinned revision:

1. `dim_k Z(k[G]) = #conj classes` — class sums are a basis of the centre. No
   centre-of-group-algebra API in Mathlib. ~150–250 lines.
2. `ConjClasses (Perm (Fin n)) ≃ Nat.Partition n` — Mathlib has
   `Equiv.Perm.partition` and `partition_eq_of_isConj`, but not the induced
   bijection, and not surjectivity of `partition`. The cheapest of the three.
3. `#{iso-classes of simple modules} = #Wedderburn blocks ≤ dim_k Z(A)` for
   semisimple `A`. `WedderburnSn.sn_wedderburnArtin` gives the decomposition
   with an **abstract** block count `N`; identifying `N` is the gap. Mathlib's
   `RingTheory/SimpleModule/Isotypic.lean` is the nearest API.

**(b) Young's rule / Specht filtration** of `M^ν`. Larger, and subsumes far
more than is needed.

### Sizing

Route (a) is 2–3 focused sessions and produces three reusable Mathlib-gap
modules. It is not a "finish the file" task. The docstring at the `sorry` site
now carries this analysis so it is not mistaken for a small remaining step.

### Do not

- Do not weaken the statement (e.g. by assuming `W` embeds in some `M^ν` with a
  dominance hypothesis) — that assumes the conclusion.
- Do not try to route it through `dom_of_nonzero_hom` alone; the branch above is
  where it fails.

## Progress 2026-08-08 (cont) — route (a), two of three bounds proved

`QOU/MathlibExt/GroupAlgebraCenter.lean`, sorry-free and axiom-clean:

    card_conjClasses_perm_fin_le        #conj classes of Sn ≤ #partitions of n
    finrank_center_le_card_conjClasses  dim_k Z(k[G]) ≤ #conj classes of G

### What made these cheap: state them as inequalities

The plan above asked for `#conj classes = #partitions` and
`dim Z = #conj classes`. The count only ever uses `≤`, and each equality's
*hard* half is the one the bound does not need:

- `≤ #partitions` needs only that `Equiv.Perm.partition` **separates** classes
  (`partition_eq_of_isConj`, in Mathlib). Surjectivity — every partition is a
  cycle type — is true, is **not** in Mathlib, and is not needed.
- `dim Z ≤ #conj classes` needs only that class sums **span** the centre. Their
  linear independence — that they are a basis — is not needed.

That is most of why this landed in one pass rather than the estimated two
sessions. Estimate the *bound*, not the theorem it comes from.

## The third bound: a materially better route than the one planned above

The plan called for `#{iso-classes of simples} ≤ dim_k Z(A)` via Wedderburn,
identifying `WedderburnSn`'s abstract block count. **Do not do that.** There is a
character route that skips the centre entirely:

    #{pairwise non-isomorphic simple k[G]-modules}
      ≤ dim_k {class functions on G}
      = #conj classes

because the characters of pairwise non-isomorphic simples are **linearly
independent**, and every character is a class function (`FDRep.char_conj`).

### The discovery that makes it work

`FDRep.char_orthonormal` carries `[IsAlgClosed k]`, which looks fatal for a
general characteristic-zero `k` (ℚ is not algebraically closed, and over it the
endomorphism division rings need not be `k`). But the lemma it is built from,

    FDRep.scalar_product_char_eq_finrank_equivariant :
      ⅟(card G) • ∑ g, W.character g * V.character g⁻¹ = finrank k (V ⟶ W)

carries **no `IsAlgClosed`** — only `[Fintype G] [Invertible (card G : k)]`,
which char 0 supplies. That is enough:

- off-diagonal: `V ≇ W` simple ⇒ `finrank (V ⟶ W) = 0`
  (`finrank_hom_simple_simple_eq_zero_of_not_iso`, also no `IsAlgClosed`);
- diagonal: `finrank (V ⟶ V) ≥ 1` since `id ≠ 0`.

So the Gram matrix of the characters is diagonal with nonzero (char-0) entries,
hence they are linearly independent. Algebraic closure is only ever needed to
pin the diagonal entries to `1`, which the bound does not care about.

### Consequence for this bean

`finrank_center_le_card_conjClasses` is **off the critical path** under the
character route — it bounds `dim Z`, which the character route never mentions.
It remains a legitimate standalone Mathlib gap-fill and is proved; just do not
build the Wedderburn block-count identification on top of it.

### What is actually left

The bridge from this repo's `Representation`/`IsSimpleModule` formulation to the
categorical `FDRep`/`Simple` one that Mathlib's character API is stated in:

1. `IsSimpleModule (MonoidAlgebra k G) ρ.asModule` ↔ `CategoryTheory.Simple` of
   the corresponding `FDRep k G` object. **No such bridge in Mathlib** — checked.
2. `(V ⟶ W)` in `FDRep k G` ↔ `Hom_{k[G]}(V, W)`; `Representation.invariantsEquivFDRepHom`
   is the nearest hook.
3. `IsRepIso` (this repo's hand-rolled intertwiner predicate) ↔ `V ≅ W` in `FDRep`.
4. Linear independence from a diagonal Gram matrix; class functions inject into
   `ConjClasses G → k`; assemble against `specht_pairwise_noniso`.

Alternatively redevelop 1–3 at the `Representation` level using
`Representation.averageMap` / `isProj_averageMap` / `invariantsEquivRepHom`,
which exist. That avoids the category plumbing but re-proves the scalar-product
formula, whose risky step is `trace (linHom ρV ρW) g = χ_V(g⁻¹) · χ_W(g)`.

Either way ~300–500 lines. The mathematics is settled; what remains is a
formulation bridge.

## Progress 2026-08-08 (cont 2) — the character API, on `Representation`

`QOU/MathlibExt/RepresentationCharacter.lean`, sorry-free and axiom-clean. The
character route of the previous section, redeveloped off the category layer:

    charOf                      χ_ρ(g) = tr (ρ g)
    charOf_conj                 characters are class functions
    linHom_comp                 dualTensorHom intertwines dual ρV ⊗ ρW with linHom
    charOf_linHom               χ_{Hom(V,W)}(g) = χ_V(g⁻¹) · χ_W(g)
    average_charOf              ⅟|G| • Σ_g χ_ρ(g) = dim_k ρ^G
    homG / mem_homG_iff         Hom_G(V,W) as invariants (linHom ρV ρW)
    charPairing_eq_finrank_homG ⅟|G| • Σ_g χ_V(g⁻¹)·χ_W(g) = dim_k Hom_G(V,W)

**No `IsAlgClosed`** anywhere, and no `FDRep`/`Rep` object. That removes the
bridge listed as the blocker in the previous section: the Specht cluster carries
bare `Representation`s and can now use the pairing directly.

### Friction worth recording — all instance-level, none mathematical

Every proof is Mathlib's `FDRep` proof with the category layer stripped, but the
plumbing fought back for a dozen compiles:

- `LinearMap.trace_conj'` sends `isDefEq` into `dualTensorHomEquiv`'s definition
  trying to unify `Module.End k (V* ⊗ W)` with `(V* ⊗ W) →ₗ[k] (V* ⊗ W)`. It does
  not terminate in a **million** heartbeats (78 s of `exact`). Replaced by
  `trace_comp_comm'` on composites, which keeps everything at the `→ₗ` level.
- `trace_comp_comm'` then leaves `M`, `N` as metavariables and the elaborator
  gets stuck on `Module.Finite k ?m`. Passing `(R := k) (M := …) (N := …)`
  explicitly is what finally lands it. This was the single blocking step.
- Type-ascribing `Module.Dual k V ⊗[k] W →ₗ[k] X` in a `set` picks
  `TensorProduct.addCommMonoid`, which will not `rw`-unify against
  `AddCommGroup.toAddCommMonoid` in Mathlib's `CommRing`-based trace section.
  Use `(…).toLinearMap` and let the instances be inferred.
- Stating the file over `[Field k]` vs `[CommRing k]` matters: `Field` gives the
  `Field → Semifield → DivisionSemiring → Semiring` path, the trace lemmas carry
  `CommRing → CommSemiring → Semiring`, and `rw` cannot bridge them. `Field`
  wins overall because `Module.Free`/`Module.Finite` on submodules
  (`invariants`, `ker averageMap`) are then automatic; over `CommRing` they must
  be carried as hypotheses.

### What is left

1. **Schur, at this level.** Non-isomorphic simple `k[G]`-modules have
   `homG ρV ρW = ⊥`, hence `finrank = 0`, hence the pairing vanishes. Needs the
   bridge `homG ↔ Hom_{k[G]}(asModule, asModule)` — `mem_homG_iff` is one half —
   plus `LinearMap.bijective_or_eq_zero`.
2. **Diagonal nonzero.** `id ∈ homG ρV ρV` and `ρV ≠ 0`, so `finrank ≥ 1`, and
   `(finrank : k) ≠ 0` in char 0.
3. **Independence ⇒ count.** A diagonal Gram matrix with nonzero entries gives
   linear independence of the `χ_i` inside class functions; class functions inject
   into `ConjClasses G → k`, so `#simples ≤ #conj classes`. Then chain with
   `GroupAlgebraCenter.card_conjClasses_perm_fin_le` and
   `specht_pairwise_noniso`.

Steps 1–2 are short. Step 3 is the assembly. The mathematics is finished; what
remains is bookkeeping of the same kind as above.
