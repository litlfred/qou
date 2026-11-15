# The binding path's seminormal matrices are not a representation of H_n(q)

> ## Note, 2026-09-12 — the `uic(1,1)` values here are the GATED return
>
> Every `unified_iterative_correction` figure in this document
> (`−0.08955968305895067` at `k_exact = 4`, `−9.147736231020852` at the default)
> is the **gated** return. The Pass-2 sign gate was **dropped** on 2026-09-12
> (bean `qou-21oc`, PR #7253); the ungated values are `−0.412212192245027` and
> `−17.6908290020795`.
>
> **This document's conclusions are untouched.** Every comparison here is a
> *ratio or a difference between two runs of the same code path*, and both sides
> move identically under the gate drop — the `IDENTICAL` fixed-vs-main check, the
> `6.2e-16` agreement, and the `+180 %` column all hold verbatim. Only the
> absolute values are superseded, and they are kept as the record of what was
> measured on 2026-08-31.

**Measured 2026-08-31** on `origin/main`, `pyhecke_native 0.9.0`. Found while
executing the performance fixes of
[`2026-08-30-binding-compute-scaling-bottleneck.md`](2026-08-30-binding-compute-scaling-bottleneck.md)
(bean `qou-sv7h`). It supersedes that document's priority ordering entirely.

## The finding

`hecke_core_legacy._build_ysn_matrices` supplies the `rho_lambda(sigma_i)` that
`unified_iterative_correction` — and hence `binding_energy` — multiplies
together. Those matrices **satisfy the Hecke quadratic relation and violate the
braid relation**:

```
     partition  dim    impl    quadratic        BRAID    commuting
        (2, 1)    2  python     4.81e-17       0.7315          0.0   <-- NOT A REPRESENTATION
        (2, 1)    2    rust    1.203e-50    2.005e-50          0.0
        (3, 1)    3  python     4.81e-17       0.7315          0.0   <-- NOT A REPRESENTATION
        (2, 2)    2  python     4.81e-17       0.7315          0.0   <-- NOT A REPRESENTATION
        (3, 3)    5  python     4.81e-17       0.7315          0.0   <-- NOT A REPRESENTATION
        (4, 2)    9  python    8.694e-17       0.7315          0.0   <-- NOT A REPRESENTATION
     (2, 2, 2)    5  python     4.81e-17       0.7315          0.0   <-- NOT A REPRESENTATION
     (3, 2, 1)   16  python    8.694e-17       0.7315          0.0   <-- NOT A REPRESENTATION
```

**7 of 7 partitions, defect 0.7315 every time.** A constant defect across
different partitions and dimensions is one structural error, not accumulated
noise. Re-run it:
[`computations/audits/ysn_braid_relation_audit.py`](../../computations/audits/ysn_braid_relation_audit.py)
(exit 1 while the defect stands).

## Why the quadratic relation passing is not reassurance

`sigma^2 = h*sigma + I` constrains **each generator separately** — it fixes the
trace to `h` and the determinant to `-1`, i.e. the eigenvalues to `{q, -1/q}`.
It says nothing about how two generators sit **relative to each other**. The
braid relation is the one that does, and it is the defining relation of the
braid group: without it there is no representation of `B_n`, hence none of
`H_n(q)`, and a product of these matrices is not the image of a braid.

Visible at the smallest case, `lambda = (2,1)`, `n = 3`, `dim 2`. Both
implementations agree exactly on `sigma_1 = diag(q, -1/q)`, and **both** give
`sigma_2` the correct trace `h` and determinant `-1`. They differ only in the
off-diagonal:

```
python sigma_2 = [[-0.1039637101,  0.9835938505],
                  [ 0.9835938505,  0.3130240088]]

rust   sigma_2 = [[-0.4036277384,  0.8675840670],
                  [ 0.8675840670,  0.6126880371]]
```

Each is individually a valid Hecke generator. Only the Rust pair braids. Note
that the Rust diagonal entry `0.6126880371` is exactly
`z_D = q^3/(q^2+1)` — the canonical convention-D Markov parameter of the
2026-08-15 owner ruling — which is an independent check that the Rust family is
the intended object.

## What this invalidates

Every quantity `unified_iterative_correction` produces is a product of these
matrices, so the "Markov trace over the Wedderburn blocks" reading of that
accumulator does not hold as computed. `binding_energy` is
`unified_iterative_correction + sdp_cross_channel_contribution +
binding_from_frobenius_pairing`, and the first term carries the defect
directly.

**Blast radius, measured:** `33` files under `computations/` reference
`unified_iterative_correction` or `binding_energy`.
`_build_ysn_matrices` / `entry['ysn']` is also consumed by
`computations/sdp_cross_channel.py`, so the second term of `binding_energy` is
in scope too and has not yet been separately assessed.

**Scope, stated per the (a)/(b) discipline.** This is a **scope-(b) structural
exclusion** and it is entitled to be one: the braid relation is a *proved
invariant* of `H_n(q)`, and a family violating it is excluded from being a
representation by that invariant, not by a numerical near-miss. What is
*not* claimed here: that any particular downstream number is wrong by any
particular amount. Nothing has been re-run with the correct matrices yet — that
is the next step, and it needs the correct family wired in first.

## What is correct, and already in the repo

`pyhecke_native.seminormal_matrices_mpfr` satisfies all three relations at
`2e-50`. It is the Rust MPFR seminormal build, already exported, already
importable. On `lambda = (4,2)` it agrees with the Python family's `sigma_1` to
`3e-17` — the float64 floor — so the two are the *same intended object*, and the
Python one has both lost its digits and lost the braid relation.

## Also landed here, from `qou-sv7h`

Two changes from the performance analysis, both independently verified. They are
included because they were already measured; they do **not** address the defect
above.

1. **The unreachable sparse guard is fixed.** `if s['sparse'] and not
   exact_chain:` was never true (`exact_chain` is True for every physical chain
   — `c` is the Python int `1`, which is not a `float`), so the O(dim*nnz) path
   and its COO object accumulator were both dead and everything ran O(dim^3).
   Now `if s['sparse']:`; the inner dtype test already dispatches correctly.
   **Value-equality verified** against the pre-fix result at `k_exact = 4,5,6,7`
   — identical. **Speed: 71.9s -> 12.4s at k_exact = 8 (5.8x)**, which carries
   12 sparse partitions.

   At `k_exact = 8` the two differ by `2.28e-16` relative — **1 ulp of float64**,
   not a disagreement about the mathematics. Both paths are float64-limited
   because the YSN matrices are built in float64 (`a_rho = h/q_int(rho)` with
   float `h`; `off = math.sqrt(...)`), so exact agreement is unobtainable until
   the matrices themselves are exact. That is the same root cause as the finding
   above.

2. **A Rust kernel for the accumulator:**
   `pyhecke_native.lp_accumulator_step_traces_mpfr(shape, steps, q_str, dps)`.
   One PyO3 crossing per partition per atom; the O(dim*nnz) accumulation, the
   `m_max > 1e80` rescale and the per-step trace all stay in Rust at MPFR
   precision. Coefficients cross as decimal **strings**, so nothing narrows to
   f64 at the boundary. **Not yet wired into `hecke_core_legacy`** — wiring it
   is what changes the numbers, and that must wait until the representation
   question above is settled.

## Corrected priority

The 2026-08-30 document recommended: fix the guard, export the Rust matmul, then
fix precision. **That order is wrong.** Its own equality gate cannot be
satisfied while the matrices are float64, and the matrices are not merely
imprecise — they are not a representation. The order is:

1. **Establish which family is correct** and why the Python one deviates. The
   defect is constant at 0.7315, so it is one formula, most likely the
   off-diagonal.
2. **Wire the correct family in**, then re-run the binding numbers and report
   what moved. This is where published values may change.
3. Only then treat performance — with `lp_accumulator_step_traces_mpfr`, which
   is already correct and already built.

Regenerating `hadron-knot-table.witness.json` (`qou-i7ju`) should **not** proceed
until step 2. It would record numbers from a non-representation faster.

---

# SETTLED — the correct seminormal form, derived (qou-4m9u closed)

Solved symbolically rather than argued. Fix `sigma_1 = diag(q, -1/q)` (both
implementations agree on it exactly) and write `sigma_2 = [[a, b], [b, h-a]]`
— the trace is forced to `h` by the quadratic relation. Impose the **braid
relation together with `det = -1`** and solve for `(a, b)`.

**The system has exactly three solutions:**

| | `a` | `b` |
|---|---|---|
| degenerate | `q` | `0` |
| **irrep, +** | **`-1/(q(q²+1))`** | **`+√(q⁴+q²+1)/(q²+1)`** |
| **irrep, −** | **`-1/(q(q²+1))`** | **`-√(q⁴+q²+1)/(q²+1)`** |

The first is reducible (`sigma_2 = sigma_1`, `b = 0`) and is not the 2-dimensional
irrep. The other two are the same representation up to the sign of the
off-diagonal (a basis choice).

**Numerically at `q₀`:** `a = -0.4036277383`, `b = 0.8675840670`.

- **Rust matches exactly.** `seminormal_matrices_mpfr` returns precisely this.
- **Python matches none of the three.** Its `a = -0.1039637101 = -h/[2]_q`
  is not a solution of the system at all. The ratio is
  `a_correct / a_python = 1/(q(q-1)(q+1))`.

So the earlier hypothesis — that this might be a convention-C-vs-D difference
rather than a defect — is **REFUTED, and that matters**: a convention would give
*some* valid representation. Python's value satisfies neither branch, so there is
no convention under which it is a representation of `H_n(q)`. This is a defect in
`_build_ysn_matrices`, not a convention mismatch.

**Where it is.** `a_rho = h / q_int(rho)` — the diagonal entry is being computed
as `h` over a q-integer of the axial distance. The correct entry is
`-1/(q(q²+1))`, which is not of that shape. The companion `b` formula
(`bsq = a_rho*a_neg + 1`, i.e. `b² = a(h-a)+1`) is **correct** — it is exactly
the `det = -1` condition — so `b` is right *given* `a`, and `a` is the single
error. That is consistent with the measured defect being constant at `0.7315`
across every partition and dimension.

**The structural bonus.** The second diagonal entry is

```
h - a  =  q³/(q² + 1)  =  z_D
```

exactly — the canonical convention-D Markov parameter of the 2026-08-15 owner
ruling, arising here as a *forced consequence* of the braid relation rather than
as a convention choice. That is independent corroboration that convention D is
the one the algebra itself selects, and it is worth carrying back to the
convention-D excision arc (`qou-cds1`, `qou-t9r1`).

**What this still does not settle.** Nothing has been re-run with the correct
family. Which downstream numbers move, and by how much, is measured only by
wiring it in — `qou-sv7h` step 2, still open, still gating `qou-i7ju`.

---

# What it moves — measured (qou-sv7h step 2, first half)

The correct family swapped in and `unified_iterative_correction(1,1)` re-run.
**Measurement only — no witness was regenerated and no producer source was
changed.** The swap is a runtime substitution of `_build_ysn_matrices` by
`pyhecke_native.seminormal_matrices_mpfr`, returned dense at 50 dps.

| `k_exact` | current (braid-violating) | corrected (braid-exact) | relative change |
|---|---|---|---|
| 4 | `-0.03193786643543622` | `-0.08955968305895067` | **+180 %** |
| 5 | `-0.22859263051477`   | `-0.7335499391634977` | **+221 %** |
| 6 | `-0.7228588117317579` | `-1.36568481708788`   | **+89 %** |
| 7 | `-1.178155656129151`  | `-2.020000814981466`  | +71 % |

**This is a factor of 1.7–3.2, not a rounding correction.**

**`k = 4, 5, 6` are path-clean and are the rows to quote.** Measured: those
truncations carry **0 sparse partitions**, so both runs take the identical dense
code path and the only variable is the matrices. `k = 7` carries 2 sparse and
`k = 8` carries 12, so those rows mix a path difference with the matrix
difference and are weaker evidence — they are shown for continuity, not relied on.

## What this does NOT establish

Stated explicitly, because the number above is alarming enough to be
over-read:

- **This is one of three terms.** `binding_energy = unified_iterative_correction
  + sdp_cross_channel_contribution + binding_from_frobenius_pairing`. Only the
  first is measured here. The other two are unmeasured, and
  `sdp_cross_channel.py` consumes `_build_ysn_matrices` too, so it is very
  likely also affected — by an amount nobody has measured.
- **These are truncations, not the production value.** Production runs
  `k_exact = K_PARTITION_MAX = 11`. The trend across `k` is not monotone
  (+180, +221, +89, +71 %), so extrapolating to `k = 11` from these four points
  is not supported.
- **No published number has been re-derived.** No binding energy, no `B(K)`,
  no mass, no witness. The claim here is strictly about the accumulator.

## What it does establish

The defect is **consequential, not cosmetic**. A correction of this size in a
term feeding `binding_energy` means the corrected values must be computed and
published rather than assumed close, and it retires any hope that the braid
violation was a harmless normalisation. Whether the corrected numbers agree
better or worse with AME2020 is **unknown and unmeasured** — and that question,
not the speed, is what the remaining work is for.

---

# CORRECTION — the fix is right, and it moves the binding numbers by ~1e-14 (2026-09-05)

The defect above is real and is now fixed in code (`qou-4m9u` closed into
`_build_ysn_matrices`; braid defect `0.7315 -> 7.5e-17`,
[`ysn_braid_relation_audit.py`](../../computations/audits/ysn_braid_relation_audit.py)
exit 0). **But the "71-221 %" table above does not survive re-measurement, and
the reason is structural rather than arithmetic: every consumer on the binding
path takes a TRACE, and the trace is provably blind to this defect.**

## What was measured

Two runs in one process, so nothing can be contaminated by transcription:
`origin/main`'s `_build_ysn_matrices` is extracted with `git show` and `exec`'d
over the module dict, varying **only the `a_rho` formula** — same return type,
same float64 precision, same code path. A control confirms the swap took
effect (`sigma_2[0][0]`: `-0.403627738351` fixed vs `-0.103963710052` main,
exactly the two families of §"The finding").

**1. With `pyhecke_native` present — byte-identical, because the Python family
is never reached.**

```
unified_iterative_correction(1,1)   fixed: -9.147736231020852
                                    main:  -9.147736231020852     IDENTICAL
_lp_kernel_steps: 193 calls, 193 served
```

`_lp_kernel_steps(partition, chains)` takes the **partition shape**, not
`entry['ysn']` — Rust rebuilds its own seminormal family — and both consumers
early-return on it (`hecke_core_legacy.py:1538`, `:1773`). So in an environment
with the native extension the Python matrices are built (193 builds, 36.6 s) and
then discarded.

**2. With the kernel forced off — agreement at the float64 floor.** This is the
configuration a bare container actually runs, since `pyhecke-native` is not on
PyPI and cannot be `pip install`ed.

| | fixed | main | rel |
|---|---|---|---|
| `uic(1,1)` k_exact=4 | `-0.0895596830589507` | `-0.08955968305895065` | `6.2e-16` |
| `uic(1,1)` k_exact=5 | `-0.7335499391634968` | `-0.7335499391634722` | `3.3e-14` |
| `uic(1,1)` k_exact=6 | `-1.3656848170878788` | `-1.3656848170878515` | `2.0e-14` |
| `atom_character_raw(1,1)` (2,1) | `0.22198499898729818` | `0.22198499898729923` | `4.7e-15` |
| `atom_character_raw(1,1)` (3,1) | `1.569165548376476` | `1.5691655483764773` | `8.3e-16` |
| `atom_character_raw(1,1)` (2,2) | `1.6538107571632679` | `1.6538107571632668` | `6.7e-16` |
| `atom_character_raw(1,1)` (3,2,1) | `-0.019884149989698785` | `-0.019884149989699906` | `5.6e-14` |

The chains are not degenerate — every generator `0..n_gens-1` appears, over 11
and 12 factors per step.

## Why: the trace cannot see this defect

For any `A`, `B` with `A² = hA + I`, `B² = hB + I` and `Tr A = Tr B`:

```
Tr(ABA) = Tr(A²B) = h·Tr(AB) + Tr(B)
Tr(BAB) = Tr(B²A) = h·Tr(AB) + Tr(A)
```

so `Tr(ABA) − Tr(BAB) = Tr(B) − Tr(A) = 0`. **The trace of the braid relation is
a consequence of the quadratic relation alone, in any dimension.** Measured on
`lambda = (2,1)` in float64 through the production path: main's family has matrix
braid defect `0.7315` and trace braid defect **exactly `0.000e+00`**; the fixed
family gives `5.6e-17`.

Re-run it at MPFR, off the production path and free of the float64 caveat:
[`computations/audits/ysn_trace_blindness_probe.py`](../../computations/audits/ysn_trace_blindness_probe.py)
(9/9, exit 0). At `dps = 50` the legacy family's **matrix** braid defect is
`0.731514` while its **trace** braid defect is `6.68e-52` — i.e. zero to the
precision carried, not merely below a float64 floor. The probe cross-checks
itself against the two values this document recorded independently (`a =
-0.1039637101`, defect `0.7315`), which is what caught its own first version:
written with `rho = +2` it measured `a = +0.1039` and defect `1.0269`, a family
the code never built. The axial distance is negative and `[-2]_q = -[2]_q`.

`unified_iterative_correction` accumulates `ln|Tr M_λ|` and
`atom_character_raw` returns `Tr(M_λ(W_atom))`. Both are trace consumers, so
neither can distinguish the two families — which is also why this defect sat in
the corpus undetected: the audit that found it had to compare **matrices**, and
every character-level check the corpus already ran was structurally incapable of
firing.

**Scope, per the (a)/(b) discipline.** The proof above is scope-(b) for word
length 3 — a proved invariant. The length-11/12 agreement is scope-(a): measured
at the float64 floor, and this run does **not** separate "equal in exact
arithmetic" from "equal to within float64 rounding". It cannot: the builder is
float64 by construction (§"Also landed here" item 1), so there is no higher
precision to re-run at.

## What retires, and what stands

**Retired: the 71-221 % table** of §"What it moves — measured". Its *corrected*
column is reproduced exactly by today's `main` (`-0.08955968305895065` vs its
`-0.08955968305895067` at k=4, and likewise at k=5,6) — i.e. `main` **already**
produces what that table called the corrected value, with the braid-violating
matrices still in place. Its *current* column (`-0.0319`, `-0.2286`, `-0.7229`)
is not reproducible on any tree measured here. That table was written at
`8a3c748ae90` (2026-08-31); the only later commit in the window that touches the
accumulation is `d943f2acfac` (the COO object fallback ported to
`atom_character_raw`, same day) — **named as the candidate, not asserted as the
cause**, since that table also reports k=4,5,6 as carrying 0 sparse partitions,
which would make the COO path irrelevant to exactly those rows.

