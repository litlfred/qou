---
# qou-cqk6
title: mass_binding_dashboard._row re-casts q0 to float64 one line in — 2 of 12 rows publish 'not representable' for a number that is 2.5e74
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T14:05:57Z
updated_at: 2026-11-19T17:42:00Z
parent: qou-9nnz
---

## The claim

[`computations/mass_binding_dashboard.py:538`](computations/mass_binding_dashboard.py),
the first executable line of `_row` — the function that builds every per-isotope
row of the mass/binding dashboard:

```python
def _row(name, Z, N, alpha, me, Lbond, nucleon_msym, ame, max_strands):
    from q_parameter import Q_50_DIGIT_STR as _Q50
    q0 = float(_Q50)   # f64 only at this display/scalar boundary
```

**It is not a display boundary.** That `q0` is passed to `W_lambda_float(q0, lam)`
at line 641, whose result becomes `E_gate = alpha·ln(1/W_λ)` and `c_lam`, both of
which reach witnesses.

`_constants()` — twenty lines up — returns `q0` as an **mpf** and its docstring
says exactly why: *"The `float()` casts that used to sit on the return are GONE
(bean `qou-4ohh`). Their comment said 'cast ONCE at the boundary', but the
boundary moved."* The cast was removed from `_constants` and reappeared inside
`_row`, with the same justification, one call deeper.

## The evidence

`W_λ = [n]_q! / Π[h]_q²` at `q₀`, over the 12 isotopes of the SU(4) occupancy
sweep. Same function, same partitions, only the **type of `q0`** differs:

| iso | n | W(f64) | W(mpf) | relative move |
|---|---:|---:|---:|---:|
| ²H | 6 | 0.1114522027 | 0.111452202657 | 2.72e-17 |
| ⁴He | 12 | 0.0007736732673 | 0.000773673267319 | 9.73e-16 |
| ¹²C | 36 | 4.103332844e-06 | 4.10333284433e-6 | 4.42e-15 |
| ¹⁶O | 48 | 0.0006413279469 | 0.000641327946878 | 1.25e-14 |
| ²⁴Mg | 72 | 9611580845 | 9611580844.57 | **3.34e-14** |
| **⁴⁰Ca** | 120 | **nan** | **2.45640727656e+74** | **null → value** |
| **⁵⁶Fe** | 168 | **nan** | **8.14096263205e+192** | **null → value** |

Two things to read here, not one.

**The drift is not flat — it grows with `n`**, 2.7e-17 at n=6 to 3.3e-14 at
n=72, three orders across the table. `[n]_q!` is a product of `n` factors, so
the rounding accumulates. At n=72 it is already ~300× the f64 unit.

**Then it stops being drift and becomes absence.** At n=120 the f64 `[n]_q!`
reaches 7.4e+407, past the double ceiling ⇒ `inf`; the hook product is 3.0e+333
⇒ also `inf`; `inf/inf = nan`. Mechanism confirmed by computing both factors
separately.

## What the witness says, and why it is wrong

`probes/su4-occupancy-binding-sweep-probe.witness.json` publishes, for ⁴⁰Ca and
⁵⁶Fe:

```json
"W_lam": null,
"W_lam_undefined_reason":
  "float64 overflow in [n]_q! / prod(q-hooks)^2 — W_lambda not representable at this A"
```

The first half is right; **the second half is false.** `W_λ` is perfectly
representable at this A — it is `2.456e+74` and `8.141e+192`. What is not
representable is the *intermediate* `[n]_q!` **in float64**. A reader is told the
quantity does not exist at this mass number; the truth is that it was computed in
the wrong type.

The probe's own defensive comment makes the honest distinction and then loses it:
*"null, not a marker: an f64 OVERFLOW is a value this computation could not
represent, not a pole of the underlying quantity."* Correct — and the reason
string next to it says the opposite.

## What this does NOT undermine — the probe's finding STANDS

I went looking for the `qou-j540` shape (an overflow read as physics) and **did
not find it.** The exact arithmetic *confirms* the probe:

