---
# qou-augu
title: Fourteen of 57 committed LP/SDP witnesses report a zero net-constraint dual — the cause is t = G e0, not the radical
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T12:19:51Z
updated_at: 2026-10-04T15:19:22Z
parent: qou-5vkl
---


Split out of `qou/8na1`, which asked only whether the `a_K` chain divides by a
dual now known to be zero. It does not — all four divisions in the corpus are
guarded. The sweep that answered that question turned up something wider.

## The sweep

Every `computations/**/*.witness.json` carrying a `y0_star` field, flagged when
`max|y₀*| ≤ 1e-12`. **Fourteen of the 57** distinct witnesses carrying a
numeric `y0_star` hit — about a quarter — of which `8na1` knew about two:

```
a-K-via-lp-dual-full            (known)     a-K-via-lp-dual-hecke-basis  (known)
all-nuclides-sdp-admissibility              co-bond-order-active-set
confinement-lp                              frobenius-repose
he3-pairknot-composite-lp                   lp-duality-check
molecular-frobenius-lp                      pn-alpha-lp-dual
qbeta-c3-barodd-binding-sdp-dual            qbeta-confinement-sdp-offset-homogeneity
qbeta-symbolic-sdp-strict-complementarity   wedderburn-pair-volumes
```

**Count correction 2026-08-22.** This filing said "thirteen" throughout. It is
**fourteen** — miscounted off the sweep output, not off the sweep. Re-derived
programmatically over distinct witness filenames, with the denominator this
time: 57 witnesses carry a numeric `y0_star`, 14 of them zero.

## What is NOT claimed

That these share `8na1`'s mechanism. `y_0_eq_zero_of_radical` needs three
things — a radical `v` with `Gv = 0`, a cost vector with `⟨t,v⟩ = 0`, and
`Σⱼvⱼ ≠ 0`. None of the fourteen has been checked against them.

Nine of the eleven producing scripts build a trace-form / Gram object, which is
where the mechanism lives. Two — `all_nuclides_sdp_admissibility.py`,
`co_bond_order_active_set.py` — mention neither `tr_M` nor a Gram, so **at
least two of the fourteen have a different cause**, whatever it is.

`qou/pin3` is the standing reason to be careful: it was filed as the same
degeneracy seen from the numerics, and it was not — `alpha_5_lp_dual_crystal.py`
builds `G = diag(|weight_λ|)`, has no radical at all, and its real problem was
a solver tolerance amplified by dividing by `|w| ~ 1e-06`. A shared symptom is
not a shared cause, and this bean exists to check rather than to assume.

The control that shows this is not "every LP in the corpus":
`rho-k-h3a-lp-dual` reports **`y₀* = 8.671`**. A real `scipy.linprog` solve
over a Wedderburn refinement with a Plancherel or Frobenius cost —
trace-adjacent, and not degenerate.

## Second finding: the guard threshold is below the band

The four divisions by a dual all guard at `1e-12`:

- `aK_via_lp_dual_full.py:198`, `aK_via_lp_dual_hecke_basis.py:191`,
  `probes/ak_lp_dual_quotient_probe.py:189` — each returns `None`
- `aK_via_lp_dual.py:185` divides by `|tr_M|`, not a dual

Two committed witnesses report a net-constraint dual **between** the guard and
any plausible physical scale:

- `borromean-axial-coupling` — `y₀* = 1.076e-10`
- `habiro-correction-shadow-price-test` — `5.949e-08`
  (`nucleus-real-sdp-he4`, `5.933e-08`)

Neither divides by it, so nothing is wrong today. But `1e-12` would **pass** on
`1.08e-10` and hand back a quotient inflated by ~1e10 with no signal. The guard
is calibrated to floating-point zero rather than to the scale at which these
solves actually report a vanishing dual — and `pin3` is the precedent for a
small denominator producing a large wrong number that reads as a result.

---

## 2026-08-22 — answered, and the mechanism is not the radical

Ran the test. The answer is that **I was looking for the wrong hypothesis**,
and the corpus already had the right explanation written down.

### The canonical Gram, computed directly

`pyhecke` **is** importable — it just needs the path
(`PYTHONPATH=tools/pyhecke/python:tools/qou-substrate/python:computations/substrate:computations`).
`k4f8` recorded it as unimportable on 2026-08-16 and that has been carried
forward since; it is wrong, the same way the numpy/mpmath blocker was.

