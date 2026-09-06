---
# qou-hok7
title: 'Deuteron-wall resummation: classical Borel on q=1 period is the WRONG transform (substrate object is q-Gevrey) -> reopen; needs q-Borel of Z_n(q0)'
status: todo
type: task
priority: high
created_at: 2026-08-21T15:02:55Z
updated_at: 2026-09-06T15:44:14Z
---


DIAGNOSTIC DONE (2026-08-21). Confirmed the full-transseries negative resummed a_D^(n)=I(n)/n (q=1 telephone period) with classical Gamma(n/2+1) Borel; substrate object Z_n(q0) is q-Gevrey (log Z_n ~ Theta(n^2), lever1 order q0^{n^2/2}). classical Gamma-Borel coeff q0^{n^2/2}/Gamma(n/2+1) DIVERGES (1.15->7.3e17, n<=40) => wrong transform. Deuteron-wall resummation REOPENED. OPEN next step: q-Borel-Laplace resummation of Z_n(q0) (divisor ~q0^{n^2/2}); q-Borel machinery exists (qborel-ecalle-resum-barodd, qbeta_habiro_tail_util) but not pointed at the deuteron. Probe: deuteron_wall_wrong_transform_diagnostic.py; audit: 2026-08-21-deuteron-wall-resummation-wrong-transform.md


## 🛑 CORRECTION 2026-09-06 — the divisor in this bean is wrong by a square root (`qou-p6m1` session)

This bean's open step reads "q-Borel-Laplace resummation of Z_n(q0) (divisor
~q0^{n^2/2})". **Measured: the divisor is `q0^{n^2}`.** An agent building the
transform on `q0^{n^2/2}` divides away only half the growth, is left with
`q0^{n^2/2}` still undivided, fails to converge — and would likely read that
failure as a fact about the deuteron rather than about the divisor.

**Probe:** `computations/deltalambda/deuteron_qborel_kernel_level_probe.py` (7/7,
witness `deuteron-qborel-kernel-level.witness.json`).

**Method.** `log Z_n / n^2` is still falling at n=30, so it cannot decide this by
eye. Second differences can, with no fit and no tolerance on the limit:
`d2(a n^2) = 2a` (positive constant) vs `d2` of classical Gevrey-1/2
`(n/2)log n` ~ `1/2n -> 0`. The involution numbers `I(n) = Z_n(1)` are carried as
an IN-PROBE CONTROL: their d2 must fall, and does (0.0553 -> 0.0158). So the
discriminator is validated on a known-classical object, not assumed.

**R1.** `d2 log Z_n` RISES 0.1685 -> 0.1862 toward `2 ln q0 = 0.2087`. Since
`d2(a n^2) = 2a`, that gives `a = ln q0`, i.e. **`Z_n ~ q0^{n^2}`**. The
`q0^{n^2/2}` hypothesis predicts `d2 -> ln q0 = 0.1043`, which is **1.78x below**
the measured value.

**Where the error came from — the producer contradicts itself.**
`lever1_transfer_operator_spectral_qgevrey.py`'s docstring says in ONE sentence
that the multiplier slope is `2 log q0` (correct — it is what its own assertion
`S2_target_2_ln_q0` tests) and then concludes `q0^{n^2/2}`, which does not
follow: slope `2a = 2 ln q0` gives `a = ln q0`. The wrong half propagated here
and into the 2026-08-21 diagnostic.

**R2 — and level 1 is not enough anyway.** `Z_n` is DEFINED as
`S^bal(n;q) * q^{n(n-1)/2}`, and `n(n-1)/2 = C(n,2)` is exactly the exponent of
the corpus's own Lean-proved `QOU.MathlibExt.QBorelKernel.qBorelKernel`. So the
level-1 q-Borel transform of `Z_n` is not a new object — it IS `S^bal`. Stripping
it leaves `d2 log S^bal` RISING 0.0642 -> 0.0819 toward `ln q0`, **5.2x the
control**: `S^bal ~ q0^{n^2/2}`, still q-Gevrey.

Note where `q0^{n^2/2}` correctly belongs: it is the order of **`S^bal`**, the
kernel-STRIPPED object. This bean attached `S^bal`'s order to `Z_n`.

## What is now open (narrowed, NOT closed)

The resummation itself is still not done. What changed is that the target is
specified correctly:

- the divisor is `q0^{n^2}`, i.e. **two** level-1 kernels' worth, not one;
- so the open question is which q-Borel LEVEL applies — `qBorelExp d n` with the
  right `d`, or a level-1 kernel applied twice, or the ramified level-2 family
  that `QBorelKernelLevel.lean:24-27` already names as open;
- `B_D` is NOT reached here and nothing is wired. scope-(a).


## The missing object is SHARED with `qou-odh5` (2026-09-06)

The kernel this bean needs and the one `qou-odh5` is blocked on are the same object.

- **`qou-hok7` (here).** `Z_n ~ q0^{n^2}` needs exponent `n(n-1) = 2*C(n,2)` — twice
  the level-1 exponent. `qBorelExp d n ~ n^2/(2d)` is DECREASING in `d`, so no
  integer level in the corpus family supplies it; what is required is a **half
  level**. Lean: `QOU.MathlibExt.QBorelKernel.two_mul_qBorelExp_one` (sorry-free).
- **`qou-odh5`.** "C1 infinity: extract the two Stokes multipliers." Its own body
  records the lower hull at infinity as the single edge `(0,0) -> (2,-1)`,
  **slope −1/2**, and the open residue as the ramification square roots `B_1,B_2`.
- **`QBorelKernelLevel.lean:24-27`** already names the **ramified level-2 family**
  as the open item, for exactly the slope-1/2 case.

Three descriptions of one gap: a half level / slope −1/2 / the ramified level-2
family. **Constructing it once unblocks both beans.** That is a statement about
the work plan, not a new mathematical result — but it means these should not be
attacked as two separate tranches.

## `qou-odh5` is a STALLED CLAIM, not live work (measured 2026-09-06)

I reported it as "in-progress right now" earlier this session on the strength of
its `status:` field. Measured: its last commit `2ce063f238` is **2026-08-07,
30.6 days ago**, and it is **NOT on main** — the work never landed. Under the
AGENTS.md stalled-claim policy (>3h without a commit on the branch backing a live
in-progress bean) it is available for takeover, following the protocol: re-claim
with a body-append noting the takeover and the stale SHA, continue from that
branch's tip or from main, and never force-push over it.

Recording rather than taking it: reading a `status:` field as evidence of current
activity is the same error class as everything else this bean corrects — a label
quoted in place of a measurement.