**Stands: everything about the mathematics.** The Python family satisfies no
branch of the braid+determinant system (§SETTLED), so it is not a representation
under any convention; the derived `a = -1/(q(q²+1))` is correct and is now what
the code computes; and `h − a = q³/(q²+1) = z_D` remains independent
corroboration of convention D.

**Stands: the fix is worth landing.** Not for the binding numbers — those move
by `1e-14` — but because the detector is red on `main`, because the object is
wrong, and because any consumer that uses the matrices rather than their traces
would be wrong.

**The one such consumer is dead code, measured.** `q_sweep_sdp_atom` in
[`sdp_cross_channel.py`](../../computations/sdp_cross_channel.py) is the only
importer of `_build_ysn_matrices` outside `hecke_core_legacy` itself, and it
uses the matrices rather than their traces — so it is the single place where
this defect could have moved a number. It is **defined at line 394 and called
nowhere**: a repo-wide grep returns its own `def`, and otherwise only the three
places this session wrote *about* it (two beans and this paragraph). No witness
references it. So no recorded number in the corpus came from the braid-violating
family through this path either, and the fix makes it correct before anyone
calls it. That is a grep, not a run — it establishes there is no caller, not
that the function would be right if there were.

**`qou-i7ju` is unblocked.** `hadron_knot_table.py` reaches the matrices only
through `binding_energy`, which is fully kernel-served. Regenerating
`hadron-knot-table.witness.json` was gated on step 2 of the corrected priority;
step 2 is now measured and the answer is "nothing moves".

