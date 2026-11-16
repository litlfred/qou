---
# qou-4qno
title: 'Staircase EW-residual: every testable case is in the TL kernel — rho_k has k rows, so only k=2 is physical at N=2, and the block calls that case untestable'
status: in-progress
pr: 8193
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-01T07:53:25Z
updated_at: 2026-11-16T20:41:00Z
parent: qou-10v9
---

Found while auditing the Standard-Model work against the full tower (owner request, 2026-09-01). Probe: `computations/qbeta/qbeta_staircase_ew_lives_in_the_tl_kernel_probe.py` (4/4).

## The observation

`folio/quantum-observable-universe/mass-theory/staircase-ew-residual.md`
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

- [x] Decide with the owner whether the block should carry a row-cap caveat.
      **Owner said do all four options, 2026-09-02.** Landed below.
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


---

## Resolved 2026-09-02 — all four options, plus the owner's steer

Owner directive: "do all. formalization is important". Plus a steer that
changed the order of work and nearly changed the answer, recorded next.

### The steer, and why it went first

> "there may be more than one observable that's really in play. some may be at
> n=2 some maybe higher, but still need to take trace. some observables are not
> really direct observables of n=2, but 'computable' observables -- operators
> acting at higher orders, observable at order 0 only by subtraction. A
> higher-tower operator projected down is not obviously a convex combination of
> the two crossings, which is precisely the property needed."

If computable observables escaped the row cap, the caveat would have been wrong
on all four surfaces at once. So it was probed before anything was written.
Probe: `computations/qbeta/qbeta_computable_observables_vs_row_cap_probe.py`
(8/8). **The question splits, and the halves go opposite ways.**

**The owner is right about the tower, and it is not speculative — it is the
Hecke quadratic relation.** In the two-crossing basis `x = a.sigma +
b.sigma^-1`, with `sigma^-1 = sigma - h`, an element `c_1.1 + c_sigma.sigma` has
`b = -c_1/h`. So `sigma^2 = h.sigma + 1` gives `b = -1/h < 0`: **two crossings
compose to something outside the segment between the two crossings.** Measured
for `sigma^k`, k = 2..8 — none is in the cone. The convex hull of the crossings
is not closed under multiplication.

And the corpus's own object shows it. `atom_braid_word_3A` returns letters
`(c, d, g)` meaning `c.sigma_g + d.1`, and **every one of the deuteron's 23
letters is a convex combination of the two crossings** (11 pure `sigma`, 7 pure
`sigma^-1`, 5 averaged at `a = b = 1/2`) — so the atom is a convex combination
of 2^5 signed braid words. Its order-0 projection is not:

| operator | a | b | in cone? |
|---|---|---|---|
| `E_2(beta_atom)` | +1.71000 | −1.17070 | no |
| `E_2(beta_free)` | +3.36463 | −2.30348 | no |
| `E_2(Delta_bind)` | **−1.65462** | +1.13278 | **no** |

(`E_2` = the Markov-trace-orthogonal projection onto `H_2 = span{1, sigma_1}`,
fixed by `tr_M(E(x).y) = tr_M(x.y)` for `y` in `{1, sigma_1}`.)

**But subtraction does not escape the row cap, by linearity.** A computable
observable is a *difference of Markov traces*:
`tr_M(Delta_bind) = tr_M(atom) - tr_M(free)` — verified to a residual of
`2.3e-41` — and `tr_M = sum_lambda y_lambda chi_lambda` with `y_lambda = 0` for
`l(lambda) > 2`. A linear combination of functionals blind to the tall blocks is
blind to the tall blocks. Being computable rather than directly observed buys
**nothing** against the cap.

**What survives, and it is not a rescue.** Reading a *spectrum* instead of a
trace does see the tall blocks. Measured: `rho_(3,2,1)(Delta_bind)` has max
entry `5.12` — a genuinely nonzero 16x16 operator — while `|y_(3,2,1)| =
1.1e-17`, so its contribution to `tr_M(Delta_bind)` is exactly zero. That is
the precise sense in which the tower carries what the trace cannot see, and the
precise sense in which reading it is not physical.

**So the caveat is unconditional, but the reason is sharper than "unverified":**
every route from a `>2`-row block to a physical number is either a **trace**
(which the row cap zeroes) or a **spectrum** (which has no states). Subtraction
opens no third.

### G — the general row cap, formalized

`folio/quantum-observable-universe/lean/QOU/Hecke/RowCap.lean`, registered in
`QOU.lean`. `QOU.Eightfold.RowCapObstruction` proved the cap for `V^(x)3` alone
(`weylDimAlt N = N.choose 3`); every other appeal to it — `(3,2,1)` at n = 6,
`(2,2,1,1)`, the whole `l(lambda) > 2` sector — was corpus prose plus a
measurement. This proves it for every partition, in one pigeonhole step:
`dim V_lambda = #SSYT(lambda, N)`, a column of `l(lambda)` boxes is a strictly
monotone `Fin (l lambda) -> Fin N`, and an injection into a smaller finite type
does not exist. The asymmetry is the content — rows increase *weakly* so give no
bound; columns increase *strictly*.

