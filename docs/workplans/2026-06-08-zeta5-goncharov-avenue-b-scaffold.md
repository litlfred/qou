# Avenue B scaffold — discharge Goncharov's depth-3 at ℚ(ζ₅) via a Markov-trace realization

**Date:** 2026-06-08
**Branch:** `claude/vigilant-fermat-SROph`
**Parent:** [`conj:qou-infra-discharges-goncharov-zeta5`](../../folio/quantum-observable-universe/appendix-surreals/qou-infra-discharges-goncharov-zeta5.md)
**Status:** formalize-first **preflight**. States the constraints that prune the
search for the Hecke element *before* any enumeration. No computation run yet.

## The target (Avenue B, restated)

Find a Hecke element `β ∈ H_n(q)` such that

1. **Trace condition.** `τ_arch(tr_M(β))` at `q → ζ₅` equals Goncharov's
   22-term relation `G_22(ζ₅) ∈ ℚ⟨Li₃(ζ₅), …, Li₃(ζ₅⁴)⟩`.
2. **NF condition.** The GS normal form of `β` reduces to the identity modulo
   depth-≤2 terms.

Then `tr_M(β) = 0 (mod depth ≤ 2)` ⟹ `G_22(ζ₅) = 0` in `𝒫₃/𝒫₂` **by NF
reduction alone** — i.e. the 22-term relation at `ζ₅` becomes a theorem of QOU
infrastructure, discharging one cyclotomic case of Goncharov's depth-3
conjecture. This is the **surreal-free** real result (the proof uses Hecke NF +
Markov trace, not `No`).

## Formalize-first preflight — the constraints that prune the β-search

Before enumerating braid words, the following structural constraints must hold;
each one prunes the search space, and any one failing kills the avenue early.

### P1 — Depth/weight (bar-class ⇒ chiral)

`G_22` is **weight-3 / depth-3**. Per the verified bridge map
([`prop:two-filtration-bridge-small-cases`](../../folio/quantum-observable-universe/stochastic-mechanics/two-filtration-bridge-small-cases.md)):
depth-3 ⟺ a **chiral pair** `λ ≠ λ'` cell (`CS ≠ 0`). So `β` must be supported on
a **bar-asymmetric** (chiral) Wedderburn cell, *not* a self-conjugate one
(self-conjugate ⇒ `CS = 0` ⇒ depth-2, wrong weight). **Prune:** restrict to
chiral-cell braids.

### P2 — Root-of-unity non-semisimplicity (the delicate step)

`q → ζ₅` is a **root of unity**, where `H_n(q)` is **NOT semisimple**
(Wenzl / Gyoja–Uno; cf. the genericity-keeps-Wedderburn discipline in
[`2026-06-04-kontsevich-soibelman-0811.2435-qou-comparison.md` §6](../audits/2026-06-04-kontsevich-soibelman-0811.2435-qou-comparison.md)).
The generic Hoefsmit seminormal form **degenerates** there. Consequences:

- the Markov trace at `q = ζ₅` must be taken via **cell modules / the
  Gyoja–Uno decomposition**, not the generic `Σ_λ y_λ χ_λ` form;
- the depth-filtration `G^{(n)}` argument of the keystone uses **generic** `q`;
  the `ζ₅` specialization is a *limit*, so the reduction must commute with the
  specialization. **This is the load-bearing technical risk** — establish it
  first (a `ℤ[q^{±1}]`-flatness / specialization-commutes lemma) before any
  braid enumeration.

### P3 — Realizability of the 22 arguments

`G_22` involves 22 specific cyclotomic arguments `ζ₅^k`. Each must be realizable
as the Markov trace of an explicit sub-braid via the Faddeev–Kashaev /
Reshetikhin–Turaev expansion (`tr_M` of a closed braid at `ζ₅` is a `ℤ[ζ₅]`-linear
combination of `Li₃` values). **Prune:** the minimal `n` is bounded below by the
number of independent `ζ₅^k`-arguments expressible in `H_n(ζ₅)` — estimate `n`
before enumerating (likely `n ≥ 5`, matching the Bring `S₅` natural field).

### P4 — NF-tail = identity (the discharge mechanism)

The discharge needs `NF_GS(β) ≡ id (mod depth ≤ 2)`. **Prune:** search only among
braids whose GS normal form is known to collapse to a short depth-≤2 tail — the
recursive atom-knot atlas already stores NF tails, so filter the atlas for
"identity-tail mod depth-2" candidates rather than enumerating `H_n` blindly.

## Algebraic cross-checks (must pass before claiming a hit)

- **Bar-parity:** `tr_M(β)` must respect `q ↦ q^{-1}` per the chiral-cell
  parity — depth-3 is bar-**odd** (`CS`-type, imaginary part).
