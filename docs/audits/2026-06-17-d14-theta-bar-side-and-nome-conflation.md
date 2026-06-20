# D14 modular-S-transform — theta lives on the bar side; E_q is not the modular torus

**Date:** 2026-06-17
**Branch:** `claude/bold-rubin-wahq2l`
**Scope:** Jacobi-triple-product / theta avenue for the modular S-transform
conjecture [`conj:modular-s-transform-q-q-tilde`](../../content/quantum-observable-universe/q-geometric-langlands/modular-s-transform-q-q-tilde.md)
(duality **D14**). Formalize-first probe + two structural findings + a
correction to the conjecture's stated premise.
**Probe:** [`computations/probes/d14_theta_bar_side_probe.py`](../../computations/probes/d14_theta_bar_side_probe.py)
→ witness [`d14-theta-bar-side.witness.json`](../../computations/probes/d14-theta-bar-side.witness.json)
**Lean invariant:** `theta_nome_norm_lt_one_iff` in
[`modular-s-transform-q-q-tilde.lean`](../../content/quantum-observable-universe/q-geometric-langlands/modular-s-transform-q-q-tilde.lean).

## Origin

The question "can we exploit a q-version of Euler's distinct = odd partition
identity?" leads, at the deep end, to the **Jacobi triple product**

$$
  \prod_{k\ge1}(1-q^{2k})(1+zq^{2k-1})(1+z^{-1}q^{2k-1})
  \;=\; \sum_{n\in\mathbb{Z}} z^n q^{n^2}
  \;=\; \vartheta(z\mid q),
$$

of which Euler's identity is the $\mathbb{Z}/2$ baby case. The product side is a
$\Phi_q = (x;q)_\infty$-type object (already in the framework, cheat-sheet §4);
the sum side is a Jacobi **theta** function — a section on the elliptic curve
$\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$, $q=e^{2\pi i\tau}$. The framework
already conjectures a modular $S$-transform $\tau\mapsto-1/\tau$ (D14), so the
JTP is the natural bridge: the classical theta functional equation
$\vartheta(-1/\tau)=\sqrt{-i\tau}\,\vartheta(\tau)$ *is* the D14 transform.
Before pursuing that, the formalize-first discipline (AGENTS.md §3.3) demands
the prunable invariants. Two fall out immediately, both $q_0$-robust.

## Finding A — theta converges only on the bar image $q_0^{-1}$

The theta series $\sum_n z^n q^{n^2}$ converges **iff** $|q|<1$ **iff**
$\operatorname{Im}\tau>0$ (upper half-plane $\mathbb{H}$). At the substrate:

| branch | nome | $\tau$ (from $q=e^{2\pi i\tau}$) | $\operatorname{Im}\tau$ | in $\mathbb{H}$? | theta converges? |
|---|---|---|---|---|---|
| $q_0$ | $1.10998$ | $-0.0166065\,i$ | $<0$ | **no** | **no** |
| $q_0^{-1}$ | $0.900917$ | $+0.0166065\,i$ | $>0$ | **yes** | **yes** |

Because the Hecke substrate $q_0\approx1.11>1$, the modular parameter
$\tau_0=\log q_0/(2\pi i)$ sits in the **lower** half-plane and theta diverges.
Only the **bar image** $q_0^{-1}<1$ — the $\mathrm{Li}_2^q$ / binding /
bar-even side of the $\Phi_q$(mass)/$\mathrm{Li}_2^q$(binding) split — lands in
$\mathbb{H}$. **A QOU theta object is intrinsically a binding-sector object.**

### Correction to the D14 conjecture (actionable)

The conjecture states "$\tau\in\mathbb{H}$" but defines $\tau$ directly from
$q_0$ (its "Connection to TQFT / Volume Conjecture" paragraph: "writing
$q_0=e^{2\pi i\tau_0}$ with $\tau_0$ small imaginary"). With $q_0>1$ real,
$\tau_0$ is in the *lower* half-plane, contradicting the $\mathbb{H}$ premise.
The fix is exactly Finding A: **D14 must use $q_0^{-1}$** (or equivalently
$\tau_0=+|\log q_0|/(2\pi)\,i$). The $S$-image is then
$-1/\tau_0\approx+60.2\,i$, large positive imaginary part → root-of-unity
($\tilde q\to0$) limit, as the conjecture intends. The narrative is corrected
in this PR.

## Finding B — the Descartes/color curve $\mathcal{E}_q$ is **not** the modular torus

The framework's named elliptic curve
[`prop:descartes-elliptic-curve`](../../content/quantum-observable-universe/predicted-spectra/elliptic-stability-locus.md),
$\mathcal{E}_q : y^2=x^3+0.7087x+0.8056$, has $j\approx129.86$ (paper: 129.9 ✓).
Inverting Klein-$j$ on the fundamental-domain arc gives period
$\tau_E\approx0.366+0.931\,i$ and period **nome** $\approx0.00289$. Compare:

| object | nome | location |
|---|---|---|
| Hecke modular torus (bar side) | $q_0^{-1}\approx0.901$ | near cusp $\tau\to0$ ($\tau\approx0.0166\,i$) |
| Descartes curve $\mathcal{E}_q$ | $\approx0.00289$ | deep in fund. domain ($\tau\approx i$) |
| **ratio** | **$\approx312\times$** | — |

For **any** curve with $0<j<1728$ the nome is in
$[\,e^{-2\pi},\,e^{-\pi\sqrt3}\,]\approx[0.0019,0.0043]$, so this is structural,
not a tuning artifact. **The modular $\tau$ of D14 and the period $\tau$ of
$\mathcal{E}_q/\mathcal{E}_z$ are different elliptic structures — do not
identify them.** This is the central trap for anyone pursuing the theta avenue.

## What survives for the payoff

The genuine, narrow payoff is intact: **the JTP gives D14 a concrete
realization via the classical theta functional equation**, provided the setup
is on the bar side $q_0^{-1}$ and kept distinct from $\mathcal{E}_q$. Mathlib's
`jacobiTheta` is *defined* on the upper half-plane $\mathbb{H}$ — exactly the
convergent (bar) side — and carries the functional equation realizing
$\tau\mapsto-1/\tau$. The remaining gap is the **assembly conjecture** (that the
framework's Hecke/$\Phi_q$ products assemble into a genuine theta section); that
stays conjectural and is what the D14 class axiomatises.

This does **not** compute a new observable on its own. The deeper avenue —
Poisson/theta resummation of the mass sum $\sum_\lambda y_\lambda\chi_\lambda$
as the $q_0\leftrightarrow$ root-of-unity bridge — is scoped separately in
[`docs/scope/2026-06-17-theta-poisson-mass-resummation-scope.md`](../scope/2026-06-17-theta-poisson-mass-resummation-scope.md).

## Cross-references

- D14 conjecture: [`conj:modular-s-transform-q-q-tilde`](../../content/quantum-observable-universe/q-geometric-langlands/modular-s-transform-q-q-tilde.md)
- $\Phi_q$ / $\mathrm{Li}_2^q$ bar-conjugate split: cheat-sheet §4
- Euler q-version origin: this session's prior turn (two q-exponentials
  $E_q,e_q$ inverse; JTP as the master identity)
- Bar even/odd ($\cosh$/$\sinh$) parity: [`docs/scope/2026-06-05-reeb-sinh-parity-c3-source-scope.md`](../scope/2026-06-05-reeb-sinh-parity-c3-source-scope.md)
