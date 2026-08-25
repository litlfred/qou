# Q_β and 1ppq-L2 — what the last week's landings actually buy (2026-08-08)

**Scope.** The question asked: *of everything that landed in the last week,
what can be used to close 1ppq-L2, specifically around Q_β — is there
potential to improve compute by closing a derivation gap?*

This is an assessment, not a closure. Every claim carries an epistemic tier.
One compute bug is fixed (mechanism, not number); nothing is wired; no fit.

## 0. Answer up front

| question | answer |
|---|---|
| Did anything land that closes Q_β's derivation gap? | **No.** |
| Did anything land that *changes where the gap is*? | **Yes** — two sorry-free modules newly localize it, and one owner directive newly bounds it. |
| Is there a compute improvement available now? | **Yes, one, and it is a mechanism fix, not an accuracy gain** (§2). |
| Is the "measurement-limited ⇒ not framework-closable" framing correct? | **Over-scoped as written** (§4). It is right for the *cal-anchored extraction* route, wrong as a blanket statement about Q_β's prediction error. |

## 1. The Q_β number, and where its error lives

Committed L2 dashboard (`per-observable-100x-status.witness.json`,
computedAt 2026-07-18):

```
Q_β   pred 0.782334386518 MeV   err 1248 ppb
      σ_exp 779.7 ppb   100× target 7.797 ppb   miss 160.1×
```

The prediction is the **N=2 rung** — `c_2 = −1`, the only Taylor-exact,
Lean-proved, q₀-independent coefficient
(`qou:QOU.BraidKnot.q_beta_categorical_precision_ladder` + Kashiwara
`N2_factor`). The `qbeta-ck-cache` witness records `c_3` as
`tier: "cal-anchored"` with its own explicit self-indictment:

> *"value extracted from CAL-3 Q_codata at this q₀; reusable calibrated
> constant, NOT a prediction — must not count toward any 100×/1× dashboard
> pass"*

So the entire 1248 ppb residual **is** the c₃-and-beyond truncation. That is
the derivation gap, and it is unchanged this week.

Note the trio identity holds: `m_n = m_p + Q_β + m_e`, `Δ_pn = Q_β + m_e`.
Q_β drives **3 of the 5** L2 misses. It remains the highest-leverage single
observable.

## 2. The one real compute finding — the tier auto-promotion was dead code

`per_observable_100x_status.py::load_witness` resolved names **flat only**:

```python
p = COMPUTE_DIR / name          # computations/<name>
if not p.exists(): return {}
```

But the cache lives at `computations/qbeta/qbeta-ck-cache.witness.json`. So
`load_witness("qbeta-ck-cache.witness.json")` returned `{}` on every run and
the Q_β row went down the **legacy fallback** branch — which is why the
committed witness carries the source string:

```
"Q_N2 (fallback; qbeta-ck-cache witness not present)"
```

The witness *is* present. The message is wrong, and more importantly the
**tier-keyed auto-promotion mechanism was inert**. The producer's own comment
promises:

> *"Keying off `tier` means a future agent who proves a higher c_k
> Taylor-exact in Lean promotes it (tier='derived') and the dashboard
> auto-picks it up."*

It would not have. An agent who closed c₃ in Lean and set `tier='derived'`
would have seen the dashboard silently keep reporting Q_N2 — a false
negative on the exact event this whole ladder exists to detect.

**Fixed** in this branch: `load_witness` now falls back to a one-level scan of
`computations/` subdirectories.

**Numerically a no-op today**, and this is verified rather than assumed — both
branches yield the identical value because k=2 is the only `derived` rung:

```
fallback Q_N2    = 0.7823343865181718847573065835778360…
cache k=2 Q_pred = 0.782334386518171884757306583578
deepest DERIVED rung after fix: k = 2   (k=3 correctly rejected: cal-anchored)
```

*Tier: symbolic-exact (file resolution + string comparison).* The
anti-circularity discipline is preserved by the fix, not weakened: the
`cal-anchored` c₃ is still refused.

