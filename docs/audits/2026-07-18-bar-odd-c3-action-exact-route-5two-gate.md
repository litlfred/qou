# Bar-odd c₃ action — the exact route is the chiral 5₂ Habiro tail; naive twist-Gaussian ansatz falsified, gate is the verified 5₂ cyclotomic coefficients

**Date:** 2026-07-18 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ · **Tier:** numerical
scope-(a) (a target statement + an ansatz falsification; **no** exact action claimed) ·
**Discipline:** no fit (nothing tuned to CODATA), no c_k wired, nothing to production,
no tier change.

## The exact route (from the merged bar-even result)

The sibling b3ix result (merged 2026-07-18): the **4₁** Habiro cyclotomic tail
`S(q) = Σ_n ∏_{j=1}^n (1−q^j)(1−q^{−j})`, at **real** `q` (the archimedean `ρ_∞`
face), is **bar-even** and has optimal-truncation resurgent action **exactly `π²/5`**
(golden-ratio dilog: minimal term at `2sinh(n*t/2)=1 ⇒ n*t/2 = arcsinh(½) = ln φ`,
then `−4∫₀^{ln φ} ln(2sinh s) ds = π²/5` via Landen `Li₂(φ⁻²)=π²/15−ln²φ`). It is
**distinct** from the geometric `Vol(4₁)/π ≈ 0.646` — the `ħ↔2πi/N` wall made exact.
That probe explicitly flagged: because 4₁ is amphichiral, its tail carries **no**
bar-odd datum, so the bar-odd channel (the c₃ / `N_odd` datum) **must use the chiral
5₂ Habiro tail**.

**Exact target, stated precisely:** the bar-odd c₃ action is the `ρ_∞` (real-`q`,
archimedean-face) optimal-truncation resurgent action of the **chiral 5₂ Habiro
cyclotomic tail** — the direct bar-odd analog of 4₁'s `π²/5`, expected to be a dilog
constant tied to `det(5₂)=7` (as `π²/5` is tied to `det(4₁)=5`'s golden ratio).

## What this probe establishes

[`qbeta_5two_habiro_archimedean_action_setup_probe.py`](../../computations/probes/qbeta_5two_habiro_archimedean_action_setup_probe.py):

1. **The 4₁ Kashaev template is sound.** `Σ_n ∏|1−q^j|²` at roots of unity gives
   `Vol_est` `2.447 → 2.271 → 2.167` (N=100,200,400), decreasing monotonically toward
   `Vol(4₁)=2.030` (the slow `log N / N` volume-conjecture convergence). The method
   reproduces the known volume.

2. **The naive twist-Gaussian 5₂ ansatz is FALSIFIED.** The plausible guess
   `Σ_n q^{−p·n(n+1)} ∏|1−q^j|²` (5₂ = twist knot K₂) does **not** reproduce
   `Vol(5₂)=2.828`:

   | ansatz | N=200 | N=400 | vs Vol(5₂)=2.828 |
   |---|---|---|---|
   | p=1 | `1.810` | `1.713` | undershoots, **decreasing** |
   | p=2 | `2.075` | `1.977` | undershoots, **decreasing** |

   At a root of unity `q^{−p·n(n+1)}` is a **pure phase** (`|·|=1`), so it only
   re-weights the interference; both `p` undershoot and *decrease* with `N`, so
   neither can converge *up* to `2.828`. The 5₂ cyclotomic coefficient is genuinely
   **more structured than a Gaussian phase**.

## The gate (why no action is computed)

The exact 5₂ archimedean action needs the **verified 5₂ cyclotomic coefficients**
`C_{5₂,n}(q)` (Masbaum's twist-knot formula) — a literature datum. It **must not be
fabricated**: an unverified cyclotomic form that happened to yield a "clean" dilog
action would be numerology, exactly the anti-laundering trap. So this front is gated
on obtaining and verifying `C_{5₂,n}(q)` (verification target: the resulting Kashaev
sum must reproduce `Vol(5₂)=2.828` at roots of unity, matching the corpus value).

**Recommended continuation:** obtain `C_{5₂,n}(q)` from Masbaum (2003) /
Habiro–Le, verify against `Vol(5₂)`, then apply the identical optimal-truncation
dilog-action method to the real-`q` tail and read off the bar-odd action (test
against `det(5₂)=7` dilog candidates). Coordinate with the b3ix/5₂ sibling (#3966,
which the merged 4₁ probe flagged) — this may already be in flight there.

## Scope (anti-laundering)

A target statement + a falsified ansatz — records what the exact route *is* and
eliminates one specific wrong turn (the twist-Gaussian). **No** exact bar-odd action
is claimed; the honest wall is the verified cyclotomic coefficients. No fit; no c_k;
no tier change.

## Cross-references

- Bar-even template (the method): 4₁ Habiro tail action `π²/5` (b3ix, merged 2026-07-18) — [`qbeta_fourone_habiro_tail_action_probe.py`](../../computations/probes/qbeta_fourone_habiro_tail_action_probe.py)
- Verified 5₂ geometric datum: [`qbeta_5two_quantum_volume_probe.py`](../../computations/probes/qbeta_5two_quantum_volume_probe.py) (`Vol(5₂)=2.828`)
- The single-level / length-blocked D-ladder route (this session): [`2026-07-18-dladder-single-instanton-extraction.md`](2026-07-18-dladder-single-instanton-extraction.md)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
