# Lean workplan — Φ_b combinatorial (cyclotomic / tetraplectic) fibre route

**Date:** 2026-07-13 · **Branch:** `claude/faddeev-phi-b-construction-wp7xau` ·
**PR:** #3768 · **Beans:** `qou-b8iu` (L1), `qou-nyvu` (L2), `qou-lgpb` (L3),
`qou-evo7` (L4), `qou-d7lh` (L5).

## Goal and honest scope

Replace the (un-formalizable) **contour integral** for Φ_b at the `|q|=1`
root-of-unity **fibre / decay saddle** by **finite algebra**, and use it to
**discharge `FaddeevPhi` on the fibre branch** in Lean — the currently-open
regime that `PhiBProd` (substrate branch, `Im b²>0`) does not reach. This
**genuinely closes gap G2** (fibre-regime construction) of
[`2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`](../audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md).

**What this does NOT close (anti-laundering, stated up front):** the **keystone
G3** — the monodromy datum `z(q₀) → S`, i.e. the Stokes constant `A_ω` that the
alien derivative `Δ_ω` computes — is **not** closed by any of L1–L5. That is the
resurgent computation (with PR #3683), genuinely open. L1–L3 close *G2*; L4 gives
*uniqueness*; L5 gives the *combinatorial organization*. The conjecture's bar-odd
`S` map stays a conjecture.

## The mechanism (verified — `qbeta_phib_cyclotomic_fibre_reduction_probe.py`)

At `q = ζ_N = e^{2πi/N}` the q-Pochhammer product **collapses to a finite
cyclotomic polynomial** (verified as a degree-N polynomial identity, mpmath
multipoint, `1e-40`, N=2..8):

$$\prod_{k=0}^{N-1}(1 - x\,\zeta_N^{k}) \;=\; 1 - x^{N}.$$

So `(x;q)_N` is the **finite** `1 - x^N`, the shift equation becomes a finite
N-periodic recursion (the cyclic quantum dilogarithm), and `N = 5` is Bring's S₅
tetraplectic modulus (`p(5)=7` partitions organize the state-sum).

## The five independent Lean results

Dependency graph: **L1 → L2 → L3** (the G2-closing chain); **L4** and **L5** are
parallel-startable (each uses only already-proved bundles). L1, L4, L5 can begin
immediately.

### L1 — Cyclotomic collapse `∏(1 − xζ^k) = 1 − x^N`  ·  `qou-b8iu` · **independent, closeable now**

Over a `CommRing R` with a primitive N-th root of unity `ζ`,
`∏_{k=0}^{N-1}(1 − x·ζ^k) = 1 − x^N`. Mathlib supplies the backbone:
`Polynomial.nthRoots`, `X^n − 1 = ∏ (X − ζ^k)` over a field with `ζ` primitive
(`Polynomial.prod_X_sub_C_primitiveRoots` / `Complex.isPrimitiveRoot_exp`). Pure
algebra, expected sorry-free.
**File:** `QOU/QBeta/CyclotomicDilogCollapse.lean` — `theorem cyclotomic_collapse`.

### L2 — Finite cyclic quantum dilog + N-periodic shift  ·  `qou-nyvu` · needs L1

Define `cyclicDilog ζ x N` as the finite product / its reciprocal, and prove the
shift equation `Φ(ζ²x) = (1 + ζx)·Φ(x)` **closes as a finite N-step recursion**
(the factor family `(1 + ζ^{2k+1}x)` is N-periodic — already verified
combinatorially: distinct odd residues mod 2N). Uses L1 for the closure identity.
**File:** `QOU/QBeta/CyclicQuantumDilog.lean` — `cyclicDilog`, `cyclicDilog_shift`,
`cyclicDilog_periodic`.

### L3 — Discharge `FaddeevPhi` on the fibre branch  ·  `qou-lgpb` · needs L1,L2 · **CLOSES G2**

Prove `cyclicDilog` satisfies the two `FaddeevPhi` shift equations at `ζ_N`,
yielding a genuine `FaddeevPhi` **instance on the fibre / root-of-unity branch** —
the regime `PhiBProd` cannot reach and where the decay physics lives. This is the
payoff: an honest construction where `PhiBProd`'s substrate-branch discharge and
this fibre-branch discharge together cover both faces.
**File:** `QOU/QBeta/FaddeevPhiFibreBranch.lean` — `faddeevPhi_cyclic_fibre`.

### L4 — Pentagon (5-term) rigidity  ·  `qou-evo7` · **independent (uniqueness lever)**

Formalize the **pentagon / 5-term** relation for the cyclic dilog (a finite
identity at `ζ_N`) and that **pentagon + inversion + unitarity + modular
invariance** — the last three already proved (`phiB_inversion`, `norm_phiB`,
`phiB_self_dual`) — pin Φ_b **uniquely** (Faddeev–Volkov rigidity). Converts the
keystone from an existence hunt into a rigidity statement: *the datum is forced,
not fitted.*
**File:** `QOU/QBeta/CyclicDilogPentagon.lean` — `cyclic_pentagon`,
`faddeevPhi_unique_of_pentagon`.

### L5 — Tetraplectic → Young state-sum  ·  `qou-d7lh` · **independent (combinatorial organization)**

Connect the `N=5` finite state-sum to the **partitions of 5 / Hoefsmit
seminormal basis** (`mass-theory/hoefsmit-ew-cell-content.md`, the 20 pure S₅
tableaux). Formalize the `p(5)=7` partition index / the S₅-irrep decomposition
organizing the finite state-sum — the tetraplectic → Young reduction the route is
named for. Ties to existing S₅ / Hoefsmit Lean infra.
**File:** `QOU/QBeta/TetraplecticYoungStateSum.lean`.

## Verification protocol

Each file verified **lean-direct** (source-built `lean` v4.24.0, restored from
`lake-cache/toolchain-v4-24-0`; `LEAN_PATH` = restored Mathlib oleans) — exit 0,
sorry-free — before commit. Standalone Mathlib-only files, one result per PR
commit. No `c_k` wired, registry untouched, scope-(a) throughout.

## Sequencing

1. **L1** (immediate; Mathlib cyclotomic backbone) → **L2** → **L3** [G2 closed].
2. **L4** and **L5** in parallel (each uses only proved bundles).
3. Report: G2 closed (L1–L3), uniqueness (L4), organization (L5); **G3 keystone
   remains open** — the resurgent monodromy datum, with #3683.