Carries `staircase_three_isEmpty`, `staircase_four_isEmpty`,
`staircase_two_nonempty` (the only physical staircase, and the untestable one),
and `choose_eq_zero_iff_isEmpty` tying the general cap back to the n = 3
arithmetic so the two cannot drift.

**COMPILED AND SORRY-FREE (corrected 2026-09-02, same session).** This section first read
**"NOT COMPILED LOCALLY, and not reported as green"** — true when written and
false within the hour. The retraction is recorded rather than quietly
overwritten, because why it was false is the useful part.

`lake build QOU.Hecke.RowCap` from the **repo root**: *Build completed
successfully (3087 jobs)*, exit 0, olean produced. `#print axioms` on all ten
theorems: `[propext, Classical.choice, Quot.sound]`, and `alt_channel_empty_iff`
needs only `[propext]`. No `sorryAx`.

**What made it look impossible, and the two traps in it.** Mathlib's olean cache
host `lakecache.blob.core.windows.net` *is* denied by organization policy here —
`lake exe cache get` failed 476 times for 476 attempts. But this repo does not
use that host: `scripts/lean-cache-restore.sh` pulls a chunked tarball from the
`lake-cache/qou-<toolchain-slug>` orphan branch over **GitHub**, which is
reachable. 2.4 GB in `lake-oleans.tgz.part*` blobs, concatenated and extracted,
gave 3470 Mathlib oleans including every module this file imports.

- **TRAP — the restore script no-ops when the cache is present but useless.** It
  skips at `>= 2000` mathlib oleans, and there were **6990** — all
  `Mathlib/Tactic/**` and `Mathlib/Lean/**` infrastructure, with `Data`,
  `Order` and `Logic` absent, so nothing mathematical would compile. The
  threshold counts files, not coverage. `lean-axiom-guard.yml` gates on the same
  `-lt 2000` test and would neutral-skip on a warm-looking cold cache the same
  way. Check for a module you actually import, not a count.
- **TRAP — build from the repo root, not from `content/…/lean/`.** The root
  `lakefile.toml` says so in its own header ("the preferred build entry point
  for CI and agents"), and the two trees carry **separate** `.lake/packages/`.
  Building in the sub-project recompiled Aesop from source while the restored
  cache sat unused at the root.

### B + C + D — the surfaces

| surface | change |
|---|---|
| `mass-theory/staircase-ew-residual.md` | new **Carrier** section: `N_min(rho_k) = k`, only k = 2 physical and it is the untestable case; trace-or-spectrum dichotomy; subtraction does not open a third. First bullet now says the exponent is selected rather than derived. |
| `mass-theory/staircase-corner-hook-proof.md` | "**arithmetic anchor**" → "makes the exponent *available*"; "uses *exactly* this corner hook" → "matches"; adds "availability is not derivation", the enumerated sweep, that the k = 4 prediction was not testable, and the row cap. The identity `h_corner = 2k-1` stands untouched. |
| `appendix-standard-model/sm-params-gauge-couplings.md` | adds the row-cap ground beside the anti-fit one, and why it is stronger: **deriving the exponent would not close the gap.** |
| `docs/sm-eightfold-derivation-cheat-sheet.md` | same, in the G6 guardrail. |
| `nuclear-interactions/weinberg-angle-categorical.md` | records that its three proposed repairs all act *inside* the carrier, which is where a repair must act, and that a construction reaching CODATA by reading a tall block's spectrum is not a competing evaluation of the same quantity. |

The contradiction the sweep found is gone: the guard said availability after a
proximity search is not derivation while the proof block called the same hook
"the arithmetic anchor". Both now say the same thing.

### Gates

- content validation: **✓ Valid**, 9 issues, all pre-existing and none in a
  touched file.
- `probe-float64-guard --diff`: clean on both new probes.
- `witness_shape_guard`: clean.
- **Lean: `lake build` green from the repo root** (3087 jobs, exit 0) and all
  ten theorems sorry-free under `#print axioms`. The first write-up of this
  bean said the gate could not run; see the correction above.

## Round 53 Progress (PR #8193)
- [x] Added `staircaseList_length`, `staircasePartition_rows`, `staircase_in_tl_kernel_iff_three_le`, `staircase_physical_at_su2_iff_le_two`, `staircase_unique_physical_ge_two`, and `staircaseStrands_small_values` to `folio/quantum-observable-universe/lean/QOU/Hecke/Staircase.lean` (`0 sorry`, `0` vacuity hits).
- [x] Verified staircase row counts and `N = 2` TL-kernel threshold in `computations/probes/route89_staircase_wpdb_stargram_probe.py` (`computations/probes/route89-staircase-wpdb-stargram.witness.json`).
- [ ] Await CI verification and Merge Manager merge of PR #8193 (`9d88b10b75877699bcfe0134c2f9a3d95a32edf4`).
