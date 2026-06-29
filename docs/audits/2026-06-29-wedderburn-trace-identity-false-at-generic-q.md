# 2026-06-29 — `Σ_λ d_q(λ)² = [n]_q!` is false for the concrete keystone `qDim` (scope (b))

**Bean:** `z2bn` (lever-1 keystone) / `08a2` (keystone de-abstraction).
**Branch:** `claude/wlambda-mtc-keystone-residual-i-2026-06-29`
**Trigger:** picking up the `wedderburn_trace_identity` `sorry` (cited "sibling #2743") as the last
input to `heckeLocalization`'s `D² ≠ 0`. Formalize-first verification of the target **before**
proving it found the target is false.
**Scope tag:** (b) structural exclusion — a polynomial-identity disproof (cited invariant: explicit
coefficient mismatch at n=2, below). Not a chat-only skepticism; gated by the corpus-grep + the
symbolic proof.

## The claim

[`mass-theory/wedderburn-trace-identity.md`](../../content/quantum-observable-universe/mass-theory/wedderburn-trace-identity.md)
(Proposition) and the library theorem
[`BraidKnot/wedderburn_trace_identity.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/wedderburn_trace_identity.lean)
(`sorry`, conditional on `HeckeQHookDimension`) both assert, for the Hecke algebra `H_n(R,q)` at
generic `q`:

$$\sum_{\lambda \vdash n} \dim_q(\lambda)^2 \;=\; [n]_q!.$$

## Disproof for the concrete keystone `qDim` (scope (b))

The concrete `dim_q` the keystone Lean actually computes is
[`QPartitionCombinatorics.qDim`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QPartitionCombinatorics.lean)
`= [n]_q! / ∏_{c∈λ} [h_c]_q` (the **hook principal specialization**). With **that** `qDim`,
symbolic computation (exact, sympy) gives, as **polynomials in q**:

| n | `Σ_λ qDim(λ)²` | `[n]_q!` | equal? | at q=1 |
|---|---|---|---|---|
| 2 | `2` | `q+1` | **no** | both `2` |
| 3 | `q²+2q+3` | `q³+2q²+2q+1` | **no** | both `6` |
| 4 | `3q⁴+4q³+8q²+4q+5` | `q⁶+3q⁵+5q⁴+6q³+5q²+3q+1` | **no** | both `24` |
| 5 | `3q⁸+…+7` | `q¹⁰+…+1` | **no** | both `120` |

Cited invariant (the (b) license): at **n=2**, `Σ qDim² = 1²+1² = 2` is a *constant* while
`[2]_q! = q+1` is *degree 1* — unequal as polynomials. The two sides agree **only at q=1**, where
`qDim → f^λ` (ordinary SYT count) and `[n]_q! → n!`, recovering the genuine
`Σ_λ (f^λ)² = n!`.

The `.md`'s own "Explicit values" table is internally inconsistent under this reading: it writes
`n=2: Σ = 1 + 1 = 2.230` — but `1 + 1 = 2`, not `2.230 = [2]_{q₀}`.

## The correct identities (both verified n=2..5, exact)

1. **Vector-space (q-independent):** `Σ_λ (f^λ)² = n!` — `dim H_n(q) = n!`. Already proved
   sorry-free in the corpus: `RegularRepBlockTrace.sumSq_dim_eq` (PR #2724, ordinary `dimHLF`).
2. **Poincaré / major-index (the genuine q-identity):**
   $$[n]_q! \;=\; \sum_{w\in S_n} q^{\operatorname{maj}(w)} \;=\; \sum_{\lambda\vdash n} f^\lambda \cdot q^{b(\lambda)}\,\dim_q(\lambda),\qquad b(\lambda)=\textstyle\sum_i (i-1)\lambda_i,$$
   because `q^{b(λ)}·dim_q(λ) = Σ_{T∈SYT(λ)} q^{maj(T)}` (the q-hook-length formula). Verified
   exact for n=2..5. Note this is `Σ f^λ·(q^{b}·dim_q)`, **not** `Σ dim_q²`: the correct summand is
   the *ordinary* dimension times the maj generating function, and it carries a `q^{b(λ)}` factor
   the bare `dim_q` drops.

So the written `Σ dim_q² = [n]_q!` conflates (1) and (2): it uses `dim_q²` where (2) needs
`f^λ·q^{b(λ)}·dim_q`, and `[n]_q!` where (1) needs `n!`.

## Disposition (no overclaim)

Two readings of the `.md` proposition; the defect is real under either:

- **(a) `dim_q` = the concrete hook specialization** (what the Lean computes, and what any
  `D² = Σ dim_q²` consumer uses): the identity is **false** (above). The `sorry` is unprovable as
  stated; "#2743" cannot close it.
- **(b) `dim_q` = a different object** (e.g. a Markov-trace / MTC weight): then the library
  `wedderburn_trace_identity.lean`, which is consumed with the concrete `QPartitionCombinatorics`
  `qDim`, is a **`.lean`↔`.md` mismatch** — the formal statement does not model the intended
  proposition.

**Owner adjudication needed:** which `dim_q` does the descent/weight-partition consumer intend, and
should the proposition be restated as the Poincaré identity (2) (ordinary dim × maj gen function) or
the vector-space identity (1)? Either way the current `Σ dim_q² = [n]_q!` should not stand as
written, and the `sorry` should not be "proved" (its statement is false under the concrete reading).

## Effect on residual (i) / `heckeLocalization`

None adverse — it removes a false dependency. `heckeLocalization`'s only structural input is
`D² = Σ_λ dim_q(λ)² ≠ 0` (`globalDim_ne`), the **concrete** sum — which does **not** equal `[n]_q!`
and does **not** need this identity. It is discharged directly from positivity (`1 < q` ⇒
`qBracket_pos`/`qFactorial_pos` ⇒ `qDim > 0` ⇒ `Σ dim_q² > 0`), independent of the false claim. The
earlier workplan/docstring note "`D² = Σ d_q² = [n]_q!`" is corrected to "`D² = Σ d_q² ≠ [n]_q!`".

## Consumer investigation (2026-06-29) — verdict (a), and the false claim is NON-load-bearing

A corpus sweep of the consumers settles the disposition and bounds the blast radius.

**Verdict: (a) — the statement is false under its only coherent reading.** The `.md` explicitly
defines `dim_q(λ)` as the hook specialization `[n]_q!/∏[h_c]_q` (= `QPartitionCombinatorics.qDim`),
the `.lean` uses that concrete `qDim`, and every consumer expects the partition-indexed hook-qDim.
It is **not** a `.lean`↔`.md` `dim_q` mismatch (option (b) is ruled out).

**Consumers (cite the identity):** `wigner-coefficient-derivation(.ts/-proof.md)`,
`em-spectral-completeness.ts`, `symbolic-character-table.ts`, `mass-categorical-descent.md`,
`mass-coefficient-shadow-price-proof.md`, `appendix .../mba-step05-wedderburn.ts`.

**But the false identity is invoked, not used.** What the consumers actually depend on is sound:
- `[n]_q!` as an **algebraic scale** (e.g. `λ_W = [5]_q!·m_e`) — well-defined, independent of the
  sum equality.
- `w̃_λ := d_q(λ)²/[n]_q!` as a **per-block weight ratio** (LP duality / shadow prices /
  `wedderburn-weight-canonical.md`) — a ratio, which does **not** require `Σ_λ d_q² = [n]_q!`.
- The genuine normalization is a **different, true** identity:
  `Σ_λ d_λ·y_λ(q) = 1` (ordinary dim `d_λ=f^λ` × Markov weight `y_λ`), Plancherel completeness
  in [`y-lambda-recipe-from-partition.lean`](../../content/quantum-observable-universe/mass-theory/y-lambda-recipe-from-partition.lean)
  (verified < 10⁻¹⁵, n≤12). Note `y_λ = w̃_λ` only on **self-conjugate** λ; they differ (ratio
  0.14–2.54 at q₀) off the diagonal (`wedderburn-weight-canonical.md`) — so even the
  `w̃_λ = d_q²/[n]_q!` weight is not the Markov weight in general.

So the "partition of the total Markov weight" the proposition claims to provide is really carried by
`Σ_λ d_λ·y_λ = 1`, not by `Σ_λ d_q² = [n]_q!`.

**Recommended fix (owner adjudicates):** restate `prop:wedderburn-trace-identity` as one of —
1. the **Markov normalization** `Σ_λ d_λ·y_λ(q) = 1` (the identity consumers actually rely on; already
   formalized), **or**
2. the **Poincaré/maj** `[n]_q! = Σ_λ f^λ·q^{b(λ)}·d_q(λ)` (the genuine q-identity for `[n]_q!`), **or**
3. the **vector-space** `Σ_λ (f^λ)² = n!` (#2724, already sorry-free) —
and update the ~6 consumers' citations (mechanical; their real dependency is sound). The `sorry` in
`wedderburn_trace_identity.lean` must **not** be "proved" (its statement is false).

## Resolution (2026-06-29, owner-approved option 1)

Restated `prop:wedderburn-trace-identity` to the **Markov-trace normalization**
`Σ_λ d_λ·y_λ(q) = 1` (option 1). Changes on this branch:

- **Proposition** `wedderburn-trace-identity.md` / `.ts`: new statement; `lean.ref` repointed from
  the false sorry'd `QOU.BraidKnot.wedderburn_trace_identity` → the true
  `QOU.BraidsAndKnots.plancherel_via_recipe`; `authorNote` records the correction. The "scale vs
  weight" distinction (`[n]_q!` scale; `w̃_λ=d_q²/[n]_q!` ratio; neither = `Σd_q²`) is now in the body.
- **Proof** `wedderburn-trace-identity-proof.md`: replaced the bogus "q-deform each factor" step with
  the genuine `tr_M(1)=Σ y_λ d_λ=1` derivation.
- **Library Lean** `BraidKnot/wedderburn_trace_identity.lean`: **removed** the false sorry'd theorem +
  its self-justifying `HeckeQHookDimension` premise (a `sorry` on a false statement is a landmine);
  kept only `qInt`/`qFactorial`; docstring records the disproof + the true decls. Compiles exit 0.
  Nothing imported the removed decl.
- **Consumer prose** de-conflated (cite `[n]_q!` as the Hecke scale / the Markov normalization, not
  the false sum): `wigner-coefficient-derivation-proof.md`, `mass-categorical-descent.md`,
  `mass-coefficient-shadow-price-proof.md`, **plus two the top-6 sweep missed** —
  `unified-iterative-correction-proof.md`, `frobenius-self-duality-forces-lp-dual-extraction-proof.md`.
- **Already correct (left as-is):** `plancherel-term-7-formulation-proof.md` independently documents
  the identity as false and uses the vector-space `Σ(dim V_λ)²=n!` — prior corpus acknowledgment.

Mass/binding numbers unchanged (the false sum was never computed; consumers use `[n]_q!` directly and
the per-block ratios). Validation infra (folio-assistant) is proxy-blocked in this env; verified by
hand (lean.ref resolves to a real theorem; library Lean compiles; prose is schema-conforming).

## Reproduce

```bash
python3 - <<'PY'
import sympy as sp
q=sp.symbols('q')
def qbr(n): return sum(q**i for i in range(n))
def qfac(n):
    r=sp.Integer(1)
    for k in range(1,n+1): r*=qbr(k)
    return sp.expand(r)
def parts(n,m=None):
    if m is None:m=n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for r in parts(n-k,k): yield (k,)+r
def conj(l): return tuple(sum(1 for r in l if r>j) for j in range(l[0])) if l else ()
def hooks(l):
    c=conj(l); return [(l[i]-j-1)+(c[j]-i-1)+1 for i in range(len(l)) for j in range(l[i])]
def qdim(l):
    d=sp.Integer(1)
    for h in hooks(l): d*=qbr(h)
    return sp.cancel(qfac(sum(l))/d)
for n in range(2,6):
    print(n, sp.simplify(sum(qdim(l)**2 for l in parts(n)) - qfac(n))==0)
PY
```
