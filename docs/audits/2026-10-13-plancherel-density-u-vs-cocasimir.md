# Plancherel-functional coproduct density `u` vs the refuted co-Casimir Δ_λ

Date: 2026-10-13. Branch `claude/frobenius-counit-axiom2-2026-10-13` (owner-approved exploration, item 4).
Producer: [`computations/deltalambda/plancherel_density_u_probe.py`](../../computations/deltalambda/plancherel_density_u_probe.py)
→ `computations/deltalambda/plancherel-density-u.witness.json` (39 PASS / 0 FAIL).
Arithmetic: exact over Q(q) (sympy). The only decimal inputs are the proton pin
`q0 = 1.1099785827513808075916690956107688798744991218736` (substituted as an exact
rational) and the n=6 deuteron characters `χ_λ(β_D)`, read as 60-digit strings from
`computations/rho-k-h3a-co-casimir.witness.json`. No float64 anywhere.

## Claim

On the generic semisimple Hecke algebra `H_n(q) ≅ ⊕_λ M_{d_λ}`, the Frobenius coproduct
`Δ(1) = Σ_λ c_λ Σ_ij E^λ_ij ⊗ E^λ_ji` with counit `ε = Σ_λ ε_λ χ_λ` requires `c_λ = 1/ε_λ`, and
the density it induces against the Markov trace `∫ = tr_M = Σ_λ y_λ χ_λ` (convention D) is

    u = (tr_M ⊗ id)Δ(1) = Σ_λ (y_λ/ε_λ) p_λ,     so the effective Δ_λ is u_λ = y_λ/ε_λ.

(The summand of the mass functional is `y_λ·u_λ = y_λ²/ε_λ`; the effective Δ_λ itself is
`y_λ/ε_λ`, not `y_λ²/ε_λ`.)

For the unweighted Plancherel functional (b) this gives `u_λ = y_λ [n]_q! / dim_q(λ)`, which is **not**
proportional to the co-Casimir `1/dim_q(λ)`; it is non-negative on every block, vanishes on
every block with ≥ 3 rows, and fails the deuteron test of
`QOU.BraidKnot.DeltaLambdaRefutation` by a wider margin than the co-Casimir does.

## Which counit — three candidates, none selected by agreement

| tag | ε | ε_λ | status |
|---|---|---|---|
| (a) | `tr_M` | `y_λ` | **no counit on `H_n` for n ≥ 3**: under D, `y_λ = 0` on every ≥3-row block, so `c_λ = 1/0`. Exists only on the quotient `H_n/rad` (TL_n), where `u = 1`. Checked: n=2 passes all axioms, n=3 fails at `(1³)`. |
| (b) | **unweighted Plancherel functional** `τ_P(p_λ) = dim_q(λ)·d_λ/[n]_q!` (docstring of `frobenius_codim_tau_invariant`, `mass-theory/frobenius-codim-universal.lean`) | `dim_q(λ)/[n]_q!` | valid counit. **Not** the canonical trace and **not normalised**: `τ_P(1) = 2q/(q²+1)` (n=2), `2q²/((q²+1)(q²−q+1))` (n=3), `8q⁴/((q²+1)²(q⁴+1))` (n=4). |
| (bκ) | **canonical trace**: with the `q^{-κ_λ}` factor of `QOU/MathlibExt/MolienFakeDegree.lean` | `q^{-κ_λ} dim_q(λ)/[n]_q!` | valid counit, and **is** the canonical trace `τ(σ_w) = δ_{w,1}` — verified symbolically on all reduced words at n = 2, 3, 4 (2 / 6 / 24 words) through explicit seminormal matrices. |

That (bκ) is the canonical symmetrising trace and (b) is not is a structural check, not a
choice. The corpus therefore carries **two different objects under the name "Plancherel
trace"**; I report both rather than picking one.

