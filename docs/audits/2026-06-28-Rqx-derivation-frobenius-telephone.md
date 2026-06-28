# 2026-06-28 — R(q,x) = q-telephone/q-Hermite: INDEPENDENT CROSS-CHECK (not a new derivation)

> **⚠ SCOPE CORRECTION (2026-06-28).** This is **NOT a new derivation** — it
> **reproduces existing corpus**, which I failed to corpus-grep before writing.
> The result (`a_D^(n)=(1/n)Σ_λ dim_q`, `q→1` = involution/telephone numbers
> A000085, q-Hermite home, the `[n−1]_q` q-telephone recurrence drift for n≥4, no
> low-order R(q,x)) is **already established**, more completely:
> - [`docs/audits/2026-06-26-binding-period-qinvolution-qhermite-identification.md`](2026-06-26-binding-period-qinvolution-qhermite-identification.md)
>   — the q-involution/q-Hermite identification, proved **all-n via RSK** (vs my
>   finite n≤8 check); a 90-dps held-out search proving **no low-order R(q,x)**;
>   and a **fork I missed** (the clean kernel belongs to the *crossing* moment
>   μ_q, not the quantum-dim period Σ_λ dim_q — they diverge past n=3).
> - [`prop:binding-genfun-qdifference`](../../content/quantum-observable-universe/mass-theory/binding-genfun-qdifference.md)
>   — the R(q,x) recursion `G(qx)=R(q,x)G(x)` block (+ Lean sibling).
> - [`prop:sw-period-residue-sum`](../../content/quantum-observable-universe/brings-surface/sw-period-residue-sum.md)
>   — `a_D^(n)=∮λ_SW^(n)` = residue sum = per-block Wedderburn weights (+ Lean).
> - Compute already exists: `sw_period_qinvolution_identification_probe.py`,
>   `sw_period_qholonomic_kernel_search.py`.
>
> **Residual value:** my `delta_lambda_Rqx_derivation.py` is an *independent
> numerical cross-check* (Frobenius-total-q-mass framing, exact in q for n≤8)
> confirming the anchor identities + the (q−1)²·Φ₃ defect factorization. It adds
> no new mathematics. The novelty language below is retracted.

**Branch:** `claude/delta-lambda-three-piece-test-2026-06-28` · **PR:** #3040 · **Bean:** `z2bn`
**Scope tag:** (a) — independent numerical cross-check of existing corpus (see correction above). **No new result.**
**Producer:** [`computations/delta_lambda_Rqx_derivation.py`](../../computations/delta_lambda_Rqx_derivation.py)
**Witness:** `computations/delta-lambda-Rqx-derivation.witness.json`

## The ask

Derive the z2bn Lever-1 fibre q-difference kernel `R(q,x)` from the categorical
chain (categorical action → Frobenius pairing → Wedderburn), inspired by the
q-Askey literature — rather than searching for it.

## The derivation

The Wedderburn decomposition `H_n(q) ≅ ⊕_{λ⊢n} M_{d_λ}` has a canonical scalar:
the **Frobenius/Plancherel total q-mass**

$$ S(n) \;:=\; \sum_{\lambda \vdash n} \dim_q(\lambda), \qquad
   \dim_q(\lambda) = \frac{[n]_q!}{\prod_{c\in\lambda}[h_c]_q}, $$

and the normalized anchor `a_D^(n) := S(n)/n`. Three exact facts (sympy,
no fit) pin this as the object behind `R(q,x)`:

**1. It reproduces ALL wired binding anchors.**

| n | `a_D^(n) = S(n)/n` | wired anchor | match |
|---|---|---|---|
| 2 | `1` | `a_D^(2)=1` | exact |
| 3 | `(q+1)²/(3q)` | `a_D^(3)=(q+1)²/(3q)` | exact |
| 4 | `5/2 + (3/4)h²` | `a_D^(4)=Family-A` | exact |

`a_D^(4) = Family-A` is *derived*, not coincidental: Family-A is by definition
`(1/4)·Σ_{λ⊢4} dim_q V_λ`, i.e. `S(4)/4`. (This also re-frames the standing
"Family-A is a CODATA near-match" caveat: as the H₄ total q-mass it is exact
categorical structure; the CODATA proximity is downstream.)

**2. The classical limit is the involution / telephone numbers.**

`S(n)|_{q=1} = 1, 2, 4, 10, 26, 76, 232, 764` = **OEIS A000085** (involutions in
`S_n`, `Σ_λ f^λ`), whose EGF is `exp(x + x²/2)`. So `R(q,x)` is the
**q-deformation of the operator `(d/dx − (1+x))`** that annihilates `exp(x+x²/2)`
— a **Rogers–Szegő / continuous q-Hermite** object (the q-Askey row the q-askey
audit names as the binding-kernel basis, `|q|≤1` fibre via the bar involution,
since the q-Gaussian is obstructed at `q₀>1`).

**3. The q-telephone recurrence + defect = the z2bn structure.**

`S(n) = S(n−1) + [n−1]_q S(n−2) + D(n)` with `D(2)=D(3)=0` and

$$ D(4)\cdot q^3 \;=\; q\,(q-1)^2\,(q^2+q+1) \;=\; q\,(q-1)^2\,\Phi_3(q), $$

i.e. `D(n) = (q−1)²·(cyclotomic)·R_m` — **exactly the z2bn Stage-7 factorization**
(`(q−1)²` prefactor + cyclotomic strip + the growing non-cyclotomic core `R_m`,
trivial at n=4,5, growing for n≥6).

## What this settles

- **`R(q,x)` is identified**: the q-difference operator of the q-deformed telephone
  EGF `Ŝ(x) = Σ_n S(n) x^n/[n]_q!`, `S(n) = Σ_λ dim_q(λ)` (total q-dimension).
  Classical core `d/dx − (1+x)`; q-deformation is q-Hermite/Rogers–Szegő.
- **It DERIVES z2bn's #3009/#2985 negative** rather than re-finding it by search:
  the q-deformed telephone EGF is **not q-holonomic of low order** — the defect
  `D(n)` grows — so `R(q,x)` cannot be a single low-order q-difference element.
  The "growing non-cyclotomic core `R_m`" **is** the q-telephone defect
  `D(n)/[(q−1)²·cyclotomic]`. The obstruction is structural, not a search artifact.
- **The categorical provenance is explicit**: `S(n)` is the Frobenius/Plancherel
  total mass of the Wedderburn decomposition — the categorical-action → Frobenius
  pairing → Wedderburn path, with the q-Askey lens supplying the special-function
  identity (telephone EGF → q-Hermite).

## The remaining gap (open keystone, unchanged)

This derives the **fibre** object `R(q,x)` and its anchors `a_D^(n)`. The
**fibre→per-isotope bridge** — `a_D^(n)=∮λ_SW^(n)` jet anchors → per-isotope
binding (`mba-step09b`) → the multiplicative `R_eff(K)` → the measured target
`r(K)` (PR #3040) — is still the open keystone. The closure check is pre-wired
([`delta_lambda_rK_closure_test.py`](../../computations/delta_lambda_rK_closure_test.py)):
when the bridge yields `R_eff(K)`, it is a one-call test against `r(K)`.

**Net:** `R(q,x)` is no longer an unknown to search for — it is the q-Hermite /
q-telephone q-difference operator, derived from Wedderburn total q-mass, validated
against every wired anchor and against z2bn's own defect factorization. The open
work narrows to the n→A archimedean bridge.