```
NF_NAMES        ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']
max|G - Gᵀ|     0.0                       symmetric, as a trace form must be
eigenvalues     [-0.75270211, 0.0, 0.75270211, 0.75270211, 0.75270211, 4.23033923]
rank            5          det 4.0e-17    min|eig| 1.85e-16
t (= TR_M)      [1, 0.61268804, 0.61268804, 0.37538663, 0.37538663, 0.69116648]
G row 0         [1, 0.61268804, 0.61268804, 0.37538663, 0.37538663, 0.69116648]
t == G[0]       True,  max diff 0.0
```

So at the substrate `q₀`, numerically: **rank 5, one exact zero eigenvalue** —
`k4f8`'s ℚ(q) result confirmed from the other direction — and **`t` is row 0
of `G` to the last bit**.

### The mechanism is `t = G e₀`, and it needs no radical

`y_0_eq_zero_of_radical` proves `y₀ = 0` is **forced**. But `y₀ = 0` being
*attained*, with optimal value 0, needs only `t = G e₀`: then `(y₀, y) = (0, e₀)`
is dual-feasible with objective 0, and for feasible `x`,
`Σⱼtⱼxⱼ = (Gx)₀ ≥ 0` is one of the constraints. `k4f8` said exactly this and
even has the Lean lemma — `dualCertificateExists_of_cost_eq_gram_row`, whose
only hypothesis is `ht`. `8na1` foregrounded the radical, and this bean
inherited that framing and went looking for radicals.

`t = G e₀` holds whenever the basis contains the identity and the cost is
`tr_M(bⱼ)`: `tⱼ = tr_M(bⱼ) = tr_M(b₀bⱼ) = G₀ⱼ`. Nothing about `det G`.

**The signature confirms it. Twelve of the fourteen report `y* = e₀`:**

```
e₀ only   confinement-lp · lp-duality-check · a-K-via-lp-dual-hecke-basis
          all-nuclides-sdp-admissibility · he3-pairknot-composite-lp
          molecular-frobenius-lp · pn-alpha-lp-dual · frobenius-repose
          qbeta-c3-barodd-binding-sdp-dual · wedderburn-pair-volumes
          qbeta-symbolic-sdp-strict-complementarity
          co-bond-order-active-set   (e₀-supported, scaled: [0.687, 0, 0, 0])
other     a-K-via-lp-dual-full       ([1.0, 1.0, 0.0] — partition-indexed, 3 blocks)
```

`frobenius-repose` reports `gram_rank = 6`, `gram_invertible = true` **and**
`y* = e₀` — an invertible Gram with the same certificate. That single row is
enough to rule the radical out as the cause.

### Correction to this bean's own filing

It said two of the eleven producing scripts "mention neither `tr_M` nor a Gram,
so at least two of the fourteen have a different cause". **One of the two does.**
`all_nuclides_sdp_admissibility.py`'s header reads

> `t = TR_M (H_3 Markov-trace cost vector), G = gram_matrix() (6x6), from
> pyhecke.gram (the H_3(q_0) NF basis [gamma, s0, s1, L+, L-, e-])`

— my grep looked for `tr_M`/`Gram` and the file writes `TR_M`/`gram_matrix()`.
Only `co_bond_order_active_set.py` is genuinely different: it builds its own
`linprog` over bond channels with `bounds=[(0, u)]` and no Gram at all, so its
single-support dual is most likely one active constraint rather than this
mechanism.

## Second finding: `confinement-lp.witness.json`'s Gram is not a trace form

Its committed `gram_matrix` **cannot be** `tr_M(bᵢbⱼ)`:

- **It is not symmetric** — `max|G - Gᵀ| = 0.4269`. A trace form is symmetric
  because `tr_M(ab) = tr_M(ba)`. Swapping rows 3 and 4 (`L₊` ↔ `L₋`) makes it
  **exactly** symmetric (`max|G - Gᵀ| = 0.0`), so this is a row-ordering error,
  not numerical noise.
- **It is rank 6** (`det = -0.3608`, `min|eig| = 0.414`), and after the row
  swap still rank 6 with eigenvalues `[0.414, 0.428, 0.428, 1.282, 1.282,
  2.893]` — all positive. The H₃ trace form is rank 5 for **every** `q ≠ 1`
  (`det G = 0` identically in ℚ(q), `k4f8`), so no `q` and no braid insertion
  `G^w` yields rank 6. The row swap alone does not recover the trace form.
