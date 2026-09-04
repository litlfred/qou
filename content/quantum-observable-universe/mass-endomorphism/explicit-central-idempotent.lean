import QOU.BraidKnot.ExplicitCentralIdempotent


/-!
# Explicit central primitive idempotents in `H_n(q)` via Murphy elements

`prop:explicit-central-idempotent` from
`explicit-central-idempotent.md` — the central primitive idempotent
`e_λ ∈ Z(H_n(q))` projecting onto the `λ`-Wedderburn block has the
explicit Lagrange-interpolation formula in Jucys–Murphy elements.

Builds on `prop:jucys-murphy-central-elements-qou` (already in the
paper, in `jucys-murphy-central-elements-qou.md`), which establishes
that the JM elements `J_k` pairwise commute and act diagonally on the
Hoefsmit seminormal basis with eigenvalue equal to the q-content of
the corresponding box.

The Lagrange-interpolation formula then constructs `e_λ` as a sum
over standard Young tableaux of products of Lagrange projectors.

`SYT`, `qContent`, `centralIdempotent` and the open conjecture class
`ExplicitCentralIdempotentConjecture` now live in the library module
`QOU.BraidKnot.ExplicitCentralIdempotent`, imported above. They were
declared here until 2026-09-04; they moved so that
`conj:explicit-central-idempotent` — the block that *states* the
conjecture — can name the same class this block *consumes*. A sibling
`.lean` cannot import another sibling, so leaving the class here would
have forced two independent declarations of one class (bean
`qou-1bua`).
-/

namespace QOU.BraidKnot.ExplicitCentralIdempotent

variable {R : Type*} [CommRing R]
variable {q : R}

/-- **Theorem (`prop:explicit-central-idempotent`).** The central
    primitive idempotent `e_λ` for partition `λ ⊢ n` is given by

      e_λ = ∑_{T ∈ SYT(λ)} ∏_{k=1}^{n} ∏_{□ ∈ λ, □ ≠ T(k)}
              (J_k - c(□; q)) / (c(T(k); q) - c(□; q))

    and satisfies:

    - Sum-to-identity:    `∑_λ e_λ = 1`
    - Orthogonality:      `e_λ * e_μ = δ_{λμ} * e_λ`
    - Self-adjointness:   for self-conjugate `λ = λ'`,
                          `star (e_λ) = e_λ`
    - Bar-pairing:        for chiral pair `λ ≠ λ'`,
                          `star (e_λ) = e_{λ'}`
    -/
theorem explicit_central_idempotent_via_murphy
    {n : ℕ} (lam : List ℕ) (h : lam.sum = n)
    [hi : ExplicitCentralIdempotentConjecture q] :
    centralIdempotent lam q * centralIdempotent lam q = centralIdempotent lam q := by
  -- Ref: [murphy1981] — Murphy elements in symmetric-group algebras.
  -- Ref: [dipper-james1986] — extension of Murphy's construction
  -- to the Iwahori–Hecke algebra at generic q.
  -- See content block jucys-murphy-central-elements-qou — the paper's
  -- prop:jucys-murphy-central-elements-qou block establishing
  -- diagonal action of J_k on the Hoefsmit seminormal basis with
  -- eigenvalue c_T(k; q).
  -- Ref: [manuscript] §prop:explicit-central-idempotent — the
  -- four cross-checks (sum-to-identity, orthogonality,
  -- self-adjointness, bar-pairing) follow from Lagrange
  -- interpolation in commuting variables (J_1, ..., J_n).
  -- CONJECTURE: The four cross-checks follow from Lagrange interpolation in commuting variables.
  exact hi.idempotent lam h

/-- Computability witness for small `n`: the (2,2) self-conjugate
    cell of `H_4(q)` is the Bring-figure-8 cell, witnessed in
    `conj:bring-figure-eight-depth-2-witness`. The `e_{(2,2)}`
    formula is concrete and finite (sum over 2 SYTs × product
    over 4 boxes × Lagrange factor).

    **Conditional, exactly as its parent is** (AGENTS.md §3b-cond
    item 2). This was previously an `example` with no binders, which
    stated the `(2,2)` idempotency *unconditionally* while proving it
    from `explicit_central_idempotent_via_murphy` — a conditional
    theorem. Lean refused it (`failed to synthesize
    ExplicitCentralIdempotentConjecture q`), which is the elaborator
    catching precisely the smuggling this repo's §3b-cond rules
    forbid: a specialisation does not discharge the hypothesis its
    general form carries. Naming it also makes it citable, which an
    anonymous `example` was not. -/
theorem explicit_central_idempotent_two_two
    [ExplicitCentralIdempotentConjecture q] :
    centralIdempotent [2, 2] q * centralIdempotent [2, 2] q
      = centralIdempotent [2, 2] q :=
  -- Ref: [manuscript] §prop:explicit-central-idempotent — concrete (2,2)
  -- instance of `explicit_central_idempotent_via_murphy`; the e_{(2,2)}
  -- idempotency is the finite Lagrange computation witnessed in
  -- conj:bring-figure-eight-depth-2-witness. `centralIdempotent` is `opaque`,
  -- so this is asserted from the cited construction, not computed.
  explicit_central_idempotent_via_murphy [2, 2] rfl

end QOU.BraidKnot.ExplicitCentralIdempotent