Checks run (all exact): the seminormal matrices satisfy the Hecke and braid relations
(n = 2, 3, 4); `Σ y_λ f^λ = 1`; `tr_M` is Markov with `z = q³/(q²+1)` on every H_{n−1} basis
word (n = 2, 3, 4); for (b) and (bκ) at n = 2, 3 on abstract matrix units: counit law on both
sides, the Frobenius relation `(a⊗1)Δ(1) = Δ(1)(1⊗a)`, coassociativity, and
`u = Σ (y_λ/ε_λ) p_λ`.

## Evidence — exact values

Small n (convention D, `[k]_q` balanced):

| n | λ | y_λ | u_λ^(b) | u_λ^(bκ) |
|---|---|---|---|---|
| 2 | (2) | (q⁴+q²+1)/(q²+1)² | (q⁴+q²+1)/(q(q²+1)) | (q⁴+q²+1)/(q²+1) |
| 2 | (1,1) | q²/(q²+1)² | q/(q²+1) | 1/(q²+1) |
| 3 | (3) | (q⁴+1)/(q²+1)² | (q⁴+1)(q⁴+q²+1)/(q³(q²+1)) | (q⁴+1)(q⁴+q²+1)/(q²+1) |
| 3 | (2,1) | q²/(q²+1)² | (q⁴+q²+1)/(q²+1)² | same |
| 3 | (1³) | 0 | 0 | 0 |

At q0, n = 6 (the deuteron level):

| λ | f^λ | dim_q | y_λ | 1/dim_q (co-Casimir) | u^(b) | u^(bκ) | (−1)^{n(λ)} f^λ |
|---|---|---|---|---|---|---|---|
| (6) | 1 | 1.0 | 0.11532422 | 1.0 | 96.738499 | 462.72006 | 1 |
| (5,1) | 5 | 5.2204413 | 0.07895296 | 0.19155468 | 12.686447 | 32.446765 | −5 |
| (4,2) | 9 | 9.6690482 | 0.04603243 | 0.10342279 | 3.9935490 | 6.7287131 | 9 |
| (3,3) | 5 | 5.4486070 | 0.01512381 | 0.18353314 | 2.3283836 | 3.1841853 | −5 |
| 7 blocks with ≥ 3 rows | | | 0 | (nonzero) | 0 | 0 | ± |

Tables for n = 2…6 are in the witness (symbolic and at q0).

## Verdicts

**(i) Proportional to co-Casimir? No.** `u^(b)_λ · dim_q(λ) = y_λ [n]_q!`, constant in λ only if
`y_λ` is, which it is not at any n ≥ 2 (recorded at n = 2…6; e.g. n=6 ratios run 96.7 → 12.7·5.22
→ …). The co-Casimir sum is τ-invariant (`frobenius_codim_tau_invariant`) because the τ(p_λ)
factor telescopes; the density `u` is not, because `∫ = tr_M` and `ε = τ_P` are different
traces and their ratio `y_λ/ε_λ` survives. So the Plancherel-coproduct density is a **different
object** from the co-Casimir, not a re-derivation of it.

**(ii) Sign pattern. Excluded structurally from reproducing the signed value.** At real q > 0,
`y_λ ≥ 0` (principal specialisation of a two-row Schur function over its positive normaliser),
`[n]_q! > 0`, `dim_q(λ) > 0`, `q^{κ} > 0`; so `u^(b)_λ, u^(bκ)_λ ≥ 0` on every block (asserted at
q0, n = 2…6). The proved value `Δ_λ = (−1)^{n(λ)} f^λ`
(`dtEuler_eq_deltaLambda_unconditional`) is mixed-sign at every n ≥ 2. A per-block weight that is
non-negative cannot equal it. This is the same invariant as the PROBE-4 KL-positivity prune.

**(iii) Deuteron test (n = 6), the test of `coCasimir_refuted_deuteron` / `coCasimir_wrong_sign`:**
`tol < |Σ_λ y_λ χ_λ(β_D) Δ_λ − target|` with `tol = 1` and target `−B_D/m_e = −4.3533674913`
(the current witness value).

