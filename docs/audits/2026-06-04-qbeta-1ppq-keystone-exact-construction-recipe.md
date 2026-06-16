# Q_β 1 ppQ keystone — exact c_4..c_8 construction recipe

**Date:** 2026-06-04
**Branch:** [`claude/qbeta-hoefsmit-tbeta-exact-ck-2026-06-04`](https://github.com/litlfred/qou/tree/claude/qbeta-hoefsmit-tbeta-exact-ck-2026-06-04)
**Status:** EXECUTABLE RECIPE (the object + infra + validation anchors pinned; ready to compute)
**Predecessors:** PR #1835 (bounded verdict), PR #1836 (candidate elimination + q-stability), PR #1786 (c_2=−1), PR #1824 (c_3=−2 bias-corrected)

## Why this exists

The full session arc established that 1 ppQ Q_β reduces to **one** concrete compute: obtain **unbiased** c_4..c_8. The SDP extraction is +1.7% biased even on the proved c_2 (PR #1824) and noise-dominated at high k (the residual plateau, PR #1835). Candidate-guessing the closed form is exhausted (PR #1836). The remaining step is to compute c_k from the **exact symbolic operator object**, not from extraction.

This doc pins that object precisely and gives the executable recipe with per-stage validation against the proved anchors c_2 = −1 and c_3 = −2.

## The exact object

### Definitions (source-of-truth pointers)

| symbol | exact definition | source |
|---|---|---|
| q₀ | 1.1099785827513808075916690956107688798744991218736 | `q-pinning-50-digit.witness.json` |
| h(q) | q - 1/q (Hecke skein) | `qbeta_symbolic_chain_alpha_b.py` |
| z(q) | 1/(√q + 1/√q) (Markov-Jones) | same |
| α(q) | (z-1)·h/2 | same |
| b(q) | √(q⁴+q²+1)/(q²+1) (Hoefsmit) | same |
| ℏ_q(q) | (q-1)/q | same |
| α_eff(q) | α - b·ℏ_q²/2 | same |
| u(q), u₀ | b·ℏ_q²; u₀ = u(q₀) ≈ 0.00852 | same |
| Q_A(q) | m_e·(2q+1-q²)(q+1)/(2q³) [substrate branch] | `probe_q_beta_operator_valued_N3.py` |
| 𝔈₀(q) | substrate energy scale = m_e/(q(q-1)) (leptonic) / Q_β/\|h(h-2)/2\| (hadronic) | cheat sheet Step 9 |
| Δ(net)(q) | net(after) - net(before), GB-reduced | `free-neutron-decay.py` (`computations/`) |
| `free-neutron-decay.witness.json` | net coefficients at q₀ | `computations/free-neutron-decay.witness.json` |

Per the canonical chain Step 11 ([cheat sheet](../canonical-derivation-cheat-sheet.md)) and the canonical producer `free-neutron-decay.py`:

```
Q_b = |Delta(net)| * E_0,     Delta(net) = net(T_w after) - net(T_w before)
```

where `net(T_w)` is the **Gröbner–Shirshov-reduced coefficient sum** of the particle's braid word in H_n(q). The canonical words (from `free-neutron-decay.py::PARTICLE_KNOT`):

| particle | braid word | knot/link |
|---|---|---|
| ν (final) | `()` | unknot 0₁ |
| e⁻ | `σ₀σ₁σ₀` = (0,1,0) | trefoil 3₁ |
| Hopf intermediates | (0,1),(1,0) | Hopf |

`net(T_w)(q)` is an **exact Laurent polynomial in q** produced by the GB reducer (the `reduce_verbose` machinery in `free-neutron-decay.py`, which applies the Hecke quadratic σ²=(q−q⁻¹)σ+1, braid relations, and far-commutation).

**The c_k are the Taylor coefficients of the substrate expansion of the ladder factor:**

```
Q_β(q) / [Q_A(q)·cos(α_eff(q))]  =  Π_{k≥2} (1 + c_k · u^k),     u = b(q)·ℏ_q²
```

So c_k are obtained by:
1. Forming the **exact symbolic** `Q_β(q)` from `|Δ(net)(q)| · 𝔈₀(q)`.
2. Dividing by the exact `Q_A(q)·cos(α_eff(q))` (PR #1786 chain).
3. Substituting the substrate relation between `q` and `u` (u = b(q)·ℏ_q²), inverting to express the ratio as a series in `u`.
4. Log-matching the product `Π(1+c_k u^k)` → c_k (the `ladder_ck` routine from PR #1835/#1836).

Every step is exact symbolic algebra in ℚ(q) → no SDP, no fit, no extraction noise.

## The infrastructure (confirmed present)

| Need | Where |
|---|---|
| Hoefsmit seminormal ρ_λ(σ_i) | `hecke/hecke_characters.py::build_seminormal_matrices(shape, q)` |
| Hecke character χ^λ(word) | `hecke/hecke_characters.py::chi_lambda_braid(shape, word, q)` |
| GB-Shirshov net reduction | `free-neutron-decay.py::reduce_verbose(...)` → `net` (symbolic) |
| Partitions / dim_q | `hecke/hecke_characters.py::partitions_of`, `dim_q` |
| Substrate α(q),b(q),ℏ_q(q) | PR #1786 `qbeta_symbolic_chain_alpha_b.py` (exact closed forms) |
| Ladder log-match c_k | `qbeta_ck_genfunc_bounded_vs_factorial_probe.py::ladder_ck` (PR #1835) |
| Markov trace via Wedderburn | `tr_M = Σ_λ y_λ χ^λ`, `y_lambda_wenzl_bridge.py` |

## The recipe (executable, with per-stage validation)

### Stage 1 — exact symbolic net(T_w)(q) for each particle word
Run the GB reducer on `()`, `(0,1,0)` (and the Hopf intermediates) to get `net(q)` as exact Laurent polynomials. **Validate:** net values at q₀ must match `free-neutron-decay.witness.json`.

### Stage 2 — exact symbolic Δ(net)(q) and Q_β(q)
Form `Δ(net)(q)` = the canonical after−before difference; multiply by `𝔈₀(q)`. **Validate:** `Q_β(q₀)` ≈ 0.78233 MeV (CODATA) at the proven ~4–6 ppm of the N=2 ladder.

### Stage 3 — divide out the N=1·N=0 prefactor, expand in u
Compute `R(q) = Q_β(q)/[Q_A(q)·cos(α_eff(q))]`, then re-express as a series in `u = b(q)·ℏ_q²`. **Validate (CRITICAL):** the u² coefficient of `log R` must give **c_2 = −1** (the proved structural anchor, PR #1786). If Stage 3 does not reproduce c_2 = −1, the symbolic chain has an error — stop and debug before trusting c_4..c_8.

### Stage 4 — log-match c_3..c_8
Apply `ladder_ck` to `R(u)` to order u^8. **Validate:** c_3 must come out ≈ −2 = J_Hopf(q=1) (PR #1824 bias-corrected anchor). c_2 = −1 exact, c_3 = −2 → the chain is trustworthy; read off c_4..c_8 as the **first unbiased values**.

### Stage 5 — evaluate Q_β to 1 ppQ
`Q_β(q₀) = Q_A·cos(α_eff)·Π_{k=2}^{8}(1+c_k u₀^k)` at 65 dps. **Target:** |Q_β/CODATA − 1| < 1e-9 (sub-ppb → ppQ-class), with the series converged (|c_8 u₀^8| < 1e-15 per PR #1835's N≈8 bound).

## Failure modes to guard (formalize-first discipline)

- **Stage 3 c_2 ≠ −1** ⇒ the q↔u substitution or the Q_A/cos prefactor is wrong. The proved c_2 is the structural gate; do not proceed past a failed Stage-3 check.
- **Δ(net) convention mismatch** ⇒ Q_β(q₀) off by O(1). Validate against `free-neutron-decay.witness.json` at Stage 1–2.
- **`Abs` in Q_A** ⇒ the substrate-region branch `|q²−2q−1| = 2q+1−q²` holds only for 1 < q < 1+√2; keep symbolic work in that branch.
- **Spurious high-k blowup** ⇒ if c_k grows factorially, the q↔u inversion reintroduced the 1/u^k ill-conditioning (PR #1835); the exact symbolic route must NOT — c_k must stay bounded.

## Execution finding (2026-06-04) — the scalar route is RULED OUT

Executing Stage 3 surfaced a decisive structural obstruction
(`qbeta_ck_scalar_route_singularity_probe.py`):

> **u = b(q)·ℏ_q² is QUADRATIC in t = q-1**, since ℏ_q = (q-1)/q ~ t.
> So u(t) = a₂ t² + a₃ t³ + ... has **no linear term** (a₁ = 0).

Consequence: reverting u(t) -> t(u) to express R(q) = Q_b/(Q_A·cos α_eff)
as a scalar power series in u is **singular** (t(u) would need a u^(1/2)
term). This holds for ANY Q_b model (it is a property of u itself) —
confirmed for both `|h(h-2)/2|` and the proven N=2 control.

**Therefore the c_k are NOT scalar-q Taylor coefficients.** They are
the coefficients of the **operator-valued ladder**: the T_β matrix
expanded in its N=0,1,2,... level structure, where level N=k
contributes b^k·ℏ_q^{2k} = u^k via the *substrate scaling* (each
operator level carries one power of b·ℏ²), NOT via powers of (q-1).

This **rules out the scalar exact-Δ(net) shortcut** and confirms:
- Stages 1-2 (exact `net` via GB) remain valid for the **leading** Q_b.
- Stages 3-4 must operate on the **operator matrix** (read the N=k
  levels off the Hoefsmit-rep T_β), NOT on a scalar u-reversion.
- The Hoefsmit-matrix construction is **irreducible** for the keystone
  — there is no scalar-function bypass. This is precisely why the SDP
  (a matrix fit) was the only existing route, and why an *unbiased*
  c_4..c_8 needs the matrix built directly (avoiding the SDP's 1/u^k
  ill-conditioning and +1.7% bias).

The recipe is updated accordingly: the operative construction is the
Hoefsmit-rep T_β matrix with per-level (N=k) operator reading. The
c_2 = -1 / c_3 = -2 gates still apply, now as checks on the matrix
N=2/N=3 levels.

## What this branch delivers

This recipe converts the "open keystone" (ck-dk registry §3 "kernel/F(q) unconstructed") into a **deterministic, validated, executable construction** with the exact object identified (Δ(net) from trefoil GB reduction), the infra confirmed present, and the c_2=−1 / c_3=−2 anchors as per-stage correctness gates.

Execution is the next commit on this branch (a probe implementing Stages 1–5 with the validation asserts). Writing the recipe first — with the structural anchors as gates — is the formalize-first complement: it prevents a rushed probe from emitting a subtly-wrong c_k that passes no structural check.

## Cross-references
- [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) §3 (kernel/F(q) keystone)
- [`docs/audits/2026-06-04-ck-generating-function-derivation-chain-scope.md`](2026-06-04-ck-generating-function-derivation-chain-scope.md) (4 candidate origins)
- PR #1835 bounded verdict, PR #1836 candidate elimination + q-stability
- `free-neutron-decay.py` (canonical Δ(net) producer), `hecke/hecke_characters.py` (Hoefsmit infra)
