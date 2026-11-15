import QOU.Shared.MarkovTraceClaim

/-!
# QOU.BraidsAndKnots.qmn_recursive_memoized

**Canonical declaration** for content block qmn recursive memoized.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

Note: the chapter-dir uses singular `QOU.BraidKnot` for most blocks;
this plural `QOU.BraidsAndKnots` namespace was inherited from existing
`.ts` lean.ref URIs (a pre-existing convention drift).
-/

namespace QOU.BraidsAndKnots


/-- Abstract context for the `qmn_recursive_memoized` claim — manuscript-named
    typed fields below; the `holds` field carries the `Prop`-valued
    claim of the lemma. -/
class QmnRecursiveMemoizedContext extends QOU.Shared.MarkovTraceContext where
  /-- Character value `χ^λ_ρ` for partition `λ` and cycle type `ρ`, valued in
      the inherited coefficient ring `R` of the parent Markov-trace context
      (§7c: the q-character is a Laurent polynomial in `q`, not a real). -/
  chi : ℕ → ℕ → R
  /-- Recursion result via border-strip removal. -/
  chi_recursion : ℕ → ℕ → R
  /-- Manuscript sub-claim (i) — Cache identity: memoized lookup
      agrees with the recursive computation (the recursion is the
      authoritative answer). -/
  claim_i_looks_up_cache : ∀ lam ρ : ℕ, chi lam ρ = chi_recursion lam ρ
  /-- Border strips of size `ρ_1` in `λ`, as the list the recursion sums
      over.  Carrying the enumeration as a field is what lets sub-claim
      (ii) below be *stated*: the recursion's content is the sum, and a sum
      needs an index set. -/
  borderStrips : ℕ → ℕ → List ℕ
  /-- Height `ht(ξ)` of a border strip, supplying the sign `(-1)^{ht(ξ)}`. -/
  stripHeight : ℕ → ℕ
  /-- Character of the reduced pair `χ^{λ ∖ ξ}_{ρ ∖ ρ_1}` — the recursive
      call's value. -/
  chiReduced : ℕ → ℕ → ℕ → R
  /-- Manuscript sub-claim (ii) — the border-strip recursion: the recursive
      value is the signed sum over border strips of size `ρ_1`,

      `χ^λ_ρ = Σ_{ξ ∈ BS(λ, ρ_1)} (-1)^{ht(ξ)} · χ^{λ∖ξ}_{ρ∖ρ_1}`.

      **This is the Murnaghan–Nakayama rule, written out.**  It was
      `claim_ii_miss_computes_via : Prop` with a `_holds` witness beside
      it — a field typed with the *universe* `Prop`, so the instance chose
      the proposition and `⟨True, trivial⟩` discharged it.  The docstring
      said the recursion "stays abstract because it requires enumeration of
      border strips"; the enumeration is now a field, so it does not. -/
  claim_ii_border_strip_recursion : ∀ lam ρ : ℕ,
    haveI := ringR
    chi_recursion lam ρ =
      ((borderStrips lam ρ).map
        (fun ξ => (-1 : R) ^ stripHeight ξ * chiReduced lam ρ ξ)).sum
  /-- Cache lookup operation `cache_get λ ρ` returns `some v` on hit,
      `none` on miss. -/
  cache_get : ℕ → ℕ → Option R
  /-- Manuscript sub-claim (iii) — Cache invariant: when the cache
      returns a value, it equals the canonical character value (the
      stored result is faithful — no mutation effect). -/
  claim_iii_stores_result_cache : ∀ (lam ρ : ℕ) (v : R),
    cache_get lam ρ = some v → v = chi lam ρ
/-- **Proposition statement** (from manuscript):

The classical Murnaghan-Nakayama rule expresses $\chi_\rho^\lambda$
recursively via border-strip removal:*

$$
  \chi_\rho^\lambda \;=\; \sum_{\xi \in BS(\lambda, \rho_1)}
                          (-1)^{\mathrm{ht}(\xi)} \,
                          \chi_{\rho \setminus \rho_1}^{\lambda \setminus \xi}
$$

*where $BS(\lambda, \rho_1)$ is the set of border strips of size $\rho_1$
in $\lambda$, $\mathrm{ht}(\xi)$ is the height of strip $\xi$, and
$\rho \setminus \rho_1$ is $\rho$ with its first part removed.*

*The

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/qmn-recursive-memoized.ts
def qmn_recursive_memoized [ctx : QmnRecursiveMemoizedContext] :
    (∀ lam ρ : ℕ, ctx.chi lam ρ = ctx.chi_recursion lam ρ) ∧
    (∀ lam ρ : ℕ, haveI := ctx.ringR
      ctx.chi_recursion lam ρ =
        ((ctx.borderStrips lam ρ).map
          (fun ξ => (-1 : ctx.R) ^ ctx.stripHeight ξ * ctx.chiReduced lam ρ ξ)).sum) ∧
    (∀ (lam ρ : ℕ) (v : ctx.R), ctx.cache_get lam ρ = some v → v = ctx.chi lam ρ) :=
  ⟨ctx.claim_i_looks_up_cache, ctx.claim_ii_border_strip_recursion,
   ctx.claim_iii_stores_result_cache⟩

end QOU.BraidsAndKnots
