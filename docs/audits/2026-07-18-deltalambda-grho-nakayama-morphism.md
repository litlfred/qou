# Is g_ρ the Nakayama automorphism of a graded Frobenius algebra? NO — Angle A refuted

**Date:** 2026-07-18 · **Axis:** Δ_λ closure (strong sector), open problem (i) — a
self-contained categorical morphism for the sign carrier `g_ρ` ·
**Follows:** the jet-order derivation [`2026-07-11-deltalambda-grho-jet-order-derivation.md`](2026-07-11-deltalambda-grho-jet-order-derivation.md),
the sign narrowing [`2026-07-11-deltalambda-sign-operator-narrowing.md`](2026-07-11-deltalambda-sign-operator-narrowing.md),
the magnitude reduction [`2026-07-11-deltalambda-magnitude-graded-trace.md`](2026-07-11-deltalambda-magnitude-graded-trace.md) ·
**Gate:** Track-A / Δ_λ (owner-reversed for-all 2026-07-13) · **Tier:** symbolic-exact
(sympy + mpmath, parameter-free) · **Scope: (a)+(b) NEGATIVE. No fit; nothing wired.**

## What this tests (open problem (i))

The Δ_λ per-partition binding density reduces (magnitude #3537 × sign #3529) to a single
object, the principal **row** grading `g_ρ`:

> `Δ_λ = tr_{V_λ}(g_ρ) = (−1)^{n(λ)}·dim(λ)`, magnitude `= dim(λ)` (classical `q=1`),
> sign `= q^{2n(λ)}|_{q=i} = (−1)^{n(λ)}`, with `n(λ) = Σ_box row(box) =
> min_{T∈SYT(λ)} maj(T)` the **fake-degree valuation** (Steinberg/Lusztig/Macdonald I.5).

The sign carrier is currently derived via a **cited** classical theorem + compute. Open
problem (i) asks for a **self-contained categorical morphism** for `g_ρ` from the drivers.
This audit tests one specific hypothesis (Angle A):

> **Angle A.** `g_ρ` = the **Nakayama automorphism** `ν` of the GS-jet-order-graded
> Frobenius algebra (the row-graded `q^{2ρ}` object) — distinct from the already-pruned
> **content**-graded ribbon self-twist (which is `+1` at ζ₄).

Probe [`deltalambda_grho_nakayama_probe.py`](../../computations/deltalambda/deltalambda_grho_nakayama_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-grho-nakayama-morphism.witness.json)
(12/12; `contentBlock: conj:binding-manybody-eq-jet-filtration`).

## The two proved invariants that bound the search

The Nakayama automorphism `ν` of a Frobenius algebra `(A, λ)` is defined by
`λ(ab) = λ(b·ν(a))`; `A` is **symmetric** iff `ν = id`. Two invariants (not fits):

- **INV-1 — commutative ⇒ symmetric ⇒ ν = id.** `λ(ab) = λ(ba)` holds trivially for a
  commutative algebra, so `ν = id` satisfies (and by uniqueness *is*) the Nakayama map.
- **INV-2 — semisimple ⇒ ν = id.** A Frobenius form on a semisimple `A = ⊕_λ M_{d_λ}(k)`
  is `λ(x) = Σ_λ c_λ·χ_λ(x)` with `c_λ ≠ 0`; each character `χ_λ` is symmetric
  (`tr(ab)=tr(ba)`), so `λ` is symmetric ⇒ `ν = id`.

A symmetric algebra's `ν = id` acts as `+1 (= q^0)` on **every** simple — never the
nontrivial scalar `q^{2n(λ)}` (which is `−1` on the odd-`n(λ)` partitions).

## The sweep (λ⊢3,4,5,6, all exact)

| Candidate graded Frobenius algebra | Simples indexed by | Nakayama `ν` | = `g_ρ = q^{2ρ}`? | Scope |
|---|---|---|---|---|
| **Coinvariant algebra `R_n`** (where `n(λ)` natively lives) | partitions λ | `id` (commutative, INV-1) | **No** → `+1`, not `q^{2n(λ)}` | (b) proved |
| **ℂS_n**, **generic `H_n(q)`** (the algebras carrying `V_λ`) | partitions λ | `id` (semisimple, INV-2) | **No** → `+1` | (b) proved |
| **0-Hecke `H_n(0)`** | compositions / subsets (`2^{n-1}`) | nontrivial (subset flip) | **No** → wrong index set | (a) structural |
| **nilCoxeter `NC_n`** | single simple (local) | nontrivial | **No** → 1 ≠ p(n) simples | (a) structural |
| **`gr H_n(q)`** (length filtration) | compositions (0-Hecke-type) | nontrivial | **No** → wrong index set | (a) structural |
| **Markov-trace pivotal twist** `θ_λ = q^{2(n(λ')−n(λ))}` | partitions λ | — (ribbon self-twist) | **No** → **content** grading, `+1` at ζ₄, pruned #3529 | (a) prior |

**Verified computationally (parameter-free):**

1. `Hilb(R_n) = [n]_q! = Σ_λ f^λ·R_λ(q)` for n=3..6 — so `V_λ` enters the coinvariant
   algebra with fake degree `R_λ(q)`, bottom degree `n(λ) = min maj(SYT(λ))`. This is the
   algebra where the row grading `n(λ)` *natively* lives — and it is commutative.
2. `H_3(q)` Hoefsmit seminormal reps self-validated (Hecke + braid + `Σ dim² = 6`); the
   regular symmetrizing trace `τ_reg = Σ_λ dim(λ)·χ_λ` satisfies `τ(ab)=τ(ba)` on 8
   random word pairs — concretely symmetric ⇒ `ν = id`.
3. `p(n) ≠ 2^{n−1} ≠ 1` for all n≥3 (3≠4, 5≠8, 7≠16, 11≠32) — the non-symmetric
   candidates cannot even *express* a partition-indexed scalar.
4. `gr T_i² = (q−q⁻¹)T_i` (leading, length-graded) — the length-associated graded is
   0-Hecke-type, composition-indexed.
5. At ζ₄, the **row** grading `q^{2n(λ)}` reproduces the Lean `deltaSign` target
   `(−1)^{n(λ)}` (λ⊢3,5,6), whereas the **content** grading `q^{2(n(λ′)−n(λ))}` gives a
   *different* ζ₄ sign for some λ — the content twist is the wrong object.
6. **L1 divergence** `Σ_λ |q^{2n(λ)}|_{ζ₄} − ν_id| = 22.0` over λ⊢3..6 (nonzero ⇒
   `ν = id ≠ g_ρ` quantitatively).

## Verdict — NO (Angle A refuted, honestly)

**The Nakayama automorphism of a natural graded Frobenius structure is NOT `g_ρ`.**

- On **every algebra whose simples are indexed by λ** (the coinvariant algebra `R_n`,
  ℂS_n, generic `H_n(q)` — all **symmetric**), the Nakayama automorphism is the
  **identity** by the proved invariants INV-1/INV-2, acting as `+1` on every `V_λ` — never
  the row grading `q^{2n(λ)}` [**scope-(b), proved exclusion**].
- The natural **non-symmetric** graded Frobenius algebras with nontrivial Nakayama
  (0-Hecke, nilCoxeter, `gr H_n(q)`) index their simples by the **wrong set**
  (compositions / a single local simple), so cannot carry `q^{2n(λ)}` [**scope-(a),
  structural**].
- The one natural **pivotal / ribbon** "Nakayama-like" self-twist,
  `θ_λ = q^{2(n(λ′)−n(λ))}`, is the **content** grading (col−row), is `+1` at ζ₄, and was
  **already pruned** (#3529/#3523) — it is not the row grading `g_ρ`.

**Consequence for open problem (i).** The Nakayama route does **not** supply a
self-contained categorical morphism for `g_ρ`. Open problem (i) **remains open**; the
correct, already-derived home for the sign carrier stays the GS/**jet-order (fake-degree
valuation) pivotal row grading** (the #3537-line derivation). This negative **saves** the
`nakayama_eq_principalGrading` Lean effort — there is no such lemma to prove, because the
equality is false — and refines the search away from Frobenius-Nakayama structure back to
the pivotal / jet-order construction.

Per "Axiomatization is NOT a Proof" and the anti-fit discipline: this is a clean
scope-(a)/(b) **negative**, not a fit and not a forced positive. Nothing is wired.

## Honest scope of the invariants

INV-1 and INV-2 are standard Frobenius-algebra facts (commutative/semisimple ⇒
symmetric ⇒ trivial Nakayama), verified concretely here for `R_n` (commutativity + the
`[n]_q!` Hilbert series) and `H_3(q)` (the symmetric symmetrizing trace). The
scope-(a) wrong-index arguments (0-Hecke `2^{n-1}` simples, nilCoxeter locality,
`gr H_n(q)` 0-Hecke-type) are structural counts, not exhaustive proofs that *no*
exotic graded Frobenius form exists — but they close every **natural** candidate in the
S_n / Hecke family, which is what Angle A proposed.

## Lean (hand-audited — NOT machine-verified in this sandbox)

The Lean toolchain is 403-blocked in this sandbox, so the compute is the primary,
verifiable deliverable. The genuinely-provable core of the negative is the proved
invariant INV-1 (symmetric ⇒ trivial Nakayama ⇒ ≠ a nontrivial grading), sketched as a
**hand-audited** lemma in
[`QOU/BraidKnot/NakayamaGradingObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/NakayamaGradingObstruction.lean).
It is stated over a generic `CommRing` (§7c) and is marked hand-audited-not-machine-
verified; CI is the gate for its `lake build`. The Lean does **not** re-derive the
fake-degree valuation (cited classical theorem, per the jet-order audit) and does **not**
assert Angle A — it records the obstruction that refutes it.

## Cross-references

- Jet-order derivation (the correct home): [`2026-07-11-deltalambda-grho-jet-order-derivation.md`](2026-07-11-deltalambda-grho-jet-order-derivation.md)
- Sign narrowing (pivotal, not JM/framing): [`2026-07-11-deltalambda-sign-operator-narrowing.md`](2026-07-11-deltalambda-sign-operator-narrowing.md)
- Magnitude reduction (`Δ_λ = tr(g_ρ)`): [`2026-07-11-deltalambda-magnitude-graded-trace.md`](2026-07-11-deltalambda-magnitude-graded-trace.md)
- Content-grading twist prune: sign capstone #3529 / narrowing #3523
- Off-scope (magnitude problem (ii), no overlap): cluster #3888 / #3875 / #3802
- Lean algebraic core (sign): `QOU/BraidKnot/PrincipalGradingJetOrder.lean`