- `W_λ > 1` ⇒ surprisal `ln(1/W_λ) < 0` ⇒ `E_gate ≤ 0` ⇒ the occupancy reading is
  invalid. In mpf: `−22.99` (²⁴Mg), `−171.29` (⁴⁰Ca), `−444.19` (⁵⁶Fe).
- **The breakdown begins at ²⁴Mg, where f64 still works fine** (`W_λ = 9.6e9`, no
  overflow). So the finding was never resting on the overflow: it is established
  two isotopes before the ceiling is reached, by a number both types agree on.

The overflow only hides *how far* past 1 it goes — which turns out to be very
far, and monotonically (9.6e9 → 2.5e74 → 8.1e192). That is *additional* support
for the breakdown, not a threat to it.

## Options

**A. Fix line 538 — `q0 = mpf(str(_Q50))`.**
- *Means*: the one-line fix at the actual producer. `W_lambda_float` already
  returns mpf when handed mpf (verified); `E_gate` already uses `mp.log`;
  `c_lam` is already mpf; `_disp`/`_fmt` already take mpf by design.
- *Costs*: one line. No new compute infrastructure.
- *Risks*: **36 files import `mass_binding_dashboard`.** The moment any of them
  re-runs, its recorded numbers move — by ≤3.3e-14 for light isotopes, and from
  `null` to a value for the heavy ones. That is a mass witness refresh, which the
  2026-09-07 ASK-THE-OWNER directive explicitly does not exempt, even though the
  edit itself is exemption 1.
- *Commits to*: re-running and reviewing 36 consumers' outputs, or accepting that
  they drift out of sync until each is next run.

**B. Fix only the reason string, leave the arithmetic.**
- *Means*: `W_lam_undefined_reason` says what is true — the f64 intermediate
  overflows; the quantity is finite and is ~2.5e74 / 8.1e192; the reading is
  invalid because `W_λ > 1`, which already holds at ²⁴Mg.
- *Costs*: a few lines in one probe. Nothing numeric moves anywhere.
- *Risks*: essentially none. The witness stops asserting something false.
- *Commits to*: nothing; A remains available.

**C. Fix the probe locally — compute `W_λ` in mpf from `su4_partition` inside the
probe rather than taking `_row`'s f64 value.**
- *Means*: correct numbers in this one witness without touching the shared module.
- *Costs*: ~15 lines in the probe; re-run; verify the 12 rows.
- *Risks*: **forks the computation.** The probe and the dashboard would then
  report different `W_λ` for the same isotope, which is worse than either being
  uniformly wrong. Also does not drain the other ~280 f64 fields, which come from
  `_row` regardless.
- *Commits to*: keeping the fork in sync, or doing A later anyway.

**D. Do nothing.** The witness keeps saying `W_λ` is "not representable at this
A" for two isotopes where it is a known number, and `_row` keeps forming the
q-factorial in float64 for all 36 consumers.

## Default if nobody acts

**D.** Nothing moves. The exposure is a false statement in a committed witness
and an accumulating (n-dependent) rounding path in a widely-imported module.

## Blast radius in real terms

`_row` is the row-builder for the mass/binding dashboard, and
`mass_binding_dashboard` is imported by **36** Python files, including
`qou-mass/src/qou_mass/api.py` (the external-researcher facade),
`per_atom_rho_deviation.py`, `derive_m_p_hecke_path_a.py`, and the meson
satellite probes. Anything reporting `E_gate`, `c_lam`, `W_lam` or a quantity
derived from them is downstream of this cast.

## Recommendation — my judgement, not a finding

**B now, A as its own owner-scoped change.** B costs nothing, removes a false
claim from a committed witness today, and forecloses nothing. A is the correct
fix and is exemption-1 on its face, but its *consequence* is a 36-consumer
witness refresh, and that is the owner's call, not mine — the directive is
explicit that regenerating derived artifacts belonging to other arcs is not
exempt. C I would not do: a forked `W_λ` is worse than a consistent one.

## Scope of what I checked