## 3. NEW this week — the q₀-anchor layer is now a live L2 term for Q_β

The 2026-08-07 owner directive (AGENTS.md §q₀-anchor) makes the
**experimental/proton** pin the default for all production compute. The
`qbeta-ck-cache` witness is stamped `q0Anchor: "muon"`,
`q0Value: 1.10997859555733471989…`, while the L2 producer reads
`q_parameter.Q_50_DIGIT_STR`. That is a layer boundary crossed inside one
dashboard row — the straddling hazard the directive names.

Measured sensitivity (mpmath, 60 dps, this session):

```
q rel diff (proton − muon)/muon  =  −11.537 ppb
dlnQ_β/dlnq                      =  −2.5968
⇒ anchor swing on Q_β            =   29.96 ppb
```

*Tier: symbolic-exact (closed-form log-derivative of the Q_β base form).*

Read this carefully, because it cuts both ways:

- It is **2.4 % of the current 1248 ppb residual** — so it is *not* the
  reason Q_β misses today, and re-pinning is **not** a lever that closes L2.
- It is **3.8× the entire 100× target (7.797 ppb)** — so once c₃ is derived,
  **the anchor choice alone would still overshoot L2 by ~4×.** Any future
  claim that Q_β meets L2 must state its pin and be internally consistent
  about it.

That second point is new and is the most actionable durable consequence of
this week's directive for the Q_β front.

## 4. Critical assessment — "measurement-limited" is over-scoped as written

`docs/precision-goals.md` and the 2026-08-02 lever map state that Q_β / m_n /
Δ_pn are *"measurement-limited by a next-gen neutron Q_β measurement"* and
that *"the 5 L2 mass/Q_β misses are no longer framework-closable."*

The supporting Lean (`QOU/QBeta/MeasurementLimitedFloor.lean`) is sorry-free
but proves **arithmetic, not physics** — and says so honestly in its own
docstring (*"Nothing here claims the premise"*):

```lean
theorem miss_factor_ge_100 (σ err : ℝ) (hσ : 0 < σ) (h : σ ≤ err) : …
theorem qbeta_dashboard_err_ge_sigma : (7797/10 : ℝ) ≤ 1248
```

That is: *given* the prediction is currently worse than one experimental σ,
the 100× miss follows. It is a re-description of the present dashboard state,
not a bound on what framework compute can achieve.

Two distinct claims are being conflated:

1. **Verification is measurement-limited.** You cannot *confirm* accuracy
   below σ_exp = 779.7 ppb without a better measurement. **True.**
2. **The prediction error cannot be improved by framework compute.**
   **Not established.** The 1248 ppb is the c₃ truncation — a framework
   quantity. Under the *proton* pin, q₀'s own measurement uncertainty
   contributes ≈ 0.06 ppb × 2.60 ≈ **0.16 ppb** to Q_β, four orders below the
   residual. Almost none of the 1248 ppb is propagated measurement error.

Note also that a *better* neutron measurement **tightens σ_exp and makes the
L2 target harder**, since `target = σ_exp/100`. The measurement-limitation is
therefore real for the **cal-anchored extraction** route (extracting c₃ *from*
a measured Q_β is bounded by that measurement — `dq*/dQ_β ≈ −0.54`, correctly
recorded), but it does **not** transfer to a **categorical derivation** of c₃.

Per AGENTS.md §"Before declaring refuted", this should read as a
**scope-(a)** statement — *"the cal-anchored extraction route is
measurement-limited; a derived-c₃ route is not excluded"* — not the
scope-(b) blanket *"no longer framework-closable"*. No proved invariant
forbids a derived c₃. Recommend re-scoping the wording in
`docs/precision-goals.md` and the lever map; the numbers in both stand.

## 5. What DID land that bears on deriving c₃ — one genuine structural lead