- Its committed `gram_eigenvalues` `[-0.7408, 0.4140, 0.4281, 0.7408, 1.2820,
  2.8931]` are the eigenvalues of the **asymmetric** matrix — note the spurious
  `±0.7408` pair, the fingerprint of an antisymmetric component. `lp-duality-check`
  reports `±0.9557` around the same core and flags `"indefinite": true`.
- Its `z = 0.4993203340335982` is `G[0][1]`, whereas canonical
  `tr_M(σ₀) = 0.61268804`. Its `q0 = 1.1099785955541805` agrees with the
  canonical `1.1099785827513808` to 8 figures, so `q` does not explain it. The
  witness is dated **2026-05-02**, `git_sha c8dbe912`.

Internally it is consistent — its `markov_traces` field equals its own row 0,
so the `t = G e₀` identity holds for whatever object it is.

**And its headline claim is the one the degeneracy denies.** The description
reads *"LP proof that B₃ is the **unique** optimal confinement operator over
all of H₃(q)"*, while its own duals record `y₀* = -0.0`, `dual_obj = -0.0`,
`primal_obj = -2.04e-16`, `y* = e₀`, `active_set = [0]` — optimal value 0 for
every target. `qbeta-confinement-sdp-offset-homogeneity` states the consequence
in its own witness: *"the optimal face is not a point, so `x*` … [is] not
determined by the LP; the returned point is a solver choice."* Uniqueness is
exactly what a non-singleton optimal face precludes.

## Limitation of the sweep, found 2026-08-22

**It can only see witnesses that carry a `y0_star` field at all.** A degenerate
LP/SDP whose producer never extracts the dual is invisible to it, and there is
at least one: `computations/lp_dual_witness_validator.py` reports
`binding-sdp-bondgraph-degenerate.witness.json` missing **all six** required
fields — `y0_star`, `y_star`, `active_set`, `primal_obj`, `dual_obj`,
`duality_gap` — while its own name says "degenerate". So "14 of 57" is a count
over witnesses that report duals, not over LP/SDP computes.

(The validator runs warn-only and needs
`PYTHONPATH=computations:tools/pyhecke/python:tools/qou-substrate/python:computations/substrate`;
without it, `lp_dual_solver` fails to import `pyhecke` and the whole check
dies before scanning anything — another instance of the missing-path pattern.)

---

## 2026-08-22 — the dual-less sweep, and the gate that was meant to catch them

Started from the scripts rather than the witnesses, which is the right way
round: **71 scripts under `computations/` import a real LP/SDP solver**
(`linprog`, `cvxpy`, `lp_dual_solver`); 19 are deprecated. Of the 52 live ones,
**6 emit a same-stem witness carrying none of the required dual fields**:

```
ak-lp-dual-quotient-probe          benzene-assembly-spine
binding-sdp-bondgraph-degenerate   nucleus-operator-selection-sdp
three-quark-borromean-lp-sweep     two-quark-active-set-mahler-sweep
```

**Nothing is claimed about their duals.** They report none, so whether any is
degenerate is unknown — which is the point. The "14 of 57" figure earlier in
this bean counts witnesses that *report* a `y0_star`; the population that
should report one is larger, and the difference is invisible by construction.

### `lp_dual_witness_validator.py` found one of the six, for two reasons

Its docstring states the failure mode exactly: *"scripts that solve the primal
LP but never extract / report the dual, losing the principled binding-energy
interpretation."* It was catching **1 of 6**.

**(a) It gated on the witness's name before consulting the script.** A witness
had to contain one of ten literal strings in `LP_SDP_HINTS` before its sibling
was even looked at. `nucleus-operator-selection-sdp` — an *operator-selection*
witness — misses because the hint is `operator-selection-lp` and this one ends
`-sdp`. `three-quark-borromean-lp-sweep`, `two-quark-active-set-mahler-sweep`
and `benzene-assembly-spine` carry no hint substring at all. The property being
tested — does this script solve an LP? — is a property of the *script*, and the
solver-import test was already the guard doing the real work. Inverted: flag on
the script, keep the hint to enrich the reason.

**(b) The walk was not recursive.** `root.glob("*.witness.json")` over
`computations/` only. The Phase 6 subdirectory refactor (2026-06-02,
`computations/_path_bridge.py`) moved compute scripts and witnesses into
cluster directories, and this walk was never updated:

```
scanned by the validator : 1410
live witnesses in tree   : 2697
INVISIBLE                : 1287   (516 probes/, 362 qbeta/, 169 deltalambda/, …)
```

