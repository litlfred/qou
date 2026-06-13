# Q_β heat-route — symbolic f-map exploration + literature situating

**Date:** 2026-06-13
**Probe:** [`folio-assistant/computations/qbeta/qbeta_heat_fmap_symbolic_explore.py`](../../folio-assistant/computations/qbeta/qbeta_heat_fmap_symbolic_explore.py)
**Follows:** [the a_1-gate probe](2026-06-13-qbeta-heat-kernel-a1-gate-probe.md) (heat-route bar-odd a_1; ε-order ε³).
**Discipline:** STRUCTURAL only — no `c_3` value claimed or wired; flip-flop guard
respected (`c_3` stays near-match per [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)).

## 1. Symbolic result — the fibre carrier and the f-map constraint

Sympy closed forms for `κ_λ(q) = (q−1)·μ_λ(q)`, `λ ⊢ 3`:

| λ | `κ_λ(q)` | bar-parity |
|---|---|---|
| (3) | `(q−1)(q²(q³−2)−q+2)/q²` | neither |
| **(2,1)** | **`(q−1)²(q²−1)/q² = (q−1)³(q+1)/q²`** | **ODD** (sympy-exact: `bar(κ)+κ = 0`) |
| (1,1,1) | `(q−1)²(q²−1)/q⁵` | neither |
| **Σ_λ (=e_1)** | `q⁴−q³+q²−4q+1+6/q−5/q²+2/q⁻⁴−1/q⁵` | **neither** |

**Two structural facts, both proved symbolically:**

1. **The f-map must be mode-selective, not a global scalar.** A bar-EVEN scalar
   `S(q)` preserves parity (`S·neither = neither`). Since the full mode-sum
   `e_1` is bar-*neither*, **no scalar f-map can produce a bar-ODD `a_1`** from
   it. The bar-odd character lives **only** in `κ_(2,1)` — the `c=1`-dominated
   **standard rep**, the leading Reeb heat mode. So the assembly (f-map) must
   *project onto* the (2,1) channel. This is a genuine constraint on the open
   kernel, not a tuning knob.

