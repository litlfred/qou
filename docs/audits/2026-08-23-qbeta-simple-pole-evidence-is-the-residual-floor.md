# The Q_β simple-pole evidence is the residual-floor identity

**Date:** 2026-08-23
**Scope:** the PR #1727 "simple pole at `u_substrate`, residue `A ≈ 1.804e-15 ≈ 1 ppQ`"
verdict, and the ~8 durable artifacts that still carry it.
**Status:** the *evidence* is withdrawn. The *pole* is not refuted — see §4.

## 1. What happened

`qou-8ofm` and `qou-frch` (both 2026-08-10) established that the SDP `c_k`
extractor emits the model's **accuracy floor as data**:

> A contributing rung drops the residual by ~`1/u` = 117×. After the stall it
> drops by 1×: that is the model's ACCURACY FLOOR, not a rung contribution.
> Dividing a fixed floor by an ever-smaller `u^k` is exactly what manufactures
> `c_k ~ floor/u^k`.
> — `e5885ebc0f`

`qou-frch` sharpened it further: `R(q0)` is a **single scalar**, so **at most
one** `c_k` is determinable by this procedure at all.

Both commits fixed the producer. **Neither swept the consumers.** The
retraction doc itself notes *"Prose caveats do not stop downstream
consumption"* — and then the downstream was not touched.

## 2. Why this specifically invalidates the simple-pole evidence

PR #1727 read the verdict off three signatures, all at **k = 8, 9, 10** — which
`qou-frch` places deep inside the stalled range. In that range
`c_k := (R_k − 1)/u^k` with `R_k − 1` pinned at a constant floor `f`, so:

| signature cited as evidence | what it actually is |
|---|---|
| `c_k·u^k → const` (flat asymptote, 0.02 % spread) | `c_k·u^k = f` — **an identity** |
| ratio test `c_{k+1}/c_k → 1/u_subst` | `(f/u^{k+1})/(f/u^k) = 1/u` — **an identity** |
| branch-fit `β = 0.999` (β = 1 *is* the simple-pole case) | a pure geometric sequence has `β = 1` — **an identity** |
| residue `A = L·u_subst ≈ 1.804e-15` | `f·u_subst` — **a rescaled floor** |

The three "independent" confirmations are one arithmetic fact stated three ways.

### Measured, on the current committed extraction

[`qbeta_singularity_cross_anchor_probe.py`](../../computations/qbeta/qbeta_singularity_cross_anchor_probe.py)
now runs this as a diagnostic against the extractor's **own** emitted quotients
(`c_k_unresolved_raw_quotient`), not a re-derivation of them:

```
  k                floor f    |c_k u^k|/f - 1    (c_k+1/c_k)*u - 1
  2  0.0006743793302680503        2.97059e-22             0.107506
  4  0.0006006447141187657        4.76974e-22           9.92184e-6
  7  0.0006006386996532087         8.8859e-22          4.32819e-11
  8  0.0006006386996272119        3.81877e-21          1.04429e-13
  9  0.0006006386996272747        2.22186e-21          2.36334e-15
 10  0.0006006386996272732        4.29644e-21
```

`|c_k·u^k|` equals the recorded floor to **1e-21**, and the ratio test returns
`1/u = 117.40900102154` to **2.4e-15** by k = 9. The "0.02 % spread" that
passed the 1 % tier was the floor's own stability.

### The "suspicious but unexplained" 1 ppQ coincidence dissolves

The 2026-06-02 audit flagged `A ≈ 1.804e-15 ≈ 1 ppQ` as *"the precision-target
scale, suspicious but unexplained"*. It is explained: `A = f·u_subst`, and `f`
**is** the computation's numerical accuracy floor, which sits near the precision
target by construction. This also explains why the 38-candidate categorical
search for `A` across 6 hypothesis families
(`qbeta_residue_categorical_id_probe.py`) came back uniformly negative — it was
searching for a closed form of a numerical artifact.

## 3. Why the floor is 6.0e-4 today — already answered on `main`

The extraction now resolves **nothing**: `last_resolved_rung: null`,
`n_unresolved: 9`, floor 6.0e-4 against the 7.4e-5 that `qou-frch` instrumented.
I filed that as an open question (`qou-1g6q`) before finding it **already
answered in the producer's own header**, added 2026-08-21 (`qou-m9xp`) — a
corpus-grep miss on my part: I searched the witness history and the commit
messages, not the producer source.

The answer is neither "anchor effect" nor "regeneration defect". It is the
**convention C → D substitution**:

```
-    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))     # convention C
+    z = q**3 / (q**2 + 1)                     # convention D
```

