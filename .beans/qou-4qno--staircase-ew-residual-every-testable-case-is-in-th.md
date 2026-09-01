---
# qou-4qno
title: 'Staircase EW-residual: every testable case is in the TL kernel — rho_k has k rows, so only k=2 is physical at N=2, and the block calls that case untestable'
status: todo
type: task
created_at: 2026-09-01T07:53:25Z
updated_at: 2026-09-01T07:53:25Z
---

Found while auditing the Standard-Model work against the full tower (owner request, 2026-09-01). Probe: `computations/qbeta/qbeta_staircase_ew_lives_in_the_tl_kernel_probe.py` (4/4).

## The observation

`content/quantum-observable-universe/mass-theory/staircase-ew-residual.md`
conjectures, for the staircase partition `rho_k = (k, k-1, ..., 1)`, an
eigenvalue ratio `q^{1/(2k-1)}` on the Specht module `V_{rho_k}` of
`H_{n_k}(q)`. **`rho_k` has exactly `k` rows**, so the Schur-Weyl row cap
(`dim V_lambda = 0` when `l(lambda) > N`) gives `N_min(rho_k) = k`.

The framework's fibre is `N = 2` — `lem:feynman-eigenbasis-decomposition`
puts the cap `l(lambda) <= 2` **in the index set** of the mass channel's
decomposition. So of the conjecture's "for every `k >= 2`", **exactly one
instance is physical: `k = 2`.**

And `k = 2` is the case the block itself calls **untestable** — *"the word
collapses to length 0 ... renders the case untestable"*.

| k | rho_k | rows | dim | N_min | physical at N=2? | block's empirical content |
|---|---|---|---|---|---|---|
| 2 | (2,1) | 2 | 2 | 2 | **yes** | **untestable** (word length 0) |
| 3 | (3,2,1) | 3 | 16 | 3 | no | closes `cot theta_W` 2.19 % -> 0.13 % |
| 4 | (4,3,2,1) | 4 | 768 | 4 | no | pairwise ratio, 0.14 % rel. error |
| 5 | (5,4,3,2,1) | 5 | 292864 | 5 | no | — |

**Measured**, n = 6, convention D: `|omega_(3,2,1)| = 1.87e-16` against a
minimum `7.56e-2` over the `<=2`-row shapes; `720 = 6!` total against
`132 = Catalan(6) = dim TL_6` visible. So `(3,2,1)` is in the **kernel** of
`H_6(q) -> TL_6(q) = End_{U_q(sl_2)}(V^{(x)6})` and contributes nothing to any
trace the framework computes.

## What this is NOT

**Not a refutation.** The conjecture is about Specht modules of `H_{n_k}(q)`
as an abstract algebra; those exist for every `k` and the eigenvalue ratio is
not challenged here. **Downstream Lean is unaffected** — the block axiomatises
the conjecture as a hypothesis-only `class`, so its consumers are
rigorous-conditional and stay so.

What is in question is what the **empirical content** can mean. `cot theta_W`
is a physical observable, and the `k = 3` bullet reads it off a module the
framework's own fibre gives dimension zero.

## Why it matters beyond this block

This is the same defect `qou-i9gk` closed against Step 27 of `qou-cds1` on
2026-09-01 — reading physical content out of the trace-blind sector — surfacing
**independently in the electroweak sector**, where it has not been recognised.
It is a second instance, so the pattern is worth a sweep rather than a one-off
fix.

Related: `qou-e9le` (the two-row cap is proved in Lean and unused in compute)
is the compute-waste face of the same fact; `qou-fvzm` proves `N = 2` is
locked for the mass pipeline and that moving to `N = 3` re-weights channels the
pipeline already evaluates.

## Todo

- [ ] Decide with the owner whether the block should carry a row-cap caveat. It
      already disowns the number in other ways; this is an additional and
      structural ground, and editing a content block with a QA sidecar is an
      owner-facing editorial call, not an agent one.
- [x] Sweep for other physical numbers read off `l(lambda) > 2` blocks. **Done
      2026-09-01** — see below. No new sector.


---

## The sweep, done (2026-09-01)

Probe: `computations/qbeta/qbeta_row_cap_sweep_of_physical_numbers_probe.py`
(10/10). 3064 live witnesses scanned (`_deprecated/` excluded), 435 carry a
`>2`-row partition, **91** single one out *and* mention an observable. Triaged
in full — the assertion `triage_is_total_no_untriaged_left` is what makes the
headline worth anything:

