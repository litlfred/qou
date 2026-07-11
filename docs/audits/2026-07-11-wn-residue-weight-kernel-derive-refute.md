# Jet-filtration residue weight w_n(K) — the q-difference kernel R(q,x) derive-or-refute

**Date:** 2026-07-11 · **Bean:** t7qv (θ_λ magnitude gate) · **Axis:** A≥3
binding closure · **Tier:** numerical derive-or-refute (scope-(a) negative) ·
**Discipline:** no fit, no value wired, no tier change. Probe
[`binding_wn_kernel_derive_refute.py`](../../computations/binding_wn_kernel_derive_refute.py).

## Context

The na-Stokes / Reeb jet-filtration binding
`B_strong(K) = Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K)` has two factors: the **derived
extensive kernel** `a_D^(n)=lw(n−1)` (the super-exponential SW period / mean
quantum dimension — Lean-proved extensive in `QOU.Mass.JetFiltrationExtensive`,
sorry-free) and the **open residue weight** `w_n(K)`. Option #2 of the
[jet-filtration audit](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)
is the decisive backstop: does `w_n` follow a *parameter-free* q-difference
recursion `G(qx;q)=R(q,x)G(x;q)` (the conjecture's own prescription), or is it a
fit?

## Method (no per-isotope fit)

1. **Coulomb correction** `B_strong = B_AME + E_Coulomb` (from `coulomb_energy.py`)
   isolates the strong sector: D 2.225, ³H 8.482, ³He 8.716, ⁴He 29.203 MeV.
2. **A=3 mirror universality** — after Coulomb, ³H (pnn) and ³He (ppn) agree to
   **+2.73 %** (charge-symmetry-breaking, a small separate effect), so a
   body-order-only `w_n` is admissible.
3. **Extract** universal `w_2, w_3, w_4 = 4.353, 9.331, 15.919` (ratios
   w₃/w₂ = 2.143, w₄/w₃ = 1.706) from D / avg(³H,³He) / ⁴He — three equations,
   three unknowns, no tuning.
4. **Test** the ratios against parameter-free derived kernels.

| candidate R(q,n) | pred w₃/w₂ | pred w₄/w₃ | max \|err\| |
|---|---|---|---|
| geometric (r32 = r43?) | 2.143 | 1.706 | 22.7 % |
| R = [n]_q | 1.514 | 1.350 | 29.4 % |
| R = a_D self-ratio | 1.337 | 1.894 | 37.6 % |
| R ∝ n | 1.500 | 1.333 | 30.0 % |
| **R = [n]_q²** | **2.291** | **1.823** | **6.9 %** (lone near-miss) |

## Verdict — REFUTED (scope-(a))

No parameter-free derived kernel reproduces both ratios to 5 %. **`[n]_q²`** is
the lone near-miss (6.9 %), notably echoing the **`√C_λ` amplitude near-miss**
(11.14 vs 12.72, ~12 %) of the merged compact-weight PR #3518 — the true weight
sits *between* the q-integer and its square in both probes, a cross-probe
"squared-q-dimension near-but-not-exact" signature. A recursion tuned to
reproduce the three `w_n` would be a banned **seventh Δ_λ ansatz**.

This **confirms** the corpus finding
([`2026-07-06-reeb-flow-pn-magnitude-...md`](2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md)
§2j tranche 8): the residue weight `w_n(K)` **is the Δ_λ / W_λ gate in
disguise** — free per-body-order data carrying the same irreducible content, not
a recursion output.

## The na-Stokes kernel's eigenfunction relation → the q-Hermite basis (owner steer)

Owner steer (2026-07-11): *"how does `a_D^(n)` inform the kernel? look at the
relations defining the eigenfunction → the appropriate orthogonal basis for
q-hyperbolic and categorical action."* Followed, and it is the productive lead:

`a_D^(n) = S(n)/n`, `S(n) = Σ_{λ⊢n} dim_q V_λ` = the **q-involution number**
(→ 1, 2, 4, 10, 26, … at q=1). `S` obeys a **three-term recurrence**
`S(n) = S(n−1) + c_n·S(n−2)`:

| n | c_n | [n−1]_q | c_n/[n−1]_q |
|---|---|---|---|
| 3 | 2.01090 | 2.01090 | **1.0000000** |
| 4 | 3.06011 | 3.04371 | 1.0053897 |
| 5 | 4.17602 | 4.10968 | 1.0161408 |
| 6 | 5.37732 | 5.22044 | 1.0300510 |
| 7 | 6.70428 | 6.38809 | 1.0494975 |
| 8 | 8.17409 | 7.62534 | 1.0719632 |

**`c_3 = [2]_q` exactly** (to compute precision); `c_n/[n−1]_q` rises
monotonically — the **q-Hermite / Rogers–Szegő** recurrence, i.e. the orthogonal
basis of the q-oscillator / q-hyperbolic categorical action (corpus
[`QOU.Mass.RogersSzegoInhabited`](../../content/quantum-observable-universe/lean/QOU/Mass/RogersSzegoInhabited.lean)).
This is *why* the ad-hoc constant-ratio kernels miss: they are the wrong basis.

### Does `w_n` resolve in that q-Hermite basis? — No (scope-(a))

Two zero-parameter tests, both fail:

- **Test A** — `w_n` does **not** obey the `a_D` q-involution recurrence:
  `w_4 = w_3 + c_4·w_2` predicts 22.65 vs actual 15.92 (**42.3 %** off). `w_n` is
  not in the eigenspace.
- **Test B** — no Rogers–Szegő `H_n(x;q)` reproduces the ratio-shape (2.143,
  1.706) at any natural x: closest `x=1/q` at **13.2 %** (x=1 19.1 %, x=q 25.7 %,
  x=q² 32.9 %, x=q−1 48.1 %).

The signature: the observed `w_n` ratios **decelerate** (2.143 → 1.706,
sub-geometric), whereas every Rogers–Szegő family is **near-geometric** (its two
successive ratios are nearly equal). So the q-Hermite basis is the correct
**language for the KERNEL** `a_D^(n)`, but the **MULTIPLIER `w_n` is the
genuinely gated `W_λ` content** — and its sub-geometric deceleration is a new,
sharp fingerprint the s5-so3 `W_λ` projector must reproduce (a testable
constraint on the gated construction, not another fit).

## Option #1 — the hyperbolic-link-volume route (also refuted)

The audit's un-refuted forward route was `w_n = hyperbolic volume of the n-body
inter-nucleon sub-link` (the literal "hyperbolic volumes via non-abelian
Stokes"). Tested in
[`binding_wn_link_volume_probe.py`](../../computations/binding_wn_link_volume_probe.py)
against the corpus-witnessed link volumes:

- **Refuted at n=2 — scope-(b) structural exclusion.** The 2-body sub-link of the
  Borromean atom `𝓑_K` is **non-hyperbolic** (Vol=0): the Borromean rings are
  **Brunnian**, so removing any one component leaves the 2-component unlink, and
  the SDP binding-link registry (`binding_link_volumes.py`) independently assigns
  the deuteron bond to the **Hopf** link (Seifert-fibred, Vol=0). Either way the
  n=2 volume vanishes, but the extracted `w_2 = 4.353 > 0`. Cited invariant:
  Brunnian / Seifert-fibred non-hyperbolicity.
- **The Whitehead:Borromean 1:2 near-miss is a coincidence.** Re-choosing the
  links (Whitehead L5a1 for n=2, Borromean L6a4 for n=3) gives the exact
  parameter-free ratio `Vol(Borromean)/Vol(Whitehead) = 2` (both ∝ Catalan `G`)
  vs observed `w_3/w_2 = 2.143` — a **7.2 % near-miss**, *not* a closure, and it
  contradicts the registry's Hopf assignment for the deuteron bond. So the 1:2 is
  a numerical coincidence of Catalan multiples, not a derivation.

Net: neither the q-Hermite expansion nor the literal link-volume supplies `w_n`;
both point back to the gated `W_λ` multiplier (the volume route excluded at n=2
by a proved invariant, the q-Hermite route by the sub-geometric deceleration).

## Two permanence points (scope-(a), not (b))

The refutations above are "*this parameter-free recursion / this q-Hermite
expansion, alone,* does not fix `w_n`" — **not** a structural exclusion. Two
permanence points stand:

- The na-Stokes extensive kernel `a_D^(n)=lw(n−1)` is a **permanent, correct
  contribution** (Lean-proved extensive) — refuting the *recursion form of the
  multiplier* says nothing against it.
- The **un-refuted route** is option #1: `w_n` = hyperbolic link-volume of the
  n-body inter-nucleon sub-link (a topological invariant, the literal
  "hyperbolic volumes via na-Stokes"; merges with gap #2). That needs SnapPy
  volumes, not a recursion — a separate compute, not a fit.

Owner-gated closure = the geometric `W_λ` knot-ideal projector (s5-so3 keystone,
narrow 2026-06-19 reversal). No production touch; no value wired; no tier change.

## Cross-references

- Jet-filtration audit (mechanism half): [`2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md`](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)
- "w_n IS the Δ_λ gate" invariant: [`2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`](2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md) §2j
- √C_λ amplitude near-miss (prior probe): [`2026-07-11-he4-binding-subppb-reverse-fit-trace.md`](2026-07-11-he4-binding-subppb-reverse-fit-trace.md) §4b (PR #3518)
- Δ_λ gate status: [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md), Option-E ledger [`docs/coordination/option-e.md`](../coordination/option-e.md)