The surviving c₃ route, after the real-q₀ exclusion chain (#4282/#4288/#4293,
scope-(b) for **strictly real q₀**), is a **fibre-level complex phase**:
`2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md` names it as the
q-Pochhammer denominator pole `x = q^{−k}` combined with the cusp phase
`ω = e^{iπ/3}`. The obstruction that closed the real routes is **bar-parity**:
a real, trace-built (bar-even) Gram resolvent cannot carry the bar-**odd** S.

Two sorry-free modules landed this week that speak directly to that
obstruction:

| module | content |
|---|---|
| `QOU/Information/CocenterTraceFactor.lean` | the trace factors through the cocenter `HH₀ = A/[A,A]`; any separator of a commutator is a **non-trace** |
| `QOU/Information/OuterDerivationResidue.lean` | every **inner** derivation is **trace-blind** (`trace_comp_innerDerivation_eq_zero`, cyclic τ) |
| `computations/hh1_hecke_outer_derivations.py` | `dim HH¹(H₃(q)) = 0` generic/semisimple; `= 1` at roots of unity (`[2]_q = 0`, `[3]_q = 0`) |

Put together, these say something sharp that no corpus artifact yet states:
**the derivation-theoretic content that survives the Markov trace is exactly
the outer part, and the outer part exists exactly at roots of unity.** That is
the same address — fibre-level, cyclotomic, invisible to real trace data — as
the one surviving c₃ carrier.

This is a **structural co-location, not a derivation**, and the honest caveats
are load-bearing:

- The HH¹ work was built for the **P≠NP residue**, not for c₃. Nobody has
  shown the c₃ swing *is* an HH¹ class.
- Degree mismatch needs care: c₃ arrives via `tr_M`, i.e. it lives in **HH₀**
  (the cocenter). Derivations are **HH¹**. The link would be the action of
  HH¹ on HH₀, which is exactly what bean `qou-dilv` (He–Nie class-polynomial
  cocenter basis → HH¹ lift) proposes and which **nobody has run**.
- The substrate q₀ ≈ 1.10998 is **not** a root of unity ([2]_q ≈ 2.011 ≠ 0),
  so no outer derivation exists at the archimedean evaluation point. This is
  *not* fatal — it is the expected shape. Per AGENTS.md §"Im(q) at fibre vs
  observable level", c_k coefficients live in the **fibre**, and the correct
  target is a **Habiro-ring element evaluated at q₀**. The Habiro ring is
  precisely the object assembled from evaluations at **all** roots of unity,
  so a class whose dimension jumps `0 → 1` exactly on the cyclotomic locus is
  the right *kind* of object. But "right kind" is not "is".

**The falsifiable next step** (formalize-first, prunes before it searches):
compute `dim HH¹(H₅(ζ₅))` at the actual Bring root of unity — bean `qou-jcmw`,
status `todo`, nobody on it — and test whether the outer class's action on the
cocenter is **bar-odd**. If it is bar-**even**, the whole route dies to the
same bar-parity invariant that killed the real resolvent, cheaply and
decisively. That is a genuine prune either way, and it is one finite-dimensional
linear-algebra computation.

## 6. Bottom line

- **Nothing landed last week that closes Q_β.** The 1248 ppb residual is
  unchanged and is entirely the c₃ truncation.
- **One compute defect found and fixed**: the c_k tier auto-promotion was dead
  code. No accuracy change; the ladder can now actually report a future
  derived rung.
- **One new hard constraint**: the proton/muon anchor swing is 29.96 ppb =
  3.8× the L2 target. Deriving c₃ is necessary but **not sufficient** for
  Q_β to meet L2; the anchor layer must be settled too.
- **One genuine lead**: this week's HH¹/cocenter modules land on the same
  address as the surviving fibre-level c₃ carrier. Unconnected so far, and
  cheaply testable via `qou-jcmw`.
- **One documentation correction recommended**: re-scope
  "measurement-limited ⇒ not framework-closable" from scope-(b) to scope-(a).

Nothing here is wired to production. No fit was performed. Q_β remains open.