2. **`c_3` factors as (pure-q bar-odd fibre) × (single archimedean scalar).**
   Writing `a_1 = κ_(2,1)(q)·S`:
   - `κ_(2,1) = (q−1)³(q+1)/q²` is **pure-q, bar-odd, fibre-level** (derivable
     from the (2,1) content-Casimir heat mode; no anchor).
   - `S = a_1/κ_(2,1)` is **anchor-dependent**: `S_proton = 908.4`,
     `S_muon = 886.8` (`S_p/S_μ = 1.024 ≠ 1`). So `S` is **not** a pure-q
     function — it is precisely the **single archimedean scalar `S = Q_β/E₀`**
     that the [2026-06-10 synthesis](2026-06-10-qbeta-ck-state-of-play-synthesis.md)
     §3 identifies as "the single archimedean leak" (PR #1752), the one number
     the whole `c_k` chain carries.

   This is exactly the synthesis's demanded form — **fibre q-rational × one
   archimedean scalar** — now with the fibre carrier *named*:
   `κ_(2,1) = (q−1)³(q+1)/q²`. It is also **consistent with `c_3`'s real-q
   refutation**: the anchor-dependence lives entirely in `S`, never in the
   bar-odd q-structure `κ_(2,1)`.

**Net.** The heat route pins the **fibre half** of `c_3` (the bar-odd standard-rep
content-Casimir coefficient) and reduces the open keystone to **deriving the
single scalar `S = Q_β/E₀` categorically** — which is precision-floor-protected
(CAL-3-anchored; `σ(c_k)=σ_R/u^k` ⇒ framework-derivation-only). No `c_3` value.

## 2. Literature — what we are seeing, and where it lives

The structure (a **cyclotomic ladder** `c_k` in the `(u;u)_m = ∏(1−u^j)` basis,
obeying a **q-difference recursion** `R(q,ξ)`, with a **content-Casimir heat
spectrum** `μ_λ` and a **√u/ε bar-involution** asymptotic) is the home turf of
four well-developed programs — the first three already in the bibliography:

| program | what it is | our analog | cited? |
|---|---|---|---|
| **Habiro ring / cyclotomic expansion** (Habiro 2004; colored Jones `J_N = Σ_n C_n(K)·(q;q)_n`-type) | invariants live in `Ẑ[q]`, the cyclotomic completion; coefficients in the `(q;q)_n` basis | the `(u;u)_m → u^k` change-of-basis; `c_k` ↔ cyclotomic coefficients | ✓ `habiro2004cyclotomic` |
| **AJ conjecture / quantum A-polynomial** (Garoufalidis 2004) | colored Jones is **q-holonomic**: `Â(M̂,L̂;q)·J_N = 0`, a q-difference recurrence of finite degree | **`R(q,ξ)` / the depth-d `c_k` recursion IS a Q_β-specialised AJ-type recurrence** — the closest single analog | ✓ `garoufalidis2004` |
| **q-Casimir / Jucys–Murphy** (Jucys 1974; Ram) | JM elements' eigenvalues = `Σ_□ [c]` content sums | `μ_λ = ℏ_q²Σ[c]_q[c+1]_q` is the q-Casimir spectrum | ✓ `jucys1974` |
| **q-dilogarithm / Bloch group** (Zagier 1986) | `Li_2^q`, the dilog, hyperbolic volume | the `Σ_λ log μ_λ` route — **gate-failed** (not bar-odd; the non-hyperbolic-Hopf `D(z)=0` trap) | ✓ `zagier1986` |

**Two connections our finding suggests that are NOT yet cited (a real gap):**

- **Quantum modularity** (Zagier 2010; Garoufalidis–Zagier, "Knots, perturbative
  series and quantum modularity"). The asymptotics of `J_N` near roots of unity
  expand in `ℏ` with a `√(·)` prefactor and transform **quantum-modularly** under
  `q ↦ q̃` (the modular/bar partner). **Our √u/ε expansion + the bar-involution
  `q↦q⁻¹` is exactly that setting**, and the *bar-ODD* requirement on `a_1` is
  naturally the **odd part under the modular q-transformation**. This is the
  most promising un-cited frame for *why* `a_1` must be bar-odd.
- **Nahm sums** (Nahm; Calegari–Garoufalidis–Zagier 2023). A q-hypergeometric
  `Σ q^{Q(n)}/(q;q)_n` is modular **iff** `Q` satisfies a Bloch-group/dilog
  (torsion) condition. Our `(u;u)_m` ladder is a Nahm-type series, and the
  **failure** of the naive q-dilog `a_1` (§ gate probe) mirrors a **non-Nahm-
  modular** obstruction — the same `D(z)=0` non-hyperbolicity that kills the
  Hopf-volume route. I.e. the dilog route fails for a *principled* reason the
  Nahm criterion predicts.

## 2-bis. Their recurrence (AJ) vs ours; the quantum-modular ↔ bar-involution remark

**Theirs — the AJ / quantum A-polynomial recurrence.** The colored Jones
`J_N(K;q)` (`N` = color = rep dimension) is **q-holonomic**: with operators
`M̂` (`M̂ J_N = q^N J_N`) and `L̂` (`L̂ J_N = J_{N+1}`) obeying `L̂M̂ = q M̂L̂`,
there is a **quantum A-polynomial** `Â(M̂, L̂; q)` with `Â·J_N = 0` — i.e. a
finite recurrence `Σ_j b_j(q^N, q)·J_{N+j} = 0` **in the color `N`**. As `q→1`
it degenerates to the **classical A-polynomial** `A(M,L)` cutting out the
SL₂(ℂ) character variety of the knot complement (the (M,L) holonomy-eigenvalue
relation).

**Ours.** `c_{k+1} = Σ_j a_j(q₀)·c_{k+1−j}` — a recurrence **in the truncation
order `k`** (the `u`-powers of the `Q_β` precision series), from the heat-kernel
q-difference `F(qξ) = R(q,ξ)·F(ξ)`. Two differences: (i) the index is `k`
(cyclotomic order), not `N` (color); (ii) the element `F` is **modelled** by the
q-heat partition function `Z_q = Σ_λ d_λ exp_q(−μ_λ t)` — a physical ansatz —
whereas for AJ, `J_N` *is* the knot's own invariant.

**The bridge (why "same shape").** Habiro's cyclotomic expansion re-bases `J_N`
(N-indexed) onto the cyclotomic coefficients `C_n` (n-indexed); the `C_n`
inherit a recurrence **induced** from the AJ one by the `N ↔ n` re-basing — and
that re-basing **is our `(u;u)_m → u^k` change-of-basis**. So ours is the
AJ recurrence *pushed into the cyclotomic basis* and `Q_β`-specialised: same
q-holonomic machinery, different index, plus a heat-kernel **model** for `F`.

**Quantum-modularity ↔ bar-involution — REMARK (conjectural, NOT proven).**
[Zagier 2010, `zagier2010`]: the Kashaev/colored-Jones asymptotics near roots of
unity are **quantum-modular** — controlled under SL₂(ℤ), especially the
S-transform `q ↦ q̃` (the "modular partner"), with a `√(2π/ℏ)` radial prefactor
and an `ℏ`-series of **periods** (the Ohtsuki series). The QOU **bar-involution
`q↦q⁻¹`** is the natural fibre-level avatar of that modular partner, and the
**√u/ε prefactor** + the **bar-ODD requirement on `a_1`** are exactly what
quantum modularity predicts (the odd part under the S-transform).

- **Can we prove the link?** **No, not at present.** Quantum modularity is
  itself conjectural/hard for general knots (proved case-by-case — e.g. `4_1`,
  Garoufalidis–Zagier). Establishing "QOU bar-involution = the quantum-modular
  S-partner" needs `F(q)` exhibited as a quantum modular form (or `R(q,ξ)`
  transforming under SL₂(ℤ)) — out of reach now. It stands as a **motivated
  remark**, not a theorem.
- **What we can use from it (four concrete handles):**
  1. It **explains the `√u/ε` prefactor** structurally (the radial `√(2π/ℏ)`).
  2. It makes the **bar-ODD `a_1` natural** — the odd part under the S-transform
     — turning §1's *imposed* mode-selectivity into something a modular argument
     might **derive** ((2,1)-projection from the transform).
  3. It **explains the dilog gate-failure**: the modular cocycle's leading
     (volume/Bloch–Wigner) term vanishes for the **non-hyperbolic Hopf**
     (`D(z)=0`), so the `c_k` content lives in the **sub-leading Ohtsuki
     periods** — exactly where the `k≥3` ladder sits.
  4. The **Ohtsuki-series / period structure** is a *categorical* route to
     constrain the single scalar `S` (the open keystone) — periods are
     computable invariants, not fits.

## 3. Status + recommended follow-ups

- **No `c_3` value; registry tiers untouched.** This pins the *fibre* half of
  `c_3` and constrains the f-map (mode-selective onto (2,1)); the *scalar* half
  `S = Q_β/E₀` remains the CAL-3-anchored open keystone.
- **Doc/bib follow-up (cheap):** add Zagier-2010 quantum-modularity +
  Calegari–Garoufalidis–Zagier Nahm-modularity to `references.ts`, and cross-link
  the AJ recurrence as the structural parent of `prop:q-beta-c-k-recursion-from-habiro-q-difference`.
- **Research follow-up (owner-gated):** test whether the quantum-modular
  transformation `q↦q̃` *forces* the bar-odd `κ_(2,1)` projection (would explain
  the mode-selectivity from modularity rather than imposing it).

## Cross-references
- Synthesis §3 / §3-bis: [`2026-06-10-qbeta-ck-state-of-play-synthesis.md`](2026-06-10-qbeta-ck-state-of-play-synthesis.md)
- Gate + ε-order: [`2026-06-13-qbeta-heat-kernel-a1-gate-probe.md`](2026-06-13-qbeta-heat-kernel-a1-gate-probe.md)
- Recursion engine: [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
- μ_λ: [`prop:q-heat-kernel-peter-weyl`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-peter-weyl.md)
- Tiers (flip-flop guard): [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
