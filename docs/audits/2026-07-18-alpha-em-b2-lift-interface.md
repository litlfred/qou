# α_EM B2 lift — Mathlib gate opened; the wall stated as a content-bearing class (2026-07-18)

**Bean:** `qou-tq20` (B2, the single remaining open wall after the plan
`qou-b5qg` completed at shadow level — B1 #3955, B2s #3960, B3 #3969,
B4a #3973, B4b #3977, B5 #3982, all merged).

**Lean (this PR):** [`QOU/Archimedean/TauRhoHodgeLiftInterface.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/TauRhoHodgeLiftInterface.lean)
— sorry-free, `lean`-direct exit 0 **with Mathlib**.

**Scope guard (STRICT):** the conjecture class has **no instance**; nothing
derives the lift; nothing wired; `1/(8π)` stays phase-4.

## Environment finding — the Mathlib gate is OPEN

The B2 lift had been "Mathlib-gated": `lake exe cache get` 403s through the
proxy and the from-source build dies on ProofWidgets' network JS fetch. The
**`lake-cache` orphan-branch restore** (AGENTS §Step 0,
`lake-cache/qou-v4-24-0`) sidesteps **both**: one `git fetch --depth=1` +
tar-extract (932 MB, ~2 min) restores 2962 prebuilt Mathlib oleans
(ProofWidgets included — no JS fetch ever runs), after which `lean`-direct
with `LEAN_PATH` over `.lake/packages/*/.lake/build/lib/lean` compiles
Mathlib-importing files. **Do not re-walk the cache-get/ProofWidgets path;
restore first.** This is exactly the documented recipe — the finding is that
it also clears the ProofWidgets blocker that pushed this session core-only.

## What the module does

1. **The ρ-split engine in Mathlib generality** (proved):
   `trace_map_star_eq_of_isHermitian` — for hermitian `A`,
   `(A.map star).trace = A.trace`. This upgrades B4b's concrete 3×3 sympy
   check to a general theorem (via `trace_conjTranspose` + hermiticity).

2. **The conjecture carrier** (`class TauRhoHodgeLift`, §3b-cond/§3b-tax
   compliant): parameters = the loop's spectral weight matrices `W` (on
   `H^{1,0}`) and `Wbar` (on `H^{0,1}`); fields =
   - `hermitian : W.IsHermitian` — the weight comes from a real
     self-adjoint operator (the B3 inheritance);
   - `conjugated : Wbar = W.map (starRingEnd ℂ)` — τ carries ρ to the Hodge
     conjugation (the B1 dictionary, functorially; shadow FORCED #3960).

   The fields encode the lift's **inputs**, never its conclusion; **no
   instance is declared anywhere** — the conjecture is honestly open.

3. **The conditional theorems** (derived from the fields, not assumed):
   - `TauRhoHodgeLift.equal_split` — `Wbar.trace = W.trace` (the ½ is
     ρ-forced);
   - `TauRhoHodgeLift.doubled_total` — `W.trace + Wbar.trace = 2·W.trace`
     (the selected channel carries half; q→1 one-loop restores the doubled
     unit — B4's target).

4. **The archimedean identities with a genuine `Real.pi`** (proved):
   `½·(1/(4π)) = 1/(8π)` and `|−6|/(4·(12π)) = 1/(8π)` — the rational shadow
   of #3982 upgraded to π-carrying real-number theorems.

## What remains open (the wall, unchanged in content, now pinned in type)

Exhibiting an instance of `TauRhoHodgeLift` **for the actual α_EM loop
weights** — i.e. constructing, from the categorical τ-functor, the hermitian
`H^{1,0}` weight and proving its `H^{0,1}` partner is its conjugate. Any
future categorical construction discharges the wall by *proving* the two
fields; fabricating an instance without that construction would violate
§"Axiomatization is NOT a Proof" and is not done here.

Attack surface for the next brick: the interface is now stated over
`Matrix (Fin g) (Fin g) ℂ`; the categorical side must produce these weights
from the Hecke channel data (`e₊` at the degenerate locus, the #3942
geometric carrier `dU = J`, multiplier `i` at `V`). The natural next step is
the vertex-local statement: τ of the `H₂(i)`-module structure at `V` — the
original `qou-tq20` bean title — now formalizable with Mathlib's
`CategoryTheory` in reach.