**🛑 "Untouched, deliberately" was the wrong frame, and it is retracted
(2026-09-05).** This paragraph read: *"The builder is still float64
(`math.sqrt`, `1.0` literals, no `mp.dps`). Representation first, precision
third — that is this document's own ordering, and the precision half is
`qou-sv7h` step 3."* That presents a live NO-FLOAT64 violation as a deliberate
scope choice. The corpus has no "correct-but-imprecise" state for a
`computations/` producer; float64 there is a defect, and an ordering between
two defects is not a licence to leave the second one standing.

**And the float64 was worse than the sentence describes.** It named
`math.sqrt` and the literals. Measured: `Q`, `Q_INV` and `HA` imported from
`q_parameter` are Python **floats**, so the family was float64 from its
*inputs*; `mp.dps` is **15** in a bare import of `hecke_core_legacy`, exactly
float64's significand, so carrying `mpf` without raising it would have bought
nothing; and **124 of 193** ysn entries (64 %, max dim 2310) were `scipy`
`csr_matrix`, which is float64 by construction and whose kernels reject
`dtype=object`. Three defects, one named.

**Consequence for the section above.** The `1e-14` figure in *"What it
moves — measured"* was obtained at `k_exact = 4, 5, 6`. Those truncations
carry **zero** sparse partitions — the threshold is `dim >= 32`, first reached
at `k = 7` — so that sample never touched the 124 entries where float64 σ
values met `mpf` coefficients. It measured the dense path only, and its scope
should be read as such.

**Now fixed.** The builder computes in `mpf` inside
`mp.workdps(_precision.COMPUTE_DPS)`, and the sparse carrier is `_ExactCOO`
rather than `csr_matrix`. Against the closed form this document derived
symbolically (`-1/(q(q²+1))` at `ρ = -2`): **9.5e-52**, was ~1e-16. The audit's
Python rows moved from `1.49e-16 / 1.52e-16` into the Rust MPFR reference's own
precision class, `4.0e-50 / 3.2e-50` against `1.2e-50 / 2.0e-50`.
