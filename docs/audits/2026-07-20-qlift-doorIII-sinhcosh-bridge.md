# Door-iii: sinh/cosh (bar-even/odd) NON-module bridge C1² → GGM eq 49 (2026-07-20)

**Bean:** `qou-ceg6` · **Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Status:** AUDIT — probe complete, **scope-(a) REFUTED** (with a confirmed
leading-order match; see §3). No open item declared; no conjecture status changed.

## 0. The carve-out this attacks

Door-i ([`…doorI…`](2026-07-20-qlift-doorI-analytic-summation.md)) proved, with the
permanent invariant **isoclinicity**, that C1 (`[m+2]_q b_{m+2}=b_{m+1}+b_m`,
∞-slopes {½,½}) and GGM eq 49 (`y_{m+1}=(2−q^m)y_m−y_{m−1}`, ∞-slopes {−1,+1})
are inequivalent q-difference **modules** under every gauge, formal q-Borel weight,
analytic q-summation, and ramified pullback. It left **exactly one** carve-out:
**non-module** sequence-level maps. The owner's insight names a candidate — a
sinh/cosh (bar-even/odd, `q→1/q`) **twist of the symmetric SQUARES of C1**: since
2·(½)=1, sym²(C1) sits at slope 1, the GGM slope. This probe tests that candidate.

## 1. The probe

[`computations/probes/qlift_doorIII_sinhcosh_bridge_probe.py`](../../computations/probes/qlift_doorIII_sinhcosh_bridge_probe.py)
(mpmath dps=60, m=0..50, q ∈ {0.9, 1.05, 1.10998}). Two independent C1 solutions
f₊,f₋ → rank-3 sym² basis {f₊², f₊f₋, f₋²} plus its bar copy at 1/q (6 columns).
**Pre-stated kill criterion:** fit a fixed (m-independent) coefficient vector on
m=0..14, measure the **extrapolation** residual on m=34..50; `<1e-40` ⇒ CONSISTENT
(bridge lands), `O(1)` drift ⇒ REFUTED. A **solver self-test** (fit a target that
IS a known sym² combo) recovers it to `≤4e-61` at every q, so an O(1) residual is
a genuine miss, not a solver artifact.

- **TEST A** — forward GGM solutions (y_a, y_b) vs the 6-column basis.
- **TEST B** — GGM's minimal (forward-decaying) solution, extracted by Miller
  backward recursion from m=140, vs the 3-column unbarred sym² basis — the
  **slope-matched** test (both decay at the same leading rate; see §3).

## 2. Verdict — REFUTED (scope-(a))

At **every** tested q, no fixed linear combination of the sym² or bar-sym²
sequences reproduces any GGM solution across the tail (relative residual = 1.0,
i.e. the prediction is negligible against the target — for TEST A the forward GGM
grows while every candidate does not; for TEST B even the in-window fit is 1.0).
The sinh/cosh bar-even/odd sym² construction, **alone**, does not reproduce GGM.

This is **scope-(a)** ("this construction, alone, does not reproduce the numbers"),
**not** scope-(b): no ingredient is structurally excluded here — Door-i already
supplies the module-level (b) exclusion via isoclinicity. Other non-module
identifications are untouched; this measures the miss for THIS construction only.

## 3. The honest residual structure — leading order DOES match, the sequence does not

The growth diagnostics (theta exponent γ in |·| ~ q^{γm²}) at the substrate
q=1.10998 are the informative part:

| object | γ (measured) | slope reading |
|---|---|---|
| C1 f₊ | −0.266 ≈ **−¼** | slope ½ |
| sym² f₊² | −0.533 ≈ **−½** | = 2× C1 — **confirms 2·(½)=1** |
| GGM y_a (forward/dominant) | +0.556 ≈ **+½** | slope 1 |
| GGM recessive (minimal) | −0.547 ≈ **−½** | **matches sym²** |

So the slope arithmetic is **confirmed at leading order**: sym²(C1) doubles C1's
theta exponent to −½, and GGM's *recessive* leg decays at that same −½. The
bar-even/odd sym² construction therefore reproduces GGM's leading **growth class**
(slope 1) — but the fixed-combination extrapolation still fails, so it does **not**
reproduce the GGM sequence itself: matched leading exponent, mismatched sub-leading
theta fine-structure. The forward (dominant, slope +½) GGM leg is not matched by
any candidate at all (all sym²/bar-sym² sequences decay or grow slower). The
6-column solve on the forward GGM is additionally ill-conditioned (mixing q^{−m²/2}
decay with slower bar columns; residual 2.7e15 at substrate q), consistent with
"no combination exists".

## 4. Effect on the conjecture

`conj:qdifference-kernel-prolongation-symbol` is **unchanged**. Door-i's favored
reading R1 (C1 is the binding series' own Gevrey-½ module, a distinct object from
the colored-Jones/Stokes carrier) is *reinforced*: the most natural non-module
candidate — the one whose leading slope arithmetic works exactly — still fails to
identify C1² with GGM. The non-module carve-out remains formally open but this
specific, well-motivated realization of it is refuted.

## 5. Discipline

Scope-(a) vocabulary; pre-stated kill criterion + solver self-test; parameter-free;
no AME data; the only "fit" is the m-independent linear coefficient solve whose sole
purpose is the extrapolation kill-test. Corpus-grep: the whole C1↔GGM trail is this
branch's 2026-07-20 files; no prior attempt, no closed item re-opened.
Witness: [`qlift_doorIII_sinhcosh_bridge_probe.witness.json`](../../computations/probes/qlift_doorIII_sinhcosh_bridge_probe.witness.json).