- **Borel rank:** `dim_ℚ(K_5^ind(ℚ(ζ₅)) ⊗ ℚ) = 2`
  ([`prop:borel-partial-resolution`](../../folio/quantum-observable-universe/appendix-surreals/borel-partial-resolution.md));
  the realized relations must land in a rank-2 image — a hit producing rank ≠ 2
  is wrong.
- **Independent numeric witness:** evaluate `tr_M(β)(ζ₅)` numerically (mpmath,
  ≥ 50 dps) against the known `G_22(ζ₅)` value; agreement to compute precision
  is necessary (not sufficient) before the symbolic NF claim.

## Sequencing (gated — do not skip P2)

1. **P2 first** — prove the specialization-commutes / flatness lemma for the
   depth filtration at `q → ζ₅`. If it fails, Avenue B is blocked; stop.
2. **P1 + P4** — filter the atom-knot atlas to chiral-cell braids with
   identity-tail-mod-depth-2 NF.
3. **P3** — pin minimal `n`; express the 22 arguments as sub-braid traces.
4. **Search** the pruned candidate set for `β` satisfying the trace condition;
   run the algebraic cross-checks on any hit.
5. **Symbolic NF** of the hit to upgrade the numeric match to a theorem.

This is the ~1–2 week project the parent conjecture estimates; the value here is
the **pruned** search (P1–P4) so the enumeration is over a small filtered set,
not all of `H_n(q)`.

## P2 — first structural progress (the flat part vs the pole part)

The P2 risk ("does the depth reduction commute with `q → ζ₅`?") **splits into a
free/flat part that is settled structurally, and a located pole part that is the
genuine open work.**

### P2a — the GS *filtration* commutes (free ⇒ flat ⇒ exact base change). SETTLED.

The Gröbner–Shirshov normal form gives `H_n(q)` a **free `ℤ[q^{±1}]`-basis** of
standard monomials `{T_w : w ∈ S_n}` (the PBW/GS basis). A free module is flat,
so base change along the specialization

```
   ℤ[q^{±1}]  ⟶  ℤ[q^{±1}] / Φ₅(q)  =  ℤ[ζ₅]
```

is **exact**. Therefore each GS-filtration piece base-changes term-by-term,
`J^ℓ ⊗ ℤ[ζ₅] = J^ℓ(ζ₅)`, and the depth grading `G^{(n)}` is **preserved** under
`q → ζ₅`. So `G^{(n)}(ζ₅)` is well-defined and the depth structure of the
keystone *survives the specialization* — no flatness obstruction on the
filtration side. (Provable in Lean from the existing GS-basis freeness once the
toolchain is restored; it is a `Module.Flat` / `TensorProduct` exactness fact, no
analysis.)

### P2b — the *Markov trace* has poles at `ζ₅` (the located open work).

The trace weights `ỹ_λ = dim_q²V_λ / [n]_q!` carry the denominator
`[n]_q! = ∏_{k=1}^{n}[k]_q`, and `[5]_q = (q⁵−q⁻⁵)/(q−q⁻¹)` **vanishes at a
primitive 5th root** (`q⁵ = 1 ⇒ [5]_{ζ₅} = 0`). So for `n ≥ 5` the weights have a
**pole** at `ζ₅`, and some `dim_q V_λ` vanish — the signature of the
**non-semisimple** regime (radical, cell modules, non-trivial decomposition
matrix; Gyoja–Uno). The generic `Σ_λ ỹ_λ χ_λ` form does **not** specialize
naïvely.

**So P2 is not a single risk — it is:** filtration side **free/flat (done)**;
trace side a **located renormalization** — evaluate `tr_M` at `ζ₅` via the
**cell modules / canonical basis** (Graham–Lehrer cellular structure of `H_n`),
where the `[5]_q = 0` poles cancel against the `dim_q V_λ = 0` zeros. This is the
real content, now isolated to a finite, named computation rather than a vague
"specialization risk".

**Revised gate:** P2a clears immediately (free-basis flatness); the avenue is
gated on **P2b only** — the cellular renormalization of `tr_M` at `ζ₅`. That is
the first concrete deliverable when Avenue B is run.

## Relation to the surreal keep/purge decision

**Avenue B is surreal-free** (Hecke NF + Markov trace + Bloch–Suslin/Goncharov
period theory). Succeeding here is a real, citable result, but it is **not**
evidence for keeping surreals — that decision rides entirely on the separate
rank-2 probe ([`2026-06-08-surreal-rank2-nonabelian-stokes-quadratic-probe.md`](../audits/2026-06-08-surreal-rank2-nonabelian-stokes-quadratic-probe.md)).
The two tracks are independent by design.