| Δ_λ | Σ y χ Δ | gap | > tol | wrong sign |
|---|---|---|---|---|
| co-Casimir 1/dim_q | 0.17312047168 | 4.5265 | yes | yes |
| u^(b) | 16.804605752 | 21.158 | yes | yes |
| u^(bκ) | 81.627546509 | 85.981 | yes | yes |
| proved signed value (−1)^{n(λ)} f^λ (reference) | 0.53158040875 | 4.8849 | yes | yes |

Both Plancherel-coproduct densities fail, by about 5× and 19× the co-Casimir gap. The last row
is included because it is informative: the **proved** per-partition value also fails this test
with the wrong sign. That is consistent with the gate record in AGENTS.md (the value is closed;
the many-body magnitude is the open problem and no per-block Δ_λ can supply it), and it means
this test measures the missing extensive term, not the per-block weight.

Side note: `coCasimirSum` in `DeltaLambdaRefutation.lean` is `0.144959224127`; the current
witness gives `0.173120471678` (reproduced here to 1e-40). The Lean constant predates a
regeneration of the witness. The inequalities still hold, but the Lean figure is stale. Not
fixed here.

**(iv) Three-row blocks.** Under D, `y_λ = 0` for every λ with ≥ 3 rows, so `u^(b)` and `u^(bκ)`
vanish there (7 of 11 blocks at n = 6). `u` is a non-invertible central element supported on
the TL quotient. The same fact makes candidate (a), `ε = tr_M`, impossible as a counit on
`H_n` for n ≥ 3.

## Scope classification (per AGENTS.md "Before declaring refuted")

- **(iii) is scope (a).** The Plancherel-coproduct density, used on its own as Δ_λ, does not
  reproduce the deuteron number. This limits magnitudes and does not exclude the ingredient
  from a multi-term closure.
- **(ii) is scope (b), with the cited invariant being non-negativity at real q > 0.** The
  ingredient cannot equal the signed per-partition value `(−1)^{n(λ)} f^λ`. This holds for both
  ε choices and for any ε of the form (positive)·χ_λ.
- **(i) is a structural identity** (`u·dim_q = y_λ[n]_q!`), not a refutation.

## Implications

- The co-Casimir ansatz is not rescued by passing to the coproduct density. The density is a
  different and larger-magnitude object, and it carries no sign.
- The two-object ambiguity in "Plancherel trace" (with or without `q^{-κ_λ}`) is real, and only
  the κ version is the canonical trace. Any consumer of `τ_P` from
  `frobenius-codim-universal.lean` should say which one it uses. The co-Casimir value
  `Σ 1/dim_q` is insensitive to the choice, but any ε-dependent quantity, including this `u`,
  is not.
- No fitting, no rescaling: every number above is fixed by the trace choice. Nothing was tuned.

## Not established

- Whether some other framework-fixed counit makes `u` useful. Only (a), (b) and (bκ) were
  examined.
- The symbolic tables for n = 5, 6 were not inspected for closed-form structure beyond the
  ratio identity in (i).

## Naming (2026-11-15, owner choice: rename across the corpus)

The phrase "Plancherel trace" covered three different functionals. They are now named apart:

| name | weights on `p_λ` (or on `χ_λ`) | where |
|---|---|---|
| **canonical trace** | `τ(p_λ) = q^{-κ_λ} dim_q(λ) f^λ/[n]_q!`; equals `τ(σ_w) = δ_{w,1}` | `QOU/MathlibExt/MolienFakeDegree.lean`; (bκ) above |
| **unweighted Plancherel functional** `τ_P` | `τ_P(p_λ) = dim_q(λ) f^λ/[n]_q!`; valid counit, not normalised, not canonical | `frobenius-codim-universal.lean`; (b) above |
| **q-Plancherel measure trace** `tr_qP` | `Σ_λ w_λ(q) χ^λ/f^λ` with `w_λ(q) = dim_q²/[n]_q!` | `hoefsmit_symbolic.py`, `deuteron_tr_M_symbolic.py` |

Sums `Σ_λ W_λ χ^λ` with a general transpose-invariant weight (the qbeta tower probes,
`TraceRealSpectrumComplex.lean`) are called **`W`-weighted traces**. Dated audit docs keep
their original wording as records; function and file names are unchanged.