**48% of the live corpus.** `ak-lp-dual-quotient-probe` sits in `probes/` and
was unreachable. A check written before a refactor kept passing by seeing less.

Both fixed. `_deprecated/` stays excluded — deliberate now rather than
incidental.

```
before  scanned 1410   flagged 12   missing 1
after   scanned 2697   flagged 27   missing 6
```

Still warn-only (exit 0; `--strict` exits 1), and nothing in CI runs it —
`scripts/check-sidecars.sh` only mentions it as advice. So widening it turns
nothing red.

### Third instance of the same shape in this bean

`y_0_eq_zero_of_radical` looked for the wrong hypothesis; the Python sweep lost
declarations to a missing `axiom` keyword; this gate scoped itself to a naming
convention and a pre-refactor directory. Each time the check was narrower than
its stated purpose **and said nothing about it**.

---

## 2026-08-22 (second) — three of the six were never missing a solve

**6 → 3.** The framing "route them through the solver" was wrong for half the
list: three of the six **already call the canonical solver** and had the duals
in hand. They just did not put them in the witness.

| producer | what was wrong | fix |
|---|---|---|
| `binding_sdp_bondgraph_degenerate` | computed `solve_operator_selection_lp(...).to_dict()` for three targets and emitted **one boolean** | keep the per-target duals |
| `nucleus_operator_selection_sdp` | emitted them under `lp_`-**prefixed**, `round(..., 5)`-ed names | add the canonical names alongside |
| `ak_lp_dual_quotient_probe` | emitted 3 of the 6 required fields | add `y_star`, `active_set`, `dual_obj` |

Each is worth noticing for a different reason.

`binding_sdp_bondgraph_degenerate`'s **entire claim is about the duals** — its
witness asserts `sdp_bondgraph_degenerate = 1` and carried none of the numbers
establishing it. That is the validator's stated failure mode exactly.

`nucleus_operator_selection_sdp` shows the contract is a **naming** contract.
`lp_y0_star` is not `y0_star`, so the recursive key search could not see it,
and the rounded copies fall outside `LP_DUAL_F64_FIELDS` too — the prefix cost
it both the contract check and the carve-out. `lp_confinement_nf_forcing.py`
already emits both forms; that is the pattern followed here.

`ak_lp_dual_quotient_probe` had the missing values **in the same expression
that produced its verdict** — `chir` sums `quo.y_star` over `quo.active_set` —
so the conclusion rested on numbers the witness did not carry.

### And two of them are degenerate

The point of the exercise. `nucleus-operator-selection-sdp`, now that it
reports canonically, across D / T / ³He / ⁴He:

```
y0_star     [-0.0, -0.0, -0.0, -0.0]
y_star      [[1,0,0,0,0,0]] x 4
active_set  [[0], [0], [0], [0]]
dual_obj    [-0.0, -0.0, -0.0, -0.0]
```

`binding-sdp-bondgraph-degenerate` reports `y0* = -0.000000, active_set = [0]`
at all three of its targets and calls it DEGENERATE in its own prose.

Both are the **`t = G e₀`** signature: the basis contains the identity, so
`tⱼ = tr_M(bⱼ) = tr_M(b₀bⱼ) = G₀ⱼ`, `(0, e₀)` is dual-feasible with objective
0, and the objective is bounded below by one of its own constraints. Four more
nuclei plus three more targets, previously invisible to the sweep — for two
different reasons, neither of them "the LP is fine here".

### Float64: the carve-out is the right home, and it was checked

Adding raw solver output to a witness that had **zero** raw float64 would
regress the `witness_raw_float64_audit.py` ratchet, so it was run:
`NEW dirty 0, REGRESSED 0, exit 0`, with the excused total rising 3,661 →
3,892 across 43 witnesses. The values land inside `LP_DUAL_F64_FIELDS`
(owner decision 2026-08-11) — f64 by construction, no mpf upstream to carry,
and stringifying would break every consumer that does arithmetic on them.
Counted and reported as `carved_out`, not hidden.

---

## 2026-08-22 (third) — CORRECTION: two of the "three different LPs" were the same LP

**6 → 1.** The claim above that the remaining three are "genuinely different
LPs, not missing emissions" is **wrong for two of the three**. I based it on
grepping one `linprog(...)` line per file and seeing `A_ub` / `A_eq` — reading
"has its own constraint matrices" as "different program". In
`three_quark_borromean_lp_sweep.py` the matrix is literally

```python
A_ub = -G          # G x ≥ 0 ⇔ -G x ≤ 0
A_eq = np.ones((1, d))
b_eq = np.array([n_target])
bounds = [(-M, None)] * d
```

