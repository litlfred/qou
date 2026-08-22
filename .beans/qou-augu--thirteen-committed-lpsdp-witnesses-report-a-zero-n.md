---
# qou-augu
title: Fourteen of 57 committed LP/SDP witnesses report a zero net-constraint dual — the cause is t = G e0, not the radical
status: todo
type: task
priority: normal
created_at: 2026-08-22T12:19:51Z
updated_at: 2026-08-22T15:33:12Z
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

## Next

- [ ] Re-run the sweep over LP/SDP witnesses **lacking** a `y0_star`, starting
      with `binding-sdp-bondgraph-degenerate`. A dual that was never extracted
      is a weaker signal than one extracted and found zero, but it is not no
      signal.
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