| verdict | n | |
|---|---|---|
| INSTANCE | 3 | `path-b-evacuation`, `staircase-ew-predictions`, `staircase-ew-residual-conjecture` |
| SUPPORTING | 1 | `path-b-open-questions` |
| ABOUT THE VANISHING | 8 | states the cap rather than violating it |
| SAFE | 63 | trace-only or inert |
| FALSE POSITIVE | 16 | two classes, below |

**No new sector.** Every confirmed instance is on
`conj:weinberg-angle-categorical` — the chain this bean already records — and
all three reduce to one number, the ratio of the top two positive eigenvalues
of the `beta_EW` word in the `(3,2,1)` Hoefsmit rep of `H_6`
(`path_b_evacuation.py:456-478`):

```
max+/2nd-max+   = 1.78315071        raw error   2.1896 %
x q_0^(1/5)     = 1.82075274        corrected   0.1270 %
CODATA cot th_W = 1.82306787
```

Re-run 2026-09-01 under mpmath 1.4.1 (the witness was computed under 1.3.0):
the assertion reproduces unchanged at `0.00127`. That the defect is **one
chain rather than endemic** is a real result, and it was the likelier outcome
to be wrong about.

## What is new, and it sharpens the owner decision above

**The corpus already guards this number — on anti-fit grounds, and only there.**
`appendix-standard-model/sm-params-gauge-couplings.md` records that the
exponent "was selected as the closest of 74 enumerated candidates", that
"availability after a proximity search is not derivation", and concludes the
parameter "stays *conjectural*". `docs/sm-eightfold-derivation-cheat-sheet.md`
repeats it. **Neither mentions the row cap**, and the two objections do not
have the same consequence:

- **anti-fit** → the route is **open**, pending someone deriving `q^(1/5)`.
- **row cap** → the route is **closed whatever the exponent turns out to be**,
  because the spectrum being read has no states in `V^(x)6`.

A future session that succeeded in deriving `q^(1/5)` would believe it had
closed the Weinberg gap. It would be wrong, for a reason **no surface states**.

Surface audit — 4 surfaces carry the number, none carries the row-cap ground:

| surface | guarded? |
|---|---|
| `appendix-standard-model/sm-params-gauge-couplings.md` | yes (anti-fit) |
| `docs/sm-eightfold-derivation-cheat-sheet.md` | yes (anti-fit) |
| `mass-theory/staircase-ew-residual.md` | **no** |
| `mass-theory/staircase-corner-hook-proof.md` | **no — and it contradicts the guard** |

`staircase-corner-hook-proof.md` calls the corner hook "the **arithmetic
anchor**" and says the exponent "uses *exactly* this corner hook", where the
guard says availability after a proximity search is not derivation.
`h_corner(rho_k) = 2k-1` is a theorem; that the residual exponent is
`1/h_corner` is the conjecture, and the proof block reads as though the first
established the second.

**The conjecture block's own definition already excludes Path B's object.**
`weinberg-angle-categorical.md` defines `cos th_W` through
`tr_M(e_W^+ . sigma_1^4)`, and `tr_M` puts weight zero on `(3,2,1)` by the row
cap. So `0.659` (the block's stated trace evaluation, a ~64 % miss) and
`1.8208` (Path B) are not two estimates of one quantity — one is computed
inside the carrier and one outside it. Every repair the block proposes for its
miss ("non-uniform pure-pattern multiplicities", "categorical-linking", "Higgs
vev weighting") is inside.

## Two false-positive classes, recorded because the triage nearly ate them

1. **spectrum-as-partition.** `{5,5,5,1}` and `{5,5,1,1}` are eigenvalue
   multisets of the Bring period Gram and of `M_S = 5I - J`, not Young
   diagrams — they just read as weakly-decreasing positive integer tuples.
   Five `alpha_EM` / Bring witnesses.
2. **structural-identity-on-a-tall-block.**
   `det(M_lambda).det(M_lambda') = +-1` holds in any carrier and quotes no
   physical number, but determinants are spectral invariants, so a
   spectral-vs-trace discriminator scores it as a reading
   (`beta-ew-delta-I-conjugate-pairing`). Also here: corpus-meta audit scans,
   refutations, and one **null** result
   (`reeb_rotation_pn_difference = 0.000e+00`) — the anti-fit discipline
   working, scored as though it were the defect.

## The methodological correction, which is the part worth carrying forward

An earlier draft of this probe **defaulted untriaged candidates to `SAFE`** and
reported "no new sector" while **ten** spectral-on-a-tall-block candidates —
in two sectors it had never looked at — were absorbed into that verdict. The
optimistic default *is* the failure mode. Trace-only and inert are mechanically
safe; everything else stays `UNTRIAGED` and **fails the run** until read by
hand.