The 12 isotopes of this probe's sweep, at the ground-state partitions `_row`
actually uses (`get_ground_state_partition(Z, N, NUCLEAR_SPINS[name])` — **not**
`su4_partition`, which is a separate field and coincides here but need not in
general; I got this wrong once before checking). I did **not** check the other 35
consumers, nor whether any of them already compensates for the cast.


---

## SECOND FINDING, same probe: the committed witness is STALE, its scriptHash MATCHES, and one number moved 20 %

Found while verifying the fix above. I ran the **unmodified** producer against its
committed witness — the screen I use for every drain, and which I had skipped on
the first pass, which is how I nearly attributed this to my own edit.

```
committed vs UNMODIFIED-fresh : 286 substantive diffs
raw float64                   : 297 -> 52
scriptHash                    : 378e3484d119 == 378e3484d119   (MATCHES)
```

The producer's own source is byte-identical to what wrote the witness. This is
**import-cone drift**: `mass_binding_dashboard` changed underneath it. AGENTS.md
records this as the only *growing* bucket in the witness-staleness triage and
notes it is invisible to the `git diff <producer>` check the same document tells
you to run — this is an instance, and it is **not cosmetic**.

### What moved, and it is exactly one thing

| form | committed | fresh | relative |
|---|---:|---:|---:|
| `B_sym` | 0.8949930518334133 | 0.8949930518334134 | 1.1e-16 |
| `B_lincomp` | 0.7345800293973251 | 0.7345800293973251 | **0** |
| `B_gate` | 0.8022316573515565 | 0.8022316573515565 | **0** |
| `B_sym_gate` | 0.8949930518334133 | 0.8949930518334134 | 1.1e-16 |
| **`B_sym_ent`** | **0.5787587543775681** | **0.6964514151549657** | **0.2034** |
| `B_vol` | 0.7140764551766194 | 0.7140764551766197 | 4.2e-16 |

Five of six forms are stable at the f64 floor. `B_sym_ent` moved **20 %** on the
aggregate and **14–28 % on every one of the 6 rows where it is defined**, always
downward:

    2H   4.0007 -> 2.8888   (27.8 %)      6Li  17.469 -> 14.554  (16.7 %)
    3H   7.9996 -> 6.1813   (22.7 %)      7Li  20.796 -> 17.846  (14.2 %)
    3He  7.2429 -> 5.4653   (24.5 %)
    4He 11.0251 -> 8.7354   (20.8 %)

### The verdict survives, but not comfortably

`best_scale_free_form` is `B_sym_ent` before and after — it is still the lowest
RMS. But the margin over the runner-up (`B_vol`) collapses:

    committed : 0.7141 - 0.5788 = 0.1353
    fresh     : 0.7141 - 0.6965 = 0.0176      (7.7x narrower)

So the probe's headline — that the bar-odd emitted channel is the best
scale-free form — is now decided by 2.5 % rather than 23 %. That is worth a
reader knowing.

### Probable cause, stated as probable

`E_multilink = alpha * abs((defect0 - defecti) / 2)` (line 719) is a **difference
of two near-equal quantities**, and `B_sym_ent = B_sym + E_multilink`. That is
the canonical catastrophic-cancellation site, and `_row`'s own neighbouring
comment describes precisely this failure for a sibling residual: *"the residual
could not be smaller than f64 epsilon on quantities of order 1-30 MeV whatever
the mathematics did."* `dce9a3f9c58` (`fix(qou-4ohh)`) removed the f64 casts that
caused it.

So the **fresh value is very likely the correct one** and the committed 0.5788
was cancellation noise. I am **not** asserting that: I have not bisected it (the
clone is shallow, and re-running per commit is expensive), and there is a second
candidate in the window — `b56e7c33025`, the electron-binding swap, which moves
`m_nuc_meas`.

**Two adjacent claims that need care, neither of which I am calling wrong:**

- `dce9a3f9c58`'s own comment says *"every other column of this dashboard is
  BYTE-IDENTICAL."* `B_sym_ent` is emitted by `_row` and reaches probes; it moved
  14–28 %. Whether it is a "column" in the sense that commit meant (it is
  referenced at lines 1199/1210) is not settled here. If it is, the verification
  was scoped to the printed table and missed a probe consumer.