That is `prop:operator-selection-lp` verbatim, box included.
`two_quark_active_set_mahler_sweep.py` is the same at `d = 2`. Both **already
compute** `x_star`, `y0_star`, `y_star`, `active_set` — and both write
hand-rolled witness dicts that keep the *transitions* and the *verdict* and
discard the duals the verdict is drawn from. Same defect as
`binding_sdp_bondgraph_degenerate`, third and fourth instance.

Fixed: duals emitted at each script's own named points — the four metallic
anchors for two-quark, the transition brackets for three-quark — plus
canonical top-level aggregates. `dual_obj` and `duality_gap` are derived
(`n_target · y0_star`, `|primal − dual|`) because neither solver returns them.

### And the new numbers are the H₂/H₃ contrast, visible for the first time

**`two-quark-active-set-mahler-sweep`** — `H₂`, `d = 2`:

| anchor | `y0*` | `y_star` | active |
|---|---|---|---|
| `q_0` | **-0.0** | `[1, 0]` = e₀ | `[0]` |
| `phi` | **-0.0** | `[1, 0]` = e₀ | `[0]` |
| `delta_silver` | 5.6569 | `[0, 0]` | `[]` |
| `delta_bronze` | 5.8590 | `[0, 0.125]` | `[1]` |

This is **"attained but not forced"** in one table. `k4f8` proved `H₂`'s Gram
is non-singular, so nothing forces `y₀ = 0` there — and indeed the `t = G e₀`
certificate, which is always *available*, stops being *optimal* above
`δ_silver`, where the LP finds `y₀ > 0`. At `H₃` the radical forces `y₀ = 0`
at every `q`. The distinction this bean drew from theory is now a committed
measurement, and it was unreadable while the witness discarded its duals.

**`three-quark-borromean-lp-sweep`** — `y0* ≈ 27.5` at all four brackets,
active sets `[0,3,4,5]`, `[3,4,5]`, `[1,2,3,4,5]`. **Not degenerate**, and it
should not be: its Gram is the script's own approximation
(`G[i,j] = t_i t_j / ‖t‖₁ + δ_ij |t_i|`), not the trace form, so `t` is not a
row of `G` and there is no radical. A third control alongside
`rho-k-h3a-lp-dual` (`y₀* = 8.671`) and `frobenius-repose` (invertible Gram,
`y* = e₀`): the signature tracks the trace-form Gram specifically, not "any LP
over the H₃ basis".

Ratchet re-checked: NEW 0, REGRESSED 0, exit 0; excused 3,892 → 4,052 in 45
witnesses. Validator 6 → **1**.

## Next

- [ ] The remaining **1** is genuinely a different LP:
      `benzene_assembly_spine` — `max Σxᵢ s.t. Σxᵢ ≤ min(3, pairs),
      0 ≤ xᵢ ≤ 1`, a cardinality knapsack with no Gram, no `n_target`
      equality and no Frobenius row. Its only dual is the multiplier on the
      dimension cap. Either report that in its own form, or decide the
      operator-selection contract does not apply and teach the validator so —
      **a judgement, not a mechanical fix**. Verified by reading the LP this
      time, not by grepping the call.
- [ ] Re-run the `y0_star` sweep once those three are settled, for a count
      over the whole population rather than over what happened to report.
- [ ] Consider wiring `lp_dual_witness_validator.py` into CI diff-scoped, the
      way the vacuity audit is. It is not run by anything today.
- [ ] `confinement-lp.witness.json`: re-derive the Gram from `pyhecke.gram`,
      or establish what the committed matrix is. Then re-read the "unique
      optimal B₃" claim against a degenerate optimal face. **Own bean.**
- [ ] Fold the correction back: `8na1` should lead with
      `dualCertificateExists_of_cost_eq_gram_row` (needs only `t = G e₀`) and
      treat `y_0_eq_zero_of_radical` as the *uniqueness* refinement it is.
- [ ] Correct `k4f8`'s "pyhecke is not importable in this sandbox" — it is.
- [ ] Re-calibrate the four `1e-12` guards, or justify them against the
      observed `1e-10`/`1e-8` band.
- [x] Test the trace-form scripts against `y_0_eq_zero_of_radical`'s
      hypotheses — done; the radical is not the operative hypothesis.
- [x] The non-trace scripts — one of the two was miscounted; see above.

In-progress in Round 100 PR litlfred/qou#8447.