Verified there at 60 dps: muon + C reproduces the committed 2026-06-22 value
byte for byte; muon + D and proton + D both land 6.0e-4 away. The μ–p pin shift
contributes **3.0e-8** — four orders less. I reached the same bound
independently before finding the banner (`Q_A` moves 3.0e-8 and `ℏ_q²` moves
−2.1e-7 across the anchors, against a 6.0e-4 output move), so the two routes
agree.

AGENTS.md forbids that substitution in terms — `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
(sorry-free) makes the C-frame ladder and the mass channel's three-row forcing
mutually exclusive, so **a z-swap is not a re-derivation**. So the all-null
state is not a degradation to explain: it is a C-frame ladder correctly failing
to resolve anything at a D parameter. Neither `602,433 ppb` (D-substituted) nor
`1248 ppb` (coherent C-frame, and C is excised) is currently a valid statement
about Q_β. Re-deriving under D is tranche S1 of `qou-cds1` — research, not
repair.

**This sharpens §2 rather than competing with it.** The floor identity is
arithmetic and holds in any frame; only the floor's *magnitude* is frame-
dependent. PR #1727's `f = 2.118e-13` was the muon + C floor, and the
`6.0e-4` measured above is the D-substituted one. The simple-pole evidence was
therefore **also** C-frame — one more reason it cannot be quoted as it stands.

## 4. Scope — what is NOT claimed

Per AGENTS.md §"Before declaring 'refuted'":

- **(b) structural exclusion, and it applies only to the inference.** The
  signature cannot discriminate a simple pole from a residual floor, because a
  floor reproduces all three signatures *identically*. The invariant is the
  arithmetic identity above; it is exact, not statistical.
- **(a) scope-limited, on everything else.** The **existence** of a singularity
  at `u_substrate` is **not** refuted and has independent support: PR #1713's
  radius-of-convergence argument, and PR #2454's algebraic `Q_A(silver) = 0`.
  What is withdrawn is that *this* evidence establishes the pole's **type**
  (simple) or its **residue** (`1.804e-15`). Those are **unanswered**, not
  false.
- **The Lean is unaffected.** `RadiusOfConvergenceGateClass` is a §3b-cond
  conditional class and `radius_of_convergence_gate_reject` proves an
  implication. Neither asserts the premise. Only the **docstring's empirical
  justification** ("PR #1727 established this ... 2.118e-13") is affected.

## 5. Durable artifacts still carrying the withdrawn evidence

Not swept in this pass — the rewrite is opinionated and spans a coordination
ledger, so it is filed rather than done unilaterally.

| artifact | what it carries |
|---|---|
| `content/.../mass-theory/q-beta-radius-of-convergence-gate.lean:11` | docstring: "PR #1727 established ... `c_k·u_subst^k → 2.118e-13` for k = 8, 9, 10 (0.02 % spread)" |
| `docs/coordination/1ppq-qbeta.md` | ledger rows for 2026-06-02, 2026-06-03, 2026-06-22; the dead-ends table; the open-target table ("identify residue `A ≈ 1.804e-15` categorically") |
| `docs/audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md` | the originating verdict, incl. "STRUCTURAL FACT" |
| `docs/audits/2026-06-04-residue-a-unblock-kernel-scope.md` | `A` as the residue of a simple pole |
| `docs/audits/2026-06-04-qbeta-residue-a-precision-ceiling-{plan,verdict}.md` | the per-k tail table and `A := u_subst·L` |
| `docs/audits/2026-06-04-qbeta-residue-a-followup-{plan,verdict}.md` | `A` as a live categorical-ID target |
| `docs/audits/2026-06-04-qbeta-mixed-chains-plan.md` | `A` "anchor-independent" |
| `docs/audits/2026-06-22-qbeta-two-pole-ladder-decomposition.md` | tail amplitude `L`, residue `A` |

## 6. What this pass did

- Fixed the crashing consumer. `qbeta_singularity_cross_anchor_probe.py` was
  raising `ValueError: could not convert string to float: 'none'` on the honest
  nulls. It now reports the premise's status, runs the floor-identity
  diagnostic, and returns `PREMISE_WITHDRAWN`.
- **Did not substitute `c_k_unresolved_raw_quotient`.** Those *are* the floor
  quotients; using them would re-derive the artifact under a different name.
- Part (b) of the probe (comparing `u_subst` across anchors) is independent of
  `c_k` and is unchanged; it still reports 211.6 ppb.

## References

- `e5885ebc0f` — `fix(qou-8ofm): SDP c_k extractor emitted the residual FLOOR as data`
- `6e586861b7` — `fix(qou-frch): only c_2 and c_3 are supported; my own guard was off by one`
- `6d261854d4` — `fix(qou-jvav): regenerate the q-pin consumers — drift 92 -> 69`
- [`docs/audits/2026-08-10-ck-slope-and-two-extractions.md`](2026-08-10-ck-slope-and-two-extractions.md)
- [`docs/audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`](2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md)