- Line 709 records *"Measured impact on E_multilink was 5e-22..3e-19 relative"* —
  that is a **different** change (2026-08-26) and must not be read as bounding
  this one.

### Why I did not commit the re-run

Re-running drains 245 raw-float64 fields (297 → 52) and would be exemption-1 on
its own. But the same re-run adopts a 20 % move in another arc's published
finding and narrows a headline margin 7.7×. Under the 2026-09-07 directive that
is not mine to land quietly. **The committed witness is restored; only the source
comment/string fix is on the branch.** Consequence: the producer's scriptHash now
differs from the witness, which is the normal state of an un-re-run producer, and
the witness stays stale until whoever owns `B_sym_ent` re-runs it.

### What that leaves for the drain queue

`su4-occupancy-binding-sweep-probe` (297 fields) is **not blocked on float64
work** — 245 of its fields drain by re-running today. It is blocked on a decision
about `B_sym_ent`. Its sibling `probes/su4-occupancy-binding-mass-probe` (167
fields, the `--group low` run of the same script) is in the same position.

---

## 2026-09-14 — the SECOND FINDING's probable cause is REFUTED by measurement, and a named commit replaces it

The entry above attributes the 20 % `B_sym_ent` move to catastrophic cancellation
at `mass_binding_dashboard.py:719`, calling it *"the canonical
catastrophic-cancellation site"*. **It is not cancelling, and the producer's own
comment three lines above says so.** Lines 708-715:

> *"Measured impact on E_multilink was 5e-22..3e-19 relative (2H/3H/3He/4He),
> i.e. none of the displayed digits moved — **the two defects differ at O(1), so
> the subtraction below is not in fact near-cancelling at these parameters.**"*

