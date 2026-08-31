# Binding functional: attack vectors, the interface floor theorem, and a Li₂^q guard defect

**Date**: 2026-08-08
**Branch**: `claude/anchor-followups-2026-08-08`
**Beans**: `qou-c6gx` (interface closed form), `qou-h7mh` (coordination, premise
corrected here), `qou-xzda` (Reeb override removal)
**Status**: Audit. All numbers read-only, no witness written, no producer run.

Follows the removal of the `B = 5g` Reeb override (`5e0c874b`), which had been
making the deuteron come out exact. With the trace value restored, ²H over-binds
by +74.85% and the question is where that lives. This localises it, rules out
five candidate causes with measurements, and records one outright defect found
on the way.

## §1. The interface is 2-dimensional — closed form

σ₂ is the only generator joining strand 2 (nucleon k's last quark) to strand 3
(nucleon k+1's first), so the inter-nucleon sector *is* the word at gen 2. That
subalgebra is two-dimensional: σ² = h·σ + 1 gives span{1, σ₂}. So every
interface element is a·σ₂ + b·I, and with the Markov property
tr_M(W·σ₂) = z·tr_M(W),

```
tr_atom = tr_free · (a·z + b)          B = −α·ln(a·z + b)
```

Verified against `chi_all_lambda_reduced_block` at all four whitelisted
crossings, residual **4.489e-32** (uniform — the shared tr_free floor, not a
per-case error). Consequences:

```
L_XY = −ln(z + d_XY),   z = 1/(√q₀ + 1/√q₀) = 0.4993203341836944524

  σ      (pp)  d = 0            μ = 0.499320334  L = 0.694507437  B = 2.907195
  cw     (pn)  d = −h(½ − δ/4)  μ = 0.394862086  L = 0.929218723  B = 3.889692
  avg    (pn)  d = −h/2         μ = 0.394790185  L = 0.929400833  B = 3.890455
  σ⁻¹    (nn)  d = −h           μ = 0.290260035  L = 1.236978084  B = 5.177967
```

`L_pp = ln(1/z)` **exactly**. Now wired into `mass_binding_dashboard._bond_type_L`,
replacing three transfer runs and an f64 collapse (`math.log(float(tf)/float(ta))`).

## §2. Ruled out, with measurements

| candidate | verdict |
|---|---|
| tr_free missing a term / double-counting | **No.** tr_free = tr_p·tr_n exact to 2.417e-30. The HOMFLY `((1−λq)/(√λ(1−q)))^(n−1)` prefactor and the split-link loop factor both cancel in the ratio — free and atom are both n = 6. |
| dropped writhe / framing | **Real, negligible.** The Lean-proved `Ŝ = S·(1−h)^((e−n)/2)` applies, but e_atom − e_free = 6.879e-4 because the p–n crossing sits at t ≈ 0.4997, i.e. ~zero net writhe. Worth 3.2e-4 MeV. |
| colour-weighted vs colour-blind | 0.00076 MeV apart. Cannot matter against a 1.665 MeV gap. |
| SDP weights | **Not used.** Production y_λ is `wedderburn_jones_markov.y_lambda_at(n, q₀)`, the closed-form Jones–Markov hook-length weight. The SDP dual `y_star` never reaches `tr_m_atom_zn`. Its `n_target` is the colour-**blind** trace, so it was never solved against the shipped word. |
| α is mis-scaled | **Refuted** — see §4. |

Two structural constraints also forbid *adding* knot content at the interface:
`chi_monotone_transfer.word_to_mpfr` requires a **monotone** word (so
σ₁σ₂σ₁⁻¹ to reach strands 1↔3 is rejected) and **whitelists exactly four
crossings**.

## §3. The floor theorem

For a = 1 and d ∈ [−h, 0], μ = z + d ranges over [z−h, z]; −ln is strictly
decreasing, so

```
B ∈ [α·ln(1/z), α·ln(1/(z−h))] = [2.907195, 5.177967] MeV
```

AME(²H) = 2.2245662 is **30.69% below the minimum**. No crossing sign, colour
weight, or multiplicity reaches the deuteron. Stacking is worse than useless:
σ² gives μ = 1.1044, i.e. B = −0.416 MeV.

## §4. A-scaling refutes any rescaling

Under B = −α·Σ_bonds ln μ_k the model is exactly additive, so the deficit's
A-dependence discriminates. It **changes sign**:

```
atom  nb   B_pred    B_AME    err %    per-bond deficit
2H     1   3.8897    2.2246   +74.85      +1.6651
3H     2   9.0677    8.4818    +6.91      +0.2929
3He    2   6.7969    7.7180   −11.94      −0.4606
4He    3  11.9749   28.2957   −57.68      −5.4403
6Li    5  20.0600   31.9946   −37.30      −2.3869
7Li    6  25.2380   39.2445   −35.69      −2.3344
```

Spread 7.105 MeV/bond (chain), 3.024 (full pairing). Best-fit α leaves a 178%
worst residual under chain, 56.5% under full pairing — quoted only to kill the
hypothesis, **not** as a proposal.

Stronger still: the per-bond μ *implied* by AME is not constant —
0.5878 (²H), 0.3631, 0.3978, 0.1051 (⁴He), 0.2168, 0.2096. **No single-scalar
interface model of any kind, at any q, reproduces the table.** That rules out
the functional form, not merely the parameter range.

## §5. The bond multiset is not well defined

`atom_braid_word_3A` hard-codes `ordering = ['p']*Z + ['n']*N`, and B depends
on it:

```
atom   canonical   B_canon    B_min     B_max    spread   B_AME
3He    ppn          6.7969    6.7969    7.7794   0.9825   7.7180
4He    ppnn        11.9749   10.6866   12.9574   2.2708  28.2957
6Li    pppnnn      20.0600   18.4660   21.0425   2.5766  31.9946
7Li    pppnnnn     25.2380   23.3382   26.2205   2.8823  39.2445
```

A nucleus has no ordering, so up to 2.88 MeV is a non-physical degree of freedom.
The convention is not even the good choice: `3He = pnp` gives 7.7794 (+0.79%)
where canonical `ppn` gives −11.9%. The mirror pair is decided by it outright —
`pnn`/`ppn` splits 2.271 MeV, `npn`/`pnp` splits **exactly 0** (nature: 0.764).

## §6. Charge independence is impossible unless q = 1

The strong force is charge-independent, so L_pp = L_nn is required. In this
model that is `z = z − h`, i.e. `h = 0`, i.e. `q = 1` — the classical limit
where the Hecke structure collapses. As it stands:

```
α(L_nn − L_pp) = 2.27077201889 MeV
```

which is **identically** the model's entire ³H/³He mirror splitting. So the
mirror split this framework predicts is a charge-dependence artifact of the
σ (pp) / σ⁻¹ (nn) assignment, not a physical isospin effect. Nature's 0.764 MeV
is mostly Coulomb.

## §7. The eightfold way is the right object, wrongly assigned

The Hecke quadratic already carries the isospin decomposition for free:
(σ − q)(σ + 1/q) = 0 gives orthogonal projectors, and for two nucleons T=1 is
isospin-symmetric, T=0 antisymmetric.

```
P₊ = (σ + 1/q)/(q + 1/q)      μ₊ = (z + 1/q)/(q + 1/q) = 0.696325426  B₊ = 1.5151 MeV
P₋ = (q − σ)/(q + 1/q)        μ₋ = (q − z)/(q + 1/q)   = 0.303674574  B₋ = 4.9888 MeV
                              μ₊ + μ₋ = 1 exactly
```

Assigning T=1 to all like pairs and T=0 to the pn pair improves A ≥ 3 sharply
(³H −5.46%, ³He +3.90%, ⁶Li +3.60%, against the chain's +6.91/−11.94/−37.30) but
worsens ²H to +124% and makes ³H/³He exactly degenerate. Clebsch variants
(geometric √(μ₊μ₋), arithmetic (μ₊+μ₋)/2 = ½) put ²H at +46.2% / +30.4% but
break ⁶Li/⁷Li. Right object, wrong assignment.

## §8. DEFECT: `li_2_q` reports divergence where the function is finite

`_li_2_q_util.li_2_q` sums Li₂^q(z) = Σ z^n/(n·[n]_q), radius |z| < q, and
**hard-returns `mp.mpf('inf')` when |z| ≥ q**. That guard — not the function —
is what makes the atom-word brane tower "diverge for Z ≥ 2"
(`borromean_binding_recompute` docstring, and the dashboard's `m_can⁰` note).

Closed form. With [n]_q = (qⁿ − q⁻ⁿ)/h,

```
z^n/(n[n]_q) = (h/n)·Σ_{m≥0} (z·q^{−1−2m})^n
⇒  Li₂^q(z) = −h · Σ_{m≥0} ln(1 − z·q^{−1−2m})
```

a q-product convergent off the poles {q^{1+2m}}, and it **is** the analytic
continuation. Verified against the series to **1.2e-45** at z ∈ {−1, −0.5, 0.5,
0.9, 1.05}, and finite where the guard returns inf (z = −2 → −1.43814272667888,
z = −5 → −2.75275536231868).

The tower only ever evaluates g(x) = −Li₂^q(−x) at x > 0, where every factor is
1 + x·q^{−1−2m} > 0. **So g is real, positive-argument, and finite for all x > 0
— there is no singularity on the path the tower actually takes.** Only one
argument even crosses the radius: τ_p² = 1.13488 against q = 1.10998, over by
2.2%.

**Borel resummation is the wrong tool here.** The ratio test gives
|a_{n+1}/a_n| → |z|/q — a **geometric** divergence (measured: 0.9053 at n=10,
1.0024 at n=50, 1.0173 at n=200, → 1.022432). Borel targets factorial growth; on
a geometric series it reproduces the same singularity. Analytic continuation is
the right tool and the q-product above is it, in closed form.

Recomputing the atom-word tower with the continued g:

```
atom     1-body     2-body    B_tower     B_AME     err %
2H     2.061309  0.3863699   2.447679   2.224566    +10.03
3H     3.250086  1.2786696   4.528756   8.481798    −46.61
3He    3.292395  1.2036063   4.496002   7.718043    −41.75
4He    3.756166  2.4822759   6.238442  28.295673    −77.95
6Li    3.940721  6.2877182  10.228440  31.994564    −68.03
7Li    3.665575  8.9646174  12.630193  39.244524    −67.82
```

²H at +10.03% is the best deuteron any route in the framework produces. The rest
is worse than the Borromean route, so this does not replace it — but the stated
reason for preferring Borromean ("the atom-word tower diverges") is **false as
stated** and should be restated as a numerical-accuracy or magnitude argument,
or dropped.

## §9. The tower is truncated twice

`B_can⁰` is level 0 (the linear trace difference E₀·Δtr), and `B_tower` adds only
the **2-body** term E₀·z²·Σ_pairs. 3-body (c₃) and higher are not wired. What the
2-body term supplies, and what is still missing:

```
atom     1-body     2-body    B_tower      B_AME  still missing  per-triple
2H     2.0898131  0.3904831   2.4802963   2.224566   −0.2557303        n/a
3H     3.5638785  1.3551476   4.9190261   8.481798    3.5627719   3.562772
3He    3.1287942  1.1714493   4.3002435   7.718043    3.4177995   3.417799
4He    3.8607662  2.5265969   6.3873631  28.295673   21.9083100   5.477077
6Li    4.1064712  6.4083414  10.5148130  31.994564   21.4797510   1.073988
7Li    4.1314153  9.3023347  13.4337500  39.244524   25.8107740   0.737451
```

⁴He needs ~5.48 MeV per triple. The corpus's c₃ candidates are +0.006 MeV
(Borromean, `c₃^Borr = E₀(1 − τ_Borr)`, τ_Borr = (4 + h² − 3h⁴ − h⁶)/(h² + 4),
closed form, 0 free params) and −1.59 MeV (pairwise ρ_F) — differing in **sign**,
and the larger of them ~3× too small. Higher cluster orders do not close ⁴He.

## §10. Formalizability

**Six of these are now machine-verified.**
[`content/quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean)
compiles `lean`-direct at **exit 0**, sorry-free and axiom-free. (The three
`sorry`/`axiom` tokens a grep finds in it are prose in the module docstring,
describing `jones-markov-trace.lean`, not declarations.)

Environment note, since the skill file asks for these to be recorded: the
toolchain host `release.lean-lang.org` is **403 by egress policy** here, so
`elan toolchain install` cannot work. The documented route succeeded —
`scripts/lean-toolchain-cache-restore.sh` (branch `lake-cache/toolchain-v4-24-0`)
then `scripts/lean-cache-restore.sh` (branch `lake-cache/qou-v4-24-0`,
**6990 mathlib oleans**), then `scripts/lean-verify.sh`. Total a few minutes,
no Mathlib build. `.claude/skills/local/lean-environment-setup.md` §"Mathlib
cache 403 fallback" is accurate and was the fix.

| statement | Lean name | status |
|---|---|---|
| interface subalgebra is 2-dimensional (§1) | `interface_mul` | **proved** |
| `tr_atom = tr_free·(a·z + b)` (§1) | `interface_scalar` | **proved, conditional** — takes Markov as a hypothesis |
| `L_pp = L_nn ↔ h = 0` (§6) | `charge_independence_iff` | **proved** |
| admissible `μ ∈ [z−h, z]` (§3) | `mu_mem_Icc` | **proved** |
| floor theorem — target above `z` unreachable (§3) | `mu_unreachable` | **proved** |
| stacking gives `μ > 1`, i.e. anti-bound (§3) | `stacked_crossing_gt_one` | **proved** |
| `P₊ + P₋ = 1` (§7) | `proj_add_eq_one` | **proved** |
| `P₊·P₋ = 0` (§7) | `proj_mul_eq_zero` | **proved** |
| `Li₂^q(z) = −h·Σ ln(1 − z q^{−1−2m})` (§8) | — | **not attempted** — Fubini on a doubly-indexed sum; bean `qou-cw27` |
| `g(x) = −Li₂^q(−x)` finite ∀ x > 0 (§8) | — | **not attempted** — easy (each factor `1 + x q^{−1−2m} > 0`), but belongs with the identity above |
| cluster remainder bounds (§9) | — | **not attempted** — `\|τ\| < 1` is easy, the Li₂^q remainder is real analysis |

Two deliberate choices in that file. The ordered results are stated about the
*scalar* `μ` over `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` rather
than about `ℝ`, per §7c — the `−ln` is cosmetic, the content is the interval.
And the algebra is a plain `[Ring A]` over commutative scalars, so nothing
assumes the Hecke algebra is commutative.

The floor theorem is the one that matters: `mu_unreachable` is a *machine-checked
impossibility*. No crossing sign, colour weight, or multiplicity reaches the
deuteron, and that is now settled rather than measured.

Existing Lean status of the ingredients actually used:

- `σ² = h·σ + 1` — a **structure field** (`quadratic`) in
  `knot-eigenbasis-complete.lean:88`, i.e. a hypothesis, not a theorem.
- Markov property — a structure field (`markov_stab`, same file:246) and, in
  `jones-markov-trace.lean`, `axiom jones_markov_trace_exists` carrying the
  file's single `sorry`, explicitly marking where Jones (1987) would go.
- Writhe normalisation — `QOU/QBeta/WritheNormalisation.lean`, **0 sorries,
  0 axioms**. Genuinely proved, and the one ingredient measured to be
  negligible.

So the closed form is conditional on an axiomatised Markov trace. That is
standard practice, but "Lean proved" is the wrong label, and the only fully
proved ingredient does not matter numerically.

## §10a. The functional is DERIVED, not chosen — and it is the log form

The choice between `B = −α·ln μ` and `B = α·(tr_free − tr_atom)` is not a
preference. Two facts force it, one checked here and one physical.

1. **tr_M is multiplicative** over independent subsystems — the Markov trace's
   behaviour on a split braid — and the atom word inherits it:
   `tr_atom = tr_free · Π_bonds μ_k`. Verified: the factorisation to 7.9e-31,
   the bond product to 1.2e-31.
2. **Energy is extensive**: for non-interacting `A`, `B`, `m(A ⊔ B) = m(A) + m(B)`.

A map from a multiplicative trace to an additive energy must satisfy
`f(xy) = f(x) + f(y)` — the Cauchy functional equation on `(ℝ₊, ×)` — whose only
continuous solutions are `f(x) = c·ln x`. **The log form is forced.**

> **Convention scope, added 2026-08-31.** The `1.4875` below is a
> **convention-C** figure — this audit is dated one day before the 2026-08-09
> convention-D excision. Re-measured at the proton pin with `μ_pp = z`,
> `μ_nn = z − h`: **C gives 1.487498** (matching to 1.6e-6), **D gives 0.966887**.
> The conclusion is unaffected in either convention, because the defect has the
> closed form `−α(1−x)(1−y)`, which vanishes only at `x = 1` or `y = 1`
> (`QOU.QBeta.InterfaceScalar.linearForm_extensivity_defect`, sorry-free — an
> identity, so it needs no anchor). Only the quoted number needs the scope.

Measured, on `x = μ_pp`, `y = μ_nn`:

```
f = −α·ln t     |f(xy) − f(x) − f(y)| = 0            EXTENSIVE
f = α·(1 − t)   |f(xy) − f(x) − f(y)| = 1.4875       NOT EXTENSIVE
```

The linear form's failure is not marginal — it carries a **hard ceiling**.
Since `tr_atom > 0`, `B_lin ≤ α·tr_free`, and `tr_M(nucleon) ≈ 1` makes
`tr_free ≈ 1` at every A:

```
atom   tr_free   ceiling    B_AME    exceeds ceiling?
2H     0.9835    4.1170     2.2246   no
3H     0.9080    3.8010     8.4818   YES — impossible
4He    0.9673    4.0492    28.2957   YES — impossible
7Li    0.8784    3.6768    39.2445   YES — impossible
```

The linear form cannot produce binding above ~4.2 MeV for **any** nucleus. The
dashboard's `B_can⁰` column is exactly this saturation in the open —
2.49, 3.37, 3.52, 3.82, 3.95, 3.67, all pinned under α. Its better ²H agreement
(+12.0% vs +74.9%) is the linearisation error partly cancelling the model's
over-binding, not a better functional.

## §10b. ²H is a zero-freedom prediction of q₀

With the functional derived, A = 2 has exactly one bond and therefore

```
B(²H) = −α·ln μ_pn,   α = m_e/(q₀(q₀−1)),   μ_pn = z − h(½ − δ/4),
z = 1/(√q₀ + 1/√q₀),  h = q₀ − 1/q₀,  δ = flavor_split_leading(q₀)
```

Every symbol is a function of `q₀` and `m_e`. No free parameter, no topology,
no coordination, no crossing count. It predicts **3.88969 MeV** against AME
**2.224566** — **+74.85%**.

So the gap is cornered. It is not:

| route | why not |
|---|---|
| the functional | derived above; the alternative is non-extensive and capped |
| the interface | Lean `mu_unreachable`: AME is 30.69% below the *whole* admissible family |
| coordination | one bond has no topology to get wrong |
| the anchor | making ²H exact needs q₀ = 1.23194 vs 1.10998, a **11%** shift — 9.5×10⁶ times the μ–p tension of 1.15e-8 |

What remains is narrow and specific: either the derivation of `z` (the Markov
parameter, which fixes the bond scalar) is wrong, or `α = m_e/(q₀(q₀−1))` — an
electron-scale quantity — is not the right scale for the *nucleon–nucleon*
interface. The second is worth stating plainly because the framework applies one
α to leptons, nucleon masses, and nuclear binding alike, and only the first two
are calibrated.

## §11. What this leaves

The chain is coherent from q₀ through tr_M — one anchor, exact arithmetic, and a
free-factorisation identity holding to 2.4e-30. The defect is in the map from
trace to energy, and §4 shows it is a defect of **form**, not of scale: no
single-scalar per-bond model reproduces the table. The two live routes are

1. isospin-channel assignment done properly (§7) — pn is a T=0/T=1 mixture, and
   a Clebsch weighting derived rather than guessed would break the ³H/³He
   degeneracy without a fit;
2. charge independence imposed as a constraint (§6), letting the Coulomb term
   `E_C` (already in the dashboard) carry the mirror split.

Both are parameter-free and both are formalizable. Neither is wired.