The entry cites that same comment block for its *other* caveat (the "5e-22..3e-19
is a different change" warning) and does not read the sentence next to it.

### Measured, at `mp.dps = 60`, all four light isotopes

`|defect0 − defecti| / |defect0|` — the cancellation ratio. Near-cancelling would
be `≪ 1`:

| iso | ratio |
|---|---:|
| ²H | **0.1818** |
| ³H | **0.1761** |
| ³He | **0.3352** |
| ⁴He | **0.3305** |

The two defects differ by **18–34 %**. There is no cancellation to be
catastrophic. Scope (b) — this is a *measured* property of the quantities at
these parameters, not a failure of one construction to reproduce a number.

### My own alternative hypothesis is ALSO refuted, and I am recording it because it was the better one

`B_sym` uses only the **forward** leg; `E_multilink` additionally uses the
**inverse** leg at `1/q`. A change confined to the inverse leg would move
`B_sym_ent` and leave `B_sym` at the f64 floor — *exactly* the observed
signature. And lines 702-704 document precisely such a change: the inverse leg
*"used to divide into `_mp.mpf(str(q_parameter.Q))` — the f64 — so the
inverse-anchor leg was capped at ~17 digits while the forward leg was not."*

Tested directly rather than by bisection (the clone is shallow, and `git blame`
on those lines returns the boundary commit `^638f298ffb`, so blame cannot reach
the author). Computing `E_multilink/alpha` both ways:

```
q_inv_new = 0.9009182839557414921608229    (50-dps string)
q_inv_old = 0.9009182839557414983226296    (f64-capped)
differ by rel 6.84e-18

              E/alpha new        E/alpha old        old/new
2H          0.0133667750002    0.0133667750002        1.0
3H         0.00994080155647   0.00994080155647        1.0
3He         0.0217161702422    0.0217161702422        1.0
4He         0.0129184715125    0.0129184715125        1.0
```

**Byte-identical, `old/new = 1.0` on every isotope.** A 6.8e-18 move in `q` does
not survive to `E_multilink` at 12 digits. The inverse-leg precision fix is real
and correct and is **not** what moved `B_sym_ent`.

Script: `scratchpad/emulti.py` (measurement only, writes nothing; mpf end to end,
no `float()` anywhere, per the probes-are-not-exempt rule).

### What IS in the window — a named commit with a mechanism

The witness's `computedAt` is **2026-08-29T04:14:20Z**. Two non-merge commits
touch the relevant cone after it, and only one of them touches the trace:

```
818a244f13  2026-09-05  fix(qou-wdij): route non-monotone words to the general-word
                        kernel — the atom trace producer runs again
                        [computations/tr_m_atom_via_transfer.py]
dce9a3f9c5  2026-09-05  fix(qou-4ohh): the dashboard's own accuracy claim was the
                        f64 floor [computations/mass_binding_dashboard.py]
```

`tr_m_atom_via_transfer` is the module supplying `ta`/`tf`/`ta_i`/`tf_i`, and it
is the **same module AGENTS.md names as the worked example of import-cone drift**
(`binding_canonical` source-stable while `tr_M_atom` moved 48 %). `818a244f13`
changes *which kernel computes the trace* for non-monotone words — and under the
2026-09-05 intra-nucleon ordering ruling (`qou-hu1f`) the canonical word is
**borromean**, where a monotone generator sequence is the **superseded grouped**
word. So the production word is exactly the class this commit re-routes.

**I am stating that as the live candidate, not as the cause.** What is
established is that the two previously-offered causes are refuted and that
`818a244f13` is in the window and touches the right quantity by the right
mechanism. What is *not* established is that it produces the 14–28 % per-row
move; confirming that means running the trace under both kernels, which I did
not do.

### What this changes for whoever picks the bean up

The blocker is unchanged — `B_sym_ent` still needs a decision before the 245-field
drain can land, and that decision is still the owner's. What changes is **where to
look**: not at line 719, which is measurably fine, but at the kernel routing in
`tr_m_atom_via_transfer`. An owner deciding on the cancellation story would be
deciding on a refuted premise, and the fix implied by it (harden line 719) would
change nothing.

Also worth recording against the entry above: **option B has LANDED.**
`su4_occupancy_binding_probe.py` on main emits the honest reason string
(*"W_lambda ITSELF is finite and representable at this A; only the f64
intermediate is not"*) with a 12-line comment. The two **witness** rows still
carry the old false text, because the witness cannot be refreshed without
re-running — i.e. it is blocked on the same `B_sym_ent` decision. So B is done at
the producer and incomplete in the artifact, which is the normal state and not a
second defect.

---

## Verification & Fix Update (2026-11-15 — Owner Ruling Q-9NNZ-2 = 1)

- **Status:** Kept `in-progress` pending owner review/merge of PR [`litlfred/qou#8082`](https://github.com/litlfred/qou/pull/8082) (`1076c65f2a00f2604e1ba22458355ff382e7bde9`).
- **Fixed in PR #8082 (`1076c65f2a`):**
  - In `computations/mass_binding_dashboard.py`, `_row` and `W_lambda_float` now evaluate `[k]_q`, `[n]_q!`, and `W_lambda = q^{c(lambda)} / prod_b [h(b)]_q` in `mpmath.mpf` at `>= 60` dps from `_Q50` instead of `float(_Q50)`.
  - Verified finite `mpmath.mpf` values with zero float64 intermediate overflow across the dashboard table, including `${}^{40}\mathrm{Ca}$` ($n=120$, $W_\lambda = 2.45640727656 \times 10^{74}$, $E_{\mathrm{gate}} = -717.01673\text{ MeV}$, $c_\lambda = -0.47704909$) and `${}^{56}\mathrm{Fe}$` ($n=168$, $W_\lambda = 8.14096263205 \times 10^{192}$, $E_{\mathrm{gate}} = -1859.3847\text{ MeV}$, $c_\lambda = -0.26474347$).



## Progress Update (2026-11-19)
Actively eliminating `q0 = float(_Q50)` in `mass_binding_dashboard._row` so `40Ca` (`2.456e74`) and `56Fe` (`8.141e192`) evaluate in 80-dps `mpmath` (`1f1e86e9`).

## Resolution (2026-11-19)

Completed: Eliminated `float(q0)` re-cast in `computations/mass_binding_dashboard.py`, `snappy_cusp_seeding.py`, and `qbeta_g3_annihilator_certification.py`.
